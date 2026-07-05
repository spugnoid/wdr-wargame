"""CSV-driven orchestration for infantry_calc: reads weapon and unit
roster data, runs the formulas, writes the precomputed reference table.

Source data (editable like a spreadsheet, no Python required to update):
  data/weapons.csv  -- one row per distinct weapon
  data/units.csv    -- one row per unit-variant/face

Run: PYTHONPATH=counters python3 -m infantry_calc.pipeline (from the repo root)
Output: counters/infantry_calc/infantry_roster_output.csv
"""

from __future__ import annotations

import csv
import pathlib
from dataclasses import dataclass
from typing import Literal

from infantry_calc.formulas import (
    MIN_RFP,
    WeaponClass,
    fire_interval_hexes,
    unit_defence,
    unit_morale,
    weapon_rfp,
)
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
            face = r["face"]
            if face not in ("F", "R"):
                raise ValueError(
                    f"Unit {r['unit_id']!r}: face must be 'F' or 'R', got {face!r}"
                )
            rows.append(
                UnitRow(
                    unit_id=r["unit_id"],
                    nation=r["nation"],
                    unit_type=r["unit_type"],
                    year_bracket=r["year_bracket"],
                    face=face,  # type: ignore[arg-type]
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


# Fire-line notation prefix by weapon class -- source: infantry-counter-
# design spreadsheet, UNIT ROSTER sheet's BX/BY/BZ/CA column formulas.
_NOTATION_PREFIX: dict[WeaponClass, str] = {
    "lmg": "─● ",
    "hmg": "═● ",
    "smg": "≡ ",
    "at_rifle": "╌○ ",
    "rifle": "╌ ",
    "pistol": "╌ ",  # same as rifle -- pistols rarely rate their own notation
}

_FALLOFF = 1  # every pilot-roster row uses -1; not yet a computed value (see design spec open items)


def _resolve_practical_rpm(slot: UnitWeaponSlot, weapon: WeaponRow) -> float:
    return slot.practical_rpm_override if slot.practical_rpm_override is not None else weapon.practical_rpm


def _fire_line_notation(slot: UnitWeaponSlot, weapon: WeaponRow, quality: Quality) -> str:
    practical_rpm = _resolve_practical_rpm(slot, weapon)
    rfp = weapon_rfp(slot.count, practical_rpm, weapon.weapon_class, quality)
    if rfp < MIN_RFP:
        return "omit (rFP too low)"
    interval = fire_interval_hexes(weapon.max_range_yds, rfp)
    return f"{_NOTATION_PREFIX[weapon.weapon_class]}{rfp} ⬡{interval} -{_FALLOFF}"


def write_infantry_roster_csv(
    weapons: list[WeaponRow],
    units: list[UnitRow],
    out_path: pathlib.Path,
) -> None:
    """The infantry roster reference table: per unit-face, up to three
    fire-line notations plus Defence, Morale, and M#/F#/G# -- the exact
    values printed on the physical counter. No arithmetic required at
    the table: read the row for this unit, done.
    """
    weapons_by_name = {w.name: w for w in weapons}

    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "unit_id", "nation", "unit_type", "year_bracket", "face", "quality",
                "fire_line_1", "fire_line_2", "fire_line_3",
                "defence", "morale", "m_number", "f_number", "g_number",
                "verify_status",
            ]
        )
        for unit in units:
            front_def, rear_def = unit_defence(unit.manpower_full, unit.quality)
            defence = front_def if unit.face == "F" else rear_def
            morale = unit_morale(unit.quality)

            fire_lines = [
                _fire_line_notation(slot, weapons_by_name[slot.weapon_name], unit.quality)
                for slot in unit.loadout
            ]
            fire_lines += [""] * (3 - len(fire_lines))

            writer.writerow(
                [
                    unit.unit_id, unit.nation, unit.unit_type, unit.year_bracket, unit.face, unit.quality,
                    fire_lines[0], fire_lines[1], fire_lines[2],
                    defence, morale, unit.m_number, unit.f_number, unit.g_number,
                    unit.verify_status,
                ]
            )


def main() -> None:
    weapons = load_weapons()
    units = load_units()
    write_infantry_roster_csv(weapons, units, DATA_DIR.parent / "infantry_roster_output.csv")
    print(f"Wrote infantry_calc output to {DATA_DIR.parent}")


if __name__ == "__main__":
    main()
