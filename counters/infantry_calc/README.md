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
  this covers 11 unit types across 4 nations (German Grenadier/Panzergrenadier/
  MG42-team, Soviet Guards-rifle/Rifle Pattern A/Rifle Pattern B/DP-28-team, US
  Rifle Squad/Light Machine Gun Squad, UK Rifle Section, Japan Rifle Squad),
  1943 only. The German Panzergrenadier squad's loadout was corrected the same
  day per `counters/toe/germany_1943.md` (now 2 LMG + MP40 leader; the squad's
  organic Panzerschreck resolves through the existing flat-PEN infantry AT
  weapons table, Rule 18.9, not through this pipeline's rFP formula), and the
  Soviet "Pattern B" squad variant (2x DP-28) was added alongside the existing
  Pattern A squad — see design note E.116. Scaling to additional nations/years
  beyond this is future work, using this same pipeline shape.
- **Towed anti-tank guns are now partially in scope** (Rule 17.1a): the PaK 40
  (`counters/toe/pak40_1943.md`, both PzGr 39 APCBC and PzGr 40 APCR gun curves
  in `armor_calc/data/guns.csv`) was the first one built, and the British 6pdr
  (`counters/toe/sixpdr_1943.md`) the second — reusing `armor_calc`'s existing
  gun curve (`sixpdr_57l50_apcbc`, already in the roster from the earlier
  British-vehicles work, unlike PaK 40 which needed a fresh fit) and the same
  Rule 17.1a machinery — neither needs a vehicle counter at all, since a towed
  gun has no armour. Both guns now have a printed weapon-team stat block
  (`GER_PAK40_1943.3_F`, `UK_6PDR_1943.3_F` in `units.csv`, design note
  E.128) — a `units.csv` row with all three weapon slots left blank still
  computes Defence/Morale from `manpower_full`/`quality` via
  `unit_defence()`/`unit_morale()` correctly, since neither function
  actually depends on a weapon slot existing; the blank slots just mean no
  fire-line notation prints, which is correct since a towed gun's real
  attack (PEN/Gunnery Table, HE line) is computed elsewhere, not by this
  pipeline's RPM-based small-arms formula. Crew size is sourced for both (6
  men, matching independently); quality (`regular` for both) is an
  explicitly-hedged inference, not a sourced fact, per each row's own notes.
  Two things are deliberately left unmodelled rather than guessed at: G# (no
  formula exists anywhere in this project — see below — both rows use G1 by
  analogy to this roster's tripod HMG teams) and a reduced/rear face (Rule
  17.1a describes no degraded-crew mechanic for a towed gun, unlike
  HMG/mortar teams). Other towed guns (field howitzers, Soviet 45mm, US
  57mm) are still future work; see each existing gun's own research file
  for what's separately unsourced (PaK 40: divisional-vs-regimental 1943
  fielding date; 6pdr: named crew roles).
- **Grenades and satchel charges are not derived stats.** Both already resolve via
  fixed, manually-assigned values (G# on the counter, Engineer's DEMO capability);
  they are not something derived from real-world weapon specs.
- **Militia quality tier (BTV/EM/MM = 0.36/0.81/0.81) is a computed extrapolation,
  not sourced.** The source spreadsheet only defines Green/Regular/Veteran/Elite.
  Militia continues the same multiplicative step one tier further (Green→Militia
  mirrors Regular→Green). Now exercised by a real roster row (`UK_HOMEGUARD_1943.3_F`,
  the British Home Guard, design note E.131) — and the result is a real finding,
  not a clean validation: this multiplier is severe enough under `weapon_rfp()`'s
  log-compressed formula that a historically-sourced Home Guard squad (1 BAR + 7
  bolt-action rifles) prints **zero** fire lines — both round down below `MIN_RFP`
  and are omitted. A concentrated automatic weapon (a tripod HMG, or 3+ LMGs) still
  clears the floor at Militia, so this isn't a universal "Militia units can't fire"
  result, but it's a real, un-massaged consequence worth a designer's attention
  before fielding more Militia-tier units with rifle-heavy loadouts specifically.
