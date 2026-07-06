# maps

Design-time SVG hex-map diagram generator for With Deepest Regret's
worked examples. Nothing here runs at the table — it produces the
static `.svg` files embedded in the Rules of Play to illustrate
specific rules (movement, terrain, fire combat, etc.).

## Layout

- `scene.py` — the data model for a scene (hexes, tokens, a movement
  path). Pure data, no rendering or file I/O.
- `hexgrid.py` — flat-top axial `(q, r)` to pixel coordinate math.
- `renderer.py` — turns a `Scene` into an SVG element tree, using the
  same olive/khaki palette as the Read the Docs theme
  (`docs/source/_static/custom.css`).
- `pipeline.py` — reads every `data/*.yaml` scene file, renders it,
  writes the result to `svg_output/`.
- `data/*.yaml` — one hand-edited scene description per example. Add a
  new file here to add a new diagram; no Python required.
- `svg_output/*.svg` — generated output, committed to the repo (same
  treatment as `armor_calc`/`infantry_calc`'s committed CSV outputs).
- `tests/` — coordinate-math, scene-validation, rendering, and
  end-to-end pipeline tests.

## Usage

```
pip install -r maps/requirements.txt
python3 -m pytest maps/tests/
python3 -m maps.pipeline
```

Writes one `.svg` file per `data/*.yaml` scene into `svg_output/`.
Regenerate after editing a scene file or changing the renderer, then
commit the updated `.svg` alongside the source change.

## Scene file format

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

`terrain` values must have a matching entry in `renderer.py`'s
`TERRAIN_FILL` dict — as of this writing that's `open` and
`light_woods` only (the two the pilot example needs); add an entry
before authoring a scene that uses a different Appendix B terrain type.
Same for `faction` and `FACTION_FILL` (`german`, `soviet`).

## Scope

This is deliberately narrow: one token, one movement path, no facing
arrows/arcs, no fire lines, no status markers. See
`docs/superpowers/specs/2026-07-05-svg-hex-map-diagram-tool-design.md`
for what's intentionally out of scope and why.
