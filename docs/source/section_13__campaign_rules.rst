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
     - Units rendered CI by ranged fire
     - Front face up if full strength when broken; rear face up if reduced
   * - DISPERSED
     - Units rendered CI by close assault or morale failure
     - Rear face up
   * - CAPTURED
     - Accepted surrender (POW markers)
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
     - **Dispersed Recovery**
     - **Combine Halves**
     - **Resupply**
   * - None
     - No roll
     - No roll
     - No
     - No
   * - Hours
     - No roll
     - Roll at -2
     - No
     - Partial
   * - Days
     - Roll
     - Roll
     - Yes
     - Full
   * - Extended
     - Roll at +1
     - Roll at +2
     - Yes
     - Full + bonus


**13.2.1**  The scenario outcome modifies the Recovery Window: the losing side's window is reduced one step (Days becomes Hours, Hours becomes None).

**13.2.2**  If the attacker loses ground, their Dispersed counters are vulnerable to capture by the defender during the scenario resolution step.

13.3  Between-Scenario Recovery Rolls
-------------------------------------


For each counter in the Casualty Track, roll 1d6 and add a Morale modifier based on the unit's Morale value:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit Morale**
     - **Roll Modifier**
   * - 1–3
     - -1
   * - 4–5
     - +0
   * - 6+
     - +1


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


DISPERSED zone recovery (Hours window or better, at penalty; Days or better, normal):

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1
     - No recovery — removed from campaign pool
   * - 2–3
     - Returns as rear face
   * - 4–5
     - Returns as rear face
   * - 6–7
     - Returns at full strength
   * - 8+
     - Returns at full strength with +1 Experience step


13.4  Combining Half Squads
---------------------------


**13.4.1**  During a Days or Extended Recovery Window, two rear face counters of the same unit type may be combined into one full strength counter.

**13.4.2**  Combination conditions: same nation; same unit type; same year bracket or adjacent year brackets; combination may only occur once per campaign turn per unit type.

**13.4.3**  If both combining units share the same quality level, the combined unit returns at that quality. If they differ, the combined unit uses the lower quality. If the quality gap exceeds one step, combination is not permitted.

**13.4.4**  Combined units receive a Composite marker. Composite units have -1 Morale until they complete one full scenario without being rendered CI.

13.5  Branching Campaign Structure
----------------------------------


*[ TBD: Full branching campaign design to be completed. Framework below. ]*

The campaign consists of a series of scenarios linked by a branching tree structure. The outcome of each scenario (decisive victory, marginal victory, draw, marginal defeat, decisive defeat) determines which scenario follows.

A winning campaign branch should produce momentum — better recovery time, unit experience accumulating, intelligence from prisoners. A losing branch should produce compounding pressure — no recovery time, degraded units, forced to fight with what remains.
