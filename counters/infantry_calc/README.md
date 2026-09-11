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
  transcribed from the source spreadsheet), and historical notes. The original pilot
  data was the spreadsheet's 12-row roster (German Grenadier/Panzergrenadier/MG42-team,
  Soviet Guards-rifle/Rifle/DP-28-team, all 1943, front and rear faces), transcribed
  verbatim with its existing citations. **2026-09-11:** 8 rows added for US/UK/Japan
  (Rifle Squad or Section for each, plus a US Light Machine Gun Squad) sourced from
  `counters/toe/*_1943.md`, and two existing rows corrected against that same research
  — see design note E.110 and each corrected row's own `notes` column for what changed
  and why.
- `tests/` — regression tests cross-checked against the source spreadsheet's own
  computed values for the original 12 pilot roster rows (still locked in, since the
  MG42 LMG calibration anchor was never touched), plus the 8 new/corrected rows added
  2026-09-11, plus unit tests on every formula. Run before trusting any change.

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

## New weapon sourcing (2026-09-11)

The original 7 weapons' cyclic/practical RPM and max range came from the
infantry-counter-design spreadsheet with no per-row citation trail. The 9 added
2026-09-11 to support the US/UK/Japan additions are sourced directly (`weapons.csv`
itself has no source column, so it's recorded here instead):

- **Practical RPM** — the number the rFP formula actually uses — is a real,
  web-verified figure for every new weapon: M1 Garand 45 (trained-soldier
  semi-auto rate, commonly cited 40-50), M1903 Springfield 15 (bolt-action,
  matched to Kar98k's existing figure — same mechanical class), M1918A2 BAR 130
  (well-cited 120-150 sustained range), M1919A4 150 (well-cited "usable rate...
  sustainable ~15 min"), Bren 120 (well-cited "rapid rate... sustainable"),
  Lee-Enfield 15 (period-doctrine "expected" aimed rate), Sten 90 (matched to
  MP40 — same weapon class and comparable cyclic rate), Type 96/99 LMG 120
  (estimated by class parity with Bren/DP-28 — no specific practical-rate
  citation found, flagged as an estimate, not a direct citation), Arisaka Type
  38/99 12 (matched to Mosin-Nagant — same mechanical class).
- **Max range (yards)** follows the same class-parity approach used for the
  original 7 (bolt-action rifles ~500-600, SMGs 200, LMGs 600-900, tripod HMGs
  1500-2000): M1 Garand/M1903/Lee-Enfield/Arisaka 500-600, BAR 600 (a real,
  cited effective-range figure — genuinely shorter than a true LMG's, reflecting
  its lighter automatic-rifle design), M1919A4 1500 (well-cited), Bren 600 (a
  real cited aimed effective-range figure), Type 96/99 LMG 900 (estimated by
  class parity with DP-28, not independently cited), Sten 200 (matched to
  MP40/PPSh-41's existing printed range for game-internal consistency, though
  its real effective range is somewhat shorter).
- **Cyclic RPM** is not consulted by any formula (`weapon_rfp` takes only
  `practical_rpm`) — it's reference data only. Recorded from the same sources
  as practical RPM where available.

## Known gaps (see design spec §5 for the full list)

- **Scope: infantry squads and organic support teams only.** As of 2026-09-11
  this covers 10 unit types across 4 nations (German Grenadier/Panzergrenadier/
  MG42-team, Soviet Guards-rifle/Rifle/DP-28-team, US Rifle Squad/Light Machine
  Gun Squad, UK Rifle Section, Japan Rifle Squad), 1943 only. Flagged, not yet
  modeled: the German Panzergrenadier squad's real loadout per
  `counters/toe/germany_1943.md` (2 LMG + 1 Panzerschreck, not the 1 LMG
  currently in `units.csv`) and the Soviet "Pattern B" squad variant (2x DP-28)
  documented alongside the Pattern A squad already modeled. Scaling to
  additional nations/years beyond this is future work, using this same
  pipeline shape.
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
