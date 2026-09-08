Section 7 — Movement
====================

7.1  Movement Allowance
-----------------------


**7.1.1**  A unit's movement allowance is its M# value. This is the maximum number of hexes it may move in a single Move action.

**7.1.2**  One impulse represents approximately 20-25 seconds of real time. At tactical double time (200 yards per minute) a squad can cover roughly 70-80 yards — approximately 2 hexes at 40 yards per hex. M2 is therefore the standard infantry movement allowance.

**7.1.3**  Movement allowance by unit type:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit Type**
     - **M#**
     - **Notes**
   * - Rifle squad
     - M2
     - Standard tactical bound
   * - SMG squad
     - M2
     - Same rate, lighter weapon load
   * - Panzergrenadier squad
     - M2
     - Same rate, assault doctrine
   * - LMG team
     - M2
     - Weapon slows but still two hexes
   * - HMG team (mobile)
     - M1
     - Heavy weapon significantly impedes
   * - Mortar team (mobile)
     - M1
     - Same
   * - HMG / Mortar team (deployed)
     - M0
     - Cannot move while deployed
   * - Leader
     - M3
     - Lighter load, higher initiative
   * - Sniper team
     - M1
     - Deliberate, concealed movement — snipers do not run (Section 20)


**7.1.4**  A unit may always enter any single terrain hex regardless of its movement cost, even if that cost exceeds its remaining M# for that activation. The unit simply cannot move further that activation.

**7.1.5**  Status effects on movement: Suppressed units move at half M# (round down, minimum 1). Pinned units cannot move.

7.2  Terrain Movement Costs
---------------------------


Movement costs are in Movement Points (MP). Standard infantry has M2 = 2 MP per activation. Each hex entered costs the MP listed below.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Terrain / Condition**
     - **MP Cost**
     - **Notes**
   * - Open ground
     - 1
     - Baseline
   * - Crops / tall grass
     - 1
     - No impediment
   * - Ditch / sunken road
     - 1
     - Natural movement axis
   * - Road
     - 1
     - And enables the road bonus (Rule 7.2.1)
   * - Building — ground floor entry
     - 1
     - Per floor entered including ground
   * - Building — each additional floor
     - 1
     - Stairs and ladders slow under fire
   * - Light woods
     - 2
     - Full activation for M2 unit
   * - Hedgerow (hexside crossing)
     - +1
     - Added to cost of hex being entered (open hex through hedgerow = 2 MP total)
   * - Rubble
     - 2
     - Unstable footing
   * - Shallow stream
     - 2
     - Wading
   * - Dense woods
     - 3
     - Exceeds M2 — entire activation consumed
   * - Wall / fence (hexside crossing)
     - +1
     - Added to cost of hex being entered
   * - Elevation gain (per level uphill)
     - +1
     - Added to cost of hex being entered
   * - Elevation loss (downhill)
     - +0
     - No penalty for descent
   * - River / cliff
     - Impassable
     - Except at designated crossing points


.. figure:: /../../maps/svg_output/section7_movement_example1.svg
   :alt: A squad moves two hexes across open ground into light woods, spending 1 movement point to enter the first open hex and 2 to enter the light woods hex.
   :width: 500px

   A squad crossing open ground into light woods. Movement cost is
   labeled per hex entered.

**7.2.1**  Road movement special rule: a unit moving exclusively along road hexes for its entire activation may move **M# + 1** hexes. One hex of off-road movement cancels the road bonus for that entire activation. The road bonus does not stack with Careless Movement (Rule 7.4.1) — declare one or the other.

*NOTE: earlier drafts gave a flat 3 hexes on roads, which tripled an M1 weapon team's speed while giving an M2 squad only 50% — M#+1 scales the benefit to the mover.*

**7.2.2**  Elevation interaction example: a unit with M2 moving uphill one level into open ground costs 1 (terrain) + 1 (elevation) = 2 MP — the full activation for one hex. Two levels uphill in one activation is impossible for a standard M2 unit.

**7.2.3**  Building floor interaction example: a unit with M2 entering a building at ground floor (1 MP) and moving to the first floor (1 MP) uses its entire activation. It cannot reach the second floor without starting adjacent to the building at the start of the activation.

7.3  The Assault Bound
------------------------


**7.3.1**  Rule 6.3.3 defines the Assault economy in full — up to two part-actions (Assault Move, Assault Fire) at reduced effect, in either order, marked with ASSAULT after the first and MOVED/FIRED after the second. This rule covers only the movement-specific detail of the Assault Move part-action.

**7.3.2**  An Assault Move bounds the unit exactly 1 hex regardless of M#, paying that hex's terrain cost under the ordinary rules (Rule 7.1.4 — a unit may always enter a single hex regardless of cost, even if it exceeds what a full move would otherwise afford).

**7.3.3**  A unit may take an Assault Move as either its first or second part-action; two Assault Moves in the same turn are legal (2 hexes total across two impulses) but for most infantry cover no more ground than a single Regular Move (Rule 6.3.2) at twice the AP cost.

7.4  Careless Movement
----------------------


**7.4.1**  A unit may declare Careless Movement when spending a Move action. The unit moves M#+1 hexes instead of its normal M# allowance.

**7.4.2**  Place a CARELESS marker on the unit. The unit suffers -2 CON (concealment) for the remainder of this turn.

**7.4.3**  Any enemy unit with LOS to the moving unit may attempt a free spot roll during the movement reaction window. This spot roll costs no RP.

**7.4.4**  Careless movement represents troops moving quickly without tactical caution — appropriate in areas the owning player believes are safe. It is always risky if enemy units are present.

**7.4.5**  The CARELESS marker is removed during the Recovery Phase.

7.5  Moving Target Modifier
---------------------------


**7.5.1**  A unit currently resolving a Move or Assault Move action, before that action fully completes, is a moving target. Opportunity fire against a moving target is declared at an interruption point — whenever the unit enters a new hex during its move (Rule 5.5.3) — and resolves before the unit moves further.

**7.5.2**  Opportunity fire against a moving target applies -2 rFP to the attacker.

**7.5.2a**  Exception: when the target is a vehicle, this penalty does not stack with the Gunnery Roll's own crossing-target adjustment (Rule 18.1a.6/18.1a.9) — the vehicle-specific adjustment replaces it. Rule 7.5.2 applies exactly as written when the target is infantry.

**7.5.3**  If opportunity fire produces No Effect, the moving unit continues normally.

**7.5.4**  If opportunity fire produces Suppressed, the moving unit loses 1 MP before continuing. That loss is the only effect on the current move — the Suppressed halving of M# (Rule 10.1) applies from the unit's next Move action, never retroactively to MP already allocated.

**7.5.5**  If opportunity fire produces Pinned or worse, the moving unit stops immediately. Remaining MP are lost.

7.6  Mobile Weapon Counters
---------------------------


**7.6.1**  Weapon counters with the MOBILE marker may move at infantry movement rate with a crew unit or independently.

**7.6.2**  A weapon counter with the MOBILE marker cannot fire.

**7.6.3**  Removing the MOBILE marker (deploying the weapon) costs 1 AP. The weapon may not fire in the same impulse it deploys.

**7.6.4**  Adding the MOBILE marker (limbering the weapon) costs 1 AP. The weapon may not fire in the same impulse it limbers. A weapon that expended its printed ROF this turn (Rule 6.6) may not limber until the following turn.
