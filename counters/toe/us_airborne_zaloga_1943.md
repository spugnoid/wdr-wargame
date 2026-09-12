# United States — Airborne (Parachute/Glider Infantry) Organization — Scope-Flagged Research

## Sources

- Steven J. Zaloga, *US Airborne Divisions in the ETO 1944-45* (Osprey Battle
  Orders 25), 100pp. Real OCR text layer, extracted in full via
  `pdftotext -layout` (confirmed real text, not an image scan; ~218,000
  characters). Cites primary War Department TO&Es directly (by number and
  date) and MHI/NARA archival holdings, plus named unit histories and a
  postwar General Board study.
- This is a documentation pass opening a brand-new research thread, exactly
  like `us_combat_engineer_1943.md` (E.147) — this project has **no
  Airborne/Paratrooper unit type, TOE, or roster row anywhere**, for any
  nation. A direct grep of `docs/source/*.rst` confirms "airborne" appears
  only twice in the whole project, both as a generic elite-quality exemplar
  in a parenthetical list (Section 15.5.2's Force Morale factor table and
  Section 22.3.3's scenario-difficulty table — "Elite (SS, Guards, Rangers,
  airborne)"), never as an actual structured unit.
- Cross-referenced against `counters/toe/united_states_1943.md` (the
  project's existing standard US rifle company TOE) for direct structural
  and weapons comparison, and against `counters/infantry_calc/data/units.csv`
  (`US_RIFSQ_1943.3_F`) for the existing sourced roster row it would sit
  beside if a future pass ever added one.

## Scope Verdict: This Book's Own Tables Are 1944(-45), Not 1943 — a Real Mismatch, Reported Honestly

This project's TOE convention (`counters/toe/README.md`) is "representative
1943" for all nations. This book's own title is explicit about its own
scope — "ETO 1944-45" — and that scope holds up under direct inspection,
not just in the title:

- **Every single printed organizational table in the book is dated 1942,
  February 1944, August 1944, or December 1944.** None is dated anywhere
  within 1943. The division table is explicitly captioned "Airborne
  division, TO&E 71, February 24, 1944," and the book states outright that
  this February 1944 table (not any 1943 edition) "is based on the February
  24, 1944, version that was in effect at the time of D-Day."
- The book does confirm that a real, dated **October 1943** revision
  happened to both the division table and the Parachute Infantry Regiment
  (PIR) table — "Two changes were instituted to this table in October 1943
  and February 1944" (division); "The first table of organization was
  authorized on February 17, 1942, and underwent three changes prior to
  D-Day: in July 1942, October 1943 and February 1944... for example
  deleting the M1903 Springfield .30-cal. sniper rifle, and adding the
  2.36in. bazooka" (PIR). So an Oct 1943-dated TO&E revision genuinely
  existed — but the book never reproduces it as its own standalone table;
  it only reproduces the cumulative Feb 24, 1944 state and describes the
  intervening changes in prose, without saying which specific figure
  changed at which specific one of the three revision dates.
- This is the same shape of gap `united_states_1943.md` already flagged for
  the *standard* infantry rifle company (bracketed only between a 1 Apr
  1942 and a 26 Feb 1944 primary document, no table actually dated within
  1943 located) — recurring here for airborne, but worse: the standard
  infantry gap is a one-year bracket with "minor changes" attested in
  between; the airborne gap is a *known, named, dated* Oct 1943 revision
  that changed real figures (a sniper rifle deleted, a bazooka added) and
  still isn't reproduced anywhere as its own table.

**Verdict: this is a genuine scope mismatch, not a false alarm.** The
closest usable anchor for "late-1943 organization" is the Feb 24, 1944
table, since the book's own text says the changes between Oct 1942 and Feb
1944 were "fairly modest" and it is the table nearest in time to the end of
1943 — but citing it as "1943" would be dishonest without that caveat
stated plainly, so every figure below is labeled by its actual printed
date, not silently relabeled 1943. Per this project's naming convention
this file keeps the `_1943` filename suffix anyway (matching the task's
own instruction), but its content is explicit throughout that the printed
data is Feb/Aug/Dec 1944, with a real but un-reproduced Oct 1943 revision
in between.

## Parachute Rifle Squad (nearest available anchor: Feb 24, 1944 table)

The parachute rifle squad — organic to the parachute infantry platoon,
itself organic to the parachute infantry rifle company (TO&E 7-37) — was
**12 enlisted men**, the same total size as the standard `US_RIFSQ` rifle
squad already in `units.csv`:

| Position | Count | Personal weapon |
|---|---|---|
| Squad Leader (Sergeant) | 1 | M1 Garand rifle |
| Assistant Squad Leader (Sergeant, also squad demolitions specialist) | 1 | M1 Garand rifle |
| Riflemen (one of whom doubled as grenadier) | 7 | M1 Garand rifle |
| MG Gunner | 1 | .30-cal. carbine |
| Assistant MG Gunner | 1 | .30-cal. carbine |
| Ammo Bearer | 1 | .30-cal. carbine |

**Weapon totals per squad:** 9 M1 Garand rifles, 3 .30-cal. carbines (the
MG team), and **up to two .30-cal. Browning light machine guns** — the
book states this explicitly: "the squad had seven riflemen plus a
three-man machine-gun team armed with the .30-cal. Browning light machine
gun... with up to two light machine guns... the parachute rifle squad had
more firepower with two .30-cal. machine guns/BARs versus one BAR in the
regular squad." The December 1944 table substituted a BAR for one of the
two LMGs, but that is outside this project's scope window regardless of
the 1943-vs-1944 question already flagged above.

**This is the single most load-bearing, genuinely surprising finding of
this pass, worth stating plainly against the prompt's own working
assumption:** the parachute rifle squad is **not** simply a lighter-armed
version of the standard rifle squad at the small-arms level. Same
headcount (12), *more* automatic-weapons firepower per squad (two organic
.30-cal. LMGs vs. the standard squad's single BAR), and no bazooka or
bolt-action Springfield at squad level at all (the Springfield-armed
grenadier billet the standard squad carries — see `US_RIFSQ_1943.3_F` —
does not appear in the parachute squad; grenade-launching duty is folded
into one of the seven riflemen instead, per the squad's own personnel
description, with the book not specifying which launcher model that
rifleman carried). The "airborne troops were invariably lighter armed"
framing the book itself uses (p.7) plays out at the **regiment/division**
echelon (no cannon or anti-tank company in the regiment, a 75mm pack
howitzer standing in for the standard division's 105mm howitzers, far
fewer trucks/jeeps), not uniformly all the way down to the rifle squad.

## Other Squad-Level Units

**Mortar Squad (organic to the parachute rifle *platoon*, not company)** —
6 enlisted men: squad sergeant, gunner, assistant gunner, and 3 ammo
bearers, all armed with .30-cal. carbines, serving one organic **60mm M2
mortar**. This is itself a genuine structural distinction from the
standard US infantry organization already documented in
`united_states_1943.md`: the standard rifle platoon has **no** organic
mortar at all (60mm mortars sit one echelon up, in the company's Weapons
Platoon, per that file's own findings) — the parachute platoon pushes its
organic mortar **down** to platoon level instead. This is the platoon-level
mirror of the squad-level LMG finding above: parachute infantry
concentrates more organic supporting firepower at the small-unit level
than standard infantry does, even while the parent regiment as a whole is
lighter than a standard infantry regiment.

**Glider Rifle Squad (for comparison — organic to the separate Glider
Infantry Regiment, not the PIR):** 12 riflemen, **all armed only with
.30-cal. rifles under the Feb 1944 table — no BAR, no LMG at all.** (A BAR
was added in the Dec 1944 reorganization, "bringing them closer to regular
infantry squad organization" — again outside this project's window.) The
book is explicit that glider infantry were, in every practical respect
(training, pay, equipment), treated as ordinary infantry rather than an
elite element — see Quality Tier section below. If this project ever adds
an airborne roster row, the glider infantry squad is a real, structurally
distinct sibling unit (lighter than *both* the parachute squad and the
standard `US_RIFSQ` row), not a redundant near-duplicate.

## Platoon Organization

**Parachute rifle platoon** (Feb 1944 table): platoon HQ + 2 rifle squads
+ 1 mortar squad. Platoon HQ: 1st Lieutenant (platoon commander) + 5
enlisted (platoon sergeant, platoon guide sergeant, 2 messengers, a
radioman with an SCR-536 handy-talkie), with the HQ itself carrying a
bazooka and a sniper rifle as support weapons. **Total platoon strength =
36** under the Feb 1944 table (2×12-man rifle squads + 6-man mortar squad
+ 6-man/officer HQ). (A third rifle squad was added under the Dec 1944
table, raising this to 49 — outside this project's window.)

**Glider rifle platoon** (Feb 1944 table): 3 rifle squads, no organic
mortar squad at platoon level (mortars and heavy machine guns instead sit
in the glider company's own Weapons Platoon — see below), reflecting the
opposite design choice from the parachute platoon's push-down-to-platoon
approach.

## Company Organization

**Parachute infantry rifle company** (TO&E 7-37, Feb 1944 table): company
HQ + 3 rifle platoons, **no separate weapons platoon at company level at
all** — each platoon's own mortar squad already covers that role. Company
total (from the battalion table): 8 officers, 119 enlisted.

**Glider infantry rifle company** (TO&E 7-57, Feb 1944 table): company HQ
+ a dedicated **Weapons Platoon** (2 organic .30-cal. heavy machine guns +
2 organic 60mm mortars) + 2 rifle platoons (the third rifle platoon was a
Dec 1944 addition, outside this project's window). This is structurally
closer to the standard US rifle company's own company-level Weapons
Platoon pattern (`united_states_1943.md`) than the parachute company is —
the parachute company decentralizes its mortars to platoon level, the
glider company keeps them centralized at company level like standard
infantry.

**Parachute infantry battalion** (TO&E 7-35, Feb 1944 table): HQ & HQ co.
+ 3 rifle companies + attached medical. Total 37 officers, 512 enlisted.
Battalion HQ company itself carries 4 organic 81mm mortars ("especially
vital for fire support" given how light the regiment's own artillery
support was) and 9 bazookas.

**Parachute infantry regiment** (TO&E 7-3, originally 17 Feb 1942, three
revisions to Feb 1944 as discussed above): HQ & HQ co. + Service co. + 3
battalions + attached medical/chaplain. Total (Feb 1944 cumulative table):
142 officers, 1,878 enlisted; 73 bazookas; 132 .30-cal. LMGs; 27×60mm
mortars; 12×81mm mortars. No cannon company, no anti-tank company — a
real, explicitly-stated structural absence versus a standard infantry
regiment, which the book states makes the PIR "only about two-thirds the
size of a conventional infantry regiment" even after the Dec 1944
expansion.

**Glider infantry regiment** (TO&E 7-51, originally 15 Sep 1942, revised
Feb 1944): HQ & HQ co. + Service co. + 2 battalions (not 3 — McNair's own
preference for an austere division structure, flagged by the book itself
as a real organizational defect that "caused tactical problems" and was
worked around in the field by attaching a third battalion ad hoc before
D-Day). Each glider battalion additionally deployed a jeep-borne heavy
weapons company (8 organic .30-cal. HMGs + 6 organic 81mm mortars) and an
HQ-company anti-tank platoon (3 towed 57mm AT guns) — heavier
company/battalion-level crew-served weapons than the PIR carries, made
possible by gliders' higher payload versus parachute delivery.

**Division** (TO&E 71, Feb 24 1944 table): HQ & HQ co. + MP platoon +
Divisional artillery (three 75mm pack howitzer battalions — one parachute,
two glider — versus a standard division's four 105mm/155mm battalions) + 1
PIR + 2 GIR (**on paper**) + Engineer bn. + QM co. + Signal co. + Medical
co. + AA bn. (functionally a second anti-tank battalion, per the book) +
Ordnance co. Total 564 officers, 8,032 enlisted men.

**A real, sourced divergence between paper TO&E and actual practice**,
flagged the same way `united_states_1943.md` flagged its own "Automatic
Rifle Squad" oddity: the TO&E's "1 parachute + 2 glider" regimental mix was
never actually used by the 82nd or 101st in combat. The 82nd Airborne
adopted 2 parachute + 1 glider regiments before Sicily "due to shortages of
gliders," and this mix "remained the preferred divisional configuration in
spite of the tables of organization" throughout the war. Anyone building a
future scenario order-of-battle from this file should use the
actually-fielded 2-PIR/1-GIR mix, not the paper 1-PIR/2-GIR TO&E figure,
for any 82nd/101st-based scenario.

## Quality Tier / Crew Basis

The book supports treating **parachute** infantry (not glider infantry,
and not airborne divisions as an undifferentiated whole) as a distinct
higher-quality tier, with real, citable, dated evidence — the same shape
of finding this project's Home Guard militia-tier pass (E.143,
`militia_tier_validation_1943.md`) and US Marine Corps sniper pass (E.150)
already established for other rows:

- **Recruitment:** "From the outset, paratroopers were volunteers, which
  helped to narrow down the recruitment process." Financial incentive: an
  additional $50/month jump pay ($100 for officers).
- **Training:** the standard 13-week infantry course plus a distinct
  4-week jump school at Ft. Benning, "starting with tower jumps and
  culminating in five parachute jumps from aircraft, the last of which was
  a night jump" (footnoted to Carl Smith's *US Paratrooper 1941-45*, Osprey
  Warrior 26 — a candidate title for a future dedicated follow-up pass,
  not read here).
- **A direct contemporaneous quality worry, addressed by evidence:** the
  head of Army Ground Forces, Gen. Lesley McNair, worried that
  "concentration on the 'trick' training would lead to slack standards in
  regular tactical training" — but the book's own assessment is that
  "McNair's concerns were largely misplaced. In combat, the excellent
  training and esprit de corps of the paratroopers helped to overcome the
  shortcomings in the tactics and divisional organization." This is a real
  historian's quality judgment, not this project's own inference.
- **Glider infantry are explicitly NOT part of this tier**, despite
  belonging to the same "airborne division": "little separated the glider
  infantry, or 'glider riders'... from ordinary infantry. They did not
  receive jump training, their equipment was essentially the same as
  regular infantry, and they did not receive any hazardous duty pay" —
  strong enough a distinction that resentment among glider troops became
  "serious enough that on July 1, 1944... the Army reversed its policy and
  awarded extra glider pay." This directly parallels the Army-vs-Marine
  Corps sniper split this project already modeled (E.149/E.150): a single
  parent category ("airborne," "US sniper") containing two populations
  with a real, sourced training/selection/pay gap between them.
- **German assessment of combat value (1943, Sicily):** Field Marshal
  Albert Kesselring "acknowledged later that the paratroopers had caused
  unusual delays in the movement of reserves," and Gen. Kurt Student
  (the German paratrooper commander) said the Hermann Göring Panzer
  Division "would have hurled the invasion force back into the sea were it
  not for the effective delay imposed by the paratroopers" — an
  independent, adversary-sourced quality signal, not just a US self-assessment.

**This is a real, well-cited candidate for a future "US Parachute Infantry
— veteran" roster row alongside a distinct, lower-tier "US Glider Infantry
— regular" row**, exactly the kind of two-row split E.150 already executed
for Army-vs-USMC snipers. Not added here — see Constraints.

## Mechanically Distinct: Drop Dispersion and Post-Landing Disorganization (Flagged, Not Designed)

The book gives real, concrete, repeatedly-documented figures for exactly
the kind of "arrives on the map differently than a unit that walks on"
problem this project's Section 6-24 movement/entry rules do not currently
model for any unit:

- **Sicily, July 9-10, 1943 (Operation Husky):** the 82nd Airborne's drop
  "was widely dispersed due to navigation problems, landing in a swath
  over 50 miles, with only about 425 paratroopers of the initial 3,405
  landing near Gela as planned" — roughly 12% landed on-target.
- **Salerno, night of September 14-15, 1943 (Operation Avalanche):** the
  2/509th PIR, tasked with blocking a mountain pass 20 miles north of
  Salerno, was "badly dispersed on the approach to the drop zone. The 640
  paratroopers were scattered over a 100 square miles of terrain."
  Although "unable to conduct their planned mission, they harassed German
  forces and about 510 troops managed to make their way back to Allied
  lines" — implying roughly 130 men unaccounted for from that single
  battalion-scale drop.
- The book's own throughline across both 1943 operations and the later
  1944 Normandy drops is that scatter of this magnitude was the **norm**
  for night parachute operations given 1943-44 navigation technology, not
  an unlucky exception — directly bearing on any future rules question
  about how (or whether) an airborne unit should enter a scenario
  differently from a unit that marches on.

**This is flagged as a much bigger scope question for the coordinator, not
designed here**, per this pass's own constraints. The book does not give
this project's Cover/Intervening/MP-scale system anything it can absorb
directly (no time-to-reorganize figure specific to a squad or platoon, no
formal scatter-distance formula — the 50-mile and 100-square-mile figures
describe an entire division-scale or battalion-scale drop, not a
per-counter mechanic), so no scatter/disorganization mechanic is proposed
in draft form, only flagged as real and well-evidenced if the coordinator
wants to pursue it in a dedicated pass — the same discipline
`jungle_warfare_rottman_1943.md` (E.152) used when it flagged, but did not
design, a jungle terrain type.

## 1943-Dated Combat Anecdotes (Usable for Future Flavor Text / Design Notes)

1. **Sicily, July 11, 1943** — a friendly-fire disaster during a
   reinforcement drop: while flying to reinforce the original Gela landing
   with two battalions of the 504th PIR, "the mission occurred shortly
   after a Luftwaffe bombing raid on the fleet and as a result, during the
   nighttime flight to the drop zone, the warships began firing on the
   C-47s, shooting down 23 aircraft and seriously damaging 37 more" — named
   operation (Operation Husky), named unit (504th PIR), named division
   commander (Maj. Gen. Matthew Ridgway), precisely dated.
2. **Salerno, September 13, 1943 (Operation Avalanche)** — an emergency
   airborne reinforcement of a threatened amphibious beachhead: Fifth Army
   commander Gen. Mark Clark "requested an airborne reinforcement as
   quickly as possible. Within 15 hours, some 1,300 paratroopers of the
   82nd Airborne Division were successfully dropped into the beachhead
   area on September 13, reinforced the following night by another
   regiment" — a genuinely fast, named, dated emergency-reinforcement
   anecdote distinct from the scatter/disorganization material above.

## Confidence Notes

- The organizational figures above (squad/platoon/company/battalion/
  regiment/division headcounts and weapon counts) come directly from the
  book's own reproduced War Department TO&E tables, cited by TO&E number
  and printed date — high confidence for what they say, but see the Scope
  Verdict section above for the real caveat about which calendar year they
  actually describe.
- The "up to two LMGs" parachute-squad figure and the "no organic mortar
  below platoon level" platoon-structure figure are both stated
  unambiguously in the book's own prose, not inferred from a table's raw
  numbers — high confidence.
- Whether the parachute squad's 2-LMG loadout, or its lack of an organic
  bazooka/Springfield, was already true as of the **October 1943**
  revision specifically (rather than only arriving with the Feb 1944
  change) is **not** established by this book — it only says the Oct 1943
  PIR change deleted the M1903 sniper rifle and added the bazooka
  *somewhere* in the regiment, without saying at which echelon, and does
  not disambiguate which of the three pre-Dec-1944 revisions (Jul 1942,
  Oct 1943, Feb 1944) is responsible for the squad-level 2-LMG figure
  specifically. Flagged as a genuine open question, not resolved here.
- The quality-tier finding (parachute vs. glider infantry) is
  well-supported by multiple independent statements in the book's own
  text (recruitment, training, pay, the glider-pay-riot anecdote, McNair's
  quote and the book's own rebuttal of it) — comparable in strength to the
  Pegler sniper book's US Army/USMC finding that led to E.150's roster
  split, though no roster split is made here.

## Open Questions

1. **No standalone 1943-dated TO&E table for any airborne echelon was
   located in this book** (see Scope Verdict) — a genuinely open item for
   a future session that specifically hunts for a primary-source Oct 1943
   PIR/division TO&E, the same way `united_states_1943.md` flagged an
   equivalent unresolved 1943-dated-primary-document gap for the standard
   rifle company.
2. Whether the parachute squad's 2-organic-LMG loadout already held as of
   October 1943, or only arrived with the February 1944 revision, is
   unresolved (see Confidence Notes) — this bears directly on whether this
   file's headline "more firepower than the standard squad" finding is
   safe to treat as 1943-representative at all, or is itself a Feb
   1944-only fact.
3. A dedicated scatter/disorganization mechanic for air-dropped units is a
   real, evidenced candidate (see Mechanically Distinct section) but is
   explicitly not designed here — left for the coordinator to decide
   whether it is worth a dedicated pass, on the same footing as the
   jungle-terrain-type proposal E.152 left open.
4. No `units.csv` row was added, for either a Parachute Infantry Squad or
   a Glider Infantry Squad — see the top-level design note (E.153) for why
   this constraint was followed even though the parachute-squad data here
   is comparatively well-sourced.
5. Carl Smith's *US Paratrooper 1941-45* (Osprey Warrior 26), footnoted by
   this book as the dedicated source for individual jump training, was not
   independently read this pass — a candidate for a future follow-up if
   more granular jump-school/training detail is wanted.
