# Comparison/Charting Dashboard — Design Spec

## Why this exists

Running `armor_calc`'s and `infantry_calc`'s pipelines produces rich
comparable data — 13 vehicles' armor profiles, 9 guns' penetration curves,
12 infantry/support-weapon units' stats — but the only way to look at it
today is by opening CSV files directly. There's no way to visually compare
two vehicles' armor, overlay multiple guns' penetration curves, or see at a
glance where a gun's penetration curve crosses a target's armor value. This
spec builds a local interactive dashboard for exactly that kind of
exploration and comparison — a companion tool for designers/players, not
part of the published Rules of Play.

## Decisions locked

- **Local interactive dashboard**, not static charts or a standalone HTML
  report. Real interactivity — dropdowns/multi-selects that update charts
  live, hover tooltips, legend click-to-hide — matters more here than fitting
  the project's existing all-static docs-as-code pattern. This is a genuine,
  deliberate departure from that pattern for this one tool.
- **Streamlit** for the app shell (nav, selectors, layout), **Plotly** for
  charts (hover tooltips, legend interactivity, and a built-in "download as
  PNG" button on every chart for free). **pandas** for CSV loading/filtering.
  Three new dependencies, isolated entirely to `viz/requirements.txt` — they
  do not touch `counters/` or `maps/`'s dependency lists at all.
- **New top-level `viz/` package**, sibling to `counters/`, `docs/`, `maps/`.
  Not nested under `counters/`, since that directory has so far meant "pure
  calculation engine, no UI" (`armor_calc`, `infantry_calc`, `quality`) and
  blurring that line would muddy an otherwise clean boundary.
- **Reads directly from the already-committed CSV outputs** (`roster_output.csv`,
  `gun_curves_output.csv`, `infantry_roster_output.csv`,
  `vehicle_fire_thresholds_output.csv`) via pandas — no coupling to
  `armor_calc`/`infantry_calc`'s internal Python code, just their output
  files. If the data is stale, regenerate it the existing way
  (`PYTHONPATH=counters python3 -m armor_calc.pipeline` /
  `infantry_calc.pipeline`) — the dashboard does not invoke pipelines itself.
- **Four comparison views**, chosen from the full set of available data as
  the highest-value ones for a first version (see "Out of scope" for what
  was deliberately left out): vehicle armor comparison, gun penetration
  curves, gun-vs-vehicle matchup, infantry unit comparison.

## Architecture

```
viz/
  app.py              # Streamlit entry point; top-level nav between 4 views
  data.py             # loads + caches CSVs into pandas DataFrames (pure functions)
  views/
    vehicle_armor.py       # View 1
    gun_curves.py          # View 2
    gun_vs_vehicle.py      # View 3
    infantry_comparison.py # View 4
  tests/
    test_data.py      # pytest tests for the pure data-loading/filtering logic
  requirements.txt     # streamlit, plotly, pandas
  README.md
```

`data.py` owns all CSV reading, column parsing, and filtering — pure
functions taking/returning pandas DataFrames, no Streamlit imports, fully
unit-testable. Each `views/*.py` module owns exactly one comparison view's
Streamlit widgets (selectors) and Plotly chart construction, consuming
`data.py`'s functions — it does not read files itself. `app.py` only wires
navigation between views; it contains no data logic and no chart logic of
its own.

## The four views

**1. Vehicle armor comparison** — multi-select two or more vehicles (from
`roster_output.csv`'s `vehicle` column). Default chart: grouped bar chart
of Hull-Front and Turret-Front `av_vs_capped_mm` per selected vehicle,
matching the same headline number Section 19.7's rulebook table already
uses. A toggle switches the compared value to `av_vs_tungsten_mm` or
`av_vs_heat_mm` instead. Rows are filtered to `arc == "Front"` for both
`profile == "Hull"` and `profile == "Turret"`.

**2. Gun penetration curves** — multi-select two or more guns (from
`gun_curves_output.csv`'s `gun_id` column). Line chart, x-axis = range
(parsed from the `pen_0m`..`pen_2500m` column names into numeric metres),
y-axis = PEN in mm, one line per selected gun.

**3. Gun-vs-vehicle matchup** — select exactly one gun and one target
vehicle+arc. Plots that gun's penetration curve (as in View 2) together
with the target's AV value as a horizontal reference line at the same
y-scale, so the crossing point (if any) shows the max effective range
visually. Uses `av_vs_capped_mm` as the reference by default, with the
same manual toggle as View 1 to switch to `av_vs_tungsten_mm` or
`av_vs_heat_mm` instead. (Checked the actual data before writing this:
none of the current 9 guns in `gun_curves_output.csv` are tungsten/APDS
rounds — all 9 `gun_id`s end in `apcbc`, `apc`, or `apbc` — so there's no
real case yet where auto-inferring ammunition nature from the gun id would
even matter; a manual toggle is the right scope, not a missing feature.)

**4. Infantry unit comparison** — multi-select two or more units (from
`infantry_roster_output.csv`'s `unit_id` column). Grouped bar chart of the
five purely numeric columns: `defence`, `morale`, `m_number`, `f_number`,
`g_number`. The `fire_line_1`/`2`/`3` columns are compound notation strings
(weapon-class icon + rFP + `⬡h` interval + falloff, e.g. `─● 7 ⬡4 -1`), not
plain numbers — parsing them into chartable values is out of scope for v1
(see below); instead, display them as a small text table alongside the bar
chart so the information is still visible, just not charted.

## Testing approach

- `viz/tests/test_data.py`: pytest tests for every function in `data.py` —
  loading each CSV, filtering to the rows a given view needs (e.g. `arc ==
  "Front"`), and parsing the `pen_*m` column names into a tidy
  range/PEN-value table. These are pure functions with no Streamlit
  dependency, testable the same way as `armor_calc`/`infantry_calc`'s own
  test suites.
- A basic Streamlit smoke test (does `app.py` boot without throwing) using
  Streamlit's own `AppTest` framework is a nice-to-have, added during
  implementation if it turns out to be low-friction — not a hard requirement
  if it adds real friction, since this project has no prior experience with
  that framework to draw on.
- No tests attempt to verify exact pixel/visual chart output — only that the
  underlying data going into each chart is correct.

## Out of scope

- Hit-probability/gunnery curves (`hit_probability_output.csv`,
  `gunnery_reference_output.csv`), hit-location tables
  (`hit_location_output.csv`), shatter-gap and HEAT reference data
  (`shatter_gap_reference_output.csv`, `heat_reference_output.csv`) — real,
  comparable data, but not among the four views chosen for this version.
  A future pass could add more views following the same `views/*.py`
  pattern.
- Live pipeline regeneration from within the dashboard — the dashboard is
  read-only against whatever CSVs are currently on disk.
- Saved/exported comparisons beyond Plotly's built-in per-chart PNG download
  button (no server-side state, no "save this comparison" feature).
- Parsing infantry fire-line notation strings into chartable numeric values
  (shown as text instead, per View 4 above).
- Authentication, multi-user access, or any deployment beyond running
  locally with `streamlit run viz/app.py`.
- Any change to `counters/` or `maps/` — this is purely a new, read-only
  consumer of their already-committed output files.

## Validation approach

- `viz/tests/test_data.py` passing is the primary automated check.
- Manual verification during implementation: actually run `streamlit run
  viz/app.py`, exercise all four views with real data, and confirm the
  charts show sensible values (e.g. Tiger I's Hull Front AV bar matches
  the value already in `roster_output.csv`) — matching this project's
  established practice of visually inspecting generated output rather than
  trusting that code compiles and tests pass.
- No changes to `counters/`'s or `maps/`'s existing 158 tests — this is an
  independent new package; re-confirm they still pass as a sanity check
  after `viz/` is added, but no code in this spec touches them.
