Section 16 — Mortars and Smoke
==============================

Mortars are the infantryman's organic artillery — immediately available, no coordination delay, capable of indirect fire over obstacles and onto reverse slopes. Smoke provides concealment for movement across open ground. Together they are the primary tools enabling tactical manoeuvre under fire.

16.1  Mortar Counter Design
---------------------------


Mortar counters display four specialist stats in addition to standard Defence and Morale:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Stat**
     - **Notation**
     - **Description**
   * - Range band
     - RNG ⬡min-max
     - Minimum and maximum range in hexes. Cannot target within minimum range.
   * - Blast radius
     - BLT #
     - Hexes around impact point also affected. BLT 1 = target hex + all 6 adjacent hexes.
   * - Accuracy
     - ACC #
     - Base accuracy value. Roll 1d6 vs ACC — equal or under means round lands on target hex.
   * - Ammunition
     - AMO #
     - Base ammunition per scenario. Secret bonus added at setup. See Rule 16.3.


All mortar counters use M1 F2 (mobile) or M0 F2 (deployed). Mortar teams must deploy before firing — same deploy/limber rules as HMG teams (Section 7.6).

16.2  Representative Mortar Counters — 1943
-------------------------------------------


.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit**
     - **RNG**
     - **BLT**
     - **ACC**
     - **AMO**
     - **rFP**
     - **Notes**
   * - German 50mm leGrW 36
     - ⬡1-25
     - 1
     - 3
     - 8
     - 4
     - Squad mortar — platoon organic
   * - German 81mm sGrW 34
     - ⬡3-60
     - 1
     - 3
     - 10
     - 7
     - Company mortar
   * - Soviet 50mm RM-40
     - ⬡1-20
     - 1
     - 2
     - 8
     - 4
     - Squad mortar — less accurate than German
   * - Soviet 82mm PM-36
     - ⬡3-55
     - 1
     - 3
     - 10
     - 7
     - Company mortar
   * - German 120mm GrW 42
     - ⬡5-75
     - 2
     - 3
     - 8
     - 9
     - Heavy mortar — battalion asset


16.3  Ammunition
----------------


**16.3.1**  Each mortar's base AMO value is printed on its counter. Base AMO rounds are certain — no roll, no private record. All uncertainty about total supply lives in the extended ammunition table (Rule 16.3.3), which begins only after the base rounds are spent.

.. container:: rule-guide

   **Why:** Keeps the printed AMO value completely reliable — no hidden roll or secret record shadows it — so uncertainty about ammunition enters the game only once at the single, well-defined point where the extended table (Rule 16.3.3) takes over, not scattered across two overlapping mechanisms.

   **Example:** A mortar with printed AMO 8 is guaranteed exactly 8 fire missions before any uncertainty begins — its 9th mission onward is the first point where the extended ammunition table's rolls come into play.

*NOTE: earlier drafts also added a secret 1d6−1 bonus recorded privately at setup. Two mechanisms cannot both govern the same supply — a player who rolled +5 secret rounds could still be forced dry by a first extended-table roll of 1 — and the extended table alone already provides hidden, variable ammunition without any private bookkeeping. The secret roll is removed.*

**16.3.2**  Each fire mission (HE or smoke) expends 1 AMO. HE and smoke ammunition are tracked on the same AMO count unless the scenario specifies separate pools.

.. container:: rule-guide

   **Why:** Draws ammunition down by mission, not by round type, so a mortar that alternates between HE and smoke missions depletes the same shared pool — the scenario has to explicitly call out separate pools if HE and smoke should be tracked independently.

   **Example:** A mortar with AMO 8 that fires 3 HE missions and 2 smoke missions has used 5 of its 8 AMO total, leaving 3 — the smoke missions drew from the same count as the HE ones unless the scenario says otherwise.

**16.3.3**  When the mortar has fired its base AMO rounds, rather than announcing exhaustion, the owning player rolls on the extended ammunition table for each subsequent mission:

.. container:: rule-guide

   **Why:** Continues the mortar's ability to fire past its printed AMO into genuine uncertainty, so the opponent never knows for certain when a mortar has truly run dry (Rule 16.3.4) — the extended table is what keeps that uncertainty alive rather than a hard stop at the printed number.

   **Example:** A mortar that has fired all 8 of its base AMO rounds doesn't simply stop — its next fire mission triggers a roll on the extended ammunition table, which might let it fire again, force a last salvo, or run it dry right there.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll (1d6)**
     - **Result**
   * - 1–2
     - Out of ammunition — mortar cannot fire again this scenario
   * - 3–4
     - Last salvo — fires this mission normally, then out of ammunition
   * - 5–6
     - Ammunition available — fires this mission normally, roll again next mission


**16.3.4**  The opponent never knows whether a mortar has exhausted its base AMO. A player may choose to stop firing a mortar even when rounds remain — to conserve for a critical moment or to deceive the opponent about remaining capacity.

.. container:: rule-guide

   **Why:** Keeps ammunition status private information rather than a public counter, since real-world ammunition supply is exactly the kind of thing an opponent wouldn't know — this uncertainty is also what makes a player's choice to hold fire meaningful, whether for conservation or deception.

   **Example:** An opponent watching Alpha's mortar go quiet has no way to tell whether it's out of ammunition, conserving rounds for later, or simply bluffing about being dry — the silence itself carries no information either way.

16.4  Targeting Modes
---------------------


**16.4.1**  Mortars may fire in five modes, each with different accuracy and delay:

.. container:: rule-guide

   **Why:** Trades accuracy against speed differently across five distinct modes, so a player must choose between a fast but blind shot and a slower, better-observed one — reflecting real fire-control tradeoffs between having eyes on target versus firing immediately.

   **Example:** A squad mortar with LOS to its target can fire immediately at full accuracy via Direct Lay, while a mortar firing Map Fire with no forward observer and no registration takes 3 impulses to arrive and suffers a -2 accuracy penalty for firing blind.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Mode**
     - **Requirements**
     - **ACC Modifier**
     - **Delay**
     - **Notes**
   * - Observed fire
     - Friendly unit (FO) with LOS to target hex spends 1 AP to call mission
     - +0
     - 1 impulse (light, 50–60mm) / 2 impulses (medium, 81–82mm) / 3 impulses (heavy, 120mm)
     - FO leader adds OBS rating to ACC
   * - Registered target
     - Target hex pre-designated at scenario setup (limit 2 per mortar)
     - -1
     - 1 impulse
     - Pre-calculated fire data
   * - Map fire
     - No FO, no registration
     - -2
     - 3 impulses
     - Firing blind — significant accuracy penalty
   * - Squad mortar direct lay
     - Squad mortar with LOS to target hex (crew fires own mortar)
     - +0
     - 0 impulses — immediate
     - No slip required
   * - Squad mortar blind fire
     - Squad mortar without LOS
     - -2
     - 1 impulse
     - Slip required


**16.4.2**  Effective ACC = mortar ACC + mode modifier + FO leader OBS (if applicable). If effective ACC is 0 or less, skip the accuracy roll — the round disperses automatically (Rule 16.6.3). Firing in such a mode is legal but wildly inaccurate.

.. container:: rule-guide

   **Why:** Skips the dice entirely once effective ACC bottoms out at 0 or below, since there's no meaningful roll left to make — a mission that's mathematically guaranteed to disperse gets treated as exactly that, saving a pointless roll while still allowing the (bad) shot to be legally attempted.

   **Example:** A mortar with base ACC 2 firing Map Fire (-2 modifier) with no FO has effective ACC 0 — the mission automatically disperses without a roll, though a desperate player might still call it hoping the dispersion lands somewhere useful.

**16.4.3**  Minimum range applies in all modes — a mortar cannot target a hex closer than its RNG minimum regardless of mode.

.. container:: rule-guide

   **Why:** Applies the minimum-range restriction uniformly across every targeting mode, since a mortar's minimum range reflects its actual trajectory physics (Rule 16.1) — no amount of clever spotting or fire-control mode changes that hard mechanical limit.

   **Example:** A mortar with RNG ⬡3-60 cannot target a hex 2 hexes away in any mode — not even Squad Mortar Direct Lay with perfect LOS, since the minimum range restriction applies regardless of targeting method.

16.5  Sealed Fire Mission Slips
-------------------------------


**16.5.1**  When a fire mission is called (except squad mortar direct lay), the owning player writes a sealed slip before the reaction window opens.

.. container:: rule-guide

   **Why:** Commits the fire mission's details to a sealed slip before anyone can react to it, extending the same physical-concealment approach used for hidden units (Section 14) to indirect fire — target information stays genuinely secret rather than depending on a player's word.

   **Example:** Alpha's side calls an indirect fire mission and writes the target hex and timing on a slip before the opponent's reaction window even opens — the mission's details are locked in before anyone else can respond to them.

**16.5.2**  The slip records: mortar unit ID, target hex coordinate, firing mode, turn and impulse called, turn and impulse of arrival, and AMO count used.

.. container:: rule-guide

   **Why:** Standardizes exactly what a slip must record so every fire mission's key facts — which mortar, where, how, and when — are captured completely and unambiguously at the moment of writing, leaving nothing to reconstruct or dispute later.

   **Example:** A completed slip lets anyone reading it later reconstruct the whole mission: which mortar fired, at which hex, under which mode, called on which impulse, arriving on which later impulse, and how much AMO it cost.

**16.5.3**  The slip is folded face down and placed beside the mortar counter. Both players acknowledge its presence — the existence of the slip is public, its contents are secret.

.. container:: rule-guide

   **Why:** Splits the slip's existence from its content deliberately — the opponent should know a mission is pending (creating real tension, Rule 16.5.6) while having no way to learn where it's headed until the rules say so.

   **Example:** An opponent can see a folded slip sitting beside Alpha's mortar counter and knows a fire mission is inbound, but nothing about the slip's placement or folding reveals which hex it targets.

**16.5.4**  The slip may not be modified after being placed. The target hex and arrival timing are committed at the moment of writing.

.. container:: rule-guide

   **Why:** Locks the mission in permanently at the moment of writing, preventing a player from adjusting the target after seeing how the situation develops — the whole point of a called fire mission is that it commits to a plan before knowing exactly how events will unfold by the time it arrives.

   **Example:** A slip written targeting hex D4 lands on D4 (subject to dispersion, Rule 16.6) even if the intended target has since moved away — the owning player cannot edit the slip to chase a moving target.

**16.5.5**  On the arrival impulse, the slip is revealed and read aloud. The round lands as written. No retroactive adjustment is possible.

.. container:: rule-guide

   **Why:** Executes exactly what was committed at writing time with zero opportunity for hindsight correction, since the whole tension of indirect fire comes from having to commit before knowing the final outcome — revealing the slip is the moment that commitment pays off or doesn't.

   **Example:** When Alpha's slip arrives, it's read aloud exactly as written — if circumstances at the target hex have changed since the slip was written, that's simply the fire mission's outcome, not something to be adjusted after the fact.

**16.5.6**  The opponent knows a fire mission is pending from the presence of the slip. They do not know the target hex until revelation. This creates the historical tension of incoming fire — you know it is coming but not where.

.. container:: rule-guide

   **Why:** States outright the intended emotional effect of the whole slip mechanism — the dread of known-incoming, unknown-where fire is a deliberate design goal, not an incidental byproduct of the secrecy mechanics.

   **Example:** A player who sees an enemy slip appear beside a mortar counter knows a mission is coming and roughly when, but has to make positioning decisions without knowing whether their own hex is the target — exactly the uncertainty the system is built to create.

16.6  Dispersion
----------------


**16.6.1**  On the arrival impulse, roll 1d6 vs the effective ACC value.

.. container:: rule-guide

   **Why:** Times the accuracy roll for the moment the round actually lands, not when the mission was called — everything about targeting and mode was already locked in by the sealed slip (Section 16.5); this roll is purely about where the round ends up.

   **Example:** A slip called several impulses ago finally reaches its arrival impulse; only now, at revelation, does the accuracy roll against effective ACC actually happen.

**16.6.2**  If the roll is equal to or less than ACC: the round lands on the target hex. No dispersion.

.. container:: rule-guide

   **Why:** Uses a roll-under mechanic for accuracy (rather than the roll-over pattern used elsewhere in the rules) since ACC represents a threshold of skill to beat, not a target number to reach or exceed — a lower ACC value means better accuracy, matching real fire-control ratings.

   **Example:** A mortar with effective ACC 3 lands its round precisely on the target hex on a roll of 1, 2, or 3 — anything higher triggers dispersion instead.

**16.6.3**  If the roll exceeds ACC: the round disperses. Determine landing hex:

.. container:: rule-guide

   **Why:** Sends a missed accuracy roll into a further two-part determination (distance and direction, Rules 16.6.4-16.6.5) rather than just declaring a miss outright — indirect fire that misses its exact target still lands somewhere specific and potentially dangerous, not simply nowhere.

   **Example:** A mortar round that fails its accuracy roll doesn't just vanish — it lands at a real, determined hex some distance and direction away from the original target, still capable of hitting whatever's actually there.

**16.6.4**  Dispersion distance: roll D3 (1d6, halve, round up). Result = number of hexes from the target hex (1–3).

.. container:: rule-guide

   **Why:** Keeps dispersion distance modest — at most 3 hexes — reflecting that even an inaccurate mortar round doesn't land wildly far from its intended target, and uses the D3 mechanic to produce a compact, easy-to-roll range of outcomes.

   **Example:** A dispersed round rolling D3 result of 2 lands exactly 2 hexes away from the original target hex, in whichever direction the next roll (Rule 16.6.5) determines.

**16.6.5**  Dispersion direction: roll 1d6. 1=North, 2=Northeast, 3=Southeast, 4=South, 5=Southwest, 6=Northwest. These six directions correspond to the six hexsides of the flat-top hex grid; every map carries a compass rose defining North.

.. container:: rule-guide

   **Why:** Maps the six roll results directly onto the six hexsides of the flat-top hex grid, so dispersion direction always corresponds to a real, unambiguous direction on the map — the compass rose printed on every map is what keeps this mapping consistent across different maps.

   **Example:** A dispersion roll of 3 sends the round Southeast of the target hex — the exact same direction on every map, since each map's compass rose defines North the same way this table assumes.

**16.6.6**  The round lands at the dispersed hex. Apply blast effect from that point.

.. container:: rule-guide

   **Why:** Confirms the dispersed hex — not the original target — is what actually matters from this point forward, since everything about the blast (Section 16.7) resolves from wherever the round genuinely landed, missed shot or not.

   **Example:** A round dispersed 2 hexes Southeast of its intended target applies its blast effect centered on that dispersed hex, not on the hex the mission was originally aimed at.

**16.6.7**  Friendly units within the blast area of a dispersed round are subject to friendly fire — blast effect applies regardless of side.

.. container:: rule-guide

   **Why:** Makes dispersion a genuine risk to the calling side's own troops, not just a whiffed attack against the enemy — a real mortar round doesn't check whose side is standing in its landing zone, and neither does this rule.

   **Example:** A dispersed round that lands in a hex occupied by the calling side's own unit applies its blast effect to that friendly unit exactly as it would to an enemy unit in the same hex.

16.7  Blast Effect
------------------


**16.7.1**  When a round lands, apply blast effect to the landing hex and all hexes within BLT radius.

.. container:: rule-guide

   **Why:** Extends a mortar round's effect beyond just its exact landing hex, out to the printed blast radius — a real explosive round doesn't only harm whoever happens to be standing in the precise impact hex, but everything nearby within the blast's reach.

   **Example:** A round with BLT 1 landing in a given hex also affects all 6 adjacent hexes, per the BLT 1 definition (Rule 16.1) — anyone in the target hex or its immediate surroundings is caught in the blast.

**16.7.2**  For each unit in the blast area, resolve fire combat using the mortar's rFP value. Use the standard fire resolution procedure (Section 8) with the following modifications:

.. container:: rule-guide

   **Why:** Reuses the same core fire-resolution machinery (Section 8) for mortar blast rather than inventing a separate combat system, while flagging that several specific modifications (Rules 16.7.3-16.7.6) apply on top — indirect fire is a variant of the same fire-combat model, not a wholly different one.

   **Example:** A unit caught in a mortar's blast area resolves its fire combat with the same dice-and-roll procedure as ordinary direct fire (Section 8), just using the mortar's rFP and the specific exceptions listed in the rules that follow.

**16.7.3**  Cover modifiers apply — units in cover are protected from indirect fire.

.. container:: rule-guide

   **Why:** Keeps the normal terrain cover system (Rule 4.2) fully in effect against mortar fire, since good cover genuinely does protect against blast and shrapnel the same way it protects against direct fire — indirect fire doesn't bypass the cover mechanics wholesale.

   **Example:** A unit in a foxhole (+6 cover) caught in a mortar's blast area still gets that +6 cover bonus against the blast's effective rFP, same as it would against a direct rifle shot.

**16.7.4**  Reverse slope (a position, Rule 4.4.4) and building cover are each reduced by 1 step — indirect fire angles over and into these positions. Reverse slope +4 becomes +3. Building heavy +5 becomes +4.

.. container:: rule-guide

   **Why:** Reduces the effectiveness of specifically the cover types that rely on blocking a direct line of sight or fire — since a plunging mortar round arrives from above and can angle into a reverse slope or through a building's roof, those positions offer somewhat less protection against indirect fire than they do against a flat trajectory.

   **Example:** A unit on reverse slope normally getting +4 cover against indirect fire (Rule 4.4.4) instead gets +3 against mortar blast specifically — one step less than its usual protection, reflecting that plunging fire can reach positions a direct shot couldn't.

**16.7.5**  No range falloff — mortar rFP is flat regardless of range to target. The dispersion system handles accuracy at range; lethality on impact is constant.

.. container:: rule-guide

   **Why:** Keeps a mortar round's destructive power constant no matter how far it traveled, since a shell that actually lands does the same damage whether fired from close or far — range affects whether the round hits accurately (Section 16.6's dispersion), not how hard it hits once it does.

   **Example:** A mortar's rFP against a target 10 hexes away is identical to its rFP against a target 40 hexes away — only the accuracy roll and dispersion outcome differ with range, not the blast's underlying lethality.

**16.7.6**  Mortars use a single rFP value with no ⬡h -f notation. They do not participate in fire group grouping with direct fire weapons.

.. container:: rule-guide

   **Why:** Keeps mortars out of the direct-fire notation and grouping system (Rules 2.4, 8.1) entirely, since their flat, range-independent rFP (Rule 16.7.5) and their fundamentally different targeting procedure make them incompatible with summing into a direct-fire fire group.

   **Example:** A mortar firing at the same target as a squad's direct-fire attack doesn't combine its rFP into that squad's fire group total — the mortar's blast resolves as its own separate attack using its own flat rFP value.

**16.7.7**  Hidden units in the blast area: blast effect applies regardless of visibility. A dummy marker in the blast hex produces no effect. A real hidden unit takes the blast effect and is automatically revealed — the explosion nearby discloses the position.

.. container:: rule-guide

   **Why:** Lets mortar blast strike hidden units without needing a spot roll first — an explosion doesn't care whether it can see its target — while still respecting the difference between a real hidden unit (which takes the effect and is revealed) and a dummy (which, having nothing under it, simply produces no effect at all).

   **Example:** A dispersed mortar round landing on a hidden marker either does nothing (if that marker is a dummy) or hits the real unit underneath and automatically reveals it (if it's genuine) — the blast forces the same automatic-reveal outcome as any other blast-adjacent detection rule (Rule 14.9's automatic triggers).

**16.7.8**  Vehicles in the blast area: an open-topped vehicle (the ○— symbol, Rule 17.1) or unarmoured vehicle takes the blast as a normal fire attack against its class Defence (Rule 18.8.5), like infantry. A closed AFV takes no damage from mortar blast, but its crew must pass a check (1d6 + Morale modifier, Rule 15.2.1a) or the vehicle is Suppressed — threshold 3, or 4 against 120mm-class blast. Mortars never roll on the Section 18 penetration tables.

.. container:: rule-guide

   **Why:** Splits vehicle vulnerability to mortar blast by whether the crew is actually exposed — an open-topped or unarmoured vehicle takes the blast like infantry would, while a closed AFV's armor genuinely protects the crew from shrapnel, so the worst mortar fire can do to it is rattle and suppress the crew, never penetrate.

   **Example:** An open-topped halftrack caught in a mortar blast resolves damage against its class Defence just like an infantry unit would; a closed tank in the same blast takes no damage at all, but its crew rolls to avoid Suppression at threshold 3 (or 4 if it was a 120mm-class round).

    *See also: Rule 17.1 (open-top symbol), Rule 19.1 (vehicle morale checks).*

16.8  Adjustment Fire
---------------------


**16.8.1**  After a round disperses, the FO may call an adjustment mission.

.. container:: rule-guide

   **Why:** Gives an observed fire mission's dispersed miss a real second chance, since a forward observer who actually saw where the first round landed can use that information to correct the aim — this option only makes sense when there's an FO actually watching the impact.

   **Example:** After Alpha's FO-directed mortar mission disperses off-target, the FO — having watched the round land — can call for an adjustment mission to correct toward the real target.

**16.8.2**  Write a new slip with the adjusted target hex. Adjustment delay is always 1 impulse regardless of mortar type. Effective ACC for the adjustment is the original mission's effective ACC (Rule 16.4.2, including its mode modifier) + 2 (crew is already set up and ranged in).

.. container:: rule-guide

   **Why:** Gives the adjustment mission a fixed short delay and a real accuracy bonus, since the crew is already set up, ranged in, and has fresh correction data from the first round's impact — a second shot from an already-firing crew is both faster and more accurate than the original.

   **Example:** A heavy mortar's original observed-fire mission had a 3-impulse delay; its adjustment mission, once called, arrives in just 1 impulse regardless of mortar type, and gets +2 to the original mission's effective ACC on top.

**16.8.3**  Only one adjustment is permitted per fire mission. After adjustment, the mission is either fire for effect or cancelled.

.. container:: rule-guide

   **Why:** Caps correction at a single adjustment per mission rather than allowing indefinite fine-tuning, since real fire missions don't get unlimited ranging shots — one correction is the model's abstraction of "walking in" a mortar barrage before committing to the actual attack.

   **Example:** A mission that disperses even after its one permitted adjustment cannot call for a second adjustment — the owning player must either accept firing for effect at that point or cancel the mission outright.

**16.8.4**  Adjustment costs 1 additional AMO — the ranging round and adjustment round are separate expenditures.

.. container:: rule-guide

   **Why:** Charges the adjustment as its own separate ammunition expenditure, since it represents an entirely new round fired, not a free correction to the first one — accuracy improvements from adjustment come at the real cost of additional ammunition.

   **Example:** A fire mission that disperses and then calls for an adjustment has spent 2 AMO total by the time the adjustment round lands — 1 for the original ranging round and 1 more for the adjustment.

16.9  Smoke Rounds
------------------


**16.9.1**  Smoke rounds follow the same targeting, sealed slip, delay, and dispersion procedures as HE rounds.

.. container:: rule-guide

   **Why:** Reuses the entire targeting and dispersion machinery built for HE rounds (Sections 16.4-16.6) for smoke as well, since the mechanical question of "will the round land where intended" is identical for both round types — only what happens on landing differs.

   **Example:** A smoke mission is called, sealed, delayed, and rolled for dispersion using the exact same procedure as an HE mission at the same range and mode — the round type only changes what happens once it actually lands (Rule 16.9.2).

**16.9.2**  On landing, place a SMOKE marker showing step 3 (THICK) in the landing hex and all hexes within BLT radius.

.. container:: rule-guide

   **Why:** Starts every smoke round at its maximum concealment step (THICK) covering its whole blast radius, since a fresh smoke round is at its densest and most effective the moment it lands — the smoke only begins to thin from this point on (Section 16.10).

   **Example:** A smoke round with BLT 1 landing at a hex places THICK smoke markers in that hex and all 6 adjacent hexes simultaneously — the full blast radius starts fully screened.

**16.9.3**  Each SMOKE marker is independent. Markers from different fire missions or in different hexes dissipate separately.

.. container:: rule-guide

   **Why:** Keeps each smoke marker's dissipation roll (Rule 16.10.1) independent per hex, so a screen from one mission and a screen from another (or even different hexes from the same mission) can thin out at different rates rather than all clearing in lockstep.

   **Example:** Two smoke missions called at different times, or even different hexes from the same BLT radius, each roll their own dissipation independently — one hex's smoke might clear while an adjacent hex's smoke from the same mission is still THICK.

16.10  Smoke Dissipation
------------------------


**16.10.1**  During each Recovery Phase, roll 1d6 for each individual SMOKE marker on the map:

.. container:: rule-guide

   **Why:** Times smoke dissipation to the same Recovery Phase used for other automatic per-turn rolls (Rule 5.2.8), and rolls once per individual marker (not once for all smoke on the map together) so each patch of smoke has its own independent, uncertain lifespan.

   **Example:** A map with three separate SMOKE markers rolls three separate 1d6 checks each Recovery Phase — one marker might thin out while the other two hold, purely by chance.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1–2
     - Marker advances one dissipation step (3→2→1→removed)
   * - 3–6
     - Marker holds at current step


**16.10.2**  Smoke effects by dissipation step:

.. container:: rule-guide

   **Why:** Ties smoke's game effect directly to its dissipation step, so a screen weakens gradually and predictably rather than being either fully effective or fully gone — both its firepower-blocking and its concealment bonus taper down together as the step decreases.

   **Example:** Smoke at step 2 (THINNING) still gives -2 rFP per hex to fire passing through and +2 CON to units in it — noticeably weaker than fresh THICK smoke (-3/+3), but still meaningfully better than the almost-gone step 1 (-1/+1).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Step**
     - **Name**
     - **Intervening rFP Penalty**
     - **CON Bonus (concealment)**
     - **Notes**
   * - 3
     - THICK
     - -3 per hex
     - +3
     - Full smoke — movement across is heavily screened
   * - 2
     - THINNING
     - -2 per hex
     - +2
     - Smoke patchy — partial concealment
   * - 1
     - DISSIPATING
     - -1 per hex
     - +1
     - Remnant smoke — minor effect
   * - 0
     - GONE
     - Remove marker
     - —
     - Smoke has cleared


**16.10.3**  SMOKE markers use the existing intervening terrain penalty system (Section 4.3). A unit firing through 2 hexes of THICK smoke suffers -6 rFP to its fire — effectively preventing accurate fire through a fresh smoke screen.

.. container:: rule-guide

   **Why:** Plugs smoke into the same intervening-terrain penalty system already used for woods, buildings, and other obstructing terrain (Section 4.3), so smoke's fire-blocking effect stacks and calculates exactly like any other terrain penalty rather than needing a separate calculation.

   **Example:** A fire line crossing 2 hexes of THICK smoke (-3 per hex, Rule 16.10.2) takes a total -6 rFP penalty, calculated the same way multiple hexes of any other terrain type would sum under Rule 4.3.3.

**16.10.4**  Units occupying a SMOKE hex add the smoke CON bonus to their concealment value for spotting purposes (Section 14.9).

.. container:: rule-guide

   **Why:** Gives smoke a second function beyond blocking fire — it also improves concealment against spotting (Section 14.9), plugging into the same CON modifier system as other terrain-based concealment bonuses, since a smoke-obscured unit really is harder to see as well as harder to shoot through.

   **Example:** A unit sitting in a hex with THICK smoke (+3 CON, Rule 16.10.2) adds that bonus to its concealment the same way a unit in dense woods would add its own CON bonus (Rule 14.9.7's table) — smoke is just another concealment-granting condition in that same system.

**16.10.5**  Per-hex independent dissipation means smoke clouds can develop realistic gaps — one hex clears while adjacent hexes remain thick. A player crossing through smoke should check each hex's current step as they move.

.. container:: rule-guide

   **Why:** Flags the practical consequence of Rule 16.9.3's per-hex independence — a smoke screen isn't a uniform blanket that clears all at once, so a unit moving through it needs to actually track each hex's individual dissipation step rather than assuming the whole screen behaves the same way.

   **Example:** A unit crossing a 3-hex smoke screen might find the first hex still THICK, the second THINNING, and the third already GONE — the smoke's protection varies hex by hex along its route, not uniformly across the whole screen.

16.11  Off-Map Artillery
------------------------


**16.11.1**  Off-map artillery uses the same sealed slip and dispersion system as on-map mortars with the following differences:

.. container:: rule-guide

   **Why:** Reuses the mortar system's whole sealed-slip and dispersion machinery for off-map artillery rather than a separate ruleset, since the underlying mechanics (commit, delay, reveal, disperse) are the same concept scaled up — only the specific numbers differ (Rules 16.11.2-16.11.6).

   **Example:** Calling off-map artillery still means writing a sealed slip, waiting through a delay, and rolling for dispersion on arrival — exactly the same procedural shape as calling an on-map mortar mission, just with different delay and accuracy values.

**16.11.2**  Delay: 1 full turn for registered targets. 2 full turns for unregistered fire missions. Full turn delay means: called in Turn N, arrives at start of Turn N+1 or N+2 Action Phase.

.. container:: rule-guide

   **Why:** Scales delay up to full turns rather than mere impulses, since off-map artillery genuinely takes far longer to coordinate and fire than an organic on-map mortar — the coordination chain (radio call, higher-echelon approval, actual firing battery) is realistically much slower.

   **Example:** Off-map artillery called against an unregistered target in Turn 3 doesn't arrive until the start of Turn 5's Action Phase — a full two turns of anticipation before the rounds actually land.

**16.11.3**  A radio operator or designated FO unit with artillery contact capability is required to call off-map artillery. This capability is a scenario-defined asset — not all scenarios include it.

.. container:: rule-guide

   **Why:** Gates off-map artillery behind a specific, scenario-defined asset rather than making it universally available, since real access to off-map fire support depended on having the actual communications link to call for it — a scenario without that asset simply doesn't offer this option.

   **Example:** A scenario that includes a radio operator with artillery contact capability lets that side call off-map artillery; a scenario that doesn't include such an asset has no off-map artillery available at all, regardless of what other units are present.

**16.11.4**  The number of off-map artillery support requests available is printed in the scenario parameters. Once exhausted, no further requests may be made.

.. container:: rule-guide

   **Why:** Caps off-map artillery to a fixed, scenario-defined number of calls, reflecting that supporting artillery batteries have finite ammunition and finite priority to allocate across the whole battlefield, not just this one engagement.

   **Example:** A scenario printing "2 artillery support requests" means that side can call off-map artillery missions exactly twice total during that scenario — a third request, once the first two are used, simply cannot be made.

**16.11.5**  Off-map artillery rFP and blast radius values are defined in the scenario parameters based on the asset available (light, medium, heavy artillery, or air support).

.. container:: rule-guide

   **Why:** Leaves the specific power of off-map support to each scenario's own design rather than a fixed universal value, since the actual asset behind a support request (a battery of light guns versus a flight of heavy bombers) varies enormously and should be represented accordingly.

   **Example:** A scenario offering heavy artillery support prints correspondingly high rFP and blast radius values for it in its scenario parameters — a different scenario offering only light artillery would print much smaller numbers for the same mechanic.

**16.11.6**  Off-map artillery ACC is typically 2-3 for pre-war registration and 2 for map fire, reflecting the difficulty of accurate unobserved bombardment.

.. container:: rule-guide

   **Why:** Sets off-map artillery's typical accuracy noticeably worse than an on-map mortar's usual range (Rule 16.2 table's ACC 2-3 too, but under far better observation conditions) to reflect that unobserved, long-range indirect fire is inherently less precise than a mortar crew watching its own rounds land.

   **Example:** An off-map artillery mission fired as map fire (no observation) typically uses ACC 2 — a low value reflecting the genuine difficulty of hitting anything precisely without eyes on the target.

**16.11.7**  The 2-turn delay for unregistered off-map artillery means calling it at the right moment is critical — the situation may have changed completely by the time rounds arrive.

.. container:: rule-guide

   **Why:** Calls out the tactical consequence of Rule 16.11.2's long delay explicitly — a player calling unregistered off-map artillery is committing to a target hex based on the current situation, with no guarantee the enemy will still be there two full turns later when the rounds finally land.

   **Example:** A player who calls unregistered off-map artillery on an enemy concentration might find, two turns later when the mission finally arrives, that the enemy has already advanced or withdrawn from that hex entirely — the slow timeline is a real risk built into the choice to use this asset.

16.12  Fire Mission Slip Format
-------------------------------


Fire mission slips are pre-printed components included in the game. Players fill in the following fields:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Field**
     - **Content**
   * - Mortar unit ID
     - Counter identifier (e.g. GER-81MM-1)
   * - Target hex
     - Map coordinate (e.g. D4)
   * - Mode
     - Observed / Registered / Map fire / Adjustment
   * - Called
     - Turn number and impulse number
   * - Arrives
     - Turn number and impulse number (called + delay)
   * - AMO used
     - Running total of missions fired this scenario
   * - Round type
     - HE or Smoke
