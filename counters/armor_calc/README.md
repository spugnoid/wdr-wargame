# armor_calc

Design-time armor/penetration calculator for With Deepest Regret's armored
combat redesign. Nothing here runs at the table — it produces the AV/PEN
numbers that get printed on counters. See
`docs/superpowers/specs/2026-07-04-armored-combat-penetration-physics-design.md`
for the design this implements.

## Layout

- `formulas.py` — the physics, cited to source chapter/page. Read this first.
- `pipeline.py` — reads the CSVs below, runs the formulas, writes results.
- `data/guns.csv`, `data/gun_calibration.csv` — one gun+ammo per row, one
  attested penetration data point per row. Edit these like a spreadsheet to
  add/correct a gun — no Python required.
- `data/vehicles.csv` — one row per vehicle arc-profile plate (thickness,
  angle, cast/rolled, nation/era for hardness lookup, or a manual BHN/AV
  override for cases like Tiger's mantlet that don't reduce to a flat plate).
- `data/hardness_table.csv` — BHN by nation/armor-type/era/thickness bracket.
  Only Soviet armor has sourced entries as of this writing; German/American/
  British rows are absent on purpose (see design spec §7) because the
  source material didn't provide a systematic table for them, not because
  their armor is known to sit at baseline hardness — a lookup miss means
  "no correction applied," which is a stated assumption, not a verified fact.
- `tests/` — regression tests against the worked examples validated by hand
  this session (75mm/88mm gun curves, the T-34 high-hardness correction, the
  tungsten/APBC slope-multiplier findings). Run before trusting any change.

## Usage

```
python3 -m pytest counters/armor_calc/tests/
PYTHONPATH=counters python3 -m armor_calc.pipeline
```

Writes eight plain-CSV reference tables into this directory — open any of
them directly in Excel/Sheets to review, or hand-edit the inputs under
`data/`:

- `roster_output.csv` — AV per vehicle/profile/arc: vs-Capped, vs-Tungsten,
  and vs-HEAT columns (all three are printed counter values, Rule 17.2.3).
- `gun_curves_output.csv` — range-band PEN per gun, counter ready-reckoner
  format.
- `vehicle_fire_thresholds_output.csv` — the Gunnery Table thresholds
  (Rule 18.1a) per gun/crew-quality/range band.
- `hit_location_output.csv` — the per-profile Hit Location thresholds
  (Rule 18.6a; one row per vehicle/profile).
- `hit_probability_output.csv`, `gunnery_reference_output.csv`,
  `heat_reference_output.csv`, `shatter_gap_reference_output.csv` —
  supporting reference tables (hit%, HEAT multipliers, shatter windows).

## Known gaps (see design spec §7 for the full list)

- Flaw multiplier (Ch.6) is implemented and applied where sourced (Panther
  Ausf G hull front carries a medium-severity correction). A "pre-Oct-1943
  Sherman glacis QC issue" was researched as a candidate second application
  (`counters/toe/sherman_glacis_qc_1943.md`) and came back a partial non-
  finding: real US armor QC problems from this era exist, but none converges
  into a single, dateable, Sherman-glacis-specific defect comparable to
  Panther's sourced ~50%-of-production figure. See design note E.126 —
  not applied to either existing Sherman roster row on current sourcing.
- `av_override_mm` in vehicles.csv is a manual escape hatch for plates that
  don't reduce to "one thickness at one angle" (Tiger's mantlet, Sherman's
  M34A1 gun mount) — computed by hand from the extracted source data, not
  derived by this pipeline. If more vehicles get real thickness-map data,
  this should become a proper area-weighting function instead.
- British 6pdr/17pdr K-factors (`guns.csv`) are not independently sourced,
  unlike every other gun in this file — no published value was found, so
  each was instead derived by a constrained least-squares search against
  its own calibration data (see design note E.118). A lower-confidence
  methodology tier than the rest of the roster; flagged in each row's
  `confidence_note`, not hidden.
- Churchill/Cromwell armor data has two open sourcing conflicts, flagged in
  `vehicles.csv`'s own notes rather than silently resolved: Churchill's
  stepped-glacis middle/lower plate angles aren't sourced (Hull Front uses
  only the well-cited, fully-vertical top plate), and Cromwell's hull
  side/rear and turret front thicknesses vary across sources by several mm.
- Sherman Firefly (17pdr on a Sherman hull) is now modelled (`counters/toe/sherman_firefly_1944.md`)
  — the roster's first 1944-dated vehicle, deliberately not forced into the
  1943 baseline. Two things worth a scenario designer's attention: its
  turret-front mantlet AV is a documented stand-in (the existing M4A1
  mantlet override plus a sourced "+13mm" delta, not a fresh hit-distribution
  re-weighting for the Firefly's own mantlet shape), and Firefly-specific
  APDS availability timing is unresolved — a scenario set at the Normandy
  debut (June 1944) should treat it as APCBC-only.
