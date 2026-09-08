Section 13 — Campaign Rules
===========================

*[ TBD: Campaign rules are not yet fully designed. This section contains the locked framework and placeholder detail. ]*

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

**13.2.2**  *[ TBD: the Resupply column reserves a mechanism the campaign economy does not define yet — ammunition is currently per-scenario (Rule 16.3) and there are no replacement points to resupply. The column stands as framework; no rule consumes it. ]*

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

**13.5.2**  *[ TBD: "unit experience accumulating" names a promotion system (green → regular → veteran across scenarios) that does not exist yet. No rule currently changes a counter's quality between scenarios; treat printed quality as fixed until that system is designed. ]*

A winning campaign branch should produce momentum — better recovery time, intelligence from prisoners, and eventually unit experience (13.5.2). A losing branch should produce compounding pressure — no recovery time, degraded units, forced to fight with what remains.
