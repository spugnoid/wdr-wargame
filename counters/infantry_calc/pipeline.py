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

from infantry_calc.formulas import WeaponClass

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
