Section 15 — Morale Break and Rout
==================================

Most WWII engagements ended not with one side physically eliminated but with one side's morale collapsing. Units that absorbed more stress than they could sustain broke psychologically — stopping their advance, fleeing their positions, or simply ceasing to function as fighting elements. This section models that process at both the unit and force level.

15.1  Unit Morale Check Triggers
--------------------------------


**15.1.1**  A unit must make a morale check when any of the following triggers occur:

.. container:: rule-guide

   **Why:** Fixes a specific, enumerated list of triggers rather than leaving morale checks to referee judgment — every situation serious enough to test a unit's will to keep fighting is named up front, so both players always know exactly when a check is required.

   **Example:** Alpha takes a Casualty result while already Suppressed — that combination is one of the named triggers (Rule 15.1 table), so Alpha must make a morale check against threshold 4, not just continue on as normal.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Trigger**
     - **Break Threshold**
     - **Notes**
   * - Receives Casualty + Suppressed result
     - 4
     - Step loss under sustained fire
   * - Pinned for a second consecutive turn
     - 3
     - Prolonged suppression without relief
   * - Adjacent friendly unit becomes CI or begins Routing
     - 2
     - Witnessing comrades break
   * - Leader in same hex is eliminated
     - 3
     - Loss of command and cohesion
   * - Any of the above while already Suppressed
     - Threshold +2
     - Compounding stress makes the check harder

**15.1.2**  Multiple triggers in the same impulse require only one morale check, at the highest (hardest) threshold among all triggers.

.. container:: rule-guide

   **Why:** Consolidates several simultaneous triggers into one roll rather than stacking multiple separate checks — a unit hit by several bad things at once faces the worst single threshold among them, not a compounding series of rolls for the same impulse.

   **Example:** A unit that both takes a Casualty+Suppressed result (threshold 4) and sees an adjacent friendly unit break (threshold 2) in the same impulse makes only one morale check, at the harder threshold of 4.

**15.1.3**  A unit in Normal status that has not fired or moved this turn adds +1 to its morale check roll — steadiness under fire.

.. container:: rule-guide

   **Why:** Rewards a unit that's been holding still and composed (not yet Suppressed or otherwise degraded, and hasn't spent this turn acting) with a small morale bonus, reflecting that a unit still fully in control of itself is steadier when trouble arrives than one already mid-action.

   **Example:** Alpha in Normal status, having neither fired nor moved yet this turn, gets +1 on a morale check triggered this same turn — the same trigger against a unit that already fired or moved gets no such bonus.

15.2  Morale Check Procedure
----------------------------


**15.2.1**  Roll 1d6 and add the unit's **Morale modifier**. Compare to the break threshold.

.. container:: rule-guide

   **Why:** Uses the same simple roll-plus-modifier-versus-threshold pattern as every other quality check in the game (recovery rolls, rally rolls, Rule 15.2.1a), so morale checks don't need a separate resolution mechanic of their own.

   **Example:** A unit facing a morale check with threshold 3 needs its 1d6 roll plus Morale modifier to reach 3 or better to hold — the same meets-or-exceeds pattern used throughout the rules.

**15.2.1a**  The Morale modifier is the unit's Morale value minus 5. It applies to every 1d6 quality check in these rules — morale checks, recovery rolls, rally rolls, and engineer skill rolls — wherever a rule says "1d6 + Morale modifier".

.. container:: rule-guide

   **Why:** Defines one universal Morale-modifier formula that every quality-based roll across the whole rulebook reuses, so a unit's single Morale value drives its odds consistently everywhere rather than needing separate quality scales for each different kind of check.

   **Example:** A Veteran unit's Morale 6 gives Morale modifier +1 (6 − 5); that same +1 applies whether the roll in question is a morale check, a Recovery Phase roll (Rule 5.2.4), a Rally roll (Rule 12.6.2), or an engineer skill roll (Section 21) — one number, used everywhere.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Quality**
     - **Morale**
     - **Morale Modifier**
   * - Militia
     - 3
     - -2
   * - Green
     - 4
     - -1
   * - Regular
     - 5
     - +0
   * - Veteran / Elite
     - 6
     - +1
   * - Elite specialist (veteran snipers, senior leaders)
     - 7
     - +2


*NOTE: earlier drafts rolled 1d6 + the full Morale value. With Morale spanning only 3–6 and thresholds of 5–7, regular and better troops could never fail most checks — the scale was inert. The modifier form keeps the same quality spread while placing thresholds in honest 1d6 space, where a threshold of 4 means a regular unit holds half the time.*

**15.2.2**  If the roll meets or exceeds the threshold: the unit holds. No effect. The check is resolved and discarded.

.. container:: rule-guide

   **Why:** Makes a successful morale check leave no lingering trace — the unit simply continues on with no marker, no note, no cumulative record — so passing a check is a clean non-event rather than something that needs tracking for later.

   **Example:** A unit that rolls a 5 against a morale threshold of 4 holds and continues its turn exactly as before — nothing about that successful check needs to be remembered or referenced again.

**15.2.3**  If the roll is below the threshold: the unit breaks. Determine whether the result is a Break or a Rout (see Rule 15.3).

.. container:: rule-guide

   **Why:** Treats "the unit breaks" as the umbrella failure outcome that then branches into one of two specific results (Break or Rout) depending on the unit's situation, rather than a single fixed penalty for every failed check.

   **Example:** A unit that fails its morale check doesn't automatically know its fate yet — Rule 15.3's situational table decides whether that failure becomes an in-place Break or a fleeing Rout.

**15.2.4**  A leader within command radius of the checking unit adds their CMD rating to the morale check roll.

.. container:: rule-guide

   **Why:** Lets nearby leadership directly improve a unit's odds of holding together under stress, the same way leadership bonuses apply to recovery rolls (Rule 5.2.6) and rally attempts (Rule 12.6.2) — command presence steadies a unit facing a morale test.

   **Example:** A unit making a morale check with a CMD 2 leader in command radius adds +2 to its 1d6 + Morale modifier roll — meaningfully improving its chance of holding against the threshold.

15.3  Break vs Rout
-------------------


**15.3.1**  When a unit fails a morale check, determine the result based on the unit's situation:

.. container:: rule-guide

   **Why:** Bases the outcome of a failed morale check on the unit's actual physical circumstances rather than a fixed roll or flat rule, since whether a broken unit can plausibly flee at all depends entirely on whether it has somewhere to go.

   **Example:** A unit that fails its morale check while surrounded with no escape path is cornered and collapses in place (Break, Rule 15.3.2); the same failed roll for a unit with open ground behind it instead sends the unit fleeing (Rout, Rule 15.3.3).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Situation**
     - **Result**
   * - Unit is Pinned
     - Break — cannot flee, collapses in place
   * - Unit is in a building or fortification
     - Break — nowhere to flee easily
   * - Unit is surrounded (no clear path away from enemy)
     - Break — cornered
   * - Unit has a clear path away from nearest visible enemy
     - Rout — unit flees


**15.3.2**  Break result: counter removed from map to BROKEN zone of Casualty Track with white CI cause marker. See Rule 10.4.

.. container:: rule-guide

   **Why:** Sends a cornered or trapped unit straight to the BROKEN zone with the psychological-break marker color, since Rule 15.3.1's Break outcomes are specifically the situations where a unit collapses in place rather than fleeing — mechanically identical to the psychological-break path of Rule 10.4.4.

   **Example:** A unit that fails its morale check while Pinned (unable to flee at all) is removed from the map to the BROKEN zone with a white CI cause marker — eligible for the psychological-break recovery bonus (Rule 10.4.6) between scenarios.

**15.3.3**  Rout result: ROUTING marker placed on unit counter. Unit remains on map. See Section 10.6 for routing unit rules.

.. container:: rule-guide

   **Why:** Keeps a Routing unit's counter physically present and trackable on the map, distinct from a Break's complete removal, since Rout specifically represents a unit that still has somewhere to flee to and remains a visible (if combat-ineffective) presence until it escapes, rallies, or is captured (Section 10.6).

   **Example:** A unit that fails its morale check with a clear escape path gets a ROUTING marker and stays on the map, immediately subject to the forced-flight and rally mechanics of Section 10.6, rather than being removed to the Casualty Track outright.

15.4  Cascade Effect
--------------------


**15.4.1**  When a unit Breaks or begins Routing, every friendly unit within 2 hexes that has LOS to the breaking unit's hex must immediately make a cascade morale check.

.. container:: rule-guide

   **Why:** Models the very real psychological effect of watching a nearby unit break — panic is contagious, so witnessing a comrade collapse or flee genuinely tests everyone close enough to see it happen, not just the unit that failed originally.

   **Example:** When Squad Bravo breaks in full view of Alpha two hexes away, Alpha must immediately make its own cascade morale check, even though nothing has directly happened to Alpha itself.

**15.4.2**  Cascade morale check threshold: 2.

.. container:: rule-guide

   **Why:** Sets the cascade threshold deliberately low compared to typical morale-check thresholds (Rule 15.1 table's 2-4), since witnessing a break is a real but usually survivable shock — the cascade is meant to be a mild scare most units shrug off, not a near-guaranteed second failure.

   **Example:** A regular unit (Morale modifier +0) rolling a cascade check against threshold 2 holds on almost any roll except a 1 — the cascade is rarely fatal on its own for a steady unit.

**15.4.3**  Roll 1d6 + Morale modifier vs 2. Apply the suppressed modifier if applicable (+2 to threshold = threshold 4 while suppressed). A leader within command radius adds CMD rating to the roll.

.. container:: rule-guide

   **Why:** Uses the exact same roll-plus-modifier mechanics as an ordinary morale check (Rule 15.2.1), including the same Suppressed-threshold penalty and leader CMD bonus, so cascade checks don't need a separate resolution system of their own.

   **Example:** A unit already Suppressed facing a cascade check rolls against threshold 4 (2 + 2), not the base threshold of 2 — the same compounding-stress penalty (Rule 15.1 table) applies here too.

**15.4.4**  A veteran unit (modifier +1) rolling minimum (1) scores 2 vs threshold 2 — automatic cascade success. Veteran units are immune to cascade from a single break unless suppressed (threshold 4: they then hold on 3+, 67%).

.. container:: rule-guide

   **Why:** Walks through the actual arithmetic to show veteran troops are effectively immune to an ordinary cascade check — even their worst possible roll clears the low threshold — while confirming that immunity has a real limit once Suppressed raises the bar.

   **Example:** As printed: a veteran (modifier +1) rolling the minimum possible 1 on 1d6 still totals 2, exactly meeting the cascade threshold — meaning no roll a veteran unit could make fails an unsuppressed cascade check.

**15.4.5**  A green unit (modifier -1) needs a roll of 3 or higher (67%) — usually holds but not certain. A militia unit (modifier -2) holds on 4+ (50%).

.. container:: rule-guide

   **Why:** Shows how the same low cascade threshold produces meaningfully different odds for lower-quality troops than for veterans (Rule 15.4.4) — the cascade stays survivable for everyone, but green and militia units carry genuine risk that veteran units simply don't.

   **Example:** As printed: a green unit (modifier -1) needs a raw roll of 3+ to clear the cascade threshold of 2 (a 67% chance), while a militia unit (modifier -2) needs a 4+ (a 50% chance) — worse odds than a veteran's guaranteed pass, but still not a coin-flip disaster.

**15.4.6**  The cascade is designed to be survivable in normal circumstances. Its danger is in compounding — multiple simultaneous breaks produce multiple simultaneous cascade checks, and failure probabilities multiply.

.. container:: rule-guide

   **Why:** States the cascade's actual design intent plainly — a single break's cascade is meant to be a manageable scare, but a battlefield where several units break at once creates real compounding danger, since several units are all facing that scare simultaneously and each has its own chance to fail.

   **Example:** One unit breaking near a green squad gives that squad a single cascade check at 67% odds to hold; if two nearby units break in the same impulse, that same green squad might face two separate cascade checks, each an independent chance for its morale to give out.

**15.4.7**  Cascade checks do not themselves trigger further cascades in the same impulse. Cascade is resolved once per original break event.

.. container:: rule-guide

   **Why:** Caps the cascade at one layer to prevent an unbounded chain reaction — if a cascade-failed unit's own break triggered yet another round of cascades in the same impulse, a single initial break could theoretically collapse an entire force in one uncontrollable domino effect.

   **Example:** If Squad Bravo's break triggers a cascade check that Alpha fails (and Alpha itself then breaks), Alpha's break does not trigger a second wave of cascade checks against units near Alpha within that same impulse — the chain stops at one layer.

15.5  Force Morale
------------------


**15.5.1**  Each force has a Force Morale value calculated at scenario setup:

.. container:: rule-guide

   **Why:** Fixes Force Morale as a single number computed once at setup, giving the whole side a collective breaking point that scales with its actual starting size and quality (Rule 15.5.2), separate from any individual unit's own morale checks.

   **Example:** A force's Force Morale value is calculated once when a scenario begins and then used throughout that scenario as the running threshold for how much cumulative loss the whole side can sustain before risking collapse (Rule 15.5.3).

**Force Morale value = total unit count at scenario start × force factor (round down, minimum 1)**

**15.5.2**  Force factors by quality:

.. container:: rule-guide

   **Why:** Scales a force's collective breaking point with its overall quality, using the same force-factor idea across nations and periods (Rule 15.6) so historically brittle or resilient forces come out of the same formula with meaningfully different Force Morale values.

   **Example:** Two 10-unit forces of different quality get different Force Morale values from the same starting size: an Elite force (factor 0.6) gets Force Morale 6, while a Green force (factor 0.3) gets only Force Morale 3 — the Green force can absorb far fewer losses before risking collapse.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Force Quality**
     - **Factor**
     - **Example**
   * - Elite (SS, Guards, Rangers, airborne)
     - 0.6
     - 10 units × 0.6 = Force Morale 6
   * - Veteran regular
     - 0.5
     - 10 units × 0.5 = Force Morale 5
   * - Regular
     - 0.4
     - 10 units × 0.4 = Force Morale 4
   * - Green / conscript / militia
     - 0.3
     - 10 units × 0.3 = Force Morale 3
   * - Mixed quality force
     - Average of all units
     - Calculate per unit, sum, divide by count

*Sourcing note (E.153): Steven J. Zaloga's* US Airborne Divisions in the ETO 1944-45 *(Osprey Battle Orders 25) was read to open a research thread on this project's complete absence of an Airborne/Paratrooper unit type — "airborne" appears in this project only as an exemplar in tables like this one, never as a structured roster row. The book gives real, citable support for parachute infantry specifically (volunteer recruitment, dedicated jump training, a historian's own judgment that "the excellent training and esprit de corps of the paratroopers helped to overcome the shortcomings in the tactics and divisional organization") but is equally explicit that glider infantry within the same airborne divisions were NOT an elite population — no jump training, no jump pay, "little separated the glider infantry... from ordinary infantry." This table's "airborne" exemplar is accurate for parachute infantry specifically but would overstate glider infantry if the two were ever broken out as separate Force Quality entries. No change made to this table — see* ``counters/toe/us_airborne_zaloga_1943.md`` *for full citations.*

**15.5.3**  When the total count of CI units plus routing units reaches the Force Morale value, a Force Morale check is triggered immediately.

.. container:: rule-guide

   **Why:** Uses accumulated losses — CI units plus routing units together — as the trigger for testing the whole force's collective will, since Force Morale is meant to model the cumulative psychological weight of mounting casualties, not any single dramatic event.

   **Example:** A force with Force Morale 5 that has accumulated 3 CI units and 2 routing units (totaling 5) triggers a Force Morale check the instant that fifth unit's status is reached — whether the fifth came from a Break, a Dispersal, or a new Rout makes no difference to the trigger.

**15.5.4**  Force Morale check: roll 1d6 + CMD rating of the highest-rated functional leader still on the map vs threshold 8.

.. container:: rule-guide

   **Why:** Lets the single best surviving leader on the map represent the whole force's remaining command backbone for this one critical roll, rather than averaging or summing every leader — one strong senior officer can meaningfully steady an entire force at this pivotal moment.

   **Example:** A force with a surviving CMD 3 platoon leader and a CMD 1 squad leader uses the higher CMD 3 rating for its Force Morale check roll — the lesser leader's rating doesn't apply here at all.

**15.5.5**  If no functional leader remains on the map, roll 1d6 only with no bonus.

.. container:: rule-guide

   **Why:** Removes any leadership bonus entirely once a force has no functional leader left, reflecting that a completely leaderless force facing a Force Morale check has nothing steadying it at the moment that matters most.

   **Example:** A force whose every leader has been eliminated, evacuated, captured, or is Routing rolls a bare 1d6 against threshold 8 for its Force Morale check — no CMD bonus of any kind applies.

**15.5.6**  Success: the force holds. The new Force Morale threshold advances by 1 — the next check triggers when one more unit becomes CI or begins routing. This continues until the force either collapses or the scenario ends.

.. container:: rule-guide

   **Why:** Ratchets the threshold up by one after every successful check rather than resetting it, so a force that survives one Force Morale check earns no permanent immunity — it must keep holding as losses continue to mount, one more unit at a time.

   **Example:** A force with Force Morale 5 passes its check when the 5th CI/routing unit is reached; the next check now triggers at the 6th such unit, and so on — each pass buys exactly one more unit's worth of breathing room, not a clean slate.

**15.5.7**  Failure: the force collapses. The scenario ends immediately. All remaining units on the map are considered routing for scenario resolution purposes only — this is a scoring abstraction for determining the victor, not a status change, and does not place a ROUTING marker on any unit or trigger Rule 10.6.9. The opposing force wins.

.. container:: rule-guide

   **Why:** Ends the scenario immediately and decisively on a failed Force Morale check, but carefully scopes the "considered routing" language to scoring only — it deliberately avoids actually placing ROUTING markers or triggering the end-of-scenario capture rule (Rule 10.6.9), since the scenario is already over and there's no further play in which real routing mechanics would matter.

   **Example:** A force that fails its Force Morale check loses the scenario immediately; its surviving units are treated as routing purely for determining the victor, but none of them physically gain a ROUTING marker or become subject to capture under Rule 10.6.9, since that rule only applies to units still actually routing when a scenario ends through the normal turn sequence.

    *See also: Rule 10.6.9 (capture at scenario end applies only to units with an actual ROUTING marker).*

**15.5.8**  Force Morale checks may trigger multiple times per scenario as the threshold advances. A force that passes early checks can still collapse under sustained attrition.

.. container:: rule-guide

   **Why:** Reinforces that surviving one or several Force Morale checks doesn't guarantee a force will survive the whole scenario — the advancing threshold (Rule 15.5.6) means sustained losses can eventually produce a failed check even for a force that held firm earlier.

   **Example:** A force might pass its first two Force Morale checks comfortably, but as attrition continues to add CI and routing units, a later check against a higher-CMD-required roll can still fail and collapse the force, even though nothing about that particular loss was unusually severe on its own.

15.6  National Morale Characteristics
-------------------------------------


Morale break behaviour differed significantly by nation and period. These differences are encoded in unit Morale values and force factors rather than special rules. The system produces historically differentiated behaviour without additional rules text.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Nation / Period**
     - **Characteristic**
     - **Encoding**
   * - Germany 1941–42
     - High cohesion, breaks rare
     - High Morale values, factor 0.5
   * - Germany 1944–45
     - More brittle under pressure
     - Reduced Morale values, factor 0.4
   * - USSR 1941
     - Catastrophic rout common
     - Low Morale values, factor 0.25
   * - USSR 1943+
     - Significantly improved
     - Increased Morale values, factor 0.4
   * - US 1944–45
     - Generally steady, good recovery
     - Moderate Morale, factor 0.45
   * - UK 1943–45
     - Steady, professional regular army; later-war infantry replacement quality strained by manpower shortages
     - Moderate Morale, factor 0.45
   * - Japan throughout
     - Rarely routed, fanatical holds
     - High Morale, factor 0.8 — collapse check almost never reached


15.7  Scenario End Conditions
-----------------------------


With the morale break system in place, scenarios may end in four ways:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **End Condition**
     - **Trigger**
     - **Notes**
   * - Force morale collapse
     - One side fails a Force Morale check
     - Most common historical ending
   * - Objective achieved
     - Scenario victory condition met
     - Attacker captures objective, defender holds to turn limit, etc.
   * - Turn limit reached
     - Final turn completed
     - Both sides count VP, scenario designer determines winner
   * - Mutual elimination
     - Both sides reach zero functional units
     - Rare — mutual destruction edge case
