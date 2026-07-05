Section 22 — Scenario Design Guidelines
=======================================

This section provides guidelines for designing With Deepest Regret... scenarios. It is written for scenario designers — players who want to create their own engagements rather than use pre-designed scenarios. Following these guidelines will produce scenarios with historically plausible outcomes and balanced tactical decisions.

22.1  Scenario Parameter Block
------------------------------


Every scenario sheet must include the following parameters. Players read these before setup to understand the tactical situation.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Parameter**
     - **Description**
     - **Example**
   * - Scenario title
     - Short descriptive name
     - Farmhouse at Prokhorovka
   * - Historical date
     - Date of the action
     - July 12, 1943
   * - Theatre / front
     - Geographic context
     - Eastern Front, Kursk salient
   * - Turn limit
     - Number of game turns
     - 6 turns
   * - Recovery Window
     - Time between scenarios in campaign play
     - Hours
   * - Map size
     - Grid dimensions
     - 12 × 8 hexes
   * - Scale
     - Tactical (40 yds) or Operational (250 yds)
     - Tactical
   * - Victory conditions
     - What each side must achieve
     - See Rule 22.6
   * - Special conditions
     - Scenario-specific rules
     - Night: visibility 2 hexes
   * - Off-map artillery
     - Available support requests per side
     - Germans: 2 × 81mm battery
   * - Force Morale values
     - Pre-calculated for each side
     - Germans: 4 / Soviets: 3
   * - Setup zones
     - Where each side deploys
     - Germans: columns A–B / Soviets: columns G–H


22.2  Force Ratio Guidelines
----------------------------


**22.2.1**  Force ratios determine the likely outcome before play begins. Use these guidelines to design scenarios with meaningful decisions rather than foregone conclusions:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Attacker:Defender ratio**
     - **Expected outcome**
     - **Design intent**
   * - 1:1
     - Defender advantage — attacker rarely wins without significant tactical skill
     - Desperate defence scenario · attacker needs perfect play
   * - 1.5:1
     - Roughly balanced — quality and tactics decide
     - Standard balanced scenario · both sides have winning lines
   * - 2:1
     - Attacker advantage — defender needs terrain and prepared positions
     - Standard assault scenario · attacker wins with decent play
   * - 3:1
     - Attacker should win — defender can delay but not hold
     - Pursuit or breakout scenario · question is attacker's cost
   * - 3:1+ with prepared positions
     - Roughly balanced
     - Attacker needs fire support and good tactics


**22.2.2**  Count only combat units for force ratio calculations. Leaders, supply units, and off-map assets are not counted.

**22.2.3**  Quality adjusts the ratio. A veteran unit is worth approximately 1.5 regular units for ratio purposes. An elite unit is worth approximately 2 regular units. A green unit is worth approximately 0.6 regular units.

**22.2.4**  Vehicle units count as 2 combat units for ratio purposes at tactical scale. A heavy tank (Tiger, KV-1) counts as 3.

22.3  Force Morale Calculation
------------------------------


**22.3.1**  Calculate Force Morale for each side at scenario design time and record it on the scenario sheet. Players need this value at the start of play.

**22.3.2**  Force Morale = total combat unit count × force factor (round down, minimum 1).

**22.3.3**  Force factors:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Force composition**
     - **Factor**
   * - Entirely elite (SS, Guards, airborne, Rangers)
     - 0.6
   * - Predominantly veteran
     - 0.5
   * - Predominantly regular
     - 0.4
   * - Predominantly green / conscript / militia
     - 0.3
   * - Mixed — calculate weighted average
     - Sum (units × individual factor) ÷ total units


**22.3.4**  Example: German force of 8 units, 3 veteran (factor 0.5) and 5 regular (factor 0.4). Force Morale = floor(3×0.5 + 5×0.4) = floor(3.5) = 3 (round down, minimum 1 — Rule 15.5.1).

**22.3.5**  Record Force Morale on the scenario sheet. Do not recalculate during play — the value is fixed at scenario start.

22.4  Terrain Density Guidelines
--------------------------------


**22.4.1**  Terrain density determines the tactical style of the scenario. Use these guidelines:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Density**
     - **Cover hexes / total hexes**
     - **Tactical character**
   * - Open (steppe, airfield, large field)
     - < 20%
     - Vehicle-dominant · range and firepower decide · infantry vulnerable without cover
   * - Mixed (typical countryside)
     - 20–40%
     - Combined arms · terrain channels movement · smoke and indirect fire important
   * - Dense (village, forest, bocage)
     - 40–60%
     - Infantry-dominant · close range · vehicles vulnerable without infantry screens
   * - Extremely dense (urban, heavy forest)
     - > 60%
     - Close assault focus · mortars and grenades dominate · vehicles nearly useless without engineers


**22.4.2**  Place terrain to create tactical decisions, not decoration. Every terrain feature should do one of: channel movement, provide a defensible position, create a covered approach route, or obstruct LOS in a tactically meaningful way.

**22.4.3**  Ensure at least one covered approach route exists for each attacking force. A map with no covered approach makes the attacker's task nearly impossible and produces a one-sided scenario regardless of force ratio.

**22.4.4**  Objectives should be defensible terrain — buildings, high ground, prepared positions. An objective in open ground with no natural cover produces poor defensive play because the defender has no tactical advantage to exploit.

22.5  Turn Limit Guidelines
---------------------------


**22.5.1**  Turn limits should be set so that: a well-played attacker can just achieve the objective in time; a poorly-played attacker cannot; a well-played defender can hold to the limit without being eliminated.

**22.5.2**  As a starting point, estimate the number of turns the attacker needs to cross the map and engage the objective, then add 1-2 turns for tactical complications.

**22.5.3**  Rough turn estimates by scenario type:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Scenario type**
     - **Typical turn limit**
     - **Notes**
   * - Assault (attacker crosses full map)
     - 5–7 turns
     - Tight enough to create urgency
   * - Meeting engagement (forces start near centre)
     - 4–6 turns
     - Both sides have offensive options
   * - Defence (attacker crosses half map)
     - 4–5 turns
     - Attacker has less distance to cover
   * - Delay (defender withdraws, attacker pursues)
     - 6–8 turns
     - Extended time for withdrawal mechanics
   * - Raid (attacker strikes objective and withdraws)
     - 5–7 turns
     - Include withdrawal time in estimate


**22.5.4**  Always playtest the turn limit before finalising. The most common error is setting too few turns — the attacker never has a realistic chance.

22.6  Victory Conditions
------------------------


**22.6.1**  Victory conditions define what each side is trying to achieve. Clear, unambiguous conditions are essential — players should never be uncertain whether a condition has been met.

**22.6.2**  Victory condition types:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Type**
     - **Definition**
     - **Example**
   * - Objective control
     - One side controls a specific hex or hexes at a defined point
     - Germans control hex F4 at end of Turn 6
   * - Force morale collapse
     - One side's Force Morale collapses during play
     - Automatic — built into the rules
   * - Casualty threshold
     - One side loses a specific number of units
     - Soviets lose 4 or more units
   * - Time limit survival
     - Defender holds until turn limit expires
     - Soviets prevent German objective control through Turn 5
   * - Combined
     - Multiple conditions, weighted by VP
     - Control objective = 3VP · each enemy CI = 1VP


**22.6.3**  Define occupation clearly: a side controls an objective hex when they have at least one combat unit in the hex and the opponent has none. A hex with both sides present is contested — neither side controls it.

**22.6.4**  Victory point scenarios require pre-defined VP values for each condition recorded on the scenario sheet. Calculate total possible VP for each side and verify the scenario is winnable from both sides.

22.7  Recovery Window Selection
-------------------------------


**22.7.1**  Recovery Window is a campaign parameter set by the scenario designer. It represents time elapsed between scenarios in campaign play.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Recovery Window**
     - **Historical equivalent**
     - **When to use**
   * - None
     - Immediate continuation — hours apart
     - Back-to-back actions · continuous operation · no time to collect wounded
   * - Hours
     - Same day, later · 4–12 hours
     - Multiple actions in one day · partial reorganisation possible
   * - Days
     - 1–3 days between actions
     - Standard operational tempo · reorganisation and resupply possible
   * - Extended
     - Week or more
     - Operational pause · full recovery possible · replacements arrive


**22.7.2**  The losing side in a scenario has their Recovery Window reduced one step. A force that loses a scenario and has only Hours recovery will fight the next scenario with no recovery at all — compounding pressure that models real operational dynamics.

**22.7.3**  Set Recovery Windows honestly based on historical context. German forces in the summer of 1944 frequently had no recovery time between actions — this should be reflected in the campaign chain.

22.8  FIXED Unit Placement
--------------------------


**22.8.1**  FIXED units represent ambush positions, prepared defensive positions, and units not yet in contact. Their positions must be recorded on the scenario record sheet before play begins.

**22.8.2**  Both players must agree that all FIXED positions have been recorded before the scenario begins. Neither player may add FIXED units after setup is complete.

**22.8.3**  FIXED units must be placed within their designated setup zone unless the scenario specifically permits otherwise.

**22.8.4**  Guidelines for FIXED unit placement by scenario type:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Scenario type**
     - **FIXED unit guidelines**
   * - Assault (attacker vs prepared defender)
     - Defender may place all units as FIXED. Attacker units are VISIBLE — they are advancing and known to be present.
   * - Meeting engagement
     - Both sides may place up to half their units as FIXED. Represents advance elements not yet in contact.
   * - Ambush
     - Ambushing side places all units as FIXED. Victim side places all units as VISIBLE — they are moving on a route.
   * - Patrol
     - Both sides may place any unit as FIXED. High hidden unit density — spotting and information are primary tactical challenges.


**22.8.5**  Limit FIXED dummy markers to a number equal to actual FIXED units — one dummy per real FIXED unit. More dummies than real units becomes implausible and tedious.

22.9  Setup Zone Guidelines
---------------------------


**22.9.1**  Setup zones define where each side deploys at scenario start. They should be defined in hexes or columns on the scenario sheet.

**22.9.2**  Setup zones should not overlap — both sides occupying the same zone at scenario start produces an immediate engagement that bypasses the approach and contact mechanics.

**22.9.3**  Minimum separation between setup zone edges: 4 hexes (160 yards) for infantry-only scenarios. 6 hexes (240 yards) for scenarios including vehicles — longer engagement ranges require more separation.

**22.9.4**  The defender should have at least one turn to reach and occupy key terrain before the attacker can engage at effective range. If the attacker can reach effective fire range in one activation from their setup zone, the defender has no time to set up — increase separation or restrict attacker setup depth.

22.10  Scenario Design Checklist
--------------------------------


Before finalising a scenario, verify the following:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Check**
     - **Criterion**
   * - Force ratio calculated
     - Attacker:Defender ratio within intended range
   * - Quality adjustment applied
     - Veteran/elite/green units factored into effective ratio
   * - Force Morale calculated
     - Both sides' Force Morale values recorded on scenario sheet
   * - Covered approach exists
     - At least one covered approach route for attacker
   * - Objective is defensible
     - Objective hex has natural cover or prepared position
   * - Turn limit playtested
     - Attacker can just achieve objective with good play
   * - Victory conditions unambiguous
     - No possible dispute about whether condition is met
   * - Recovery Window set
     - Appropriate to historical context
   * - FIXED positions recorded
     - All setup agreed before play begins
   * - Setup zones defined
     - Minimum separation maintained
   * - Special conditions noted
     - Night, weather, restricted terrain, off-map assets
   * - Both sides have decisions
     - Neither side has an obviously dominant strategy


22.11  Historical Scenario Example Parameters
---------------------------------------------


The following parameters represent the Farmhouse at Prokhorovka test scenario used during rules development. It is provided as a worked example of a complete scenario parameter block.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Parameter**
     - **Value**
   * - Title
     - Farmhouse at Prokhorovka
   * - Date
     - July 12, 1943
   * - Theatre
     - Eastern Front — Kursk salient
   * - Scale
     - Tactical (40 yards per hex)
   * - Map
     - 6 × 6 hexes
   * - Turn limit
     - 4 turns
   * - Recovery Window
     - Hours (campaign play)
   * - German forces
     - 2 × PZGR 43 (veteran) · 1 × GREN 43 (regular) · 1 × MG42 HMG · 1 × German Platoon Leader CMD3
   * - Soviet forces
     - 1 × GDS 43 (veteran) · 1 × RIF 43 (regular) · 1 × DP-28 team · 1 × Soviet Guards Platoon Leader CMD3
   * - Force ratio
     - 5 German vs 3 Soviet — approximately 1.7:1 adjusted for quality
   * - Force Morale (Germans)
     - 5 × 0.45 (mixed) = 2 — rounds to 2
   * - Force Morale (Soviets)
     - 3 × 0.45 (mixed) = 1 — minimum 1
   * - German setup zone
     - Columns A–B
   * - Soviet setup zone
     - Columns E–F
   * - German objective
     - Occupy hex E3 (heavy building) by end of Turn 4
   * - Soviet objective
     - Prevent German occupation of E3 through Turn 4
   * - FIXED units
     - Soviets may place DP-28 team as FIXED
   * - Special conditions
     - None
