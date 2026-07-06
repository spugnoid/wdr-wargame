Section 15 — Morale Break and Rout
==================================

Most WWII engagements ended not with one side physically eliminated but with one side's morale collapsing. Units that absorbed more stress than they could sustain broke psychologically — stopping their advance, fleeing their positions, or simply ceasing to function as fighting elements. This section models that process at both the unit and force level.

15.1  Unit Morale Check Triggers
--------------------------------


**15.1.1**  A unit must make a morale check when any of the following triggers occur:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Trigger**
     - **Break Threshold**
     - **Notes**
   * - Receives Casualty + Suppressed result
     - 7
     - Step loss under sustained fire
   * - Pinned for a second consecutive turn
     - 6
     - Prolonged suppression without relief
   * - Adjacent friendly unit becomes CI or begins Routing
     - 5
     - Witnessing comrades break
   * - Leader in same hex is eliminated
     - 6
     - Loss of command and cohesion
   * - Any of the above while already Suppressed
     - Threshold -2
     - Compounding stress


**15.1.2**  Multiple triggers in the same impulse require only one morale check, at the lowest (hardest) threshold among all triggers.

**15.1.3**  A unit in Normal status that has not fired or moved this turn adds +1 to its morale check roll — steadiness under fire.

15.2  Morale Check Procedure
----------------------------


**15.2.1**  Roll 1d6 and add the unit's Morale value. Compare to the break threshold.

**15.2.2**  If the roll meets or exceeds the threshold: the unit holds. No effect. The check is resolved and discarded.

**15.2.3**  If the roll is below the threshold: the unit breaks. Determine whether the result is a Break or a Rout (see Rule 15.3).

**15.2.4**  A leader within command radius of the checking unit adds their CMD rating to the morale check roll.

15.3  Break vs Rout
-------------------


**15.3.1**  When a unit fails a morale check, determine the result based on the unit's situation:

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

**15.3.3**  Rout result: ROUTING marker placed on unit counter. Unit remains on map. See Section 10.6 for routing unit rules.

15.4  Cascade Effect
--------------------


**15.4.1**  When a unit Breaks or begins Routing, every friendly unit within 2 hexes that has LOS to the breaking unit's hex must immediately make a cascade morale check.

**15.4.2**  Cascade morale check threshold: 5.

**15.4.3**  Roll 1d6 + Morale vs 5. Apply the suppressed modifier if applicable (-2 to threshold = threshold 3 while suppressed). A leader within command radius adds CMD rating to the roll.

**15.4.4**  A veteran unit with Morale 6 rolling minimum (1) scores 7 vs threshold 5 — automatic cascade success. Veteran units are essentially immune to cascade from a single break.

**15.4.5**  A green unit with Morale 3 needs a roll of 2 or higher — usually holds but not certain.

**15.4.6**  The cascade is designed to be survivable in normal circumstances. Its danger is in compounding — multiple simultaneous breaks produce multiple simultaneous cascade checks, and failure probabilities multiply.

**15.4.7**  Cascade checks do not themselves trigger further cascades in the same impulse. Cascade is resolved once per original break event.

15.5  Force Morale
------------------


**15.5.1**  Each force has a Force Morale value calculated at scenario setup:

**Force Morale value = total unit count at scenario start × force factor (round down, minimum 1)**

**15.5.2**  Force factors by quality:

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


**15.5.3**  When the total count of CI units plus routing units reaches the Force Morale value, a Force Morale check is triggered immediately.

**15.5.4**  Force Morale check: roll 1d6 + CMD rating of the highest-rated functional leader still on the map vs threshold 8.

**15.5.5**  If no functional leader remains on the map, roll 1d6 only with no bonus.

**15.5.6**  Success: the force holds. The new Force Morale threshold advances by 1 — the next check triggers when one more unit becomes CI or begins routing. This continues until the force either collapses or the scenario ends.

**15.5.7**  Failure: the force collapses. The scenario ends immediately. All remaining units on the map are considered routing for scenario resolution purposes only — this is a scoring abstraction for determining the victor, not a status change, and does not place a ROUTING marker on any unit or trigger Rule 10.6.9. The opposing force wins.

    *See also: Rule 10.6.9 (capture at scenario end applies only to units with an actual ROUTING marker).*

**15.5.8**  Force Morale checks may trigger multiple times per scenario as the threshold advances. A force that passes early checks can still collapse under sustained attrition.

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
   * - Japan throughout
     - Rarely routed, fanatical holds
     - High Morale, factor 0.2 — threshold almost never reached


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
