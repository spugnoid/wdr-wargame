Section 10 — Unit Status
========================

10.1  Status Levels
-------------------


Units may be in one of the following status levels at any time. Status is tracked with markers placed on the counter.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Status**
     - **Movement**
     - **Fire**
     - **Reaction**
     - **Defence**
   * - Normal
     - Full M#
     - Full F#
     - Full
     - Normal
   * - Suppressed
     - Half M# (round down)
     - At -2 rFP
     - At -1 rFP
     - -2
   * - Pinned
     - No movement
     - At -4 rFP
     - Cannot react
     - -3
   * - Routing
     - D3 hexes away from enemy per activation
     - Cannot fire
     - Cannot react
     - -3
   * - Broken
     - N/A — counter removed
     - N/A
     - N/A
     - N/A
   * - Dispersed
     - N/A — counter on Casualty Track, DISPERSED marker in hex
     - N/A
     - N/A
     - N/A


10.2  Suppressed
----------------


**10.2.1**  A Suppressed unit has its movement halved, fires at -2 rFP, and reacts at -1 rFP.

**10.2.2**  A Suppressed unit's effective Defence is reduced by 2.

**10.2.3**  Suppressed status is removed during the Recovery Phase if the unit passes a recovery roll (Rule 5.2.4) or a leader successfully rallies it (Section 12).

**10.2.4**  A Suppressed unit that receives a second Suppressed result is upgraded to Pinned.

10.3  Pinned
------------


**10.3.1**  A Pinned unit cannot move and fires at -4 rFP.

**10.3.2**  A Pinned unit cannot spend RP for opportunity fire or other reactions.

**10.3.3**  A Pinned unit's effective Defence is reduced by 3.

**10.3.4**  Pinned status is removed during the Recovery Phase if the unit passes a recovery roll at threshold 10 (Rule 5.2.4).

**10.3.5**  A Pinned unit that receives a Suppressed result remains Pinned (Pinned is worse than Suppressed; the result is absorbed).

10.4  Broken
------------


**10.4.1**  A Broken unit has been rendered Combat Ineffective. Its counter is removed from the map and placed in the BROKEN zone of the Casualty Track.

**10.4.2**  A unit may become Broken through two distinct paths:

**10.4.3**  Physical break — the unit takes a final Casualty result while already on its rear face. Place a red CI cause marker in the unit's Casualty Track slot.

**10.4.4**  Psychological break — the unit fails a morale check (see Section 15). Place a white CI cause marker in the unit's Casualty Track slot.

**10.4.5**  A Broken unit is placed face up if it was at full strength when broken, face down if it was on its rear face.

**10.4.6**  A Broken unit may not be rallied during the current scenario. It is available for between-scenario recovery rolls with a +1 bonus if the CI cause marker is white (psychological break).

10.5  Dispersed
---------------


**10.5.1**  A Dispersed unit has been rendered Combat Ineffective by close assault or melee morale failure. Its counter moves immediately to the DISPERSED zone of the Casualty Track in its current state — front face up if full strength when dispersed, rear face up if reduced.

**10.5.2**  A serialised DISPERSED marker (e.g. GER-01, SOV-02) is placed in the hex where the unit was dispersed. The matching numbered box on the Casualty Track holds the unit's counter, linking map marker to counter unambiguously.

**10.5.3**  The DISPERSED marker is not a combat unit. It cannot fire, move, or react. It exists solely to indicate that men are physically present in that hex.

**10.5.4**  A Dispersed unit that is not captured may attempt to rally during the Recovery Phase: roll 1d6 + Morale - 2 vs threshold 8. On success, the counter returns to play at rear face (reduced strength) in the hex of the friendly RALLY POINT marker with the fewest hexes between it and the hex where this unit's own DISPERSED marker sits (Rule 12.6a), or in the hex where the DISPERSED marker was if no friendly RALLY POINT marker exists anywhere on the map. The DISPERSED marker is removed from its hex either way. On failure, the counter is removed from the Casualty Track permanently for this scenario and the marker is also removed.

    *See also: Rule 12.6a (Rally Point Action).*

**10.5.5**  An enemy unit that occupies or is adjacent to a DISPERSED marker may spend 1 AP to formally capture it (see Section 11).

10.6  Routing
-------------


**10.6.1**  A routing unit is one that has failed a morale check and has a clear escape path. It has not yet left the map but is fleeing and no longer combat effective.

**10.6.2**  Place a ROUTING marker on the unit. The unit remains on the map as a counter.

**10.6.3**  A routing unit must move D3 hexes directly away from the nearest visible enemy unit each time it is activated. Movement follows the most cover-heavy route available.

**10.6.4**  A routing unit cannot fire, cannot react, and cannot be used for any action except movement.

**10.6.5**  A routing unit that reaches the friendly map edge is removed from the map and placed in the BROKEN zone of the Casualty Track with a white CI cause marker.

**10.6.6**  A routing unit that reaches a hex containing a functional friendly leader may attempt an immediate rally: roll 1d6 + Morale vs leader RAL value. Success removes the ROUTING marker and the unit resumes normal status. Failure — the unit continues routing.

**10.6.7**  During the Recovery Phase, routing units may attempt to rally at threshold 12 (roll 1d6 + Morale ≥ 12). A leader within command radius adds their CMD rating to this roll. Without a leader, a regular unit (Morale 5) rallies from rout only on a roll of 6 — routed troops rarely recover themselves; leaders bring them back.

**10.6.8**  A routing unit counts toward the force's CI total for Force Morale purposes (see Section 15.4).

10.7  Combat Ineffective
------------------------


**10.7.1**  The term Combat Ineffective (CI) refers collectively to units in Broken or Dispersed status. Routing units count as CI for Force Morale purposes but remain on the map.

**10.7.2**  A CI result does not necessarily mean the unit's personnel are all killed. Historically, approximately 25% of WWII infantry casualties were killed in action; the remainder were wounded, captured, or dispersed. A CI counter represents a unit that has ceased to function as a tactical element, not a pile of corpses.

**10.7.3**  CI units are tracked on the Casualty Track and may return to play through between-scenario recovery rolls depending on the Recovery Window (Section 13). Psychological breaks (white marker) recover at +1 to the roll.
