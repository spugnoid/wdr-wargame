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

Writes `roster_output.csv` (AV-vs-Capped per vehicle/profile/arc) and
`gun_curves_output.csv` (range-band PEN values per gun, matching the
counter ready-reckoner format) into this directory. Both are plain CSV —
open directly in Excel/Sheets to review or hand-edit inputs.

## Known gaps (see design spec §7 for the full list)

- AV-vs-Tungsten is not yet wired into the pipeline output (formulas exist
  in `formulas.py`, just not plumbed through `pipeline.py` yet).
- HEAT reference table not yet implemented.
- Flaw multiplier (Ch.6) not yet implemented — no vehicle in the roster has
  a flaw correction applied, though pre-Oct-1943 Sherman glacis QC issues
  are a known candidate.
- `av_override_mm` in vehicles.csv is a manual escape hatch for plates that
  don't reduce to "one thickness at one angle" (Tiger's mantlet, Sherman's
  M34A1 gun mount) — computed by hand from the extracted source data, not
  derived by this pipeline. If more vehicles get real thickness-map data,
  this should become a proper area-weighting function instead.
