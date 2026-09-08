Section 22 — Scenario Design Guidelines
=======================================

This section provides guidelines for designing With Deepest Regret... scenarios. It is written for scenario designers — players who want to create their own engagements rather than use pre-designed scenarios. Following these guidelines will produce scenarios with historically plausible outcomes and balanced tactical decisions.

22.1  Scenario Parameter Block
-------------------------------


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

.. container:: rule-guide

   **Why:** Publishing expected outcomes by ratio gives a scenario designer a concrete lever for the kind of game they want to produce — a desperate defence, a balanced fight, or a foregone-conclusion pursuit — rather than guessing at force sizes and discovering the balance only through playtesting.

   **Example:** A designer wanting a tense, evenly matched scenario picks a 1.5:1 attacker-to-defender ratio rather than 3:1, since the table shows 1.5:1 as the entry where both sides have genuine winning lines.

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

.. container:: rule-guide

   **Why:** Leaders and support assets don't independently hold ground or trade fire the way combat units do, so including them in the ratio would inflate a force's apparent strength without reflecting its actual tactical weight on the table.

   **Example:** A German force of 4 rifle squads plus 1 attached leader counts as 4 combat units for ratio purposes — the leader is excluded even though it's a valuable counter in play.

**22.2.3**  Quality adjusts the ratio. A veteran unit is worth approximately 1.5 regular units for ratio purposes. An elite unit is worth approximately 2 regular units. A green unit is worth approximately 0.6 regular units.

.. container:: rule-guide

   **Why:** A raw unit count treats a green conscript squad the same as an elite veteran squad, which doesn't reflect their actual combat value — these multipliers let a designer calculate an effective ratio that accounts for the real difference training and experience make.

   **Example:** 2 veteran German squads count as 2 × 1.5 = 3.0 effective units for ratio purposes, worth exactly as much as 5 green Soviet conscript squads at 5 × 0.6 = 3.0.

**22.2.4**  Vehicle units count as 2 combat units for ratio purposes at tactical scale. A heavy tank (Tiger, KV-1) counts as 3.

.. container:: rule-guide

   **Why:** A single tank brings vastly more firepower and battlefield impact than a single infantry squad, so weighting it at 2 (or 3 for a heavy tank) keeps the force ratio meaningful when comparing mixed infantry-and-armour forces rather than treating every counter as equivalent.

   **Example:** A defending force of 3 infantry squads plus 1 Tiger tank counts as 3 + 3 = 6 effective combat units for ratio purposes, not just 4.

22.3  Force Morale Calculation
-------------------------------


**22.3.1**  Calculate Force Morale for each side at scenario design time and record it on the scenario sheet. Players need this value at the start of play.

.. container:: rule-guide

   **Why:** Force Morale (Section 15) drives collapse checks throughout the scenario, so it must be known before the first unit is ever placed — calculating it during play would leave players uncertain about a value the rules assume is already fixed.

   **Example:** Before setup begins, the scenario designer works out each side's Force Morale and writes it directly on the scenario sheet, so both players know the collapse thresholds from Turn 1.

**22.3.2**  Force Morale = total combat unit count × force factor (round down, minimum 1).

.. container:: rule-guide

   **Why:** Scaling Force Morale by unit count reflects that a larger force can absorb more losses before its collective will to fight breaks, while the minimum-1 floor guarantees even a tiny force has some resilience rather than collapsing on its very first casualty.

   **Example:** A force of 6 units with a factor of 0.4 has Force Morale = floor(6 × 0.4) = floor(2.4) = 2.

**22.3.3**  Force factors:

.. container:: rule-guide

   **Why:** Higher factors for elite and veteran forces reflect that better-trained, higher-morale troops absorb losses without collapsing more readily than green or conscript forces — this table is what converts a force's quality composition into a concrete Force Morale multiplier.

   **Example:** An entirely elite SS force uses factor 0.6, giving it a proportionally higher Force Morale than an equally sized predominantly-green force using factor 0.3, reflecting the elite force's greater resilience to losses.

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

.. container:: rule-guide

   **Why:** A fully worked example removes any ambiguity about how the weighted-average formula in Rule 22.3.3 is actually applied to a mixed-quality force, since summing per-unit factors rather than averaging the two factors directly is easy to get wrong without seeing it done once.

   **Example:** Following the same method for a Soviet force of 2 veteran (0.5) and 6 regular (0.4) units: Force Morale = floor(2×0.5 + 6×0.4) = floor(3.4) = 3.

**22.3.5**  Record Force Morale on the scenario sheet. Do not recalculate during play — the value is fixed at scenario start.

.. container:: rule-guide

   **Why:** Locking Force Morale at scenario start prevents it from drifting as units are damaged or eliminated during play, which would make collapse thresholds a moving target and undermine the whole point of pre-calculating the value in Rule 22.3.1.

   **Example:** Even after Germans lose two units in the fighting, their scenario sheet still lists the original Force Morale of 3 calculated before the scenario began — that value never changes mid-play.

22.4  Terrain Density Guidelines
---------------------------------


**22.4.1**  Terrain density determines the tactical style of the scenario. Use these guidelines:

.. container:: rule-guide

   **Why:** The proportion of cover on the map fundamentally shapes what kind of fight results — open terrain favours vehicles and firepower while dense terrain favours infantry and close assault — so a designer choosing terrain density is really choosing the scenario's tactical identity.

   **Example:** A designer wanting a vehicle-dominant tank battle sets terrain density under 20% (open steppe), while a designer wanting an infantry-focused close-quarters fight aims for 40-60% (dense village or bocage terrain).

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

.. container:: rule-guide

   **Why:** Terrain that exists only to look historically appropriate but has no mechanical effect on movement, LOS, or cover wastes map space that could otherwise be shaping meaningful decisions — every feature should earn its place by affecting how the scenario actually plays.

   **Example:** A designer adding a small woods patch checks that it either blocks LOS along an approach lane, offers a defensible fallback position, or funnels attackers around it — rather than placing it purely because a real farmhouse map had trees there.

**22.4.3**  Ensure at least one covered approach route exists for each attacking force. A map with no covered approach makes the attacker's task nearly impossible and produces a one-sided scenario regardless of force ratio.

.. container:: rule-guide

   **Why:** Even a favourable force ratio (Rule 22.2.1) can't compensate for an attacker forced to cross open ground under fire the entire way — this is the terrain-design safeguard that keeps a well-calculated force ratio from being undermined by a map that makes the advance mechanically impossible.

   **Example:** A designer reviewing a completed map notices the attacker's only route to the objective crosses open ground with no woods, buildings, or dead ground to use — they add a hedgerow line to create at least one viable covered approach before finalising the scenario.

**22.4.4**  Objectives should be defensible terrain — buildings, high ground, prepared positions. An objective in open ground with no natural cover produces poor defensive play because the defender has no tactical advantage to exploit.

.. container:: rule-guide

   **Why:** If the objective itself offers no cover, the defender gains nothing from holding it tactically and the scenario reduces to a pure numbers contest — placing objectives on defensible terrain ensures the defending side has real decisions to make about how to use that advantage.

   **Example:** A designer places the German objective on a heavy-building hex rather than an open field, giving the defending force a genuine +5 cover advantage worth fighting to hold rather than an arbitrary point on the map.

22.5  Turn Limit Guidelines
-----------------------------


**22.5.1**  Turn limits should be set so that: a well-played attacker can just achieve the objective in time; a poorly-played attacker cannot; a well-played defender can hold to the limit without being eliminated.

.. container:: rule-guide

   **Why:** This three-part test is what separates a well-designed turn limit from an arbitrary one — a limit that's too generous removes urgency, one that's too tight makes the attacker's task impossible regardless of skill, and this rule gives designers a concrete standard to playtest against.

   **Example:** A designer playtesting their scenario finds a skilled attacker reaches the objective with 2 turns to spare — they tighten the turn limit until only strong play, not mediocre play, can just make it in time.

**22.5.2**  As a starting point, estimate the number of turns the attacker needs to cross the map and engage the objective, then add 1-2 turns for tactical complications.

.. container:: rule-guide

   **Why:** Starting from a pure movement-time calculation and padding it for combat friction gives designers a quick, repeatable first estimate rather than guessing at a turn count from scratch — the padding accounts for the reality that combat rarely goes exactly as planned.

   **Example:** An attacker needs roughly 3 turns of movement to reach the objective given the map's size and terrain — the designer sets an initial turn limit of 4-5 turns to account for enemy resistance along the way.

**22.5.3**  Rough turn estimates by scenario type:

.. container:: rule-guide

   **Why:** Different scenario archetypes have structurally different pacing needs — a raid needs time budgeted for withdrawal that a straightforward assault doesn't, and a delay scenario needs more turns to let withdrawal mechanics play out — so a single blanket turn-count guideline wouldn't fit every scenario type equally well.

   **Example:** A designer building a raid scenario budgets 5-7 turns specifically because that estimate already accounts for the attacker needing time to strike the objective and then withdraw, unlike a straightforward assault scenario's 5-7 turn estimate which covers only the advance.

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

.. container:: rule-guide

   **Why:** The estimation guidelines in Rules 22.5.2-22.5.3 are starting points, not guarantees — actual play routinely reveals frictions a paper calculation misses, and this rule flags the single most common failure mode designers should specifically watch for.

   **Example:** A designer who calculated a 5-turn limit on paper playtests the scenario and finds even a well-played attacker consistently falls one turn short due to unexpected suppression along the approach — they add a turn rather than assuming the attacker simply played badly.

22.6  Victory Conditions
--------------------------


**22.6.1**  Victory conditions define what each side is trying to achieve. Clear, unambiguous conditions are essential — players should never be uncertain whether a condition has been met.

.. container:: rule-guide

   **Why:** An ambiguous victory condition creates disputes at the exact moment a scenario should be delivering a clean, satisfying resolution — stating this principle up front sets the bar every condition type in Rule 22.6.2 is designed to meet.

   **Example:** "Germans control the village" is ambiguous (which hexes count as "the village"?), while "Germans control hex F4 at end of Turn 6" leaves no room for dispute — exactly the clarity this rule requires.

**22.6.2**  Victory condition types:

.. container:: rule-guide

   **Why:** Different scenario concepts call for different ways of measuring success — a defensive stand is best measured by survival to a time limit, while a raid is better measured by casualties inflicted — so offering several condition types lets a designer match the win condition to the story the scenario is telling.

   **Example:** A designer building a raid scenario chooses a casualty-threshold victory condition ("Soviets lose 4 or more units") rather than objective control, since the raid's premise is about inflicting damage and withdrawing, not holding ground.

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

.. container:: rule-guide

   **Why:** "Objective control" (Rule 22.6.2) is meaningless without a precise definition of what counts as controlling a hex — this rule closes the exact loophole that would otherwise let players argue over a contested hex at the moment victory is being determined.

   **Example:** At the scenario's end, a German unit and a Soviet unit both occupy the objective hex — under this rule, neither side controls it, so an objective-control victory condition is not met by either player.

**22.6.4**  Victory point scenarios require pre-defined VP values for each condition recorded on the scenario sheet. Calculate total possible VP for each side and verify the scenario is winnable from both sides.

.. container:: rule-guide

   **Why:** A combined VP scenario (Rule 22.6.2) can accidentally be unwinnable for one side if the designer never adds up the maximum achievable points — checking both sides' totals before finalising the scenario is a basic sanity check against building a scenario that is a foregone conclusion.

   **Example:** A designer totals the maximum VP available to each side in a combined-condition scenario and discovers the Soviet side can never reach more than 2VP against the Germans' guaranteed 3VP — they rebalance the point values before publishing the scenario.

22.7  Recovery Window Selection
---------------------------------


**22.7.1**  Recovery Window is a campaign parameter set by the scenario designer. It represents time elapsed between scenarios in campaign play.

.. container:: rule-guide

   **Why:** Campaign play needs a way to represent the passage of time between linked scenarios — how much reorganisation, resupply, and recovery a force gets before its next fight — and Recovery Window is the single parameter that captures that for the whole scenario chain.

   **Example:** A campaign designer chaining two scenarios together sets a Days Recovery Window between them, representing roughly 1-3 days during which both sides can reorganise and resupply before the next engagement.

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

.. container:: rule-guide

   **Why:** A defeated force historically had less opportunity to reorganise — it was often still under pressure, retreating, or reeling from losses — so stepping the Recovery Window down for the loser creates a mechanical spiral that mirrors how real defeats compound rather than resolve cleanly between engagements.

   **Example:** A Soviet force that loses a scenario with a Hours Recovery Window enters the next linked scenario at None — no recovery at all — compounding the pressure from their defeat exactly as the rule intends.

**22.7.3**  Set Recovery Windows honestly based on historical context. German forces in the summer of 1944 frequently had no recovery time between actions — this should be reflected in the campaign chain.

.. container:: rule-guide

   **Why:** Recovery Window is meant to model actual historical operational tempo, not simply give designers a free knob to balance difficulty — choosing it honestly based on the historical situation keeps campaign chains grounded in the real pressures forces faced rather than artificial game balancing.

   **Example:** A campaign designer depicting the German retreat through France in summer 1944 sets None or Hours Recovery Windows throughout the chain, reflecting the historical reality of near-continuous contact rather than picking Extended just to make the campaign easier on the German side.

22.8  FIXED Unit Placement
----------------------------


**22.8.1**  FIXED units represent ambush positions, prepared defensive positions, and units not yet in contact. Their positions must be recorded on the scenario record sheet before play begins.

.. container:: rule-guide

   **Why:** Recording FIXED positions before play starts is what makes the concealment mechanic (Section 14.7) trustworthy — if a position could be decided or adjusted after seeing the opponent's moves, it would no longer represent a genuine prepared ambush or defensive stance established in advance.

   **Example:** Before the scenario begins, the defending player writes down the exact hex of their FIXED HMG team on the record sheet, sealing that decision before either side has seen the other's setup.

**22.8.2**  Both players must agree that all FIXED positions have been recorded before the scenario begins. Neither player may add FIXED units after setup is complete.

.. container:: rule-guide

   **Why:** Requiring mutual agreement before play starts closes off any opportunity to quietly add a FIXED unit later, once the tactical situation has developed — without this checkpoint, a player could effectively cheat by "discovering" they'd secretly hidden a unit wherever it would be most advantageous.

   **Example:** Both players confirm the recorded FIXED positions and sign off before Turn 1 begins — from that point on, neither side can claim an additional hidden unit exists that wasn't on the original record sheet.

**22.8.3**  FIXED units must be placed within their designated setup zone unless the scenario specifically permits otherwise.

.. container:: rule-guide

   **Why:** Without this constraint, FIXED placement could otherwise be used to plant ambush units anywhere on the map, undermining the setup-zone separation (Rule 22.9.2-22.9.3) that governs how the scenario's approach and contact phase is meant to unfold.

   **Example:** A defender cannot place a FIXED HMG team deep inside the attacker's own setup zone unless the scenario explicitly calls for that kind of infiltration ambush — normally, FIXED units stay within the defender's own designated zone.

**22.8.4**  Guidelines for FIXED unit placement by scenario type:

.. container:: rule-guide

   **Why:** How much concealment is appropriate depends heavily on the scenario's premise — an ambush calls for the ambushing side to be entirely hidden while the victim is visible, while a patrol scenario calls for mutual uncertainty on both sides — so FIXED placement guidance is tied to scenario archetype rather than being a single fixed rule.

   **Example:** A designer building an ambush scenario places the ambushing German force entirely as FIXED per this table's guidance, while the Soviet "victim" convoy is placed fully VISIBLE, since it's moving along a known route unaware of the threat.

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


**22.8.5**  FIXED units have no markers at all until they act (Rule 14.7.1), so there is no such thing as a FIXED dummy marker. This guideline instead limits **recorded decoy positions**: a scenario may let the defender record up to one decoy position per real FIXED unit on the record sheet — a decoy behaves like a FIXED unit's recorded hex for Rule 14.7.7 (an enemy entering it halts and the "position" is revealed as empty) but can never fire or transition. More decoys than real units becomes implausible and tedious.

.. container:: rule-guide

   **Why:** Since FIXED units have no physical marker to duplicate, a decoy has to be defined as a purely record-sheet concept — a written position that behaves like a real FIXED unit for triggering an enemy halt, without ever being able to actually fight; capping decoys at one-per-real-unit keeps this "fog of war" tool from becoming an implausible flood of empty hexes.

   **Example:** A defender with 3 real FIXED units may record up to 3 decoy positions on the sheet — an attacking unit that enters a decoy hex halts and discovers it empty, exactly as if it had triggered a real FIXED position, but that decoy could never have fired back.

22.9  Setup Zone Guidelines
-----------------------------


**22.9.1**  Setup zones define where each side deploys at scenario start. They should be defined in hexes or columns on the scenario sheet.

.. container:: rule-guide

   **Why:** A precisely defined setup zone (rather than a vague area) removes any ambiguity about where units can legally be placed at the start of the scenario, preventing disputes before the game has even begun.

   **Example:** A scenario sheet specifies "Germans: columns A-B" rather than "Germans deploy on the western side" — the exact column boundary leaves no room for interpretation.

**22.9.2**  Setup zones should not overlap — both sides occupying the same zone at scenario start produces an immediate engagement that bypasses the approach and contact mechanics.

.. container:: rule-guide

   **Why:** The approach-and-contact phase is a deliberate part of the game's pacing — overlapping setup zones would collapse that phase entirely, dropping both sides straight into close combat without the maneuvering and positioning decisions the early turns are meant to provide.

   **Example:** A designer checking their scenario sheet catches that both sides' setup zones both include column D — they narrow one zone so the two no longer overlap before finalising the scenario.

**22.9.3**  Minimum separation between setup zone edges: 4 hexes (160 yards) for infantry-only scenarios. 6 hexes (240 yards) for scenarios including vehicles — longer engagement ranges require more separation.

.. container:: rule-guide

   **Why:** Vehicles engage effectively at longer ranges than infantry small-arms fire, so a separation adequate for an infantry-only scenario would let vehicles start the game already within effective firing range of each other — the larger minimum for vehicle scenarios preserves a genuine approach phase.

   **Example:** A scenario with only infantry uses the 4-hex minimum separation, but a scenario adding a platoon of tanks on each side is designed with 6 hexes of separation instead, so the tanks don't start the game already trading fire.

**22.9.4**  The defender should have at least one turn to reach and occupy key terrain before the attacker can engage at effective range. If the attacker can reach effective fire range in one activation from their setup zone, the defender has no time to set up — increase separation or restrict attacker setup depth.

.. container:: rule-guide

   **Why:** A defender who can't reach their prepared position before being engaged loses the entire tactical premise of playing the defensive side — this rule is the practical test a designer applies to verify the minimum separations in Rule 22.9.3 actually deliver a genuine defensive setup phase, not just a technical distance requirement.

   **Example:** A designer playtests their scenario and finds the attacker's fastest unit can reach effective firing range against the defender's objective in a single turn — they widen the setup zone separation so the defender gets at least one full turn to occupy their position first.

22.10  Scenario Design Checklist
----------------------------------


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
------------------------------------------------


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
     - 4 German combat units vs 3 Soviet (leaders not counted, Rule 22.2.2) — adjusted for quality per Rule 22.2.3: German 2×1.5 + 2×1.0 = 5.0 vs Soviet 1×1.5 + 2×1.0 = 3.5, approximately **1.4:1**
   * - Force Morale (Germans)
     - floor(2×0.5 + 2×0.4) = floor(1.8) = **1** (weighted average, Rule 22.3.3)
   * - Force Morale (Soviets)
     - floor(1×0.5 + 2×0.4) = floor(1.3) = **1** (minimum 1)
   * - German setup zone
     - Column A only
   * - Soviet setup zone
     - Column F only (4-hex separation, meeting Rule 22.9.3's infantry minimum)
   * - German objective
     - Occupy hex E3 (heavy building) by end of Turn 4
   * - Soviet objective
     - Prevent German occupation of E3 through Turn 4
   * - FIXED units
     - Soviets may place DP-28 team as FIXED
   * - Special conditions
     - None


*NOTE: this parameter block is recomputed to follow this section's own rules — the original draft counted the platoon leader as a combat unit, used a flat 0.45 factor instead of 22.3.3's weighted average, and placed setup zones 2 hexes apart against 22.9.3's 4-hex minimum. At this skirmish's size both Force Morale values floor to 1, so the first CI unit on either side triggers a collapse check — small engagements are brittle by construction, which suits a 4-turn farmhouse fight; designers wanting more resilience at this scale should add units, not inflate the factor.*
