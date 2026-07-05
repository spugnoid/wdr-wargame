Section 22 — Engineers and Assault Specialists
==============================================

Combat engineers were the unit that made the impossible possible. Minefields, wire obstacles, fortified buildings, water crossings, demolished bridges — all the terrain features that stopped regular infantry cold were the engineer's working environment. At the same time, engineers were among the most dangerous close-assault specialists, their training and specialist equipment making them significantly more effective in building clearance and fortification assault than line infantry.

22.1  Engineer Counter Design
-----------------------------


**22.1.1**  Engineer counters use the wave symbol [≋] and display capability icons on the support weapon band at the bottom of the counter.

**22.1.2**  Standard engineer counter stats:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Stat**
     - **Value**
     - **Notes**
   * - M#
     - M1
     - Heavy equipment limits speed
   * - F#
     - F2
     - Standard fire capability
   * - G#
     - G5
     - High — specialist assault equipment
   * - Fire line
     - ╌ 5 ⬡4 -1
     - Standard rifle capability — engineers are trained infantry
   * - Defence
     - 7
     - Specialist equipment, trained for close combat
   * - Morale
     - 6–7
     - Selected troops, high quality across most nations


**22.1.3**  Engineer capability icons appear on the bottom support band. Each capability may be used a limited number of times per scenario. When expended, cover the icon with an EXPENDED strip — the same strip used for single-shot AT weapons.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Icon**
     - **Capability**
     - **Uses per scenario**
     - **Description**
   * - DEMO
     - Demolitions
     - 1
     - Destroy bridge, building, fortification, or road junction
   * - BRH
     - Breach
     - 1 per obstacle
     - Clear wire, hedgehog, dragon's teeth, or open minefield path
   * - MINE
     - Mine clearing
     - 1 per hex
     - Clear a minefield hex to safe passage
   * - FLAM
     - Flamethrower
     - AMO 3
     - Close-range area weapon — ignores cover
   * - BRDG
     - Assault bridge
     - Scenario asset
     - Cross water obstacles — scenario defined
   * - FORT
     - Fortification
     - Ongoing
     - Improve terrain cover value — takes multiple turns


22.2  Breaching Obstacles
-------------------------


**22.2.1**  Engineer units may attempt to breach obstacles that are impassable or prohibitively expensive for regular infantry.

**22.2.2**  Breaching action: engineer unit adjacent to or in the obstacle hex, spend 1 AP. Roll 1d6 + engineer Morale vs breach threshold:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Obstacle type**
     - **Breach threshold**
     - **Notes**
   * - Wire / fence
     - 3
     - Light obstacle — usually succeeds
   * - Hedgehog / dragon's teeth
     - 4
     - Anti-vehicle obstacles — harder for infantry
   * - Minefield — clear path
     - 5
     - Open lane only — does not clear entire hex
   * - Fortification wall / berm
     - 6
     - Reinforced construction
   * - Reinforced bunker entrance
     - 7
     - Designed to resist assault


**22.2.3**  Success: place a BREACH marker. All friendly units may use the breach — no additional AP cost, movement cost equals normal hex entry cost. Expend BRH icon on engineer counter.

**22.2.4**  Failure: attempt failed this turn. May retry next turn. BRH icon not expended on failure.

**22.2.5**  Under fire: if the engineer hex receives any fire result this turn, the breach attempt automatically fails regardless of the roll. Covering fire suppressing the enemy position is essential before breaching.

22.3  Demolitions
-----------------


**22.3.1**  Engineer units with the DEMO capability may destroy terrain features when given time to set charges.

**22.3.2**  Demolition action: engineer unit in or adjacent to target feature, spend 1 AP.

**22.3.3**  Not under fire: demolition succeeds automatically. No roll required.

**22.3.4**  Under fire (any fire result received this turn): roll 1d6 + Morale vs 5. Failure — charges not set this turn, may retry. Success — demolition proceeds.

**22.3.5**  Demolition targets and results:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Target**
     - **Result**
   * - Bridge
     - Destroyed — impassable to all units until repaired by engineers (BRDG capability, 2 turns)
   * - Building — heavy
     - Reduced to building light (+5 cover → +4 cover)
   * - Building — light
     - Reduced to rubble (+4 cover)
   * - Rubble
     - Reduced to open ground (+0 cover) — cleared
   * - Fortification / bunker
     - Reduced to entrenchment (+8 cover → +6 cover)
   * - Road junction
     - Cratered — road movement bonus lost in this hex


**22.3.6**  Expend DEMO icon after use. Each engineer counter carries one demolition charge.

22.4  Mine Clearing
-------------------


**22.4.1**  Minefield hexes impose a movement cost of 3 (all units) and a casualty risk on entry.

**22.4.2**  Mine strike: when any non-engineer unit enters a minefield hex, roll 1d6: on 1-2, the unit takes a Casualty result (mine strike). On 3-6, the unit passes safely.

**22.4.3**  Engineer units entering a minefield hex are not subject to the mine strike roll — they advance carefully with probe and detector.

**22.4.4**  Mine clearing action: engineer unit in or adjacent to minefield hex, spend 1 AP. Roll 1d6 + Morale vs 5.

**22.4.5**  Success: place BREACH marker — a safe lane has been cleared through the hex. Units using the BREACH marker are not subject to mine strike. Expend MINE icon.

**22.4.6**  Failure: clearing incomplete this turn. May retry. MINE icon not expended.

**22.4.7**  A cleared lane (BREACH marker) is a narrow path — it only protects units explicitly declared to be using the lane. A unit that moves into the hex without using the lane is still subject to mine strike.

22.5  Flamethrower
------------------


**22.5.1**  The flamethrower is a short-range area weapon that ignores cover. It was most effective in clearing fortifications, bunkers, and buildings where conventional fire was ineffective.

**22.5.2**  Flamethrower fire line:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Stat**
     - **Value**
     - **Notes**
   * - Icon
     - ≋ (wave)
     - Flamethrower weapon class
   * - rFP
     - 8
     - High lethality on impact
   * - ⬡h
     - 1
     - Loses effectiveness rapidly with range
   * - -f
     - 3
     - Steep falloff — effective only at close range
   * - Effective range
     - 0–3 hexes
     - rFP 0 at range 4+
   * - AMO
     - 3
     - Three flame attacks per scenario


**22.5.3**  Cover modifier: halved for flamethrower attacks (round down). Flame flows around and into cover rather than being blocked by it. Same principle as the grenade phase cover reduction in close assault.

**22.5.4**  Burning marker: when a flamethrower attack produces a Suppressed result or better, place a BURNING marker in the target hex in addition to the combat result.

**22.5.5**  Burning hex effects: at the start of each activation by a unit in a BURNING hex, that unit takes an automatic rFP 3 attack (no roll — just apply result thresholds to margin). Additionally all units in a BURNING hex suffer -2 CON (fire reveals position).

**22.5.6**  Extinguishing fire: a unit in a BURNING hex may spend 1 AP to attempt to extinguish. Roll 1d6 on 4+ fire is extinguished, BURNING marker removed. On 1-3 fire continues.

**22.5.7**  Fire duration: if not extinguished, BURNING marker is removed after 3 turns automatically. Buildings struck: each full turn of burning reduces the building one cover level.

**22.5.8**  Vehicle targets: flamethrower attacks target the engine deck regardless of facing arc — flames flow around the vehicle. Treat as rear arc for AV purposes. Engine fire on any penetrating result (see Rule 18.10).

**22.5.9**  Expend FLAM icon when all 3 AMO shots are used.

22.6  Building Assault
----------------------


**22.6.1**  Engineers are specialists in clearing buildings. Their training, equipment (satchel charges, shaped charges, smoke grenades), and doctrine specifically address close-quarters building assault.

**22.6.2**  When an engineer unit participates in a close assault against a building hex the following bonuses apply:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Phase**
     - **Engineer bonus**
     - **Notes**
   * - Grenade phase
     - G# + 2
     - Specialist equipment — satchel charges, shaped charges
   * - Entry fire phase
     - +2 rFP
     - Fatal funnel clearance training
   * - Melee continuation
     - +1 to all morale checks
     - Confidence and doctrine in close quarters


**22.6.3**  These bonuses apply only when the engineer unit is the assaulting unit or is in the same hex as the assaulting unit during close assault. Engineer bonuses do not apply if the engineer is providing supporting fire from an adjacent hex.

22.7  Fortification Building
----------------------------


**22.7.1**  Engineers can improve terrain cover values given sufficient uninterrupted working time.

**22.7.2**  Fortification action: engineer unit in hex, spends its entire activation each turn working. Unit cannot move or fire while fortifying.

**22.7.3**  Under fire: if the engineer hex receives any fire result during a fortification turn, work stops. Engineer must begin again on the next turn (time already invested is lost).

**22.7.4**  Fortification times and results:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Work**
     - **Turns required**
     - **Result**
   * - Open ground → Entrenchment
     - 2 turns
     - Cover +0 → Cover +6
   * - Entrenchment → Fortification
     - 4 turns
     - Cover +6 → Cover +8
   * - Building → Reinforced building
     - 3 turns
     - Cover +4 or +5 → +1 additional
   * - Rubble → Field position
     - 2 turns
     - Cover +4 → irregular cover, counts as entrenchment


**22.7.5**  Place a FORT marker showing current state. Multiple engineer units working on the same position halve the time required (minimum 1 turn per stage).

22.8  Assault Bridge
--------------------


**22.8.1**  Assault bridges are scenario-defined assets available to engineer units. Not all scenarios include them.

**22.8.2**  Bridge deployment: engineer unit at water obstacle edge, spend 2 AP. Roll 1d6 + Morale vs 5 (vs 7 if under fire).

**22.8.3**  Success: bridge placed — BRDG marker at obstacle. All units may cross at normal movement cost. Expend BRDG capability.

**22.8.4**  Failure: may retry next turn. 2 AP cost again.

**22.8.5**  Bridge capacity: all unit types including vehicles.

**22.8.6**  Bridge destruction: a bridge takes a Casualty result from any fire directed at the BRDG marker hex — remove BRDG marker, obstacle impassable again.

22.9  Representative 1943 Engineer Counters
-------------------------------------------


.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit**
     - **Fire line**
     - **G#**
     - **Capabilities**
     - **Defence**
     - **Morale**
     - **Notes**
   * - German Pioneer squad (Pioniere) — veteran
     - ╌ 5 ⬡4 -1
     - G5
     - DEMO BRH MINE FLAM
     - 7
     - 6
     - Full assault pioneer capability including flamethrower
   * - German Pioneer squad (Pioniere) — regular
     - ╌ 5 ⬡4 -1
     - G5
     - DEMO BRH MINE FLAM
     - 7
     - 6
     - Standard assault engineers
   * - Soviet Sapper squad — regular
     - ╌ 4 ⬡4 -1
     - G4
     - DEMO BRH MINE
     - 6
     - 5
     - No organic flamethrower — separate flamethrower units
   * - Soviet Assault engineer — veteran
     - ╌ 5 ⬡4 -1
     - G5
     - DEMO BRH MINE FLAM
     - 7
     - 7
     - 1943+ specialist assault units — Guards Sapper battalions
   * - British Royal Engineers — regular
     - ╌ 5 ⬡4 -1
     - G4
     - DEMO BRH MINE BRDG
     - 7
     - 6
     - Strong bridge capability — BRDG standard
   * - US Combat Engineers — regular
     - ╌ 5 ⬡4 -1
     - G4
     - DEMO BRH MINE BRDG
     - 7
     - 6
     - Similar to British — strong logistics engineering


.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Summed Effective rFP**
     - **Resolution FP**
   * - 1
     - 1
   * - 2
     - 2
   * - 3
     - 4
   * - 4
     - 5
   * - 5
     - 5
   * - 6
     - 6
   * - 7
     - 7
   * - 8
     - 7
   * - 9
     - 8
   * - 10
     - 8
   * - 12
     - 9
   * - 15
     - 9
   * - 18
     - 10
   * - 24
     - 11
   * - 30
     - 11
   * - 40
     - 12
   * - 50+
     - 12 (maximum)


Values between listed entries: round down to the nearest listed value. Example: summed effective rFP of 11 uses the row for 10 (Resolution FP 8).
