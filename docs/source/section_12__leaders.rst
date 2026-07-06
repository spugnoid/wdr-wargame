Section 12 — Leaders
====================

Leaders represent squad leaders, platoon commanders, and company officers. They are the command and control layer of the game. A force with good leaders fights as a coordinated unit; a force without them degrades into independent elements that suppress, stall, and break.

12.1  Leader Counter Design
---------------------------


Leader counters use a diamond symbol (◆) and display four stats in addition to Morale and Defence:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Stat**
     - **Notation**
     - **Description**
   * - Command
     - CMD ●●●
     - Command rating 1–3 shown as filled dots. Drives AP contribution and command radius.
   * - Observation
     - OBS 1–3
     - Observation rating. Added as bonus to spot rolls when leader is present.
   * - Rally threshold
     - RAL #
     - Target number for mid-turn rally rolls. Lower is better.
   * - Assault bonus
     - ASL +#
     - Added to attacker's grenade rFP during close assault when leader is in hex.


All leaders have M3 F1 — movement allowance 3, fire rate 1. Leaders move faster than squads (lighter load, higher initiative) and rarely fire directly.

12.2  Command Rating and Radius
-------------------------------


**12.2.1**  A leader's CMD rating (1–3) determines both their AP contribution and their command radius — the area within which they can affect friendly units.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **CMD**
     - **Quality**
     - **AP Contribution**
     - **Command Radius**
     - **Typical Role**
   * - 1
     - Poor / inexperienced
     - +0 AP
     - 1 hex (adjacent only)
     - Junior NCO, replacement officer
   * - 2
     - Regular
     - +1 AP
     - 2 hexes
     - Squad leader, platoon sergeant
   * - 3
     - Veteran / elite
     - +2 AP
     - 3 hexes
     - Platoon commander, company officer


**12.2.2**  At 40 yards per hex, CMD 3 radius = 120 yards — consistent with historical effective voice communication range in combat.

**12.2.3**  Elite leaders use CMD 3 but are distinguished by superior RAL, ASL, and OBS values rather than a separate CMD tier.

12.3  Action Point Generation
-----------------------------


**12.3.1**  Total AP per turn is calculated as:

**AP = 1 (base) + Σ CMD ratings of all functional leaders**

**12.3.2**  RP = round(AP / 2), minimum 1. This formula is unchanged from Section 5.3.

**12.3.3**  A side with no functional leaders has AP = 1. One activation per turn — the minimum needed to prevent complete paralysis.

**12.3.4**  Example: German platoon with one CMD 3 platoon leader and two CMD 2 squad leaders: AP = 1 + 3 + 2 + 2 = 8, RP = 4.

**12.3.5**  A wounded or eliminated leader immediately reduces the AP pool for the remainder of the turn.

12.4  Command Radius and Out of Command
---------------------------------------


**12.4.1**  A unit is in command if at least one friendly functional leader has that unit within their command radius.

**12.4.2**  A unit with no friendly leader in command radius is out of command. Out of command effects:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Effect**
     - **Modifier**
   * - Morale checks
     - -1
   * - Recovery rolls
     - -1
   * - Rally action
     - Not available — no leader present
   * - Fire coordination bonus
     - Not available
   * - Assault bonus
     - Not available


**12.4.3**  Out of command units still activate normally using AP. They fight but fight less effectively and recover more slowly.

12.5  Leader Actions
--------------------


When a leader is activated (costs 1 AP), they may take one of the following actions:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Action**
     - **Effect**
     - **Range**
   * - Move
     - Leader moves up to M3 hexes following terrain movement costs.
     - N/A
   * - Direct Fire
     - Add CMD rating as bonus rFP to one fire group this impulse. Applied after falloff and terrain, before Resolution Strip.
     - Command radius
   * - Rally
     - One Suppressed or Pinned unit attempts mid-turn recovery at RAL threshold instead of standard threshold. See Rule 12.6.
     - Command radius
   * - Rally Point
     - Places a RALLY POINT marker in the leader's current hex — a rally destination for Dispersed units. See Rule 12.6a.
     - Current hex
   * - Coordinate Assault
     - Add ASL value to assaulting unit's grenade rFP for the Grenade Phase. Does not apply to Entry Fire or Melee Continuation.
     - Same hex as assaulting unit
   * - Spot
     - Leader takes Spot Action. Adds OBS to all spot rolls this turn. May attempt free spot rolls against all hidden markers in LOS.
     - LOS range
   * - Inspire
     - One adjacent unit gains one extra fire action this turn beyond its normal F#. Represents sustained fire under direct leadership pressure.
     - Adjacent hex only


12.6  Rally Action
------------------


**12.6.1**  A leader spending 1 AP on Rally selects one Suppressed or Pinned unit within command radius. That unit immediately attempts a recovery roll outside the normal Recovery Phase.

**12.6.2**  The unit rolls 1d6 + Morale and compares to the leader's RAL value (not the standard threshold).

**12.6.3**  If the roll meets or exceeds the RAL value, the unit recovers from its current status.

**12.6.4**  RAL values by leader quality:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **CMD / Quality**
     - **RAL Value**
     - **Effect**
   * - CMD 1 / Poor
     - 5
     - Suppressed recovery harder than standard; Pinned unchanged
   * - CMD 2 / Regular
     - 4
     - Same as standard suppressed threshold
   * - CMD 3 / Veteran
     - 3
     - Suppressed automatic for Morale 4+; Pinned frequently succeeds
   * - CMD 3 / Elite
     - 2
     - Near-automatic suppressed recovery; Pinned usually succeeds


12.6a  Rally Point Action
-------------------------


**12.6a.1**  A leader spending 1 AP places a RALLY POINT marker in their current hex. A leader may have only one active RALLY POINT marker at a time — placing a new one removes any previous RALLY POINT marker placed by that same leader.

**12.6a.2**  A RALLY POINT marker is not tied to the leader's continued presence or survival — it remains a valid marker on the map even if the placing leader later moves away, becomes a casualty, or is removed from play.

**12.6a.3**  A RALLY POINT marker, once placed, remains a valid destination for the rest of the scenario regardless of subsequent events in that hex, including enemy occupation.

    *See also: Rule 10.5.4 (Dispersed units rally to the nearest RALLY POINT marker, not necessarily where they dispersed).*

**12.6a.4**  If two or more RALLY POINT markers are equally nearest (measured in hexes from the hex where the Dispersed unit's own DISPERSED marker currently sits) when Rule 10.5.4 is resolved, the owning player chooses which one applies.

12.7  Direct Fire Coordination
------------------------------


**12.7.1**  A leader spending 1 AP on Direct Fire adds their CMD rating as bonus rFP to one fire group within command radius.

**12.7.2**  The bonus is applied to the summed effective rFP after range falloff and terrain modifiers, before the Resolution Strip lookup. It participates in strip compression along with the rest of the group's rFP.

**12.7.3**  Multiple leaders cannot stack fire coordination bonuses on the same fire group in the same impulse. The highest single CMD bonus applies.

**12.7.4**  A hidden leader cannot Direct Fire — command requires visible presence to coordinate a fire group effectively.

12.8  Assault Coordination
--------------------------


**12.8.1**  When a leader is in the same hex as an assaulting unit and spends 1 AP on Coordinate Assault, the leader's ASL value is added to the attacker's grenade rFP for the Grenade Phase only.

**12.8.2**  ASL values by leader quality:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Quality**
     - **ASL**
     - **Notes**
   * - Poor
     - +0
     - No assault benefit
   * - Regular
     - +1
     - Moderate improvement
   * - Veteran
     - +1
     - Same value — quality shows in other stats
   * - Elite
     - +2
     - Significant assault enhancement


**12.8.3**  The ASL bonus does not apply to Entry Fire or Melee Continuation phases — those are too chaotic for direct officer coordination.

12.9  Leader Casualties
-----------------------


**12.9.1**  When a hex containing a leader takes a Casualty result or worse, the owning player rolls 1d6 to determine who was hit:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1–2
     - Leader hit — apply result to leader counter
   * - 3–6
     - Subordinate hit — owning player applies result to a non-leader unit in the hex of their choice


**12.9.1a**  Exception: a Casualty result produced by sniper deliberate targeting (Rule 20.2) applies directly to the named target. No allocation roll is made.

    *See also: Rule 20.2 (Sniper Deliberate Targeting)*

**12.9.2**  If the leader is hit, flip the leader counter to its wounded rear face. A wounded leader continues to function but at reduced effectiveness.

**12.9.3**  If the hex contains only the leader (no subordinate units), the leader is automatically hit — no roll needed.

12.10  Wounded Leaders
----------------------


**12.10.1**  The rear face of a leader counter represents a wounded officer. Wounded leaders apply the following stat reductions:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Stat**
     - **Change on Rear Face**
   * - CMD
     - -1 (minimum 1)
   * - OBS
     - -1 (minimum 1)
   * - RAL
     - +2 (higher threshold, harder to rally)
   * - ASL
     - -1 (minimum 0)
   * - Defence
     - -2
   * - Morale
     - Unchanged


**12.10.2**  A wounded leader that takes another Casualty result or worse: roll 1d6. On 1–3 the leader is eliminated and moved to the BROKEN zone of the Casualty Track. On 4–6 the leader is captured or evacuated and moved to the DISPERSED zone.

**12.10.3**  Leader elimination has immediate effect — AP pool drops from the next impulse onward. The remaining leaders must compensate or the force becomes seriously degraded.

12.11  Representative 1943 Leader Counters
------------------------------------------


The following counters are provided for the 1943 Eastern Front test scenarios:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit**
     - **CMD**
     - **OBS**
     - **RAL**
     - **ASL**
     - **Morale**
     - **Defence**
   * - German Platoon Leader (Veteran) — GREN PLT 43
     - 3
     - 2
     - 3
     - +1
     - 7
     - 6
   * - German Squad Leader (Regular) — GREN SL 43
     - 2
     - 2
     - 4
     - +1
     - 6
     - 6
   * - Soviet Platoon Leader (Regular) — RIF PLT 43
     - 2
     - 2
     - 4
     - +1
     - 6
     - 6
   * - Soviet Guards Platoon Leader (Veteran) — GDS PLT 43
     - 3
     - 2
     - 3
     - +1
     - 7
     - 6


*NOTE: German leaders in 1943 generally rated higher than Soviet counterparts due to the superior German NCO training system. By 1944-45 this gap narrowed significantly as Soviet experience accumulated. Year-bracket leader counters reflect this progression.*
