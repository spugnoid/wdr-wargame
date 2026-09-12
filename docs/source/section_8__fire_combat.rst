Section 8 — Fire Combat
=======================

8.1  Fire Resolution Overview
-----------------------------


Fire combat in With Deepest Regret... uses a single unified resolution procedure for all ranged fire. The procedure calculates effective firepower at range, optionally looks up a Resolution FP value, then resolves with a dice roll against the target's defence.

The full procedure for any fire combat action:

**8.1.1**  All units firing at the same target as part of one Fire action form a single fire group, regardless of ⬡h interval (Rule 8.3).

.. container:: rule-guide

   **Why:** Defines "fire group" membership by the one Fire action, not by target or range proximity — this is the anchor definition that Rule 8.3's grouping mechanics build on.

   **Example:** If Alpha and a second unit both declare Fire at Bravo as part of the same Fire action, they form one fire group; if Alpha fires now and the second unit fires as a separate action later in the same impulse (e.g. via Interrupt), they don't group (see 8.8.1).

**8.1.1a**  A unit with multiple fire lines fires **all** of them in one Fire action: each line computes its own effective rFP at the target's range (Rule 8.2) and the values join the fire group's sum like separate firers. A single fire action never splits a unit's lines across different targets. Exception: a sniper's deliberate-targeting shot (Rule 20.2) uses the sniper line alone and never groups.

.. container:: rule-guide

   **Why:** Keeps a multi-line unit's full firepower in play for a single Fire action rather than forcing an artificial choice between its lines, while still preventing that same action from being split across multiple targets.

   **Example:** A unit with two printed fire lines computes both lines' effective rFP at the same target's range and adds both into the fire group's total — it cannot fire one line at Bravo and the other at a different enemy unit in the same action.

**8.1.2**  For each firing unit, calculate the effective rFP at that unit's own firing range (Rule 8.2).

.. container:: rule-guide

   **Why:** Makes range-based falloff the very first calculation in the whole procedure, since every later step — grouping, the dice roll, the margin — depends on having each unit's own effective rFP already in hand.

   **Example:** Before Alpha's fire can be summed with anyone else's or compared to Bravo's Defence, Alpha's own effective rFP at its actual firing range must be calculated first (Rule 8.2).

**8.1.3**  Apply intervening terrain penalties and any other modifiers (elevation, exposure status, etc.) to each unit's effective rFP individually — each firer uses its own range and its own line of sight.

.. container:: rule-guide

   **Why:** Keeps every firer's terrain and status penalties individual to that firer's own line of sight and position, since two units in a group can easily be looking at the target through different terrain even while firing at the same hex.

   **Example:** Alpha fires through a hedgerow that a second friendly unit in the same group doesn't have in its own line of sight. Alpha's intervening-terrain penalty applies only to Alpha's effective rFP, not to the group's total as a flat deduction.

**8.1.4**  Sum the effective rFP values within each group. Units occupying the same hex may use the sum-first shortcut instead (Rule 8.3.3).

.. container:: rule-guide

   **Why:** Is the moment a fire group actually becomes one number rather than several — everything before this step is per-unit, everything after is group-level.

   **Example:** Two units contribute effective rFP of 5 and 4 to the same fire group. Their sum, 9, is what proceeds to the Resolution Strip (Rule 8.4) as one combined attack.

**8.1.5**  If a single unit fires, use effective rFP directly as Resolution FP. If multiple units in a group fire, consult the Resolution Strip (Rule 8.4) to find the Resolution FP.

.. container:: rule-guide

   **Why:** Draws the line between "small enough to read directly" and "needs the compression table" at exactly one firer — a lone attacker's own effective rFP already accounts for everything relevant, with nothing left to compress.

   **Example:** Alpha fires alone. Its effective rFP (say, 5) is used directly as Resolution FP — no Resolution Strip lookup is needed since there's only one contributor.

**8.1.6**  Roll 1d6 + 1d8 + 1d12. Add Resolution FP to the roll.

.. container:: rule-guide

   **Why:** Fixes the dice pool as constant across every fire attack in the game, so variability always comes from the same source regardless of weapon type, range, or grouping.

   **Example:** Whether Alpha fires alone or as part of a ten-unit fire group, the same three dice are rolled and the same Resolution FP is added — only the size of that addition changes.

**8.1.7**  Subtract the target's Defence value plus applicable cover modifier.

.. container:: rule-guide

   **Why:** Subtracts the target's own defensive stats at the very end, after the attacker's side of the equation is fully resolved, keeping attacker-side and defender-side modifiers cleanly separated in the calculation order.

   **Example:** A combat total of 18 (dice + Resolution FP) against a target with Defence 5 in cover +3 produces a margin of 18 − 5 − 3 = 10.

**8.1.8**  The result is the margin. Consult the Result Threshold Table (Rule 8.6 / Appendix C) to determine the result.

.. container:: rule-guide

   **Why:** Closes the loop by handing the final margin to a single shared lookup table rather than a bespoke result scale for each weapon or situation.

   **Example:** A margin of 10 from the previous example reads as Pinned (9–13 band) on the Result Threshold Table — the same table every other fire attack in the game consults.

8.2  Falloff Calculation
------------------------


**8.2.1**  Effective rFP at a given range is calculated as follows:

.. container:: rule-guide

   **Why:** Gives falloff a single formula rather than a per-weapon lookup table, so any fire line's effective rFP at any range can be computed the same way from three printed numbers.

   **Example:** See the worked calculation in 8.2.4 just below — the same formula applies to every fire line in the game.

**Effective rFP = rFP − (f × floor(max(0, range − 1) / h))**

**8.2.2**  Where rFP is the base firepower value, f is the falloff loss value (printed as -f on the counter), h is the hex interval (printed inside the ⬡ symbol), and range is the distance in hexes from firer to target.

.. container:: rule-guide

   **Why:** Names each symbol printed on a fire line so the formula in 8.2.1 has a concrete referent for each of its terms.

   **Example:** A fire line printed as "7 ⬡4 -1" has rFP=7, h=4, f=1 — the three values 8.2.1's formula actually uses.

**8.2.3**  Range 0 (same hex) and range 1 (adjacent hex) both use the full rFP value with no falloff reduction.

.. container:: rule-guide

   **Why:** Gives close ranges a flat floor rather than letting the formula's own math produce a falloff step at range 1 that wouldn't match "still basically point-blank."

   **Example:** A fire line's effective rFP at range 1 equals its full printed rFP, identical to firing at range 0 — falloff only begins to bite from range 2 onward.

**8.2.4**  Example: A fire line reading 7 ⬡4 -1 at range 9 hexes. Effective rFP = 7 − (1 × floor(8 / 4)) = 7 − 2 = 5.

.. container:: rule-guide

   **Why:** Works the falloff formula through one concrete case, so a reader can check their own arithmetic against a known-correct result before relying on the formula elsewhere.

   **Example:** As printed: a fire line reading 7 ⬡4 -1 at range 9 gives effective rFP = 7 − (1 × floor(8/4)) = 7 − 2 = 5.

**8.2.5**  A fire line whose effective rFP after **all** modifiers (falloff, intervening terrain, smoke, status and exposure penalties) is 0 or less contributes nothing: it adds nothing to a fire group's sum, and if no line in the group has a positive effective rFP, no attack occurs and no FIRE marker is placed. Effective rFP never goes below 0 for any purpose — a deeply degraded line cannot drag a group's total down.

.. container:: rule-guide

   **Why:** Gives a fully-degraded fire line a clean floor of zero contribution rather than letting it go negative and drag a group's total down — a badly-out-of-range weapon simply contributes nothing, it doesn't actively hurt its own side's fire group.

   **Example:** A fire line reduced to an effective rFP of -1 after every modifier is applied instead contributes exactly 0 to its fire group's sum — not -1.

8.3  Grouping by Interval
-------------------------


**8.3.1**  When multiple units fire at the same target in the same impulse as part of one Fire action, they combine into a single fire group. Grouping is not optional and has no ⬡h restriction: the per-unit method of Rule 8.3.2 is well-defined for any mix of fire lines, because each unit's falloff is computed on its own printed curve before the values are summed.

.. container:: rule-guide

   **Why:** Makes grouping mandatory and interval-independent, closing off any temptation to treat units with mismatched ⬡h values as ineligible to combine — the per-unit method (8.3.2) works for any mix precisely because each unit's own falloff curve is computed before summing.

   **Example:** A ⬡4 unit and a ⬡6 unit firing at the same target in the same Fire action must group — there's no rule permitting them to resolve as two separate attacks just because their falloff intervals differ.

    *See also: Rule 8.8 (attacks that cannot group — reaction fire, sniper deliberate targeting, separate fire actions).*

**8.3.2**  To form a fire group: each unit first calculates its own effective rFP (falloff at its own range per Rule 8.2, plus its own intervening terrain and modifiers). Sum the effective rFP values. The group is resolved as a single attack using the summed value.

.. container:: rule-guide

   **Why:** Is the general-case procedure every fire group ultimately reduces to — compute each unit's own effective rFP first, then sum — with the same-hex shortcut (8.3.3) as a pure convenience for a common special case, never a separate calculation.

   **Example:** See 8.3.7's worked mixed-interval example, which applies exactly this per-unit-then-sum method.

**8.3.3**  Same-hex shortcut: when every unit in the group occupies the same hex **and shares the same ⬡h interval**, all firers share an identical range, line of sight, and falloff step. The group may instead sum rFP values and f values first — expressed as (total rFP) ⬡h −(total f) — and apply the falloff formula once to the summed values. This produces a result identical to the per-unit calculation (Rule 8.3.6). Mixed-⬡h groups simply use the per-unit method of Rule 8.3.2; the shortcut is a convenience, never a requirement.

.. container:: rule-guide

   **Why:** Only applies when every firer genuinely shares the same range, LOS, and falloff step — summing rFP and f values first is a shortcut specifically because, in that narrow case, it's mathematically guaranteed to produce the same answer as computing each unit separately (proven in 8.3.6).

   **Example:** See 8.3.5's worked example — three same-hex, same-⬡h units combine their rFP and f values before applying falloff once, rather than computing three separate falloff calculations.

**8.3.5**  Example (same-hex shortcut): Three units in the same hex with fire lines 6 ⬡4 -1, 8 ⬡4 -1, and 5 ⬡4 -1 form a group: 19 ⬡4 -3. At range 5, effective rFP = 19 − (3 × floor(4/4)) = 19 − 3 = 16.

.. container:: rule-guide

   **Why:** Works the same-hex shortcut through a concrete three-unit case, mirroring 8.2.4's single-unit worked example but for the grouped, shortcut-eligible scenario.

   **Example:** As printed: three same-hex units (6 ⬡4 -1, 8 ⬡4 -1, 5 ⬡4 -1) combine to 19 ⬡4 -3. At range 5: effective rFP = 19 − (3 × floor(4/4)) = 16.

**8.3.6**  Mathematical proof of the shortcut: for units sharing a hex, the falloff term floor(max(0, range − 1) / h) is identical for every firer — it depends only on range and h. It therefore distributes across the sum: Σ(rFPᵢ − fᵢ × k) = ΣrFPᵢ − (Σfᵢ) × k. The equivalence holds at all ranges, but only when range, ⬡h, and intervening terrain are identical for all firers. Units firing from different hexes or with different ⬡h have different falloff terms — their effective rFP must be computed per unit before summing (Rule 8.3.2).

.. container:: rule-guide

   **Why:** Proves the shortcut is exact, not an approximation, for the specific case it applies to — a reader doesn't have to take 8.3.3's claim on faith, and the proof also states precisely why the shortcut breaks for mixed hexes or mixed ⬡h (the falloff term is no longer identical across firers).

   **Example:** The algebra shows Σ(rFPᵢ − fᵢ×k) = ΣrFPᵢ − (Σfᵢ)×k whenever k (the falloff step) is the same for every firer — which is only guaranteed when range, ⬡h, and terrain all match.

**8.3.7**  Example (mixed intervals): a ⬡4 -2 unit (rFP 7) and two ⬡5 -1 units (rFP 5 each) fire at a target 6 hexes away. Per unit: 7 − 2×floor(5/4) = 5; each 5 − 1×floor(5/5) = 4. Summed effective rFP = 5 + 4 + 4 = 13 → Resolution Strip.

.. container:: rule-guide

   **Why:** Works a mixed-interval case, where the shortcut of 8.3.3 does not apply, to show the fallback per-unit method in practice — directly contrasting with 8.3.5's same-hex shortcut example.

   **Example:** As printed: a ⬡4 -2 unit (rFP 7) and two ⬡5 -1 units (rFP 5 each) at range 6: 7−2×floor(5/4)=5; each 5−1×floor(5/5)=4. Summed: 5+4+4=13, which then goes to the Resolution Strip.

8.4  Resolution Strip
---------------------


**8.4.1**  When a single unit fires, use its effective rFP directly as the Resolution FP. No strip lookup is required regardless of the rFP value.

.. container:: rule-guide

   **Why:** Reconfirms, from the Resolution Strip's own section, the same single-firer exemption already stated in 8.1.5 — a lone attacker's effective rFP needs no compression because there's nothing yet to compress.

   **Example:** Alpha, firing alone, uses its effective rFP of 6 directly as Resolution FP — no strip lookup, regardless of how high that 6 might otherwise look on the table.

**8.4.2**  When multiple units are combined into a fire group (Rule 8.3), always consult the Resolution Strip to determine the Resolution FP. The strip applies logarithmic compression to concentrated fire, reflecting diminishing returns from massed volume. This ensures that dice remain meaningful at all firepower levels.

.. container:: rule-guide

   **Why:** Applies compression specifically, and only, to grouped fire, reflecting that massed fire has diminishing returns — ten rifles firing together don't inflict ten times the harm of one, and the strip's logarithmic shape is what keeps the dice roll meaningful even at very high summed rFP.

   **Example:** A fire group's summed effective rFP of 24 doesn't add 24 to the dice roll — it converts to Resolution FP 11 via the strip, reflecting the diminishing marginal value of each additional rifle in the group.

**8.4.3**  The Resolution Strip is printed on the player aid card for quick reference. Summed values between listed entries round down to the nearest listed row (a summed effective rFP of 11 uses the row for 10, Resolution FP 8). The strip is the identity up to 7 — compression only begins where massed fire does.

.. container:: rule-guide

   **Why:** Gives the strip a simple, memorizable rounding rule — round down to the nearest listed row — so players don't need to interpolate between printed values during play, and confirms the strip does nothing at all below 8: compression starts exactly where grouped fire starts mattering.

   **Example:** A fire group with a summed effective rFP of 11 (not itself a printed row) uses the row for 10, giving Resolution FP 8 — the same value a group summing to exactly 10 would use.

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

.. container:: rule-guide

   **Why:** Fixes the exact dice pool used everywhere in the game, so "roll for fire combat" always means the same physical dice regardless of context.

   **Example:** Every fire attack in the game — Regular Fire, Assault Fire, reaction fire, close assault fire — rolls the same 1d6, 1d8, and 1d12.

**8.5.2**  Roll all three dice simultaneously and sum the results. Add Resolution FP to the sum.

.. container:: rule-guide

   **Why:** Keeps the roll-and-add sequence simple and identical every time — sum the dice first, then add the single Resolution FP number already computed by the earlier steps.

   **Example:** A roll of 1d6=3, 1d8=5, 1d12=7 sums to 15; adding a Resolution FP of 8 gives a combat total of 23, before Defence and cover are subtracted.

**8.5.3**  The three-dice combination produces a symmetric distribution (range 3–26, mean 14.5, std dev 4.48). The right-skewed shape of real combat outcomes — most fire suppresses, casualties are fewer, elimination is rare — emerges from the modifier system rather than the dice: range falloff, cover, intervening terrain, and status penalties weight the majority of fire events toward low margins, while rare close-range engagements against exposed targets supply the tail.

.. container:: rule-guide

   **Why:** Explains where the game's real-world-accurate outcome shape — mostly suppression, casualties rarer, elimination rare — actually comes from: not from a skewed die, but from the modifiers doing the work of weighting most fire events toward low margins.

   **Example:** The three-dice sum itself is symmetric around 14.5; it's the systematic subtraction of Defence, cover, and falloff-reduced Resolution FP that pushes the majority of actual combat margins down into the Suppressed band, not any asymmetry in the dice themselves.

**8.5.3a**  There is no "miss" at effective range, by design: because the minimum roll is 3, any attack at a net modifier of −3 or better always produces at least Suppressed. Aimed fire at combat ranges reliably makes the target's men put their heads down — the dice decide only how much worse than that it gets. This is the system's core identity: **fire suppresses, manoeuvre kills.** Whiffed attacks live at long range, in deep cover, and through smoke (where the net modifier drops below −3 and the No Effect band opens); at effective range, the meaningful question is never "did I hit?" but "can they still act?", and the suppression-and-recovery cycle (Rules 5.2, 10.2) is the engine the whole game runs on.

.. container:: rule-guide

   **Why:** States outright, as a deliberate design identity rather than an accident, that effective-range fire essentially never misses — the game's tension comes from how badly a hit lands and whether the target can still function, not from a coin-flip on whether it connects at all.

   **Example:** An attack at net modifier −3 (the borderline case) still guarantees at least a Suppressed result, since the dice pool's minimum roll is 3. True misses (No Effect) only show up at long range, in deep cover, or through smoke, where the net modifier has dropped below that threshold.

**8.5.4**  Subtract the target's Defence value and applicable cover modifier from the combat total. The result is the margin.

.. container:: rule-guide

   **Why:** Is the actual point at which attacker and defender numbers finally meet — everything before this step built up the attacker's total, and this step is where the defender's own stats get to push back.

   **Example:** A combat total of 20, against a target with Defence 6 and a cover modifier of +2, yields a margin of 20 − 6 − 2 = 12.

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


**8.7.1**  When the effective rFP after all modifiers (falloff, intervening terrain, other penalties) is low, the maximum possible result is capped regardless of the dice roll margin:

.. container:: rule-guide

   **Why:** Caps outcomes at low effective rFP regardless of how lucky the dice roll runs, since a genuinely weak, far-away shot shouldn't be able to produce a Broken result purely off an exceptional roll.

   **Example:** A fire line reduced to effective rFP 2 after falloff can, at best, inflict Suppressed this attack — even a maximum dice roll cannot push the result past that cap.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Effective rFP**
     - **Maximum result**
   * - 1–2
     - Suppressed
   * - 3
     - Pinned
   * - 4+
     - Uncapped


**8.7.2**  This represents the physical reality that long-range harassing fire suppresses and occasionally pins but rarely causes casualties.

.. container:: rule-guide

   **Why:** States the real-world logic behind the cap in plain terms — harassing fire at extreme range keeps heads down but rarely causes actual casualties, which is exactly the behavior the cap enforces mechanically.

   **Example:** A rifle squad exchanging fire at the edge of its weapons' range can pin an enemy repeatedly but essentially never inflicts a Casualty result on them, matching historical long-range engagement outcomes.

**8.7.3**  The long range cap applies after all modifiers have been calculated. The two-band grading removes the old cliff at rFP 3/4, where a single point of intervening penalty toggled a firer between "can never inflict a casualty" and the full table including Broken.

.. container:: rule-guide

   **Why:** Smooths what used to be an abrupt, unrealistic threshold — one point of extra intervening-terrain penalty shouldn't be the difference between "can never hurt them" and "can potentially wipe them out" — into a graduated two-step cap instead.

   **Example:** A fire line at effective rFP 3 (Pinned cap) and one at effective rFP 4 (uncapped) are adjacent points on a smooth two-step scale, rather than the old system's single sharp cliff between "no casualties ever" and "full table available."

**8.7.4**  Sniper exemption:  Sniper fire lines (weapon class icon ╌○) are exempt from the long range cap when deliberate targeting is declared (see Rule 20.2). Full result thresholds apply regardless of effective rFP. A sniper firing without declaring a deliberate target is treated as normal area fire and the cap applies normally.

.. container:: rule-guide

   **Why:** Exempts precision fire — a sniper's single aimed round — from a cap designed for volume fire. The physical phenomena are genuinely different, and folding them into the same cap would understate what a well-aimed single shot can do at range.

   **Example:** A sniper's effective rFP might read low enough to trigger the ordinary long-range cap, but if the shot is declared as deliberate targeting (Rule 20.2), the full Result Threshold Table applies regardless — that same sniper firing without declaring a target is capped like ordinary area fire.

    *See also: Rule 20.2 (Sniper Deliberate Targeting)*

*NOTE: The long range cap was designed for volume fire — many weapons degraded to marginal effectiveness at extreme range. A sniper fires one precise round. The physical phenomenon being modelled is different: a sniper at 500 yards can kill; a rifle squad at 500 yards mostly suppresses. The exemption distinguishes precision fire from volume fire.*

8.8  Multiple Attacks Against Same Target
-----------------------------------------


**8.8.1**  Fire directed at the same target in the same impulse that cannot form one fire group resolves as separate attacks. This occurs only when the attacks come through different resolution paths: a declared Fire action plus reaction fire (opportunity or defensive fire) resolving in the same window, a sniper's deliberate-targeting shot (Rule 20.2, which never groups), or fire from separate fire actions in the same impulse (e.g. an Interrupt). Units contributing to the same Fire action always group (Rule 8.3.1).

.. container:: rule-guide

   **Why:** Names the narrow, specific circumstances under which the same target can be hit by more than one separately-resolved attack in one impulse — anything contributing to the same Fire action always groups (8.3.1), so this rule only ever applies across genuinely distinct resolution paths.

   **Example:** Alpha declares a Fire action at Bravo. During the same window, a second friendly unit lands a Defensive Fire reaction against Bravo too, because Bravo had itself just declared Close Assault. These two attacks resolve separately and then combine per 8.8.2, rather than merging into one fire group.

**8.8.2**  After all attacks are resolved, combine the results as follows: take the highest single result; each additional attack whose **own result is Pinned or better** steps the combined result up once, to a **maximum of two step-ups** regardless of the number of attacks.

.. container:: rule-guide

   **Why:** Caps how much multiple separate attacks can compound each other's severity — the highest single result sets the baseline, and each additional qualifying attack nudges it up by one step at most twice, rather than letting an unlimited pile-on of small attacks add up to an automatic Broken result.

   **Example:** Three separate attacks against Bravo in the same impulse produce Pinned, Casualty, and Suppressed individually. The highest (Casualty) is the baseline; the Pinned result qualifies as a step-up (its own result was Pinned or better), pushing the combined result to Casualty+Suppressed. The Suppressed-only attack does not qualify as a step-up (8.8.4).

**8.8.3**  Result step order: Suppressed → Pinned → Casualty → Casualty+Suppressed → Broken.

.. container:: rule-guide

   **Why:** Gives the step-up mechanic (8.8.2) a fixed ladder to climb, using the exact same five-rung order as the main Result Threshold Table, so "one step up" always means the same thing regardless of which two results are involved.

   **Example:** Stepping up from a Pinned baseline moves the combined result to Casualty; stepping up twice from Pinned reaches Casualty+Suppressed.

**8.8.4**  An additional attack whose own result is No Effect or Suppressed adds no step-up.

.. container:: rule-guide

   **Why:** Sets a real bar for what counts as a qualifying step-up attack — an attack that itself barely mattered (No Effect or just Suppressed) shouldn't be able to escalate a more serious result any further.

   **Example:** A weak reaction-fire attack that only manages Suppressed on its own does not add a step-up to a combined result, even though a Fire action against the same target in the same impulse achieved Casualty.

**8.8.5**  The combined result may never exceed the most severe result any single contributing attack was itself permitted to inflict. In particular, if every contributing attack was capped (Rule 8.7), the combined result remains capped at the **highest** cap among them — step-ups cannot manufacture casualties that no individual attack could cause.

.. container:: rule-guide

   **Why:** Closes off the possibility of manufacturing a result no single contributing attack could ever have produced on its own — step-ups escalate severity within what was already possible, they don't create new possibility.

   **Example:** If every attack against Bravo this impulse was long-range-capped at Pinned (Rule 8.7), the combined result cannot exceed Pinned even after step-ups — there's no path to Casualty or worse when nothing contributing to the pile-on could individually inflict it.

    *See also: Rule 8.7 (Long Range Cap).*

8.9  Adjacent Fire Bonus
------------------------


**8.9.1**  Fire at range 1 (adjacent hex) receives a +2 bonus to effective rFP (applied before any Resolution Strip lookup, for grouped fire).

.. container:: rule-guide

   **Why:** Rewards genuinely close engagement with a real, unconditional bonus rather than letting range-1 fire be treated the same as any other in-range shot — adjacency is dramatically more lethal than standing off even slightly.

   **Example:** A fire line at range 1 gets +2 effective rFP before that value joins a fire group's sum or goes to the Resolution Strip — the bonus applies before any compression, not after.

**8.9.2**  Fire at range 0 (same hex, close assault entry fire) receives a +3 bonus to effective rFP. See Section 9 for close assault procedure.

.. container:: rule-guide

   **Why:** Gives point-blank fire — same hex, specifically close assault's Entry Fire and Melee Continuation phases — an even larger bonus than merely-adjacent fire, matching the greater lethality of a fight happening in the exact same space.

   **Example:** Fire resolved during close assault's Entry Fire Phase (Section 9), at range 0, gets +3 effective rFP — one point more than the range-1 adjacent bonus.

**8.9.3**  These bonuses represent the dramatically increased effectiveness of close-range fire.

.. container:: rule-guide

   **Why:** States the real-world rationale in one line — close-range fire is disproportionately more effective, and the two bonuses (adjacent, same-hex) are this game's way of expressing that without inventing a separate resolution system just for close combat.

   **Example:** The same Result Threshold Table and dice procedure govern both a long-range duel and a point-blank exchange — only the size of the range bonus folded into effective rFP before resolution differs.

8.10  Assault and Reaction Fire
---------------------------------


**8.10.1**  Assault Fire (Rule 6.3.3) and reaction fire (Rule 6.2.3) are ordinary fire attacks resolved by this section, at half effective rFP rather than full — nothing else about their resolution differs. A stationary F#-greater-than-1 weapon's reaction (Rule 6.6) is a full-effective-rFP attack instead, exactly like its own Regular Fire.

.. container:: rule-guide

   **Why:** Confirms that Assault Fire and reaction fire are not special resolution systems of their own — they're ordinary fire attacks under this whole section, just computed at half effective rFP, so nothing about grouping, the Resolution Strip, or the dice procedure needs a separate version for them.

   **Example:** An Assault Fire at half effective rFP still goes through falloff calculation, potential grouping, the Resolution Strip if grouped, and the same three-dice roll — only the rFP value feeding into all of that is halved going in.

**8.10.2**  A moving unit's own fire is unaffected by this rule — it is the attacker in that exchange, not the target. The -2 rFP penalty for firing *at* a moving target is Rule 7.5.2.

.. container:: rule-guide

   **Why:** Clarifies a scope boundary so this rule — about a unit's own reduced-effect fire — isn't confused with the different, defender-side moving-target penalty in Rule 7.5.2: one concerns the firer's own economy, the other concerns firing at a target that happens to be moving.

8.11  Reduced-Visibility Fire Eligibility
--------------------------------------------


**8.11.1**  A unit may not declare fire combat against a target beyond the active visibility cap — night's (Rule 23.1) or a declared Weather condition's (Rules 24.2.1, 24.3.1, 24.4.1) — unless the target's hex is lit (Rule 23.2). Where more than one cap is active (Rule 24.1.2), the most restrictive governs. This is a flat eligibility gate, independent of the Long Range Cap (Rule 8.7) — that rule still does its own separate job of capping *results* for weak effective rFP once a target is in range; this rule is about whether the attack may be declared at all.

.. container:: rule-guide

   **Why:** Keeps two genuinely different questions separate — whether a target can be engaged at all given how far the battlefield can currently be seen, and, once it can, how weak fire at long range is allowed to resolve — rather than folding a detection limit into a rule that was built to cap combat outcomes. Stated once, generically, rather than as a separate near-identical rule per condition, since night, fog, and precipitation all create the same kind of eligibility gate and differ only in their printed hex number.

   **Example:** Under Fog (1-hex cap), a unit may not declare fire at an unlit target 2 hexes away — the same flat prohibition Night's 2-hex cap would apply at a longer range. The same target inside a starshell's light radius (Rule 23.3) is a legal target, subject to the ordinary rules (including 8.7) exactly as it would be at any range in daylight — illumination cancels night, but not a Weather cap (Rule 24.1.2).

    *See also: Rule 23.1 (Ambient Visibility), Rule 24.1 (Weather — General), Rule 23.2 (Illumination), Rule 8.7 (Long Range Cap — a separate, still-applicable rule).*

8.12  Weapon Malfunction (Optional Rule)
--------------------------------------------

*If this module is in use for the scenario:*

*Design note: automatic weapons jamming under sustained fire is one of the most recognisable pieces of tactical-wargame chrome (Advanced Squad Leader's Malfunction result is the best-known example), and a real historical phenomenon — but it adds a check to every single automatic-weapon shot in the game, which is exactly the kind of table overhead the base game deliberately avoids. Scoped as optional for that reason, not because the phenomenon isn't real. See design note E.115.*

**8.12.1**  Whenever a unit fires a weapon with class lmg, hmg, or smg (Rule 6.6.2's mount-type table, or the printed weapon_class on the fire line), check for malfunction using the same 1d6+1d8+1d12 roll already made for the attack: if the 1d6 **and** the 1d8 both show their minimum value (1 and 1), regardless of the 1d12 or the attack's own result, the weapon malfunctions. This reuses the existing roll — no second roll, no new dice.

.. container:: rule-guide

   **Why:** Piggybacks on the dice already being rolled for the attack itself rather than adding a separate malfunction check, keeping the added overhead to "notice one more thing about a roll you were making anyway" instead of a whole extra procedure. The 1-and-1 trigger on two of the three dice gives a modest, ASL-comparable frequency (1/6 × 1/8 = 1/48, about 2.1% of shots) without needing a new die or a lookup table.

   **Example:** A unit fires its LMG and rolls 1d6=1, 1d8=1, 1d12=7. The attack itself resolves normally against the rolled total, but because both the d6 and d8 came up 1, the weapon also malfunctions — both facts are read off the same single roll.

**8.12.2**  The shot that triggers a malfunction still resolves normally against its target — the weapon fires and then jams, not the reverse. Place a MALFUNCTION marker on the counter; that weapon's fire line contributes 0 rFP (as if omitted) to any fire group until repaired.

.. container:: rule-guide

   **Why:** A jam happens as a mechanical consequence of firing, not instead of it — the round already fired is already downrange regardless of what the action does next, matching the real sequence of events a stoppage actually follows.

   **Example:** A unit's LMG line contributes its usual rFP to this attack despite malfunctioning on the same roll; on every subsequent attack until repaired, that same line contributes nothing, exactly as if it had been omitted from the counter.

**8.12.3**  Repair: at the start of a later activation, the unit may spend 1 AP attempting to clear the malfunction instead of moving or firing. Roll 1d6: on 5-6 the MALFUNCTION marker is removed; on 1-4 it remains (retry in a later activation). A weapon that has failed **three** repair attempts in the same scenario is permanently disabled — place an EXPENDED strip (Rule 18.9.1's component) over that weapon band for the rest of the scenario.

.. container:: rule-guide

   **Why:** Gives a malfunction a real in-scenario cost (an AP spent not fighting, for uncertain odds) without making it a permanent loss on the first bad roll, while the three-strikes cap reflects that some stoppages genuinely can't be cleared in the field, matching the same permanence Rule 18.9.1's EXPENDED strip already gives a spent single-shot weapon.

   **Example:** A unit spends 1 AP repairing its jammed HMG and rolls a 3 — still jammed, one failed attempt recorded. If it fails two more attempts across the scenario, the HMG is permanently disabled; only the printed rear-face profile (if any) remains usable for that counter.

*NOTE: this module deliberately does not touch vehicle-mounted weapons (Section 18's own Gunnery Roll and damage tables already have their own, more detailed resolution machinery) — it covers infantry-carried and independently-crewed automatic weapons only.*

8.13  Pre-Registered Defensive Fire (Optional Rule)
--------------------------------------------------------

*If this module is in use for the scenario:*

*Design note: Rule 16.4.1 already lets a mortar pre-designate up to two target hexes for a real accuracy bonus (Registered Target). Direct-fire weapons — an HMG, an AT gun, a defending tank in a prepared position — had no equivalent, even though boresighting a likely approach is exactly the kind of preparation real defenders actually did. Reuses the mortar rule's own registration limit and the Gunnery Roll's own existing band-shortening idiom rather than inventing new numbers. See design note E.115.*

**8.13.1**  During scenario setup, a weapon that will not move for the rest of the scenario (a deployed HMG, an AT gun, or a vehicle the scenario designates as fixed/dug-in) may pre-register up to **2 hexes** within its printed range — the same limit Rule 16.4.1 already sets for mortar Registered Target.

.. container:: rule-guide

   **Why:** Reuses the mortar rule's own limit rather than choosing a new number, since the underlying tactical idea — a small number of pre-ranged spots, not the whole field of fire — is identical whether the weapon lobs a shell indirectly or fires flat.

   **Example:** A dug-in Panzer IV pre-registers the two hexes covering a likely road approach into its position before the scenario begins — no more than two, matching the mortar rule it borrows from.

**8.13.2**  The first shot fired at a target in a pre-registered hex this scenario gains a bonus: an infantry/HMG attack (Section 8) treats the target as one hex closer for falloff purposes; a vehicle or AT gun's attack (Section 18) shortens its Gunnery Table band by one step, exactly as Rule 18.1a.7's follow-up-shot adjustment already does. Only the first shot at that hex gains this — it represents a known distance and aiming point, not a standing accuracy bonus for the rest of the scenario.

.. container:: rule-guide

   **Why:** Reuses Rule 18.1a.7's existing band-shortening mechanic for the vehicle case rather than adding a second way to adjust the Gunnery Table, and scopes the infantry case to the same falloff-shortening idiom already used elsewhere — a pre-ranged shot is mechanically identical to a follow-up shot in everything that matters: the gunner already knows the range.

   **Example:** A pre-registered AT gun's first shot at a tank entering its registered hex reads the Gunnery Table one band shorter than the actual range, exactly as a genuine follow-up shot would — the second shot at that same hex gets no further bonus.

**8.13.3**  Pre-registration is lost — the marker is removed — the instant the weapon moves, exactly as a mortar's Registered Target assumes a fixed firing position throughout.

.. container:: rule-guide

   **Why:** Ties the bonus to the same fixed-position assumption the mortar version already makes, since a weapon that repositions no longer has a genuinely pre-ranged shot at its old registered hex.

   **Example:** An AT gun that limbers and moves to a new position loses both of its pre-registered hexes — reaching that bonus again means registering new hexes from wherever it stops next, if the scenario still allows it.

   **Example:** A unit taking an Assault Move and then firing on its next activation is not itself penalized for having moved earlier — its own fire is judged solely by whether it's a Regular or Assault Fire (this rule). A -2 rFP penalty only applies to whoever is shooting at a currently-moving target (Rule 7.5.2), a completely separate situation.
