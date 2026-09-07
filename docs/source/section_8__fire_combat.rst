Section 8 — Fire Combat
=======================

8.1  Fire Resolution Overview
-----------------------------


Fire combat in With Deepest Regret... uses a single unified resolution procedure for all ranged fire. The procedure calculates effective firepower at range, optionally looks up a Resolution FP value, then resolves with a dice roll against the target's defence.

The full procedure for any fire combat action:

**8.1.1**  All units firing at the same target as part of one Fire action form a single fire group, regardless of ⬡h interval (Rule 8.3).

**8.1.1a**  A unit with multiple fire lines fires **all** of them in one Fire action: each line computes its own effective rFP at the target's range (Rule 8.2) and the values join the fire group's sum like separate firers. A single fire action never splits a unit's lines across different targets. Exception: a sniper's deliberate-targeting shot (Rule 20.2) uses the sniper line alone and never groups.

**8.1.2**  For each firing unit, calculate the effective rFP at that unit's own firing range (Rule 8.2).

**8.1.3**  Apply intervening terrain penalties and any other modifiers (elevation, exposure status, etc.) to each unit's effective rFP individually — each firer uses its own range and its own line of sight.

**8.1.4**  Sum the effective rFP values within each group. Units occupying the same hex may use the sum-first shortcut instead (Rule 8.3.3).

**8.1.5**  If a single unit fires, use effective rFP directly as Resolution FP. If multiple units in a group fire, consult the Resolution Strip (Rule 8.4) to find the Resolution FP.

**8.1.6**  Roll 1d6 + 1d8 + 1d12. Add Resolution FP to the roll.

**8.1.7**  Subtract the target's Defence value plus applicable cover modifier.

**8.1.8**  The result is the margin. Consult the Result Threshold Table (Rule 8.6 / Appendix C) to determine the result.

8.2  Falloff Calculation
------------------------


**8.2.1**  Effective rFP at a given range is calculated as follows:

**Effective rFP = rFP − (f × floor(max(0, range − 1) / h))**

**8.2.2**  Where rFP is the base firepower value, f is the falloff loss value (printed as -f on the counter), h is the hex interval (printed inside the ⬡ symbol), and range is the distance in hexes from firer to target.

**8.2.3**  Range 0 (same hex) and range 1 (adjacent hex) both use the full rFP value with no falloff reduction.

**8.2.4**  Example: A fire line reading 7 ⬡4 -1 at range 9 hexes. Effective rFP = 7 − (1 × floor(8 / 4)) = 7 − 2 = 5.

**8.2.5**  A fire line whose effective rFP after **all** modifiers (falloff, intervening terrain, smoke, status and exposure penalties) is 0 or less contributes nothing: it adds nothing to a fire group's sum, and if no line in the group has a positive effective rFP, no attack occurs and no FIRE marker is placed. Effective rFP never goes below 0 for any purpose — a deeply degraded line cannot drag a group's total down.

8.3  Grouping by Interval
-------------------------


**8.3.1**  When multiple units fire at the same target in the same impulse as part of one Fire action, they combine into a single fire group. Grouping is not optional and has no ⬡h restriction: the per-unit method of Rule 8.3.2 is well-defined for any mix of fire lines, because each unit's falloff is computed on its own printed curve before the values are summed.

    *See also: Rule 8.8 (attacks that cannot group — reaction fire, sniper deliberate targeting, separate fire actions).*

**8.3.2**  To form a fire group: each unit first calculates its own effective rFP (falloff at its own range per Rule 8.2, plus its own intervening terrain and modifiers). Sum the effective rFP values. The group is resolved as a single attack using the summed value.

**8.3.3**  Same-hex shortcut: when every unit in the group occupies the same hex **and shares the same ⬡h interval**, all firers share an identical range, line of sight, and falloff step. The group may instead sum rFP values and f values first — expressed as (total rFP) ⬡h −(total f) — and apply the falloff formula once to the summed values. This produces a result identical to the per-unit calculation (Rule 8.3.6). Mixed-⬡h groups simply use the per-unit method of Rule 8.3.2; the shortcut is a convenience, never a requirement.

**8.3.5**  Example (same-hex shortcut): Three units in the same hex with fire lines 6 ⬡4 -1, 8 ⬡4 -1, and 5 ⬡4 -1 form a group: 19 ⬡4 -3. At range 5, effective rFP = 19 − (3 × floor(4/4)) = 19 − 3 = 16.

**8.3.6**  Mathematical proof of the shortcut: for units sharing a hex, the falloff term floor(max(0, range − 1) / h) is identical for every firer — it depends only on range and h. It therefore distributes across the sum: Σ(rFPᵢ − fᵢ × k) = ΣrFPᵢ − (Σfᵢ) × k. The equivalence holds at all ranges, but only when range, ⬡h, and intervening terrain are identical for all firers. Units firing from different hexes or with different ⬡h have different falloff terms — their effective rFP must be computed per unit before summing (Rule 8.3.2).

**8.3.7**  Example (mixed intervals): a ⬡4 -2 unit (rFP 7) and two ⬡5 -1 units (rFP 5 each) fire at a target 6 hexes away. Per unit: 7 − 2×floor(5/4) = 5; each 5 − 1×floor(5/5) = 4. Summed effective rFP = 5 + 4 + 4 = 13 → Resolution Strip.

8.4  Resolution Strip
---------------------


**8.4.1**  When a single unit fires, use its effective rFP directly as the Resolution FP. No strip lookup is required regardless of the rFP value.

**8.4.2**  When multiple units are combined into a fire group (Rule 8.3), always consult the Resolution Strip to determine the Resolution FP. The strip applies logarithmic compression to concentrated fire, reflecting diminishing returns from massed volume. This ensures that dice remain meaningful at all firepower levels.

**8.4.3**  The Resolution Strip is printed on the player aid card for quick reference. Summed values between listed entries round down to the nearest listed row (a summed effective rFP of 11 uses the row for 10, Resolution FP 8). The strip is the identity up to 7 — compression only begins where massed fire does.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Summed Effective rFP**
     - **Resolution FP**
   * - 1
     - 1
   * - 2
     - 2
   * - 3
     - 3
   * - 4
     - 4
   * - 5
     - 5
   * - 6
     - 6
   * - 7
     - 7
   * - 8
     - 7
   * - 9
     - 8
   * - 10
     - 8
   * - 12
     - 9
   * - 15
     - 9
   * - 18
     - 10
   * - 24
     - 11
   * - 30
     - 11
   * - 40
     - 12
   * - 50+
     - 12 (maximum)


8.5  Dice and Roll Procedure
----------------------------


**8.5.1**  With Deepest Regret... uses three dice for all fire combat resolution: 1d6, 1d8, and 1d12.

**8.5.2**  Roll all three dice simultaneously and sum the results. Add Resolution FP to the sum.

**8.5.3**  The three-dice combination produces a symmetric distribution (range 3–26, mean 14.5, std dev 4.48). The right-skewed shape of real combat outcomes — most fire suppresses, casualties are fewer, elimination is rare — emerges from the modifier system rather than the dice: range falloff, cover, intervening terrain, and status penalties weight the majority of fire events toward low margins, while rare close-range engagements against exposed targets supply the tail.

**8.5.4**  Subtract the target's Defence value and applicable cover modifier from the combat total. The result is the margin.

8.6  Result Thresholds
----------------------


.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Margin**
     - **Result**
   * - Below 0
     - No effect
   * - 0 to 8
     - Suppressed
   * - 9 to 13
     - Pinned
   * - 14 to 18
     - Casualty
   * - 19 to 22
     - Casualty + Suppressed
   * - 23+
     - Broken (Combat Ineffective)


8.7  Long Range Cap
-------------------


**8.7.1**  When the effective rFP after all modifiers (falloff, intervening terrain, other penalties) is 3 or less, the maximum possible result is Pinned regardless of the dice roll margin.

**8.7.2**  This represents the physical reality that long-range harassing fire suppresses and occasionally pins but rarely causes casualties.

**8.7.3**  The long range cap applies after all modifiers have been calculated. A unit with effective rFP 4 or higher is not subject to the cap.

**8.7.4**  Sniper exemption:  Sniper fire lines (weapon class icon ╌○) are exempt from the long range cap when deliberate targeting is declared (see Rule 20.2). Full result thresholds apply regardless of effective rFP. A sniper firing without declaring a deliberate target is treated as normal area fire and the cap applies normally.

    *See also: Rule 20.2 (Sniper Deliberate Targeting)*

*NOTE: The long range cap was designed for volume fire — many weapons degraded to marginal effectiveness at extreme range. A sniper fires one precise round. The physical phenomenon being modelled is different: a sniper at 500 yards can kill; a rifle squad at 500 yards mostly suppresses. The exemption distinguishes precision fire from volume fire.*

8.8  Multiple Attacks Against Same Target
-----------------------------------------


**8.8.1**  Fire directed at the same target in the same impulse that cannot form one fire group resolves as separate attacks. This occurs only when the attacks come through different resolution paths: a declared Fire action plus reaction fire (opportunity or defensive fire) resolving in the same window, a sniper's deliberate-targeting shot (Rule 20.2, which never groups), or fire from separate fire actions in the same impulse (e.g. an Interrupt). Units contributing to the same Fire action always group (Rule 8.3.1).

**8.8.2**  After all attacks are resolved, combine the results as follows: take the highest single result; each additional attack whose **own result is Pinned or better** steps the combined result up once, to a **maximum of two step-ups** regardless of the number of attacks.

**8.8.3**  Result step order: Suppressed → Pinned → Casualty → Casualty+Suppressed → Broken.

**8.8.4**  An additional attack whose own result is No Effect or Suppressed adds no step-up.

**8.8.5**  The combined result may never exceed the most severe result any single contributing attack was itself permitted to inflict. In particular, if every contributing attack was subject to the Long Range Cap (Rule 8.7), the combined result remains capped at Pinned — step-ups cannot manufacture casualties that no individual attack could cause.

    *See also: Rule 8.7 (Long Range Cap).*

8.9  Adjacent Fire Bonus
------------------------


**8.9.1**  Fire at range 1 (adjacent hex) receives a +2 bonus to effective rFP (applied before any Resolution Strip lookup, for grouped fire).

**8.9.2**  Fire at range 0 (same hex, close assault entry fire) receives a +3 bonus to effective rFP. See Section 9 for close assault procedure.

**8.9.3**  These bonuses represent the dramatically increased effectiveness of close-range fire.

8.10  Firing Exposed
--------------------


**8.10.1**  See Section 6.6 for the full Firing Exposed rules and trigger conditions.

**8.10.2**  Summary: Move and fire (ASSAULT) = Exposed. Second or later fire this turn while in open ground = Firing Exposed. First fire from any position = not Exposed.

**8.10.3**  Exposed units may be targeted by opportunity fire at 1 RP cost. Firing Exposed units impose -1 rFP on the attacker. Moving units impose -2 rFP on the attacker.
