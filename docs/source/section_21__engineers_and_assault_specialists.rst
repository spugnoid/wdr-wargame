Section 21 — Engineers and Assault Specialists
==============================================

Combat engineers were the unit that made the impossible possible. Minefields, wire obstacles, fortified buildings, water crossings, demolished bridges — all the terrain features that stopped regular infantry cold were the engineer's working environment. At the same time, engineers were among the most dangerous close-assault specialists, their training and specialist equipment making them significantly more effective in building clearance and fortification assault than line infantry.

21.1  Engineer Counter Design
-----------------------------


**21.1.1**  Engineer counters use the wave symbol [≋] and display capability icons on the support weapon band at the bottom of the counter.

.. container:: rule-guide

   **Why:** A dedicated symbol and a visible capability band let a player identify an engineer counter and see at a glance which specialist actions (demolitions, breaching, mine clearing, and so on) it can still perform, without cross-referencing a separate roster.

   **Example:** Alpha's engineer counter shows the ≋ symbol with DEMO, BRH, MINE, and FLAM icons on its support band — a glance tells the player it can still demolish a target, breach an obstacle, clear a minefield, or use its flamethrower this scenario.

**21.1.2**  Standard engineer counter stats:

.. container:: rule-guide

   **Why:** Engineers trade raw mobility for close-combat and specialist capability — the low M# reflects the weight of demolition and breaching equipment, while the high G# and Defence reflect training and gear specifically suited to close-quarters and fortification assault.

   **Example:** Alpha's engineer squad moves at only M1 due to its equipment load, but brings G5 into a close assault — far higher than a standard rifle squad's assault rating.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Stat**
     - **Value**
     - **Notes**
   * - M#
     - M1
     - Heavy equipment limits speed
   * - F#
     - F1
     - Standard fire capability — engineers are an ordinary (non-ROF) unit
   * - G#
     - G5
     - High — specialist assault equipment
   * - Fire line
     - ╌ 5 ⬡4 -1
     - Standard rifle capability — engineers are trained infantry
   * - Defence
     - 7
     - Specialist equipment, trained for close combat
   * - Morale
     - 6
     - Selected troops — veteran/elite quality (Morale modifier +1) across most nations


**21.1.3**  Engineer capability icons appear on the bottom support band. Each capability may be used a limited number of times per scenario. When expended, cover the icon with an EXPENDED strip — the same strip used for single-shot AT weapons.

.. container:: rule-guide

   **Why:** Reusing the EXPENDED strip mechanic already established for single-shot AT weapons keeps the game's "limited-use capability" bookkeeping consistent across unit types, rather than introducing a new tracking method just for engineers.

   **Example:** After Alpha's engineer squad uses its one DEMO charge to destroy a bridge, the DEMO icon is covered with an EXPENDED strip — the squad can still breach, clear mines, or use its flamethrower, but cannot demolish anything else this scenario.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Icon**
     - **Capability**
     - **Uses per scenario**
     - **Description**
   * - DEMO
     - Demolitions
     - 1
     - Destroy bridge, building, fortification, or road junction
   * - BRH
     - Breach
     - 1 per obstacle
     - Clear wire, hedgehog, dragon's teeth, or open minefield path
   * - MINE
     - Mine clearing
     - 1 per hex
     - Clear a minefield hex to safe passage
   * - FLAM
     - Flamethrower
     - AMO 3
     - Close-range area weapon — ignores cover
   * - BRDG
     - Assault bridge
     - Scenario asset
     - Cross water obstacles — scenario defined
   * - FORT
     - Fortification
     - Ongoing
     - Improve terrain cover value — takes multiple turns


21.2  Breaching Obstacles
-------------------------


**21.2.1**  Engineer units may attempt to breach obstacles that are impassable or prohibitively expensive for regular infantry.

.. container:: rule-guide

   **Why:** Restricting breaching to engineers reinforces their specialist role — regular infantry can be stopped cold by wire, minefields, and fortified obstacles that only trained engineers, with the right tools, can reliably clear.

   **Example:** Squad Bravo (regular infantry) cannot attempt to breach a dragon's-teeth obstacle blocking its advance — only Alpha's engineer squad, brought up in support, can attempt it.

**21.2.2**  Breaching action: engineer unit adjacent to or in the obstacle hex, spend 1 AP. Roll 1d6 + Morale modifier (Rule 15.2.1a) vs breach threshold. A veteran engineer squad (modifier +1) clears wire on 2+ and forces a reinforced bunker entrance only on a natural 6:

.. container:: rule-guide

   **Why:** Scaling breach thresholds by obstacle type and folding in the unit's Morale modifier means better-trained engineers are meaningfully more likely to succeed against harder targets, reflecting real differences in training and experience rather than a flat pass/fail chance.

   **Example:** Alpha's veteran engineer squad (Morale modifier +1) attempts to breach wire (threshold 3) — needing only a 2+ after the modifier — but the same squad attempting a reinforced bunker entrance (threshold 7) needs a natural 6 regardless of modifier.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Obstacle type**
     - **Breach threshold**
     - **Notes**
   * - Wire / fence
     - 3
     - Light obstacle — usually succeeds
   * - Hedgehog / dragon's teeth
     - 4
     - Anti-vehicle obstacles — harder for infantry
   * - Minefield — clear path
     - 5
     - Open lane only — does not clear entire hex
   * - Fortification wall / berm
     - 6
     - Reinforced construction
   * - Reinforced bunker entrance
     - 7
     - Designed to resist assault


**21.2.3**  Success: place a BREACH marker. All friendly units may use the breach — no additional AP cost, movement cost equals normal hex entry cost. Expend BRH icon on engineer counter.

.. container:: rule-guide

   **Why:** A successful breach benefits the whole force, not just the engineer that made it — once wire or a minefield lane is opened, any friendly unit can exploit it at normal cost, reflecting that the obstacle itself has genuinely been cleared.

   **Example:** After Alpha's engineer squad successfully breaches a wire obstacle, Squad Bravo moves through the same hex later that turn at normal movement cost, using the BREACH marker Alpha placed.

**21.2.4**  Failure: attempt failed this turn. May retry next turn. BRH icon not expended on failure.

.. container:: rule-guide

   **Why:** Not consuming the BRH icon on failure means a difficult obstacle doesn't permanently strip an engineer's capability just because the dice were unlucky — the limited-use resource is only spent on an attempt that actually works.

   **Example:** Alpha's engineer squad fails its first breach roll against a hedgehog obstacle — the BRH icon remains available, and the squad can try again next turn.

**21.2.5**  Under fire: if the engineer hex receives any fire result this turn, the breach attempt automatically fails regardless of the roll. Covering fire suppressing the enemy position is essential before breaching.

.. container:: rule-guide

   **Why:** Breaching requires exposed, methodical work at the obstacle — being under fire while attempting it isn't just a modifier to the odds, it makes the careful work impossible outright, which is why suppressing the defenders first is a real tactical prerequisite.

   **Example:** Alpha's engineer squad rolls a success on its breach attempt, but the hex took a Suppressed result from enemy fire earlier that turn — the breach automatically fails despite the good roll.

21.3  Demolitions
-----------------


**21.3.1**  Engineer units with the DEMO capability may destroy terrain features when given time to set charges.

.. container:: rule-guide

   **Why:** Gating demolitions behind the DEMO icon (rather than any engineer unit automatically having it) lets scenario design control how many demolition opportunities exist, since destroying a bridge or fortification can be a decisive, game-shaping action.

   **Example:** Alpha's engineer squad has an unexpended DEMO icon, so it may attempt to destroy the bridge ahead of it — a Soviet Sapper squad without organic flamethrower capability could still have DEMO and attempt the same action.

**21.3.2**  Demolition action: engineer unit in or adjacent to target feature, spend 1 AP.

.. container:: rule-guide

   **Why:** Allowing the action from an adjacent hex, not just from inside the target feature, reflects that setting charges on a bridge span or building wall doesn't require the engineer to physically stand on the target itself.

   **Example:** Alpha's engineer squad sets charges on a bridge from the hex at its near end, spending 1 AP, without needing to occupy the bridge hex itself.

**21.3.3**  Not under fire: demolition succeeds automatically. No roll required.

.. container:: rule-guide

   **Why:** With no enemy fire disrupting the work, setting demolition charges is a matter of trained procedure rather than chance — removing the roll entirely when conditions are safe keeps the rule from adding unnecessary randomness to an otherwise straightforward task.

   **Example:** Alpha's engineer squad sets charges on an undefended road junction with no fire incoming this turn — the demolition simply succeeds, no roll needed.

**21.3.4**  Under fire (any fire result received this turn): roll 1d6 + Morale modifier vs 5. Failure — charges not set this turn, may retry. Success — demolition proceeds.

.. container:: rule-guide

   **Why:** Enemy fire turns careful charge-placement into a rushed, dangerous task — introducing a roll (rather than automatic failure, as with breaching under fire in Rule 21.2.5) reflects that demolitions can still succeed under pressure, just less reliably.

   **Example:** Alpha's engineer squad takes a Pinned result while setting charges on a bunker — it must now roll 1d6 plus its Morale modifier against 5 to complete the demolition this turn instead of automatically succeeding.

**21.3.5**  Demolition targets and results:

.. container:: rule-guide

   **Why:** Different targets call for different destruction outcomes — a bridge becomes fully impassable while a building only degrades a cover level — so a single table lets demolitions produce historically appropriate, terrain-specific results rather than one generic "destroyed" effect.

   **Example:** Alpha's engineer squad demolishes a heavy building, reducing its cover from +5 to +4 (light building) rather than removing it entirely — a full demolition effect is reserved for targets like bridges and road junctions.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Target**
     - **Result**
   * - Bridge
     - Destroyed — impassable to all units until repaired by engineers (BRDG capability, 2 turns)
   * - Building — heavy
     - Reduced to building light (+5 cover → +4 cover)
   * - Building — light
     - Reduced to rubble (+4 cover — occupant cover unchanged, but movement cost worsens to 2 and the hex no longer blocks LOS as a solid building, Rule 4.4.2)
   * - Rubble
     - Reduced to open ground (+0 cover) — cleared
   * - Fortification / bunker
     - Reduced to entrenchment (+8 cover → +6 cover)
   * - Road junction
     - Cratered — road movement bonus lost in this hex


**21.3.6**  Expend DEMO icon after use. Each engineer counter carries one demolition charge.

.. container:: rule-guide

   **Why:** Limiting each engineer counter to a single demolition charge keeps demolitions a scarce, decisive resource rather than something that can be used repeatedly to reshape the battlefield turn after turn.

   **Example:** After Alpha's engineer squad destroys the bridge, its DEMO icon is covered with an EXPENDED strip — it cannot demolish anything else this scenario, even if a second high-value target presents itself.

21.4  Mine Clearing
-------------------


**21.4.1**  Minefield hexes impose a movement cost of 3 (all units) and a casualty risk on entry.

.. container:: rule-guide

   **Why:** Combining a movement penalty with a casualty risk makes minefields a genuine area-denial tool rather than just difficult terrain — units are both slowed down and put at risk simply by choosing to cross, which is what made real minefields so effective at channeling attacks.

   **Example:** Squad Bravo, with M4, spends 3 of its 4 movement points just entering a single minefield hex, and risks a mine strike the moment it does.

**21.4.2**  Mine strike: when any non-engineer unit enters a minefield hex, roll 1d6: on 1-2, the unit takes a Casualty result (mine strike). On 3-6, the unit passes safely.

.. container:: rule-guide

   **Why:** A flat, unmodified roll for mine strikes keeps minefields a real threat to any unit that isn't specifically trained to handle them (engineers, per Rule 21.4.3) — there's no way to reduce the risk through tactics or terrain, only by avoiding the hex or clearing it first.

   **Example:** Squad Bravo enters a minefield hex and rolls a 2 — a mine strike inflicts a Casualty result on the squad, a real cost for taking the direct route.

**21.4.3**  Engineer units entering a minefield hex are not subject to the mine strike roll — they advance carefully with probe and detector.

.. container:: rule-guide

   **Why:** Engineers' specialist mine-detection training and equipment is exactly what let them move through minefields that would maim ordinary infantry — this exemption is what makes them uniquely valuable for spearheading an advance through mined terrain.

   **Example:** Alpha's engineer squad enters the same minefield hex Squad Bravo was struck in, but takes no mine-strike roll at all — its training lets it move through safely.

**21.4.4**  Mine clearing action: engineer unit in or adjacent to minefield hex, spend 1 AP. Roll 1d6 + Morale modifier vs 5.

.. container:: rule-guide

   **Why:** Actively clearing a lane (rather than just safely traversing the hex per Rule 21.4.3) is a distinct, roll-based action because it must produce a result other units can rely on — a lane other troops can trust their lives to needs to be genuinely verified as cleared.

   **Example:** Alpha's engineer squad spends 1 AP to clear a lane through the minefield hex it's standing beside, rolling 1d6 plus its Morale modifier against a target of 5.

**21.4.5**  Success: place BREACH marker — a safe lane has been cleared through the hex. Units using the BREACH marker are not subject to mine strike. Expend MINE icon.

.. container:: rule-guide

   **Why:** Reusing the same BREACH marker mechanic from obstacle breaching (Rule 21.2.3) keeps "a safe lane exists here" a single, consistent concept across obstacle types, rather than introducing a separate marker just for cleared minefields.

   **Example:** After Alpha's engineer squad successfully clears the minefield hex, a BREACH marker is placed there — Squad Bravo can now cross that hex later without risking a mine strike, as long as it uses the marked lane.

**21.4.6**  Failure: clearing incomplete this turn. May retry. MINE icon not expended.

.. container:: rule-guide

   **Why:** As with breach failures (Rule 21.2.4), a failed clearing roll shouldn't cost the engineer its limited-use capability — the MINE icon stays available so a difficult minefield can still eventually be cleared with persistence.

   **Example:** Alpha's engineer squad fails its first mine-clearing roll — the MINE icon (limited to 1 use per hex) remains available for a retry next turn.

**21.4.7**  A cleared lane (BREACH marker) is a narrow path — it only protects units explicitly declared to be using the lane. A unit that moves into the hex without using the lane is still subject to mine strike.

.. container:: rule-guide

   **Why:** A cleared lane is a specific, narrow path through the hex, not a blanket clearance of the entire minefield — a unit that doesn't explicitly follow that path is still walking through unswept ground and remains at risk.

   **Example:** Squad Bravo moves into the cleared minefield hex but its player forgets to declare it's using the BREACH lane — the mine strike roll still applies, since the protection only covers units explicitly using the marked lane.

21.5  Flamethrower
------------------


**21.5.1**  The flamethrower is a short-range area weapon that largely negates cover (cover modifiers are halved — Rule 21.5.3). It was most effective in clearing fortifications, bunkers, and buildings where conventional fire was ineffective.

.. container:: rule-guide

   **Why:** Cover that stops bullets does little against a stream of burning fuel that flows into loopholes, doorways, and firing slits — halving cover's effectiveness against flamethrower fire captures why this weapon was specifically prized for clearing exactly the fortified positions conventional fire struggled against.

   **Example:** A bunker with +8 cover would make conventional rifle fire nearly useless, but Alpha's flamethrower attack against that same bunker only applies half that cover value, making it a far more viable option for clearing it.

**21.5.2**  Flamethrower fire line:

.. container:: rule-guide

   **Why:** The flamethrower's stat line is defined by extremes — very high rFP but a brutally steep range falloff — to model a weapon that is devastating up close and completely useless beyond a few dozen metres, unlike the more gradual falloff of rifle or MG fire.

   **Example:** Alpha's flamethrower team, with rFP 8 and a falloff of -f 3, is lethal against a target 1 hex away but contributes zero effective rFP against anything at range 4 or beyond.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Stat**
     - **Value**
     - **Notes**
   * - Icon
     - ≋ (wave)
     - Flamethrower weapon class
   * - rFP
     - 8
     - High lethality on impact
   * - ⬡h
     - 1
     - Loses effectiveness rapidly with range
   * - -f
     - 3
     - Steep falloff — effective only at close range
   * - Effective range
     - 0–3 hexes
     - rFP 0 at range 4+
   * - AMO
     - 3
     - Three flame attacks per scenario


**21.5.3**  Cover modifier: halved for flamethrower attacks (round down). Flame flows around and into cover rather than being blocked by it. Same principle as the grenade phase cover reduction in close assault.

.. container:: rule-guide

   **Why:** Tying this explicitly to the grenade-phase cover reduction already used in close assault keeps the underlying principle — an area effect that seeps into cover rather than being stopped by it — consistent across every rule that uses the same mechanic, rather than restating it from scratch.

   **Example:** A target with +5 cover facing a flamethrower attack only benefits from +2 cover (5 halved, rounded down) — the same halving logic already familiar from close assault's grenade phase.

**21.5.4**  Burning marker: when a flamethrower attack produces a Suppressed result or better, place a BURNING marker in the target hex in addition to the combat result.

.. container:: rule-guide

   **Why:** A flamethrower doesn't just deliver one instant of damage — it sets its target on fire, creating an ongoing hazard that continues to threaten anyone in that hex after the initial attack resolves, which the BURNING marker exists to track.

   **Example:** Alpha's flamethrower attack produces a Suppressed result against a squad in a building — beyond the Suppressed result itself, a BURNING marker is now placed in that hex, threatening further harm on subsequent turns.

**21.5.5**  Burning hex effects: at the start of each activation by a unit in a BURNING hex, that unit takes a fire attack with Resolution FP 3 — roll 1d6+1d8+1d12 normally against the unit's Defence (no cover modifier: the fire is in the cover with them). This attack is exempt from the Long Range Cap (Rule 8.7) — flame kills at any "range". Additionally all units in a BURNING hex suffer -2 CON (fire reveals position).

.. container:: rule-guide

   **Why:** Removing the cover modifier reflects that a burning building or trench offers no protection from a fire that's already inside it, and exempting the attack from the Long Range Cap (Rule 8.7) makes sense since flame doesn't attack at "range" at all — it's already on top of the target; the CON penalty models how a burning hex is impossible to miss from a distance.

   **Example:** A squad that stays in a BURNING hex takes a Resolution FP 3 attack against its full Defence with no cover credit at the start of every activation, and any attempt to remain hidden there suffers a -2 CON penalty from the visible fire.

**21.5.6**  Extinguishing fire: a unit in a BURNING hex may spend 1 AP to attempt to extinguish. Roll 1d6 on 4+ fire is extinguished, BURNING marker removed. On 1-3 fire continues.

.. container:: rule-guide

   **Why:** Giving units in a burning hex an active option to fight the fire — rather than simply enduring it until it burns out — reflects the real urgency of extinguishing flames before they cause further casualties or destroy the position entirely.

   **Example:** A squad caught in a BURNING hex spends 1 AP to extinguish rather than moving out, rolls a 5, and successfully removes the BURNING marker before taking another round of fire damage.

**21.5.7**  Fire duration: if not extinguished, BURNING marker is removed after 3 turns automatically. Buildings struck: each full turn of burning reduces the building one cover level.

.. container:: rule-guide

   **Why:** A capped burn duration keeps flamethrower effects from becoming a permanent, uncounterable hazard, while the ongoing building degradation reflects how sustained fire progressively destroys structural cover the way a single demolition charge (Rule 21.3.5) does instantly.

   **Example:** A heavy building (+5 cover) hit by a flamethrower and left burning for two full turns without being extinguished drops two cover levels, ending at +3, in addition to whatever the initial attack accomplished.

**21.5.8**  Vehicle targets: flamethrower attacks target the engine deck regardless of facing arc — flames flow around the vehicle. Treat as rear arc for AV purposes. Engine fire on any penetrating result (see Rule 18.10).

.. container:: rule-guide

   **Why:** Since flame flows around a vehicle's hull rather than striking one specific facing, it always finds the thinnest armour — the engine deck — regardless of which way the vehicle is actually facing, which is why it's resolved against rear-arc AV values no matter the vehicle's orientation.

   **Example:** Alpha's flamethrower team attacks an enemy tank that is facing directly toward them — the attack is still resolved against the tank's rear-arc AV, since flame reaches the engine deck regardless of facing.

**21.5.9**  Expend FLAM icon when all 3 AMO shots are used.

.. container:: rule-guide

   **Why:** Tracking FLAM as expended only once all 3 shots are exhausted (rather than after any single use) lets the flamethrower behave like a genuinely limited-ammunition weapon within a scenario, consistent with its AMO 3 rating in Rule 21.5.2.

   **Example:** Alpha's flamethrower team has used 2 of its 3 AMO shots — the FLAM icon remains uncovered until the third and final shot is fired, at which point it is marked EXPENDED.

21.6  Building Assault
----------------------


**21.6.1**  Engineers are specialists in clearing buildings. Their training, equipment (satchel charges, shaped charges, smoke grenades), and doctrine specifically address close-quarters building assault.

.. container:: rule-guide

   **Why:** Establishing engineers' building-clearance specialty in prose sets up the concrete mechanical bonuses that follow in Rule 21.6.2 — without this framing, the bonuses would read as arbitrary rather than a direct reflection of specialist training and equipment.

   **Example:** When Alpha's engineer squad joins an assault on a fortified building alongside Squad Bravo, it's Alpha's satchel charges and clearance training — not Bravo's rifles — that the mechanical bonuses in the next rule represent.

**21.6.2**  When an engineer unit participates in a close assault against a building hex the following bonuses apply:

.. container:: rule-guide

   **Why:** Spreading the engineer bonus across three separate assault phases (grenade, entry fire, melee) reflects that their advantage isn't a single flat combat bonus but specialist capability at every distinct stage of clearing a fortified structure, from breaching to the close-quarters fighting that follows.

   **Example:** Alpha's engineer squad leads an assault into a building — its grenade phase uses G# + 2 for satchel and shaped charges, its entry fire gets +2 rFP from fatal-funnel training, and any melee continuation benefits from +1 to morale checks.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Phase**
     - **Engineer bonus**
     - **Notes**
   * - Grenade phase
     - G# + 2
     - Specialist equipment — satchel charges, shaped charges
   * - Entry fire phase
     - +2 rFP
     - Fatal funnel clearance training
   * - Melee continuation
     - +1 to all morale checks
     - Confidence and doctrine in close quarters


**21.6.3**  These bonuses apply only when the engineer unit is the assaulting unit or is in the same hex as the assaulting unit during close assault. Engineer bonuses do not apply if the engineer is providing supporting fire from an adjacent hex.

.. container:: rule-guide

   **Why:** The building-assault bonuses represent hands-on specialist technique in the actual room-to-room clearance, not general engineer competence — an engineer firing support from next door isn't applying satchel charges or fatal-funnel training, so the bonus rightly stays tied to physical participation in the assault itself.

   **Example:** Alpha's engineer squad assaults a building directly and gets the full set of bonuses, but if Alpha instead stayed in an adjacent hex providing covering fire while Squad Bravo made the actual assault, none of the engineer bonuses would apply.

21.7  Fortification Building
----------------------------


**21.7.1**  Engineers can improve terrain cover values given sufficient uninterrupted working time.

.. container:: rule-guide

   **Why:** Fortification is deliberately slow and requires uninterrupted effort, reflecting the real labour of digging entrenchments or reinforcing a position — this is a defensive, preparation-phase capability rather than something usable reactively during active combat.

   **Example:** Alpha's engineer squad spends several consecutive turns digging in an open-ground position before a battle, converting it into a proper entrenchment ahead of the enemy's advance.

**21.7.2**  Fortification action: engineer unit in hex, spends its entire activation each turn working. Unit cannot move or fire while fortifying.

.. container:: rule-guide

   **Why:** Committing the unit's entire activation to fortification — with no ability to move or fire — makes the trade-off explicit: a unit digging in is undefended and immobile for that turn, so a player must genuinely choose between fortifying and staying combat-ready.

   **Example:** Alpha's engineer squad spends its full activation fortifying a position and cannot react to nearby enemy movement or return fire that same turn, even if threatened.

**21.7.3**  Under fire: if the engineer hex receives any fire result during a fortification turn, work stops. Engineer must begin again on the next turn (time already invested is lost).

.. container:: rule-guide

   **Why:** Losing all invested progress the moment fire disrupts the work (rather than merely pausing it) reflects how enemy fire doesn't just interrupt digging — it forces the engineers to take cover and abandon the careful, precise work already done, much like the "under fire" penalties for breaching (Rule 21.2.5) and demolitions (Rule 21.3.4).

   **Example:** Alpha's engineer squad is on its third of four turns fortifying an entrenchment into a full fortification when it takes a Pinned result — all three turns of progress are lost, and the squad must restart the 4-turn count from the beginning next time.

**21.7.4**  Fortification times and results:

.. container:: rule-guide

   **Why:** Scaling required turns by the cover improvement's size — quick for basic entrenching, much longer for a full fortification — reflects the real difference in labour between digging a foxhole and constructing a hardened bunker position.

   **Example:** Alpha's engineer squad needs only 2 uninterrupted turns to dig open ground into an entrenchment (+0 to +6 cover), but a further 4 turns to upgrade that entrenchment into a full fortification (+6 to +8 cover).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Work**
     - **Turns required**
     - **Result**
   * - Open ground → Entrenchment
     - 2 turns
     - Cover +0 → Cover +6
   * - Entrenchment → Fortification
     - 4 turns
     - Cover +6 → Cover +8
   * - Building → Reinforced building
     - 3 turns
     - Cover +4 or +5 → +1 additional
   * - Rubble → Field position
     - 2 turns
     - Cover +4 → irregular cover, counts as entrenchment


**21.7.5**  Place a FORT marker showing current state. Multiple engineer units working on the same position halve the time required (minimum 1 turn per stage).

.. container:: rule-guide

   **Why:** Letting multiple engineer units combine effort on the same position models the practical reality that more hands genuinely speed up digging and construction, while the 1-turn-per-stage floor keeps even a large engineer force from fortifying a position instantly.

   **Example:** Alpha's engineer squad alone needs 4 turns to build a full fortification from an entrenchment, but with a second engineer squad joining the same position, that drops to 2 turns — though a third squad couldn't push it below the 1-turn minimum per stage.

21.8  Assault Bridge
--------------------


**21.8.1**  Assault bridges are scenario-defined assets available to engineer units. Not all scenarios include them.

.. container:: rule-guide

   **Why:** Making assault bridges a scenario-defined asset, rather than something every engineer unit automatically carries, lets scenario designers control whether a water-obstacle crossing is even possible, which can be a decisive factor in scenario balance.

   **Example:** A scenario set along a river might grant the attacking engineer force one assault bridge asset, while a scenario with no water obstacles simply omits BRDG entirely from that engineer unit's capabilities.

**21.8.2**  Bridge deployment: engineer unit at water obstacle edge, spend 2 AP. Roll 1d6 + Morale modifier vs 5 (vs 7 if under fire).

.. container:: rule-guide

   **Why:** The higher target number under fire (7 versus 5) reflects that assembling a bridge span while under fire is significantly more difficult than doing it under safe conditions, consistent with the "harder under fire" pattern used throughout Section 21's other engineer actions.

   **Example:** Alpha's engineer squad deploys an assault bridge across a river at an undefended crossing point, needing only a 5+ after its Morale modifier — but the same action against a defended crossing under fire requires a 7+.

**21.8.3**  Success: bridge placed — BRDG marker at obstacle. All units may cross at normal movement cost. Expend BRDG capability.

.. container:: rule-guide

   **Why:** Once placed, the bridge benefits the entire force just like a successful obstacle breach (Rule 21.2.3) — any unit can use it at normal cost, since the bridge itself, not the engineer squad personally, is what enables the crossing.

   **Example:** After Alpha's engineer squad successfully deploys the assault bridge, both infantry and vehicles from the rest of the force cross the river at that hex for normal movement cost.

**21.8.4**  Failure: may retry next turn. 2 AP cost again.

.. container:: rule-guide

   **Why:** Unlike breaching and mine-clearing failures (Rules 21.2.4, 21.4.6), a failed bridge deployment does cost AP again on retry — reflecting the greater physical effort of assembling bridging equipment compared to simply attempting a skill roll a second time.

   **Example:** Alpha's engineer squad fails its first bridge deployment roll and must spend another full 2 AP to attempt it again next turn, rather than retrying for free.

**21.8.5**  Bridge capacity: all unit types including vehicles.

.. container:: rule-guide

   **Why:** Explicitly including vehicles distinguishes the assault bridge from lighter crossing solutions (like an infantry-only breach lane) — a proper assault bridge is engineered to bear the weight of armour, which is what makes it valuable enough to be a scarce scenario asset.

   **Example:** Once Alpha's engineer squad places the BRDG marker, even a heavy tank can cross the river at that hex, something no infantry-only breach or ford could support.

**21.8.6**  Bridge destruction: a bridge takes a Casualty result from any fire directed at the BRDG marker hex — remove BRDG marker, obstacle impassable again.

.. container:: rule-guide

   **Why:** A hastily assembled assault bridge is a fragile, exposed structure compared to a permanent bridge — a single well-placed hit destroying it (rather than requiring a dedicated demolition action, as with permanent bridges in Rule 21.3.5) reflects how vulnerable field-expedient bridging equipment actually was.

   **Example:** Enemy artillery targets the BRDG marker hex and scores a Casualty result — the assault bridge is destroyed instantly, and the water obstacle becomes impassable again until a new bridge is deployed.

21.9  Representative 1943 Engineer Counters
-------------------------------------------


.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit**
     - **Fire line**
     - **G#**
     - **Capabilities**
     - **Defence**
     - **Morale**
     - **Notes**
   * - German Pioneer squad (Pioniere) — veteran
     - ╌ 5 ⬡4 -1
     - G5
     - DEMO BRH MINE FLAM
     - 7
     - 6
     - Full assault pioneer capability including flamethrower
   * - German Pioneer squad (Pioniere) — regular
     - ╌ 5 ⬡4 -1
     - G5
     - DEMO BRH MINE FLAM
     - 7
     - 6
     - Standard assault engineers
   * - Soviet Sapper squad — regular
     - ╌ 4 ⬡4 -1
     - G4
     - DEMO BRH MINE
     - 6
     - 5
     - No organic flamethrower — separate flamethrower units
   * - Soviet Assault engineer — veteran
     - ╌ 5 ⬡4 -1
     - G5
     - DEMO BRH MINE FLAM
     - 7
     - 7
     - 1943+ specialist assault units — Guards Sapper battalions
   * - British Royal Engineers — regular
     - ╌ 5 ⬡4 -1
     - G4
     - DEMO BRH MINE BRDG
     - 7
     - 6
     - Strong bridge capability — BRDG standard
   * - US Combat Engineers — regular
     - ╌ 5 ⬡4 -1
     - G4
     - DEMO BRH MINE BRDG
     - 7
     - 6
     - Similar to British — strong logistics engineering
