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
