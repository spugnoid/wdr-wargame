"""Pure data-loading and filtering for the comparison dashboard.

No Streamlit imports here -- every function takes/returns pandas
DataFrames and is fully unit-testable on its own. See app.py and
views/*.py for the Streamlit-facing layer that calls these functions.

Reads directly from the already-committed CSV outputs of armor_calc and
infantry_calc -- no coupling to their internal Python code, just their
output files. If the data looks stale, regenerate it the existing way:
  PYTHONPATH=counters python3 -m armor_calc.pipeline
  PYTHONPATH=counters python3 -m infantry_calc.pipeline
"""

from __future__ import annotations

import pathlib

import pandas as pd

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
ARMOR_CALC_DIR = REPO_ROOT / "counters" / "armor_calc"
INFANTRY_CALC_DIR = REPO_ROOT / "counters" / "infantry_calc"

ROSTER_CSV = ARMOR_CALC_DIR / "roster_output.csv"
GUN_CURVES_CSV = ARMOR_CALC_DIR / "gun_curves_output.csv"
INFANTRY_ROSTER_CSV = INFANTRY_CALC_DIR / "infantry_roster_output.csv"

PEN_RANGE_COLUMNS = {
    "pen_0m": 0,
    "pen_250m": 250,
    "pen_500m": 500,
    "pen_750m": 750,
    "pen_1000m": 1000,
    "pen_1250m": 1250,
    "pen_1500m": 1500,
    "pen_1750m": 1750,
    "pen_2000m": 2000,
    "pen_2500m": 2500,
}

INFANTRY_NUMERIC_COLUMNS = ["defence", "morale", "m_number", "f_number", "g_number"]


def load_roster() -> pd.DataFrame:
    """Load the vehicle armor roster (one row per vehicle/profile/arc)."""
    return pd.read_csv(ROSTER_CSV)


def vehicle_names() -> list[str]:
    """Distinct vehicle names available for comparison, in file order."""
    return load_roster()["vehicle"].drop_duplicates().tolist()


def vehicle_armor_for(vehicles: list[str], av_column: str = "av_vs_capped_mm") -> pd.DataFrame:
    """Hull/Turret Front AV for the given vehicles, tidy for a grouped bar chart.

    Args:
        vehicles: vehicle names to include (must match the roster's
            `vehicle` column).
        av_column: which AV column to compare -- "av_vs_capped_mm",
            "av_vs_tungsten_mm", or "av_vs_heat_mm".

    Returns:
        DataFrame with columns [vehicle, profile, av_mm], one row per
        selected vehicle x {Hull, Turret}, filtered to arc == "Front".
    """
    roster = load_roster()
    filtered = roster[(roster["vehicle"].isin(vehicles)) & (roster["arc"] == "Front")]
    result = filtered[["vehicle", "profile", av_column]].rename(columns={av_column: "av_mm"})
    return result.reset_index(drop=True)


def load_gun_curves() -> pd.DataFrame:
    """Load the gun penetration curve roster (one row per gun)."""
    return pd.read_csv(GUN_CURVES_CSV)


def gun_ids() -> list[str]:
    """Distinct gun ids available for comparison, in file order."""
    return load_gun_curves()["gun_id"].tolist()


def gun_curve_long(guns: list[str]) -> pd.DataFrame:
    """Penetration-vs-range for the given guns, tidy for a line chart.

    Args:
        guns: gun_id values to include (must match gun_curves_output.csv's
            `gun_id` column).

    Returns:
        DataFrame with columns [gun_id, range_m, pen_mm], one row per
        selected gun x range band.
    """
    curves = load_gun_curves()
    filtered = curves[curves["gun_id"].isin(guns)]
    rows = []
    for _, row in filtered.iterrows():
        for column, range_m in PEN_RANGE_COLUMNS.items():
            rows.append({"gun_id": row["gun_id"], "range_m": range_m, "pen_mm": row[column]})
    return pd.DataFrame(rows, columns=["gun_id", "range_m", "pen_mm"])


def load_infantry_roster() -> pd.DataFrame:
    """Load the infantry/support-weapon unit roster (one row per unit)."""
    return pd.read_csv(INFANTRY_ROSTER_CSV)


def infantry_unit_ids() -> list[str]:
    """Distinct unit ids available for comparison, in file order."""
    return load_infantry_roster()["unit_id"].tolist()


def infantry_stats_for(units: list[str]) -> pd.DataFrame:
    """Numeric stat columns for the given units, tidy for a grouped bar chart.

    Args:
        units: unit_id values to include.

    Returns:
        DataFrame with columns [unit_id, stat, value], one row per
        selected unit x numeric stat column.
    """
    roster = load_infantry_roster()
    filtered = roster[roster["unit_id"].isin(units)]
    long = filtered.melt(
        id_vars=["unit_id"],
        value_vars=INFANTRY_NUMERIC_COLUMNS,
        var_name="stat",
        value_name="value",
    )
    return long.reset_index(drop=True)


def infantry_fire_lines_for(units: list[str]) -> pd.DataFrame:
    """Fire-line notation text for the given units, for display as a table.

    Args:
        units: unit_id values to include.

    Returns:
        DataFrame with columns [unit_id, fire_line_1, fire_line_2, fire_line_3].
    """
    roster = load_infantry_roster()
    filtered = roster[roster["unit_id"].isin(units)]
    columns = ["unit_id", "fire_line_1", "fire_line_2", "fire_line_3"]
    return filtered[columns].reset_index(drop=True)
