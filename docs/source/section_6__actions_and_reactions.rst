Section 6 — Actions and Reactions
=================================

6.1  Action Points
------------------


**6.1.1**  Spending 1 AP activates one unit or stack for that impulse, granting exactly one action from the Section 6.3 table.

**6.1.2**  A unit may be activated more than once per turn, in separate impulses, each activation costing 1 AP. A unit's turn ends — no further movement or fire this turn — the moment it is marked MOVED/FIRED (Rule 6.5.4): a fresh unit reaches MOVED/FIRED after one Regular action (Rule 6.3.2) or after its second Assault part-action (Rule 6.3.3); a stationary weapon with ROF greater than 1 (Rule 6.6) reaches it only once its printed ROF is expended. A unit already MOVED/FIRED may not be activated again this turn (see Rule 6.7 for its remaining defensive rights).

    *See also: Rule 6.5 (the marker progression), Rule 5.5.1 (one action per impulse).*

**6.1.3**  Reactions (Rule 6.4) are not activations: a unit may react during an enemy impulse regardless of how many times it has been activated this turn, subject to Rule 6.2.3's marking.

6.2  Reaction Points
---------------------


**6.2.1**  RP are spent by the non-active player during the reaction window of an enemy impulse.

**6.2.2**  RP expenditure does not require unit activation. Any eligible unit may react if RP are available, regardless of whether it has already been activated this turn.

**6.2.3**  A reaction is momentary: it responds to the triggering action at the Rule 5.5 timing point that action creates, and the opportunity is gone once that window closes — a unit that could have fired on an enemy crossing hex A and chose not to gets no second chance once the enemy has moved on to hex B, even though hex B opens its own new window. Reacting costs the reacting unit no AP and no impulse, but marks it exactly as though it had taken that fire on its own turn:

  - A unit using the ordinary (non-ROF) economy reacts with an **Assault Fire** (Rule 6.3.3, half effective rFP): a fresh unit becomes ASSAULT-marked; an already ASSAULT-marked unit becomes MOVED/FIRED.
  - A stationary weapon with ROF greater than 1 (Rule 6.6) reacts at **full effective rFP**, expending one FIRED pip.
  - A unit already MOVED/FIRED may not react with Opportunity Fire (the sole exception is Desperate Fire against its own attackers, Rule 6.7.1).

A unit may react more than once per turn while it still has an unspent part-action, ROF pip, or (for Desperate Fire) is the actual target of a close assault — reacting is limited by resources (RP) and remaining capacity, not by a fixed count.

6.3  Regular and Assault Actions
---------------------------------


**6.3.1**  A unit takes its turn in exactly one of two ways: a single **Regular** action at full effect, or up to two **Assault** part-actions at reduced effect. The two do not mix — a unit that has taken a Regular action this turn may not also take an Assault part-action, and a unit that has taken an Assault part-action may not take a Regular action this turn.

**6.3.2**  Regular actions (each costs 1 AP unless noted; each ends the unit's turn — MOVED/FIRED — except where an action's own rule says otherwise):

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Action**
     - **AP Cost**
     - **Description**
   * - Move
     - 1
     - Move one unit up to its M# movement allowance (Section 7). → MOVED/FIRED.
   * - Fire
     - 1
     - One attack at full effective rFP (Section 8). → MOVED/FIRED — unless the firing weapon is a stationary weapon with ROF greater than 1 (Rule 6.6), which is marked FIRED 1 instead and may fire again.
   * - Close Assault
     - 1
     - Declare close assault against an adjacent occupied enemy hex. A completely fresh unit (no ASSAULT, FIRED, or MOVED/FIRED marker present this turn) may declare freely. See Section 9 and Rule 6.3.3 for the ASSAULT-marked case.
   * - Rally
     - 1
     - Leader attempts to rally one suppressed or pinned unit within command radius. See Rule 12.6.
   * - Deploy Weapon
     - 1
     - Remove MOBILE marker from a weapon counter. The weapon may not fire in the impulse it deploys, but is not otherwise marked — it may still take a Regular or Assault action (including Fire) in a later impulse this turn.
   * - Limber Weapon
     - 1
     - Place MOBILE marker on a deployed weapon counter. The weapon may not fire in the impulse it limbers. A weapon that has expended its printed ROF this turn may not limber until the following turn (Rule 6.6.5).
   * - Accept Surrender
     - 1
     - Formally accept surrender of Dispersed enemy unit in same or adjacent hex. Place GUARD marker on accepting unit.
   * - Go Hidden
     - 1
     - Unit transitions from VISIBLE to HIDDEN. Place counter on chart under cover, place blind marker on map. Receive free hidden impulse. → MOVED/FIRED. See Section 14.
   * - Spot Action
     - 1
     - Unit spends its entire turn observing. Gains +3 OBS for all spot rolls this turn. → MOVED/FIRED. See Section 14.
   * - Move Dummy Marker
     - 1
     - Move one dummy marker independently (free if the real unit in its group also moves this turn). Not a combat unit's Move/Fire action — does not interact with the MOVED/FIRED marker.
   * - Leader Action
     - 1
     - Leader moves, coordinates, provides a fire bonus to a fire group within command radius (Rule 12.7), or places a RALLY POINT marker. → MOVED/FIRED.


**6.3.3**  Assault part-actions (each costs 1 AP; a fresh unit may take one as its first part-action of the turn):

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Part-Action**
     - **AP Cost**
     - **Description**
   * - Assault Move
     - 1
     - Bound 1 hex, regardless of M# (Rule 7.1.4 governs terrain cost as normal).
   * - Assault Fire
     - 1
     - One attack at half effective rFP, rounded down — the halving is applied to the final effective rFP after falloff, terrain, and status modifiers (Rule 8.2.5 governs a result of 0 or less).
   * - Close Assault
     - 1
     - Available only to a unit already carrying the ASSAULT marker (one part-action already spent), as its **second** part-action, and only with a leader present — in the assaulting unit's hex, either coordinating that unit alone or activating it together with other units in the same stack (Rule 6.1.1). Without a leader present, an ASSAULT-marked unit may not declare Close Assault this turn — its second part-action must be an ordinary Assault Move or Assault Fire. See Rule 9.1.2.


After a unit's **first** part-action this turn (of either kind, in either order), place the ASSAULT marker: one part-action spent, one remains — a move or a fire, whichever the player chooses. After the **second** part-action, remove ASSAULT and place MOVED/FIRED. Legal sequences include Assault Move → Assault Fire, Assault Fire → Assault Move, and Assault Fire → Assault Fire; a unit may also take Assault Move → Assault Move, though for most infantry this covers no more ground than a single Regular Move at half the AP efficiency.

**6.3.4**  Half, rounded down, is this game's standard convention for a halving with no more specific rule of its own (Rule 2.5). It governs the Assault Fire halving above.

6.4  Reaction Types
--------------------


The following reactions are available to the non-active player during a reaction window (Rule 5.5).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Reaction**
     - **RP Cost**
     - **Trigger Condition**
   * - Opportunity Fire
     - 1
     - Enemy unit moves within or into LOS (declared at an interruption point, Rule 5.5.3), fires, or takes any other fire-drawing action. Marking consequences: Rule 6.2.3.
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

**6.4.2**  If the interrupting action renders the held action illegal — the target is destroyed or no longer in line of sight, or the acting unit is Suppressed or Pinned — the acting player retains the AP and may declare a different action instead, consistent with Rule 5.5.2.

**6.4.3**  During an Interrupt, the players' roles swap fully for that one action: the original active player becomes the reacting player and may spend their own RP on reactions to the interrupting action (Opportunity Fire, Defensive Fire, Spot Roll), using the same timing windows of Rule 5.5. An Interrupt may not itself be interrupted.

**6.4.4**  Limit: one Interrupt per declared enemy action.

6.5  Action Markers
---------------------


**6.5.1**  Action markers track how much of its turn a unit has spent:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Marker**
     - **Meaning**
   * - ASSAULT
     - One Assault part-action spent this turn; one remains (Rule 6.3.3).
   * - FIRED 1 / FIRED 2 / FIRED 3
     - A stationary ROF-greater-than-1 weapon has fired that many times this turn (Rule 6.6).
   * - MOVED/FIRED
     - The unit is done for the turn — no further movement or fire (Rule 6.7 covers its remaining defensive rights).


**6.5.2**  A unit displaying ASSAULT or a FIRED pip may be activated again this turn to take its remaining part-action or ROF fire; a unit displaying MOVED/FIRED may not.

**6.5.3**  A unit's Regular or Assault economy and its ROF track never apply at once: a weapon firing under ROF (Rule 6.6) never carries an ASSAULT marker, and a unit carrying ASSAULT is, by definition, not exercising ROF this turn.

**6.5.4**  All action markers (ASSAULT, FIRED 1/2/3, MOVED/FIRED, OPPORTUNITY, CARELESS) are removed during the Recovery Phase at the start of the following turn.

6.6  ROF Weapons — Stationary Machine Guns
---------------------------------------------


**6.6.1**  Some weapons may fire more than once per turn while stationary — **ROF** (Rate of Fire), a property of the weapon itself, distinct from the printed F# value on the counter. F# is not consulted by this rule; it remains on the counter pending a full counter-data review (Rule 6.6.6).

**6.6.2**  ROF by weapon:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Weapon**
     - **ROF (stationary)**
     - **Notes**
   * - HMG team, deployed (tripod)
     - 3
     - A tripod mount is pre-sighted or range-carded on deployment — the extra bursts assume that setup, not a fresh aim each time.
   * - LMG team, and any bipod- or light-tripod-mounted MG, while stationary
     - 2
     - The bipod position buys one extra burst over the ordinary economy — but only while planted; see Rule 6.6.4.
   * - Any other unit, or any weapon in transit
     - 1
     - One full-effect fire is the unit's entire turn (Rule 6.3.2); the Assault economy (Rule 6.3.3) is its only path to a second, reduced shot.


**6.6.3**  A stationary ROF-greater-than-1 weapon's Regular Fire is a full-effect attack (Rule 6.3.2); it is marked FIRED 1 rather than MOVED/FIRED, and while fire remains under its ROF it may be activated again this turn (1 AP each) for FIRED 2, then FIRED 3. Once its ROF is expended, mark MOVED/FIRED.

**6.6.4**  ROF applies only in a turn the weapon has not moved. A weapon that takes any Move action this turn — Regular or Assault — is in the ordinary Assault economy for the rest of its turn: no weapon fires at ROF greater than 1 in a turn it moved. An LMG (or any bipod-capable MG) that chooses to move therefore fights like any other unit — one crewman operating it off the bipod, at half rFP.

**6.6.5**  A deployed weapon that has expended its printed ROF this turn may not Limber (Rule 6.3.2) until the following turn — the crew is serving the gun, not packing it up.

**6.6.6**  *[Interim note: F# as printed on infantry and weapon-team counters predates this rule and is not currently used by it. A full counter-data review to reconcile F# with ROF, and to extend ROF to weapon types not yet covered here, is a planned future pass — see Appendix E, design note recording this redesign.]*

6.7  Desperate Fire and Close-Combat Defense
-----------------------------------------------


**6.7.1**  A unit marked MOVED/FIRED that is the target of a declared Close Assault or Overrun may still take **Desperate Fire** against those incoming attackers only — one Assault Fire (half effective rFP, Rule 6.3.3), 1 RP, at the declaration window (Rule 5.5.2). It may not fire at any other target this turn.

**6.7.2**  Close-combat defense — defensive grenades, melee, and withdrawal rights (Section 9) — is always available to a unit regardless of its action markers.
