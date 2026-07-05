Section 4 — Terrain
===================

4.1  Terrain Types
------------------


**4.1.1**  Each hex is assigned a terrain type. The terrain type determines the cover modifier it provides to units occupying it and any LOS penalty it applies to fire passing through it.

**4.1.2**  A hex may contain only one terrain type for game purposes. When a hex contains mixed terrain, the dominant terrain type is used.

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
   * - Wall / fence
     - +2
     - Low cover, protects prone troops
   * - Hedgerow / bocage edge
     - +2
     - Partial cover
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
   * - Reverse slope
     - +4
     - No direct LOS; indirect fire only
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

**4.3.5**  Effective rFP after all modifiers has a minimum value of 1 regardless of penalties.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Intervening Terrain**
     - **rFP Penalty Per Hex**
   * - Open ground
     - 0
   * - Crops / tall grass
     - -1
   * - Hedgerow / bocage
     - -1
   * - Light woods
     - -2
   * - Dense woods
     - -3
   * - Smoke (one hex)
     - -3
   * - Building (firing through)
     - -2
   * - Hill crest (grazing fire)
     - -1


4.4  Line of Sight
------------------


**4.4.1**  Line of sight (LOS) is required to fire at a target. LOS is traced from the centre of the firer's hex to the centre of the target's hex.

**4.4.2**  LOS is blocked entirely by the following terrain when it lies in an intervening hex:

**Hill mass —**  A hex designated as a hill body (not a crest hex)

**Cliff —**  A cliff-face hex

**Solid building —**  A building hex not designated as having windows or breaches in the relevant direction

**4.4.3**  Dense woods and other non-blocking terrain degrade fire through the per-hex penalty system (Rule 4.3) but do not block LOS entirely unless three or more consecutive hexes of dense woods intervene.

**4.4.4**  A unit in a reverse slope hex has no direct LOS to units on the other side of the slope. Only indirect fire (mortars, artillery) may target such units.

4.5  Elevation
--------------


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
