# Hit Location and Crew Position System — Design Spec

## 1. Why this exists

The armored-combat penetration physics redesign (see the sister spec, `2026-07-04-armored-combat-penetration-physics-design.md`) explicitly deferred hit-location/crew-position/component-damage as "phase 2" from the start (§8 of that document). Today, when a shot produces a Casualty result (Rule 18.5/18.6), the owning player freely chooses whether it's a MOB kill or a GUN kill, justified narratively ("based on the most plausible damage given shot geometry" — Rule 17.1.1). This phase replaces that free choice with a real, sourced determination.

**Source material**: Bird & Livingston's Appendix 6 ("Theoretical Hit Probability Method") and Appendix 15 ("Shot Placement System") were flagged in the phase-1 spec as "already fully extracted." Direct verification this session found that claim was stale — neither had actually been transcribed anywhere. Both were read in full for the first time as part of this design pass.

**What each source appendix actually turned out to be** (a real finding, not an assumption carried over from the phase-1 spec):
- **Appendix 6** is pure shot-accuracy modelling (whether a shot hits at all) — trajectory-height equations, an aim-error formula, and a quartic polynomial approximating a normal-distribution CDF. It includes the *exact same* crew-quality max-hit-% table (Elite 90%/Veteran 85%/.../Militia 50%) already implemented this session via the Gunnery Roll (built from Appendix 17's real calibration data instead). Appendix 6 contributes nothing new — the Gunnery Roll already solves this problem, from better-calibrated data.
- **Appendix 15** is the real hit-location tool, but not in the form assumed. It is **not** a discrete "roll d6: 1-2 driver, 3-4 engine, 5-6 ammo" table. It's a **continuous 2D scatter model**: given an overall hit probability, dice rolls convert to a displacement in metres (vertical and lateral) from wherever the gunner aimed. The book's own worked example ("shots 0.2m up and 0.4m left of the turret ring hit the mantlet underside") determines *what* was hit by eyeballing a diagram — the book provides the scatter math but explicitly does not provide per-vehicle component-position diagrams. That overlay work does not exist yet for any vehicle in this project's roster, and is real, separate research.

## 2. Decisions locked this session

Reached through direct questions, not assumed:

- **Scope: full rigor.** Real Appendix 15 scatter math, plus real per-vehicle zone geometry (driver, gunner, loader, commander, engine, transmission, ammo, fuel, tracks as distinct positioned zones) — not an abstracted zone system and not a generic percentage table. Consistent with how every other addition this session was built (real formulas, cited sources, "zero lines" only at the point of play).
- **Mechanical scope: narrow.** Hit location's only job this phase is replacing the free MOB-kill/GUN-kill choice at the Casualty tier (Rule 18.5.1/18.6.1/18.7.1) with a real determination. It does **not** introduce new damage categories (no ammo cook-off tables, no crew-position-specific casualty effects) — that's explicitly a possible future phase, not this one.
- **New "Neither" outcome, and a real rules consequence.** Every possible scatter position must land in *some* zone — Mobility, Gun, or Neither (whatever coordinate space isn't claimed by the first two). A "Neither" result downgrades what would have been a Casualty to a **Pinned** result instead: the round penetrated, crew took a bad fright, but nothing essential was hit. This means some hits that currently always produce a player-chosen Casualty will, under this system, sometimes resolve to something less severe than before — a genuine change in outcomes, not just in how the outcome is decided.
- **Aim point: center-of-mass only, for this phase.** No declared-aim-point tactical option (e.g. "aim for the turret ring," a real historical tactic the source describes). Deferred as a possible future addition rather than doubling this phase's precomputation work (aimed vs. normal variants of every table).
- **Pilot vehicles: Tiger I and Sherman M4A1**, Front arc only. Mirrors how the phase-1 physics work itself started with one fully-rigorous vehicle (Tiger) before scaling to the roster. Sherman M4A1 specifically chosen as the **dry-stowage** variant — sponson-mounted ammunition, the historically infamous "Ronson" fire vulnerability — a strong test of whether this mechanic captures something historically real rather than just being mechanically elaborate. Side/Rear arcs and the other 11 roster vehicles are explicitly out of scope until the pilot proves out.
- **Implementation basis: the closed-form equations, not the raw dice table.** Appendix 15 gives both. The two-page percentile table is real but risks OCR/transcription error if hand-digitized; the equations are directly implementable and independently testable against the book's own worked examples.
- **Precomputation strategy: Monte Carlo, not analytic integration.** Sampling many (vertical roll, lateral roll, direction) triples and tallying which zone each lands in is robust to irregular zone shapes and straightforward to test for convergence, unlike solving integrals over arbitrary polygon geometry.

## 3. Architecture

### 3.1 Data flow

```
Casualty result occurs (Rule 18.5.1 or 18.6.1)
  -> look up Hit Location Table for (target vehicle, profile [Hull/Turret], arc [Front only, this phase], range band, attacker's crew quality)
  -> roll 1d6+1d8+1d12 (same combination used everywhere else) against the printed thresholds
  -> result: MOB kill / GUN kill / Neither (-> downgrades to Pinned, replacing the Casualty)
```

This slots directly into the existing Rule 18.7.1 hook ("owning player chooses which rear face applies") — the choice is replaced by a roll, nothing upstream (18.1-18.6's penetration determination) changes.

### 3.2 Zone geometry and coordinate system

Each pilot vehicle's Hull Front and Turret Front gets a set of positioned zones on a metre-scale (x, y) grid centred on that profile's aim point (center-of-mass), matching Appendix 15's own coordinate convention. Each zone is classified:

- **Mobility**: engine, transmission/final-drive, (tracks/drive sprockets are visible from Side arc only, out of scope this phase since only Front is modelled)
- **Gun**: turret ring, gun/breech, ammunition stowage within the profile
- **Neither**: crew positions with no adjacent critical system, and any unclaimed coordinate space

A real, historically-grounded example this geometry has to get right: Tiger (and most WW2-era German and American medium/heavy tanks) used a **front-mounted transmission** with the engine at the rear, connected by a driveshaft under the crew floor. This means Hull Front is not simply "crew, therefore Neither" — it genuinely contains a Mobility-critical component. A cruder model (front = crew/gun-adjacent only, rear = mobility only) would get this specific, well-documented case wrong.

### 3.3 Precomputation pipeline (per gun × range band × crew quality × target vehicle × profile)

1. Reuse the existing `hit_probability()` computation (already built for the Gunnery Roll — same number, not a new one).
2. Convert overall hit% to separate vertical/lateral hit% via Appendix 15's Table 1 (19-row lookup, digitized directly — same pattern as the HEAT reference table elsewhere in this project).
3. Monte Carlo sample many (vertical roll, lateral roll, direction) triples, convert each to an actual (dx, dy) via the closed-form displacement equations (validated against the book's own worked examples first), and tally which zone each lands in.
4. Collapse the tally into a Mobility/Gun/Neither percentage split, convert to a 1d6+1d8+1d12 die-roll threshold pair (reusing the same dice-CDF machinery already built for the Gunnery Roll's Miss/Hull thresholds).

### 3.4 Player-facing surface

A new small table per vehicle profile/arc, same shape as the existing Gunnery Table: range bands as rows, thresholds as columns. At the table: roll once (same dice already rolled for the Gunnery Roll and everything else), read the result directly. No new dice, no new lookup shape — the "zero lines" principle holds exactly as it has everywhere else this session.

**Implemented and tested** (`formulas.py`: `shot_displacement_m`, `vertical_lateral_hit_pct`, `HitZone`, `classify_hit_location`, `HitLocationThresholds`, `hit_location_thresholds`; `data/hit_zones.csv`: Front-arc zone geometry for both pilot vehicles; `pipeline.py`: `load_hit_zones`, `write_hit_location_reference_csv`, wired into `main()`), 19 new regression tests across `test_formulas.py` and `test_pipeline.py`, all passing (99 total). Rulebook updated: Rule 17.1.1 rewritten, new Rule 17.7 and Rule 18.6a added, Section 1.3 definitions extended, Appendix E.58 added. Verified with a real Sphinx build (`sphinx-build -b dummy -W`), zero warnings.

## 4. Validation approach

1. **Formula validation**: `formulas.py`'s displacement-equation implementation is validated against Appendix 15's one genuine equation-based worked example — 0.7m @ 85% hit / roll 66 (p.117-118). Two other figures the book gives (0.2m @ 95%/roll 22, 0.4m @ 95%/roll 50) were initially assumed to be additional equation worked examples but turned out, on direct primary-source verification, to come from the book's separate discrete percentile lookup table (introduced in the text as "an alternative to table use") applied to an unrelated scenario — not valid equation-reproduction tests. Corrected mid-implementation; see `formulas.py`'s `TestShotDisplacement` test class docstring for the full explanation.
2. **Monte Carlo convergence**: independent runs with different random seeds must produce stable zone-split percentages within a small tolerance — a regression test, not just a one-off check.
3. **Historical sanity check**: final precomputed tables should be spot-checked against basic historical expectation before being treated as final — e.g. Tiger's Rear arc (not built this phase, but worth stating as the eventual check) should show a much higher Mobility-zone probability than Front, given the rear-mounted engine; Sherman M4A1's Front arc should show a real, non-trivial Gun-zone (ammo) probability given its dry sponson stowage.

## 5. Out of scope this phase (explicit, not implied)

- Side and Rear arcs, for both pilot vehicles.
- The other 11 vehicles in the roster.
- Declared aim points as a tactical option (center-of-mass only, this phase).
- New damage categories beyond MOB/GUN/Neither-downgrades-to-Pinned (no ammo cook-off explosion tables, no individual crew-casualty-by-station effects).
- Appendix 6's own hit-probability method (superseded by the already-built Gunnery Roll; contributes nothing new).

## 6. Open items — flagged honestly, not resolved here

- **Zone geometry provenance.** Tiger and Sherman M4A1 zone coordinates will come from general historical/technical knowledge (well-documented vehicle dimensions and internal layouts), not from either project source — neither source provides interior layout diagrams. This is a real confidence gap, higher-stakes than similar external-knowledge flags used elsewhere this session (e.g. Panther's rear hull figures) because it drives an actual gameplay outcome (MOB vs. GUN kill), not just an AV number. Each zone's coordinates should be flagged with their own confidence level when the actual layout research is done, not assumed uniformly reliable.
- **Generalizing beyond Front arc.** The scatter math is a property of gun dispersion, not of which arc is being engaged, so applying the same equations to Side/Rear arcs later is a reasonable generalization — but it is a generalization beyond the book's own (frontal) worked example, and should be flagged as such when that expansion happens, not silently assumed.
- **Whether crew-quality-dependent scatter width is worth the table size.** This spec keeps full fidelity (range × crew quality, mirroring the Gunnery Table), since design-time table size isn't a "zero lines" violation — but if the per-crew-quality difference turns out to be a small, second-order effect once real numbers are computed, collapsing to a single "average crew" table may be worth reconsidering during implementation.
- **Whether the "Neither → downgrade to Pinned" rule is the right one**, versus, say, treating it as a full miss of the Casualty tier entirely and re-rolling one band down through Rule 18.5/18.6's own bands rather than landing specifically on Pinned. Chosen for simplicity; not stress-tested against edge cases (e.g. a vehicle already Suppressed when this triggers).
- **Scaling beyond the pilot.** This pass covers 2 of 13 roster vehicles and Front arc only. Expanding to the rest of the roster (and to Side/Rear arcs) means: (a) building real zone geometry for 11 more vehicles, general historical knowledge each time, not a quick copy-paste; (b) deciding whether the single-representative-attacker-gun simplification (Task 6) still holds once a genuinely diverse set of attacking guns is in play, or whether a full per-gun table becomes necessary; (c) re-checking whether Side/Rear arc geometry (tracks become visible, engine bay fully exposed from Rear) meaningfully changes the zone classifications rather than just repositioning them.

## 7. Pilot results — real numbers, not just a working mechanism

Computed values at 500m, Regular crew quality (illustrative — see `hit_location_output.csv` for the full table across all range bands and crew qualities):

| Vehicle | Profile | Mobility % | Gun % | Neither % |
|---|---|---|---|---|
| Tiger I Ausf E | Hull | 12.0 | 0.0 | 88.0 |
| Tiger I Ausf E | Turret | 0.0 | 21.8 | 78.2 |
| Sherman M4A1 (75mm) | Hull | 11.8 | 0.7 | 87.5 |
| Sherman M4A1 (75mm) | Turret | 0.0 | 17.8 | 82.2 |

Both vehicles' Turret profiles correctly show 0% Mobility — no vehicle's turret contains a mobility-critical component, and the classification pipeline reflects a real absence rather than defaulting to some nonzero placeholder (confirmed by `test_tiger_turret_never_produces_a_mobility_threshold`). Tiger's Hull profile shows a literal 0.0% Gun-classification chance: no gun/ammo zone exists in that profile's geometry at all. Sherman's Hull profile, by contrast, shows a real, non-zero Gun-classification chance (0.7% at this specific range/crew combination) driven directly by its sponson-mounted ammunition zones. While the quantitative gap at this range/crew is modest, the qualitative contrast is what validates the Sherman pilot choice: a genuine, present-but-modest, non-zero risk of hitting gun-critical components that simply does not exist in Tiger's hull geometry. This is the concrete result the Sherman pilot vehicle was chosen to test for.
