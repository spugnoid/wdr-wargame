"""Sphinx extension: give every numbered rule its own stable HTML anchor.

Every rule in this book is written as a paragraph whose text begins with a
bold rule number -- ``**6.3.3**  Some text...`` -- rendered by docutils as
``<p><strong>6.3.3</strong>  Some text...</p>``. This extension walks each
document's doctree after parsing, finds every such paragraph, and adds a
stable id (``rule-6-3-3``) to it so it can be linked to directly with a URL
fragment, both from other pages in this build and from client-side JS
(``_static/rule_links.js``) that turns "Rule 6.3.3" mentions into real
links and cross-page hover previews.

Nothing here changes rendered rule *text* -- only adds an invisible id
attribute to the paragraph. It intentionally does not touch appendix E's
design-note headings, glossary bold terms, or lettered close-assault-table
items like "(e)" -- the regex requires the entire bold span to be nothing
but a rule number.

Also emits ``_static/rule_index.json`` at build end: a flat map from every
rule number to the HTML page it lives on, e.g. ``{"6.3.3":
"section_6__actions_and_reactions.html", ...}``. The client-side JS fetches
this once per page load to resolve a rule mention to a URL before it can
turn it into a link.

Sphinx may read documents in parallel worker processes (``sphinx-build
-j``, which is what Read the Docs' hosted builder uses); each worker gets
its own copy of the environment, so data a doctree-read handler stashes
directly on ``app.env`` (as ``rule_locations`` is here) is invisible to the
main process unless explicitly merged back via the ``env-merge-info``
event -- without it, a parallel build silently produces an empty manifest
even though a plain sequential ``sphinx-build`` works fine.
``env-purge-doc`` similarly drops a document's stale
entries before an incremental rebuild re-reads it. See design note E.100.
"""

from __future__ import annotations

import json
import re

from docutils import nodes

RULE_ID_RE = re.compile(r"^\d+[a-z]?(?:\.\d+[a-z]?)*$")


def _anchor_id(rule_number: str) -> str:
    """'6.3.3' -> 'rule-6-3-3'; '18.1a.6' -> 'rule-18-1a-6'."""
    return "rule-" + rule_number.replace(".", "-")


def _leading_rule_number(paragraph: nodes.paragraph) -> str | None:
    """Return the rule number if this paragraph's first child is a bold
    span containing nothing but a rule number, else None."""
    if not paragraph.children:
        return None
    first = paragraph.children[0]
    if not isinstance(first, nodes.strong):
        return None
    text = first.astext().strip()
    if RULE_ID_RE.match(text):
        return text
    return None


def _collect_rule_ids(app, doctree):
    """doctree-read handler: tag every numbered-rule paragraph with a
    stable id, and record (rule number -> docname) for the manifest.

    Sphinx's doctree-read event only passes (app, doctree) -- the
    docname of the document currently being read is available via
    app.env.docname during this phase (the standard pattern for
    extensions that need it here rather than at doctree-resolved time).
    """
    docname = app.env.docname
    if not hasattr(app.env, "rule_locations"):
        app.env.rule_locations = {}

    for paragraph in doctree.findall(nodes.paragraph):
        rule_number = _leading_rule_number(paragraph)
        if rule_number is None:
            continue
        anchor = _anchor_id(rule_number)
        if anchor not in paragraph["ids"]:
            paragraph["ids"].append(anchor)
        # Last write wins if a rule number were ever reused across docs;
        # in practice every rule number in this book is unique.
        app.env.rule_locations[rule_number] = docname


def _purge_rule_locations(app, env, docname):
    """env-purge-doc handler: drop this document's previously recorded rule
    numbers before an incremental rebuild's doctree-read repopulates them --
    otherwise a rule renumbered or removed from an edited document leaves a
    stale entry in the manifest pointing at the wrong page."""
    locations = getattr(env, "rule_locations", None)
    if not locations:
        return
    for rule_number in [rn for rn, dn in locations.items() if dn == docname]:
        del locations[rule_number]


def _merge_rule_locations(app, env, docnames, other):
    """env-merge-info handler: a parallel read (sphinx-build -j) collects
    rule_locations in each worker's own environment copy; merge each
    worker's data back into the main environment after the read phase.
    Required for the manifest to come out complete under parallel builds --
    Read the Docs' hosted builder uses one, even though this repo's own
    sequential test build never exercised the gap."""
    if not hasattr(env, "rule_locations"):
        env.rule_locations = {}
    env.rule_locations.update(getattr(other, "rule_locations", {}))


def _write_manifest(app, exception):
    """build-finished handler: dump the accumulated manifest as JSON into
    the build's _static directory, docname -> html filename."""
    if exception is not None:
        return
    locations = getattr(app.env, "rule_locations", {})
    manifest = {
        rule_number: f"{docname}.html" for rule_number, docname in locations.items()
    }
    out_dir = app.outdir / "_static"
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "rule_index.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, sort_keys=True, indent=0, separators=(",", ":"))


def setup(app):
    app.connect("doctree-read", _collect_rule_ids)
    app.connect("env-purge-doc", _purge_rule_locations)
    app.connect("env-merge-info", _merge_rule_locations)
    app.connect("build-finished", _write_manifest)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
