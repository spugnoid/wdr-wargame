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
