Section 5 — Turn Structure
==========================

5.1  Turn Sequence Overview
---------------------------


Each game turn proceeds through three phases in the following order:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Phase**
     - **Description**
   * - 1. Recovery Phase
     - All units attempt to recover from Suppressed and Pinned status. All action markers removed.
   * - 2. Command Phase
     - Initiative is determined. Action Points and Reaction Points are allocated.
   * - 3. Action Phase
     - Players alternate spending Action Points in a series of impulses until both pass consecutively.


5.2  Recovery Phase
-------------------


**5.2.1**  The Recovery Phase occurs at the start of each game turn before any actions are taken.

.. container:: rule-guide

   **Why:** Puts recovery first in the turn so units enter the Action Phase already knowing their current status — nothing that happens later in the same turn can retroactively change whether a unit shook off Suppressed or Pinned status this turn.

   **Example:** Alpha becomes Suppressed near the end of one turn. It gets its recovery roll at the very start of the next turn's Recovery Phase, before either side spends any Action Points.

**5.2.2**  All action markers (ASSAULT, FIRED 1/2/3, MOVED/FIRED, CARELESS) are removed from all counters.

.. container:: rule-guide

   **Why:** Resets the action-tracking markers every turn since they only ever describe what a unit did *this* turn (Rule 3.6) — leaving them in place into the next turn would incorrectly restrict actions the unit hasn't taken yet.

   **Example:** Alpha ends a turn with a MOVED/FIRED marker. That marker is removed in the following Recovery Phase, so Alpha starts the new turn free to move and fire again.

**5.2.3**  Each unit with a SUPPRESSED or PINNED status marker attempts a recovery roll.

.. container:: rule-guide

   **Why:** Scopes the automatic recovery roll to status markers specifically — action markers already got cleared unconditionally in Rule 5.2.2, so this step only concerns the effects that persist until actively thrown off.

   **Example:** A unit with a FIRED 2 marker and no status markers has nothing to roll for this step; a unit carrying a SUPPRESSED marker does, regardless of what action markers it also had before Rule 5.2.2 cleared them.

**5.2.4**  Recovery roll procedure: roll 1d6 and add the unit's Morale modifier (Rule 15.2.1a). Compare to the recovery threshold for the unit's current status.

.. container:: rule-guide

   **Why:** Ties recovery odds to unit quality via the Morale modifier, so a green unit and a veteran unit facing the same Suppressed status don't have identical chances of shaking it off.

   **Example:** A unit with a +1 Morale modifier rolls 1d6+1 against the Suppressed threshold of 3 (Rule 5.2 table) — a base roll of 2 would fail alone but succeeds once the modifier is added.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Status**
     - **Recovery Threshold**
     - **Notes**
   * - Suppressed
     - 3
     - Roll + Morale modifier ≥ 3 to recover
   * - Pinned
     - 5
     - Roll + Morale modifier ≥ 5 to recover
   * - Casualty + Suppressed
     - 6
     - Roll + Morale modifier ≥ 6 to recover suppression (step loss remains)


**5.2.5**  Recovery is never automatic. A regular unit (modifier +0) recovers from Suppressed on a roll of 3+ (67%) and from Pinned on 5+ (33%). An elite unit (modifier +1) recovers on 2+ (83%) and 4+ (50%) respectively. A leader's CMD bonus (Rule 5.2.6) can make recovery certain — this is deliberate: morale quality and leadership, not time alone, determine how quickly a force shakes off fire effects.

.. container:: rule-guide

   **Why:** States outright that recovery has real failure odds even for good units, so a player doesn't treat the Recovery Phase as a formality — Suppressed and Pinned statuses are meant to sometimes persist and shape the following turn.

   **Example:** A regular Pinned unit recovers only 33% of the time per attempt (roll 5+ on 1d6) — it can easily stay Pinned into the next turn's Action Phase without a leader's help (Rule 5.2.6).

**5.2.6**  A leader adjacent to a recovering unit adds their CMD rating to the recovery roll during the Recovery Phase. For mid-turn rally using the Rally action, use the RAL threshold instead (see Rule 12.6).

.. container:: rule-guide

   **Why:** Gives leadership a direct, mechanical payoff during automatic recovery, distinct from the separate mid-turn Rally action (Rule 12.6) — the same leader helps in two different ways depending on when the recovery attempt happens.

   **Example:** A leader with CMD 2 standing adjacent to a Pinned unit during the Recovery Phase adds +2 to that unit's 1d6 recovery roll against the threshold of 5 — turning a 33% chance into a near-certain one.

**5.2.7**  Units may not attempt recovery mid-turn. Recovery occurs only during this phase unless a leader spends 1 AP to rally an adjacent unit (see Section 12).

.. container:: rule-guide

   **Why:** Keeps recovery from status effects tied to the structured Recovery Phase by default, so a Suppressed or Pinned unit's condition is a real cost for the rest of that turn — the Rally action is the one deliberate, AP-priced exception, not a loophole.

   **Example:** A unit Pinned mid-turn stays Pinned for the remainder of that turn's Action Phase; a leader can still spend 1 AP to Rally it early (Section 12), but the unit can't simply attempt its own recovery roll again before the next Recovery Phase.

**5.2.8**  Recovery Phase internal sequence — resolve in this order (several subsystems act "during the Recovery Phase"; when order matters, this list governs):

.. container:: rule-guide

   **Why:** Fixes a single resolution order for the several different subsystems that all technically happen "during the Recovery Phase," since prisoner escapes, marker aging, recovery rolls, and rally attempts can interact if left to resolve in an arbitrary order.

   **Example:** Because escapes (step 2) resolve before rout/dispersed rallies (steps 6-7), a leader's CMD used to help a routing unit rally is never diverted earlier in the same phase to stop a prisoner escape attempt — the sequence keeps the two from competing.

1. Remove action markers (Rule 5.2.2).
2. Prisoner escape attempts for under-guarded groups (Rule 11.4.2).
3. CONTACT markers age one step; COLD markers are removed (Rule 14.8.2).
4. Suppressed/Pinned recovery rolls (Rules 5.2.3–5.2.4) and vehicle bail-out checks (Rule 19.2.1).
5. Molotov engine-fire rolls (Rule 18.10.3).
6. Routing units attempt rally (Rule 10.6.7).
7. Dispersed units attempt rally (Rule 10.5.4).

*Escapes precede rallies (prisoners slip away while the line is still disorganised); status recovery precedes rout and dispersed rallies so a just-recovered leader's CMD is available to them.*

5.3  Command Phase
------------------


**5.3.1**  Both players roll 1d6 and add any applicable leader bonus. The higher result wins initiative for this turn. Re-roll ties.

.. container:: rule-guide

   **Why:** Decides who acts first each turn with a contest that leadership can influence but chance still decides, rather than a fixed or purely leader-determined order that would make one side predictably always lead.

   **Example:** A side with a leader bonus of +1 rolls 1d6+1 for initiative; a strong roll from the other side can still beat it, since the bonus tilts the odds without guaranteeing the win.

**5.3.2**  The initiative winner acts first in each impulse and wins all reaction timing ties. Initiative grants tempo, not resources — both sides' RP pools are computed identically (Rule 5.3.4).

.. container:: rule-guide

   **Why:** Keeps initiative's benefit limited to sequencing and tie-breaking rather than letting it also inflate the winner's resource pool — a side that loses the initiative roll still has the same RP to react with, just slightly worse timing on ties.

   **Example:** Winning initiative lets Alpha's side act first this turn and win any simultaneous-reaction ties, but it doesn't give that side more Reaction Points than the other side's own AP-based RP calculation (Rule 5.3.4) would produce.

**5.3.3**  Action Points (AP) are calculated as: AP = 1 (base) + Σ CMD ratings of all functional leaders. See Section 12 for full leader rules.

.. container:: rule-guide

   **Why:** Makes a side's action economy scale directly with its surviving, functional leadership — losing leaders doesn't just remove their personal actions, it shrinks the whole side's AP pool for the turn.

   **Example:** A side with one functional leader of CMD 2 gets AP = 1 + 2 = 3 for the turn; losing that leader mid-battle (and gaining no replacement) drops future turns toward the base AP = 1, moderated by the NCO floor (Rule 5.3.3a).

**5.3.3a**  NCO floor: a side with **no functional leaders** that still has at least 3 unbroken combat units on the map receives AP = 2 (and thus RP = 1) — junior NCOs take over enough to keep the force fighting, at half or less of a typical led pool. With fewer than 3 unbroken combat units remaining, the base AP = 1 stands: the remnant is beyond coordination.

.. container:: rule-guide

   **Why:** Keeps a leaderless-but-substantial force from collapsing all the way to the bare AP = 1 minimum (Rule 5.3.3), since real junior NCOs would step up informally — but only while enough of the unit still exists to organize; a shattered remnant genuinely can't coordinate even that much.

   **Example:** A side that loses its only leader but still has 4 unbroken combat units gets AP = 2 under the NCO floor; if attrition later drops it to 2 unbroken units, the floor no longer applies and AP reverts to the base 1.

    *See also: Rule 12.3.4 (functional leaders), Rule 12.3.3.*

**5.3.4**  Reaction Points (RP) are calculated: RP = round(AP / 2), minimum 1.

.. container:: rule-guide

   **Why:** Derives a side's reactive capacity directly from its active capacity rather than tracking it separately, so a side with a bigger AP pool also has more RP to interrupt and respond with — leadership strength pays off on both sides of the impulse.

   **Example:** A side with AP = 3 gets RP = round(3 / 2) = 2 for the turn (this rounding uses the round-half-up carve-out of Rule 2.5.3, not the general halve-round-down convention).

**5.3.5**  For test scenarios without leaders, use fixed values: AP = 3, RP = 2 per side.

.. container:: rule-guide

   **Why:** Gives designers and playtesters a simple, symmetric baseline for scenarios that intentionally strip out leader mechanics, so action economy testing isn't tangled up with unrelated leader-assignment questions.

   **Example:** A stripped-down test scenario with no leader counters on either side simply uses AP = 3, RP = 2 for both sides, bypassing the CMD-summation calculation in Rule 5.3.3 entirely.

**5.3.6**  Unspent AP and RP are lost at the end of the Action Phase. They may not be carried forward to the next turn.

.. container:: rule-guide

   **Why:** Forces each turn's resources to be spent or wasted within that turn, preventing a side from hoarding AP/RP across turns to unleash an oversized action phase later — the pressure to act now is part of the game's pacing.

   **Example:** A side that only spends 2 of its 3 AP one turn simply loses the remaining 1 AP when the Action Phase ends — the next turn starts with a fresh AP total from Rule 5.3.3, not a carried-over surplus.

5.4  Action Phase
-----------------


**5.4.1**  The Action Phase consists of a series of impulses. The initiative player takes the first impulse.

.. container:: rule-guide

   **Why:** Breaks the whole Action Phase down into small, alternating impulses rather than one big simultaneous turn, so each side's actions can be seen and reacted to individually — the initiative winner (Rule 5.3.1) gets the tempo advantage of going first.

   **Example:** After winning initiative, Alpha's side takes the very first impulse of the Action Phase, declaring one action before the other side gets any chance to act.

**5.4.2**  Players alternate impulses. Each impulse consists of one action by the active player, followed by a reaction window for the non-active player.

.. container:: rule-guide

   **Why:** Keeps the Action Phase strictly one-action-then-react at a time, which is what makes the reaction system (Rule 5.5) meaningful — a player never has to guess what a whole batch of enemy actions will be before responding.

   **Example:** Alpha's side declares and resolves one action; only then does the other side get its reaction window before the next impulse (Squad Bravo's side, if alternating normally) begins.

**5.4.3**  The Action Phase ends when both players pass consecutively without taking an action.

.. container:: rule-guide

   **Why:** Ends the phase on mutual exhaustion or mutual choice to stop, rather than a fixed impulse count, so a phase naturally runs as long as either side still has something worth spending AP on.

   **Example:** If Alpha's side passes and then the other side also passes on the very next impulse, the Action Phase ends immediately — but if either side takes an action in between, the phase continues.

5.5  Impulse Sequence
---------------------


Each impulse proceeds through three timing steps. Reactions occur only at the moments these steps define.

**5.5.1**  Declaration: the active player declares one action (costs 1 AP), naming the acting unit and, where relevant, the target or intended path — or passes.

.. container:: rule-guide

   **Why:** Requires the acting unit, target, and path to be named up front, before any dice are rolled, so the non-active player's declaration-window reaction (Rule 5.5.2) has real, specific information to respond to rather than a vague intention.

   **Example:** Alpha's side declares "Alpha fires at Squad Bravo" as its one action for 1 AP — the target is fixed by that declaration, so the reacting player knows exactly what they're responding to in the next step.

**5.5.2**  Declaration window: after the declaration but before the action resolves, the non-active player may spend RP on reactions that respond to the declaration itself — Defensive Fire against a declared Close Assault, an Interrupt, or Opportunity Fire against an eligible target already in LOS. Reactions in this window resolve before the declared action. If a declaration-window reaction leaves the acting unit Suppressed or Pinned, or renders the declared action illegal (target destroyed, LOS lost), the declared action is cancelled; the active player retains the AP and may declare a different action.

.. container:: rule-guide

   **Why:** Lets a declared action be pre-empted by a fast reaction that resolves first, then refunds the AP if that reaction actually invalidates the declared action — the active player loses tempo to a good reaction but doesn't also lose the resource for an action that never happened.

   **Example:** Alpha declares a Close Assault; the defender spends RP on Defensive Fire in this window, which Suppresses Alpha before the assault resolves. The Close Assault is cancelled, but Alpha's side keeps the 1 AP it spent and may declare something else instead.

    *See also: Rule 6.4.2 (the same cancellation rule for Interrupts).*

**5.5.3**  Resolution: the action resolves. A Move action (or the move portion of an Assault action) resolves hex by hex — each time the moving unit enters a new hex, an interruption point occurs: the non-active player may spend RP on Opportunity Fire against the moving unit (and take any free spot rolls, Rule 7.4.3) before it moves further. Results of fire at an interruption point apply per Rules 7.5.3–7.5.5.

.. container:: rule-guide

   **Why:** Breaks movement into per-hex interruption points instead of resolving a whole move as one instantaneous jump, since a unit crossing open ground is realistically exposed to fire at every hex it passes through, not just at its final destination.

   **Example:** Alpha moves 3 hexes across open ground. The defender gets a fresh Opportunity Fire chance at each of the 3 hexes entered, not a single chance only once Alpha reaches its final hex.

**5.5.4**  Post-action window: after the action resolves, the non-active player may spend RP on reactions triggered by the action's outcome — for example, Opportunity Fire against the unit that just moved or fired, or a Spot Roll against a unit that fired or became visible. Multiple reactions may be taken in one window if sufficient RP are available.

.. container:: rule-guide

   **Why:** Gives the non-active player one more chance to react after the dust from the resolved action settles — some responses (like spotting a unit that just revealed itself by firing) only make sense once the action's outcome is already known, not while it's still being declared or resolved.

   **Example:** After Alpha fires and reveals its position, the defender's side can spend RP in this window on a Spot Roll against Alpha, and — if enough RP remains — also on Opportunity Fire against a different unit that moved earlier in the same action.

**5.5.5**  All windows close. The next impulse begins with the opposing player as active.

.. container:: rule-guide

   **Why:** Cleanly hands off "active player" status each impulse rather than letting reaction windows blur into who acts next — once every window from this impulse is closed, the turn structure resets and the roles simply swap.

   **Example:** After Alpha's side finishes its impulse (declaration, resolution, and both reaction windows), the very next impulse belongs to the other side as the active player, regardless of how many reactions were spent in the impulse that just ended.

5.6  Passing
------------


**5.6.1**  A player may pass their impulse without spending AP. Passing does not prevent the player from acting in subsequent impulses.

.. container:: rule-guide

   **Why:** Lets a player hold AP for a better moment without being punished for it — passing costs nothing and doesn't lock the player out of acting later, so waiting is always a live tactical option, not a one-way commitment.

   **Example:** A side with 2 AP remaining passes one impulse to see what the opponent does, then spends its AP normally in a later impulse once a better target or moment appears.

**5.6.2**  When both players pass consecutively (one after the other), the Action Phase ends immediately.

.. container:: rule-guide

   **Why:** Uses mutual passing as the phase's natural end condition (Rule 5.4.3 restates this), since two consecutive passes mean neither side currently wants to spend more AP — there's nothing left worth waiting for.

   **Example:** Alpha's side passes; if the other side also passes on the very next impulse, the Action Phase ends right there, even if both sides still have unspent AP.

**5.6.3**  A player who has exhausted their AP must pass all remaining impulses.

.. container:: rule-guide

   **Why:** Makes passing a forced default once a side is out of AP rather than an option it retains — a side with 0 AP has nothing legal to declare (Rule 5.5.1 costs 1 AP per action), so its remaining impulses are formalities.

   **Example:** A side that has spent all 3 of its AP for the turn must simply pass every impulse for the rest of the Action Phase, even while the other side still has AP left to spend.
