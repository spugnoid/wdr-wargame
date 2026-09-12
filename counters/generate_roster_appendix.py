"""Generates docs/source/appendix_h__consolidated_roster.rst from this
project's own already-generated CSV outputs (infantry_calc/infantry_roster_output.csv,
armor_calc/roster_output.csv, armor_calc/gun_curves_output.csv).

Run this after regenerating those CSVs (i.e. after running the infantry_calc
and armor_calc pipelines) to keep the consolidated appendix in sync with the
actual roster. This script only reads already-computed output -- it does not
run either pipeline itself and does not recompute any AV/PEN/rFP value.

Usage (from repo root):
    PYTHONPATH=counters python3 counters/generate_roster_appendix.py
"""

from __future__ import annotations

import csv
import pathlib

REPO_ROOT = pathlib.Path(__file__).parent.parent
INFANTRY_CSV = REPO_ROOT / "counters" / "infantry_calc" / "infantry_roster_output.csv"
VEHICLE_ROSTER_CSV = REPO_ROOT / "counters" / "armor_calc" / "roster_output.csv"
GUN_CURVES_CSV = REPO_ROOT / "counters" / "armor_calc" / "gun_curves_output.csv"
OUT_PATH = REPO_ROOT / "docs" / "source" / "appendix_h__consolidated_roster.rst"

RANGE_COLUMNS = ["pen_0m", "pen_250m", "pen_500m", "pen_750m", "pen_1000m", "pen_1250m", "pen_1500m", "pen_1750m", "pen_2000m", "pen_2500m"]


def _cell(value: str) -> str:
    """A blank CSV cell renders as an em-dash in the printed table rather
    than a confusing empty row -- RST list-table cells can't be truly empty
    without a stray blank bullet line."""
    value = (value or "").strip()
    return value if value else "—"


def _read_rows(path: pathlib.Path) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def render_infantry_table(rows: list[dict[str, str]]) -> str:
    lines = [
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: auto",
        "",
        "   * - **Unit**",
        "     - **Nation**",
        "     - **Year**",
        "     - **Quality**",
        "     - **Face**",
        "     - **Fire line 1**",
        "     - **Fire line 2**",
        "     - **Fire line 3**",
        "     - **Def**",
        "     - **Mor**",
        "     - **M#**",
        "     - **F#**",
        "     - **G#**",
    ]
    for r in rows:
        lines += [
            f"   * - {r['unit_type']}",
            f"     - {r['nation']}",
            f"     - {r['year_bracket']}",
            f"     - {r['quality']}",
            f"     - {r['face']}",
            f"     - {_cell(r['fire_line_1'])}",
            f"     - {_cell(r['fire_line_2'])}",
            f"     - {_cell(r['fire_line_3'])}",
            f"     - {r['defence']}",
            f"     - {r['morale']}",
            f"     - M{r['m_number']}",
            f"     - F{r['f_number']}",
            f"     - G{r['g_number']}",
        ]
    return "\n".join(lines)


def render_vehicle_armour_table(rows: list[dict[str, str]]) -> str:
    lines = [
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: auto",
        "",
        "   * - **Vehicle**",
        "     - **Profile**",
        "     - **Arc**",
        "     - **AV vs Capped**",
        "     - **AV vs Tungsten**",
        "     - **AV vs HEAT**",
        "     - **Schürzen**",
        "     - **Face-hardened**",
    ]
    for r in rows:
        lines += [
            f"   * - {r['vehicle']}",
            f"     - {r['profile']}",
            f"     - {r['arc']}",
            f"     - {r['av_vs_capped_mm']}",
            f"     - {r['av_vs_tungsten_mm']}",
            f"     - {r['av_vs_heat_mm']}",
            f"     - {'Yes' if r['schurzen'] == 'True' else '—'}",
            f"     - {'Yes' if r['face_hardened'] == 'True' else '—'}",
        ]
    return "\n".join(lines)


def render_gun_curves_table(rows: list[dict[str, str]]) -> str:
    header_ranges = ["0m", "250m", "500m", "750m", "1000m", "1250m", "1500m", "1750m", "2000m", "2500m"]
    lines = [
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: auto",
        "",
        "   * - **Gun**",
        "     - **Confidence**",
    ] + [f"     - **{r}**" for r in header_ranges]
    for r in rows:
        lines.append(f"   * - {r['gun_id']}")
        lines.append(f"     - {r['confidence']}")
        for col in RANGE_COLUMNS:
            lines.append(f"     - {_cell(r[col])}")
    return "\n".join(lines)


PREAMBLE = """\
Appendix H — Consolidated Unit and Vehicle Roster
====================================================

*This appendix is generated directly from this project's own calculation
tools, in* ``counters/infantry_calc/`` *and* ``counters/armor_calc/``\\ *, and
is never hand-edited. Regenerate it with the command* ``PYTHONPATH=counters
python3 counters/generate_roster_appendix.py`` *after re-running either
pipeline, and commit the regenerated file alongside whatever data change
produced it. Full sourcing, confidence notes, and open questions for any
given row live in the underlying* ``data`` *CSV files and the*
``counters/toe/`` *research documents they cite — this appendix intentionally
omits that detail to stay scannable as a single reference table.*

*Vehicle Gunnery Tables (Rule 18.1a) are not included here: a Gunnery Table
depends on the firing vehicle's own Crew Quality (Rule 17.3.6), which is
derived from a vehicle's printed Morale at counter-design time — a
scenario-specific choice this roster does not currently track as structured
data for every vehicle. A scenario's own parameter block states each side's
vehicle crew qualities; look up that gun's full Gunnery Table in the file*
``vehicle_fire_thresholds_output.csv`` *once the crew quality is chosen.*

H.1  Infantry and Weapon Team Roster
----------------------------------------

{infantry_table}

H.2  Vehicle Armour Roster
-------------------------------

{vehicle_table}

H.3  Gun Penetration Curves
--------------------------------

*0°-equivalent millimetres by range band (Rule 17.3.1) — read the row for
the ammunition nature actually fired.*

{gun_table}
"""


def main() -> None:
    infantry_rows = _read_rows(INFANTRY_CSV)
    vehicle_rows = _read_rows(VEHICLE_ROSTER_CSV)
    gun_rows = _read_rows(GUN_CURVES_CSV)

    content = PREAMBLE.format(
        infantry_table=render_infantry_table(infantry_rows),
        vehicle_table=render_vehicle_armour_table(vehicle_rows),
        gun_table=render_gun_curves_table(gun_rows),
    )
    OUT_PATH.write_text(content, encoding="utf-8")
    print(f"wrote {OUT_PATH} ({len(infantry_rows)} infantry rows, {len(vehicle_rows)} vehicle plate rows, {len(gun_rows)} guns)")


if __name__ == "__main__":
    main()
