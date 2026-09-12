Section 6 — Actions and Reactions
=================================

6.1  Action Points
------------------


**6.1.1**  Spending 1 AP activates one unit or stack for that impulse, granting exactly one action from the Section 6.3 table.

.. container:: rule-guide

   **Why:** Ties the AP resource directly to the Section 6.3 action menu, so every activation is both priced (1 AP) and limited to exactly one action — no free extra actions bundled into a single AP spend.

   **Example:** Alpha's player spends 1 AP to activate Alpha this impulse, choosing one action from the 6.3 table (e.g. Move). Alpha may not also Fire in the same impulse without spending a second AP in a later impulse.

**6.1.2**  A unit may be activated more than once per turn, in separate impulses, each activation costing 1 AP. A unit's turn ends — no further movement or fire this turn — the moment it is marked MOVED/FIRED (Rule 6.5.4): a fresh unit reaches MOVED/FIRED after one Regular action (Rule 6.3.2) or after its second Assault part-action (Rule 6.3.3); a stationary weapon with F# greater than 1 (Rule 6.6) reaches it only once its printed F# is expended. A unit already MOVED/FIRED may not be activated again this turn (see Rule 6.7 for its remaining defensive rights).

.. container:: rule-guide

   **Why:** Names the actual stopping condition — the MOVED/FIRED marker — rather than a simple "once per turn" count, since some units (F#-capable weapons, Assault-economy units) legitimately activate more than once before reaching that state.

   **Example:** A tripod HMG fires three times this turn (FIRED 1, FIRED 2, FIRED 3), each a separate 1-AP activation, before finally reaching MOVED/FIRED on its third shot. An ordinary rifle squad reaches MOVED/FIRED after just one Regular Fire.

    *See also: Rule 6.5 (the marker progression), Rule 5.5.1 (one action per impulse).*

**6.1.3**  Reactions (Rule 6.4) are not activations: a unit may react during an enemy impulse regardless of how many times it has been activated this turn, subject to Rule 6.2.3's marking.

.. container:: rule-guide

   **Why:** Keeps reactions off a unit's activation count entirely, so a unit that has already acted this turn (and isn't yet MOVED/FIRED) can still react — reactions draw on a separate resource (RP), not a share of the unit's own activations.

   **Example:** Alpha has already taken an Assault Move this turn (ASSAULT marker, one part-action spent) but hasn't yet used its second part-action. It may still react with Opportunity Fire during the enemy's impulse, spending RP rather than AP.

6.2  Reaction Points
---------------------


**6.2.1**  RP are spent by the non-active player during the reaction window of an enemy impulse.

.. container:: rule-guide

   **Why:** Keeps RP strictly a non-active-player resource spent only during the reaction window, so reacting never competes with the active player's own AP economy in the same impulse.

   **Example:** During Alpha's (active player's) impulse, only Bravo's player (non-active) may spend RP to react to whatever Alpha just did.

**6.2.2**  RP expenditure does not require unit activation. Any eligible unit may react if RP are available, regardless of whether it has already been activated this turn.

.. container:: rule-guide

   **Why:** Decouples reacting from the AP-activation system entirely — a unit doesn't need to be "fresh" or unactivated to react, only to have RP available and the capacity described in 6.2.3.

   **Example:** Bravo already took a Regular Fire action earlier this turn and carries MOVED/FIRED. It is still eligible to spend RP on a reaction — subject to 6.2.3's restriction that a MOVED/FIRED unit's only reaction option is Desperate Fire (6.7.1).

**6.2.3**  A reaction is momentary: it responds to the triggering action at the Rule 5.5 timing point that action creates, and the opportunity is gone once that window closes — a unit that could have fired on an enemy crossing hex A and chose not to gets no second chance once the enemy has moved on to hex B, even though hex B opens its own new window. Reacting costs the reacting unit no AP and no impulse, but marks it exactly as though it had taken that fire on its own turn:

.. container:: rule-guide

   **Why:** Makes a reaction a use-it-or-lose-it response to one specific moment, not a standing overwatch condition — this is what keeps a unit from stacking up "owed" reactions across multiple triggering events, and it's why reacting marks the unit exactly as if it had acted normally (see design note E.94).

   **Example:** Bravo could have fired on Alpha crossing hex A but chose to hold. Once Alpha moves on to hex B, that specific opportunity is gone — Bravo's player cannot retroactively claim it — though hex B is a brand-new window Bravo may react to if it still has RP and capacity.

  - A unit using the ordinary (F1) economy reacts with an **Assault Fire** (Rule 6.3.3, half effective rFP): a fresh unit becomes ASSAULT-marked; an already ASSAULT-marked unit becomes MOVED/FIRED.
  - A stationary weapon with F# greater than 1 (Rule 6.6) reacts at **full effective rFP**, expending one FIRED pip.
  - A unit already MOVED/FIRED may not react with Opportunity Fire (the sole exception is Desperate Fire against its own attackers, Rule 6.7.1).

A unit may react more than once per turn while it still has an unspent part-action, F# pip, or (for Desperate Fire) is the actual target of a close assault — reacting is limited by resources (RP) and remaining capacity, not by a fixed count.

6.3  Regular and Assault Actions
---------------------------------


**6.3.1**  A unit takes its turn in exactly one of two ways: a single **Regular** action at full effect, or up to two **Assault** part-actions at reduced effect. The two do not mix — a unit that has taken a Regular action this turn may not also take an Assault part-action, and a unit that has taken an Assault part-action may not take a Regular action this turn.

.. container:: rule-guide

   **Why:** Forbids mixing so a unit can't get the best of both worlds — full-effect Regular actions plus the flexibility of two Assault part-actions — by picking whichever economy is more convenient action to action.

   **Example:** Alpha takes a Regular Move this turn (full M#). It cannot later also take an Assault Fire part-action — Regular and Assault are mutually exclusive for the whole turn, decided by whichever the unit does first.

**6.3.1a**  Vehicles do not follow this Regular/Assault split. See Rule 17.4.1a for the vehicle action economy.

.. container:: rule-guide

   **Why:** Flags the exception at the point a reader would otherwise assume it's universal, rather than leaving it to be inferred from a vehicle-specific rule elsewhere (Rule 17.4.2's TRAV penalty) that only makes sense once the exception is already known.

   **Example:** A rifle squad that moves this turn is MOVED/FIRED and done; a Panzer IV that moves the same turn is not — it may still take a separate Fire action later in the turn, per Rule 17.4.1a.

**6.3.2**  Regular actions (each costs 1 AP unless noted; each ends the unit's turn — MOVED/FIRED — except where an action's own rule says otherwise):

.. container:: rule-guide

   **Why:** The "AP Cost" and "ends the unit's turn" columns exist because most Regular actions are meant to be a unit's entire turn at full effect — a unit trades flexibility for full-strength results by choosing this over the Assault economy.

   **Example:** Alpha spends 1 AP for a Regular Fire at full effective rFP. Even though Alpha wasn't Suppressed or otherwise unable to act again, it is now MOVED/FIRED and done for the turn — the trade-off for firing at full strength rather than a reduced Assault Fire.

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
     - One attack at full effective rFP (Section 8). → MOVED/FIRED — unless the firing weapon is a stationary weapon with F# greater than 1 (Rule 6.6), which is marked FIRED 1 instead and may fire again.
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
     - Place MOBILE marker on a deployed weapon counter. The weapon may not fire in the impulse it limbers. A weapon that has expended its printed F# this turn may not limber until the following turn (Rule 6.6.5).
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
   * - Change Floor (Building)
     - 1
     - Move exactly one floor, up or down, within the unit's current building hex. See Rule 7.2a. Does not by itself end the unit's turn — a unit may still act normally (including changing floor again) in a later activation this turn.


**6.3.3**  Assault part-actions (each costs 1 AP; a fresh unit may take one as its first part-action of the turn):

.. container:: rule-guide

   **Why:** The ASSAULT/MOVED-FIRED marker progression is what makes the Assault economy legible at a glance — a player can tell exactly how much of a unit's turn remains just by which marker (if any) sits on it.

   **Example:** Alpha takes an Assault Move (ASSAULT marker placed, one part-action spent). Later in the turn, Alpha takes an Assault Fire as its second part-action — ASSAULT is removed and MOVED/FIRED is placed. Alpha covered 1 hex and got one reduced-effect shot, instead of a single full-effect Regular action.

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

.. container:: rule-guide

   **Why:** States the halving convention exactly once, centrally, so every other rule that halves something (Assault Fire here, and any future rule) can just say "halved" without re-specifying the rounding direction each time.

   **Example:** Alpha's full effective rFP for a given shot is 7. Its Assault Fire uses half of that, rounded down: 3, not 3.5 or 4.

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

.. container:: rule-guide

   **Why:** Spells out exactly what "interrupting" means mechanically — a full action inserted before the held one resolves — so Interrupt doesn't need its own separate action-resolution rules beyond borrowing the normal ones.

   **Example:** Alpha declares a Move action. Bravo's player spends 2 RP to Interrupt. Bravo's chosen unit completes one full action (say, a Fire) before Alpha's Move is allowed to resolve.

**6.4.2**  If the interrupting action renders the held action illegal — the target is destroyed or no longer in line of sight, or the acting unit is Suppressed or Pinned — the acting player retains the AP and may declare a different action instead, consistent with Rule 5.5.2.

.. container:: rule-guide

   **Why:** Protects the interrupted player from being forced into a now-nonsensical action — there's no point making Alpha "resolve" a Move to a hex that no longer exists as a legal destination, or a Fire at a target that just got destroyed by the interrupt.

   **Example:** Bravo's Interrupt destroys Alpha's intended fire target before Alpha's held Fire action resolves. Alpha's player keeps the AP they spent and may instead declare a different, currently-legal action.

**6.4.3**  During an Interrupt, the players' roles swap fully for that one action: the original active player becomes the reacting player and may spend their own RP on reactions to the interrupting action (Opportunity Fire, Defensive Fire, Spot Roll), using the same timing windows of Rule 5.5. An Interrupt may not itself be interrupted.

.. container:: rule-guide

   **Why:** Makes an Interrupt a genuine, if temporary, full role-swap rather than a one-sided free action — the original active player still gets their own reactions to it, keeping the interrupt itself subject to the same checks and balances as any other action.

   **Example:** During Bravo's Interrupt action, Alpha's player (now the reacting party for this one action) may spend their own RP on Opportunity Fire against Bravo's interrupting unit.

**6.4.4**  Limit: one Interrupt per declared enemy action.

.. container:: rule-guide

   **Why:** Caps the back-and-forth at one level so Interrupts can't recursively chain into an unresolvable stack of interruptions-within-interruptions.

   **Example:** Bravo Interrupts Alpha's declared action. Alpha cannot then Interrupt Bravo's interrupting action — 6.4.3's role-swap grants reactions (Opportunity Fire, Defensive Fire, Spot Roll) during that action, but not a second Interrupt.

6.5  Action Markers
---------------------


**6.5.1**  Action markers track how much of its turn a unit has spent:

.. container:: rule-guide

   **Why:** Collects every action marker's meaning in one table so a player can read a counter's current marker and immediately know both what it's already done and what, if anything, it can still do.

   **Example:** A unit displaying MOVED/FIRED has used its entire turn; one displaying ASSAULT has one part-action left; one displaying FIRED 2 (an F#-capable weapon) has one more shot available before reaching MOVED/FIRED.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Marker**
     - **Meaning**
   * - ASSAULT
     - One Assault part-action spent this turn; one remains (Rule 6.3.3).
   * - FIRED 1 / FIRED 2 / FIRED 3
     - A stationary F#-greater-than-1 weapon has fired that many times this turn (Rule 6.6).
   * - MOVED/FIRED
     - The unit is done for the turn — no further movement or fire (Rule 6.7 covers its remaining defensive rights).


**6.5.2**  A unit displaying ASSAULT or a FIRED pip may be activated again this turn to take its remaining part-action or F# fire; a unit displaying MOVED/FIRED may not.

.. container:: rule-guide

   **Why:** Draws the actual eligibility line for re-activation — not "has this unit already acted" but "does its current marker leave it anything left to do."

   **Example:** Alpha carries ASSAULT. Its player may spend another 1 AP to activate it again for its second part-action. Bravo carries MOVED/FIRED and cannot be activated again this turn at all.

**6.5.3**  A unit's Regular or Assault economy and its F# track never apply at once: a weapon firing under F# (Rule 6.6) never carries an ASSAULT marker, and a unit carrying ASSAULT is, by definition, not exercising F# this turn.

.. container:: rule-guide

   **Why:** The two systems (Assault economy and F#) are two different tracks that never overlap on the same unit in the same turn, closing off a potential combination — an ASSAULT-marked weapon later claiming F#, or vice versa — that neither system was designed to interact with.

   **Example:** A tripod HMG firing under F# is never marked ASSAULT — it uses the FIRED 1/2/3 track exclusively. A unit that has taken an Assault Move (ASSAULT marker) is, by definition, in the Assault economy, not exercising F#.

**6.5.4**  All action markers (ASSAULT, FIRED 1/2/3, MOVED/FIRED, CARELESS) are removed during the Recovery Phase at the start of the following turn.

.. container:: rule-guide

   **Why:** Gives every marker a fixed, predictable lifetime — exactly one turn — so a player never has to remember to manually track when a marker "expires" mid-game.

   **Example:** At the start of the Recovery Phase, every ASSAULT, FIRED 1/2/3, MOVED/FIRED, and CARELESS marker on the map is removed at once, regardless of when each was placed during the previous turn.

6.6  F# and Rate of Fire — Stationary Weapons
-------------------------------------------------


**6.6.1**  Some weapons may fire more than once per turn while stationary — the printed F# value on the counter (Rule 3.3.2) determines how many times. F# is keyed to mount type, per the table below.

.. container:: rule-guide

   **Why:** Ties the printed stat directly to a single authoritative source (the mount-type table below) rather than leaving a designer to assign it by feel per counter, so every weapon's stationary fire rate traces back to one consistent rule.

   **Example:** A tripod HMG's printed F3 is the same number Rule 6.6.2's table would assign it by mount type — reading the counter and reading the table give the identical answer, because they're the same fact.

**6.6.2**  F# by weapon:

.. container:: rule-guide

   **Why:** Keys F# specifically to the mount type — tripod vs. bipod vs. anything else — rather than to weapon class alone, since it's the pre-sighted, planted mount, not the gun itself, that buys the extra bursts.

   **Example:** An HMG on its tripod gets F3. The same class of gun, if printed as a bipod-mounted variant, only gets F2 — and only while stationary (Rule 6.6.4).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Weapon**
     - **F# (stationary)**
     - **Notes**
   * - HMG team, deployed (tripod)
     - 3
     - A tripod mount is pre-sighted or range-carded on deployment — the extra bursts assume that setup, not a fresh aim each time.
   * - LMG team, and any bipod- or light-tripod-mounted MG, while stationary
     - 2
     - The bipod position buys one extra burst over the ordinary economy — but only while planted; see Rule 6.6.4.
   * - Mortar, deployed (Section 16)
     - 2
     - Same deploy/limber system as an HMG (Rule 7.6); a planted baseplate supports a second fire mission the way a bipod supports a second burst. Mobile mortars use the row below.
   * - Any other unit, or any weapon in transit
     - 1
     - One full-effect fire is the unit's entire turn (Rule 6.3.2); the Assault economy (Rule 6.3.3) is its only path to a second, reduced shot.


**6.6.3**  A stationary F#-greater-than-1 weapon's Regular Fire is a full-effect attack (Rule 6.3.2); it is marked FIRED 1 rather than MOVED/FIRED, and while fire remains under its F# it may be activated again this turn (1 AP each) for FIRED 2, then FIRED 3. Once its F# is expended, mark MOVED/FIRED.

.. container:: rule-guide

   **Why:** Gives F#-capable weapons their own marker progression (FIRED 1/2/3) distinct from ASSAULT, since their shots are all at full effect, unlike an Assault economy's reduced-effect part-actions — they need a different track to say so.

   **Example:** A tripod HMG (F3) fires three separate times this turn, each a full-effect Regular Fire, marked FIRED 1, then FIRED 2, then FIRED 3 in turn. Only after the third shot does it become MOVED/FIRED.

**6.6.4**  F# greater than 1 applies only in a turn the weapon has not moved. A weapon that takes any Move action this turn — Regular or Assault — is in the ordinary Assault economy for the rest of its turn: no weapon fires above F1 in a turn it moved. An LMG (or any bipod-capable MG) that chooses to move therefore fights like any other unit — one crewman operating it off the bipod, at half rFP.

.. container:: rule-guide

   **Why:** Ties the extra bursts specifically to staying planted — the moment a weapon with F# greater than 1 moves, whatever pre-sighting or range-carding gave it those extra shots is gone, so it drops to the ordinary Assault economy for the rest of that turn.

   **Example:** An LMG team takes an Assault Move this turn. Even though it's an F2 weapon while stationary, having moved it no longer qualifies — its only remaining option this turn is an ordinary Assault Fire at half rFP, not a second full-effect F# shot.

**6.6.5**  A deployed weapon that has expended its printed F# this turn may not Limber (Rule 6.3.2) until the following turn — the crew is serving the gun, not packing it up.

.. container:: rule-guide

   **Why:** Reflects that a crew actively serving a gun under F# this turn hasn't had the time or free hands to also break it down and pack it up — Limbering is a separate, incompatible activity from that turn's firing.

   **Example:** A tripod HMG fires all three of its F# shots this turn (reaching MOVED/FIRED). Its crew cannot also Limber the weapon this same turn — that must wait until next turn.

6.7  Desperate Fire and Close-Combat Defense
-----------------------------------------------


**6.7.1**  A unit marked MOVED/FIRED that is the target of a declared Close Assault or Overrun may still take **Desperate Fire** against those incoming attackers only — one Assault Fire (half effective rFP, Rule 6.3.3), 1 RP, at the declaration window (Rule 5.5.2). It may not fire at any other target this turn.

.. container:: rule-guide

   **Why:** Gives a fully spent (MOVED/FIRED) unit exactly one narrow, desperate option against the specific threat closing on it, rather than leaving it with zero defensive recourse just because it happened to act earlier in the turn.

   **Example:** Bravo is MOVED/FIRED from an earlier Regular Fire this turn. Alpha now declares Close Assault against Bravo. Bravo's player may spend 1 RP for Desperate Fire — an Assault Fire at half effective rFP — against Alpha specifically, but could not use this same fire against some other, unrelated enemy unit.

**6.7.2**  Close-combat defense — defensive grenades, melee, and withdrawal rights (Section 9) — is always available to a unit regardless of its action markers.

.. container:: rule-guide

   **Why:** Keeps close-combat defense entirely outside the action-marker economy, since Section 9's close assault procedure already has its own eligibility rules — a unit's action markers govern what it can do on its own initiative, not what it's entitled to defend itself with once attacked.

   **Example:** A unit marked MOVED/FIRED, with no part-actions or RP remaining, still fully participates in the Grenade Phase and Entry Fire Phase if it's the target of a close assault — those defensive rights aren't something its action markers could ever remove.
