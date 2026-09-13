"""Generates docs/source/appendix_g__consolidated_roster.rst from this
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
GUNNERY_CSV = REPO_ROOT / "counters" / "armor_calc" / "vehicle_fire_thresholds_output.csv"
SHATTER_CSV = REPO_ROOT / "counters" / "armor_calc" / "shatter_gap_reference_output.csv"
HIT_LOCATION_CSV = REPO_ROOT / "counters" / "armor_calc" / "hit_location_output.csv"
OUT_PATH = REPO_ROOT / "docs" / "source" / "appendix_g__consolidated_roster.rst"

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


GUNNERY_BANDS = ["100", "250", "500", "750", "1000", "1500", "2000", "2500"]
CREW_ORDER = ["elite", "veteran", "regular", "green", "militia"]


def _gunnery_cell(miss: str, hull: str) -> str:
    """Rule 18.1a.1a: no Miss Threshold means the band is an automatic miss;
    a Miss Threshold with no Hull Threshold means every hit strikes the Turret."""
    miss, hull = (miss or "").strip(), (hull or "").strip()
    if not miss:
        return "—"
    return f"{miss} / {hull}" if hull else f"{miss} / T"


def render_gunnery_tables(rows: list[dict[str, str]]) -> str:
    by_key: dict[tuple[str, str], dict[str, tuple[str, str]]] = {}
    for r in rows:
        key = (r["gun_id"], r["crew_quality"])
        by_key.setdefault(key, {})[r["range_m"]] = (r["miss_below"], r["hull_at_or_above"])
    lines = [
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: auto",
        "",
        "   * - **Gun**",
        "     - **Crew**",
    ] + [f"     - **{b}m**" for b in GUNNERY_BANDS]
    for gun in sorted({g for g, _ in by_key}):
        for crew in CREW_ORDER:
            if (gun, crew) not in by_key:
                continue
            bands = by_key[(gun, crew)]
            lines.append(f"   * - {gun}")
            lines.append(f"     - {crew}")
            for b in GUNNERY_BANDS:
                miss, hull = bands.get(b, ("", ""))
                lines.append(f"     - {_gunnery_cell(miss, hull)}")
    return "\n".join(lines)


def render_shatter_gap_table(rows: list[dict[str, str]]) -> str:
    lines = [
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: auto",
        "",
        "   * - **Target AV (mm)**",
        "     - **Shatter Window — lower PEN**",
        "     - **Shatter Window — upper PEN**",
    ]
    for r in rows:
        lines += [
            f"   * - {r['av_mm']}",
            f"     - {r['shatter_window_lower_mm']}",
            f"     - {r['shatter_window_upper_mm']}",
        ]
    return "\n".join(lines)


def render_hit_location_table(rows: list[dict[str, str]]) -> str:
    lines = [
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: auto",
        "",
        "   * - **Vehicle**",
        "     - **Profile**",
        "     - **Neither Threshold**",
        "     - **Mobility Threshold**",
    ]
    for r in rows:
        lines += [
            f"   * - {r['vehicle']}",
            f"     - {r['profile']}",
            f"     - {_cell(r['neither_below'])}",
            f"     - {_cell(r['mobility_at_or_above'])}",
        ]
    return "\n".join(lines)


PREAMBLE = """\
Appendix G — Consolidated Unit and Vehicle Roster
====================================================

*Every printed counter value in the game, collected in one place: infantry
and weapon teams in G.1, vehicle armour profiles in G.2, and gun penetration
curves by range in G.3.*

*Vehicle combat reference follows in G.4 to G.6: the Gunnery Tables behind
every gun's printed Miss and Hull Thresholds, the Shatter Gap windows, and
the Hit Location thresholds. A gun's thresholds are printed on its own
counter for that vehicle's Crew Quality (Rule 18.1a.1); G.4 reproduces
every quality so a scenario can field the same gun behind a better or
worse crew. Crew Quality is derived from the vehicle's printed Morale
(Rules 17.3.6, 18.1a.2), not chosen per scenario.*

G.1  Infantry and Weapon Team Roster
----------------------------------------

{infantry_table}

G.2  Vehicle Armour Roster
-------------------------------

{vehicle_table}

G.3  Gun Penetration Curves
--------------------------------

*0°-equivalent millimetres by range band (Rule 17.3.1) — read the row for
the ammunition nature actually fired.*

{gun_table}

G.4  Vehicle Gunnery Tables
--------------------------------

*Miss and Hull Thresholds for the Gunnery Roll (Rule 18.1a), by gun, crew
quality and range band. Each cell reads* **miss / hull**\\ *: a roll below the
first number misses, a roll at or above the second strikes the Hull, and
anything between strikes the Turret.* **T** *in place of a Hull Threshold
means every hit at that range strikes the Turret;* **—** *means the band is
an automatic miss (Rule 18.1a.1a). These bands are the Gunnery Table's own
and are read independently of the PEN bands in G.3.*

{gunnery_table}

G.5  Shatter Gap Table
---------------------------

*Used only when the Shatter Gap optional module is in play (Rule 18.2a).
Look up the target's AV in the profile and arc being hit; if effective PEN
falls inside that row's window, inclusive, the shot is forced to a
Non-Penetrating Hit (Rule 18.2a.3). Applies to Capped, Uncapped AP and
Soviet APBC only, and only where the gun's calibre does not exceed the
target's AV (Rule 18.2a.1).*

{shatter_table}

G.6  Hit Location Thresholds
---------------------------------

*Used only by vehicles with a printed Hit Location Table, and only for
Front-arc hits (Rules 17.7.1, 18.6a). One pair of numbers per profile,
valid at every range and against every attacker. Roll below the Neither
Threshold for Neither (a Casualty downgrades to Pinned, Rule 18.6a.2), at
or above the Mobility Threshold for a MOB kill, and between the two for a
GUN kill. A profile with no Mobility Threshold can never produce a MOB
kill (Rule 17.7.2).*

{hit_location_table}
"""


def main() -> None:
    infantry_rows = _read_rows(INFANTRY_CSV)
    vehicle_rows = _read_rows(VEHICLE_ROSTER_CSV)
    gun_rows = _read_rows(GUN_CURVES_CSV)

    gunnery_rows = _read_rows(GUNNERY_CSV)
    shatter_rows = _read_rows(SHATTER_CSV)
    hit_location_rows = _read_rows(HIT_LOCATION_CSV)

    content = PREAMBLE.format(
        infantry_table=render_infantry_table(infantry_rows),
        vehicle_table=render_vehicle_armour_table(vehicle_rows),
        gun_table=render_gun_curves_table(gun_rows),
        gunnery_table=render_gunnery_tables(gunnery_rows),
        shatter_table=render_shatter_gap_table(shatter_rows),
        hit_location_table=render_hit_location_table(hit_location_rows),
    )
    OUT_PATH.write_text(content, encoding="utf-8")
    print(f"wrote {OUT_PATH} ({len(infantry_rows)} infantry rows, {len(vehicle_rows)} vehicle plate rows, "
          f"{len(gun_rows)} guns, {len(gunnery_rows)} gunnery rows, {len(shatter_rows)} shatter rows, "
          f"{len(hit_location_rows)} hit-location rows)")


if __name__ == "__main__":
    main()
