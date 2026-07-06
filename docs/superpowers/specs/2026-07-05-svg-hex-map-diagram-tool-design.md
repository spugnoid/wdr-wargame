# SVG Hex-Map Diagram Tool — Design Spec

## Why this exists

Worked examples are genuinely sparse across the rulebook — only 7 `Example:`
callouts exist across all 22 sections, and none are illustrated. The
`maps/` directory has existed since the initial commit as a stub
(`README.md` describes it as "SVG hex map generator (planned, not yet
built)") but contains nothing but a `.gitkeep`. This spec builds that tool.

## Scope decomposition

This request bundles two independent projects: (1) a tool that renders a
hex-map scene (terrain, unit tokens, movement) to SVG, and (2) actually
writing illustrated examples for most of the rulebook's 22 sections. Only
(1) is in scope here. (2) is a large, ongoing content-authoring effort that
should be tackled section-by-section once this tool exists and has proven
itself on a real pilot example — not attempted in one pass.

## Decisions locked

- **Static, build-time generation** — not interactive/JS diagrams. A scene
  is described in a data file, a Python pipeline renders it to a static
  `.svg`, matching how `armor_calc`/`infantry_calc` already generate CSV
  output from `data/` files rather than computing anything live in the
  browser. No JavaScript; works in any browser, PDF export, or print.
- **YAML scene files + a separate render pipeline**, not a custom Sphinx
  directive. One `.yaml` file per example under `maps/data/`; a pipeline
  script (`python3 -m maps.pipeline`) renders each to `maps/svg_output/`;
  the RST references the generated file with a plain `.. image::`
  directive. Regeneration is a manual/CI step, exactly like the other two
  packages — not a live Sphinx-build hook.
- **Simplified schematic tokens, not counter-accurate reproductions.** A
  token is a small filled hex with a short label (e.g. "GREN"), colored by
  faction — enough to follow an example without reproducing the full
  printed-counter layout (fire lines, M#/F#/G#, etc.). This keeps the tool
  independent of the counter-design data/format entirely.
- **Hand-rolled hex coordinate math + stdlib `xml.etree.ElementTree`** for
  SVG output — no new dependency for *drawing*. `counters/requirements.txt`
  has stayed at exactly `numpy` and `pytest`, deliberately, matching how
  `armor_calc` hand-implements its own penetration physics rather than
  pulling in a wargaming library. Flat-top hex axial→pixel math is
  well-documented and small (roughly 40 lines); the shape vocabulary
  needed here (hexagons, circles, arrows, text) stays manageable in plain
  `ElementTree` without a dedicated SVG library. One new dependency is
  still required elsewhere: Python's stdlib has no YAML parser, so reading
  the scene files needs `PyYAML` — small, standard, and worth it for a
  human-editable scene format, but a real addition to `maps/requirements.txt`
  and worth being explicit about rather than folding it into "zero new
  dependencies," which would only be true for the drawing layer.
- **Reuse the exact olive/khaki/aged-paper palette** from
  `docs/source/_static/custom.css` — no separate diagram color scheme.
- **Pilot scope: one Section 7 (Movement) example.** The first version
  supports exactly what that example needs: hex grid + terrain fills + one
  token + one movement path with per-step cost labels. Facing arrows/arcs,
  fire lines, multiple simultaneous tokens, and status markers are
  explicitly deferred to later, smaller follow-on phases once this proves
  out — not built now on spec.

## Architecture

New `maps/` package at the repo root, sibling to `counters/`, following the
same docs-as-code pattern as `armor_calc`/`infantry_calc`:

```
maps/
  data/
    section7_movement_example1.yaml
  scene.py           # dataclasses: Hex, Token, MovementPath, Scene
  hexgrid.py         # flat-top axial (q,r) -> pixel (x,y) coordinate math
  renderer.py        # Scene -> SVG (xml.etree.ElementTree)
  pipeline.py        # reads data/*.yaml, renders each, writes svg_output/*.svg
  svg_output/
    section7_movement_example1.svg
  tests/
    test_hexgrid.py
    test_scene.py
    test_renderer.py
    test_pipeline.py
  README.md
  requirements.txt   # PyYAML>=6.0, pytest>=8.0
```

Each file has one responsibility: `scene.py` defines what a scene *is*
(pure data, no rendering logic); `hexgrid.py` only converts hex coordinates
to pixel coordinates (no drawing); `renderer.py` only draws a already-valid
`Scene` (no coordinate math of its own, no file I/O); `pipeline.py` is the
only place that touches the filesystem (reads YAML, writes SVG). This
mirrors the existing separation in `infantry_calc` (`formulas.py` vs.
`pipeline.py`).

## Scene data model

One YAML file per example. Example (the Phase 1 pilot):

```yaml
title: "Movement Example: Crossing Open Ground into Light Woods"
hexes:
  - {q: 0, r: 0, terrain: open}
  - {q: 1, r: 0, terrain: open}
  - {q: 2, r: 0, terrain: light_woods}
tokens:
  - {id: squad1, label: "GREN", faction: german, q: 0, r: 0}
movement:
  - token: squad1
    path: [{q: 0, r: 0}, {q: 1, r: 0}, {q: 2, r: 0}]
    cost_labels: ["1", "2"]
```

- `hexes`: every hex in the scene, with an axial `(q, r)` coordinate and a
  `terrain` key. Terrain keys match Appendix B's existing categories (open,
  crops, wall/fence, hedgerow, light_woods, ditch/sunken_road, dense_woods,
  building_light, reverse_slope, rubble, building_heavy, entrenchment,
  fortification/bunker) — the exact enum and its color mapping is a plan-
  level detail, but every value must trace to an existing Appendix B row;
  this tool does not invent new terrain categories.
- `tokens`: unit markers. `id` is a stable reference used by `movement`
  entries; `label` is the short text drawn on the token; `faction`
  selects its fill color; `q`/`r` is its starting position.
- `movement`: optional. Each entry names a token (by `id`) and an ordered
  list of hexes it moves through, plus optional per-step cost labels drawn
  along the path.

## Rendering & visual style

Flat-top hexes, axial coordinate system. Palette pulled directly from the
existing CSS custom properties (`--paper`, `--paper-alt`, `--olive`,
`--olive-dark`, `--khaki`, `--khaki-light`, `--khaki-dark`, `--ink`,
`--ordnance-red`, `--cream`) — the same values, not re-derived. Grid lines
in khaki; terrain fills vary by type (open ground closer to paper/paper-alt,
wooded/built terrain in olive/khaki-dark tones); movement arrows in
ordnance-red for visibility; token fill colored by faction (proposed
default: olive-drab for German units, khaki-dark for Soviet — adjustable,
not load-bearing on the rest of the design).

## Sphinx integration

Generated `.svg` files are committed to the repo (same treatment as the
committed CSV outputs from `armor_calc`/`infantry_calc` — build products
that live in version control, not gitignored). Referenced from RST with a
plain `.. image:: /path/to/maps/svg_output/section7_movement_example1.svg`
and appropriate alt text. Regenerating after a scene-data edit is a manual
step: `PYTHONPATH=maps python3 -m maps.pipeline`, matching the exact
invocation style of the other two packages.

## Testing approach

- `test_hexgrid.py`: axial-to-pixel conversion checked against hand-computed
  coordinates for a handful of known `(q, r)` inputs.
- `test_scene.py`: YAML parses into the expected `Scene` dataclass; invalid
  terrain keys or dangling token references (a movement path naming a
  token `id` that doesn't exist) raise clear errors rather than silently
  producing a broken diagram.
- `test_renderer.py`: given a small, fully-specified `Scene`, the rendered
  SVG is parsed back with `ElementTree` and asserted against expected
  element counts/positions/colors — not a pixel-diff/snapshot test.
- `test_pipeline.py`: end-to-end, same shape as the existing pipeline tests
  in `armor_calc`/`infantry_calc` — run the pipeline against the real
  pilot YAML file and confirm the expected SVG file is produced.

## Out of scope

- Interactive/JS-driven diagrams (explicitly rejected — static SVG only).
- Counter-accurate token rendering (explicitly rejected — simplified
  schematic markers only, independent of the counter-design data/format).
- Facing arrows/arcs, fire lines, multiple simultaneous tokens or movement
  paths, status markers (SUPPRESSED/PINNED/etc.), and terrain-as-edge
  features (roads, rivers, walls between hexes rather than hex fills) — all
  deferred to later, smaller phases once the pilot proves the core
  primitives (grid, terrain fill, token, single movement path) work.
- Illustrating any section other than the one Phase 1 pilot example.
  "Write examples for most of the rulebook" is a separate, later project.
- A full terrain-type-to-color mapping covering every Appendix B category —
  the pilot only needs `open` and `light_woods`; the remaining mappings are
  a plan-level (or later-phase) detail, not required to prove the tool out.

## Validation approach

- The pilot example (Section 7, movement across open ground into light
  woods) is the acceptance test: if the pipeline produces a correct,
  legible SVG for it, matching the scene data, Phase 1 is done.
- No changes to any existing package (`armor_calc`, `infantry_calc`,
  `quality`) — this is a new, independent package. Existing test suites
  (140 passing) are unaffected and should be re-confirmed after this work
  lands, per this project's standing practice.
- Full Sphinx build (`-b html -W`) after the pilot `.. image::` reference
  is added to `section_7__movement.rst`, confirming the image resolves and
  the build stays warning-free.
