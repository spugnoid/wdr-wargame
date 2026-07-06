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
