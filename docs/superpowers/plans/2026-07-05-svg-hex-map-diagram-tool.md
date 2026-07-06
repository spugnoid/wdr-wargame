# SVG Hex-Map Diagram Tool Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a `maps/` package that renders a hex-map scene (terrain, unit tokens, a movement path) to a static SVG file from a YAML description, proven on one real pilot example from Section 7 (Movement).

**Architecture:** A new top-level package, sibling to `counters/`, following the exact docs-as-code pattern already established by `armor_calc`/`infantry_calc`: YAML source data in `data/`, pure-data dataclasses, a rendering module, and a pipeline script that ties them together and writes output files. No JavaScript, no live Sphinx-build hook — regeneration is a manual pipeline run, same as the other two packages.

**Tech Stack:** Python 3, stdlib `xml.etree.ElementTree` for SVG generation, `PyYAML` for scene parsing, `pytest` for tests.

## Global Constraints

- No new dependency for drawing SVG — use stdlib `xml.etree.ElementTree` only, not a third-party SVG library. This plan only calls `ET.Element()`, `ET.SubElement()`, and `ET.tostring()` — building and serializing our own trusted, hand-constructed tree — and never `ET.fromstring()`/`ET.parse()`/`ET.iterparse()`. The XXE and billion-laughs vulnerabilities stdlib `ElementTree` is known for (and that `defusedxml` guards against) are exploits against *parsing* untrusted external XML; they don't apply to code that only builds and serializes its own output and never parses external XML input. The only external input parsed anywhere in this plan is YAML, via `yaml.safe_load()` (already the safe choice, not `yaml.load()`).
- `PyYAML` is required for parsing scene files (stdlib has no YAML parser) — add it to `maps/requirements.txt`.
- Tokens are simplified schematic markers (small hex + short label), never a reproduction of the actual printed counter layout.
- Reuse the exact color values already defined in `docs/source/_static/custom.css` — do not invent a separate palette.
- Flat-top hexes, axial `(q, r)` coordinates — matches this project's existing "flat-top hex grid" convention (Appendix E.54).
- Generated `.svg` files are committed to the repo (same treatment as the committed CSV outputs from `armor_calc`/`infantry_calc`), not gitignored.
- Phase 1 scope is exactly: hex grid + terrain fills + one token + one movement path with per-step cost labels. Do not add facing arrows/arcs, fire lines, multiple simultaneous tokens/paths, or status markers — those are explicitly out of scope for this plan.
- Every piece of code in this plan has already been written and run end-to-end in a scratch simulation before this plan was drafted (hex math, scene loading/validation, rendering, and pipeline orchestration all independently verified, including visually inspecting the rendered SVG in a browser and fixing one real bug found that way — an oversized arrowhead marker). The code below is the corrected, verified version.

---

### Task 1: Hex coordinate math

**Files:**
- Create: `maps/__init__.py` (empty)
- Create: `maps/hexgrid.py`
- Create: `maps/tests/__init__.py` (empty)
- Create: `maps/tests/conftest.py`
- Test: `maps/tests/test_hexgrid.py`

**Interfaces:**
- Produces: `Point` (a `NamedTuple` with `x: float`, `y: float`), `axial_to_pixel(q: int, r: int, size: float) -> Point`, `hex_corners(center: Point, size: float) -> list[Point]` — all later tasks import these from `maps.hexgrid`.

- [ ] **Step 1: Create the package `__init__.py` files**

```bash
mkdir -p /home/marvin/ClaudeCodeProjects/wdr_repo/maps/tests
touch /home/marvin/ClaudeCodeProjects/wdr_repo/maps/__init__.py
touch /home/marvin/ClaudeCodeProjects/wdr_repo/maps/tests/__init__.py
```

- [ ] **Step 2: Create the test-path conftest**

Create `maps/tests/conftest.py`:

```python
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
```

This mirrors the exact pattern used in `counters/infantry_calc/tests/conftest.py` — `parents[2]` from `maps/tests/conftest.py` resolves to the repo root (the parent of `maps/`), which is what makes `from maps.hexgrid import ...`-style imports resolve when pytest runs.

- [ ] **Step 3: Write the failing tests**

Create `maps/tests/test_hexgrid.py`:

```python
import math

from maps.hexgrid import Point, axial_to_pixel, hex_corners


def test_origin_hex_is_at_pixel_origin():
    assert axial_to_pixel(0, 0, 50) == Point(0.0, 0.0)


def test_q_neighbor_pixel_position():
    result = axial_to_pixel(1, 0, 50)
    assert result.x == 75.0
    assert math.isclose(result.y, 43.30127018922193)


def test_r_neighbor_pixel_position():
    result = axial_to_pixel(0, 1, 50)
    assert result.x == 0.0
    assert math.isclose(result.y, 86.60254037844386)


def test_hex_corners_returns_six_points():
    corners = hex_corners(Point(0, 0), 50)
    assert len(corners) == 6


def test_hex_corners_first_corner_position():
    corners = hex_corners(Point(0, 0), 50)
    assert math.isclose(corners[0].x, 50.0)
    assert math.isclose(corners[0].y, 0.0, abs_tol=1e-9)
```

- [ ] **Step 4: Run tests to verify they fail**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest maps/tests/test_hexgrid.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'maps.hexgrid'` (the module doesn't exist yet).

- [ ] **Step 5: Write the implementation**

Create `maps/hexgrid.py`:

```python
"""Flat-top hex grid coordinate math (axial coordinates).

Formulas from the standard flat-top axial hex grid reference (Red Blob
Games, https://www.redblobgames.com/grids/hexagons/). No drawing or file
I/O here -- see renderer.py and pipeline.py for those.
"""

from __future__ import annotations

import math
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


def axial_to_pixel(q: int, r: int, size: float) -> Point:
    """Convert flat-top axial hex coordinates to pixel coordinates.

    Args:
        q: Axial column coordinate.
        r: Axial row coordinate.
        size: Hex radius in pixels (center to vertex distance).

    Returns:
        Pixel-space center point of the hex.
    """
    x = size * (3 / 2 * q)
    y = size * (math.sqrt(3) / 2 * q + math.sqrt(3) * r)
    return Point(x, y)


def hex_corners(center: Point, size: float) -> list[Point]:
    """Return the 6 corner points of a flat-top hex centered at `center`.

    Args:
        center: Pixel-space center of the hex.
        size: Hex radius in pixels (center to vertex distance).

    Returns:
        List of 6 (x, y) corner points, in angle order starting at 0
        degrees (the rightmost vertex).
    """
    corners = []
    for i in range(6):
        angle_rad = math.pi / 180 * (60 * i)
        corners.append(
            Point(
                center.x + size * math.cos(angle_rad),
                center.y + size * math.sin(angle_rad),
            )
        )
    return corners
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest maps/tests/test_hexgrid.py -v`
Expected: `5 passed`

- [ ] **Step 7: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add maps/__init__.py maps/hexgrid.py maps/tests/__init__.py maps/tests/conftest.py maps/tests/test_hexgrid.py
git commit -m "feat: add flat-top hex axial coordinate math for maps/ package"
```

---

### Task 2: Scene data model

**Files:**
- Create: `maps/scene.py`
- Test: `maps/tests/test_scene.py`

**Interfaces:**
- Consumes: nothing from Task 1.
- Produces: `HexCell` (dataclass: `q: int`, `r: int`, `terrain: str`), `Token` (dataclass: `id: str`, `label: str`, `faction: str`, `q: int`, `r: int`), `MovementPath` (dataclass: `token: str`, `path: list[tuple[int, int]]`, `cost_labels: list[str]`), `Scene` (dataclass: `title: str`, `hexes: list[HexCell]`, `tokens: list[Token]`, `movement: list[MovementPath]`), `load_scene(data: dict) -> Scene` — all later tasks import these from `maps.scene`.

- [ ] **Step 1: Write the failing tests**

Create `maps/tests/test_scene.py`:

```python
import pytest

from maps.scene import HexCell, MovementPath, Token, load_scene


def test_load_scene_builds_expected_structure():
    data = {
        "title": "Test Scene",
        "hexes": [
            {"q": 0, "r": 0, "terrain": "open"},
            {"q": 1, "r": 0, "terrain": "light_woods"},
        ],
        "tokens": [
            {"id": "squad1", "label": "GREN", "faction": "german", "q": 0, "r": 0},
        ],
        "movement": [
            {
                "token": "squad1",
                "path": [{"q": 0, "r": 0}, {"q": 1, "r": 0}],
                "cost_labels": ["1"],
            }
        ],
    }
    scene = load_scene(data)
    assert scene.title == "Test Scene"
    assert scene.hexes == [
        HexCell(q=0, r=0, terrain="open"),
        HexCell(q=1, r=0, terrain="light_woods"),
    ]
    assert scene.tokens == [Token(id="squad1", label="GREN", faction="german", q=0, r=0)]
    assert scene.movement == [
        MovementPath(token="squad1", path=[(0, 0), (1, 0)], cost_labels=["1"])
    ]


def test_load_scene_rejects_movement_referencing_unknown_token():
    data = {
        "title": "Test Scene",
        "hexes": [{"q": 0, "r": 0, "terrain": "open"}],
        "tokens": [{"id": "squad1", "label": "GREN", "faction": "german", "q": 0, "r": 0}],
        "movement": [
            {"token": "does_not_exist", "path": [{"q": 0, "r": 0}], "cost_labels": []}
        ],
    }
    with pytest.raises(ValueError, match="unknown token id"):
        load_scene(data)


def test_load_scene_rejects_movement_referencing_hex_not_in_scene():
    data = {
        "title": "Test Scene",
        "hexes": [{"q": 0, "r": 0, "terrain": "open"}],
        "tokens": [{"id": "squad1", "label": "GREN", "faction": "german", "q": 0, "r": 0}],
        "movement": [
            {
                "token": "squad1",
                "path": [{"q": 0, "r": 0}, {"q": 5, "r": 5}],
                "cost_labels": ["1"],
            }
        ],
    }
    with pytest.raises(ValueError, match="not in the scene's hexes list"):
        load_scene(data)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest maps/tests/test_scene.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'maps.scene'`

- [ ] **Step 3: Write the implementation**

Create `maps/scene.py`:

```python
"""Data model for a hex-map example scene.

A Scene is pure data -- no rendering or coordinate-math logic lives here.
See renderer.py for drawing and hexgrid.py for coordinate conversion.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

TerrainType = Literal[
    "open",
    "crops",
    "wall_fence",
    "hedgerow",
    "light_woods",
    "ditch_sunken_road",
    "dense_woods",
    "building_light",
    "reverse_slope",
    "rubble",
    "building_heavy",
    "entrenchment",
    "fortification_bunker",
]

Faction = Literal["german", "soviet"]


@dataclass
class HexCell:
    q: int
    r: int
    terrain: TerrainType


@dataclass
class Token:
    id: str
    label: str
    faction: Faction
    q: int
    r: int


@dataclass
class MovementPath:
    token: str
    path: list[tuple[int, int]]
    cost_labels: list[str] = field(default_factory=list)


@dataclass
class Scene:
    title: str
    hexes: list[HexCell]
    tokens: list[Token]
    movement: list[MovementPath] = field(default_factory=list)


def load_scene(data: dict) -> Scene:
    """Build a Scene from a parsed YAML dict, validating references.

    Raises:
        ValueError: if a movement path references a token id that isn't
            among the scene's tokens, or a hex coordinate that isn't in
            the scene's hexes list.
    """
    hexes = [HexCell(q=h["q"], r=h["r"], terrain=h["terrain"]) for h in data["hexes"]]
    tokens = [
        Token(id=t["id"], label=t["label"], faction=t["faction"], q=t["q"], r=t["r"])
        for t in data["tokens"]
    ]
    token_ids = {t.id for t in tokens}
    hex_coords = {(h.q, h.r) for h in hexes}

    movement = []
    for m in data.get("movement", []):
        if m["token"] not in token_ids:
            raise ValueError(
                f"movement path references unknown token id {m['token']!r} "
                f"(known token ids: {sorted(token_ids)})"
            )
        path = [(p["q"], p["r"]) for p in m["path"]]
        for coord in path:
            if coord not in hex_coords:
                raise ValueError(
                    f"movement path for token {m['token']!r} references hex "
                    f"{coord} which is not in the scene's hexes list"
                )
        movement.append(
            MovementPath(
                token=m["token"],
                path=path,
                cost_labels=m.get("cost_labels", []),
            )
        )

    return Scene(
        title=data["title"],
        hexes=hexes,
        tokens=tokens,
        movement=movement,
    )
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest maps/tests/test_scene.py -v`
Expected: `3 passed`

- [ ] **Step 5: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add maps/scene.py maps/tests/test_scene.py
git commit -m "feat: add Scene data model with reference validation"
```

---

### Task 3: Renderer

**Files:**
- Create: `maps/renderer.py`
- Test: `maps/tests/test_renderer.py`

**Interfaces:**
- Consumes: `Point`, `axial_to_pixel`, `hex_corners` from `maps.hexgrid` (Task 1); `Scene` from `maps.scene` (Task 2).
- Produces: `SVG_NS` (str constant `"http://www.w3.org/2000/svg"`), `terrain_fill_color(terrain: str) -> str`, `faction_fill_color(faction: str) -> str`, `render_scene(scene: Scene, hex_size: float = 50.0) -> xml.etree.ElementTree.Element`, `render_to_string(scene: Scene, hex_size: float = 50.0) -> str` — later tasks import these from `maps.renderer`.

- [ ] **Step 1: Write the failing tests**

Create `maps/tests/test_renderer.py`:

```python
import pytest

from maps.renderer import faction_fill_color, render_scene, terrain_fill_color
from maps.scene import HexCell, MovementPath, Scene, Token


def _pilot_scene() -> Scene:
    return Scene(
        title="Test",
        hexes=[
            HexCell(q=0, r=0, terrain="open"),
            HexCell(q=1, r=0, terrain="open"),
            HexCell(q=2, r=0, terrain="light_woods"),
        ],
        tokens=[Token(id="squad1", label="GREN", faction="german", q=0, r=0)],
        movement=[
            MovementPath(
                token="squad1",
                path=[(0, 0), (1, 0), (2, 0)],
                cost_labels=["1", "2"],
            )
        ],
    )


def test_render_scene_draws_one_polygon_per_hex_plus_one_per_token():
    svg = render_scene(_pilot_scene())
    polygons = svg.findall("polygon")
    assert len(polygons) == 4  # 3 hex fills + 1 token marker


def test_render_scene_draws_one_path_per_movement_entry():
    svg = render_scene(_pilot_scene())
    paths = svg.findall("path")
    assert len(paths) == 1


def test_render_scene_draws_one_text_per_cost_label_plus_one_per_token():
    svg = render_scene(_pilot_scene())
    texts = svg.findall("text")
    assert len(texts) == 3  # 2 cost labels + 1 token label


def test_terrain_fill_color_known_type():
    assert terrain_fill_color("open") == "#f2eee1"


def test_terrain_fill_color_unknown_type_raises():
    with pytest.raises(ValueError, match="no fill color mapped for terrain type"):
        terrain_fill_color("swamp")


def test_faction_fill_color_known_faction():
    assert faction_fill_color("german") == "#333a16"


def test_faction_fill_color_unknown_faction_raises():
    with pytest.raises(ValueError, match="no fill color mapped for faction"):
        faction_fill_color("french")
```

Note: `svg.findall("polygon")` uses a **plain, non-namespaced** tag name. This matters: `render_scene()` returns an `Element` tree built directly via `ET.Element(...)`/`ET.SubElement(...)` calls with plain tag strings like `"polygon"` — `ElementTree` only applies `{namespace}tag` Clark-notation rewriting when *parsing* serialized XML text (e.g. via `ET.fromstring()`), not to trees built programmatically. Searching a hand-built tree with a namespaced tag (`f"{{{SVG_NS}}}polygon"`) silently returns zero matches. This was verified empirically before writing this plan — using the namespaced form here would make every one of these tests pass with an always-empty list, which `assert len(...) == 4` would still catch, but only by failing confusingly rather than for the right reason.

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest maps/tests/test_renderer.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'maps.renderer'`

- [ ] **Step 3: Write the implementation**

Create `maps/renderer.py`:

```python
"""Render a Scene to SVG using flat-top hex coordinates.

No file I/O and no YAML parsing here -- this module only turns an
already-valid Scene into an in-memory SVG element tree. See pipeline.py
for reading scene files and writing SVG files to disk.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET

from maps.hexgrid import Point, axial_to_pixel, hex_corners
from maps.scene import Scene

SVG_NS = "http://www.w3.org/2000/svg"

# Palette reused exactly from docs/source/_static/custom.css -- do not
# invent separate values here.
PAPER = "#f2eee1"
OLIVE_DARK = "#333a16"
KHAKI = "#8b7355"
KHAKI_DARK = "#6f5a3f"
INK = "#2b2b24"
ORDNANCE_RED = "#6b2c2c"
CREAM = "#fbf8f0"

HEX_SIZE = 50.0
MARGIN = 60.0

TERRAIN_FILL = {
    "open": PAPER,
    "light_woods": OLIVE_DARK,
}

FACTION_FILL = {
    "german": OLIVE_DARK,
    "soviet": KHAKI_DARK,
}


def terrain_fill_color(terrain: str) -> str:
    """Look up the fill color for a terrain type.

    Raises:
        ValueError: if `terrain` has no color mapping yet. Only the
            terrain types used by existing example scenes are mapped;
            add a new entry to TERRAIN_FILL before authoring a scene
            that uses a new terrain type.
    """
    try:
        return TERRAIN_FILL[terrain]
    except KeyError:
        raise ValueError(
            f"no fill color mapped for terrain type {terrain!r} -- "
            f"add an entry to TERRAIN_FILL in maps/renderer.py"
        ) from None


def faction_fill_color(faction: str) -> str:
    """Look up the fill color for a faction.

    Raises:
        ValueError: if `faction` has no color mapping yet.
    """
    try:
        return FACTION_FILL[faction]
    except KeyError:
        raise ValueError(
            f"no fill color mapped for faction {faction!r} -- "
            f"add an entry to FACTION_FILL in maps/renderer.py"
        ) from None


def _points_attr(points: list[Point]) -> str:
    return " ".join(f"{p.x:.2f},{p.y:.2f}" for p in points)


def render_scene(scene: Scene, hex_size: float = HEX_SIZE) -> ET.Element:
    """Render a Scene to an SVG element tree.

    Args:
        scene: The scene to render.
        hex_size: Hex radius in pixels (center to vertex distance).

    Returns:
        The root <svg> Element. Use ET.tostring() to serialize it, or
        render_to_string() for a ready-to-write document string.
    """
    centers = {(h.q, h.r): axial_to_pixel(h.q, h.r, hex_size) for h in scene.hexes}
    xs = [p.x for p in centers.values()]
    ys = [p.y for p in centers.values()]
    min_x, max_x = min(xs) - hex_size - MARGIN, max(xs) + hex_size + MARGIN
    min_y, max_y = min(ys) - hex_size - MARGIN, max(ys) + hex_size + MARGIN
    width, height = max_x - min_x, max_y - min_y

    svg = ET.Element(
        "svg",
        {
            "xmlns": SVG_NS,
            "viewBox": f"{min_x:.2f} {min_y:.2f} {width:.2f} {height:.2f}",
            "width": f"{width:.0f}",
            "height": f"{height:.0f}",
        },
    )

    defs = ET.SubElement(svg, "defs")
    marker = ET.SubElement(
        defs,
        "marker",
        {
            "id": "movement-arrowhead",
            # userSpaceOnUse: a fixed absolute size regardless of the
            # movement path's stroke-width. The default (markerUnits=
            # strokeWidth) scales the marker BY the stroke width, which
            # at stroke-width=4 blows the 10x10 marker up to 40x40px --
            # nearly the size of a hex. Confirmed by rendering the pilot
            # scene and inspecting the actual output before writing
            # this plan; this fixed version was re-verified the same way.
            "markerUnits": "userSpaceOnUse",
            "markerWidth": "16",
            "markerHeight": "16",
            "refX": "12",
            "refY": "8",
            "orient": "auto-start-reverse",
        },
    )
    ET.SubElement(marker, "path", {"d": "M0,0 L16,8 L0,16 Z", "fill": ORDNANCE_RED})

    ET.SubElement(
        svg,
        "rect",
        {
            "x": f"{min_x:.2f}",
            "y": f"{min_y:.2f}",
            "width": f"{width:.2f}",
            "height": f"{height:.2f}",
            "fill": PAPER,
        },
    )

    for h in scene.hexes:
        center = centers[(h.q, h.r)]
        corners = hex_corners(center, hex_size)
        ET.SubElement(
            svg,
            "polygon",
            {
                "points": _points_attr(corners),
                "fill": terrain_fill_color(h.terrain),
                "stroke": KHAKI,
                "stroke-width": "2",
            },
        )

    for m in scene.movement:
        path_points = [centers[(q, r)] for (q, r) in m.path]
        d = "M " + " L ".join(f"{p.x:.2f},{p.y:.2f}" for p in path_points)
        ET.SubElement(
            svg,
            "path",
            {
                "d": d,
                "fill": "none",
                "stroke": ORDNANCE_RED,
                "stroke-width": "4",
                "marker-end": "url(#movement-arrowhead)",
            },
        )
        for i, label in enumerate(m.cost_labels):
            a, b = path_points[i], path_points[i + 1]
            mid = Point((a.x + b.x) / 2, (a.y + b.y) / 2 - 10)
            text = ET.SubElement(
                svg,
                "text",
                {
                    "x": f"{mid.x:.2f}",
                    "y": f"{mid.y:.2f}",
                    "fill": INK,
                    "font-size": "16",
                    "text-anchor": "middle",
                },
            )
            text.text = label

    for t in scene.tokens:
        center = centers[(t.q, t.r)]
        corners = hex_corners(center, hex_size * 0.55)
        ET.SubElement(
            svg,
            "polygon",
            {
                "points": _points_attr(corners),
                "fill": faction_fill_color(t.faction),
                "stroke": CREAM,
                "stroke-width": "2",
            },
        )
        text = ET.SubElement(
            svg,
            "text",
            {
                "x": f"{center.x:.2f}",
                "y": f"{center.y + 5:.2f}",
                "fill": CREAM,
                "font-size": "14",
                "text-anchor": "middle",
            },
        )
        text.text = t.label

    return svg


def render_to_string(scene: Scene, hex_size: float = HEX_SIZE) -> str:
    """Render a Scene to a complete, ready-to-write SVG document string."""
    svg = render_scene(scene, hex_size)
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(svg, encoding="unicode")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest maps/tests/test_renderer.py -v`
Expected: `7 passed`

- [ ] **Step 5: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add maps/renderer.py maps/tests/test_renderer.py
git commit -m "feat: add Scene-to-SVG renderer with olive/khaki palette"
```

---

### Task 4: Pipeline, pilot data, and package docs

**Files:**
- Create: `maps/pipeline.py`
- Create: `maps/data/section7_movement_example1.yaml`
- Create: `maps/requirements.txt`
- Create: `maps/README.md`
- Test: `maps/tests/test_pipeline.py`

**Interfaces:**
- Consumes: `render_to_string` from `maps.renderer` (Task 3); `load_scene` from `maps.scene` (Task 2).
- Produces: `DATA_DIR` (`pathlib.Path`), `OUTPUT_DIR` (`pathlib.Path`), `render_all() -> list[pathlib.Path]`, `main()` — Task 5 (Sphinx integration) relies on `OUTPUT_DIR` containing `section7_movement_example1.svg` after this task runs.

- [ ] **Step 1: Write the failing tests**

Create `maps/tests/test_pipeline.py`:

```python
from maps.pipeline import DATA_DIR, OUTPUT_DIR, render_all


def test_render_all_writes_svg_for_pilot_scene():
    written = render_all()
    stems = {p.stem for p in written}
    assert "section7_movement_example1" in stems

    output_path = OUTPUT_DIR / "section7_movement_example1.svg"
    assert output_path.exists()
    content = output_path.read_text()
    assert content.startswith('<?xml version="1.0" encoding="UTF-8"?>')
    assert "<svg" in content
    assert "GREN" in content


def test_render_all_processes_every_yaml_file_in_data_dir():
    written = render_all()
    yaml_files = sorted(DATA_DIR.glob("*.yaml"))
    assert len(written) == len(yaml_files)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest maps/tests/test_pipeline.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'maps.pipeline'`

- [ ] **Step 3: Create the pilot scene data file**

Create `maps/data/section7_movement_example1.yaml`:

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

- [ ] **Step 4: Write the implementation**

Create `maps/pipeline.py`:

```python
"""YAML-driven orchestration for maps: reads scene description files,
renders each to SVG, writes output.

Source data (one YAML file per example scene):
  data/*.yaml

Run: python3 -m maps.pipeline (from the repo root -- maps/ needs no
PYTHONPATH entry, unlike counters/armor_calc or counters/infantry_calc
which need PYTHONPATH=counters. maps/ already sits directly under the
repo root, and Python's -m flag adds the current working directory to
sys.path, so the package is found without help. Verified empirically
before writing this plan.)
Output: maps/svg_output/*.svg (one per data/*.yaml file, same stem)
"""

from __future__ import annotations

import pathlib

import yaml

from maps.renderer import render_to_string
from maps.scene import load_scene

DATA_DIR = pathlib.Path(__file__).parent / "data"
OUTPUT_DIR = pathlib.Path(__file__).parent / "svg_output"


def render_all() -> list[pathlib.Path]:
    """Render every scene in DATA_DIR to an SVG file in OUTPUT_DIR.

    Returns:
        Paths of the SVG files written, in the order processed.
    """
    OUTPUT_DIR.mkdir(exist_ok=True)
    written = []
    for yaml_path in sorted(DATA_DIR.glob("*.yaml")):
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
        scene = load_scene(data)
        svg_text = render_to_string(scene)
        output_path = OUTPUT_DIR / f"{yaml_path.stem}.svg"
        output_path.write_text(svg_text)
        written.append(output_path)
    return written


def main() -> None:
    for path in render_all():
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest maps/tests/test_pipeline.py -v`
Expected: `2 passed`

- [ ] **Step 6: Create the requirements file**

Create `maps/requirements.txt`:

```
PyYAML>=6.0
pytest>=8.0
```

- [ ] **Step 7: Create the package README**

Create `maps/README.md`:

```markdown
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
```

- [ ] **Step 8: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add maps/pipeline.py maps/data/section7_movement_example1.yaml maps/requirements.txt maps/README.md maps/tests/test_pipeline.py
git commit -m "feat: add maps pipeline, pilot scene data, and package README"
```

---

### Task 5: Sphinx integration

**Files:**
- Modify: `docs/source/section_7__movement.rst`

**Interfaces:**
- Consumes: `maps/svg_output/section7_movement_example1.svg`, produced by Task 4's pipeline run.

- [ ] **Step 1: Confirm the SVG file exists**

Run: `ls -la /home/marvin/ClaudeCodeProjects/wdr_repo/maps/svg_output/section7_movement_example1.svg`
Expected: the file exists (written by Task 4's pipeline run and committed in that task's commit).

- [ ] **Step 2: Read Section 7's terrain-cost rule to place the diagram correctly**

Run: `grep -n "^7\.2\|Terrain Movement Costs" /home/marvin/ClaudeCodeProjects/wdr_repo/docs/source/section_7__movement.rst`

Find the `7.2  Terrain Movement Costs` heading and the rule text immediately following it (the rule that explains that moving into light woods costs more than open ground — this is the rule the pilot diagram illustrates). Insert the image directly after that rule's explanatory text, before the next numbered rule or heading.

- [ ] **Step 3: Insert the image reference**

Using the Edit tool, insert this block immediately after the Rule 7.2 text that explains terrain movement costs (read the file first to find the exact surrounding text — it varies depending on the current wording, so there is no fixed line number to give here):

```rst
.. figure:: /../../maps/svg_output/section7_movement_example1.svg
   :alt: A squad moves two hexes across open ground into light woods, spending 1 movement point to enter the first open hex and 2 to enter the light woods hex.
   :width: 500px

   A squad crossing open ground into light woods. Movement cost is
   labeled per hex entered.
```

- [ ] **Step 4: Verify the Sphinx build resolves the image and stays warning-free**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m sphinx -b html docs/source /tmp/maps_integration_check -W 2>&1 | tail -10`
Expected: ends with `build succeeded.` If the image path doesn't resolve, Sphinx will report a specific warning naming the missing file — adjust the `:figure:` path (relative to `docs/source/section_7__movement.rst`) until it resolves; do not change the actual file location established in Task 4.

- [ ] **Step 5: Visually confirm the rendered page**

Run:
```bash
cd /tmp/maps_integration_check && python3 -m http.server 8799 &
sleep 1
curl -sI http://localhost:8799/section_7__movement.html | head -1
```
Expected: `HTTP/1.0 200 OK`. Then open `http://localhost:8799/section_7__movement.html` in a browser (or take a screenshot via any available browser-automation tool) and visually confirm: the diagram appears in the right place in the rendered page, at a reasonable size, with the alt text and caption visible, and no broken-image icon. Stop the server afterward: `kill %1` (or find and kill the `http.server 8799` process).

- [ ] **Step 6: Run the full test suite as a sanity check**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/ maps/ -q`
Expected: all tests pass — the existing 140 from `counters/` plus the 17 new ones from `maps/` (`5` hexgrid + `3` scene + `7` renderer + `2` pipeline).

- [ ] **Step 7: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add docs/source/section_7__movement.rst
git commit -m "docs: illustrate Section 7 terrain movement costs with a hex-map diagram"
```

**This task's deliverable is independently testable:** the strict Sphinx build (Step 4) and the visual confirmation (Step 5) together confirm the diagram is correctly wired into the actual rulebook, not just that the `maps/` package works in isolation.

---

## Self-Review Notes

**Spec coverage:** every locked decision in the design spec maps to a task — static build-time generation (Task 4's pipeline), YAML scene files (Task 2/4), simplified schematic tokens (Task 3's `render_scene` token-drawing block, a small hex + label, no counter-layout fields), hand-rolled hex math + stdlib `ElementTree` (Tasks 1 and 3), reused olive/khaki palette (Task 3's color constants, copied from `custom.css`), and the one-example pilot scope (Task 4's single YAML file, Task 5's single `.. figure::` reference).

**Placeholder scan:** no TBDs — every step shows complete, already-verified code. Task 5's Steps 2-3 don't give a fixed line number for the RST insertion point because the plan was written before Task 4 exists to change that file's exact current line count; the step gives the exact search command and exact block to insert instead, which is unambiguous without needing a number that could drift.

**Type/interface consistency:** `Scene`, `HexCell`, `Token`, `MovementPath` field names and types are identical between Task 2's definition, Task 3's `render_scene()` usage, and Task 4's `load_scene()`/pipeline usage — confirmed by having actually run all four modules together end-to-end (all 17 tests passing, plus a real rendered SVG visually inspected in a browser) before this plan was written, not just by reading the code back.
