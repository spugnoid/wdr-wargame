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

**5.2.2**  All action markers (MOVED, FIRE 1/2/3, ASSAULT, OPPORTUNITY) are removed from all counters.

**5.2.3**  Each unit with a SUPPRESSED or PINNED status marker attempts a recovery roll.

**5.2.4**  Recovery roll procedure: roll 1d6 and add the unit's Morale modifier (Rule 15.2.1a). Compare to the recovery threshold for the unit's current status.

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

**5.2.6**  A leader adjacent to a recovering unit adds their CMD rating to the recovery roll during the Recovery Phase. For mid-turn rally using the Rally action, use the RAL threshold instead (see Rule 12.6).

**5.2.7**  Units may not attempt recovery mid-turn. Recovery occurs only during this phase unless a leader spends 1 AP to rally an adjacent unit (see Section 12).

5.3  Command Phase
------------------


**5.3.1**  Both players roll 1d6 and add any applicable leader bonus. The higher result wins initiative for this turn. Re-roll ties.

**5.3.2**  The initiative winner acts first in each impulse, wins all reaction timing ties, and receives +1 RP for this turn.

**5.3.3**  Action Points (AP) are calculated as: AP = 1 (base) + Σ CMD ratings of all functional leaders. See Section 12 for full leader rules.

**5.3.4**  Reaction Points (RP) are calculated: RP = round(AP / 2), minimum 1.

**5.3.5**  For test scenarios without leaders, use fixed values: AP = 3, RP = 2 per side.

**5.3.6**  Unspent AP and RP are lost at the end of the Action Phase. They may not be carried forward to the next turn.

5.4  Action Phase
-----------------


**5.4.1**  The Action Phase consists of a series of impulses. The initiative player takes the first impulse.

**5.4.2**  Players alternate impulses. Each impulse consists of one action by the active player, followed by a reaction window for the non-active player.

**5.4.3**  The Action Phase ends when both players pass consecutively without taking an action.

5.5  Impulse Sequence
---------------------


Each impulse proceeds through three timing steps. Reactions occur only at the moments these steps define.

**5.5.1**  Declaration: the active player declares one action (costs 1 AP), naming the acting unit and, where relevant, the target or intended path — or passes.

**5.5.2**  Declaration window: after the declaration but before the action resolves, the non-active player may spend RP on reactions that respond to the declaration itself — Defensive Fire against a declared Close Assault, an Interrupt, or Opportunity Fire against an eligible target already in LOS (including an Exposed unit). Reactions in this window resolve before the declared action. If a declaration-window reaction leaves the acting unit Suppressed or Pinned, or renders the declared action illegal (target destroyed, LOS lost), the declared action is cancelled; the active player retains the AP and may declare a different action.

    *See also: Rule 6.4.2 (the same cancellation rule for Interrupts).*

**5.5.3**  Resolution: the action resolves. A Move action (or the move portion of an Assault action) resolves hex by hex — each time the moving unit enters a new hex, an interruption point occurs: the non-active player may spend RP on Opportunity Fire against the moving unit (and take any free spot rolls, Rule 7.4.3) before it moves further. Results of fire at an interruption point apply per Rules 7.5.3–7.5.5.

**5.5.4**  Post-action window: after the action resolves, the non-active player may spend RP on reactions triggered by the action's outcome — for example, Opportunity Fire against a unit that is now Exposed, or a Spot Roll against a unit that fired or became visible. Multiple reactions may be taken in one window if sufficient RP are available.

**5.5.5**  All windows close. The next impulse begins with the opposing player as active.

5.6  Passing
------------


**5.6.1**  A player may pass their impulse without spending AP. Passing does not prevent the player from acting in subsequent impulses.

**5.6.2**  When both players pass consecutively (one after the other), the Action Phase ends immediately.

**5.6.3**  A player who has exhausted their AP must pass all remaining impulses.
