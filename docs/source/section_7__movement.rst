Section 7 — Movement
====================

7.1  Movement Allowance
-----------------------


**7.1.1**  A unit's movement allowance is its M# value. This is the maximum number of hexes it may move in a single Move action.

.. container:: rule-guide

   **Why:** Ties movement allowance directly to the printed M# stat, keeping "how far can this unit move" a single, countable number rather than a formula.

   **Example:** A unit with M2 may move up to 2 hexes in a single Move action; it may choose to move fewer, but never more, in that one action.

**7.1.2**  One impulse represents approximately 20-25 seconds of real time. At tactical double time (200 yards per minute) a squad can cover roughly 70-80 yards — approximately 2 hexes at 40 yards per hex. M2 is therefore the standard infantry movement allowance.

.. container:: rule-guide

   **Why:** Grounds the M2 standard in real-world pacing — roughly 70-80 yards per 20-25-second impulse at double time — so the movement scale isn't an arbitrary game number but a deliberate translation of historical infantry tempo.

   **Example:** An M2 rifle squad's 2-hex move represents a squad jogging roughly 70-80 yards in the ~20-25 seconds one impulse abstracts, consistent with tactical double time at 40 yards per hex.

**7.1.3**  Movement allowance by unit type:

.. container:: rule-guide

   **Why:** Collects every unit type's movement rate in one place so a player never has to derive M# from first principles — heavier weapons and deployed guns are slower or immobile by design, reflecting their real weight and setup requirements.

   **Example:** A mobile HMG team (M1) moves half as far per activation as a rifle squad (M2); once deployed, that same HMG team is M0 and cannot move at all until it limbers (Rule 7.6.4).

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

.. container:: rule-guide

   **Why:** Prevents a unit from being stranded by a single expensive hex that happens to exceed its entire movement allowance — forbidding entry into terrain costlier than a unit's full M# would be far more disruptive than simply letting the activation end there.

   **Example:** An M2 unit facing a Dense Woods hex (3 MP) may still enter it, spending its entire activation's worth of MP on that one hex, rather than being forbidden from moving into terrain costlier than its full M#.

**7.1.5**  Status effects on movement: Suppressed units move at half M# (round down, minimum 1). Pinned units cannot move.

.. container:: rule-guide

   **Why:** Applies the same two ranged-fire statuses (Suppressed, Pinned) to movement specifically, since a unit keeping its head down or pinned in place has an obviously reduced — or zero — capacity to relocate.

   **Example:** A Suppressed M2 unit moves at half M#, rounded down: 1 hex, not 2. A Pinned unit of any M# cannot move at all this turn.

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
   * - Building (ground floor entry)
     - 1
     - Floors above ground have no separate entry cost — see Rule 7.2a
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

.. container:: rule-guide

   **Why:** Scales the road bonus to the mover's own M# (M#+1) rather than a flat bonus, so a fast unit and a slow unit both gain proportionally from moving in a column down a road, instead of the flat-bonus version that used to triple a slow unit's speed while barely helping a fast one (see the note quoted just below this rule).

   **Example:** An M1 HMG team moving entirely along road hexes gets M1+1 = 2 hexes that activation. An M2 rifle squad on the same road gets M2+1 = 3 hexes — each benefits by exactly one extra hex, not by a fixed multiple.

*NOTE: earlier drafts gave a flat 3 hexes on roads, which tripled an M1 weapon team's speed while giving an M2 squad only 50% — M#+1 scales the benefit to the mover.*

**7.2.2**  Elevation interaction example: a unit with M2 moving uphill one level into open ground costs 1 (terrain) + 1 (elevation) = 2 MP — the full activation for one hex. Two levels uphill in one activation is impossible for a standard M2 unit.

.. container:: rule-guide

   **Why:** Works through a concrete elevation-plus-terrain stacking case so the "costs add" principle — terrain cost plus elevation cost, both charged to the same hex entered — isn't left to be inferred from the terrain table alone.

   **Example:** An M2 unit moving uphill one level into open ground pays 1 (open ground) + 1 (elevation gain) = 2 MP for that single hex — its entire activation, even though open ground alone would only cost 1.

**7.2.3**  *Superseded — see Rule 7.2a.* Climbing within a building is no longer priced in Movement Points; it is its own AP-costing action (Rule 6.3.2, Change Floor).

7.2a  Building Floors
-----------------------

*Design note: Rule 7.2's table used to charge MP for "each additional floor" entered, and 7.2.3 worked through an example of a unit spending its whole MP allowance just climbing — but "floor" never appeared anywhere else in the rules. Nothing tracked which floor a unit ended up on, and nothing depended on it: the cost was real, the consequence wasn't. Confirmed with the designer: floor-to-floor movement becomes its own action, 1 AP per floor, rather than a line item in a Move's MP budget — and floor now does something once a unit is actually on one. See design note E.114.*

**7.2a.1**  A building hex may have more than one floor, as printed on the map or set in the scenario's own setup instructions. A unit entering a building hex from outside starts on the ground floor, at the hex's normal terrain MP cost (Rule 7.2) — there is no separate MP cost for the floors above it.

.. container:: rule-guide

   **Why:** Keeps the horizontal move into a building costing exactly what any other terrain entry costs, since climbing floors is now a wholly separate action rather than a component folded into the Move's own MP total.

   **Example:** A unit moving into a building hex pays the building's normal 1 MP entry cost, arrives on the ground floor, and its M# is otherwise unaffected by however many floors that building happens to have.

**7.2a.2**  Changing floors is its own action (Rule 6.3.2, Change Floor): 1 AP moves a unit exactly one floor, up or down, within its current building hex. It does not mark the unit MOVED/FIRED — the unit may act normally, including changing floor again, in a later activation this same turn, the same exception already granted to Deploy/Limber Weapon (Rule 6.3.2).

.. container:: rule-guide

   **Why:** Pricing every floor at its own AP, rather than folding several floors into one action, keeps climbing a real, separately-chosen cost at every step — a unit bound for the third floor genuinely commits three activations' worth of AP to get there, exactly as reaching it used to cost three MP under the old rule, just charged in the currency that actually has consequences (AP, not MP a Move never gets to spend elsewhere anyway).

   **Example:** A unit on the ground floor spends 1 AP to reach the first floor, then a second 1-AP activation later in the same turn to reach the second floor — two activations, two floors, with AP left over (if any) still available for a Move or Fire action afterward.

**7.2a.3**  A unit on a floor above ground applies Rule 14.9.8's Elevated OBS bonus (+1 for one floor above the target, +2 for two or more) when spotting or observing, using its floor number as its elevation for that purpose only. Floors do not otherwise block or degrade LOS between units in the same building, or between a building's occupants and the outside — the building's own terrain cover values already govern that.

.. container:: rule-guide

   **Why:** Gives the climb a real, historically grounded payoff — observers and snipers favouring upper floors is a genuine WWII tactical reality — without building a parallel LOS-blocking system for building interiors that nobody asked for; reusing the existing Elevated OBS bonus (Rule 14.9.8) is the smallest change that makes the AP cost mean something.

   **Example:** A sniper team on a building's second floor gets +2 OBS (two floors up) on top of any other applicable modifiers when attempting to spot a target outside — the same bonus a unit on a two-level hilltop would get over a target in the valley below, just earned by climbing stairs instead of a hillside.

    *See also: Rule 14.9.8 (the Elevated OBS bonus this rule reuses), Rule 6.3.2 (the Change Floor action).*

7.3  The Assault Bound
------------------------


**7.3.1**  Rule 6.3.3 defines the Assault economy in full — up to two part-actions (Assault Move, Assault Fire) at reduced effect, in either order, marked with ASSAULT after the first and MOVED/FIRED after the second. This rule covers only the movement-specific detail of the Assault Move part-action.

.. container:: rule-guide

   **Why:** Keeps the Assault Move part-action's own movement-specific mechanics (the 1-hex bound) here in Section 7, while leaving the full Assault economy — how many part-actions, what markers result — defined once in Section 6, so movement rules and action-economy rules don't duplicate each other.

   **Example:** A player looking up "how far does an Assault Move go" finds the answer here (7.3.2); a player asking "how many part-actions can I take, and what happens to my markers" finds that in Rule 6.3.3.

**7.3.2**  An Assault Move bounds the unit exactly 1 hex regardless of M#, paying that hex's terrain cost under the ordinary rules (Rule 7.1.4 — a unit may always enter a single hex regardless of cost, even if it exceeds what a full move would otherwise afford).

.. container:: rule-guide

   **Why:** Bounds an Assault Move to exactly 1 hex regardless of M#, so a fast unit (M3 leader) and a slow one (M1 HMG team) get the identical, deliberately modest distance from this part-action — the Assault economy trades reach for flexibility across the board, not just for slow units.

   **Example:** A leader (M3) and an HMG team (M1) both move exactly 1 hex if either takes an Assault Move — the leader's higher printed M# gives it no extra distance under this part-action.

**7.3.3**  A unit may take an Assault Move as either its first or second part-action; two Assault Moves in the same turn are legal (2 hexes total across two impulses) but for most infantry cover no more ground than a single Regular Move (Rule 6.3.2) at twice the AP cost.

.. container:: rule-guide

   **Why:** Allows two Assault Moves back-to-back, since nothing in the Assault economy forbids taking the same kind of part-action twice, while being upfront that this rarely beats a single Regular Move in ground covered — so players don't mistake the option for a hidden speed advantage.

   **Example:** An M2 rifle squad takes Assault Move, then Assault Move again (2 hexes total across two separate 1-AP activations) — the same 2 hexes a single Regular Move would have covered for half the AP cost.

7.4  Careless Movement
----------------------


**7.4.1**  A unit may declare Careless Movement when spending a Move action. The unit moves M#+1 hexes instead of its normal M# allowance.

.. container:: rule-guide

   **Why:** Is the one case where a Move action gains extra distance (M#+1) rather than merely avoiding a penalty, in exchange for the concealment cost defined in 7.4.2 — speed traded directly for being seen.

   **Example:** An M2 unit declaring Careless Movement may move up to 3 hexes (M#+1) this activation, instead of the normal 2.

**7.4.2**  Place the unit's MOVED/FIRED marker CARELESS-side up. The unit suffers -2 CON (concealment) for the remainder of this turn. Careless Movement is only ever taken as a Regular Move action, which already ends the unit's turn as MOVED/FIRED (Rule 6.3.2) — so this one physical marker, shown CARELESS-side up, carries both facts at once (Rule 3.6).

.. container:: rule-guide

   **Why:** Explains why Careless Movement gets away with sharing its physical marker with MOVED/FIRED (the Rule 3.6 consolidation) — since it's only ever taken as a Regular Move action, a carelessly-moved unit is always MOVED/FIRED for that turn too, so one marker can honestly carry both facts.

   **Example:** A unit takes Careless Movement this turn. Its marker is flipped to the CARELESS face rather than a separate token being added — that single marker means both "done for the turn" and "-2 CON" at once.

**7.4.3**  Any enemy unit with LOS to the moving unit may attempt a free spot roll during the movement reaction window. This spot roll costs no RP.

.. container:: rule-guide

   **Why:** Gives the -2 CON penalty a real, immediate consequence — a free spot attempt right when the risk is taken — rather than a passive stat that only matters if someone happens to check later.

   **Example:** An enemy unit with LOS to the carelessly-moving unit gets a free spot roll during the movement reaction window, at no RP cost, specifically because of the Careless declaration.

**7.4.4**  Careless movement represents troops moving quickly without tactical caution — appropriate in areas the owning player believes are safe. It is always risky if enemy units are present.

.. container:: rule-guide

   **Why:** States the tactical judgment call in plain language — Careless Movement is for ground the owning player genuinely believes is clear, not a free speed boost to use reflexively regardless of enemy presence.

   **Example:** A player uses Careless Movement to rush a unit across open ground behind their own lines, judged safe from enemy observation — using the same declaration to rush across a contested field would carry real spotting risk.

**7.4.5**  The marker is removed during the Recovery Phase, along with all other action markers (Rule 5.2.2).

.. container:: rule-guide

   **Why:** Gives the marker the same fixed one-turn lifetime as every other action marker, so the -2 CON penalty doesn't linger past the turn it was earned on.

   **Example:** The CARELESS-side marker placed this turn is removed, along with every other action marker, during the following turn's Recovery Phase.

7.5  Moving Target Modifier
---------------------------


**7.5.1**  A unit currently resolving a Move or Assault Move action, before that action fully completes, is a moving target. Opportunity fire against a moving target is declared at an interruption point — whenever the unit enters a new hex during its move (Rule 5.5.3) — and resolves before the unit moves further.

.. container:: rule-guide

   **Why:** Defines the exact window during which a unit counts as "moving" for opportunity-fire purposes — mid-move, before the action fully completes — rather than treating the whole turn as one long exposure.

   **Example:** A unit taking a 2-hex Move is a moving target only while that Move action is still resolving; once it completes and the unit is stationary again, it is no longer a moving target for this rule's purposes.

**7.5.2**  Opportunity fire against a moving target applies -2 rFP to the attacker.

.. container:: rule-guide

   **Why:** Gives moving targets a flat accuracy penalty against opportunity fire, reflecting that a unit in motion is a harder target than one holding still — this is the infantry-side version of what 18.1a.6/18.1a.9 handle separately for vehicles (see 7.5.2a).

   **Example:** An opportunity-firing unit's effective rFP against a moving infantry target is reduced by 2 compared to firing at the same target stationary.

**7.5.2a**  Exception: when the target is a vehicle, this penalty does not stack with the Gunnery Roll's own crossing-target adjustment (Rule 18.1a.6/18.1a.9) — the vehicle-specific adjustment replaces it. Rule 7.5.2 applies exactly as written when the target is infantry.

.. container:: rule-guide

   **Why:** Prevents the infantry moving-target penalty from double-stacking with the Gunnery Roll's own, more detailed crossing-target adjustment for vehicles — one penalty should apply, not both, when the target is a vehicle specifically.

   **Example:** A moving vehicle target uses only its Gunnery Roll crossing-target adjustment (Rule 18.1a.6/18.1a.9); Rule 7.5.2's flat -2 rFP does not additionally apply on top of it. A moving infantry target uses 7.5.2 exactly as written, since it has no Gunnery Roll to interact with.

**7.5.3**  If opportunity fire produces No Effect, the moving unit continues normally.

.. container:: rule-guide

   **Why:** Closes the loop for the mildest possible outcome — if opportunity fire achieves nothing, the interrupted move simply resumes as though the reaction hadn't happened.

   **Example:** Opportunity fire against a moving unit produces No Effect. That unit continues its Move action exactly as originally declared, with no MP lost.

**7.5.4**  If opportunity fire produces Suppressed, the moving unit loses 1 MP before continuing. That loss is the only effect on the current move — the Suppressed halving of M# (Rule 10.1) applies from the unit's next Move action, never retroactively to MP already allocated.

.. container:: rule-guide

   **Why:** Gives a Suppressed result from opportunity fire an immediate, one-time cost (1 MP) rather than retroactively degrading the unit's overall M# for movement already in progress — the ongoing Suppressed penalty (Rule 10.1) only applies going forward, to the unit's next Move action.

   **Example:** A unit with 2 MP remaining in its current Move is Suppressed by opportunity fire mid-move. It loses 1 MP immediately (down to 1 remaining) and continues; it does not also have its move recalculated at half M# retroactively.

**7.5.5**  If opportunity fire produces Pinned or worse, the moving unit stops immediately. Remaining MP are lost.

.. container:: rule-guide

   **Why:** Treats Pinned-or-worse as an immediate, hard stop rather than a partial penalty, since a unit taking that much punishment mid-move has plausibly gone to ground exactly where it stands rather than continuing forward.

   **Example:** A unit with 2 MP remaining is Pinned by opportunity fire mid-move. It stops immediately in its current hex; the remaining 2 MP are simply lost, not banked for a future activation.

7.6  Mobile Weapon Counters
---------------------------


**7.6.1**  Weapon counters with the MOBILE marker may move at infantry movement rate with a crew unit or independently.

.. container:: rule-guide

   **Why:** Gives towed/carried support weapons the same infantry movement rate as the units around them, whether or not a dedicated crew is currently attached, so a MOBILE weapon counter never becomes stranded just because its crew stepped away.

   **Example:** A MOBILE-marked mortar counter moves at infantry rate (per its own printed M#) whether it's moving together with its crew unit or being repositioned on its own.

**7.6.2**  A weapon counter with the MOBILE marker cannot fire.

.. container:: rule-guide

   **Why:** Makes MOBILE and "can fire" mutually exclusive by definition — a weapon being carried or towed isn't set up to shoot, matching Rule 6.6.4's parallel point that a moved ROF weapon drops out of its stationary firing mode.

   **Example:** A weapon counter still carrying its MOBILE marker cannot be declared as firing this turn, regardless of what its printed fire stats would otherwise allow — it must first deploy (7.6.3).

**7.6.3**  Removing the MOBILE marker (deploying the weapon) costs 1 AP. The weapon may not fire in the same impulse it deploys.

.. container:: rule-guide

   **Why:** Makes deploying cost a real action (1 AP) with a one-impulse setup delay, rather than a free, instantaneous state change — setting up a weapon to fire takes a moment even before the first shot.

   **Example:** A weapon counter spends 1 AP to remove its MOBILE marker (deploy). It cannot also fire in that same impulse — firing must wait for a later activation this turn.

**7.6.4**  Adding the MOBILE marker (limbering the weapon) costs 1 AP. The weapon may not fire in the same impulse it limbers. A weapon that expended its printed ROF this turn (Rule 6.6) may not limber until the following turn.

.. container:: rule-guide

   **Why:** Mirrors 7.6.3 for the reverse action, and cross-references the same ROF-expenditure restriction already established in Rule 6.6.5, so the two "packing up" rules — Section 6's ROF-specific one and this general one — stay consistent with each other.

   **Example:** A weapon counter spends 1 AP to add its MOBILE marker (limber). If that weapon expended its printed ROF earlier this turn, it cannot limber until next turn — the same restriction Rule 6.6.5 already states for ROF weapons specifically.

7.7  Night Movement Risk
-------------------------


**7.7.1**  A Move or Assault Move at night that takes a unit beyond the Rule 23.1 visibility cap from where it started, and not entirely through a lit hex (Rule 23.2), requires a check: roll 1d6 + Morale modifier against threshold 3 — the same threshold already used for Suppressed recovery (Rule 5.2.4) and the reduced-face close-assault nerve check (Rule 9.1.3a). On failure, the unit stops 2 hexes short of its intended hex — a fixed shortfall, not randomly determined — though its full movement allowance is still spent.

.. container:: rule-guide

   **Why:** Reuses a threshold players already know rather than adding a new number to memorise, and makes the failure consequence a fixed, unambiguous shortfall instead of a further roll — a unit that loses its way in the dark ends up somewhere predictable, not somewhere else the dice have to determine.

   **Example:** A Regular unit (Morale modifier +0) moving 4 hexes at night with no lit hex along the way rolls 1d6 against threshold 3 — a 67% pass rate, the same odds as an ordinary Suppressed recovery roll. On a failure, it stops after only 2 hexes of movement despite having paid for all 4.

    *See also: Rule 23.1 (the visibility cap this rule is measured against), Rule 23.2 (illumination that removes the check entirely along a lit route).*
