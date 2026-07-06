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


def test_load_scene_rejects_too_many_cost_labels_for_path_length():
    data = {
        "title": "Test Scene",
        "hexes": [
            {"q": 0, "r": 0, "terrain": "open"},
            {"q": 1, "r": 0, "terrain": "open"},
        ],
        "tokens": [{"id": "squad1", "label": "GREN", "faction": "german", "q": 0, "r": 0}],
        "movement": [
            {
                "token": "squad1",
                "path": [{"q": 0, "r": 0}, {"q": 1, "r": 0}],
                "cost_labels": ["1", "2", "3"],
            }
        ],
    }
    with pytest.raises(ValueError, match="segments to label"):
        load_scene(data)
