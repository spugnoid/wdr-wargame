Section 17 — Vehicles: Counter Design and Movement
==================================================

Vehicles in With Deepest Regret... are represented by individual counters at tactical scale (one counter = one vehicle) and section counters at operational scale (one counter = 3-5 vehicles). The same counter design serves both scales — scenario rules define which resolution mode applies.

*Vehicle AV, PEN, and Gunnery Table values are computed by the project's calculation tool (*`counters/armor_calc/`*) from sourced ballistics data (Rule 17.2.5, 17.3.7) and cross-checked against a historical-matchup table covering the full roster (Rule 18.12) — not hand-derived placeholders. See that tool's own README and* `docs/superpowers/specs/2026-07-04-armored-combat-penetration-physics-design.md` *for the full sourcing and validation detail, including the roster's own known gaps (e.g. no British guns modelled yet).*

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

**17.1.2**  Casemate vehicles (TRAV 0 — no separate turret) print only Hull armour values, which apply regardless of which "profile" Rule 18.1a's Gunnery Roll would otherwise indicate. There is no Hull/Turret hit allocation for these vehicles.

17.2  Armour Values
-------------------


**17.2.1**  Armour Values (AV) represent effective armour protection in millimetres, already resolved at design time to a 0°-equivalent figure (slope angle, cast/rolled deficiency, high-hardness deviation, documented flaws, and face-hardening are all folded in before the number is printed). Players never apply slope or material-quality modifiers at the table — the printed AV is final.

**17.2.2**  Every vehicle counter with a separate turret (TRAV 1 or higher) prints **two independent profiles** — Hull and Turret — each with its own Front/Side/Rear AV. Which profile a shot resolves against is determined by the Gunnery Roll (Rule 18.1a), not chosen by the attacker. Casemate vehicles (TRAV 0) print Hull values only (Rule 17.1.2).

**17.2.3**  Each arc of each profile prints **three AV values**: AV-vs-Capped (for APC/APCBC rounds), AV-vs-Tungsten (for HVAP/APCR/APDS rounds), and AV-vs-HEAT (for all shaped-charge attacks — Rule 17.2.4). Uncapped and capped kinetic rounds have measurably different slope sensitivity, tungsten rounds lose relative effectiveness faster as impact angle increases, and HEAT ignores velocity entirely — one number cannot represent them all.

**17.2.3a**  Uncapped AP and Soviet APBC attackers also use the AV-vs-Capped value — **except** against face-hardened plates (marked FH on the counter), where the printed Capped figure bakes in a correction that applies to capped noses only. Against the roster's face-hardened plates, an APBC or uncapped-AP attacker uses these values instead:

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

**17.2.5**  AV, PEN, and the Gunnery Table are all computed by the project's calculation tool (`counters/armor_calc/`) from sourced ballistics data, not derived by formula at the table. See that tool's own documentation for the full physics — nothing beyond the printed numbers is needed to play.

**17.2.6**  Slope, material quality, hardness, and flaw corrections are all already resolved into the printed AV (Rule 17.2.1) — there is no separate step for players to apply any of them.

**17.2.7**  HEAT Reference Table — designer reference only (the multipliers from which the printed AV-vs-HEAT values are computed; never consulted during play):

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
     - 1.15
   * - 45°
     - 1.41
   * - 60°
     - 2.00
   * - 75°
     - 3.86


**17.2.8**  Shatter Gap (optional/advanced rule) and Schürzen (standoff skirt armour vs. HEAT) are covered in Rules 18.2a and 18.2b respectively — both apply after the AV comparison above, not as part of it.

17.3  Penetration Values
------------------------


**17.3.1**  Penetration values (PEN) are printed as 0°-equivalent millimetres at a small set of range bands (typically 0/250/500/750/1000/1500/2000m), not as a single value with falloff notation. Read the row for the actual range to target, using the next lower printed band if the exact range falls between two listed bands — a shot at less than 250m reads the 0m (point-blank) row.

**17.3.2**  A gun prints one PEN line per ammunition nature it historically carried — Capped, Uncapped AP, or Tungsten (HVAP/APCR/APDS) — up to two or three lines. The firing player freely chooses which loaded nature to fire with each shot, tracked via the extended-ammunition mechanism (Rule 16.3.3) for any premium (Tungsten) rounds: the scenario states the vehicle's base Tungsten load; past it, roll the extended table per shot.

**17.3.3**  HEAT weapons (Panzerfaust, PIAT, Bazooka, HEAT rounds) have flat penetration values — no range bands. Their accuracy degrades with range through hard range limits (Rule 18.9), not through penetration reduction.

**17.3.4**  Compare the PEN value for the actual range and chosen ammunition nature against the target's AV-vs-Capped or AV-vs-Tungsten (matching the ammunition fired) on the profile and arc selected by the Gunnery Roll (Rule 18.1a) — see Rule 18.2.

**17.3.5**  Gunnery Table — every vehicle-mounted gun also prints a Gunnery Table: a Miss Threshold and a Hull Threshold for each range band, already resolved for that gun's own vehicle's Crew Quality. Rule 18.1a covers how to read and roll against it — no calculation is required at the table.

**17.3.6**  Crew Quality is derived from the firing vehicle's own Morale value and fixed at counter-design time: Morale 7+ = Elite, Morale 6 = Veteran, Morale 5 = Regular, Morale 3–4 = Green, Morale 2 or less = Militia.

**17.3.7**  PEN, AV, and Gunnery Table values are computed by the project's calculation tool from sourced ballistics data (velocity-at-range, slope multipliers by ammunition nose shape, and the flight-time-based hit-probability model) — not derived by formula at the table.

17.4  Traverse Rating
---------------------


**17.4.1**  Traverse rating (TRAV) determines how many hexsides a vehicle's gun can cover from its current facing in one fire action. All TRAV arcs are contiguous and centred on the facing arrow — no choice of which hexsides are covered is required. (TRAV arcs govern where the gun can shoot; armour facing arcs, Rule 17.5.2, govern which AV an incoming shot strikes. The two are independent.)

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

**17.4.3**  Between fire actions in the same turn, the turret is assumed to return to forward facing. A vehicle with TRAV 1 that fires left cannot immediately fire right in the same turn — it must fire forward or wait until next turn.

**17.4.4**  Casemate vehicles (TRAV 0) cannot rotate the gun independently. To engage targets outside the front hex, the entire vehicle must pivot. Each 60° of vehicle pivot costs 1 additional MP on top of normal pivot cost.

17.5  Vehicle Facing
--------------------


**17.5.1**  Vehicle facing is tracked by orienting the counter's printed facing arrow toward one of the six hex sides of the vehicle's current hex.

**17.5.2**  Facing arcs are the six 60° wedges of the map radiating from the vehicle's hex, one per hexside, extended to **any range** — each wedge contains the adjacent hex through that hexside and every hex beyond it in that sixth of the map:

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

*NOTE: a 60° front means oblique fire at any range strikes SIDE armour — positioning and facing matter at 1,000 yards as much as at 40. The historical-matchup table (Rule 18.12) states its engagements as head-on (attacker in the FRONT wedge); an attacker manoeuvred onto a flank uses the Side AVs, which is the point.*


**17.5.3**  When a vehicle moves, its facing changes to match the direction of movement unless the player explicitly declares a pivot.

**17.5.4**  Pivot without moving: costs 1 MP per 60° of rotation. A vehicle pivoting from facing north to facing east (120° turn) costs 2 MP.

**17.5.5**  TRAVERSED marker: when a turreted vehicle fires at a target outside its hull's front hexside — i.e. the shot requires the turret to traverse away from the hull's facing arrow, within its TRAV rating (Rule 17.4) — place a TRAVERSED marker on the vehicle, oriented toward the engaged hexside. This shows the turret's actual current facing, independent of the hull's facing arrow.

While a TRAVERSED marker is present, any attack resolving against this vehicle's **Turret** profile (per Rule 18.1a's Gunnery Roll) determines its arc relative to the TRAVERSED marker, not the hull's facing arrow. Attacks resolving against the **Hull** profile always use the hull's facing arrow, regardless of the TRAVERSED marker.

The marker is removed the instant the vehicle takes another fire action this turn (replaced by a new one if that shot also requires an off-forward traverse), and in any case is removed at the Recovery Phase along with all other action markers — consistent with Rule 17.4.3 (turret returns to forward facing between fire actions).

Casemate vehicles (TRAV 0) never receive a TRAVERSED marker; they have no separate turret profile.

17.6  Vehicle Movement
----------------------


**17.6.1**  Vehicle movement allowances:

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

**17.6.2b**  Reverse movement: a vehicle may back directly into the hex behind it (its rear-wedge adjacent hex) without changing facing, at **double** the terrain's MP cost per hex. This is how a casemate tank destroyer disengages without exposing its side or rear armour.

**17.6.3**  Vehicle LOS: vehicles are larger than infantry. Any unit with LOS to a vehicle's hex automatically has LOS to the vehicle through up to 2 hexes of light woods or 1 hex of dense woods. Normal LOS rules apply beyond these limits.

17.7  Hit Location
-------------------


**17.7.1**  Vehicles with a Hit Location Table printed (Tiger I Ausf E and Sherman M4A1 (75mm), this edition — see Rule 18.6a) resolve MOB kill vs. GUN kill by roll rather than free choice, for Front-arc hits only — this edition's tables cover only that arc. Side- and Rear-arc hits on these vehicles, and all hits on vehicles without a printed Hit Location Table, continue to use the owning player's judgement call (Rule 17.1.1) until a table covering that arc is built.

**17.7.2**  The table gives one **Neither Threshold** and one **Mobility Threshold** per profile (Hull, Turret), printed on the player aid card — a single pair of numbers, valid at every range and for every attacker. The split is conditional on the shot having already hit the profile (the Gunnery Roll settled that), and where a confirmed hit lands on a plate is governed by the plate's own geometry, not by how hard the shot was to make — so range, attacker crew quality, and attacker identity all drop out. An infantry AT penetration (Panzerfaust, Rule 18.9) rolls against the same two thresholds.

*Read: roll below the Neither Threshold — Neither (Casualty downgrades to Pinned, Rule 18.6a.2). Roll at or above the Mobility Threshold — MOB kill. Between the two — GUN kill. A profile with no printed Mobility Threshold (e.g. a turret with no mobility-critical systems) can never produce a MOB kill. See* ``hit_location_output.csv`` *for the computed values.*
