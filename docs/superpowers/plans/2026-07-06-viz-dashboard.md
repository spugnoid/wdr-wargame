# Comparison/Charting Dashboard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local interactive Streamlit + Plotly dashboard (`viz/` package) with four comparison views over `armor_calc`'s and `infantry_calc`'s already-committed CSV outputs.

**Architecture:** A new top-level `viz/` package, sibling to `counters/`, `docs/`, `maps/`. A pure-data layer (`data.py`, no Streamlit imports, fully unit-testable) is consumed by four Streamlit view modules (`views/*.py`), wired together by a thin navigation shell (`app.py`). Reads directly from committed CSV files via pandas — no coupling to `armor_calc`/`infantry_calc`'s internal code.

**Tech Stack:** Python 3, pandas (data loading/filtering), Streamlit (app shell, widgets), Plotly (charts), pytest + Streamlit's `AppTest` framework (tests).

## Global Constraints

- Three new dependencies (`pandas`, `plotly`, `streamlit`), isolated entirely to `viz/requirements.txt` — do not add them to `counters/requirements.txt` or `maps/requirements.txt`, and do not touch either of those packages' code.
- `data.py` must have zero Streamlit imports — pure functions taking/returning pandas DataFrames, fully testable without a Streamlit runtime.
- Reads directly from these already-committed files (paths relative to the repo root): `counters/armor_calc/roster_output.csv`, `counters/armor_calc/gun_curves_output.csv`, `counters/infantry_calc/infantry_roster_output.csv`. Does not invoke any pipeline itself.
- No caching layer for v1 — the source CSVs are small (roster ~10KB, gun curves ~1KB, infantry roster ~1.5KB) and re-reading them on every Streamlit rerun is effectively free; adding `@st.cache_data` now would be premature optimization for data this size.
- Every piece of code in this plan was already written and run end-to-end before this plan was drafted: `data.py`'s functions were exercised against the real committed CSVs (not synthetic fixtures), all four views and `app.py` were verified booting via Streamlit's `AppTest` framework with zero exceptions, and the actual dashboard was launched with a real `streamlit run` and visually confirmed in a browser (including the Gun-vs-Vehicle Matchup view's crossing-lines chart, the one combining two data sources). The code below is the corrected, verified version.
- Use `width="stretch"` on `st.plotly_chart`/`st.dataframe` calls, not `use_container_width=True` — the latter is deprecated in the installed Streamlit version (1.53.0) and its stated removal date has already passed; this was caught by running the app for real during planning, not by reading Streamlit's changelog.
- Pyright will report type errors on several pandas method chains in `data.py` (e.g. `.rename()`, `.melt()` followed by `.reset_index()`) — this is a well-known pandas type-stub limitation, not a real bug. This is the first use of pandas in this codebase; do not add suppression comments or restructure the code to appease the type checker, since doing so would make the code less readable for a well-understood, ubiquitous ecosystem limitation.

---

### Task 1: Data layer

**Files:**
- Create: `viz/__init__.py` (empty)
- Create: `viz/data.py`
- Create: `viz/tests/__init__.py` (empty)
- Create: `viz/tests/conftest.py`
- Test: `viz/tests/test_data.py`

**Interfaces:**
- Produces: `REPO_ROOT`, `ARMOR_CALC_DIR`, `INFANTRY_CALC_DIR`, `ROSTER_CSV`, `GUN_CURVES_CSV`, `INFANTRY_ROSTER_CSV` (all `pathlib.Path`); `PEN_RANGE_COLUMNS: dict[str, int]`; `INFANTRY_NUMERIC_COLUMNS: list[str]`; `load_roster() -> pd.DataFrame`; `vehicle_names() -> list[str]`; `vehicle_armor_for(vehicles: list[str], av_column: str = "av_vs_capped_mm") -> pd.DataFrame`; `load_gun_curves() -> pd.DataFrame`; `gun_ids() -> list[str]`; `gun_curve_long(guns: list[str]) -> pd.DataFrame`; `load_infantry_roster() -> pd.DataFrame`; `infantry_unit_ids() -> list[str]`; `infantry_stats_for(units: list[str]) -> pd.DataFrame`; `infantry_fire_lines_for(units: list[str]) -> pd.DataFrame` — Task 2's views import all of these from `viz.data`.

- [ ] **Step 1: Create the package scaffolding**

```bash
mkdir -p /home/marvin/ClaudeCodeProjects/wdr_repo/viz/tests
touch /home/marvin/ClaudeCodeProjects/wdr_repo/viz/__init__.py
touch /home/marvin/ClaudeCodeProjects/wdr_repo/viz/tests/__init__.py
```

- [ ] **Step 2: Create the test-path conftest**

Create `viz/tests/conftest.py`:

```python
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
```

This mirrors the exact pattern used in `counters/infantry_calc/tests/conftest.py` and `maps/tests/conftest.py` — `parents[2]` from `viz/tests/conftest.py` resolves to the repo root (the parent of `viz/`), which is what makes `from viz.data import ...`-style imports resolve when pytest runs.

- [ ] **Step 3: Write the failing tests**

Create `viz/tests/test_data.py`:

```python
from viz import data


def test_vehicle_names_includes_known_vehicles():
    names = data.vehicle_names()
    assert "Tiger I Ausf E" in names
    assert "Panther Ausf G" in names
    assert len(names) == len(set(names))  # no duplicates


def test_vehicle_armor_for_returns_hull_and_turret_front_only():
    result = data.vehicle_armor_for(["Tiger I Ausf E"])
    assert list(result.columns) == ["vehicle", "profile", "av_mm"]
    assert set(result["profile"]) == {"Hull", "Turret"}
    assert len(result) == 2  # exactly one Hull row, one Turret row


def test_vehicle_armor_for_known_value():
    # Spot-check against a value already verified elsewhere in this
    # project (Section 19.7's vehicle counter table).
    result = data.vehicle_armor_for(["Tiger I Ausf E"])
    hull_row = result[result["profile"] == "Hull"].iloc[0]
    assert hull_row["av_mm"] == 102.0


def test_vehicle_armor_for_respects_av_column_choice():
    capped = data.vehicle_armor_for(["Tiger I Ausf E"], av_column="av_vs_capped_mm")
    tungsten = data.vehicle_armor_for(["Tiger I Ausf E"], av_column="av_vs_tungsten_mm")
    # Different columns should (at least for this vehicle) give different
    # numbers -- confirms the av_column argument actually changes the result.
    assert not capped["av_mm"].equals(tungsten["av_mm"])


def test_gun_ids_includes_known_guns():
    ids = data.gun_ids()
    assert "tiger_88_apcbc" in ids
    assert "pziv_75l48_apcbc" in ids


def test_gun_curve_long_covers_all_range_bands_for_each_gun():
    result = data.gun_curve_long(["tiger_88_apcbc", "pziv_75l48_apcbc"])
    assert list(result.columns) == ["gun_id", "range_m", "pen_mm"]
    assert len(result) == 2 * len(data.PEN_RANGE_COLUMNS)
    assert set(result["range_m"]) == set(data.PEN_RANGE_COLUMNS.values())


def test_gun_curve_long_only_includes_requested_guns():
    result = data.gun_curve_long(["tiger_88_apcbc"])
    assert set(result["gun_id"]) == {"tiger_88_apcbc"}


def test_infantry_unit_ids_includes_known_units():
    ids = data.infantry_unit_ids()
    assert "GER_GREN_1943.3_F" in ids
    assert "SOV_RIFSQ_1943.3_F" in ids


def test_infantry_stats_for_covers_all_numeric_columns_for_each_unit():
    result = data.infantry_stats_for(["GER_GREN_1943.3_F", "SOV_RIFSQ_1943.3_F"])
    assert list(result.columns) == ["unit_id", "stat", "value"]
    assert len(result) == 2 * len(data.INFANTRY_NUMERIC_COLUMNS)
    assert set(result["stat"]) == set(data.INFANTRY_NUMERIC_COLUMNS)


def test_infantry_fire_lines_for_returns_expected_columns():
    result = data.infantry_fire_lines_for(["GER_GREN_1943.3_F"])
    assert list(result.columns) == [
        "unit_id",
        "fire_line_1",
        "fire_line_2",
        "fire_line_3",
    ]
    assert len(result) == 1
```

- [ ] **Step 4: Run tests to verify they fail**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest viz/tests/test_data.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'viz.data'`

- [ ] **Step 5: Write the implementation**

Create `viz/data.py`:

```python
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
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest viz/tests/test_data.py -v`
Expected: `10 passed`

- [ ] **Step 7: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add viz/__init__.py viz/data.py viz/tests/__init__.py viz/tests/conftest.py viz/tests/test_data.py
git commit -m "feat: add viz data layer over armor_calc/infantry_calc CSVs"
```

---

### Task 2: Views, app shell, package docs

**Files:**
- Create: `viz/views/__init__.py` (empty)
- Create: `viz/views/vehicle_armor.py`
- Create: `viz/views/gun_curves.py`
- Create: `viz/views/gun_vs_vehicle.py`
- Create: `viz/views/infantry_comparison.py`
- Create: `viz/app.py`
- Create: `viz/requirements.txt`
- Create: `viz/README.md`
- Test: `viz/tests/test_app.py`

**Interfaces:**
- Consumes: every function and constant from `viz.data` produced in Task 1 (imported as `from viz import data`).
- Produces: `render()` (no args, returns `None`) in each of the four `views/*.py` modules — `app.py` imports and calls these by name; no other module depends on anything from this task.

- [ ] **Step 1: Create the requirements file**

Create `viz/requirements.txt`:

```
pandas>=2.0
plotly>=5.0
streamlit>=1.30
```

- [ ] **Step 2: Install dependencies**

```bash
pip install -r /home/marvin/ClaudeCodeProjects/wdr_repo/viz/requirements.txt
```

- [ ] **Step 3: Write the failing app-level test**

Create `viz/tests/test_app.py`:

```python
import pathlib

from streamlit.testing.v1 import AppTest

APP_PATH = str(pathlib.Path(__file__).resolve().parents[1] / "app.py")


def test_app_boots_without_exception():
    at = AppTest.from_file(APP_PATH)
    at.run(timeout=15)
    assert not at.exception


def test_every_view_renders_without_exception():
    at = AppTest.from_file(APP_PATH)
    at.run(timeout=15)
    view_names = at.sidebar.radio[0].options
    assert view_names == [
        "Vehicle Armor Comparison",
        "Gun Penetration Curves",
        "Gun vs. Vehicle Matchup",
        "Infantry Unit Comparison",
    ]
    for view_name in view_names:
        at.sidebar.radio[0].set_value(view_name).run(timeout=15)
        assert not at.exception, f"{view_name} raised: {at.exception}"
```

- [ ] **Step 4: Run the test to verify it fails**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest viz/tests/test_app.py -v`
Expected: FAIL — `FileNotFoundError` or `ModuleNotFoundError`, since `viz/app.py` and the view modules don't exist yet.

- [ ] **Step 5: Create the package init for views**

```bash
mkdir -p /home/marvin/ClaudeCodeProjects/wdr_repo/viz/views
touch /home/marvin/ClaudeCodeProjects/wdr_repo/viz/views/__init__.py
```

- [ ] **Step 6: Write the Vehicle Armor Comparison view**

Create `viz/views/vehicle_armor.py`:

```python
"""Vehicle armor comparison view."""

from __future__ import annotations

import plotly.express as px
import streamlit as st

from viz import data

AV_COLUMN_LABELS = {
    "av_vs_capped_mm": "vs. Capped",
    "av_vs_tungsten_mm": "vs. Tungsten",
    "av_vs_heat_mm": "vs. HEAT",
}


def render() -> None:
    st.header("Vehicle Armor Comparison")
    st.caption(
        "Hull-Front and Turret-Front armor value, from armor_calc's "
        "roster_output.csv."
    )

    all_vehicles = data.vehicle_names()
    vehicles = st.multiselect(
        "Vehicles to compare", options=all_vehicles, default=all_vehicles[:2]
    )
    av_label = st.radio(
        "Armor value", options=list(AV_COLUMN_LABELS.values()), horizontal=True
    )
    av_column = next(k for k, v in AV_COLUMN_LABELS.items() if v == av_label)

    if not vehicles:
        st.info("Select at least one vehicle to compare.")
        return

    chart_data = data.vehicle_armor_for(vehicles, av_column=av_column)
    fig = px.bar(
        chart_data,
        x="vehicle",
        y="av_mm",
        color="profile",
        barmode="group",
        labels={"av_mm": "AV (mm)", "vehicle": "Vehicle", "profile": "Profile"},
    )
    st.plotly_chart(fig, width="stretch")
```

- [ ] **Step 7: Write the Gun Penetration Curves view**

Create `viz/views/gun_curves.py`:

```python
"""Gun penetration curve comparison view."""

from __future__ import annotations

import plotly.express as px
import streamlit as st

from viz import data


def render() -> None:
    st.header("Gun Penetration Curves")
    st.caption("Penetration vs. range, from armor_calc's gun_curves_output.csv.")

    all_guns = data.gun_ids()
    guns = st.multiselect("Guns to compare", options=all_guns, default=all_guns[:2])

    if not guns:
        st.info("Select at least one gun to compare.")
        return

    chart_data = data.gun_curve_long(guns)
    fig = px.line(
        chart_data,
        x="range_m",
        y="pen_mm",
        color="gun_id",
        markers=True,
        labels={"range_m": "Range (m)", "pen_mm": "Penetration (mm)", "gun_id": "Gun"},
    )
    st.plotly_chart(fig, width="stretch")
```

- [ ] **Step 8: Write the Gun vs. Vehicle Matchup view**

Create `viz/views/gun_vs_vehicle.py`:

```python
"""Gun-vs-vehicle matchup view."""

from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

from viz import data

AV_COLUMN_LABELS = {
    "av_vs_capped_mm": "vs. Capped",
    "av_vs_tungsten_mm": "vs. Tungsten",
    "av_vs_heat_mm": "vs. HEAT",
}


def render() -> None:
    st.header("Gun vs. Vehicle Matchup")
    st.caption(
        "A gun's penetration curve against a target vehicle's armor value -- "
        "the crossing point (if any) is the max effective range."
    )

    gun = st.selectbox("Attacking gun", options=data.gun_ids())
    vehicle = st.selectbox("Target vehicle", options=data.vehicle_names())
    av_label = st.radio(
        "Target armor value", options=list(AV_COLUMN_LABELS.values()), horizontal=True
    )
    av_column = next(k for k, v in AV_COLUMN_LABELS.items() if v == av_label)

    if not gun or not vehicle:
        st.info("Select a gun and a target vehicle.")
        return

    curve = data.gun_curve_long([gun])
    armor = data.vehicle_armor_for([vehicle], av_column=av_column)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=curve["range_m"],
            y=curve["pen_mm"],
            mode="lines+markers",
            name=f"{gun} PEN",
        )
    )
    for _, row in armor.iterrows():
        fig.add_trace(
            go.Scatter(
                x=curve["range_m"],
                y=[row["av_mm"]] * len(curve),
                mode="lines",
                name=f"{vehicle} {row['profile']} AV",
                line={"dash": "dash"},
            )
        )
    fig.update_layout(xaxis_title="Range (m)", yaxis_title="mm")
    st.plotly_chart(fig, width="stretch")
```

- [ ] **Step 9: Write the Infantry Unit Comparison view**

Create `viz/views/infantry_comparison.py`:

```python
"""Infantry/support-weapon unit comparison view."""

from __future__ import annotations

import plotly.express as px
import streamlit as st

from viz import data


def render() -> None:
    st.header("Infantry Unit Comparison")
    st.caption(
        "Defence/Morale/M#/F#/G#, from infantry_calc's "
        "infantry_roster_output.csv. Fire lines are shown as text below "
        "since their notation isn't a plain number to chart."
    )

    all_units = data.infantry_unit_ids()
    units = st.multiselect("Units to compare", options=all_units, default=all_units[:2])

    if not units:
        st.info("Select at least one unit to compare.")
        return

    chart_data = data.infantry_stats_for(units)
    fig = px.bar(
        chart_data,
        x="stat",
        y="value",
        color="unit_id",
        barmode="group",
        labels={"stat": "Stat", "value": "Value", "unit_id": "Unit"},
    )
    st.plotly_chart(fig, width="stretch")

    st.subheader("Fire lines")
    st.dataframe(data.infantry_fire_lines_for(units), width="stretch")
```

- [ ] **Step 10: Write the app shell**

Create `viz/app.py`:

```python
"""Streamlit entry point for the comparison dashboard.

Run: streamlit run viz/app.py (from the repo root)

This module only wires navigation between views -- no data loading or
chart construction of its own. See data.py for the data layer and
views/*.py for each comparison view.
"""

from __future__ import annotations

import streamlit as st

from viz.views import gun_curves, gun_vs_vehicle, infantry_comparison, vehicle_armor

st.set_page_config(page_title="With Deepest Regret -- Data Comparison", layout="wide")

VIEWS = {
    "Vehicle Armor Comparison": vehicle_armor.render,
    "Gun Penetration Curves": gun_curves.render,
    "Gun vs. Vehicle Matchup": gun_vs_vehicle.render,
    "Infantry Unit Comparison": infantry_comparison.render,
}

st.sidebar.title("With Deepest Regret...")
st.sidebar.caption("Data comparison dashboard")
choice = st.sidebar.radio("View", options=list(VIEWS.keys()))

VIEWS[choice]()
```

- [ ] **Step 11: Run the app-level test to verify it passes**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest viz/tests/test_app.py -v`
Expected: `2 passed`

- [ ] **Step 12: Run the real app and visually confirm it**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m streamlit run viz/app.py --server.headless true --server.port 8765 &
sleep 4
curl -sI http://localhost:8765 | head -1
```

Expected: `HTTP/1.1 200 OK`. Then open `http://localhost:8765` in a browser (or use any available browser-automation tool) and confirm: the sidebar lists all 4 views, each view's chart renders with real data (e.g. Vehicle Armor Comparison's default two vehicles show a grouped bar chart; Gun vs. Vehicle Matchup shows a declining penetration line crossing one or two flat armor-value reference lines). Stop the server afterward:

```bash
pkill -f "streamlit run viz/app.py"
```

- [ ] **Step 13: Write the package README**

Create `viz/README.md`:

```markdown
# viz

Local interactive comparison dashboard for With Deepest Regret's calculated
vehicle and infantry data. Nothing here is part of the published Rules of
Play -- it's a companion tool for exploring and comparing the numbers
`armor_calc` and `infantry_calc` produce.

## Layout

- `data.py` -- loads and filters the CSV outputs into pandas DataFrames.
  Pure functions, no Streamlit dependency, fully unit-testable.
- `views/` -- one module per comparison view (vehicle armor, gun
  penetration curves, gun-vs-vehicle matchup, infantry units). Each has a
  single `render()` function that draws its Streamlit widgets and Plotly
  chart.
- `app.py` -- the Streamlit entry point. Only wires sidebar navigation
  between views; no data or chart logic of its own.
- `tests/` -- pytest tests for `data.py`'s pure functions, plus an
  app-level smoke test (via Streamlit's `AppTest` framework) confirming
  every view renders without error.

## Usage

```
pip install -r viz/requirements.txt
python3 -m pytest viz/tests/
streamlit run viz/app.py
```

Opens the dashboard in your browser (default `http://localhost:8501`).

If the data looks stale, regenerate it the usual way (this dashboard
never writes to these files, only reads them):

```
PYTHONPATH=counters python3 -m armor_calc.pipeline
PYTHONPATH=counters python3 -m infantry_calc.pipeline
```

## Views

1. **Vehicle Armor Comparison** -- pick 2+ vehicles, compare Hull-Front
   and Turret-Front armor value (toggle between vs. Capped / Tungsten /
   HEAT).
2. **Gun Penetration Curves** -- pick 2+ guns, overlay their
   penetration-vs-range curves.
3. **Gun vs. Vehicle Matchup** -- pick one gun and one target vehicle,
   see the gun's penetration curve plotted against the vehicle's armor
   value as a reference line -- the crossing point is the max effective
   range.
4. **Infantry Unit Comparison** -- pick 2+ infantry/support-weapon units,
   compare Defence/Morale/M#/F#/G#. Fire-line notation is shown as a text
   table below the chart, since it isn't a plain number to chart.

## Scope

Deliberately excludes hit-probability/gunnery curves, hit-location
tables, and shatter-gap/HEAT reference data -- real, comparable data, but
not among the four views built for this version. See
`docs/superpowers/specs/2026-07-06-viz-dashboard-design.md` for the full
list of what's out of scope and why.
```

- [ ] **Step 14: Run the full test suite as a final sanity check**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/ maps/ viz/ -q`
Expected: all tests pass — the existing 158 (140 `counters/` + 18 `maps/`) plus 12 new from `viz/` (10 `test_data.py` + 2 `test_app.py`) = `170 passed`.

- [ ] **Step 15: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add viz/views/__init__.py viz/views/vehicle_armor.py viz/views/gun_curves.py viz/views/gun_vs_vehicle.py viz/views/infantry_comparison.py viz/app.py viz/requirements.txt viz/README.md viz/tests/test_app.py
git commit -m "feat: add viz dashboard views and Streamlit app shell"
```

**This task's deliverable is independently testable:** the `AppTest`-based smoke test (Step 11) and the real `streamlit run` + visual confirmation (Step 12) together confirm the whole dashboard actually works end to end, not just that each module imports cleanly.

---

## Self-Review Notes

**Spec coverage:** every locked decision maps to a task — pandas/plotly/streamlit isolated to `viz/requirements.txt` (Task 2 Step 1), `data.py` with zero Streamlit imports (Task 1), reads directly from the three named CSVs (Task 1), no pipeline invocation (both tasks, never called), no caching (Global Constraints, explicitly not added), all four views built exactly as specified (Task 2 Steps 6-9), `AppTest` smoke test included since it proved low-friction during verification (Task 2 Step 3).

**Placeholder scan:** no TBDs — every step shows complete, already-verified code (all of it was actually run against real data and a real running server before this plan was written, not just drafted).

**Type/interface consistency:** every function name and signature in Task 2's views (`data.vehicle_names()`, `data.vehicle_armor_for(...)`, `data.gun_ids()`, `data.gun_curve_long(...)`, `data.infantry_unit_ids()`, `data.infantry_stats_for(...)`, `data.infantry_fire_lines_for(...)`) matches Task 1's definitions exactly — confirmed by having actually run all six modules together end-to-end (12 tests passing, a live `streamlit run` server serving real charts, screenshots visually inspected) before this plan was written, not just by reading the code back.
