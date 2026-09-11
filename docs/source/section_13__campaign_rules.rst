Section 13 — Campaign Rules
===========================

*[ Note: the campaign economy is complete. Authoring an actual campaign's specific scenarios and branch tables (Rule 13.5) is campaign-specific content the framework supports but does not itself provide. ]*

13.1  Casualty Track
--------------------


The Casualty Track is a designated area beside the map. It has four zones: BROKEN, DISPERSED, CAPTURED, and GUARD. Eliminated counters are placed in the appropriate zone as follows:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Zone**
     - **Counter Placement**
     - **Face**
   * - BROKEN
     - Units rendered CI by ranged fire (Rule 10.4.3), psychological breaks from failed morale checks (Rules 10.4.4, 15.3.2), units routed off the friendly map edge (Rule 10.6.5), escaped prisoners returning to their owner (Rule 11.4.2), and ABANDONED or DAMAGED vehicle hulls not captured by the enemy (Rule 19.3.1)
     - Front face up if full strength when broken; rear face up if reduced. For a vehicle hull: "front face" means ABANDONED (functional, no crew), "rear face" means DAMAGED (MOB or GUN kill) — see Rule 13.3.2.
   * - DISPERSED
     - Units rendered CI by close assault or melee morale failure (Rule 10.5.1) — in-scenario holding only; every Dispersed unit rallies or is captured by scenario end (Rule 11.2a), so this zone is always empty between scenarios
     - Front face up if full strength when dispersed; rear face up if reduced (Rule 10.5.1)
   * - CAPTURED
     - Accepted surrenders (Rule 11.2), administrative captures (Rule 11.2a), and ABANDONED vehicle hulls successfully captured in-scenario (Rule 19.4)
     - Front face up
   * - GUARD
     - Not a zone for counters — used to track which units have GUARD markers
     - N/A


13.2  Recovery Windows
----------------------


Each scenario has a Recovery Window value printed in its scenario parameters. The Recovery Window determines which between-scenario recovery rolls are available.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Recovery Window**
     - **Broken Recovery**
     - **Combine Halves**
     - **Resupply**
   * - None
     - No roll
     - No
     - No
   * - Hours
     - No roll
     - No
     - Partial
   * - Days
     - Roll
     - Yes
     - Full
   * - Extended
     - Roll at +1
     - Yes
     - Full + bonus


**13.2.1**  The scenario outcome modifies the Recovery Window: the losing side's window is reduced one step (Extended becomes Days, Days becomes Hours, Hours becomes None).

.. container:: rule-guide

   **Why:** Punishes the losing side with a worse recovery outcome on top of whatever losses it already suffered — losing a battle costs the loser time to recover, not just the immediate scenario result, compounding disadvantage into the next campaign turn.

   **Example:** A side scheduled for a Days Recovery Window that loses its scenario has that window reduced to Hours for this campaign turn — fewer of its BROKEN-zone units get to roll for recovery (Rule 13.2 table), and Resupply is only Partial instead of Full.

**13.2.2**  Resupply covers two things: clearing EXPENDED strips from support weapons (Rule 21) and issuing Replacement Points to mitigate bad recovery rolls (13.2.2a). It does not touch scenario ammunition (Rule 16.3), which resets fresh every scenario regardless of Recovery Window.

.. container:: rule-guide

   **Why:** Scopes Resupply to exactly two specific things so it doesn't get confused with the separate, always-fresh scenario ammunition system (Rule 16.3) — Resupply is a between-scenario campaign mechanic, while scenario ammo tracking starts clean every time regardless of how a campaign is going.

   **Example:** A side with a Days Recovery Window gets Full Resupply — clearing all its EXPENDED support-weapon strips and issuing 1 Replacement Point — but this has no effect on how much ammunition its units start the next scenario with, since that's governed separately by Rule 16.3.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Resupply Tier**
     - **EXPENDED Strips Cleared**
     - **Replacement Points Issued**
   * - No Resupply
     - None
     - 0
   * - Partial
     - Half of the side's EXPENDED strips, rounded down
     - 0 (half of the 1-point baseline, rounded down)
   * - Full
     - All of the side's EXPENDED strips
     - 1
   * - Full + bonus
     - All of the side's EXPENDED strips
     - 2


**13.2.2a**  A Replacement Point is spent on one counter in the BROKEN zone, after that counter's recovery roll (13.3) is made, to raise its result one tier on the 13.3 table (e.g. "no recovery — removed from campaign pool" becomes "returns as rear face"; "returns as rear face" becomes "returns at full strength"). Multiple Replacement Points may be spent on the same counter, one tier per point. Replacement Points not spent this campaign turn are lost — they do not carry over.

.. container:: rule-guide

   **Why:** Lets Replacement Points improve a roll already made rather than adding to the die roll itself, so a player can target scarce points at the unit that most needs saving after seeing all the recovery rolls, instead of committing points blindly before results are known.

   **Example:** A unit rolls a 2 on its BROKEN-zone recovery roll (would be removed from the campaign pool). Spending one Replacement Point on it raises the result one tier to "returns as rear face" instead — a second point on the same counter would raise it again, to "returns at full strength."

**13.2.2b**  Leaders recovering under Rule 13.3.1 use the same procedure, reading "returns as rear face" as "returns wounded" and "returns at full strength" as "returns unwounded."

.. container:: rule-guide

   **Why:** Reuses the exact same Replacement Point mechanism for leaders as for regular units (Rule 13.2.2a) rather than inventing a separate leader-specific system, just remapping the table's "rear face"/"full strength" language to the leader-appropriate "wounded"/"unwounded" terms.

   **Example:** A leader's BROKEN-zone recovery roll lands on "returns as rear face" — read here as "returns wounded." A Replacement Point spent on that leader raises the result to "returns at full strength," read as "returns unwounded."

**13.2.3**  A **campaign turn** is the interval between two consecutive scenarios in the campaign tree. Every between-scenario step — recovery rolls (13.3), combining half squads (13.4), Intelligence Point spending (11.6.3) — happens once per campaign turn.

.. container:: rule-guide

   **Why:** Defines "campaign turn" as the unit of time all the between-scenario mechanics share, so rules like recovery rolls, half-squad combination, and Intelligence Point spending don't need to separately specify their own cadence — they all happen exactly once per gap between scenarios.

   **Example:** Between finishing one scenario and starting the next in the campaign tree, a side resolves its recovery rolls (13.3), any eligible half-squad combinations (13.4), and any Intelligence Point spending (11.6.3) — all as part of that one campaign turn, not spread across multiple.

13.3  Between-Scenario Recovery Rolls
-------------------------------------


For each counter in the **BROKEN zone**, roll 1d6 and add the unit's Morale modifier (Morale − 5, Rule 15.2.1a). CAPTURED counters belong to the enemy and never roll; the DISPERSED zone is always empty between scenarios (Rule 13.1). Psychological breaks (white CI cause marker) roll at +1 (Rule 10.4.6).


BROKEN zone recovery (Days window or better):

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Front Face Up (Full Strength When Broken)**
     - **Rear Face Up (Reduced When Broken)**
   * - 1–2
     - No recovery — removed from campaign pool
     - No recovery — removed
   * - 3–4
     - Returns as rear face (half squad)
     - No recovery — removed
   * - 5–6
     - Returns as rear face
     - Returns as rear face
   * - 7+
     - Returns at full strength
     - Returns as rear face


**13.3.1**  Leaders in the BROKEN zone (eliminated or evacuated, Rule 12.10.2) roll on the same table: read "returns as rear face" as returning on the **wounded** face, and "returns at full strength" as returning unwounded. A wounded leader who finished the scenario on the map heals — flip to the front face — in a Days or Extended window; in a shorter window the wound carries into the next scenario.

.. container:: rule-guide

   **Why:** Reuses the single BROKEN-zone recovery table for leaders (relabeling its outcomes) rather than a separate leader table, while adding one leader-specific detail — a wounded leader who stayed on the map (not sent to BROKEN) can still heal on its own given enough recovery time, distinct from the roll-based table entirely.

   **Example:** A leader who ended the scenario wounded but still on the map (not eliminated or evacuated) simply flips back to their healthy front face automatically during a Days or Extended Recovery Window — no roll needed, unlike a BROKEN-zone leader who must roll on the 13.3 table.

**13.3.2**  Vehicle hulls in the BROKEN zone (ABANDONED or DAMAGED, not captured — Rule 13.1) roll on the same table using the crew's own Morale modifier (the same reuse Rule 19.4.3 already makes for capture attempts), reading the front/rear columns as ABANDONED and DAMAGED respectively: "no recovery" means the hull is written off and removed from the campaign's vehicle pool; "returns as rear face" means the hull returns, but DAMAGED — it needs a further Days-or-better Recovery Window before it can be fielded, rolling again next campaign turn; "returns at full strength" means the hull returns fully repaired. A recovered hull needs a CREW counter assigned before its next scenario, from the replacement pool if its original crew did not survive — Rule 13.5.2c's EM reset applies exactly as it already does for any re-crewed vehicle.

.. container:: rule-guide

   **Why:** Rule 13.5.2b already gave vehicle crews the same campaign mechanics as infantry (Experience Modifier, quality progression), but nothing repaired the vehicle's own hull between scenarios — a DAMAGED or ABANDONED tank simply had no path back into the campaign at all, unlike everything else the Casualty Track already tracks. Reusing the identical table (rather than a new one) keeps the campaign layer's recovery logic in one place, and routing a recovered hull through the existing re-crewing rule means this doesn't invent a second EM mechanic alongside the one Rule 13.5.2c already provides.

   **Example:** A DAMAGED Panzer IV (regular crew quality, Morale modifier +0) rolls a 6 on the BROKEN-zone table — reading the "rear face" column for a DAMAGED hull, that's "returns as rear face," so the hull comes back but is still not battle-ready; it needs one more Days-or-better Recovery Window before it can be issued to a scenario, and whatever crew mans it then is assigned (and EM-reset, Rule 13.5.2c) from the replacement pool like any other re-crewed vehicle.

    *See also: Rule 19.3.1 (ABANDONED/DAMAGED vehicle states), Rule 19.4 (capture — the path that removes a hull from this table entirely), Rule 13.5.2c (EM reset on re-crewing).*

13.4  Combining Half Squads
---------------------------


**13.4.1**  During a Days or Extended Recovery Window, two rear face counters of the same unit type may be combined into one full strength counter.

.. container:: rule-guide

   **Why:** Gives a campaign a way to consolidate accumulated under-strength survivors back into effective fighting units, but only when there's enough time (Days or Extended window) to actually reorganize personnel between scenarios — a short window doesn't allow for it.

   **Example:** Two rear-face (reduced) rifle squads of the same type surviving from earlier scenarios can be combined into one full-strength squad during a Days Recovery Window, but not during an Hours window, which is too short for reorganization.

**13.4.2**  Combination conditions: same nation; same unit type; same year bracket or adjacent year brackets; combination may only occur once per campaign turn per unit type.

.. container:: rule-guide

   **Why:** Keeps combination realistic and bounded — you can't merge units from different armies or wildly different equipment eras, and the once-per-turn-per-type cap prevents a side from combining its way through an unlimited chain of mergers in a single campaign turn.

   **Example:** Two reduced German rifle squads from adjacent year brackets can combine, but a German squad cannot combine with a Soviet one, and a side with three eligible rifle-squad pairs can still only perform one rifle-squad combination that campaign turn.

**13.4.3**  If both combining units share the same quality level, the combined unit returns at that quality. If they differ, the combined unit uses the lower quality. If the quality gap exceeds one step, combination is not permitted.

.. container:: rule-guide

   **Why:** Prevents a mismatched quality merger from producing an unrealistically strong combined unit — the result is capped at the lower of the two source qualities, and if the gap is too wide, the two groups of survivors are treated as too different to reorganize together at all.

   **Example:** A Regular-quality half squad combining with a Veteran-quality half squad produces a Regular-quality combined unit; a Militia half squad combining with a Veteran one is not permitted at all, since that quality gap exceeds one step.

**13.4.4**  Record the combined unit as Composite on its roster/OB sheet entry — no physical marker is placed on the map. A Composite unit has -1 Morale until it completes one full scenario without being rendered CI, at which point the notation is cleared from the roster sheet. See design note E.98.

.. container:: rule-guide

   **Why:** Tracks the Composite status only on paper, not as a map marker, since it's a roster-level fact rather than something that needs to be visible during play — and the temporary -1 Morale penalty models the newly-merged unit's lack of cohesion until it proves itself together in one clean scenario.

   **Example:** A newly-combined Composite squad fights its next scenario at -1 Morale; if it gets through that scenario without being rendered CI, the Composite notation and its penalty are both cleared from the roster sheet before the following scenario.

13.5  Branching Campaign Structure
----------------------------------


The campaign consists of a series of scenarios linked by a branching structure (13.5.3–13.5.7). The outcome of each scenario (decisive victory, marginal victory, draw, marginal defeat, decisive defeat) determines which scenario follows.

**13.5.1**  Outcome grades map from the scenario's own end state (Rules 15.7, 22.6): a win by Force Morale collapse or with at least **twice** the loser's victory points is a **decisive victory**; any other win is a **marginal victory**; equal victory points at the turn limit is a **draw**. Defeats mirror the victories from the loser's side.

.. container:: rule-guide

   **Why:** Converts a scenario's raw victory-point outcome into one of five standardized grades that the whole branching campaign structure (13.5.3-13.5.7) can route on, so campaign branching logic never needs to look at raw victory-point math directly — just the grade.

   **Example:** A side that wins with triple its opponent's victory points is graded a decisive victory; a side that wins with only slightly more points is graded a marginal victory instead — both are wins, but they route to potentially different next nodes in the campaign tree (Rule 13.5.3).

**13.5.2**  A unit's Experience Modifier (EM, Rule 1.3) begins at +0 for every counter fielded at its printed quality. Track a **CI-free streak** on the unit's roster sheet: it increases by one at the end of any scenario the unit finishes without being rendered CI (broken, dispersed, or captured — Rule 13.1), and resets to zero the instant the unit is rendered CI in a scenario.

.. container:: rule-guide

   **Why:** Gives units a way to grow more experienced over a campaign by tracking sustained survival rather than any single scenario's performance — one bad scenario resets the streak, but the streak itself is what eventually earns a real, permanent stat improvement (13.5.2a).

   **Example:** A unit that survives three consecutive scenarios without ever being broken, dispersed, or captured builds a CI-free streak of 3; if it's rendered CI in its fourth scenario, that streak resets to zero and the unit must start building toward its next promotion from scratch.

**13.5.2a**  When a unit's CI-free streak reaches 3, its EM increases by one step and the streak resets to zero. Each EM step raises the unit's effective Quality one level on the Rule 15.2.1a ladder (Militia → Green → Regular → Veteran/Elite). EM earned this way caps at Veteran/Elite — the Elite specialist row (veteran snipers, senior leaders) is a printed classification the promotion track cannot reach.

.. container:: rule-guide

   **Why:** Turns a completed CI-free streak into a lasting Quality improvement, capping the earnable ceiling at Veteran/Elite rather than the specialist Elite tier — that top row represents dedicated specialists the promotion path specifically shouldn't be able to manufacture out of an ordinary unit's battlefield success.

   **Example:** A Militia-quality unit that reaches its third CI-free streak is promoted to Green quality and its streak resets to zero; a unit already at Veteran/Elite that reaches another CI-free streak of 3 gains no further Quality improvement, since that's the promotion track's ceiling.

**13.5.2b**  EM applies to any counter with a printed Quality rating — combat units, weapon teams, and vehicle crews alike (Rule 19.6.1). A unit fielded at Militia can, over a long campaign, reach Veteran/Elite after three separate 3-scenario CI-free streaks (9 CI-free scenarios total, with the streak resetting on every intervening CI).

.. container:: rule-guide

   **Why:** Extends the EM promotion mechanic to every kind of Quality-rated counter, not just infantry squads, since weapon teams and vehicle crews earn combat experience the same way — and spells out the full arithmetic (9 CI-free scenarios across 3 separate streaks) so a player can see just how much sustained success the top of the ladder actually requires.

   **Example:** A vehicle crew fielded at Militia quality that survives 9 total CI-free scenarios, spread across three separate 3-scenario streaks with no intervening CI, reaches Veteran/Elite — the same promotion path as an infantry squad's.

**13.5.2c**  EM is lost, not just gained: it resets to zero whenever a counter is diluted with replacement personnel. A unit formed by Combining Half Squads (13.4) is a newly-raised Composite counter with no shared combat history — it starts at EM +0, regardless of either source counter's accumulated EM, on top of whatever quality 13.4.3 already assigns it. A vehicle re-crewed from the replacement pool after losing its original crew (Rule 19.6.1) likewise resets to EM +0.

.. container:: rule-guide

   **Why:** Ties EM specifically to a counter's continuous, undiluted combat history — once fresh replacement personnel are mixed in (via combination or re-crewing), that shared history is broken, so accumulated experience resets rather than transferring to what is functionally a new unit.

   **Example:** A veteran squad with EM +2 that gets combined with another rear-face squad under Rule 13.4 produces a Composite unit starting at EM +0 — the veteran squad's hard-earned experience doesn't carry over into the newly-formed unit.

**13.5.2d**  Ordinary casualties, a bad recovery roll, or being rendered CI do not by themselves cost EM — only combining or re-crewing does (13.5.2c). This keeps EM loss tied to a single, unambiguous event rather than a second parallel bad-performance tracker alongside the CI-free streak (13.5.2) and the Composite marker's own -1 Morale penalty (13.4.4), which already covers a freshly-combined unit's shakiness in the short term. See design note E.104.

.. container:: rule-guide

   **Why:** Prevents EM from being punished twice over for the same bad outcome — a CI-free streak reset already captures the setback of being rendered CI, so EM loss is reserved strictly for the dilution event of Rule 13.5.2c rather than piling a second penalty onto ordinary battlefield misfortune.

   **Example:** A unit rendered CI in a scenario loses its CI-free streak progress (Rule 13.5.2) but keeps whatever EM it had already earned — only if that unit is later combined with another counter (Rule 13.4) or re-crewed does its EM actually reset to zero.

**13.5.3**  A campaign is authored as a set of **nodes**, each one linking a single scenario to a **branch table**: an assignment of every outcome grade (13.5.1) to either another node or to **END**. A campaign always designates one node as its **start**.

.. container:: rule-guide

   **Why:** Gives a campaign designer a clean, modular unit — the node — that pairs one scenario with the routing logic deciding what happens after it, so the whole campaign structure can be authored and reasoned about one node at a time rather than as one giant flowchart.

   **Example:** A campaign designer authors a node linking "Scenario 3: River Crossing" to a branch table that routes a decisive victory to Node 5, a marginal victory to Node 4, and both defeat grades to END — that pairing is the whole node.

**13.5.4**  A branch table's five outcome grades need not each name a different node — the scenario designer may route multiple grades to the same next node (e.g. both victory grades to one node, both defeat grades to another, draw to a third), or route all five to distinct nodes, entirely at the designer's discretion. Every grade must route somewhere; a branch table with a grade left unassigned is incomplete.

.. container:: rule-guide

   **Why:** Gives designers full flexibility in how finely they want outcomes to matter — a simple win/lose branch or a fully five-way split are both valid — while still requiring every one of the five grades to have a defined destination, so no possible scenario outcome ever leaves the campaign with nowhere to go.

   **Example:** A designer might route both victory grades to the same "advance" node and both defeat grades to the same "retreat" node, using only two next-node destinations total across all five outcome grades — as long as every grade, including draw, is assigned to something.

**13.5.5**  More than one node's branch table may point to the same next node. A campaign is therefore not required to be a strict tree — different paths through it may reconverge — but it may never point back to a node already visited earlier in the same playthrough's path (no cycles). This keeps the total scenarios a designer must author manageable as a campaign grows deeper, without ever letting a campaign run forever.

.. container:: rule-guide

   **Why:** Allows a campaign's branches to merge back together (keeping the total number of scenarios a designer must write manageable) while banning cycles specifically, since a campaign that could loop back on itself would have no guaranteed end — every playthrough needs to terminate.

   **Example:** Two different early-game outcomes might both route to the same "Node 7: Consolidation" — that's fine, since it's convergence, not a cycle. But Node 7 could never route back to an earlier node already visited on that same playthrough's path.

**13.5.6**  Playing a campaign: begin at the start node and play its scenario. Determine the outcome grade (13.5.1) from a side nominated by the campaign's own design (its "reference side" — e.g. the historical attacker, or Side A) and consult that node's branch table. If it names another node, that node's scenario is played next, applying the Recovery Window and between-scenario steps (13.2–13.4) for the campaign turn between them. If it names END, the campaign is over.

.. container:: rule-guide

   **Why:** Walks through the full campaign-playing procedure end to end — start node, outcome grading from one designated reference side, branch table lookup, and applying the between-scenario steps — so a group actually running a campaign has one clear sequence to follow rather than piecing it together from the individual rules.

   **Example:** A campaign designates Side A as its reference side. After playing the start node's scenario, the group grades the outcome from Side A's perspective (13.5.1), consults that node's branch table, applies the Recovery Window and between-scenario steps (13.2-13.4) for the gap, and moves on to whatever node the table names — repeating until a node names END.

**13.5.7**  The side that won the terminal scenario — by the same outcome grade (13.5.1) used throughout — wins the campaign. A terminal scenario ending in a draw is a drawn campaign.

.. container:: rule-guide

   **Why:** Decides the overall campaign winner by the single terminal scenario's outcome rather than tallying every scenario played along the way — the branching structure means different playthroughs see different numbers of scenarios, so only the final one is a fair basis for the campaign-level result.

   **Example:** A campaign that took 4 scenarios to reach END is won by whichever side won that 4th, terminal scenario — a marginal victory in an earlier scenario along the path has no bearing on who wins the campaign overall, beyond having shaped which node came next.

A winning campaign branch should produce momentum — better recovery time, intelligence from prisoners, and eventually unit experience (13.5.2). A losing branch should produce compounding pressure — no recovery time, degraded units, forced to fight with what remains.
