Section 18 — Vehicle Combat Resolution
======================================

Vehicle combat uses a dedicated resolution sequence that determines whether a round penetrates armour and what damage results. The sequence integrates with the existing fire resolution system — the same dice, the same result bands, the same graduated damage philosophy.

18.1  Resolution Sequence Overview
----------------------------------


**18.1.1**  When a weapon fires at a vehicle, resolve in this order:

**18.1.2**  Step 1: Gunnery Roll. Roll to determine whether the round hits the target at all and, if so, whether it strikes the Hull or Turret profile. See Rule 18.1a. **If the result is a Miss, resolution ends here — the round has no further effect.**

**18.1.3**  Step 2: Determine arc. Identify whether the attacker is in the target's front, side, or rear arc **of whichever profile (Hull or Turret) the Gunnery Roll selected in Step 1.** Use the corresponding AV value from that profile — AV-vs-Capped or AV-vs-Tungsten, matching the ammunition nature fired (Rule 17.2.3).

**18.1.4**  Step 3: Check TRAV. Confirm target vehicle's TRAV rating allows it to be engaged this turn. If TRAV is insufficient to cover the attacker's hex, the vehicle cannot return fire this impulse.

**18.1.5**  Step 4: Calculate effective PEN at range — read the printed PEN line for the ammunition nature fired at the actual range band (Rule 17.3.1).

**18.1.6**  Step 5: Check Shatter Gap and Schürzen if applicable (Rules 18.2a, 18.2b — optional/situational), then compare effective PEN to target AV and determine penetration outcome (Rule 18.2).

**18.1.7**  Step 6: Apply result using the vehicle damage table.

18.1a  Gunnery Roll
--------------------


**18.1a.1**  Every vehicle-mounted gun counter prints a Gunnery Table: a Miss Threshold and a Hull Threshold for each range band, already calculated for that vehicle's own Crew Quality (Rule 18.1a.2). No separate lookup, chart, or calculation is required at the table — read the row for the actual range.

*Example (88mm KwK36, Regular crew — the actual computed rows from* ``vehicle_fire_thresholds_output.csv``):*

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Range**
     - **Result**
   * - 100m
     - Roll < 12: Miss. Roll 12–13: Turret. Roll ≥ 14: Hull.
   * - 250–500m
     - Roll < 12: Miss. Roll 12–14: Turret. Roll ≥ 15: Hull.
   * - 750m
     - Roll < 13: Miss. Roll 13–15: Turret. Roll ≥ 16: Hull.
   * - 1000m
     - Roll < 16: Miss. Roll 16–17: Turret. Roll ≥ 18: Hull.
   * - 1500m
     - Roll < 21: Miss. Roll 21: Turret. Roll ≥ 22: Hull.
   * - 2000m
     - Roll < 25: Miss. Roll 25: Turret. Roll ≥ 26: Hull.
   * - 2500m+
     - Automatic miss. No roll required.


**18.1a.1a**  Blank thresholds: a band with no printed Miss Threshold is an **automatic miss** (the shot is beyond the dice combination's resolution floor). A band with a Miss Threshold but no Hull Threshold means every hit at that range strikes the **Turret** — at extreme range only the taller profile presents. The Gunnery Table prints its own band set (typically 100/250/500/750/1000/1500/2000/2500m); the PEN lines use Rule 17.3.1's bands — the two are read independently.


**18.1a.2**  Crew Quality is derived from the firing vehicle's own Morale value (Rule 17.3.6): Morale 7+ = Elite, Morale 6 = Veteran, Morale 5 = Regular, Morale 3–4 = Green, Morale 2 or less = Militia. This is fixed at counter-design time, not chosen or looked up during play.

**18.1a.3**  Roll 1d6+1d8+1d12 (the same combination used for every other fire attack, Rule 8.5.1) and compare to the Miss Threshold and Hull Threshold for the actual range to target, using the next lower printed range band if the exact range falls between two listed bands.

**18.1a.4**  If the roll is below the Miss Threshold, the round misses. No further resolution — the round has struck terrain, passed over the target, or otherwise failed to connect.

**18.1a.5**  If the roll meets or exceeds the Hull Threshold, the round strikes the target's Hull profile. If the roll is at or above the Miss Threshold but below the Hull Threshold, the round strikes the Turret profile instead. Proceed to Rule 18.1.3 using the indicated profile. Casemate vehicles (TRAV 0, no separate turret) always resolve against Hull regardless of roll — see Rule 17.1.2.

**18.1a.6**  Crossing target: if the target vehicle has a MOVED marker this turn and the attacker's line of fire falls in the target's Side arc, read the Gunnery Table one range band longer than the actual range (e.g. a shot at 750m against a crossing target uses the 1000m row instead).

**18.1a.7**  Follow-up shot: if the firing unit's previous fire action this turn targeted the same vehicle and the firing unit has not moved since, read the Gunnery Table one range band shorter than the actual range (minimum: the shortest printed band). If both Rule 18.1a.6 and 18.1a.7 apply to the same shot, apply the crossing adjustment first, then the follow-up adjustment, to the resulting band.

**18.1a.8**  A Gunnery Roll is not required for anti-infantry fire (Rule 18.8), infantry anti-tank weapons (Rule 18.9), or Overrun (Rule 18.11) — those retain their existing resolution procedures unchanged.

**18.1a.9**  Rule 6.6.7's existing −2 rFP penalty for opportunity fire against a moving target does not stack with Rule 18.1a.6 when the target is a vehicle — the Gunnery Roll's own crossing-target adjustment replaces it for vehicle targets specifically. Rule 6.6.7 continues to apply exactly as written when the target is infantry.

*NOTE: The Gunnery Roll reuses the exact 1d6+1d8+1d12 combination already rolled for every other attack in the game rather than introducing new dice. Below the dice combination's resolution floor (rarer than about 0.17%, the probability of rolling the single maximum value), a shot is an automatic miss rather than requiring an unrollable threshold.*

*NOTE: The crossing-target and follow-up-shot adjustments (18.1a.6–18.1a.7) trade some numerical precision for reusing the same printed table under all circumstances — no second table, no arithmetic, no die-roll modifier to remember.*

18.2  Penetration Outcomes
--------------------------


Compares effective PEN (Rule 17.3.1) against the AV of the profile and arc selected by the Gunnery Roll (Rule 18.1a).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **Outcome**
     - **Proceed to**
   * - Effective PEN ≥ AV + 10
     - Automatic penetration — no roll needed
     - Full penetration damage table
   * - Effective PEN ≥ AV
     - Contested — roll 1d6
     - Penetration roll table
   * - Effective PEN < AV
     - Non-penetrating hit — roll 1d6
     - Non-penetrating hit table
   * - Effective PEN < AV − 10
     - Bounce — no effect
     - No further resolution


*NOTE: the ±10mm margins restore the width the outcome bands had before the millimetre migration (the original ±3 was in the old 1-point≈10mm scale and was never rescaled — a 6mm total window against PEN values that move 8–10mm per range band made nearly every matchup a binary auto-penetration or bounce, and Rules 18.3/18.4 almost never fired). ±10mm is comparable to real penetration scatter at these armour thicknesses and keeps the Contested and Non-penetrating bands live at exactly the ranges where engagements were historically uncertain.*


18.2a  Shatter Gap (Optional Rule)
----------------------------------


*If this module is in use for the scenario:*

**18.2a.1**  Before applying Rule 18.2, check Shatter Gap if all of the following hold: (a) the firing ammunition is Capped, Uncapped AP, or Soviet APBC nature (not Tungsten/APDS, not HEAT); (b) the attacking gun's printed calibre (mm) does not exceed the target's AV in the profile/arc being hit.

*NOTE: condition (b) is a deliberate at-table simplification of the sourced eligibility ratio (shatter applies from T/D ≥ 0.8, i.e. calibre up to 1.25× AV). The simplified test exempts a narrow band of shots the source says could shatter (e.g. an 88mm gun against an 80mm plate); the calculation tool implements the full ratio — see* ``shatter_gap_failure`` *in* ``counters/armor_calc/formulas.py``.*

**18.2a.2**  If 18.2a.1's conditions hold, look up the target's AV on the Shatter Gap Table (player aid card) to find its Shatter Window — a lower and upper PEN value.

**18.2a.3**  If effective PEN falls within the Shatter Window (inclusive), the shot is forced to a Non-Penetrating Hit (Rule 18.4), regardless of what Rule 18.2 would otherwise indicate. Proceed directly to 18.4 — do not consult 18.2 or 18.3 for this shot.

**18.2a.4**  If effective PEN falls outside the Shatter Window (either below it, or above it), resolve normally via Rule 18.2 — Shatter Gap does not apply.

*NOTE: This can only ever make an otherwise-favorable shot worse, never better — it has no effect on shots where PEN < AV already.*

18.2b  Schürzen (Standoff Skirt Armour)
----------------------------------------


**18.2b.1**  A vehicle counter with a Schürzen marker on a given Hull or Turret Side arc has standoff skirt armour protecting that arc against HEAT specifically.

**18.2b.2**  Before comparing effective PEN to AV (Rule 18.2), if the attack (a) uses HEAT ammunition of any kind — gun-fired HEAT round, Panzerfaust, Bazooka, PIAT — and (b) targets a Side arc bearing a Schürzen marker, halve the attacking weapon's effective PEN (round down) before proceeding.

**18.2b.3**  Schürzen has no effect on Capped, Uncapped AP, Soviet APBC, or Tungsten/APDS attacks, and no effect on any arc other than the marked Side arc.


18.3  Contested Penetration Roll
--------------------------------


**18.3.1**  When effective PEN equals or exceeds AV but is less than AV + 3, roll 1d6:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
     - **Proceed to**
   * - 1–2
     - Bounce — round deflects
     - No further resolution
   * - 3–4
     - Partial penetration
     - Partial penetration damage table
   * - 5–6
     - Full penetration
     - Full penetration damage table


18.4  Non-Penetrating Hit
-------------------------


**18.4.1**  A round that strikes but cannot penetrate may still affect the crew through spalling, concussion, and psychological shock. Roll 1d6:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1–4
     - No effect — round bounces harmlessly
   * - 5–6
     - Crew shock — vehicle Suppressed


18.5  Partial Penetration Damage
--------------------------------


**18.5.1**  A partially penetrating round causes significant crew disturbance and possible damage. Roll 1d6:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1–2
     - Crew shock — vehicle Suppressed
   * - 3–4
     - Crew pinned — vehicle Pinned (buttoned up)
   * - 5–6
     - Component damage — vehicle Casualty (owning player chooses MOB or GUN kill)


18.6  Full Penetration Damage
-----------------------------


**18.6.1**  A fully penetrating round enters the crew compartment and causes serious damage. Roll 1d6 and apply modifiers:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Modified Roll**
     - **Result**
   * - 1
     - Crew shock — vehicle Suppressed
   * - 2–3
     - Crew pinned — vehicle Pinned (buttoned up)
   * - 4–5
     - Component damage — vehicle Casualty
   * - 6+
     - Catastrophic kill — vehicle Eliminated


**18.6.1a**  A natural 6 on the damage roll is always a Catastrophic kill, regardless of modifiers. A round inside the fighting compartment can find ammunition or fuel no matter how experienced the crew — negative modifiers shift the odds, they do not confer immunity.

*NOTE: without this rule, the veteran-crew modifier (-1) made Elimination arithmetically impossible for any gun under 88mm firing non-HEAT ammunition at a veteran-crewed vehicle (maximum modified roll 5) — a Sherman 76, T-34/85, or SU-85 could never destroy a German vehicle outright, while historically 75mm-class penetrations brewed up tanks routinely. The natural-6 floor gives every full penetration a minimum 1-in-6 chance of a kill.*

**18.6.2**  Full penetration modifiers applied to the damage roll:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **Modifier**
   * - HEAT warhead (Panzerfaust, PIAT, Bazooka, HEAT round)
     - +1
   * - Large calibre round (88–120mm)
     - +1
   * - Very large calibre round (122mm+)
     - +2
   * - Crew quality veteran or elite
     - -1 (experienced crew better at surviving hits)
   * - Vehicle already damaged (on rear face)
     - +1


18.6a  Hit Location
--------------------


**18.6a.1**  Whenever Rule 18.5.1 or 18.6.1 produces a "Component damage — vehicle Casualty" result, roll 1d6+1d8+1d12 (the same combination used for every other attack, Rule 8.5.1) against the target vehicle's own Hit Location Table (Rule 17.7) for the profile that was hit (Hull or Turret, per the Gunnery Roll's own determination, Rule 18.1a — Hull for infantry AT weapons, Rule 18.9). One threshold pair per profile covers every range and attacker.

**18.6a.2**  If the roll is below the Neither Threshold, the hit landed somewhere non-critical — downgrade the result from Casualty to Pinned (Rule 18.7) instead. The round penetrated, but nothing essential was destroyed.

**18.6a.3**  If the roll is at or above the Mobility Threshold, the hit is a MOB kill. If the roll is at or above the Neither Threshold but below the Mobility Threshold, the hit is a GUN kill.

**18.6a.4**  This rule applies only to Front-arc hits on vehicles whose Hit Location Table has actually been built (Tiger I Ausf E and Sherman M4A1 (75mm), this edition) — this edition's tables cover only that arc. Side- and Rear-arc hits on these vehicles, and all hits on any other vehicle, use Rule 17.1.1's owning-player judgement call instead.

*NOTE: This can only ever make an outcome different from what free choice would have picked — it has no effect on whether a Casualty occurs in the first place (Rule 18.5/18.6 are unchanged), only on which specific outcome follows one. A hit that resolves to "Neither" is a real, sourced consequence of this system, not an edge case being carved out: it reflects that not every penetrating hit finds something critical to destroy.*


18.7  Vehicle Damage States
---------------------------


**18.7.1**  Vehicle damage states mirror infantry status bands for system consistency:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **State**
     - **Infantry equivalent**
     - **Effect on vehicle**
   * - Suppressed (crew shock)
     - Suppressed
     - Fires at -20 PEN (mm) and -2 rFP. Moves at half M#. Bail-out check each Recovery Phase.
   * - Pinned (buttoned up)
     - Pinned
     - MG only at -4. Cannot move. -2 OBS. Cannot spot hidden units. -1 morale checks. Bail-out check each Recovery Phase.
   * - Casualty — MOB KILL
     - Casualty (rear face)
     - M0. Can still fire all weapons. Flip counter to MOB KILL rear face.
   * - Casualty — GUN KILL
     - Casualty (rear face)
     - MG only. Can still move at full M#. Flip counter to GUN KILL rear face.
   * - Eliminated
     - Broken
     - Vehicle destroyed. Counter removed to BROKEN zone.


18.8  Anti-Infantry Fire
------------------------


**18.8.1**  Vehicles fire against infantry using their MG fire line or HE capability. Both use standard fire resolution (Section 8) against infantry Defence values.

**18.8.2**  MG fire: uses MG rFP ⬡h -f notation, resolves against infantry defence + cover. The standard close-range bonuses apply: +3 rFP at range 0 (same hex, Rule 8.9.2), +2 rFP at range 1 (adjacent, Rule 8.9.1).

**18.8.3**  HE fire: uses the flat HE rFP value. No falloff — HE effectiveness is constant regardless of range. Cover modifier applies but is reduced by 1 step (same as mortar indirect fire against buildings and reverse slopes).

**18.8.4**  HE rFP derivation formula (resolved in spreadsheet): HE rFP = round(gun calibre in mm / 20). Examples: 37mm = 2, 75mm = 4, 88mm = 4, 105mm = 5, 122mm = 6.

**18.8.5**  Fire against vehicles as soft targets: open-topped vehicles (the ○— symbol, Rule 17.1) and unarmoured (soft) vehicles can be attacked by HE, MG/small-arms fire (range 0–1 only), mortar blast (Rule 16.7.8), and grenades as if they were infantry, using a class Defence value — no per-vehicle stat is printed:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Vehicle class**
     - **Defence vs soft-target fire**
   * - Truck / soft vehicle
     - 6
   * - Open-topped armoured vehicle (○—)
     - 8


A Casualty result or better eliminates a soft vehicle; against an open-topped armoured vehicle it is a vehicle Casualty (Rule 18.6a applies if a table exists, else Rule 17.1.1).

**18.8.6**  HE direct fire against a **closed** AFV never rolls on the penetration tables: resolve one roll on the Non-Penetrating Hit table (Rule 18.4), at +1 for guns of 105mm and larger — blast and concussion can suppress a crew but not open the tank. Damage to closed AFVs comes only through AP/HEAT penetration (Rule 18.2), overrun (18.11), Molotovs (18.10), and engineer attacks (Section 21).

18.9  Infantry Anti-Tank Weapons
--------------------------------


Infantry AT weapons do not use the Gunnery Roll (Rule 18.1a.8) — they always hit if fired within range and resolve directly against the target's Hull profile (front arc of engagement).

*[ TBD: Penetration values below are preliminary. Verify against primary sources before treating as final. ]*

**Decided: infantry AT weapons do not get a Gunnery Roll.** Three reasons, not just one: (1) these weapons are already deliberately designed around a range constraint, not an accuracy constraint (Appendix E.42) — Panzerfaust's flat, always-penetrating PEN value is a considered choice modelling "the operator must close to suicidally short range to guarantee a kill," and a hit/miss roll on top of that would blunt the exact tension the weapon is built around; (2) the vehicle Gunnery Roll's thresholds were calibrated against real data (Appendix 17's British O.B. Investigation No.659 study) — no comparable calibration data exists for infantry-fired AT weapons, so any hit-probability figure here would be invented, not sourced, unlike everything else this session has added; (3) these are already single, climactic, high-stakes actions (an exposed AT gunner takes one shot) — layering a second roll on top adds bookkeeping without a clear payoff for the moment it represents.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Weapon**
     - **PEN**
     - **Range**
     - **Notes**
   * - Rifle (all types)
     - 0
     - —
     - No AT capability
   * - LMG / HMG
     - 10 mm
     - 0–1 hex
     - Light vehicles only at point blank
   * - AT rifle (Boys, PzB 39)
     - 30 mm, −10 per 2 hexes beyond hex 1
     - 0–8 hex
     - Light armour only — ineffective vs medium tanks
   * - Panzerfaust 30
     - 140 mm (flat)
     - 0–2 hex
     - Hard range limit. Single shot — EXPENDED strip placed after use.
   * - Panzerfaust 60
     - 140 mm (flat)
     - 0–4 hex
     - Hard range limit. Single shot — EXPENDED strip placed after use.
   * - Panzerfaust 100
     - 140 mm (flat)
     - 0–6 hex
     - Hard range limit. Single shot — EXPENDED strip placed after use.
   * - Panzerschreck (RPzB 54)
     - 120 mm (flat)
     - 0–6 hex
     - Reloadable HEAT — flat PEN inside the hard range limit.
   * - PIAT
     - 100 mm (flat)
     - 0–6 hex
     - British. Reloadable HEAT — flat PEN inside the hard range limit.
   * - Bazooka M1A1
     - 90 mm (flat)
     - 0–8 hex
     - US. Reloadable HEAT — flat PEN inside the hard range limit.
   * - AT grenade bundle
     - 40 mm (flat)
     - 0 hex
     - Same hex only — close assault.
   * - Magnetic mine (Hafthohlladung)
     - 60 mm (flat)
     - 0 hex
     - Engineer unit required. Same hex only.
   * - Molotov cocktail
     - Special
     - 0–1 hex
     - Rear arc only. Engine fire on 4–6. See Rule 18.10.


*NOTE: PEN values in this table are 0°-equivalent millimetres, the same scale as every AV and gun PEN in the game (the pre-migration point values, 1 point ≈ 10mm, appeared here unconverted through v0.9.2 — under which every weapon on this list bounced off every vehicle in the roster). The HEAT weapons' accuracy degradation is modelled entirely by their hard range limits (Rule 17.3.3), not by a falloff on PEN — the old "-1 rFP per 2 hexes" notes were left over from a resolution path these weapons no longer use.*


**18.9.1**  EXPENDED strip: when a single-shot AT weapon is fired, place an EXPENDED strip over the weapon band on the infantry counter. The band is covered for the remainder of the scenario. The strip is a reusable component — same width as all support weapon bands.

**18.9.2**  Panzerfaust, Bazooka, and PIAT are HEAT weapons for the purposes of Rule 18.2b (Schürzen) — halve their effective PEN against a Side arc bearing a Schürzen marker, same as any other HEAT attack.

18.10  Molotov Cocktail
-----------------------


**18.10.1**  The Molotov cocktail can only target the engine deck — rear arc only, range 0-1 hex.

**18.10.2**  On landing: roll 1d6. On 1-3: no effect (fire suppressed or misses engine). On 4-6: engine fire — vehicle Pinned immediately.

**18.10.3**  Each subsequent Recovery Phase while engine fire is active: roll 1d6. On 1-3: crew extinguishes fire — remove Pinned status. On 4-5: fire continues — vehicle remains Pinned. On 6: fire spreads — roll on the Full Penetration Damage table (Rule 18.6.1) with a +1 modifier; its full range of outcomes (Suppressed through Eliminated) applies.

18.11  Overrun
--------------


Overrun's pre-entry defensive fire does not use the Gunnery Roll (Rule 18.1a.8) — resolved as described below instead. **Decided, and simpler than it first appeared**: this was never really an independent design fork. Pre-entry defensive fire is infantry firing AT weapons at the approaching vehicle (Rule 18.9's domain), which doesn't use the Gunnery Roll at all per that rule's own decision above — Overrun's exemption follows directly from it, not as a separate choice. The vehicle's simultaneous MG fire at the infantry was already outside the Gunnery Roll's scope too (Rule 18.1a.8 exempts anti-infantry fire generally, Rule 18.8). There is no point in Overrun's resolution where a vehicle fires at another vehicle, so there was never a real occasion for the Gunnery Roll to apply here in the first place.

**18.11.1**  A vehicle may declare an overrun when moving into a hex occupied by enemy infantry. The vehicle must have sufficient MP remaining to enter the hex.

**18.11.2**  Pre-entry defensive fire: before the vehicle enters the hex, the defending infantry may spend 1 RP to fire AT weapons at the approaching vehicle. This is resolved at range 1 (adjacent). Vehicle fires MG simultaneously at infantry.

**18.11.3**  After pre-entry fire resolves, the defending infantry must pass a morale check at threshold 5 or immediately rout.

**18.11.4**  If infantry routs: vehicle enters hex unopposed.

**18.11.5**  If infantry holds: vehicle enters hex. Both sides are now in the same hex. Close combat continues each subsequent impulse — infantry fires AT weapons at range 0, vehicle fires MG at range 0. No cover modifiers apply. Range 0 bonus (+3 rFP) applies to the vehicle MG. Both sides resolve simultaneously.

**18.11.6**  Vehicle withdrawal from overrun hex: costs the vehicle's full remaining M# to exit. The vehicle is considered to have used its entire activation withdrawing.

18.12  Historical Matchup Verification
--------------------------------------


**Re-run against the current system, following the game's own reading procedure.** Each matchup reads PEN at the next lower printed range band exactly as Rule 17.3.1 directs players to (an earlier revision of this table computed PEN at exact ranges — a procedure the players never use — which produced three verdicts the table itself would contradict at the table), applies the ±10mm outcome margins of Rule 18.2, and checks against **both** the target's Hull and Turret AV-vs-Capped independently — the single blended "Front AV" this table originally validated no longer exists as a concept. Panzerfaust rows use the flat 140mm PEN now printed in Rule 18.9 (the direct millimetre conversion of the original system's flat "PEN 14", not a re-sourced value); infantry AT weapons resolve against Hull only, never Turret (no Gunnery Roll). This table checks penetration outcome only, the same scope the original table had — it does not check Gunnery Roll hit probability, which was separately calibrated against real data during that mechanism's own build (Rule 18.1a).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Matchup**
     - **Range**
     - **Arc**
     - **Hull result**
     - **Turret result**
     - **Historical verdict**
   * - Sherman 75mm vs Tiger I
     - 200 yds
     - Front
     - Bounce
     - Bounce
     - Cannot penetrate — correct ✓
   * - Sherman 75mm vs Tiger I
     - 40 yds
     - Front
     - Bounce
     - Bounce
     - Cannot penetrate at any range — correct ✓
   * - Sherman 75mm vs Tiger I
     - 320 yds
     - Side
     - Contested
     - Contested
     - Penetrates side armour — largely correct, see note (a)
   * - Tiger I 88mm vs Sherman M4A1
     - 600 yds
     - Front
     - Auto penetration
     - Auto penetration
     - Guaranteed kill at this range — correct ✓
   * - Panzer IV H vs T-34 Model 1943
     - 320 yds
     - Front
     - Auto penetration
     - Auto penetration
     - Uncertain results historically — see note (b)
   * - T-34 Model 1943 vs Panzer IV H
     - 400 yds
     - Front
     - Auto penetration
     - Non-penetrating hit
     - Cannot reliably penetrate the turret, hull now vulnerable — see note (c)
   * - T-34 Model 1943 vs Panzer IV H
     - 120 yds
     - Front
     - Auto penetration
     - Contested
     - Can penetrate at close range — correct ✓, more decisively than before
   * - T-34/85 vs Tiger I
     - 400 yds
     - Front
     - Auto penetration
     - Bounce
     - Marginal threat — correct ✓, and now shows *why*: see note (d)
   * - Panzerfaust 60 vs T-34 Model 1943
     - 80 yds
     - Front
     - Auto penetration
     - N/A — resolves vs Hull only (Rule 18.9)
     - Devastatingly effective — correct ✓
   * - Panzerfaust 60 vs Tiger I
     - 80 yds
     - Front
     - Auto penetration
     - N/A — resolves vs Hull only (Rule 18.9)
     - Penetrates all 1943 armour — correct ✓
   * - Sherman 76mm vs Tiger I
     - 400 yds
     - Front
     - Auto penetration
     - Bounce
     - Capable but not guaranteed — correct ✓, and now shows *why*: see note (d)


**Notes on genuine changes from the original (pre-rebuild) table:**

**(a) Sherman 75mm vs Tiger I side, 320 yds** — the original table called this "Auto penetration." Under the band-read procedure (320 yds ≈ 293m reads the 250m row: PEN 84.1mm) against AV 80.1mm (both Hull and Turret side share the figure), the shot clears AV by 4mm — inside the ±10mm Contested window of Rule 18.2. "Penetrates side armour" is still the correct story, just "very likely, roll needed" rather than "guaranteed."

**(b) Panzer IV H vs T-34 Model 1943, 320 yds** — the most substantive change. The original table called this "Contested," matching a "results were historically uncertain" narrative. The rebuilt KwK40 L48 gun curve — fitted to 5 independent historical data points at <1.2% error, the highest-confidence curve in the roster — puts PEN at 126.8mm against a 93.7mm Hull AV and 55.8mm Turret AV: a comfortable, unambiguous Automatic Penetration against both profiles, not a coin-flip. This is not obviously a regression: the long-barrelled 75mm L48 (KwK40) on the Panzer IV H was specifically prized by German crews for being able to reliably defeat T-34 frontal armour at real combat ranges, unlike the earlier short-barrelled 75mm it replaced — arguably the rebuilt system's more decisive result is the more historically accurate one, and the original "uncertain" calibration may have undersold the L48's real capability. Flagged for Rod's own judgement rather than silently resolved either way.

**(c) T-34 Model 1943 vs Panzer IV H, 400 yds** — the original table called this "Non-penetrating" outright. The rebuilt system splits it: Hull is now Automatic Penetration (PEN 74.9mm vs. Hull AV 64.9mm), Turret remains a clean Bounce (vs. 78.9mm). The Hull figure dropped from the original system's blended AV specifically because of this session's face-hardened-armour work (Rule 17.2, §17 of the design spec) — Panzer IV H's hull front and side were historically face-hardened, and face-hardening is a *liability* against capped rounds once the attacking cap protects the round's nose from the shattering mechanism face-hardening relies on. **Resolved**: the Soviet 76mm F-34's BR-350A round was flagged as a possible `ap_uncapped` candidate (Russian ammunition is often generally described as lacking AP caps) — checked directly against Woodman's "Tank Armament in World War Two" table (the same source already calibrating this gun's own curve), which explicitly labels this exact round "Sov 76mm APC" (Armor-Piercing **Capped**). The general "Russian ammunition lacked caps" claim appears to describe older ammunition (the plain BR-350, fired from 1930s-era 76.2mm guns) rather than the improved "A"-suffix BR-350A the wartime F-34 actually fired. `ammo_family=capped` stands as correctly sourced, not merely assumed — this matchup's numbers are unchanged.

**(d) T-34/85 vs Tiger I (400 yds) and Sherman 76mm vs Tiger I (400 yds)** — both originally called "Contested"/"marginal"/"not guaranteed." The rebuilt system reveals *why* that framing was historically right, in a way the old blended AV couldn't show: the Hull is a clean Automatic Penetration in both cases, while the Turret (Tiger's real, edge-effect-derived 143mm mantlet figure, Rule 17.2's Ch.10 data) is a clean Bounce. "Not guaranteed" was never about any single shot being marginal against its own target — it was always about *which profile* the shot would land on, which is exactly what the Gunnery Roll (Rule 18.1a) now resolves explicitly instead of burying it inside one averaged number.

**Extended coverage: the five vehicles the original table never tested.** The original 11 matchups only ever exercised Tiger I, Panzer IV H, T-34 (both marks), and both Shermans. Panther, KV-1S, SU-85, T-70, and StuG III had never been checked against a historical matchup at all. Extending the same methodology:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Matchup**
     - **Range**
     - **Arc**
     - **Hull result**
     - **Turret result**
     - **Historical verdict**
   * - Sherman 75mm vs Panther
     - 200 yds
     - Front
     - Bounce
     - Bounce
     - Correct ✓ — Panther's frontal invulnerability to the standard Sherman 75mm is one of the best-documented facts of the 1944 tank war
   * - Sherman 76mm vs Panther
     - 200 yds
     - Front
     - Bounce
     - Bounce
     - Correct ✓ — the upgunned Sherman's M62 APC (123.5mm) closes the gap considerably but still falls well short of Panther's ~230-250mm glacis/mantlet, consistent with accounts that 76mm Shermans still generally could not beat Panther frontally
   * - Panther vs Sherman M4A1
     - 800 yds
     - Front
     - Auto penetration
     - Auto penetration
     - Correct ✓ — and notably still an automatic kill at long range (800yds), matching the KwK42 L70's reputation for out-ranging Allied tank guns entirely
   * - Panzer IV H vs T-70
     - 500 yds
     - Front
     - Auto penetration
     - Auto penetration
     - Correct ✓ — unsurprising given T-70's thin armour, included mainly to confirm the light-tank case behaves as expected at both profiles
   * - T-70 vs Panzer IV H
     - 200 yds
     - Front
     - Contested
     - Bounce
     - Plausible ✓ — see note (e); T-70's 45mm APBC has only a contested chance against the glacis at point-blank and cannot beat the turret at its own small calibre
   * - KV-1S vs Panzer IV H
     - 300 yds
     - Front
     - Auto penetration
     - Non-penetrating hit
     - Plausible ✓ — see note (f)
   * - Panzer IV H vs KV-1S
     - 500 yds
     - Front
     - Auto penetration
     - Non-penetrating hit
     - Plausible ✓ — see note (f); KV-1S's hull was thinned relative to the original KV-1 for speed, but its turret protection was largely retained (band-read PEN 128.4 vs turret AV 129.1 — a rattling near-miss, not a clean deflection)
   * - SU-85 vs Tiger I
     - 400 yds
     - Front
     - Auto penetration
     - N/A — casemate, no turret
     - Correct ✓ — SU-85 was specifically fielded to give Soviet forces a weapon that could threaten German heavies at moderate range
   * - SU-85 vs Panther
     - 300 yds
     - Front
     - Bounce
     - N/A — casemate, no turret
     - Correct ✓ — SU-85's 85mm could not reliably beat Panther's glacis frontally at any practical range, a documented limitation that led to the later SU-100
   * - StuG III vs T-34 Model 1943
     - 500 yds
     - Front
     - Auto penetration
     - N/A — casemate, no turret
     - Correct ✓ — StuG III's long 75mm made it one of the most effective German tank-killers of the war, consistent with a decisive result at moderate range
   * - T-70 (weakest gun in roster) vs Sdkfz 251
     - 1000 yds
     - Front
     - Auto penetration
     - N/A — open-top, no turret
     - Correct ✓ — the weakest gun in the roster, at unusually long range, still trivially defeats the half-track's 14.3mm armour. Included only to confirm the last untested roster vehicle behaves as expected; no real ambiguity to resolve here


**(e) T-70 vs Panzer IV H — a real methodology bug caught and fixed during this extension, not a subtle judgement call.** The first pass of this matchup compared T-70's 45mm APBC gun against Panzer IV's `av_vs_capped_mm` roster column — which would have been wrong. That column bakes in the face-hardening correction for a **Capped**-family attacker (Rule 17.2.3) specifically; T-70's 45mm fires Soviet APBC ammunition, an entirely different nose shape, for which face-hardening does not apply the same way (`face_hardened_multiplier("apbc") = 1.0`, a documented gap — no correction rather than a wrong one). Recomputing Panzer IV's front plates for a 45mm APBC attacker (bypassing the mismatched column, and at the attacker's own calibre rather than the roster's 75mm reference diameter) gives Hull 83.9mm and Turret 106.6mm — against a band-read PEN of 86.3mm (200 yds reads the 0m row), a Contested Hull shot and a clean Turret Bounce under the ±10mm margins. **Fixed since this table was first written.** `VehiclePlateRow.resolve_av()` in `counters/armor_calc/pipeline.py` was hardcoded to the Capped family — it now takes an explicit `family` parameter (defaulting to "capped", so `write_roster_csv`'s printed columns are unaffected). A future matchup or validation script needing the correct AV for an APBC or uncapped-AP attacker should call `resolve_av(diameter, hardness_table, family="apbc")` directly rather than reading `av_vs_capped_mm` off the roster CSV. The printed counter still shows only two AV columns (vs. Capped, vs. Tungsten) — APBC and uncapped AP remain rare enough as attacker families that a third and fourth printed column isn't warranted, consistent with the "least granular means necessary" design principle (§2) — but the underlying tool can no longer silently give a wrong answer when one is actually needed for a specific check. Regression tests cover the family parameter in `tests/test_pipeline.py`.

**(f) KV-1S matchups borrow gun curves, not vehicle-specific ones.** KV-1S historically mounted the 76.2mm ZIS-5 gun, not the F-34 this table uses — but ZIS-5 is a direct evolution of F-34 with closely comparable ballistic performance, and no separate ZIS-5 curve has been fitted in this roster. Similarly, SU-85's 85mm D-5S gun is modelled using the T-34/85's D-5T curve — the same gun family, tank- vs. self-propelled-mounted. StuG III's matchup uses Panzer IV's KwK40 curve directly, which is not an approximation — StuG III Ausf G by this point mounted the identical 7.5cm StuK 40 L/48. These substitutions are reasonable but unverified against separately-sourced data for the specific gun models named — flagged rather than presented as equally certain to the guns with their own fitted curves.
