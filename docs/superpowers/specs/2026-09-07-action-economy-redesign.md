# Action Economy Redesign — Regular / Assault / ROF

**Status: APPROVED 2026-09-08 (designer). Applied to the rulebook in the same branch.**

Corrects the action economy adopted in E.63/E.75, which resolved the v0.9.2
contradiction (old 6.1.2/6.1.3/6.3) with a model that does not match the
designer's intent. This spec records the intended design as confirmed in the
2026-09-07 design conversation, supersedes E.63's model and E.75's
symmetry change, and keeps everything else (reaction windows E.64, the CRT,
the morale system) untouched.

## 1. The three ways a unit can spend its turn

Every combat unit's turn ends in the **MOVED/FIRED** state (done: no more
movement or fire this turn). Three paths lead there:

### 1a. Regular action — one full-effect action, then done

- **Regular Move**: full M#, terrain costs as normal. → MOVED/FIRED.
- **Regular Fire**: one attack at full effective rFP. → MOVED/FIRED
  (exception: stationary ROF > 1 weapons, path 1c).
- Careless Movement is a Regular Move variant (M#+1, CARELESS marker as
  today). Spot Action, Go Hidden, Deploy/Limber and the other 6.3 actions
  are regular actions → MOVED/FIRED.

### 1b. Assault economy — two part-actions at reduced effect

- A fresh unit may instead take up to **two part-actions**, in any
  combination and order, in separate impulses:
  - **Assault Move**: **1 hex, regardless of M#** — the bound as printed
    in 7.3.2, kept as-is (a deliberate choice: the assault bound is a
    rush to the next position, not half a road march).
  - **Assault Fire**: one attack at **half effective rFP, rounded down**
    (applied after falloff/terrain/status modifiers — §Resolved-A).
- After the **first** part-action: place the **ASSAULT** marker (one
  part-action spent; one remains — move or fire, either kind).
- After the **second**: → MOVED/FIRED.
- The paths do not mix: a unit that has taken any regular action cannot
  take part-actions, and an ASSAULT-marked unit's only remaining option is
  its second part-action.
- Legal sequences include: assault move → assault fire; assault fire →
  assault move; assault fire → assault fire.

### 1c. ROF weapons — stationary machine guns fire more than once

- **ROF** is an equipment property (rules-text level for now; the printed
  F# and the counter pipeline are NOT changed in this pass — full counter
  review later):
  - Deployed tripod **HMG: ROF 3** (deployed = M0; can never move and fire
    in the same turn — already ruled).
  - Emplaced bipod **LMG / MMG: ROF 2** — stationary only. The bipod
    position (pre-sighting / quick range card) is what buys the extra
    burst.
  - All other units: ROF 1 (their regular fire is their turn).
- A stationary ROF > 1 weapon fires at **full effective rFP** each time,
  marked **FIRED 1 → FIRED 2 → FIRED 3** up to its ROF; when ROF is
  expended → MOVED/FIRED.
- A **moving MG is in the assault economy** like anyone else: an LMG (and
  bipod-capable MMGs) may assault move + assault fire at half rFP — one
  crewman operating it off-hand. No weapon fires at ROF > 1 in a turn it
  moved.
- A deployed weapon that has expended its ROF **may not limber (take the
  MOBILE marker) until the next turn** — the crew is serving the gun, not
  packing it.

## 2. Overwatch = reaction fire

- There is no separate overwatch state or marker. Any unit with fire
  remaining may **react** during an enemy impulse at the Rule 5.5 timing
  points (declaration window, movement interruption points, post-action
  window) against an action that draws fire — moving into a hex, firing,
  or any other fire-drawing action (Exposure is eliminated, §7).
- Reaction fire costs the reacting player **1 RP** (the existing RP
  economy stands) and costs the reacting unit **no impulse and no AP** —
  but it marks the unit exactly as if it had taken that fire on its own
  impulse:
  - Ordinary units react with **Assault Fire** (half rFP): a fresh unit
    gains ASSAULT; an ASSAULT unit goes to MOVED/FIRED; a MOVED/FIRED unit
    cannot react (except §3).
  - Stationary ROF > 1 weapons react at **full rFP**, consuming a FIRED
    pip per reaction. This is the beaten zone: a sited MG fires on
    everyone entering its field, RP permitting, until its ROF is expended.
    Range and ROF are what limit machine guns — not damage per burst.

## 3. Desperate fire and close-combat defense

- A MOVED/FIRED unit that is the target of a declared **Close Assault or
  Overrun** may still take Defensive Fire against **those incoming
  attackers only**, at assault rate (half rFP), 1 RP — desperate fire.
- Close-combat defense (defensive grenades, melee, withdrawal rights)
  is always available regardless of markers.

## 4. Global halving convention

"Half, rounded down" is stated once in Section 2 (conventions) as the
default for any halving the rules call for, and assault fire uses it.
The existing printed halvings already follow it where they say so
(suppressed movement, grenade-phase cover, flamethrower cover).
**RP = round(AP/2) is left exactly as printed** — it was a made choice,
and the convention governs new halvings, not a retrofit of old ones.

Half−1 was considered for assault fire ("two assault fires must never
equal one regular fire") and rejected as unnecessary: the CRT is
nonlinear, so two half-rFP attacks are strictly weaker than one full
attack even at equal summed rFP (rFP 8 vs Defence 8: one full fire =
58.2% Casualty-or-better; two fires at 4 = 46.4% chance of at least one,
and lower in every severity band). A unit's own two assault fires resolve
in different impulses and can never be summed into one attack.

## 5. AP costs

- Each regular action: 1 AP (as today).
- Each assault part-action: 1 AP (a full assault sequence costs 2 AP
  across two impulses — command attention is spent per order).
- Each ROF fire on the weapon's own impulse: 1 AP.
- Reactions: 0 AP, 1 RP.

## 6. Marker set (components unchanged, semantics updated)

| Marker | New meaning |
| --- | --- |
| ASSAULT | One part-action spent; one remains (move or fire) |
| FIRED 1/2/3 | ROF fires expended by a stationary ROF > 1 weapon |
| MOVED/FIRED | Done — no further movement or fire this turn (the existing MOVED component, relabelled) |
| CARELESS | As today (careless regular move) |
| OPPORTUNITY | Unchanged this pass (informational) |
| MOBILE / TRAVERSED / status markers | Unchanged |

Turn end: the Action Phase runs until both players pass or every unit is
marked — unchanged.

## 7. Exposure — eliminated (designer decision, 2026-09-08)

The Exposed and Firing Exposed conditions are removed entirely. The
action itself draws the fire: reactions resolve at the moment of the
triggering action (a hex entered, a shot fired), the reacting player
decides how much to spend on it — limited by resources (RP, the unit's
own economy/ROF) and judgment — and the window is momentary: hold fire
and the mover may reach cover two hexes on; you missed it. No token is
left behind, nothing persists. Skulking dies structurally instead: an
assault move out of cover costs one impulse, the assault fire a second,
and the unit is then MOVED/FIRED — stuck in the open until the marker
comes off for free next Recovery Phase. The old moving-target penalty
(fire at a unit in transit: attacker −2 rFP) is unrelated to Exposure
and is retained.

## 8. Explicitly out of scope this pass

- Printed F# values, `counters/infantry_calc`, and the roster CSVs —
  no counter or pipeline changes until the full counter review.
- Vehicle fire actions (18.1a follow-up shots etc.) stay on their current
  wording; mapping vehicles onto ROF is part of the counter review.
- Mortar fire missions (Section 16) keep their own mission economy.
- The OPPORTUNITY-marker consolidation question stays open (separate,
  dismissed pass).

## Resolved points (designer, 2026-09-08)

- **A. Fire halving applies to the final effective rFP** — after
  falloff, terrain, and status modifiers, round down (then the rFP ≤ 0
  rule applies normally). Halving the printed value before falloff would
  make assault fire pointless at range.
- **B. Exposure eliminated** — see §7.

## Sections affected on implementation

6.1–6.6 (rewrite), 6.3 table, 7.3 (rewrite), 7.4 (variant note),
2.x (halving convention), 5.3.4 (RP rounding), 8.10 summary, 9.1.2/9.2.2
(marker names), 1.2/1.3/3.6 marker lists and glossary, Appendix F index
entries, plus superseding design notes for E.63 and E.75.
