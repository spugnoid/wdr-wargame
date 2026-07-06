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
