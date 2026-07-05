Section 8 — Fire Combat
=======================

8.1  Fire Resolution Overview
-----------------------------


Fire combat in With Deepest Regret... uses a single unified resolution procedure for all ranged fire. The procedure calculates effective firepower at range, optionally looks up a Resolution FP value, then resolves with a dice roll against the target's defence.

The full procedure for any fire combat action:

**8.1.1**  Group all firing units by ⬡h interval value.

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

8.3  Grouping by Interval
-------------------------


**8.3.1**  When multiple units fire at the same target in the same impulse, units sharing the same ⬡h interval value may be combined into a single fire group.

**8.3.2**  To form a fire group: each unit first calculates its own effective rFP (falloff at its own range per Rule 8.2, plus its own intervening terrain and modifiers). Sum the effective rFP values. The group is resolved as a single attack using the summed value.

**8.3.3**  Same-hex shortcut: when every unit in the group occupies the same hex, all firers share an identical range and line of sight. The group may instead sum rFP values and f values first — expressed as (total rFP) ⬡h −(total f) — and apply the falloff formula once to the summed values. This produces a result identical to the per-unit calculation (Rule 8.3.6).

**8.3.4**  Units with different ⬡h intervals cannot be combined. Each interval group fires separately and is resolved separately.

**8.3.5**  Example (same-hex shortcut): Three units in the same hex with fire lines 6 ⬡4 -1, 8 ⬡4 -1, and 5 ⬡4 -1 form a group: 19 ⬡4 -3. At range 5, effective rFP = 19 − (3 × floor(4/4)) = 19 − 3 = 16.

**8.3.6**  Mathematical proof of the shortcut: for units sharing a hex, the falloff term floor(max(0, range − 1) / h) is identical for every firer — it depends only on range and h. It therefore distributes across the sum: Σ(rFPᵢ − fᵢ × k) = ΣrFPᵢ − (Σfᵢ) × k. The equivalence holds at all ranges, but only when range and intervening terrain are identical for all firers. Units firing from different hexes have different ranges and different sight lines — their effective rFP must be computed per unit before summing (Rule 8.3.2).

8.4  Resolution Strip
---------------------


**8.4.1**  When a single unit fires, use its effective rFP directly as the Resolution FP. No strip lookup is required regardless of the rFP value.

**8.4.2**  When multiple units are combined into a fire group (Rule 8.3), always consult the Resolution Strip to determine the Resolution FP. The strip applies logarithmic compression to concentrated fire, reflecting diminishing returns from massed volume. This ensures that dice remain meaningful at all firepower levels.

**8.4.3**  The Resolution Strip is printed on the player aid card for quick reference.

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
     - 4
   * - 4
     - 5
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


**8.8.1**  When two or more separate fire groups attack the same target hex in the same impulse (different ⬡h intervals, or units firing from different hexes that cannot be grouped), resolve each attack separately.

**8.8.2**  After all attacks are resolved, combine the results as follows: take the highest single result; for each additional attack that beats the target's defence, step the result up once on the result track.

**8.8.3**  Result step order: Suppressed → Pinned → Casualty → Casualty+Suppressed → Broken.

**8.8.4**  An additional attack that does not beat the target's defence adds no step-up even if the primary attack produced a result.

8.9  Adjacent Fire Bonus
------------------------


**8.9.1**  Fire at range 1 (adjacent hex) receives a +2 bonus to effective rFP before the Resolution Strip lookup.

**8.9.2**  Fire at range 0 (same hex, close assault entry fire) receives a +3 bonus to effective rFP. See Section 9 for close assault procedure.

**8.9.3**  These bonuses represent the dramatically increased effectiveness of close-range fire.

8.10  Firing Exposed
--------------------


**8.10.1**  See Section 6.6 for the full Firing Exposed rules and trigger conditions.

**8.10.2**  Summary: Move and fire (ASSAULT) = Exposed. Second fire from open ground same position = Firing Exposed. First fire from any position = not Exposed.

**8.10.3**  Exposed units may be targeted by opportunity fire at 1 RP cost. Firing Exposed units impose -1 rFP on the attacker. Moving units impose -2 rFP on the attacker.
