Section 6 — Actions and Reactions
=================================

6.1  Action Points
------------------


**6.1.1**  Spending 1 AP activates one unit or stack for that impulse.

**6.1.2**  An activated unit may take all of its available actions (up to its F# rate and M# allowance) within that single impulse.

**6.1.3**  A unit may only be activated once per turn by the AP system. However, it may respond to enemy actions using opportunity fire (see Section 6.4) even if it has already been activated.

6.2  Reaction Points
--------------------


**6.2.1**  RP are spent by the non-active player during the reaction window of an enemy impulse.

**6.2.2**  RP expenditure does not require unit activation. Any eligible unit may react if RP are available, regardless of whether it has already been activated this turn.

**6.2.3**  Reacting with opportunity fire consumes one of the reacting unit's F# fire actions for the turn.

6.3  Action Types
-----------------


The following actions are available to the active player. Each costs 1 AP unless otherwise noted.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Action**
     - **AP Cost**
     - **Description**
   * - Move
     - 1
     - Move one unit up to its M# movement allowance. Place MOVED marker.
   * - Fire
     - 1
     - Fire one unit or fire group. Place FIRE 1 marker (or FIRE 2/3 if subsequent fires this turn).
   * - Move and Fire (Assault)
     - 1
     - Unit moves then fires, or fires then moves. Places ASSAULT marker. Unit becomes Exposed.
   * - Close Assault
     - 1
     - Declare close assault against adjacent occupied enemy hex. See Section 9.
   * - Rally
     - 1
     - Leader attempts to rally one adjacent suppressed or pinned unit. See Section 12.
   * - Deploy Weapon
     - 1
     - Remove MOBILE marker from a weapon counter. Unit may not fire this impulse.
   * - Limber Weapon
     - 1
     - Place MOBILE marker on a deployed weapon counter. Unit may not fire this impulse.
   * - Accept Surrender
     - 1
     - Formally accept surrender of Dispersed enemy unit in same or adjacent hex. Place GUARD marker on accepting unit.
   * - Go Hidden
     - 1
     - Unit transitions from VISIBLE to HIDDEN. Place counter on chart under cover, place blind marker on map. Receive free hidden impulse. See Section 14.
   * - Spot Action
     - 1
     - Unit spends entire activation observing. Gains +3 OBS for all spot rolls this turn. See Section 14.
   * - Move Dummy Marker
     - 1
     - Move one dummy marker independently (free if real unit in same group also moves this turn).
   * - Leader Action
     - 1
     - Leader moves, coordinates, provides a fire bonus to an adjacent unit, or places a RALLY POINT marker.


6.4  Reaction Types
-------------------


The following reactions are available to the non-active player during the reaction window.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Reaction**
     - **RP Cost**
     - **Trigger Condition**
   * - Opportunity Fire
     - 1
     - Enemy unit moves into LOS, or enemy unit becomes Exposed (see Rule 6.6).
   * - Defensive Fire
     - 1
     - Enemy unit declares Close Assault against a friendly unit.
   * - Spot Roll
     - 1
     - Enemy unit becomes visible, moves carelessly, or enters LOS of a unit taking a Spot Action. See Section 14.
   * - Interrupt
     - 2
     - Any enemy action. The non-active player inserts their own action before the declared enemy action resolves. Initiative passes temporarily to the interrupting player for that one action.


**6.4.1**  Interrupt procedure: the declared enemy action is placed on hold. The interrupting player executes one complete action with one eligible friendly unit (normal action rules and action markers apply). The held action then resolves.

**6.4.2**  If the interrupting action renders the held action illegal — the target is destroyed or no longer in line of sight, or the acting unit is Suppressed or Pinned — the acting player retains the AP and may declare a different action instead, consistent with Rule 5.5.5.

**6.4.3**  An Interrupt may not itself be interrupted. Other reactions (Opportunity Fire, Defensive Fire, Spot Roll) may trigger off the interrupting action normally if their conditions are met.

**6.4.4**  Limit: one Interrupt per declared enemy action.

6.5  Action Markers
-------------------


**6.5.1**  Action markers track what actions a unit has taken during the current turn.

**6.5.2**  A unit may not take an action for which it already has a marker unless the rules explicitly permit it (e.g., a unit with F3 may place FIRE 1, then FIRE 2, then FIRE 3 on separate impulses).

**6.5.3**  The ASSAULT marker replaces both a MOVED and FIRE 1 marker. A unit with an ASSAULT marker may still use remaining fire actions (FIRE 2, FIRE 3) from stationary positions but may not move again this turn.

**6.5.4**  All action markers are removed during the Recovery Phase at the start of the following turn.

6.6  Exposure Rules
-------------------


**6.6.1**  A unit becomes Exposed when it takes a Move and Fire action (ASSAULT marker placed). The Exposed condition persists until the unit spends a Move action to reach terrain with cover modifier +2 or higher, or until the end of the current turn.

**6.6.2**  A unit firing from open ground (cover modifier +0) for the second time from the same position in the same turn becomes Firing Exposed after its second fire action.

**6.6.3**  First fire from any position this turn is not Firing Exposed regardless of terrain.

**6.6.4**  An Exposed unit may be targeted by opportunity fire (1 RP cost) at any point while it remains Exposed.

**6.6.5**  Opportunity fire against an Exposed unit uses full fire resolution with no penalty to the attacker's rFP.

**6.6.6**  Opportunity fire against a Firing Exposed unit applies a -1 rFP penalty to the attacker, representing a partially obscured stationary target.

**6.6.7**  Opportunity fire against a moving unit (MOVED marker present, unit in transit) applies a -2 rFP penalty to the attacker. Exception: when the target is a vehicle, this penalty does not stack with the Gunnery Roll's own crossing-target adjustment (Rule 18.1a.6/18.1a.9) — the vehicle-specific adjustment replaces it. This rule applies exactly as written when the target is infantry.
