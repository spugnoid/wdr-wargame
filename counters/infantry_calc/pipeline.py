"""CSV-driven orchestration for infantry_calc: reads weapon and unit
roster data, runs the formulas, writes the precomputed reference table.

Source data (editable like a spreadsheet, no Python required to update):
  data/weapons.csv  -- one row per distinct weapon
  data/units.csv    -- one row per unit-variant/face

Run: python3 -m counters.infantry_calc.pipeline
Output: counters/infantry_calc/infantry_roster_output.csv
"""

from __future__ import annotations

import csv
import pathlib
from dataclasses import dataclass
from typing import Literal

from infantry_calc.formulas import WeaponClass
from quality.tiers import Quality

DATA_DIR = pathlib.Path(__file__).parent / "data"


@dataclass(frozen=True)
class WeaponRow:
    name: str
    weapon_class: WeaponClass
    cyclic_rpm: float
    practical_rpm: float
    max_range_yds: float


def load_weapons(path: pathlib.Path = DATA_DIR / "weapons.csv") -> list[WeaponRow]:
    """Load weapon reference data (name, class, rates of fire, max range)."""
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append(
                WeaponRow(
                    name=r["name"],
                    weapon_class=r["weapon_class"],  # type: ignore[arg-type]
                    cyclic_rpm=float(r["cyclic_rpm"]),
                    practical_rpm=float(r["practical_rpm"]),
                    max_range_yds=float(r["max_range_yds"]),
                )
            )
    return rows


@dataclass(frozen=True)
class UnitWeaponSlot:
    weapon_name: str
    count: int
    practical_rpm_override: float | None


@dataclass(frozen=True)
class UnitRow:
    unit_id: str
    nation: str
    unit_type: str
    year_bracket: str
    face: Literal["F", "R"]
    quality: Quality
    manpower_full: int
    manpower_reduced: int
    loadout: list[UnitWeaponSlot]
    m_number: int
    f_number: int
    g_number: int
    source: str
    verify_status: str
    notes: str


def _parse_weapon_slot(r: dict[str, str], slot: int) -> UnitWeaponSlot | None:
    name = r[f"weapon{slot}_name"]
    if not name:
        return None
    override_raw = r[f"weapon{slot}_practical_rpm_override"]
    override = float(override_raw) if override_raw else None
    return UnitWeaponSlot(
        weapon_name=name,
        count=int(r[f"weapon{slot}_count"]),
        practical_rpm_override=override,
    )


def load_units(path: pathlib.Path = DATA_DIR / "units.csv") -> list[UnitRow]:
    """Load the infantry unit roster (one row per unit-variant/face).

    See that CSV's own notes/source columns for provenance -- most rows
    cite a primary or secondary historical document; rear-face rows that
    are purely derived from their front-face sibling say so explicitly.
    """
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            loadout = [
                slot
                for slot in (_parse_weapon_slot(r, n) for n in (1, 2, 3))
                if slot is not None
            ]
            rows.append(
                UnitRow(
                    unit_id=r["unit_id"],
                    nation=r["nation"],
                    unit_type=r["unit_type"],
                    year_bracket=r["year_bracket"],
                    face=r["face"],  # type: ignore[arg-type]
                    quality=r["quality"],  # type: ignore[arg-type]
                    manpower_full=int(r["manpower_full"]),
                    manpower_reduced=int(r["manpower_reduced"]),
                    loadout=loadout,
                    m_number=int(r["m_number"]),
                    f_number=int(r["f_number"]),
                    g_number=int(r["g_number"]),
                    source=r["source"],
                    verify_status=r["verify_status"],
                    notes=r["notes"],
                )
            )
    return rows
