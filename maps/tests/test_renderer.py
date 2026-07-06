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
