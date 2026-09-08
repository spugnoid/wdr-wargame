Section 13 — Campaign Rules
===========================

*[ TBD: Two pieces of the campaign economy remain undesigned: EM's downward half (Rule 13.5.2) and the full branching campaign structure (Rule 13.5) — the actual tree of linked scenarios is campaign-specific authored content, not a generic rule, and is left to each campaign's own design. Everything else in this section is complete. ]*

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
     - Units rendered CI by ranged fire (Rule 10.4.3), psychological breaks from failed morale checks (Rules 10.4.4, 15.3.2), units routed off the friendly map edge (Rule 10.6.5), and escaped prisoners returning to their owner (Rule 11.4.2)
     - Front face up if full strength when broken; rear face up if reduced
   * - DISPERSED
     - Units rendered CI by close assault or melee morale failure (Rule 10.5.1) — in-scenario holding only; every Dispersed unit rallies or is captured by scenario end (Rule 11.2a), so this zone is always empty between scenarios
     - Front face up if full strength when dispersed; rear face up if reduced (Rule 10.5.1)
   * - CAPTURED
     - Accepted surrenders (Rule 11.2) and administrative captures (Rule 11.2a)
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

**13.2.2**  Resupply covers two things: clearing EXPENDED strips from support weapons (Rule 21) and issuing Replacement Points to mitigate bad recovery rolls (13.2.2a). It does not touch scenario ammunition (Rule 16.3), which resets fresh every scenario regardless of Recovery Window.

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

**13.2.2b**  Leaders recovering under Rule 13.3.1 use the same procedure, reading "returns as rear face" as "returns wounded" and "returns at full strength" as "returns unwounded."

**13.2.3**  A **campaign turn** is the interval between two consecutive scenarios in the campaign tree. Every between-scenario step — recovery rolls (13.3), combining half squads (13.4), Intelligence Point spending (11.6.3) — happens once per campaign turn.

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

13.4  Combining Half Squads
---------------------------


**13.4.1**  During a Days or Extended Recovery Window, two rear face counters of the same unit type may be combined into one full strength counter.

**13.4.2**  Combination conditions: same nation; same unit type; same year bracket or adjacent year brackets; combination may only occur once per campaign turn per unit type.

**13.4.3**  If both combining units share the same quality level, the combined unit returns at that quality. If they differ, the combined unit uses the lower quality. If the quality gap exceeds one step, combination is not permitted.

**13.4.4**  Record the combined unit as Composite on its roster/OB sheet entry — no physical marker is placed on the map. A Composite unit has -1 Morale until it completes one full scenario without being rendered CI, at which point the notation is cleared from the roster sheet. See design note E.98.

13.5  Branching Campaign Structure
----------------------------------


*[ TBD: Full branching campaign design to be completed. Framework below. ]*

The campaign consists of a series of scenarios linked by a branching tree structure. The outcome of each scenario (decisive victory, marginal victory, draw, marginal defeat, decisive defeat) determines which scenario follows.

**13.5.1**  Outcome grades, until the full campaign design lands, map from the scenario's own end state (Rules 15.7, 22.6): a win by Force Morale collapse or with at least **twice** the loser's victory points is a **decisive victory**; any other win is a **marginal victory**; equal victory points at the turn limit is a **draw**. Defeats mirror the victories from the loser's side.

**13.5.2**  A unit's Experience Modifier (EM, Rule 1.3) begins at +0 for every counter fielded at its printed quality. Track a **CI-free streak** on the unit's roster sheet: it increases by one at the end of any scenario the unit finishes without being rendered CI (broken, dispersed, or captured — Rule 13.1), and resets to zero the instant the unit is rendered CI in a scenario.

**13.5.2a**  When a unit's CI-free streak reaches 3, its EM increases by one step and the streak resets to zero. Each EM step raises the unit's effective Quality one level on the Rule 15.2.1a ladder (Militia → Green → Regular → Veteran/Elite). EM earned this way caps at Veteran/Elite — the Elite specialist row (veteran snipers, senior leaders) is a printed classification the promotion track cannot reach.

**13.5.2b**  EM applies to any counter with a printed Quality rating — combat units, weapon teams, and vehicle crews alike (Rule 19.6.1). A unit fielded at Militia can, over a long campaign, reach Veteran/Elite after three separate 3-scenario CI-free streaks (9 CI-free scenarios total, with the streak resetting on every intervening CI).

*[ TBD: this rule covers only EM's upward, combat-experience half. EM "reflecting combat experience gained **or lost**" (Rule 1.3) and Rule 19.6.1's "quality degrades with replacement crew" both name a downward half — a unit or vehicle crew losing EM steps — that is not yet designed. Treat EM as strictly non-negative until that half is defined. See design note E.102. ]*

A winning campaign branch should produce momentum — better recovery time, intelligence from prisoners, and eventually unit experience (13.5.2). A losing branch should produce compounding pressure — no recovery time, degraded units, forced to fight with what remains.
