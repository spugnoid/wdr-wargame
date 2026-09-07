Section 4 — Terrain
===================

4.1  Terrain Types
------------------


**4.1.1**  Each hex is assigned a terrain type. The terrain type determines the cover modifier it provides to units occupying it and any LOS penalty it applies to fire passing through it.

**4.1.2**  A hex may contain only one terrain type for game purposes. When a hex contains mixed terrain, the dominant terrain type is used.

**4.1.3**  Hexside terrain: walls, fences, and hedgerows are linear features printed on **hexsides**, not hexes. A hexside feature provides its cover modifier only against fire whose line of fire crosses that hexside into the unit's hex — a squad behind a wall is protected from the field beyond it, not from fire coming through its own gate side. Hexside cover does not stack with the hex's own terrain cover: use the better of the two. Crossing a hexside feature costs movement per the Rule 7.2 table; its intervening-fire penalty applies once per such hexside the line of fire crosses (Rule 4.3).

4.2  Cover Modifiers
--------------------


Cover modifiers are added to the defender's Defence value when resolving fire combat. They represent the protection afforded by the terrain the target occupies. The open ground baseline is +0.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Terrain**
     - **Cover Modifier**
     - **Notes**
   * - Open ground
     - +0
     - Baseline — troops going prone
   * - Crops / tall grass
     - +1
     - Concealment, minimal protection
   * - Wall / fence (hexside — Rule 4.1.3)
     - +2
     - Only vs fire crossing that hexside; not cumulative with hex cover
   * - Hedgerow / bocage (hexside — Rule 4.1.3)
     - +2
     - Only vs fire crossing that hexside; not cumulative with hex cover
   * - Light woods / orchard
     - +3
     - Scattered trees and undergrowth
   * - Ditch / sunken road
     - +3
     - Natural defilade
   * - Dense woods
     - +4
     - Heavy vegetation and tree mass
   * - Building — light (wood/plaster)
     - +4
     - Structural cover
   * - Rubble
     - +4
     - Irregular cover, hard to suppress
   * - Building — heavy (stone/brick)
     - +5
     - Significant structural protection
   * - Entrenchment / foxhole
     - +6
     - Purpose-built field fortification
   * - Fortification / bunker
     - +8
     - Reinforced permanent structure


4.3  Intervening Terrain
------------------------


**4.3.1**  Terrain hexes that the line of fire passes through between the firer's hex and the target's hex impose a per-hex penalty to the attacker's effective rFP.

**4.3.2**  The firer's hex and the target's hex are not counted as intervening terrain.

**4.3.3**  The total intervening penalty is calculated as: penalty per hex × number of hexes of that terrain type crossed.

**4.3.4**  Multiple terrain types may be crossed. Calculate separately for each terrain type and sum.

**4.3.5**  Effective rFP can be driven to 0 or below by accumulated penalties. A fire line at 0 or less contributes nothing and cannot attack (Rule 8.2.5) — dense woods and layered smoke can genuinely stop fire.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Intervening Terrain**
     - **rFP Penalty Per Hex**
   * - Open ground
     - 0
   * - Crops / tall grass
     - -1
   * - Hedgerow / bocage (per hexside crossed — Rule 4.1.3)
     - -1
   * - Light woods
     - -2
   * - Dense woods
     - -3
   * - Smoke (one hex)
     - -3
   * - Building (firing through)
     - -2
   * - Crest hexside crossed at the firer's own level (grazing fire, Rule 4.4a.5)
     - -1


4.4  Line of Sight
------------------


**4.4.1**  Line of sight (LOS) is required to fire at a target. LOS is traced from the centre of the firer's hex to the centre of the target's hex.

**4.4.2**  LOS is blocked entirely by the following when it lies in an intervening hex:

**Higher ground —**  Any hex whose elevation level exceeds the levels of both the firer's and the target's hexes (see Rule 4.4a for elevation LOS in full)

**Cliff —**  A cliff-face hex

**Solid building —**  A building hex not designated as having windows or breaches in the relevant direction

**4.4.3**  Dense woods and other non-blocking terrain degrade fire through the per-hex penalty system (Rule 4.3) but do not block LOS entirely unless three or more consecutive hexes of dense woods intervene.

**4.4.4**  Reverse slope is a **position relative to a firer**, not a terrain type: a unit is on a firer's reverse slope when Rule 4.4a.4 denies that firer LOS to it across a crest. Such a unit cannot be targeted by that firer's direct fire at all; indirect fire (mortars, Section 16) may target it, and it receives +4 cover against indirect fire in that position (reduced per Rule 16.7.4). The same unit may be fully visible to a different firer on its own side of the crest — always evaluate per firer.

4.4a  Elevation and LOS
-----------------------


**4.4a.1**  Every hex has an elevation level printed on the map: level 0 (ground) unless marked higher. A **crest hexside** is any hexside between two hexes of different elevation levels.

**4.4a.2**  An intervening hex whose level is **equal to or higher than the higher** of the firer's and target's levels blocks LOS (Rule 4.4.2). Two units on top of the same hill see each other normally — hexes at their shared level on the hill mass between them block per this rule only if higher than both.

**4.4a.3**  An intervening hex at or below the **lower** endpoint's level never blocks LOS by elevation (its terrain may still degrade or block fire under Rules 4.3/4.4.2 — a unit two levels up still cannot see through a solid building).

**4.4a.4**  Crest blind zone: an intervening hex at an **intermediate** level (higher than the lower endpoint, lower than the higher endpoint) blocks LOS only to lower-level hexes **adjacent to it on the far side** — the ground immediately behind a crest is defiladed from observers beyond it. Lower-level hexes farther from the crest are visible over it. An intermediate hex adjacent to the higher unit never blocks (the unit looks over its own near crest).

**4.4a.5**  Grazing fire: LOS traced at the firer's own level that crosses one or more crest hexsides (skimming a ridge line between same-level positions) suffers -1 effective rFP per crest hexside crossed (Rule 4.3 table).

**4.4a.6**  Example: A fires from a level-2 hilltop at B on level 0, five hexes away, with a level-1 hex three hexes out along the line. B is visible (level 0, not adjacent to the level-1 hex on the far side). C, in the level-0 hex directly behind the level-1 hex, is in the crest blind zone — invisible to A, on A's reverse slope (Rule 4.4.4), and targetable by A's side only with indirect fire. C sees and fights normally against anything on its own side of the crest.

4.5  Elevation Combat Modifiers
-------------------------------


**4.5.1**  Units firing from a higher elevation than their target receive a bonus to effective rFP.

**4.5.2**  Units firing at a target on higher ground treat the target's terrain cover as one step higher than printed.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **Modifier**
   * - Firer 1 elevation level higher than target
     - +1 effective rFP
   * - Firer 2 or more levels higher than target
     - +2 effective rFP
   * - Target 1 level higher than firer
     - +1 to target cover modifier
   * - Target 2 or more levels higher than firer
     - +2 to target cover modifier
