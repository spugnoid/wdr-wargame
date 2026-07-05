Section 16 — Mortars and Smoke
==============================

Mortars are the infantryman's organic artillery — immediately available, no coordination delay, capable of indirect fire over obstacles and onto reverse slopes. Smoke provides concealment for movement across open ground. Together they are the primary tools enabling tactical manoeuvre under fire.

16.1  Mortar Counter Design
---------------------------


Mortar counters display four specialist stats in addition to standard Defence and Morale:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Stat**
     - **Notation**
     - **Description**
   * - Range band
     - RNG ⬡min-max
     - Minimum and maximum range in hexes. Cannot target within minimum range.
   * - Blast radius
     - BLT #
     - Hexes around impact point also affected. BLT 1 = target hex + all 6 adjacent hexes.
   * - Accuracy
     - ACC #
     - Base accuracy value. Roll 1d6 vs ACC — equal or under means round lands on target hex.
   * - Ammunition
     - AMO #
     - Base ammunition per scenario. Secret bonus added at setup. See Rule 16.3.


All mortar counters use M1 F2 (mobile) or M0 F2 (deployed). Mortar teams must deploy before firing — same deploy/limber rules as HMG teams (Section 7.6).

16.2  Representative Mortar Counters — 1943
-------------------------------------------


.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit**
     - **RNG**
     - **BLT**
     - **ACC**
     - **AMO**
     - **rFP**
     - **Notes**
   * - German 50mm leGrW 36
     - ⬡1-25
     - 1
     - 3
     - 8
     - 4
     - Squad mortar — platoon organic
   * - German 81mm sGrW 34
     - ⬡3-60
     - 1
     - 3
     - 10
     - 7
     - Company mortar
   * - Soviet 50mm RM-40
     - ⬡1-20
     - 1
     - 2
     - 8
     - 4
     - Squad mortar — less accurate than German
   * - Soviet 82mm PM-36
     - ⬡3-55
     - 1
     - 3
     - 10
     - 7
     - Company mortar
   * - German 120mm GrW 42
     - ⬡5-75
     - 2
     - 3
     - 8
     - 9
     - Heavy mortar — battalion asset


16.3  Ammunition
----------------


**16.3.1**  Each mortar's base AMO value is printed on its counter. At scenario setup, the owning player secretly rolls 1d6-1 and adds the result to base AMO. This total is the actual ammunition available, recorded privately. The opponent never sees this value.

**16.3.2**  Each fire mission (HE or smoke) expends 1 AMO. HE and smoke ammunition are tracked on the same AMO count unless the scenario specifies separate pools.

**16.3.3**  When the mortar has fired its base AMO rounds, rather than announcing exhaustion, the owning player rolls on the extended ammunition table for each subsequent mission:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll (1d6)**
     - **Result**
   * - 1–2
     - Out of ammunition — mortar cannot fire again this scenario
   * - 3–4
     - Last salvo — fires this mission normally, then out of ammunition
   * - 5–6
     - Ammunition available — fires this mission normally, roll again next mission


**16.3.4**  The opponent never knows whether a mortar has exhausted its base AMO. A player may choose to stop firing a mortar even when rounds remain — to conserve for a critical moment or to deceive the opponent about remaining capacity.

16.4  Targeting Modes
---------------------


**16.4.1**  Mortars may fire in three modes, each with different accuracy and delay:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Mode**
     - **Requirements**
     - **ACC Modifier**
     - **Delay**
     - **Notes**
   * - Observed fire
     - Friendly unit (FO) with LOS to target hex spends 1 AP to call mission
     - +0
     - 2 impulses (81mm) / 1 impulse (60mm)
     - FO leader adds OBS rating to ACC
   * - Registered target
     - Target hex pre-designated at scenario setup (limit 2 per mortar)
     - -1
     - 1 impulse
     - Pre-calculated fire data
   * - Map fire
     - No FO, no registration
     - -2
     - 3 impulses
     - Firing blind — significant accuracy penalty
   * - Squad mortar direct lay
     - Squad mortar with LOS to target hex (crew fires own mortar)
     - +0
     - 0 impulses — immediate
     - No slip required
   * - Squad mortar blind fire
     - Squad mortar without LOS
     - -2
     - 1 impulse
     - Slip required


**16.4.2**  Effective ACC = mortar ACC + mode modifier + FO leader OBS (if applicable).

**16.4.3**  Minimum range applies in all modes — a mortar cannot target a hex closer than its RNG minimum regardless of mode.

16.5  Sealed Fire Mission Slips
-------------------------------


**16.5.1**  When a fire mission is called (except squad mortar direct lay), the owning player writes a sealed slip before the reaction window opens.

**16.5.2**  The slip records: mortar unit ID, target hex coordinate, firing mode, turn and impulse called, turn and impulse of arrival, and AMO count used.

**16.5.3**  The slip is folded face down and placed beside the mortar counter. Both players acknowledge its presence — the existence of the slip is public, its contents are secret.

**16.5.4**  The slip may not be modified after being placed. The target hex and arrival timing are committed at the moment of writing.

**16.5.5**  On the arrival impulse, the slip is revealed and read aloud. The round lands as written. No retroactive adjustment is possible.

**16.5.6**  The opponent knows a fire mission is pending from the presence of the slip. They do not know the target hex until revelation. This creates the historical tension of incoming fire — you know it is coming but not where.

16.6  Dispersion
----------------


**16.6.1**  On the arrival impulse, roll 1d6 vs the effective ACC value.

**16.6.2**  If the roll is equal to or less than ACC: the round lands on the target hex. No dispersion.

**16.6.3**  If the roll exceeds ACC: the round disperses. Determine landing hex:

**16.6.4**  Dispersion distance: roll D3 (1d6, halve, round up). Result = number of hexes from the target hex (1–3).

**16.6.5**  Dispersion direction: roll 1d6. 1=North, 2=Northeast, 3=Southeast, 4=South, 5=Southwest, 6=Northwest. These six directions correspond to the six hexsides of the flat-top hex grid; every map carries a compass rose defining North.

**16.6.6**  The round lands at the dispersed hex. Apply blast effect from that point.

**16.6.7**  Friendly units within the blast area of a dispersed round are subject to friendly fire — blast effect applies regardless of side.

16.7  Blast Effect
------------------


**16.7.1**  When a round lands, apply blast effect to the landing hex and all hexes within BLT radius.

**16.7.2**  For each unit in the blast area, resolve fire combat using the mortar's rFP value. Use the standard fire resolution procedure (Section 8) with the following modifications:

**16.7.3**  Cover modifiers apply — units in cover are protected from indirect fire.

**16.7.4**  Reverse slope and building cover are each reduced by 1 step — indirect fire angles over and into these positions. Reverse slope +4 becomes +3. Building heavy +5 becomes +4.

**16.7.5**  No range falloff — mortar rFP is flat regardless of range to target. The dispersion system handles accuracy at range; lethality on impact is constant.

**16.7.6**  Mortars use a single rFP value with no ⬡h -f notation. They do not participate in fire group grouping with direct fire weapons.

**16.7.7**  Hidden units in the blast area: blast effect applies regardless of visibility. A dummy marker in the blast hex produces no effect. A real hidden unit takes the blast effect and is automatically revealed — the explosion nearby discloses the position.

16.8  Adjustment Fire
---------------------


**16.8.1**  After a round disperses, the FO may call an adjustment mission.

**16.8.2**  Write a new slip with the adjusted target hex. Adjustment delay is always 1 impulse regardless of mortar type. Effective ACC for the adjustment is the original ACC + 2 (crew is already set up and ranged in).

**16.8.3**  Only one adjustment is permitted per fire mission. After adjustment, the mission is either fire for effect or cancelled.

**16.8.4**  Adjustment costs 1 additional AMO — the ranging round and adjustment round are separate expenditures.

16.9  Smoke Rounds
------------------


**16.9.1**  Smoke rounds follow the same targeting, sealed slip, delay, and dispersion procedures as HE rounds.

**16.9.2**  On landing, place a SMOKE marker showing step 3 (THICK) in the landing hex and all hexes within BLT radius.

**16.9.3**  Each SMOKE marker is independent. Markers from different fire missions or in different hexes dissipate separately.

16.10  Smoke Dissipation
------------------------


**16.10.1**  During each Recovery Phase, roll 1d6 for each individual SMOKE marker on the map:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1–2
     - Marker advances one dissipation step (3→2→1→removed)
   * - 3–6
     - Marker holds at current step


**16.10.2**  Smoke effects by dissipation step:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Step**
     - **Name**
     - **Intervening rFP Penalty**
     - **CON Bonus (concealment)**
     - **Notes**
   * - 3
     - THICK
     - -3 per hex
     - +3
     - Full smoke — movement across is heavily screened
   * - 2
     - THINNING
     - -2 per hex
     - +2
     - Smoke patchy — partial concealment
   * - 1
     - DISSIPATING
     - -1 per hex
     - +1
     - Remnant smoke — minor effect
   * - 0
     - GONE
     - Remove marker
     - —
     - Smoke has cleared


**16.10.3**  SMOKE markers use the existing intervening terrain penalty system (Section 4.3). A unit firing through 2 hexes of THICK smoke suffers -6 rFP to its fire — effectively preventing accurate fire through a fresh smoke screen.

**16.10.4**  Units occupying a SMOKE hex add the smoke CON bonus to their concealment value for spotting purposes (Section 14.9).

**16.10.5**  Per-hex independent dissipation means smoke clouds can develop realistic gaps — one hex clears while adjacent hexes remain thick. A player crossing through smoke should check each hex's current step as they move.

16.11  Off-Map Artillery
------------------------


**16.11.1**  Off-map artillery uses the same sealed slip and dispersion system as on-map mortars with the following differences:

**16.11.2**  Delay: 1 full turn for registered targets. 2 full turns for unregistered fire missions. Full turn delay means: called in Turn N, arrives at start of Turn N+1 or N+2 Action Phase.

**16.11.3**  A radio operator or designated FO unit with artillery contact capability is required to call off-map artillery. This capability is a scenario-defined asset — not all scenarios include it.

**16.11.4**  The number of off-map artillery support requests available is printed in the scenario parameters. Once exhausted, no further requests may be made.

**16.11.5**  Off-map artillery rFP and blast radius values are defined in the scenario parameters based on the asset available (light, medium, heavy artillery, or air support).

**16.11.6**  Off-map artillery ACC is typically 2-3 for pre-war registration and 2 for map fire, reflecting the difficulty of accurate unobserved bombardment.

**16.11.7**  The 2-turn delay for unregistered off-map artillery means calling it at the right moment is critical — the situation may have changed completely by the time rounds arrive.

16.12  Fire Mission Slip Format
-------------------------------


Fire mission slips are pre-printed components included in the game. Players fill in the following fields:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Field**
     - **Content**
   * - Mortar unit ID
     - Counter identifier (e.g. GER-81MM-1)
   * - Target hex
     - Map coordinate (e.g. D4)
   * - Mode
     - Observed / Registered / Map fire / Adjustment
   * - Called
     - Turn number and impulse number
   * - Arrives
     - Turn number and impulse number (called + delay)
   * - AMO used
     - Running total of missions fired this scenario
   * - Round type
     - HE or Smoke
