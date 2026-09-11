Section 17 — Vehicles: Counter Design and Movement
==================================================

Vehicles in With Deepest Regret... are represented by individual counters at tactical scale (one counter = one vehicle) and section counters at operational scale (one counter = 3-5 vehicles). The same counter design serves both scales — scenario rules define which resolution mode applies.

*Vehicle AV, PEN, and Gunnery Table values are computed by the project's calculation tool (*`counters/armor_calc/`*) from sourced ballistics data (Rule 17.2.5, 17.3.7) and cross-checked against a historical-matchup table covering the full roster (Rule 18.12) — not hand-derived placeholders. See that tool's own README and* `docs/superpowers/specs/2026-07-04-armored-combat-penetration-physics-design.md` *for the full sourcing and validation detail, including the roster's own known gaps (e.g. Sherman Firefly not yet modelled).*

17.1  Vehicle Counter Layout
----------------------------


Vehicle counters display the following fields:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Field**
     - **Position**
     - **Description**
   * - Unit symbol
     - Upper left
     - ○ (circle) for all AFV. ○— for open-topped vehicle.
   * - Unit ID
     - Upper centre
     - Vehicle type and year bracket (e.g. PZ IV H, GER PZIV 43)
   * - Action values
     - Upper right
     - M# F# TRAV# — movement, fire rate, traverse rating
   * - Facing arrow
     - Centre
     - Printed arrow oriented by player to show current facing
   * - Hull armour values
     - Centre
     - F / S / R AV-vs-Capped and AV-vs-Tungsten, front/side/rear (Rule 17.2)
   * - Turret armour values
     - Centre
     - F / S / R AV-vs-Capped and AV-vs-Tungsten, front/side/rear (Rule 17.2). Casemate vehicles (TRAV 0) omit this — hull values apply to every arc.
   * - Gunnery Table
     - Centre
     - Miss/Hull thresholds by range band, already resolved for this vehicle's own Crew Quality (Rule 18.1a)
   * - PEN line(s)
     - Centre
     - Main gun penetration by range band, one line per ammunition nature the gun historically fired (Rule 17.3)
   * - HE line
     - Centre
     - High explosive anti-infantry value: HE rFP #
   * - MG line
     - Centre
     - Machine gun fire line: rFP ⬡h -f
   * - Schürzen marker
     - Centre, on affected arc(s)
     - Printed only if this vehicle/arc historically carried standoff skirt armour (Rule 18.2b)
   * - Morale
     - Lower left
     - Crew morale value
   * - Defence
     - Lower right
     - Crew defensive resilience


**17.1.1**  Vehicle counters have two rear faces representing damage states: MOB KILL (mobility killed — M0, can still fire) and GUN KILL (gun destroyed — MG only, can still move). When a vehicle takes a Casualty result, roll against the Hit Location Table (Rule 18.6a) if one is printed for this vehicle and arc (Rule 17.7); otherwise the owning player chooses which rear face applies based on the most plausible damage given the shot geometry.

.. container:: rule-guide

   **Why:** Gives vehicle damage two distinct, mutually exclusive degraded states rather than one generic "damaged" condition, reflecting that a hit disabling mobility and a hit disabling the gun are genuinely different outcomes with different tactical consequences — and lets an actual Hit Location Table (where one exists) decide it by roll rather than free choice.

   **Example:** A Sherman with a printed Hit Location Table (Rule 18.6a) rolls to determine whether a Casualty result becomes MOB KILL or GUN KILL; a vehicle without one has its owning player pick whichever rear face makes more sense given how the shot was described.

**17.1.2**  Casemate vehicles (TRAV 0 — no separate turret) print only Hull armour values, which apply regardless of which "profile" Rule 18.1a's Gunnery Roll would otherwise indicate. There is no Hull/Turret hit allocation for these vehicles.

.. container:: rule-guide

   **Why:** Simplifies the Hull/Turret split (Rule 17.2.2) away entirely for vehicles that never had a separate turret in the first place — a casemate vehicle's single armor profile is all there is to hit, so the Gunnery Roll's profile-selection step has nothing to select between.

   **Example:** A StuG III (casemate, TRAV 0) resolves every incoming shot against its single set of Hull AV values — there's no possibility of a "Turret hit" outcome for this vehicle at all.

17.2  Armour Values
-------------------


**17.2.1**  Armour Values (AV) represent effective armour protection in millimetres, already resolved at design time to a 0°-equivalent figure (slope angle, cast/rolled deficiency, high-hardness deviation, documented flaws, and face-hardening are all folded in before the number is printed). Players never apply slope or material-quality modifiers at the table — the printed AV is final.

.. container:: rule-guide

   **Why:** Pre-computes every real-world armor complexity (slope, material, hardness, flaws) into a single printed number so play-time resolution is a simple comparison, not a physics calculation — all the historical research and math happens once at design time (Rule 17.2.5), not at the table every shot.

   **Example:** A tank's printed Front AV already accounts for its actual armor thickness and its hull's slope angle — a player comparing a shot's PEN against that AV never needs to separately factor in the plate's angle themselves.

**17.2.2**  Every vehicle counter with a separate turret (TRAV 1 or higher) prints **two independent profiles** — Hull and Turret — each with its own Front/Side/Rear AV. Which profile a shot resolves against is determined by the Gunnery Roll (Rule 18.1a), not chosen by the attacker. Casemate vehicles (TRAV 0) print Hull values only (Rule 17.1.2).

.. container:: rule-guide

   **Why:** Splits a turreted vehicle into two independently-armored profiles, since a real tank's hull and turret genuinely have different armor thicknesses — and hands profile selection to a die roll rather than attacker choice, since an attacker in the heat of battle doesn't get to pick exactly where their round strikes.

   **Example:** A Panzer IV's turret and hull each have their own separate Front/Side/Rear AV values; whether an incoming shot resolves against the turret's or the hull's numbers is decided by the Gunnery Roll (Rule 18.1a), not by the firing player choosing the weaker target.

**17.2.3**  Each arc of each profile prints **three AV values**: AV-vs-Capped (for APC/APCBC rounds), AV-vs-Tungsten (for HVAP/APCR/APDS rounds), and AV-vs-HEAT (for all shaped-charge attacks — Rule 17.2.4). Uncapped and capped kinetic rounds have measurably different slope sensitivity, tungsten rounds lose relative effectiveness faster as impact angle increases, and HEAT ignores velocity entirely — one number cannot represent them all.

.. container:: rule-guide

   **Why:** Prints three separate AV values per arc because the real physics of how armor resists different ammunition types genuinely differ — a single AV number would either overstate or understate protection depending on which ammunition nature is actually firing.

   **Example:** A plate's AV-vs-Tungsten value is typically lower than its AV-vs-Capped value for the same arc, reflecting that tungsten rounds retain penetrating power at oblique angles better than capped rounds do against that same slope.

**17.2.3a**  Uncapped AP and Soviet APBC attackers also use the AV-vs-Capped value — **except** against face-hardened plates (marked FH on the counter), where the printed Capped figure bakes in a correction that applies to capped noses only. Against the roster's face-hardened plates, an APBC or uncapped-AP attacker uses these values instead:

.. container:: rule-guide

   **Why:** Fixes a real historical wrinkle where face-hardened armor responds very differently to different projectile nose shapes — a capped round's soft cap defeats face-hardening, an uncapped round's exposed nose shatters against it, and APBC falls in between — so reusing the printed Capped column for those other two ammunition types would have quietly misrepresented all three plates' actual resistance.

   **Example:** An uncapped AP round firing at a face-hardened Panzer IV Ausf H hull front uses AV 101.2 (the table's uncapped-AP-specific value) rather than the printed 64.9 Capped figure — using the wrong column would have overstated that plate's protection against an uncapped round by more than 30%.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Face-hardened plate**
     - **AV vs Capped (printed)**
     - **AV vs APBC**
     - **AV vs Uncapped AP**
   * - Panzer IV Ausf H — Hull Front
     - 64.9
     - 83.2
     - 101.2
   * - Panzer IV Ausf H — Hull Side
     - 23.8
     - 30.4
     - 35.7
   * - Panzer III Ausf M — Hull Front
     - 51.4
     - 59.9
     - 69.6
   * - StuG III Ausf G — Hull Side
     - 23.8
     - 30.4
     - 35.7


*NOTE: face-hardening is a real penalty for capped rounds (the cap defeats the hardened face), no correction at all for APBC, and a real bonus for uncapped AP (the hardened face shatters the unprotected nose) — reusing the Capped column for those attackers understated these four plates by 30–70%. Values above use the same 75mm reference diameter as the printed columns; a validation script needing exact attacker-diameter figures calls* ``resolve_av(diameter, hardness_table, family=...)`` *directly (see Rule 18.12 note (e)).*

**17.2.4**  HEAT attacks compare their flat PEN directly against the printed **AV-vs-HEAT** value for the struck profile and arc — no arithmetic at the table. Because HEAT's effective resistance depends only on the plate (thickness and angle), never on the attacker, one printed number per arc covers every HEAT weapon in the game — it is the one AV that is genuinely attacker-independent.

.. container:: rule-guide

   **Why:** Makes HEAT resolution the simplest of the three ammunition natures, since a shaped-charge jet's penetration doesn't depend on the launching weapon's velocity the way kinetic rounds do — one printed AV-vs-HEAT value serves every HEAT-firing weapon that ever targets that plate.

   **Example:** A Panzerfaust and a HEAT tank round striking the same arc of the same vehicle both compare their own flat PEN values against that single AV-vs-HEAT number — no separate HEAT figures are needed per weapon.

**17.2.5**  AV, PEN, and the Gunnery Table are all computed by the project's calculation tool (`counters/armor_calc/`) from sourced ballistics data, not derived by formula at the table. See that tool's own documentation for the full physics — nothing beyond the printed numbers is needed to play.

.. container:: rule-guide

   **Why:** Keeps the heavy ballistics math entirely in the design-time tooling rather than exposing any of it to players, so the printed counter values are all a player ever needs — the underlying physics is documented for verification, not for table-side recalculation.

   **Example:** A player never needs to open `armor_calc` to play a scenario — every AV, PEN, and Gunnery Table value already printed on the counters is the finished, ready-to-use output of that tool's calculations.

**17.2.6**  Slope, material quality, hardness, and flaw corrections are all already resolved into the printed AV (Rule 17.2.1) — there is no separate step for players to apply any of them.

.. container:: rule-guide

   **Why:** Restates Rule 17.2.1's core promise plainly — every real armor complication is already baked into the number on the counter, so a player checking a plate's protection never has a further correction step to remember or look up.

   **Example:** A player comparing PEN against a printed AV value does the comparison directly with no adjustment for the plate's actual slope, quality, or documented flaws — those were all already factored in when the number was printed.

**17.2.7**  HEAT Reference Table — designer reference only (the multipliers from which the printed AV-vs-HEAT values are computed; never consulted during play):

.. container:: rule-guide

   **Why:** Publishes the underlying HEAT-angle physics for transparency and verification, while explicitly marking it off-limits for actual play — the printed AV-vs-HEAT values (Rule 17.2.4) already have this table's multipliers baked in, so consulting it during a game would be redundant at best and a rules error at worst.

   **Example:** A player curious why a sloped plate's AV-vs-HEAT is higher than its flat-on value can check this reference table to see the angle multiplier behind that number — but never needs to during an actual game, since the final value is already printed.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Angle from vertical**
     - **HEAT multiplier**
   * - 0°
     - 1.00
   * - 15°
     - 1.04
   * - 30°
     - 1.16
   * - 45°
     - 1.41
   * - 60°
     - 2.00
   * - 75°
     - 3.86


**17.2.8**  Shatter Gap (optional/advanced rule) and Schürzen (standoff skirt armour vs. HEAT) are covered in Rules 18.2a and 18.2b respectively — both apply after the AV comparison above, not as part of it.

.. container:: rule-guide

   **Why:** Keeps the core AV comparison of this section clean and self-contained, pointing two further refinements (an optional advanced rule and a specific standoff-armor exception) to their own rules rather than folding them into the base mechanic every shot must consider.

   **Example:** A basic penetration check just compares PEN to AV as this section describes; only if the target has Schürzen or the table is using the optional Shatter Gap rule does a player need to consult Rule 18.2a or 18.2b for an additional step afterward.

17.2a  Top Armour (Optional Rule)
-----------------------------------

*If this module is in use for the scenario:*

*Design note: no vehicle in this roster printed a Top arc at all before this module — every plate was Front, Side, or Rear (Rule 17.2.2). Top AV exists to support Rule 18.2c (Sidehill Exposure) and Rule 16.7.8a (heavy mortar/artillery vs. top armour); a group not using either of those never needs this stat. See design note E.120.*

**17.2a.1**  A vehicle may print a fourth arc, Top, for its Hull and/or Turret profile — the horizontal deck or roof plate, computed and printed exactly like any other arc (Rule 17.2.1, 17.2.3): AV-vs-Capped, AV-vs-Tungsten, and AV-vs-HEAT. Top AV is printed only where a real, cited thickness exists for that specific vehicle and profile — a vehicle or profile with no printed Top AV simply has none, the same "lookup miss means not modelled, not zero" convention this project already uses for missing hardness data (`counters/armor_calc/data/hardness_table.csv`).

.. container:: rule-guide

   **Why:** Treats an unprinted Top AV as an honest gap rather than inventing a plausible-looking placeholder number, consistent with how every other under-sourced figure in this project is handled — a vehicle designer who later finds a citable figure can add the row without touching anything else.

   **Example:** Tiger I Ausf E prints a Hull Top and Turret Top AV (both sourced); Panzer III Ausf M prints neither (disputed sources, no primary tiebreaker found) — a shot that would otherwise use Panzer III's Top AV under Rule 18.2c simply has no Top AV to compare against, and resolves against Side AV alone.

**17.2a.2**  Top AV is never a fourth option in an ordinary Gunnery Roll (Rule 18.1a) — the Hull/Turret split (Rule 18.1a.5) still only ever resolves to Hull or Turret. Top AV comes into play only as a substitution under Rule 18.2c, or as the flavour (not the mechanic) behind Rule 16.7.8a's mobility-kill check.

.. container:: rule-guide

   **Why:** Keeps the base Gunnery Roll exactly as simple as it has always been — a third printed arc would otherwise imply a three-way hit-location roll for every single shot, which is far more table overhead than the narrow, conditional cases Top AV actually needs to cover.

   **Example:** An ordinary tank-vs-tank shot at normal range never even considers Top AV — it resolves Hull or Turret exactly as Rule 18.1a already describes, whether or not the target has a printed Top AV at all.

17.3  Penetration Values
------------------------


**17.3.1**  Penetration values (PEN) are printed as 0°-equivalent millimetres at a small set of range bands (typically 0/250/500/750/1000/1500/2000m), not as a single value with falloff notation. Read the row for the actual range to target, using the next lower printed band if the exact range falls between two listed bands — a shot at less than 250m reads the 0m (point-blank) row.

.. container:: rule-guide

   **Why:** Prints PEN as discrete looked-up values at fixed range bands rather than a formula with falloff notation, since real penetration-vs-range curves aren't linear — a small lookup table captures the actual ballistic behavior more accurately than a simple rate-of-loss number ever could.

   **Example:** A shot at 600m against a gun printing bands at 0/250/500/750/1000m reads the 500m row (the next lower printed band), not an interpolated value between 500m and 750m.

**17.3.2**  A gun prints one PEN line per ammunition nature it historically carried — Capped, Uncapped AP, or Tungsten (HVAP/APCR/APDS) — up to two or three lines. The firing player freely chooses which loaded nature to fire with each shot, tracked via the extended-ammunition mechanism (Rule 16.3.3) for any premium (Tungsten) rounds: the scenario states the vehicle's base Tungsten load; past it, roll the extended table per shot.

.. container:: rule-guide

   **Why:** Lets a player pick their ammunition nature shot by shot rather than committing to one loadout for the whole scenario, while still constraining premium Tungsten rounds through the same limited-supply mechanism used for mortar ammunition (Rule 16.3.3) — historically scarce ammunition stays scarce in play.

   **Example:** A tank with printed Capped and Tungsten PEN lines can fire Capped rounds freely all scenario, but its Tungsten rounds are limited to its scenario-stated base load; firing Tungsten beyond that triggers the same extended-ammunition roll a mortar would use.

**17.3.3**  HEAT weapons (Panzerfaust, PIAT, Bazooka, HEAT rounds) have flat penetration values — no range bands. Their accuracy degrades with range through hard range limits (Rule 18.9), not through penetration reduction.

.. container:: rule-guide

   **Why:** Reflects the real physics of shaped-charge weapons — a HEAT jet's penetration doesn't depend on impact velocity the way kinetic rounds do, so there's no falloff curve to print; what does degrade with range is the weapon's practical ability to hit at all, handled separately by hard range limits.

   **Example:** A Panzerfaust's penetration value is identical whether it hits at 10m or at its maximum effective range — the weapon simply can't be fired accurately much past that range at all (Rule 18.9), rather than penetrating less at longer range.

**17.3.4**  Compare the PEN value for the actual range and chosen ammunition nature against the target's AV-vs-Capped or AV-vs-Tungsten (matching the ammunition fired) on the profile and arc selected by the Gunnery Roll (Rule 18.1a) — see Rule 18.2.

.. container:: rule-guide

   **Why:** Ties the comparison together across three separate pieces of information — range-appropriate PEN, ammunition-matching AV column, and the Gunnery-Roll-determined profile and arc — all of which must line up correctly for the penetration check to be valid.

   **Example:** A Tungsten round fired at 500m compares its 500m-band Tungsten PEN value against the target's AV-vs-Tungsten (not AV-vs-Capped) figure, on whichever profile and arc the Gunnery Roll determined the shot actually struck.

**17.3.5**  Gunnery Table — every vehicle-mounted gun also prints a Gunnery Table: a Miss Threshold and a Hull Threshold for each range band, already resolved for that gun's own vehicle's Crew Quality. Rule 18.1a covers how to read and roll against it — no calculation is required at the table.

.. container:: rule-guide

   **Why:** Pre-resolves the firing vehicle's own crew quality directly into its printed Gunnery Table, so a player never needs to separately apply a crew-quality modifier at the table — the table already reflects exactly how good that vehicle's specific crew is at hitting things.

   **Example:** Two otherwise-identical guns mounted on an Elite-crewed vehicle and a Green-crewed vehicle print two different Gunnery Tables, each already adjusted for that vehicle's own crew quality — the player just reads the printed thresholds directly.

**17.3.6**  Crew Quality is derived from the firing vehicle's own Morale value and fixed at counter-design time: Morale 7+ = Elite, Morale 6 = Veteran, Morale 5 = Regular, Morale 3–4 = Green, Morale 2 or less = Militia.

.. container:: rule-guide

   **Why:** Ties vehicle crew quality to the same Morale scale used everywhere else in the rules (Rule 15.2.1a's quality ladder), rather than introducing a separate vehicle-only quality metric — one consistent Morale value drives both the crew's steadiness and, via this rule, their gunnery skill.

   **Example:** A vehicle counter printed with Morale 6 is fixed as Veteran Crew Quality at design time, which is what determined the specific numbers baked into that vehicle's own printed Gunnery Table (Rule 17.3.5).

**17.3.7**  PEN, AV, and Gunnery Table values are computed by the project's calculation tool from sourced ballistics data (velocity-at-range, slope multipliers by ammunition nose shape, and the flight-time-based hit-probability model) — not derived by formula at the table.

.. container:: rule-guide

   **Why:** Reaffirms that all this section's numbers come from real ballistics research processed by dedicated tooling rather than a simplified in-play formula, giving the printed values a documented, verifiable basis rather than being ad hoc design choices.

   **Example:** A gun's printed PEN-at-500m figure traces back through the calculation tool to actual sourced velocity-at-range data for that specific historical round, not a hand-picked number chosen to feel right.

17.4  Traverse Rating
---------------------


**17.4.1**  Traverse rating (TRAV) determines how many hexsides a vehicle's gun can cover from its current facing in one fire action. All TRAV arcs are contiguous and centred on the facing arrow — no choice of which hexsides are covered is required. (TRAV arcs govern where the gun can shoot; armour facing arcs, Rule 17.5.2, govern which AV an incoming shot strikes. The two are independent.)

.. container:: rule-guide

   **Why:** Keeps TRAV (what the gun can shoot at) and armor facing arcs (what AV an incoming shot uses) as two genuinely separate systems, since a vehicle's turret rotation speed and its hull armor thickness by direction are unrelated real-world properties — conflating them would misrepresent both.

   **Example:** A fast-turreted TRAV 3 vehicle can engage any target regardless of hull facing, but that same hull's armor facing arcs (Rule 17.5.2) still determine which AV value an incoming shot uses based on the hull's actual orientation — the two never interact.

**17.4.1a**  A vehicle does not follow Rule 6.3.1's Regular/Assault split. In a single turn it may take one Move action and one Fire action (Rule 6.3.2, 1 AP each), in either order — a vehicle's Move does not place a MOVED/FIRED marker and does not by itself end its turn. A vehicle instead tracks only whether it has moved this turn, via its own MOVED marker (Rule 18.1a.6) — a simpler, separate concept from the infantry MOVED/FIRED marker (Rule 6.5.1), which vehicles do not use. A vehicle that has both moved and fired this turn may not move or fire again. If the Fire action comes after the Move action, it is subject to Rule 17.4.2's TRAV penalty; a Fire action taken before the vehicle has moved this turn is not.

.. container:: rule-guide

   **Why:** States outright, as its own rule, an exception that otherwise has to be pieced together from two of its own side effects — Rule 17.4.2's TRAV-minus-one-if-moved penalty and the Gunnery Roll's crossing-target adjustment (Rule 18.1a.6) both only make sense once a reader already knows a vehicle can move and then fire in the same turn, something Section 6 never says and a vehicle counter's own action economy shouldn't require piecing together from elsewhere.

   **Example:** A Panzer IV spends 1 AP to move 3 hexes toward a firing position, then spends a second AP later in the turn to fire at a target it can now see — perfectly legal, and exactly what real tank tactics call for, unlike a rifle squad which would already be MOVED/FIRED after the move alone.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **TRAV**
     - **Hex sides covered**
     - **Equivalent traverse speed**
     - **Examples**
   * - 3
     - All 6 hexsides — any target in LOS
     - > 20°/second
     - T-34, Sherman, Panzer IV H
   * - 2
     - 5 of 6 hexsides — all except the rear hexside
     - 10–20°/second
     - Cromwell, early Churchill
   * - 1
     - 3 of 6 hexsides — the front hexside plus the two adjacent to it
     - 5–10°/second
     - KV-1, early Matilda
   * - 0
     - Front hexside only — fixed gun
     - < 5° or casemate
     - StuG III, Jagdpanzer, SU-85


**17.4.2**  A vehicle that moved this turn fires at TRAV -1 (minimum 0). Exception: TRAV 3 vehicles are unaffected by movement — their rapid traverse compensates.

.. container:: rule-guide

   **Why:** Penalizes a slower-traversing vehicle's firing arc after moving, since keeping a gun tracking a target while the whole vehicle is repositioning is genuinely harder — but exempts the fastest turrets (TRAV 3) specifically because their real-world traverse speed was fast enough to compensate for the vehicle's own movement.

   **Example:** A TRAV 2 vehicle that moved this turn fires at effective TRAV 1 for that action, while a TRAV 3 vehicle that moved the same distance still fires at its full TRAV 3 — the traverse-speed exception applies only at that top tier.

**17.4.3**  Between fire actions in the same turn, the turret is assumed to return to forward facing. A vehicle with TRAV 1 that fires left cannot immediately fire right in the same turn — it must fire forward or wait until next turn.

.. container:: rule-guide

   **Why:** Resets the turret to forward between fire actions rather than letting a limited-traverse vehicle freely swing its arc back and forth within one turn — TRAV 1's "3 of 6 hexsides" coverage (Rule 17.4 table) is meant to represent one arc choice per turn, not two opposite engagements.

   **Example:** A TRAV 1 vehicle fires at a target to its left this turn, using up its limited arc in that direction; it cannot then fire at a different target to its right in the same turn — the turret is assumed to have reset forward between actions.

**17.4.4**  Casemate vehicles (TRAV 0) cannot rotate the gun independently. To engage targets outside the front hex, the entire vehicle must pivot. Each 60° of vehicle pivot costs 1 additional MP on top of normal pivot cost.

.. container:: rule-guide

   **Why:** Ties a casemate vehicle's targeting flexibility entirely to whole-vehicle movement, since it has no independent turret at all — engaging anything outside the fixed front arc means physically turning the vehicle, which costs real MP on top of whatever pivot the vehicle would otherwise need.

   **Example:** A casemate tank destroyer wanting to engage a target 60° off its current front hexside must pivot the whole vehicle that 60°, paying 1 additional MP beyond normal pivot cost (Rule 17.5.4) to do so.

17.5  Vehicle Facing
--------------------


**17.5.1**  Vehicle facing is tracked by orienting the counter's printed facing arrow toward one of the six hex sides of the vehicle's current hex.

.. container:: rule-guide

   **Why:** Uses the counter's own printed arrow as the single, unambiguous physical record of facing, so both players can read a vehicle's orientation directly off the map without needing a separate tracking sheet or marker.

   **Example:** A tank's facing arrow pointing toward the northeast hexside tells both players immediately which direction that vehicle is oriented, without consulting any other record.

**17.5.2**  Facing arcs are the six 60° wedges of the map radiating from the vehicle's hex, one per hexside, extended to **any range** — each wedge contains the adjacent hex through that hexside and every hex beyond it in that sixth of the map:

.. container:: rule-guide

   **Why:** Extends facing arcs out to unlimited range rather than just the adjacent hex, since a vehicle's armor facing genuinely matters at long range too — an attacker 1,000 yards away on a tank's flank still strikes its side armor, not its front, just as one hex away would.

   **Example:** A tank facing north has a FRONT wedge extending indefinitely northward; an enemy vehicle 10 hexes away but within that same wedge still strikes the tank's Front AV, exactly as an enemy one hex directly ahead would.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Arc**
     - **Wedges covered**
     - **AV used**
   * - FRONT
     - The wedge through the faced hexside (arrow direction)
     - F value
   * - SIDE
     - The two wedges adjacent to FRONT and the two adjacent to REAR (four wedges)
     - S value
   * - REAR
     - The wedge through the opposite hexside
     - R value


**17.5.2a**  The attacker's arc is the wedge containing the attacker's hex. A hex lying exactly on the spine between two wedges counts as the wedge **less favourable to the target** (the attacker's choice of the two AVs' better side): a spine between FRONT and SIDE resolves as SIDE, between SIDE and REAR as REAR. At adjacent range this reduces exactly to the old adjacent-hex table — one hex ahead is FRONT, one behind is REAR, the four others SIDE.

.. container:: rule-guide

   **Why:** Resolves the edge case of a shot landing exactly on the boundary between two wedges by favoring the attacker, since an ambiguous geometric case shouldn't default to protecting the target — and confirms the new any-range system produces identical results to the old adjacent-hex-only table at close range, so nothing about short-range combat actually changed.

   **Example:** An attacker positioned exactly on the spine between a target's FRONT and SIDE wedges resolves as a SIDE hit (the worse AV for the target) rather than FRONT — the ambiguity breaks toward the attacker's advantage, not the target's.

*NOTE: a 60° front means oblique fire at any range strikes SIDE armour — positioning and facing matter at 1,000 yards as much as at 40. The historical-matchup table (Rule 18.12) states its engagements as head-on (attacker in the FRONT wedge); an attacker manoeuvred onto a flank uses the Side AVs, which is the point.*


**17.5.3**  When a vehicle moves, its facing changes to match the direction of movement unless the player explicitly declares a pivot.

.. container:: rule-guide

   **Why:** Makes ordinary movement automatically reorient a vehicle's facing, since a tank driving forward naturally ends up facing the direction it drove — the player only needs to declare something different (a pivot) when they specifically want to move one way while facing another.

   **Example:** A tank moving northeast simply ends the move facing northeast — the player doesn't need to separately declare a facing change unless they want the vehicle to end up facing some other direction via a pivot.

**17.5.4**  Pivot without moving: costs 1 MP per 60° of rotation. A vehicle pivoting from facing north to facing east (120° turn) costs 2 MP.

.. container:: rule-guide

   **Why:** Prices in-place rotation by the actual angle turned, since a real vehicle pivoting further genuinely takes more time and track wear — a full 180° reversal costs proportionally more MP than a small 60° adjustment.

   **Example:** As printed: a vehicle facing north that wants to face east (a 120° turn) spends 2 MP — one for each 60° increment of rotation.

**17.5.5**  TRAVERSED marker: when a turreted vehicle fires at a target outside its hull's front hexside — i.e. the shot requires the turret to traverse away from the hull's facing arrow, within its TRAV rating (Rule 17.4) — place a TRAVERSED marker on the vehicle, oriented toward the engaged hexside. This shows the turret's actual current facing, independent of the hull's facing arrow.

.. container:: rule-guide

   **Why:** Lets a turreted vehicle's gun point somewhere different from its hull's facing arrow, tracked with its own separate marker, since a real turret can rotate independently of the hull it sits on — the TRAVERSED marker is what records that the turret has swung off the hull's own forward direction.

   **Example:** A tank facing north that engages a target to its east places a TRAVERSED marker oriented east on top of its counter — the hull's own facing arrow still points north, but the turret marker shows where the gun is actually pointed.

While a TRAVERSED marker is present, any attack resolving against this vehicle's **Turret** profile (per Rule 18.1a's Gunnery Roll) determines its arc relative to the TRAVERSED marker, not the hull's facing arrow. Attacks resolving against the **Hull** profile always use the hull's facing arrow, regardless of the TRAVERSED marker.

The marker is removed the instant the vehicle takes another fire action this turn (replaced by a new one if that shot also requires an off-forward traverse), and in any case is removed at the Recovery Phase along with all other action markers — consistent with Rule 17.4.3 (turret returns to forward facing between fire actions).

Casemate vehicles (TRAV 0) never receive a TRAVERSED marker; they have no separate turret profile.

17.6  Vehicle Movement
----------------------


**17.6.1**  Vehicle movement allowances:

.. container:: rule-guide

   **Why:** Sets movement allowance by vehicle class rather than individually per counter, since real vehicles of the same broad type (light tank, medium tank, heavy tank) had genuinely similar road speeds — one class-based M# value captures that pattern without needing a bespoke number for every single vehicle.

   **Example:** A Panzer IV and a T-34, both medium tanks, share the same M3 movement allowance under this table, even though they're different vehicles from different nations — their class, not their specific model, determines the printed M#.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Vehicle type**
     - **M#**
     - **Notes**
   * - Light tank / armoured car
     - M4
     - Fast, lightly armoured
   * - Medium tank
     - M3
     - Standard — Panzer IV, T-34, Sherman
   * - Heavy tank
     - M2
     - Tiger, KV-1 — powerful but slow
   * - Tank destroyer (turreted)
     - M3
     - Same as medium tank
   * - Tank destroyer (casemate)
     - M3
     - Pivot costs extra MP — see Rule 17.4.4
   * - Half-track
     - M3
     - Tracked mobility, wheeled terrain limits
   * - Truck / soft vehicle
     - M3
     - Road only effectively — see terrain table


**17.6.2**  Vehicle terrain movement costs (see Rule 17.6.2a for bog checks):

.. container:: rule-guide

   **Why:** Gives vehicles their own separate terrain-cost table rather than reusing the infantry one (Rule 7.2), since tracked and wheeled vehicles interact with terrain very differently from foot troops — some terrain that slows infantry only mildly is completely impassable to a wheeled vehicle, and vice versa.

   **Example:** Dense woods costs infantry only 3 MP to cross, but is flatly impassable to wheeled vehicles and carries a bog-check risk for tracked ones (Rule 17.6.2a) — the same terrain type behaves very differently depending on who's moving through it.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Terrain**
     - **Infantry**
     - **Tracked vehicle**
     - **Wheeled vehicle**
     - **Notes**
   * - Open ground
     - 1
     - 1
     - 1
     - Baseline
   * - Road (special rule)
     - Special
     - +3 hexes
     - +4 hexes
     - Entire activation on road only
   * - Crops / tall grass
     - 1
     - 1
     - 1
     - 
   * - Light woods
     - 2
     - 2
     - 3
     - 
   * - Dense woods
     - 3
     - 3
     - Impassable
     - Bog check for tracked vehicles — Rule 17.6.2a
   * - Hedgerow
     - 2
     - 3
     - Impassable
     - 
   * - Building
     - 1
     - Impassable
     - Impassable
     - 
   * - Rubble
     - 2
     - 3
     - Impassable
     - 
   * - Ditch / sunken road
     - 1
     - 2
     - 2
     -
   * - Anti-tank ditch (Rule 4.1.3a)
     - 1
     - Impassable*
     - Impassable*
     - \*Except at a marked crossing point, entered at this row's ordinary tracked/wheeled cost
   * - Shallow stream
     - 2
     - 2
     - 3
     - 
   * - Soft ground
     - 1
     - 2
     - 3
     - Mud, marsh edges
   * - Slope (per level)
     - +1
     - +1
     - +2
     - Uphill only
   * - Cliff / river
     - Impassable
     - Impassable
     - Impassable
     - 


**17.6.2a**  Bog check: when a tracked vehicle enters a dense woods hex, roll 1d6 after paying the movement cost: on 1–2 the vehicle bogs — place a BOGGED marker; it cannot move (M0) but fights normally. To free a bogged vehicle, spend a full activation working it loose and roll 1d6: on 4+ remove the BOGGED marker (+1 to the roll if a friendly vehicle is adjacent to tow). A vehicle still bogged at scenario end is treated as abandoned in place (Rule 19.3) if enemy units control the hex area, else recovered.

.. container:: rule-guide

   **Why:** Gives dense woods a real chance of trapping a tracked vehicle rather than just costing extra MP, since a heavy vehicle grinding through thick terrain genuinely risks getting stuck — the recovery mechanism (an activation and a roll, with a tow bonus) models freeing it as a real but not guaranteed effort.

   **Example:** A tank entering a dense woods hex rolls 1d6 after paying the movement cost; on a 1 or 2 it becomes BOGGED — unable to move but still able to fight — until a later activation successfully works it loose, made easier if a friendly vehicle is adjacent to help tow it out.

**17.6.2b**  Reverse movement: a vehicle may back directly into the hex behind it (its rear-wedge adjacent hex) without changing facing, at **double** the terrain's MP cost per hex. This is how a casemate tank destroyer disengages without exposing its side or rear armour.

.. container:: rule-guide

   **Why:** Lets a vehicle retreat without exposing its weaker side or rear armor by keeping its front facing toward the threat, at a real cost in extra MP reflecting how much slower and less controlled reverse driving is compared to forward movement.

   **Example:** A casemate tank destroyer facing an enemy threat can back straight into the hex behind it at double the terrain's normal MP cost, disengaging while keeping its strong front armor still oriented toward the enemy the whole time.

**17.6.3**  Vehicle LOS: vehicles are larger than infantry. Any unit with LOS to a vehicle's hex automatically has LOS to the vehicle through up to 2 hexes of light woods or 1 hex of dense woods. Normal LOS rules apply beyond these limits.

.. container:: rule-guide

   **Why:** Gives vehicles a small LOS advantage over infantry's usual blocking rules (Rule 4.4.3), reflecting that a tank is a much bigger, harder-to-fully-conceal target than an infantry squad — a little terrain that would fully hide a foot unit still leaves a large vehicle at least partly visible.

   **Example:** A unit with LOS to a hex containing 1 hex of intervening dense woods can still see a vehicle sitting there, even though that same amount of dense woods might have fully blocked LOS to an infantry unit under the normal blocking rules.

17.6a  Bypass Movement (Optional Rule)
-------------------------------------------

*If this module is in use for the scenario:*

*Design note: every vehicle move fully enters a hex and takes on that hex's full terrain cost and risk (including Rule 17.6.2a's bog check) — there was no way to skirt an obstacle rather than drive through it, the way Advanced Squad Leader's Bypass rule lets a vehicle hug a hex's edge instead of its center. Scoped as optional because the trade-off it adds (speed and safety for cover and combat capability) is exactly the kind of extra declared choice the base game deliberately keeps out of ordinary movement. See design note E.115.*

**17.6a.1**  A vehicle entering a hex may declare Bypass instead of an ordinary move into it: pay open ground's MP cost (1) regardless of the hex's actual terrain, and skip Rule 17.6.2a's bog check entirely for that hex.

.. container:: rule-guide

   **Why:** Models a vehicle skirting along a hex's edge — around a building, through a gap in a wall line, along a track through rough ground — rather than actually driving through whatever fills the hex's center, which is exactly the maneuver that avoids both the terrain's usual cost and its usual risk.

   **Example:** A vehicle bypassing a dense-woods hex pays 1 MP and never rolls the Rule 17.6.2a bog check, instead of the terrain's normal 3+ MP cost and bog risk it would face entering the hex directly.

**17.6a.2**  A vehicle that bypassed a hex gains no terrain cover bonus there (treated as being in the open for Defence purposes while in that hex) and may not declare Overrun (Rule 18.11) from it this activation — it has skirted past the position, not engaged it.

.. container:: rule-guide

   **Why:** A vehicle that never actually drove into a position hasn't earned that position's cover, and hasn't physically confronted whatever might be occupying it — bypass buys speed and safety from the terrain itself at the cost of any tactical benefit that terrain would otherwise have offered.

   **Example:** A vehicle bypassing a building hex is attacked as if it were sitting in open ground, with none of the building's printed cover value — and cannot declare an Overrun against infantry in that same hex this activation, having gone around them rather than at them.

**17.6a.3**  Bypass is not available for a hex that is Impassable to that vehicle type regardless of terrain (Rule 17.6.2's table) — Bypass avoids an obstacle's cost and risk, not genuine impassability.

.. container:: rule-guide

   **Why:** Bypass represents skirting around what a hex contains, not ignoring physical facts about what a vehicle can cross at all — a river or cliff genuinely impassable to a given vehicle type stays impassable no matter how the vehicle tries to approach it.

   **Example:** A vehicle cannot Bypass its way across a River/cliff hex it could never enter under Rule 17.6.2 in the first place — Bypass only ever applies to hexes the vehicle could otherwise legally enter directly.

17.6b  Hull-Down Position (Optional Rule)
-------------------------------------------

*If this module is in use for the scenario:*

*Design note: real tank doctrine's single most basic defensive posture — back the hull below a crest so only the turret shows — had no rule of its own; a vehicle's Hull profile was always just as targetable as its Turret regardless of terrain. See design note E.120.*

**17.6b.1**  A stationary, turreted vehicle (Rule 17.2.2 — casemate vehicles have no separate Turret profile to hide behind) occupying a hex with a crest hexside (Rule 4.4a.1) may declare Hull-Down, 1 AP, oriented toward one specific low-side hexside of that crest. Declaring Hull-Down does not place a MOVED marker and does not prevent the vehicle from also firing this turn (Rule 17.4.1a).

.. container:: rule-guide

   **Why:** Costs a real action rather than being a free, automatic consequence of terrain, since a crew actually has to manoeuvre the vehicle into the precise position for this to work — but doesn't compete with the vehicle's ability to shoot the same turn, since real hull-down tanks fought from that position, they didn't just hide in it.

   **Example:** A Tiger stops at a ridge crest and spends 1 AP declaring Hull-Down facing the enemy-held low ground beyond it, then spends a second AP firing its main gun at a target across that same crest — both actions legal in the same turn.

**17.6b.2**  While Hull-Down, every Gunnery Roll (Rule 18.1a) against this vehicle from an attacker on the low side of the declared hexside resolves as a Turret hit automatically — skip Rule 18.1a.5's Hull/Turret split entirely for such a shot. Attacks from any other direction are unaffected.

.. container:: rule-guide

   **Why:** Models the real protection hull-down positioning provides — the hull is physically behind the crest and cannot be struck from that direction at all, not merely somewhat protected — by removing the Hull option from the roll rather than adding a cover modifier that a strong enough shot could still overcome.

   **Example:** An enemy tank below the crest fires at a Hull-Down vehicle and, whatever the Gunnery Roll would otherwise indicate, the shot resolves against Turret AV — Hull AV is simply not in play from that direction while the position holds.

**17.6b.3**  Hull-Down is lost the instant the vehicle moves or pivots (Rule 17.5.4) — it must be re-declared the next time the vehicle is stationary at a qualifying crest hexside.

.. container:: rule-guide

   **Why:** Ties the position to the vehicle's actual physical stance rather than letting it persist as a standing bonus, since the moment the vehicle moves it is no longer sitting in the exact spot that made the position work.

   **Example:** A Hull-Down vehicle that repositions one hex to react to a flanking threat loses Hull-Down immediately — even though it moved for good tactical reasons, it must find and declare a new qualifying position before the protection applies again.

17.7  Hit Location
-------------------


**17.7.1**  Vehicles with a Hit Location Table printed (Tiger I Ausf E and Sherman M4A1 (75mm), this edition — see Rule 18.6a) resolve MOB kill vs. GUN kill by roll rather than free choice, for Front-arc hits only — this edition's tables cover only that arc. Side- and Rear-arc hits on these vehicles, and all hits on vehicles without a printed Hit Location Table, continue to use the owning player's judgement call (Rule 17.1.1) until a table covering that arc is built.

.. container:: rule-guide

   **Why:** Rolls out actual hit-location tables incrementally, starting with just two representative vehicles and only their Front arc, rather than waiting to cover the whole roster at once — every other case falls back to the owning player's judgment (Rule 17.1.1) until more tables are built, so the game is always fully playable even with partial coverage.

   **Example:** A Tiger I hit in its Front arc rolls against its printed Hit Location Table to determine MOB kill versus GUN kill; a hit on that same Tiger's Side arc, or a Casualty result against any vehicle without a printed table at all, still uses the owning player's own judgment call instead.

**17.7.2**  The table gives one **Neither Threshold** and one **Mobility Threshold** per profile (Hull, Turret), printed on the player aid card — a single pair of numbers, valid at every range and for every attacker. The split is conditional on the shot having already hit the profile (the Gunnery Roll settled that), and where a confirmed hit lands on a plate is governed by the plate's own geometry, not by how hard the shot was to make — so range, attacker crew quality, and attacker identity all drop out. An infantry AT penetration (Panzerfaust, Rule 18.9) rolls against the same two thresholds.

.. container:: rule-guide

   **Why:** Keeps the hit-location roll to just two universal thresholds per profile, since once a shot has already confirmed a hit on a specific plate (Gunnery Roll already resolved that), exactly where on that plate the damage lands depends only on the plate's own internal layout — not on anything about how the shot got there, so range and attacker details are irrelevant to this specific roll.

   **Example:** A Tiger's Hull profile has one Neither Threshold and one Mobility Threshold that apply identically whether the confirmed hit came from a close-range tank gun or a Panzerfaust at point-blank range — the roll against those same two numbers doesn't change based on who or what fired.

*Read: roll below the Neither Threshold — Neither (Casualty downgrades to Pinned, Rule 18.6a.2). Roll at or above the Mobility Threshold — MOB kill. Between the two — GUN kill. A profile with no printed Mobility Threshold (e.g. a turret with no mobility-critical systems) can never produce a MOB kill. See* ``hit_location_output.csv`` *for the computed values.*
