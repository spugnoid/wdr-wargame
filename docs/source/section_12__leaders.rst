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

.. container:: rule-guide

   **Why:** Ties one single stat to two different effects — how much action economy a leader provides and how far their influence reaches — so a better leader is unambiguously better in both respects at once, rather than needing separate ratings for each.

   **Example:** A CMD 3 leader both contributes more AP to the side's pool (Rule 12.3.1) and projects command to units up to 3 hexes away (Rule 12.2 table), while a CMD 1 leader does less of both.

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

.. container:: rule-guide

   **Why:** Grounds the command radius numbers in a real-world constraint — voice range in combat — rather than an arbitrary game balance number, tying back to the tactical-scale yards-per-hex conversion of Rule 2.1.1.

   **Example:** A CMD 3 leader's 3-hex command radius at tactical scale (Rule 2.1.1's 40 yards/hex) works out to about 120 yards — roughly the distance a shouted order could realistically still be heard and obeyed on a real battlefield.

**12.2.3**  Elite leaders use CMD 3 but are distinguished by superior RAL, ASL, and OBS values rather than a separate CMD tier.

.. container:: rule-guide

   **Why:** Caps command radius/AP contribution at CMD 3 rather than adding a higher tier for elite leaders, since real leadership excellence shows up in rally reliability, assault coordination, and observation — not in an ever-larger area of influence.

   **Example:** An elite leader and a veteran leader both have CMD 3 and the same 3-hex radius and AP contribution, but the elite leader's better RAL, ASL, and OBS values (Rule 12.6.4, 12.8.2) make them noticeably more effective in play.

12.3  Action Point Generation
-----------------------------


**12.3.1**  Total AP per turn is calculated as:

.. container:: rule-guide

   **Why:** Restates Section 5.3's AP formula here in the Leaders section with full context on what "functional" means (Rule 12.3.4), since this is where a player actually needs to know which leaders count and why, rather than just the bare arithmetic.

   **Example:** A side with two functional leaders of CMD 2 and CMD 3 calculates AP = 1 + 2 + 3 = 6 for the turn — the same formula introduced in Rule 5.3.3, elaborated here with the leader-specific detail that formula depends on.

**AP = 1 (base) + Σ CMD ratings of all functional leaders**

**12.3.2**  RP = round(AP / 2), minimum 1. This formula is unchanged from Section 5.3.

.. container:: rule-guide

   **Why:** Confirms explicitly that the Leaders section doesn't introduce a separate RP calculation — RP still derives from the same AP total via Rule 5.3.4's formula, keeping the two sections' math consistent rather than risking a subtle divergence.

   **Example:** A side with AP = 6 has RP = round(6 / 2) = 3, using exactly the same round(AP/2) formula regardless of whether that AP came from Section 5.3's base explanation or this section's leader-driven calculation.

**12.3.3**  A side with no functional leaders has AP = 2 while at least 3 unbroken combat units remain (the NCO floor, Rule 5.3.3a), and AP = 1 below that. Losing every leader remains crippling — half or less of a typical led pool — but a platoon does not freeze solid because its officers are down.

.. container:: rule-guide

   **Why:** Repeats Rule 5.3.3a's NCO floor here in leader-specific terms, since this is where a player is actually tracking whether their side still has functional leadership — the floor exists precisely for the moment all of a side's leaders become non-functional.

   **Example:** A side that loses its last functional leader but still has 4 unbroken combat units falls to the NCO floor of AP = 2 rather than collapsing to the bare AP = 1 minimum.

**12.3.4**  **Functional** means: on the map, and not Eliminated, Evacuated, Captured, or Routing. Wounded (rear-face) leaders are functional at their reduced ratings. A Suppressed leader is functional in every respect. A **Pinned** leader still contributes CMD to the AP pool (the command structure exists even while its officer is face-down) but may not take Rally or Leader Actions and does not add CMD to any other unit's rolls until recovered — pinned command does not project.

.. container:: rule-guide

   **Why:** Defines exactly which leader states still count toward AP and command functions, since "functional" is the gatekeeping term used throughout this whole section — a leader can be degraded (wounded, Suppressed, even Pinned) and still contribute something, but several worse states remove the leader from the count entirely.

   **Example:** A wounded leader still contributes their reduced CMD to the AP pool and can still take Leader Actions; a Pinned leader in the same hex still adds CMD to the AP pool but cannot take a Rally action or project CMD to any other unit until the Pin clears.

**12.3.4**  Example: German platoon with one CMD 3 platoon leader and two CMD 2 squad leaders: AP = 1 + 3 + 2 + 2 = 8, RP = 4.

.. container:: rule-guide

   **Why:** Walks the AP/RP formulas of Rules 12.3.1-12.3.2 through a concrete multi-leader example, since real forces often field more than one functional leader at once and it helps to see the summation actually carried out.

   **Example:** As printed: with a CMD 3 platoon leader and two CMD 2 squad leaders all functional, AP = 1 + 3 + 2 + 2 = 8, giving RP = round(8 / 2) = 4.

**12.3.5**  A wounded or eliminated leader immediately reduces the AP pool for the remainder of the turn.

.. container:: rule-guide

   **Why:** Makes leader losses bite immediately rather than waiting until the next turn's AP calculation — a side that loses a leader mid-turn genuinely has less action economy left to spend right then, reflecting the real disruption of losing command mid-fight.

   **Example:** A side calculates AP = 8 at the start of a turn, but if its CMD 3 leader is eliminated partway through, the AP pool immediately drops (per Rule 12.3.1's formula recalculated without that leader) for whatever remains of that same turn — not just from the next turn onward.

12.4  Command Radius and Out of Command
---------------------------------------


**12.4.1**  A unit is in command if at least one friendly functional leader has that unit within their command radius.

.. container:: rule-guide

   **Why:** Defines "in command" as a simple presence check — any functional leader with the unit inside their radius suffices, no need for the "best" leader or a specific assigned commander — so a unit near several leaders only needs one of them to qualify.

   **Example:** A unit within the command radius of a distant CMD 1 leader and a farther-but-still-in-range CMD 3 leader is in command either way — Rule 12.4.1 only needs at least one functional leader's radius to cover it.

**12.4.2**  A unit with no friendly leader in command radius is out of command. Out of command effects:

.. container:: rule-guide

   **Why:** Bundles several small penalties into "out of command" so leaderless units are consistently worse off across morale, recovery, and combat bonuses, rather than any single missing benefit being the whole story — losing leadership coverage costs a unit in multiple, compounding ways.

   **Example:** A unit that drifts outside every friendly leader's command radius suffers -1 on both morale checks and recovery rolls, and loses access to fire coordination, assault bonuses, and Rally entirely — all five effects apply together, not just one.

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

.. container:: rule-guide

   **Why:** Keeps out-of-command status as a penalty rather than a hard lockout — a unit isn't disabled by losing leadership coverage, it's just worse at everything it still does, which matters for how a player weighs advancing units beyond their leaders' reach.

   **Example:** An out-of-command unit can still move, fire, and take other normal actions for its usual AP cost — it just does so at the penalties listed in Rule 12.4.2's table rather than being unable to act at all.

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

.. container:: rule-guide

   **Why:** Gives a leader an active way to fix a status problem right now, at the cost of 1 AP, rather than making a Suppressed or Pinned unit wait for the next Recovery Phase — spending action economy to buy back a unit's effectiveness mid-turn is exactly what leadership should let a player do.

   **Example:** Alpha becomes Pinned mid-turn. A leader within command radius can immediately spend 1 AP on Rally to give Alpha an extra recovery attempt right then, rather than leaving it Pinned until the next Recovery Phase.

**12.6.2**  The unit rolls 1d6 + Morale modifier (Rule 15.2.1a) and compares to a target derived from the leader's RAL value: **RAL − 1** to recover from Suppressed, **RAL + 1** to recover from Pinned.

.. container:: rule-guide

   **Why:** Derives the Rally target from a single leader stat (RAL) with a fixed offset for each status, rather than needing separate RAL values for Suppressed and Pinned — a better (lower) RAL value improves both odds at once, consistent with a single number capturing overall rally skill.

   **Example:** A leader with RAL 4 gives a Suppressed rally target of 3 (4 − 1) and a Pinned rally target of 5 (4 + 1) — one RAL value producing two related but distinct targets.

**12.6.3**  If the roll meets or exceeds the target, the unit recovers from its current status.

.. container:: rule-guide

   **Why:** Uses a plain meets-or-exceeds success condition, the same pattern as the standard Recovery Phase roll (Rule 5.2.4), so Rally doesn't need a different resolution mechanic — only the target number changes based on the leader's RAL.

   **Example:** A unit rolling against a Rally target of 3 recovers on a roll of exactly 3 or higher, just as it would against the standard Recovery Phase threshold of 3 for Suppressed (Rule 5.2 table).

**12.6.4**  RAL values by leader quality. Percentages are for a regular unit (modifier +0); the standard Recovery Phase thresholds for comparison are 3 (Suppressed, 67%) and 5 (Pinned, 33%):

.. container:: rule-guide

   **Why:** Lays the RAL-based Rally odds side by side with the standard Recovery Phase thresholds so a player can see directly whether a given leader's Rally action is actually better than just waiting — a poor leader's Rally can be a worse bet than the automatic roll.

   **Example:** A CMD 1/Poor leader's RAL 5 gives a Suppressed rally target of 4 (50%) — worse than simply waiting for the standard Recovery Phase threshold of 3 (67%) — so spending 1 AP on that leader's Rally for a Suppressed unit is actually a bad trade.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **CMD / Quality**
     - **RAL Value**
     - **Effect**
   * - CMD 1 / Poor
     - 5
     - Suppressed target 4 (50%) — worse than waiting for the Recovery Phase; Pinned target 6 (17%) — cannot reliably rally pinned units
   * - CMD 2 / Regular
     - 4
     - Suppressed target 3 (67%) — the standard threshold, bought mid-turn; Pinned target 5 (33%) — standard
   * - CMD 3 / Veteran
     - 3
     - Suppressed target 2 (83%, automatic for veterans); Pinned target 4 (50%) — frequently succeeds
   * - CMD 3 / Elite
     - 2
     - Suppressed target 1 — automatic for green and better; Pinned target 3 (67%) — usually succeeds


12.6a  Rally Point Action
-------------------------


**12.6a.1**  A leader spending 1 AP places a RALLY POINT marker in their current hex. A leader may have only one active RALLY POINT marker at a time — placing a new one removes any previous RALLY POINT marker placed by that same leader.

.. container:: rule-guide

   **Why:** Limits each leader to one active RALLY POINT marker so establishing a new one is a real choice with a cost — abandoning the old destination — rather than letting a single leader blanket the map with an unlimited number of rally options.

   **Example:** A leader who placed a RALLY POINT marker earlier in the scenario and later moves to a new position and spends 1 AP to place another one removes the first marker automatically — that leader always has at most one active RALLY POINT.

**12.6a.2**  A RALLY POINT marker is not tied to the leader's continued presence or survival — it remains a valid marker on the map even if the placing leader later moves away, becomes a casualty, or is removed from play.

.. container:: rule-guide

   **Why:** Makes a placed RALLY POINT marker a durable, independent piece of battlefield infrastructure rather than something that vanishes if its placing leader is lost — the physical rally point remains useful to Dispersed units even after the leader who established it is gone.

   **Example:** A leader who placed a RALLY POINT marker is later eliminated in combat; that marker still stands and remains a valid rally destination for Dispersed friendly units under Rule 10.5.4.

**12.6a.3**  A RALLY POINT marker is removed immediately, permanently, and without further effect if an enemy unit ever occupies its hex. Otherwise, once placed, it remains a valid destination for the rest of the scenario.

.. container:: rule-guide

   **Why:** Gives an otherwise-permanent RALLY POINT marker exactly one vulnerability — enemy occupation of its hex — so the marker's durability (Rule 12.6a.2) isn't absolute; ground truly has to be held for a rally point to keep working.

   **Example:** A RALLY POINT marker sitting undisturbed in friendly-controlled territory remains valid all scenario, but if an enemy unit later advances into and occupies that exact hex, the marker is removed permanently right then, with no further effect.

    *See also: Rule 10.5.4 (Dispersed units rally to the nearest RALLY POINT marker, not necessarily where they dispersed).*

**12.6a.4**  If two or more RALLY POINT markers are equally nearest (measured in hexes from the hex where the Dispersed unit's own DISPERSED marker currently sits) when Rule 10.5.4 is resolved, the owning player chooses which one applies.

.. container:: rule-guide

   **Why:** Resolves the tie case for Rule 10.5.4's nearest-rally-point rule with a simple player choice rather than an arbitrary tiebreaker, since either equally-near destination is equally valid by the rule's own logic.

   **Example:** A Dispersed unit sits exactly 3 hexes from two different friendly RALLY POINT markers. The owning player picks which of the two the unit rallies to when its Recovery Phase roll succeeds.

12.7  Direct Fire Coordination
------------------------------


**12.7.1**  A leader spending 1 AP on Direct Fire adds their CMD rating as bonus rFP to one fire group within command radius.

.. container:: rule-guide

   **Why:** Gives a leader a direct way to boost a fire attack's raw firepower rather than just improving morale or coordination indirectly, spending the same 1 AP that any other Leader Action costs (Rule 12.5) so it competes with those other options for the leader's turn.

   **Example:** A CMD 2 leader spending 1 AP on Direct Fire adds +2 bonus rFP to a nearby fire group's attack this impulse, on top of whatever effective rFP the firing units already contribute.

**12.7.2**  The bonus is applied to the summed effective rFP after range falloff and terrain modifiers, before the Resolution Strip lookup. It participates in strip compression along with the rest of the group's rFP.

.. container:: rule-guide

   **Why:** Places the leader's bonus at a specific point in the fire-resolution sequence (Rule 8.1) — after the group's own falloff and terrain penalties are already applied, but before Resolution Strip compression — so the bonus behaves exactly like any other contribution to the group's summed rFP, not as a separate late modifier.

   **Example:** A fire group's terrain-and-falloff-adjusted rFP sums to 7 before the leader's CMD 2 bonus; the bonus is added to make 9, and that combined total of 9 (not 7) is what gets looked up on the Resolution Strip (Rule 8.4).

**12.7.3**  Multiple leaders cannot stack fire coordination bonuses on the same fire group in the same impulse. The highest single CMD bonus applies.

.. container:: rule-guide

   **Why:** Caps a fire group's leadership bonus at one leader's worth even if several leaders are in range, preventing a cluster of leaders from compounding an already-large firepower bonus onto a single attack — command coordination has a ceiling per attack.

   **Example:** If both a CMD 2 leader and a CMD 3 leader are in range of the same fire group and both would want to apply Direct Fire to it in the same impulse, only the higher CMD 3 bonus actually applies — the two bonuses don't add together.

**12.7.4**  A HIDDEN leader's command is limited to what silence permits: they contribute CMD to the AP pool (Rule 12.3.1 — planning happens off-map) and add CMD to rolls of units **in their own hex only**. Every other leader function — Direct Fire coordination, Rally, Inspire, Leader Actions, command radius to other hexes, and the Recovery Phase CMD bonus of Rule 5.2.6 for units outside their hex — requires the leader to be VISIBLE: shouting orders across a field reveals the shouter. A hidden leader may reveal voluntarily at the start of any friendly impulse (remove the blind marker) to use these functions.

.. container:: rule-guide

   **Why:** Reconciles the hidden-information system (Section 14) with leader command functions by treating audible commands as inherently revealing — a hidden leader can still plan (AP contribution) and help their own hex quietly, but projecting command outward requires the leader to break cover and become visible.

   **Example:** A HIDDEN leader still contributes their CMD to the side's AP pool and can add CMD to a unit sharing their own hex, but if that leader wants to use Direct Fire on a fire group two hexes away, they must first reveal (removing the blind marker) — silent long-range coordination isn't an option.

12.8  Assault Coordination
--------------------------


**12.8.1**  When a leader is in the same hex as an assaulting unit and spends 1 AP on Coordinate Assault, the leader's ASL value is added to the attacker's grenade rFP for the Grenade Phase only.

.. container:: rule-guide

   **Why:** Requires the leader to physically be in the same hex as the assaulting unit, unlike Direct Fire's command-radius range (Rule 12.7.1) — coordinating a close assault means being right there with the assault, not directing it from a distance.

   **Example:** A leader standing in the same hex as Alpha when Alpha declares a close assault can spend 1 AP on Coordinate Assault to boost Alpha's grenade rFP; a leader two hexes away, even well within command radius, cannot provide this specific bonus.

**12.8.2**  ASL values by leader quality:

.. container:: rule-guide

   **Why:** Scales the assault bonus with leader quality the same way CMD, OBS, and RAL do, but keeps ASL's own scale — where Regular and Veteran share the same value (Rule 12.8.2's table) — reflecting that assault leadership doesn't always track cleanly with the other stats.

   **Example:** A Regular and a Veteran leader both provide the same +1 ASL bonus to a close assault's grenade rFP — quality differences between them show up elsewhere (RAL, OBS), not in this particular stat.

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

.. container:: rule-guide

   **Why:** Limits ASL's benefit to the one phase (Grenade Phase) where a coordinating officer can meaningfully organize the attack — once a close assault degenerates into Entry Fire or ongoing melee, the fighting is too close and chaotic for a leader's coordination to have a clean, separable effect.

   **Example:** A leader's Coordinate Assault action boosts grenade rFP during the Grenade Phase, but that same leader's presence provides no additional bonus once the assault moves into Entry Fire or Melee Continuation — those phases resolve without any ASL contribution.

12.9  Leader Casualties
-----------------------


**12.9.1**  When a hex containing a leader takes a Casualty result or worse, the owning player rolls 1d6 to determine who was hit:

.. container:: rule-guide

   **Why:** Introduces an allocation roll so a Casualty result against a mixed hex doesn't automatically hit the leader — a leader sharing a hex with combat units has some real chance of being spared while a subordinate takes the hit, reflecting how fire doesn't precisely target rank.

   **Example:** A hex containing both a leader and a rifle squad takes a Casualty result. Rather than automatically applying it to the leader, the owning player rolls 1d6 to see which one was actually hit.

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

.. container:: rule-guide

   **Why:** Carves out the one case where the allocation roll of Rule 12.9.1 doesn't apply — a sniper's deliberate shot already picked its specific target on purpose (Rule 20.2), so re-randomizing who actually got hit would defeat the entire point of that targeted shot.

   **Example:** A sniper deliberately targets a leader specifically and scores a Casualty result. That result applies directly to the leader — no 1d6 allocation roll gives a chance for a nearby subordinate to have been hit instead.

    *See also: Rule 20.2 (Sniper Deliberate Targeting)*

**12.9.2**  If the leader is hit, flip the leader counter to its wounded rear face. A wounded leader continues to function but at reduced effectiveness.

.. container:: rule-guide

   **Why:** Gives a hit leader the same front/rear-face step-loss mechanism as an infantry counter (Rule 3.2.1) rather than removing them outright — a wounded leader is degraded, not gone, matching Rule 12.10's reduced-stat rear face.

   **Example:** A leader hit by the allocation roll's "leader hit" result is flipped to its wounded rear face and continues fighting at the reduced CMD/OBS/RAL/ASL/Defence values of Rule 12.10.1, rather than being removed from play.

**12.9.3**  If the hex contains only the leader (no subordinate units), the leader is automatically hit — no roll needed.

.. container:: rule-guide

   **Why:** Skips the allocation roll entirely when there's no one else in the hex to allocate the hit to — the roll of Rule 12.9.1 only exists because a subordinate might have been hit instead, and that possibility disappears when the leader is alone.

   **Example:** A lone leader (no combat units in the hex) that takes a Casualty result is automatically hit — there's no 1d6 roll, since there's no subordinate present who could have taken it instead.

**12.9.4**  Suppressed and Pinned results against a hex containing both a leader and combat units apply to a combat unit, never to the leader — the allocation roll of Rule 12.9.1 exists only for Casualty or worse. A leader **alone** in a hex takes Suppressed and Pinned results personally, with the usual markers and recovery rolls; while Pinned, Rule 12.3.4's projection limits apply.

.. container:: rule-guide

   **Why:** Scopes the leader-casualty allocation roll (Rule 12.9.1) to Casualty-or-worse results only — a Suppressed or Pinned result against a mixed hex simply goes to a subordinate automatically, since those lesser results aren't worth rolling to protect the leader from, but a lone leader has no subordinate to absorb them and takes the status personally.

   **Example:** A hex with a leader and a combat unit that takes a Suppressed result applies it to the combat unit automatically, with no roll — but if that same leader were alone in the hex, the Suppressed result would apply directly to the leader instead.

12.10  Wounded Leaders
----------------------


**12.10.1**  The rear face of a leader counter represents a wounded officer. Wounded leaders apply the following stat reductions:

.. container:: rule-guide

   **Why:** Reduces most of a leader's key stats at once rather than singling out one — a wounded officer is diminished broadly in command capability, observation, rally reliability, and assault coordination, matching the real effect of an injury on someone still trying to lead.

   **Example:** A leader flipped to their wounded rear face after being hit (Rule 12.9.2) applies every reduction in the Rule 12.10.1 table simultaneously — CMD, OBS, RAL, ASL, and Defence all shift together, not just one stat.

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


**12.10.2**  A wounded leader that takes another Casualty result or worse: roll 1d6. On 1–3 the leader is eliminated and moved to the BROKEN zone of the Casualty Track. On 4–5 the leader is evacuated and moved to the BROKEN zone of the Casualty Track. On 6 the leader is captured (Rule 11.2a) and moves to the CAPTURED zone of the Casualty Track.

.. container:: rule-guide

   **Why:** Gives a wounded leader's second serious hit three distinct outcomes rather than a single fixed one, reflecting the real uncertainty of a second casualty on someone already hurt — most rolls end the leader's scenario one way or another, but only a minority result in capture.

   **Example:** A wounded leader hit again by a Casualty result rolls 1d6: a 2 sends them to the BROKEN zone as eliminated, a 5 sends them to the BROKEN zone as evacuated (mechanically identical placement, different narrative outcome), and only a 6 routes them to capture under Rule 11.2a instead.

    *See also: Rule 11.2a (Administrative Capture).*

**12.10.3**  Leader elimination has immediate effect — AP pool drops from the next impulse onward. The remaining leaders must compensate or the force becomes seriously degraded.

.. container:: rule-guide

   **Why:** Reaffirms Rule 12.3.5's immediate-effect principle specifically for the elimination outcome of Rule 12.10.2, so a lost leader's impact on the AP pool is felt right away in the very next impulse, not deferred to a future turn's recalculation.

   **Example:** A side's CMD 3 leader is eliminated on a 1-3 roll under Rule 12.10.2. That side's AP pool drops for the remainder of the current turn starting with the very next impulse, immediately reducing what it can still accomplish that turn.

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
