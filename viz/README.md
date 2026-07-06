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
