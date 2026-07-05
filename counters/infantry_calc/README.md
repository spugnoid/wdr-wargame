# infantry_calc

Design-time infantry/support-weapon counter calculator for With Deepest Regret's
infantry counter redesign. Nothing here runs at the table — it produces the
rFP/Defence/Morale/M#/F#/G# numbers that get printed on counters. See
`docs/superpowers/specs/2026-07-05-infantry-counter-system-design.md`
for the design this implements.

## Layout

- `formulas.py` — the infantry counter algorithm, cited to the project's own
  infantry-counter-design spreadsheet. These are calibrated game-design constants
  (not primary military documents, unlike `armor_calc`'s sourced physics), anchored
  to one worked example (German Grenadier 1943 squad's MG42 LMG → rFP 7).
  Read this first.
- `pipeline.py` — reads the CSVs below, runs the formulas, writes results.
- `data/weapons.csv` — one row per weapon: name, weapon class (rifle/lmg/hmg/smg/
  at_rifle/pistol), cyclic and practical rates of fire (RPM), max range (yards).
  Edit these like a spreadsheet to add a weapon — no Python required.
- `data/units.csv` — one row per unit-variant/face (front or rear). Columns:
  unit ID, nation, unit type (squad/team name), year bracket, face (F/R), quality
  tier (elite/veteran/regular/green/militia), manpower (full strength and reduced),
  weapon loadout (up to three weapons, each referenced by name from `weapons.csv`,
  with count and optional practical-RPM override), primary source citation,
  verify status (ANCHOR/PRELIMINARY/CROSS-CHECKED/PRIMARY-SOURCE — confidence tiers
  transcribed from the source spreadsheet), and historical notes. The pilot data is
  the spreadsheet's existing 12-row roster (German Grenadier/Panzergrenadier/MG42-team,
  Soviet Guards-rifle/Rifle/DP-28-team, all 1943, front and rear faces), transcribed
  verbatim with its existing citations.
- `tests/` — regression tests cross-checked against the source spreadsheet's own
  computed values for all 12 pilot roster rows, plus unit tests on every formula.
  Run before trusting any change.

## Usage

```
python3 -m pytest counters/infantry_calc/tests/
PYTHONPATH=counters python3 -m infantry_calc.pipeline
```

(run both from the repo root)

Writes `infantry_roster_output.csv` (one row per unit-face: fire-line notations,
Defence, Morale, M#/F#/G#, and verify status) into this directory. This is the
precomputed reference table — read the row for a unit-face, done; no arithmetic
required at the table. Plain CSV — open directly in Excel/Sheets to review or
hand-edit inputs.

## Known gaps (see design spec §5 for the full list)

- **Scope: infantry squads and organic support teams only.** This pilot covers
  6 unit types (German Grenadier/Panzergrenadier/MG42-team, Soviet Guards-rifle/
  Rifle/DP-28-team), 2 nations, 1943 only. Scaling to the full roster (other
  nations, other years) is future work, using this same pipeline shape.
- **Towed artillery is explicitly out of scope.** Support guns not mounted on a
  vehicle (PAK40, field howitzers, etc.) would reuse `armor_calc`'s gun-curve-fitting
  machinery — not built this phase.
- **Grenades and satchel charges are not derived stats.** Both already resolve via
  fixed, manually-assigned values (G# on the counter, Engineer's DEMO capability);
  they are not something derived from real-world weapon specs.
- **Militia quality tier (BTV/EM/MM = 0.36/0.81/0.81) is a computed extrapolation,
  not sourced.** The source spreadsheet only defines Green/Regular/Veteran/Elite.
  Militia continues the same multiplicative step one tier further (Green→Militia
  mirrors Regular→Green). Worth revisiting once a real Militia-tier unit
  (e.g. Volkssturm, opolcheniye) is added to the roster.
