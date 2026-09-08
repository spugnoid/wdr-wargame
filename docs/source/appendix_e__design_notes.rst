Appendix E — Design Notes
=========================

This appendix records the reasoning behind significant design decisions. It is intended for the designer's reference during revision and playtesting. New design decisions should be documented here as the project develops.

E.1  Why Yards, Not Metres
--------------------------


*Design note: Primary source data for WWII weapons — US Army manuals, British War Office documents, Wehrmacht Heeresdruckvorschriften — predominantly expresses effective ranges in yards. While Soviet data uses metres, the rounding error when converting at 40-yard hex scale is negligible (40 yards = 36.6 metres; within 10% of any reasonable range bracket). Using yards avoids constant conversion noise and keeps the data pipeline clean from source to counter.*

E.2  Why 40 Yards Per Hex
-------------------------


*Design note: 40 yards is approximately the width of a city block, a narrow field, or the effective radius of a grenade burst with dispersal. At this scale a squad occupying a hex makes physical sense — ten men in a 40-yard space are dispersed but mutually supporting. ASL uses 40 metres for similar reasons. 40 yards is close enough to 40 metres that scenario conversion between systems is straightforward.*

E.3  The rFP / Falloff Notation System
--------------------------------------


*Design note: Traditional hex and counter games use a single firepower value and a Combat Results Table. The CRT is the real resolution engine — the firepower number is almost meaningless without it. This system replaces the CRT with a formula encoded on the counter itself. The player can calculate any engagement result from first principles using only the counter values and a handful of memorised thresholds. The ⬡h notation groups units naturally for combined fire without requiring any lookup beyond the Resolution Strip for large concentrations.*

E.4  Why the Falloff Formula Uses Floor Division
------------------------------------------------


*Design note: FP(r) = rFP − (f × floor(max(0, r−1) / h)). The floor function produces a stepped curve rather than a smooth linear decline. This is intentional. Real weapon effectiveness does not degrade smoothly — a weapon performs near-optimally within its effective range envelope and then degrades more sharply beyond it. The stepped curve approximates this behaviour using integer arithmetic that players can perform mentally.*

E.5  Summing rFP and f Within a Fire Group
------------------------------------------


*Design note: The summation rule (sum rFP, sum f, retain ⬡h interval) is mathematically equivalent to calculating each unit's effective rFP at range individually and summing the results. This was proven across the full range curve, not just at a single range. The equivalence holds because the floor function distributes across addition when the interval h is identical. Units with different intervals cannot be summed because the floor function does not distribute across different denominators — hence the grouping requirement.*

    *See also: E.60 (the ban this note explains is scoped to the summation shortcut specifically — Rule 8.3.4a permits mixed-⬡h combining under a narrower condition that doesn't need the shortcut at all).*

E.6  Why the Resolution Strip Applies Only to Combined Fire
-----------------------------------------------------------


*Design note: The Resolution Strip applies logarithmic compression to concentrated fire only — single unit fire uses effective rFP directly. This distinction matters because a single unit's rFP already reflects weapon physics correctly through the counter design process. Applying compression to a single unit would understate its firepower. The compression is only needed when multiple units combine, because linear summation of rFP values would otherwise allow massed fire to produce guaranteed eliminations making the dice irrelevant. An earlier draft used an rFP threshold of 6 to trigger strip use — this was removed in v0.2 because it conflated the single-unit vs. combined-fire distinction with an arbitrary numerical threshold, creating ambiguity.*

E.7  Why 1d6 + 1d8 + 1d12
-------------------------


*Design note: An earlier draft (v0.1–v0.9.1) claimed the 1d6+1d8+1d12 combination produces a right-skewed curve. This was incorrect — the sum of independent symmetric dice is symmetric regardless of die sizes (skewness = 0, verified computationally across all 576 outcomes). The mixed sizes flatten the peak and widen the spread but do not skew it. The correction matters because it clarifies where the realism actually lives: the dice model within-engagement variance (aim, luck, exposure at the instant of fire), which is plausibly symmetric, while the circumstance modifiers supply the asymmetry of real outcomes. A skewed randomizer would impose the same tail on a point-blank ambush and long-range harassing fire alike — less accurate, not more. The three different dice are retained for their practical virtues: players immediately know which die is which, no identical dice to sort, and each die remains individually usable for subsystem rolls (morale, spotting, dispersion).*

E.8  The Skulking Fix — Exposure System
---------------------------------------


*Design note: In Advanced Squad Leader and similar games, a unit can fire on its own turn and then move back into cover before the opponent can respond. This skulking behaviour has no historical basis — a unit that exposes itself to fire remains exposed until it physically reaches cover. The Exposure system addresses this by separating exposure state from action timing. A unit that takes a Move and Fire action receives an ASSAULT marker and is Exposed. The Exposed condition persists until the unit spends a Move action to reach cover. The non-active player may spend 1 RP at any point while the unit is Exposed to fire at it. The unit cannot declare itself unexposed — it must earn cover by moving to it.*

E.9  Recovery at Start of Turn, Not End
---------------------------------------


*Design note: Placing recovery at the start of the turn rather than the end creates an exploitation window. A unit suppressed late in Turn 1 attempts recovery at the start of Turn 2. If it fails, the opponent gets a full turn's first impulse advantage against it while it is still suppressed. This models the real tactical value of suppressive fire — it doesn't just reduce the target's effectiveness, it creates a window of vulnerability the attacker can exploit before the target shakes it off. End-of-turn recovery would eliminate this window entirely.*

E.10  Fixed Reduction (Rear Face Stats)
---------------------------------------


*Design note: Many games use a single step-loss marker or simply halve front face values. With Deepest Regret... calculates rear face stats independently from a reduced TO**&**E. A Grenadier squad that loses its MG42 crew does not have half a Grenadier squad — it has a fundamentally different weapon mix with a different range profile and different tactical utility. The rear face encodes this correctly. The computational cost (more counter variants to design) is justified by the accuracy gain and the counter itself becoming a self-contained tactical information card.*

E.11  Weapon Counters and the MOBILE Marker
-------------------------------------------


*Design note: Independently crewed weapons (HMG teams, mortars, AT guns) need to represent the transition between moving and firing states. A single flip is insufficient because the weapon has four states: mobile-full crew, deployed-full crew, deployed-reduced crew, and destroyed. Two counter faces plus one MOBILE marker covers all four states with physical pieces already in the game. The deploy/limber action costing 1 AP and prohibiting fire in the same impulse reflects the real time cost of setting up and breaking down crew weapons.*

E.12  CI Does Not Mean Dead
---------------------------


*Design note: The term Combat Ineffective was chosen deliberately over Eliminated. WWII infantry data consistently shows approximately 25% killed in action, 60% wounded and evacuated, 10% captured or missing, and 5% dispersed or fled. A unit that receives a CI result on the game table represents a unit that has ceased to function tactically — not a pile of corpses. The Casualty Track, recovery rolls, and dispersed rally rules all flow from this design principle. Campaign play becomes more historically textured when players understand that their broken units may return, and that aggressive play that produces CI results without time to recover will compound into a losing campaign.*

E.13  The Long Range Cap
------------------------


*Design note: At very low effective rFP (3 or less after all modifiers), the dice can produce any result from the threshold table — including casualties and elimination — purely from variance. This is historically wrong. Harassing fire at extreme range suppresses and occasionally pins; it does not routinely cause casualties. The cap at rFP ≤ 3 truncates the result table to Pinned maximum, reflecting the physical reality that degraded long-range fire lacks the precision and energy to reliably cause casualties.*

E.14  Close Assault Simultaneity
--------------------------------


*Design note: Both the Grenade Phase and Entry Fire Phase of close assault resolve simultaneously for both sides. This models the reality that close combat is mutual — the attacker does not get free shots while the defender sits still. Historically, assault on a prepared position was extremely costly to both sides. The simultaneous resolution ensures that a determined defender can inflict significant casualties on the attacker even in defeat, discouraging casual close assaults without fire preparation.*

E.15  Prisoner Handling
-----------------------


*Design note: Most wargames ignore prisoners entirely or treat them as automatic removals. In practice, WWII prisoner handling was a genuine tactical burden — guards had to be detailed, movement was constrained, and unsecured prisoners were unpredictable. The guard requirement, movement restrictions, and escape mechanics add historical texture without complex rules. The Intelligence Point reward for securing prisoners gives capturing enemies strategic value beyond tactical elimination, encouraging players to invest in guard units rather than simply shooting everything.*

E.16  Recovery Window Framework
-------------------------------


*Design note: Recovery opportunity is scenario-driven rather than fixed. A campaign scenario set hours after the previous engagement should not allow the same recovery as one set three days later. The Recovery Window value in the scenario parameters gives the scenario designer explicit control over this. The scenario outcome modifier (loser drops one step) creates compounding consequences for losing — a losing force fights the next battle without recovery time, which is historically accurate and produces differentiated campaign trajectories.*

E.17  Serialised DISPERSED Markers
----------------------------------


*Design note: A face-down counter in a hex cannot tell a player which unit is dispersed there without picking it up — which is impractical during play and creates a memory burden. Serialised DISPERSED markers (GER-01, SOV-02, etc.) solve this by creating a physical link between the hex and the matching numbered box on the Casualty Track. The player places the marker in the hex and the counter in the corresponding box. At any point during play — including when the opponent is deciding whether to spend AP accepting surrender — the exact unit, its strength state, and its quality are visible on the track without touching anything on the map. The serialisation also prevents ambiguity when multiple dispersed units exist simultaneously.*

E.18  Movement Derived from Impulse Duration
--------------------------------------------


*Design note: Rather than setting movement allowance independently and hoping it felt right, M2 was derived from the physical duration of one impulse. One game turn is approximately 3 minutes; with 8 impulses per turn that is roughly 22 seconds per impulse. At tactical double time (200 yards/minute) a squad covers approximately 73 yards in 22 seconds — just under 2 hexes at 40 yards per hex. This grounds the movement allowance in the same physical timeframe as the fire resolution, ensuring both mechanics describe the same slice of real time.*

E.19  Careless Movement as Risk/Reward
--------------------------------------


*Design note: Careless movement exists because tactical reality includes soldiers moving at different vigilance levels depending on perceived threat. Troops who believe they are safe behind their own lines move quickly and noisily. The mechanic gives players a genuine choice: +1 hex of movement at the cost of -2 CON and a free enemy spot attempt. The free spot attempt (no RP cost) means careless movement is always risky if enemy units are present — it cannot be made safe by the opponent having exhausted their RP. This prevents the mechanic from being gamed.*

E.20  Physical Hidden Information System
----------------------------------------


*Design note: Hidden unit systems in wargames typically require either a referee (unavailable for two-player games), an honour system (gameable), or a screen between players (limits interaction). The covered chart system solves all three problems. The physical cover (cup, opaque token) prevents retroactive position changes without trust or a referee. Both players can see how many hidden units exist from the number of covered slots — neither side can pretend to have no hidden forces. The blind markers on the map maintain spatial presence without revealing contents. The system was designed specifically around physical game components rather than digital solutions.*

E.21  Dummy Markers and Information Decay
-----------------------------------------


*Design note: The dummy system models how real intelligence works. A unit that disappears creates uncertainty that decays over time. The free hidden impulse gives the owning player a brief window to make that uncertainty immediate and real — three markers appear where one was, and the opponent cannot know which is real without spending resources to find out. CONTACT markers formalise the decay: Fresh (you saw it this turn), Recent (one turn ago), Cold (two turns ago, removed). After two turns without contact the intelligence is worthless. This forces continuous active reconnaissance rather than marking a position once and treating it as known forever.*

E.22  FIXED Units and the Ambush Window
---------------------------------------


*Design note: FIXED units that fire and disperse receive a free hidden impulse because the ambush scenario creates a genuine information gap. When an ambush fires, the target is absorbing casualties, going to ground, and trying to identify the threat direction — not carefully observing where the ambush went. The +2 rFP surprise bonus on the first FIXED fire reflects the target's failure to use cover effectively when not expecting fire. These two bonuses together make ambush positions genuinely dangerous: one powerful surprise shot followed by immediate disappearance into three-marker uncertainty. The choice to sit tight vs fire and disperse creates a real tactical decision — staying put means a follow-up shot is possible but the position is now known; dispersing maximises deception but sacrifices the follow-up shot.*

E.23  CMD Rating as Unified Leader Stat
---------------------------------------


*Design note: Early design used separate Leader Quality tiers (Poor/Regular/Veteran/Elite) that fed into multiple derived values. CMD 1-3 replaces the abstract quality label with a single concrete number that simultaneously determines AP contribution, command radius, and implicitly anchors the other stats. Three steps rather than four was a deliberate simplification — the difference between veteran and elite leaders shows in RAL, ASL, and OBS values, not in a fourth CMD tier. This keeps the counter readable and the formulas simple while preserving meaningful differentiation between leader types.*

E.24  RAL Threshold vs Roll Bonus
---------------------------------


*Design note: Most wargame rally systems add a leader bonus to the recovery roll (e.g. +2 to the dice). RAL works the opposite way — it sets the target number the unit must meet. This inversion was deliberate. A roll bonus scales linearly and can produce automatic results even for poor leaders. A target number creates a more nuanced curve — a good leader with RAL 2 makes recovery nearly automatic for any unit with Morale 4+, while a poor leader with RAL 5 barely helps with suppression and cannot reliably rally pinned units. The RAL system also makes leader quality intuitively readable on the counter: lower number = better leader, which matches how threshold values work elsewhere in the game.*

E.25  Leader Casualty Roll
--------------------------


*Design note: The 1d6 roll when a hex takes a casualty (1-2 = leader hit, 3-6 = subordinate) was set at roughly 1-in-3 chance of leader casualty. WWII platoon and company officer casualty rates were disproportionately high — officers led from the front, were targeted by snipers, and were often the most exposed person in an advance. However a 50/50 chance would make leaders too fragile to invest in tactically. The 1-in-3 rate creates genuine risk without making leaders disposable. Players who concentrate leaders will eventually pay a price; players who keep them back lose the coordination benefits. This tension produces historically appropriate leader placement decisions.*

E.26  Inspire Action — Sustained Fire
-------------------------------------


*Design note: The Inspire action (leader spends 1 AP to give adjacent unit one extra fire action) exists because historical accounts consistently describe officers personally maintaining fire discipline under pressure — literally standing beside gun crews to keep them firing when they would otherwise seek cover. Mechanically it is expensive: the leader's entire activation for one extra fire action on one unit. But at critical moments — suppressing a threat long enough for another unit to close — that extra fire action can be decisive. It also creates an interesting risk: the leader must be visible and adjacent to use Inspire, which exposes them to the 1-in-3 casualty check if that hex is fired upon.*

E.27  Why Morale Break is Separate from Combat Results
------------------------------------------------------


*Design note: The existing combat result track (Suppressed → Pinned → Casualty → Broken) models physical attrition. The morale break system models psychological collapse. These are genuinely different phenomena — a unit can break psychologically after light physical casualties if it witnesses enough stress, or it can absorb heavy casualties and hold. Separating the two systems allows both to produce historically accurate outcomes. A unit breaking from cascade after its leader is killed is not the same as a unit broken by concentrated MG fire, and the recovery rules reflect this — psychological breaks recover better because the men are physically intact.*

E.28  Cascade Threshold Calibration
-----------------------------------


*Design note: The cascade threshold of 5 was deliberately set so that veteran units are essentially immune (Morale 6 + minimum roll 1 = 7, always passes) while green units face genuine risk (Morale 3 + roll needed ≥ 2 — fails on a 1 only). The cascade is not designed to be devastating in isolation — it is designed to be dangerous in combination. Multiple simultaneous breaks compound the cascade checks, and this is where historically catastrophic collapses emerge from the system naturally. The threshold was calibrated so that a single break almost never cascades into a general rout, but three breaks in one turn frequently do.*

E.29  Force Morale Factor Values
--------------------------------


*Design note: The force factors (0.3–0.6) were derived from historical unit cohesion data. An elite force at factor 0.6 can lose 60% of its units before the first Force Morale check triggers — consistent with documented SS and Guards unit performances in defensive engagements. A green force at factor 0.3 checks at 30% losses — consistent with conscript unit performance where a third of the force breaking would trigger general disintegration. The advancing threshold (each passed check raises the bar by 1) models how a force under pressure gradually passes a point of no return — early checks are passed easily but later ones become progressively more likely to fail as the force shrinks and the dice remain the same.*

E.30  Break vs Rout Distinction
-------------------------------


*Design note: The Break/Rout distinction exists because units in different tactical situations behave differently when their morale fails. A unit pinned in a building cannot flee — it collapses in place, potentially capturable. A unit in the open with a clear escape route flees — it becomes a routing counter that the owning player must manage, spending AP to move it away from the enemy each turn. The routing counter represents the unit still being present on the battlefield but out of control — a real phenomenon in WWII where routing soldiers would run through adjacent positions, spreading panic. The cascade rule captures this contagion. Routing is not just a CI shortcut — it is an active drain on the AP economy and a morale contagion risk.*

E.31  Sealed Fire Mission Slips
-------------------------------


*Design note: The sealed slip solves the retroactive fire mission problem without requiring a referee or honour system. A player who says 'I called that in two impulses ago' with no written record is claiming something unverifiable — the opponent has no recourse. The slip creates a physical commitment at the moment of declaration. Both players see the slip exist; neither sees its contents until arrival. This preserves the historical fog of war — you know fire is coming, not where — while making cheating physically impossible. The slip also serves as an AMO tracking record, reducing bookkeeping errors.*

E.32  Ammunition Fog of War
---------------------------


*Design note: Tracking mortar ammunition openly creates a metagame where the opponent adjusts behaviour the moment base AMO is exhausted — 'he's out, I can move freely now.' Real soldiers never knew exactly how many rounds an enemy mortar team had. The secret bonus AMO (1d6-1 rounds above base) and the extended ammunition table both serve the same purpose: the opponent never knows whether the mortar has stopped because it is out of ammunition or because the owning player made a tactical decision. A player might deliberately stop firing early to deceive the opponent into thinking the mortar is exhausted. The table also means that even the owning player faces uncertainty past base AMO — they know the bonus but the table creates genuine chance of running dry at a bad moment.*

E.33  Per-Hex Smoke Dissipation
-------------------------------


*Design note: Smoke dissipating uniformly by fire mission would produce a cleaner marker system but misrepresents how smoke behaves. Real smoke is affected by local air turbulence, wind variation, terrain, and heat — it clears unevenly. Per-hex independent dissipation rolls mean that a smoke screen can develop gaps even while still mostly intact. A player planning to cross under smoke cover faces a genuine decision about whether a gap-riddled thinning smoke screen is still sufficient. The tactical uncertainty this creates is worth the minor bookkeeping overhead of rolling per hex.*

E.34  Flat Mortar rFP
---------------------


*Design note: Mortars do not use the ⬡h -f falloff notation because their accuracy-at-range is handled by the dispersion system rather than by FP reduction. A mortar round that arrives on target at 1000 yards is as lethal as one at 200 yards — the difficulty is hitting at range, not the lethality of the round itself. Separate systems for separate phenomena: dispersion handles accuracy degradation, blast rFP handles what happens when the round arrives. This avoids the awkward situation of a mortar having extremely long range with the falloff formula producing near-zero FP at maximum range, which would understate its danger if it actually lands on target.*

E.35  Range Measurement Correction (v0.6.1)
-------------------------------------------


*Design note: The original range measurement rules (v0.1 through v0.6) stated range is measured 'inclusive of neither' firer nor target hex. This is inconsistent: if neither endpoint is counted, adjacent hexes have zero hexes between them — which would make adjacent range 0, not 1. The rule was internally contradicted by the stated adjacent range of 1 and the same-hex range of 0. The boundary-crossing definition adopted in v0.6.1 resolves this cleanly: range equals the number of hex boundaries the line of fire crosses. Same hex = 0 boundaries = range 0. Adjacent = 1 boundary = range 1. This definition was queued for correction after v0.4 but missed in v0.5 and v0.6 updates.*

E.36  Penetration Curve Mirroring rFP Falloff (superseded)
-----------------------------------------------------------


*Design note, original (v0.1–v0.9.x): Using the identical ⬡h -f notation for penetration as for rFP was a deliberate consistency decision — the same formula, the same calculation procedure, no new mental model required.*

*Superseded: a full re-derivation of the penetration physics from primary ballistics sources (velocity-at-range via the DeMarre equation, slope multipliers fitted per ammunition nose shape) showed real penetration curves are not well-approximated by the same linear per-hex falloff used for rFP — the fitted curves are power-law in velocity, not linear in range. Range-band PEN values (Rule 17.3.1), curve-fitted from attested historical data points rather than a generic linear formula, replace the falloff notation. The consistency goal (no new arithmetic at the table) is preserved a different way: players still just read a row and compare two numbers, they simply read the row directly rather than computing it via ⬡h -f subtraction.*

E.37  Split Hull/Turret AV, AV-vs-Capped/AV-vs-Tungsten (supersedes "Composite AV and Slope-Baked-In Approach")
-----------------------------------------------------------------------------------------------------------------


*Design note, original (v0.1–v0.9.x): a single composite AV per arc, baking in a fixed 60/40 (front) or 70/30 (side/rear) hull/turret area-weighting at design time, avoided giving players trigonometry to do at the table.*

*Superseded: keeping slope/quality calculations off the table remains essential and unchanged. But a single blended number can't represent two things that turned out to matter: (1) which profile a given shot actually hits is a per-shot question, not a fixed ratio — resolved instead by the Gunnery Roll (Rule 18.1a), which allocates Hull vs. Turret per shot based on range and the same dice already used for hit resolution; (2) capped and tungsten rounds have measurably different slope sensitivity against the same plate, and uncapped AP differs from both — a single AV number cannot represent all three simultaneously. The counter now prints two profiles (Hull, Turret) each with two AV values (vs. Capped, vs. Tungsten) — more printed numbers, but each one is still just compared directly against a printed PEN value, with no arithmetic added at the table. HEAT uses neither column — a small universal reference table (Rule 17.2.7) applied to raw thickness instead, since HEAT's effective resistance doesn't depend on the attacking projectile's diameter the way kinetic AV does.*

E.38  TRAV Rating and the TRAVERSED Marker
--------------------------------------------


*Design note, original (v0.1–v0.9.x): tracking exact turret facing with a separate marker was rejected because it adds a geometric puzzle to every fire action. TRAV rating alone — a simple number capturing how much of the clock a turret can cover from its current facing — was judged sufficient.*

*Refined, not reversed: the TRAV rating's reasoning still holds for what it was designed to solve (how far can this turret reach this turn) and is unchanged. What it didn't capture: once a turret genuinely does traverse to engage a flank target, it is exposed to that flank at that angle for as long as that remains true — a real tactical fact with no bookkeeping cost, because Rule 17.4.3 already establishes that turret facing resets to forward between fire actions. The TRAVERSED marker (Rule 17.5.5) captures exactly this window — placed when a shot requires off-forward traverse, removed the instant the vehicle fires again or at the next Recovery Phase — without requiring players to track turret position continuously the way E.38 originally worried about. It answers a narrower question (which arc does a hit against the Turret profile land on, while the marker is present) than full turret-position tracking would, at effectively zero added cost beyond what TRAV already requires the player to declare.*

E.39  Graduated Vehicle Damage Mirroring Infantry
-------------------------------------------------


*Design note: Using the same four-state damage progression (Suppressed/Pinned/Casualty/Eliminated) for vehicles as for infantry was a consistency decision that also happens to be historically accurate. Tank hits produced a spectrum of outcomes: crew shock from near-misses and non-penetrating hits, functional degradation from partial penetrations, mobility or gun kills from solid hits, and catastrophic destruction from full penetrations into ammunition or fuel. The two Casualty sub-states (MOB KILL and GUN KILL) are the only vehicle-specific addition — they reflect the real distinction between a tank that cannot move but can still fight and one that can move but has lost its main armament.*

E.40  Bail-Out and the Infantry Support Requirement
---------------------------------------------------


*Design note: The infantry support morale trigger (threshold 6 when infantry support eliminated within 2 hexes) is the mechanical enforcement of combined arms doctrine. Historically tank crews were acutely aware of their vulnerability to infantry AT weapons when unsupported — Panzerfaust teams, satchel charges, magnetic mines, and close assault all became immediate threats without infantry screening. The bail-out mechanic means a player who advances tanks without infantry faces a genuine game consequence, not just a theoretical tactical error. The buttoned-up isolation rule (Pinned vehicles cannot see cascade failures) adds a second dimension — isolated crews are more vulnerable because they cannot see the tactical picture deteriorating around them.*

E.41  Penetration Value Reliability Warning
-------------------------------------------


*Design note: The preliminary penetration and armour values in Section 17.3 were originally derived from recalled historical figures that could contain errors — the Sherman 76mm was initially cited at a flat PEN 16 base but this appears to have overstated the M62 APC round's performance relative to Aberdeen data. This class of error is exactly what the project's calculation tool (`counters/armor_calc/`) now exists to prevent for any gun it covers: every PEN/AV value it produces is a curve fit to attested calibration data points, cited to source chapter and page, with a confidence tier (fitted/interpolated/rough) printed alongside it rather than presented as equally certain. For the 13-vehicle roster and guns already run through that tool, treat its output as the current values — not the hand-recalled figures this note originally warned about. Any vehicle or gun NOT yet run through the tool remains exactly as uncertain as this note originally described, and should be treated as a starting point pending the same treatment, not assumed reliable by association.*

E.42  HEAT Weapons as Tactical Equaliser
----------------------------------------


*Design note: Giving Panzerfaust PEN 14 (flat) means it penetrates virtually every 1943-era vehicle from any angle. This is historically correct and was a deliberate design choice. The Panzerfaust was a tactical revolution precisely because it gave individual infantrymen the ability to destroy any tank — the constraint was range (0-4 hexes for the Panzerfaust 60, 80-160 yards). This range constraint is the entire tactical problem: infantry had to close to ranges where they were extremely vulnerable to tank MG fire in order to use the weapon. The system enforces this — tanks are lethal at range, Panzerfausts are lethal at close range. This is exactly why combined arms tactics evolved: tanks needed infantry to screen AT threats; infantry needed tanks for fire support. Both dependencies are mechanically real in this system.*

E.43  Scenario Design as a System Layer
---------------------------------------


*Design note: Scenario design guidelines were included in the rules document rather than a separate booklet because they are part of the game system — not an afterthought. The Force Morale calculation, Recovery Window, and FIXED unit placement rules are mechanical elements that must be set correctly for the game to produce historical outcomes. A scenario designer who ignores force ratios or sets an impossible turn limit has broken the simulation as surely as using incorrect unit stats. The checklist in Rule 22.10 formalises the quality bar — every scenario that passes the checklist should produce a playable, balanced engagement with historically plausible outcomes.*

E.44  Player Aid Card Design Principles
---------------------------------------


*Design note: The player aid card was designed to eliminate all rulebook lookups during normal play. Every action that a player takes at the table — fire resolution, spotting, morale checks, vehicle combat, turn sequence — should be resolvable from the card without opening the rules. The card uses colour coding (amber for suppression band results, red for casualty band, blue for vehicle penetration bands) to allow players to find the relevant row visually rather than reading every entry. The resolution strip is given the most prominent position because it is consulted most frequently. The two-sided format separates combat resolution (Side 1) from procedures and reference (Side 2) — players who are in the middle of resolving combat rarely need the procedure reference simultaneously.*

E.45  Title: With Deepest Regret...
-----------------------------------


*Design note: The title was selected after an extended design process exploring rally cries, slang terms, dying wishes, and condolence letter language. The criterion was a phrase that captured the game's core philosophical commitment — historical accuracy without glorification, equal treatment of all nations, acknowledgement of the human cost of the war at squad level.*

*Design note: With Deepest Regret... was the universal opening of death notification letters in every nation that fought in World War II. German officers wrote Mit tiefstem Bedauern. American telegrams read We regret to inform you. Soviet notifications carried S glubokim sozhaleniem. The same words, the same moment, in every household in every country across six years of war.*

*Design note: The ellipsis is intentional and essential. It implies the sentence that follows — which every reader completes themselves. The men on the counters are that sentence. The game does not glorify what they did. It models it with accuracy and respects what it cost.*

*Design note: The title takes no sides. A German mother and a Soviet mother and an American mother all received a letter that opened with these words. They were all just people. Their sons were all just people. The ordinary soldiers of every nation were not evil — they were young men doing what their countries asked of them, most without full knowledge of what they were serving. The tragedy of World War II is universal. This game is for those people.*

E.46  Counter Design Philosophy — Information on the Counter
------------------------------------------------------------


*Design note: The decision to maximise information on the counter rather than in tables was driven by play experience with existing systems. ASL and similar games require constant cross-referencing between counters, chapter tables, and the rulebook during normal play. This creates lookup chains that interrupt tactical thinking and slow the game. The solution is to encode all combat-relevant data directly on the counter at design time, accepting higher counter complexity in exchange for lower table complexity at the table.*

*Design note: The rFP ⬡h -f notation encodes the complete fire resolution formula on the counter. A player never needs to look up a weapon's effective range — they calculate it from the counter values using the falloff formula. Vehicle counters carry all three facing AV values and the complete AP penetration curve. The player who picks up a vehicle counter knows everything they need to resolve combat with it. No vehicle data tables are required during play.*

*Design note: The counter size decision (0.75 inch or 1 inch vs the 0.5 inch industry standard) follows directly from this philosophy. More information on the counter is only useful if the information is readable. At 0.5 inch, encoding three fire lines, armour values, penetration curves, and action stats would require font sizes too small for comfortable reading. At 0.75 or 1 inch the same information is comfortable at arm's length. The SVG format means this size choice has no production cost — the same vector file prints at any size.*

*Design note: The hex size matching guideline (Rule 1.5.5) was added because counter size and hex size must be coordinated. A 1 inch counter in a 9/16 inch hex cannot be picked up without disturbing adjacent counters. The recommended 1.25 inch hex for 1 inch counters allows comfortable stacking of 2-3 counters with room to pick up individual pieces — a practical requirement that is easy to miss at design time but immediately obvious at the table.*

E.47  Sniper Long Range Cap Exemption
-------------------------------------


*Design note: The long range cap (maximum result Pinned when effective rFP ≤ 3) was designed for volume fire scenarios — many weapons degraded to marginal effectiveness at extreme range. A sniper with rFP 3 has low rFP by design because they fire one precise round, not because their effectiveness has degraded with range. Applying the cap to snipers would mean a sniper could never cause a casualty beyond point blank range — the opposite of their historical role. The exemption is tied to deliberate targeting to preserve the design intent: a sniper suppressing an area with unaimed fire is subject to the cap; a sniper taking an aimed shot at a specific leader is not. The two modes of sniper use produce different mechanical outcomes, which is correct.*

E.48  Sniper Psychological Suppression
--------------------------------------


*Design note: The area movement penalty from a known sniper CONTACT marker (-1 M#, no careless movement) was included because historical accounts consistently describe this effect. Entire units changed their movement patterns when a sniper was suspected in an area. The movement penalty is not caused by the sniper firing at you — it is caused by the knowledge that one is present. This is modelled by the CONTACT marker persisting after firing and the penalty applying to all friendly units within range. The effect ends when the marker ages to COLD and is removed or the sniper is revealed and eliminated — representing the position being either too old to be relevant or the threat being confirmed and dealt with.*

E.49  Engineer Capability Strip System
--------------------------------------


*Design note: Engineer capabilities use the same EXPENDED strip system as single-shot AT weapons (Panzerfaust). This was a deliberate component economy decision — one strip type covers all expendable capabilities across all unit types. The strip is placed over the specific capability icon when expended, leaving other capabilities visible and usable. Players can see at a glance which capabilities remain available without consulting a separate tracking sheet. The visual of a covered icon is more immediately readable than a checkbox or tally on a record sheet, particularly in the heat of a game turn.*

E.50  Engineer Building Assault Bonuses
---------------------------------------


*Design note: The engineer close assault bonuses (G# +2 grenade phase, +2 rFP entry fire, +1 morale checks) reflect documented differences in building clearance effectiveness between line infantry and combat engineers. The Stalingrad factory district, the Siegfried Line bunkers, the Atlantic Wall fortifications — all required specialist engineer assault techniques that produced meaningfully better results than standard infantry assault. The bonus applies only when engineers are the assaulting unit, not when they are providing supporting fire, because the advantage is in their close-quarters doctrine and equipment, not in their ranged fire capability.*

E.51  Result Threshold Recalibration (v0.9.2)
---------------------------------------------


*Design note: The result thresholds were rebanded in v0.9.2 after computing exact outcome probabilities against the 1943 test counters. Under the original bands (Suppressed 0–3, Casualty at 9+), a single LMG line at effective rFP 7 produced a casualty or worse 85.6% of the time against a squad in open ground and 41.8% against an entrenched squad — inverting the stated design intent of Rule 8.5.3. The rebanded thresholds restore the intended profile: verified across a weighted mix of typical engagement circumstances, aggregate outcomes are approximately 42% Suppressed, 33% Pinned, 18% Casualty, 4% Casualty+Suppressed, 0.6% Broken. Open ground remains genuinely lethal (roughly 50% casualty-or-worse against an MG at effective range) — cover is the decision that matters. The suppression penalty (−2 rFP) remains tactically meaningful under the new bands: at a typical net of −4 it roughly halves the firer's casualty-or-worse probability.*

E.52  Recovery Threshold Recalibration (v0.9.2)
-----------------------------------------------


*Design note: The original recovery thresholds (Suppressed 4, Pinned 7) made suppression recovery automatic for any unit with Morale 3 or higher — the minimum roll of 1 plus Morale 3 already met the threshold. Since every unit in the game has Morale 5 or 6, suppression never persisted past a Recovery Phase and Pinned recovery succeeded 5 times in 6. Status effects were transient theater; casualties were the only lasting currency — the opposite of the suppression-first philosophy. The v0.9.2 thresholds (Suppressed 8, Pinned 10, Casualty+Suppressed 11) make recovery probabilistic and morale-differentiated: regulars (Morale 5) recover from suppression 67% of the time and from pinning 33%; elites (Morale 6) recover 83% and 50%. Fire superiority now produces persistent effects worth exploiting, and leader CMD bonuses — which can push recovery to certainty — become genuinely valuable. The routing rally threshold rose in step (9 to 12) to preserve the design principle that routed troops rarely self-rally: alone, a regular unit rallies from rout only on a natural 6; with a CMD 3 leader in radius, on a 4+.*

E.53  TRAV Arc Geometry (v0.9.2)
--------------------------------


*Design note: The original TRAV table listed 6/4/2/1 hexsides covered, with TRAV 1 described as "front arc only" while the front armour arc was defined as a single hexside — a contradiction, and the 4- and 2-hexside arcs could not be drawn symmetrically about the facing arrow, forcing an arbitrary choice of which sides were covered. The v0.9.2 ladder (6/5/3/1) is the unique set of contiguous arcs symmetric about the facing arrow: all six; all but the rear hexside; the front hexside and its two neighbours; the front hexside alone. No diagram or player choice is required, and the firing-arc terminology is now fully independent of the armour-facing terminology in Rule 17.5.*

E.54  Dispersion Distance as D3 (v0.9.2)
----------------------------------------


*Design note: The original flat 1d6 dispersion distance made a 6-hex miss (240 yards) as likely as a 1-hex miss. Documented WWII medium mortar dispersion at typical combat ranges is on the order of 25–50 metres — one hex, occasionally two. D3 (1–3 hexes) keeps misses meaningful, keeps friendly fire a real risk on danger-close missions, and stays within historical dispersion envelopes, while using the existing d6 rather than introducing a new die. The direction roll's compass mapping (N, NE, SE, S, SW, NW) is exactly the neighbour set of a flat-top hex grid, so map orientation is now stated explicitly rather than implied.*

E.55  Gunnery Roll — Unifying Hit/Miss and Hull/Turret Allocation
--------------------------------------------------------------------


*Design note: The original vehicle system had no hit/miss step at all — every declared shot was assumed to land, and only the penetration outcome (Rule 18.2) was resolved. Adding one, and unifying it with Hull/Turret hit allocation into a single roll (Rule 18.1a), was chosen over two separate systems because a large aim-error result is naturally a miss and a small one naturally lands on a specific profile — the same underlying dispersion logic produces both outcomes. The unification reuses the exact 1d6+1d8+1d12 combination already rolled for every other attack (Rule 8.5.1, see E.7) rather than inventing new dice: two thresholds (Miss, Hull) are derived algebraically from that combination's own exact 576-outcome distribution, so "roll ≥ X" means precisely what the printed number says at whatever resolution the dice allow (24 distinct probability steps between roughly 0.17% and 100%). Below that floor a shot reads as an automatic miss rather than an unrollable threshold — this matters at long range, where a raw hit-probability calculation would otherwise round to a number smaller than any single die combination can represent. Crew Quality reuses the existing Morale stat via a fixed band mapping rather than adding a new printed value, and the crossing-target/follow-up-shot adjustments (18.1a.6-18.1a.7) deliberately trade a small amount of precision for staying within one printed table under all circumstances — no second table, no arithmetic, no roll modifier to remember.*

E.56  Shatter Gap — Optional Rule, Not Core
-----------------------------------------------


*Design note: a kinetic round that badly over-penetrates a plate can shatter its own nose before completing penetration and fail — a real, sourced phenomenon (documented in historical firing tests against Tiger E armour) explaining otherwise-puzzling reports of "should have penetrated but didn't." It resolves as a deterministic override to Non-Penetrating Hit (Rule 18.2a) rather than a new roll, matching how confidently the source material states the effect. It is scoped as an optional/advanced rule specifically because it is genuinely counter-intuitive to a newer player — "why didn't my clearly superior shot penetrate" is a legitimate question with a non-obvious answer, and the base game should not require every table to resolve that question to play a scenario.*

E.57  Schürzen — HEAT-Only, Not a General Armour Bonus
------------------------------------------------------------


*Design note: standoff skirt armour (Schürzen) defeats HEAT by forcing the shaped-charge jet to begin forming well before it reaches the real armour, degrading it before impact — a mechanism with no equivalent for kinetic rounds, which fail (if at all) by plugging or nose-shatter, not jet dispersion. Schürzen is therefore modelled as a flat PEN reduction applied to the attacker's HEAT round specifically (Rule 18.2b), never as a bonus to the defender's AV — deliberately, so it cannot be mistaken for "more armour" against kinetic attacks, where it provides no benefit at all (and, per the same physics governing spaced armour generally, arguably none-to-slightly-negative). The 50% figure is a wargame-design convention (recognisable from Advanced Squad Leader's own Side Skirts vehicle note) rather than a project-source-cited measurement — flagged in Rule 18.2b's own text as the one mechanic in the vehicle-combat system built on general engineering knowledge rather than a specific citation.*

E.58  Hit Location — Precomputed Scatter, Not a Live Roll-and-Diagram
------------------------------------------------------------------------


*Design note: Bird & Livingston's Appendix 15 "Shot Placement System" gives real dice-to-displacement mathematics but no per-vehicle component diagrams — the book's own worked example determines what a hit struck by eyeballing a diagram, which does not exist for any vehicle in this project. Two ways to use the sourced math were considered: have players roll the dice live and consult a printed vehicle diagram each time a Casualty occurs, or precompute the distribution once per vehicle/profile/range/crew-quality and print a single small threshold table, the same "zero lines" pattern used for the Gunnery Table and the Shatter Gap Table elsewhere in this system. The precomputed approach was chosen — real per-vehicle zone geometry (driver, gunner, loader, commander, engine, transmission, ammunition, fuel, each independently positioned and classified Mobility/Gun/Neither) feeds a Monte Carlo simulation of the sourced scatter equations once, at design time, rather than requiring a diagram lookup at the table every time a tank is hit. A genuine finding surfaced by modelling real zone geometry rather than a flat Front=crew/Rear=mobility assumption: Tiger (and most WW2-era German and American medium/heavy tanks) mounted the transmission at the front of the hull with the engine at the rear, so a Hull Front hit is a real mobility risk, not just a crew risk — a cruder abstraction would have missed this. The pilot deliberately covers only two vehicles (Tiger I, Sherman M4A1) and only their Front arc — Sherman M4A1 chosen specifically as the dry-stowage variant, since its sponson ammunition placement is a historically real case where location mattered (the "Ronson" reputation), a meaningful test of whether the mechanic captures something true rather than being mechanically elaborate for its own sake. Vehicles without a built Hit Location Table keep the original free-choice rule (17.1.1) until their own table exists — this is an incremental replacement, not a flag day.*

E.59  Cross-Reference Notes — a "See Also" Convention
-------------------------------------------------------


*Design note: The Section 20/21/22 reorder (moving Snipers and Engineers ahead of Scenario Design Guidelines) surfaced a recurring risk: a rule mentions another rule's concept by name — the Sniper deliberate-targeting exception, say — and only a reader who already knows exactly where to look benefits from the citation. Appendix F's index helps, but only if the reader thinks to go there. The convention adopted going forward: whenever a rule's text depends on or is depended on by a rule elsewhere in the document, add a small indented italic note directly beneath the specific numbered rule — "See also: Rule X.Y (short description)" — at both ends of the reference, not just the end that happens to mention it first. This is applied opportunistically as chapters are touched, not as a one-time retrofit of the whole book; Rule 8.7.4, Rule 12.9.1a, and Rule 20.2 carry the first three notes as a working example.*

E.60  Mixed-Interval Fire Grouping — Bounded by the Smallest ⬡h
---------------------------------------------------------------


*Design note: Rule 8.3.4 originally banned combining fire from units with different ⬡h values outright, even though the ban was only mathematically required for the same-hex shortcut (Rule 8.3.3) — the general per-unit method (Rule 8.3.2) already computes each unit's own falloff independently before summing, so matching ⬡h was never actually necessary there. Two ways to relax it were checked by direct calculation before choosing either: allowing the group only while every unit stays within the smallest ⬡h in the group (so none has taken any falloff yet) produces the exact same sum the general method already gives — zero skew, just a narrower eligibility window. Forcing the whole group onto the smallest unit's degrade curve at any range was also checked and rejected: at range 9, a mixed ⬡4/⬡5 group's true per-unit sum (11) came out 18% higher than the forced-curve number (9), and by range 20 the gap grows to 4x — the longer-⬡h units get punished on a curve steeper than their own printed weapon, purely for being grouped with a faster-degrading one. Rule 8.3.4a adopts the first approach only.*

E.61  Rally Points — A Destination, Not a Roll Bonus
----------------------------------------------------


*Design note: Before this rule, a leader had zero mechanical ability to help a Dispersed unit — the existing Rally Action (Rule 12.6) is explicitly scoped to Suppressed or Pinned units only. Rally Points close that gap narrowly: they change where a successful Rule 10.5.4 roll sends the returning unit, not whether or how easily it succeeds. The roll itself stays exactly 1d6 + Morale − 2 vs. threshold 8, with no leader bonus of any kind — even though this surfaced a real, pre-existing asymmetry (ordinary Suppressed/Pinned recovery already gets a CMD-adjacency bonus, Rule 5.2.6, that Dispersed rally has never had). That asymmetry is deliberately not closed here; a roll-odds change is a distinct, separable idea for later. Travel to the Rally Point is fully abstracted — the DISPERSED marker never moves, and nothing tracks a path between the dispersal hex and the Rally Point — matching how this project already avoids marker-movement bookkeeping everywhere else in the system. A placed Rally Point is not indestructible, however: Rule 12.6a.3 removes the marker immediately and permanently the moment an enemy unit occupies its hex. This revises the rule's original position (which held the marker "always valid... regardless of subsequent events in that hex, including enemy occupation") for two reasons. First, it is the more intuitive result at the table — a rally point physically overrun by the enemy no longer functions as one, whatever the travel abstraction says about the hexes in between. Second, it resolves cleanly what had been an open gap (see below): an enemy-occupied hex can never be a live Rally Point candidate at the moment Rule 10.5.4 is resolved, because occupation would already have destroyed it, so the two rules can no longer collide.*

*Design note (resolved gap): Rule 3.5.1 caps a hex at 3 combat units, with no exception for a unit returning from the Casualty Track (Rule 3.5.2 exempts only leaders). Under the rule's original "always valid, even under enemy occupation" wording, a Rally Point hex already at that limit when a Dispersed unit's rally roll succeeded had no defined resolution — a gap deliberately left unresolved and flagged here for whoever played it out first. The enemy-occupation change above closes it by construction rather than by patching around it: a marker cannot survive to be a rally destination in a hex the enemy holds, so the stacking-limit collision this note originally flagged can no longer arise.*

E.62  CI Resolution — No Unit Left Undecided at Scenario's End
--------------------------------------------------------------

*Design note: Rule 10.5.4's failure clause ("removed from the Casualty Track permanently for this scenario") and Rule 10.7.3's blanket claim that "CI units are tracked on the Casualty Track and may return to play through between-scenario recovery rolls" could not both be true as written — Rule 13.3's DISPERSED zone recovery table implied real between-scenario odds for exactly the units 10.5.4 said were already gone. Routing units had an even larger gap: Rule 10.6 defined how a unit rallies (10.6.6, 10.6.7) or escapes off-map (10.6.5), but nothing at all for a unit still routing when the scenario simply ends. Rather than patch each gap independently, both are resolved the same way: a Dispersed or Routing unit now has exactly two possible endings by the scenario's close — it returns to play, or it is captured (Rule 11.2a). Administrative capture needs no accepting enemy unit and no AP, extending the abstraction Rule 10.7.2 already established (a CI counter has "ceased to function as a tactical element," not a literal, trackable path of individuals) to how that status resolves — the game does not need to know which enemy unit rounded up which stragglers, only that the unit's fate is settled by the time the guns fall silent. It is deliberately exempt from Rule 11.3's guard requirements and Rule 11.4's escape attempts, both of which assume a live in-scenario guarding relationship that an administratively captured unit, by definition, never has; without that exemption an unguarded prisoner would attempt to escape almost every remaining turn, undoing "captured" almost as soon as it happened.*

*This removes the "Dispersed Recovery" path from Section 13 entirely — the 13.2 Recovery Window table's Dispersed Recovery column, 13.3's DISPERSED zone recovery table, and 13.2.2's narrower "attacker loses ground" capture clause are all superseded, since a Dispersed unit is never left in the Casualty Track at a between-scenario boundary anymore. Broken units are deliberately untouched: a Broken unit still leaves the map to a genuine holding zone with no in-scenario resolution path, so 13.3's between-scenario recovery remains exactly the mechanism it needs. The existing voluntary capture (Rule 11.2, an adjacent enemy unit spending 1 AP to accept a Dispersed unit's surrender) is not made redundant by this — a Dispersed unit can keep re-attempting its rally roll every Recovery Phase until it succeeds or fails once, so an enemy player who wants to deny that chance outright, rather than wait for a possible failure, still has a reason to spend the AP and capture it proactively.*

*Fix (whole-branch review): the final review of this branch surfaced two integration gaps neither task-scoped review could see. First, Rule 12.10.2's "captured or evacuated" wounded-leader outcome routed to the DISPERSED zone — a path this same branch had just orphaned by removing DISPERSED-zone between-scenario recovery. Resolved by splitting the roll: an evacuated leader still goes to the BROKEN zone (Rule 13.3's recovery table is untouched and still covers it), while a captured leader now goes through Rule 11.2a like any other capture, matching the word "captured" to the zone it actually means. Second, Rule 10.6.9's "still Routing when the scenario ends" trigger could be misread against Rule 15.5.7's "all remaining units are considered routing for scenario resolution purposes" on a Force Morale collapse — a scoring abstraction for determining the victor that, before this branch, carried no further consequence. Rule 10.6.9 is now scoped explicitly to units carrying an actual ROUTING marker (Rule 10.6.2), so a force's collapse does not itself mass-capture its surviving units.*

E.63  One Action Per Activation — Resolving the AP Economy Contradiction
------------------------------------------------------------------------

*Design note: v0.9.2 carried two incompatible models of what 1 AP buys. Rule 6.1.2 said an activated unit "may take all of its available actions... within that single impulse," while the Rule 6.3 table priced each action at 1 AP and Rule 6.5.2 had F3 units placing FIRE 1, 2, and 3 "on separate impulses" — impossible under the old Rule 6.1.3's once-per-turn activation limit. The full-activation model was rejected because it collapses the impulse structure: a unit that does everything at once gives the opponent a single reaction window against its whole turn, and the FIRE 1/2/3 marker progression, the interleaved opportunity-fire economy, and the Interrupt reaction all presume actions spread across impulses. The adopted model is the one the marker system was already built for: 1 AP = one activation = one action, a unit may be activated in multiple impulses per turn, and its per-turn totals are bounded by its markers (one MOVED, up to F# FIREs). AP scarcity (Rule 5.3.3) remains the real throttle — a force with AP 4 chooses between concentrating three fires on one squad or spreading single actions across three squads, which is exactly the command-attention trade-off the AP system exists to model.*

E.64  Reaction Timing — Two Windows and Interruption Points
-----------------------------------------------------------

*Design note: the original impulse sequence opened its only reaction window "after the action executes" (old Rule 5.5.2), yet three rules required reacting earlier: pre-action opportunity fire (old 5.5.5), Defensive Fire against a declared close assault, and the mid-move MP-loss/stop effects of Rules 7.5.4–7.5.5, which are meaningless if fire can only land after the move is complete. Rather than delete those rules — the pre-emptive and interdiction reactions are most of what makes the RP economy interesting — the impulse now defines three explicit timing moments: a declaration window (respond to what the enemy is about to do; resolves first and can cancel the action), interruption points during movement (one per hex entered, where Rules 7.5.3–7.5.5 apply exactly as written), and a post-action window (respond to what just happened). Interrupts were also unexecutable in the old text: Rule 6.2.1 only let the non-active player spend RP, so nobody could legally react to an interrupting action even though old 6.4.3 said reactions "trigger normally." Rule 6.4.3 now swaps roles fully for the interrupting action. The one-Interrupt-per-action limit (6.4.4) and the no-interrupting-an-Interrupt rule together bound the recursion: the deepest legal chain is action → interrupt → simple reactions, which ends.*

E.65  Movement Allowances — One Table of Record
-----------------------------------------------

*Design note: Sections 3.3 and 7.1.3 carried two different movement-allowance tables — every infantry M value differed by 1 (rifle squad M1 vs M2, leader M2 vs M3), with Appendix D siding with the stale Section 3 values. Rule 7.1.2's derivation (tactical double time of 200 yards per minute over a 20–25 second impulse covers roughly two 40-yard hexes) is the reasoned anchor, the counter pipeline already emits M2 for squads, and the movement-cost table in 7.2 was priced against M2 throughout ("Dense woods 3 — exceeds M2"), so Section 3.3 and Appendix D now match Section 7.1.3. The one deliberate exception is the sniper team: Section 20's stat block (M1, "snipers do not run") and the old Section 3 value both said M1 with a stated rationale, against 7.1.3's lone M2 — so snipers are M1 everywhere and 7.1.3's sniper row now carries Section 20's rationale. Section 7.1.3 is the table of record for movement allowances; Section 3.3's copy exists for counter-reading convenience and must be changed in lockstep.*

E.66  The Morale Modifier — Making 1d6 Quality Checks Failable
--------------------------------------------------------------

*Design note: v0.9.2's quality checks rolled 1d6 + the full Morale value (3–6) against thresholds of 5–8. Checked case by case, nearly every one was inert: a veteran unit (Morale 6, minimum roll 7) could never fail any Section 15 morale check, cascade checks were auto-passed by green troops and better, and the rout self-rally at threshold 12 was arithmetically impossible for an unled regular unit even though 10.6.7's own text claimed it succeeded "on a roll of 6" (6 + 5 = 11 < 12). Three sign inversions compounded this: the suppressed modifier lowered the threshold (compounding stress made checks easier), 15.1.2 resolved multiple triggers at the "lowest (hardest)" threshold (lowest is easiest), and the melee table set Casualty + Suppressed at an easier threshold than plain Casualty. The fix generalises the idiom Section 13.3 already used: every 1d6 quality check now rolls 1d6 + Morale modifier, where the modifier is Morale − 5 (militia −2, green −1, regular +0, veteran/elite +1), against a threshold in honest 1d6 space, and the suppressed modifier is +2 to the threshold. Recovery thresholds (5.2.4: 8/10/11 → 3/5/6) and the dispersed rally (10.5.4: 1d6 + Morale − 2 vs 8 → 1d6 + modifier vs 5) are pure renumberings — the pass rates 5.2.5 documents are preserved exactly, because the transform is affine. The break-check triggers (15.1.1: 7/6/5/6 → 4/3/2/3), cascade (5 → 2), melee (8/6 → 3/4, inversion corrected), and rout self-rally (12 → 6, making 10.6.7's worked example true) are recalibrations: a regular squad now holds a Casualty + Suppressed check 50% of the time instead of 83%, and break/rout — which this section's own preamble calls how most WWII engagements ended — can actually occur to regular and veteran troops. Section 13.3's banded modifier table is superseded by the same formula (its Morale 3 and 4 rows shift by one point of modifier); E.61's description of the dispersed-rally roll is superseded by the renumbered, odds-identical form.*

E.67  Leader Rally — RAL as a Real Threshold
--------------------------------------------

*Design note: under the old roll (1d6 + full Morale vs RAL 2–5), a regular unit's minimum result was 6 — no leader in the game could fail to rally it, the Suppressed/Pinned distinction the 12.6.4 effect column described did not exist in the formula, and the mid-turn Rally action strictly dominated the Recovery Phase thresholds, contradicting E.24. Printed RAL values are deliberately unchanged (Poor 5 / Regular 4 / Veteran 3 / Elite 2 — the 12.11 roster and the rear-face +2 wound penalty stay valid); the roll becomes 1d6 + Morale modifier vs RAL − 1 for Suppressed and RAL + 1 for Pinned. The ±1 split around the printed value gives the two-state distinction the effect column always claimed, and anchors CMD 2 / RAL 4 exactly at the standard Recovery Phase thresholds (3/5) — a regular leader buys timing, not odds; better leaders buy both, and a poor leader's mid-turn attempt is genuinely worse than waiting for the phase. The rout rally at a leader's hex (10.6.6) uses RAL + 1 — as hard as rallying a pinned unit, and now failable, where before it was automatic for every unit in the game.*

E.68  Engineer Skill Rolls — The Thresholds Were Right All Along
----------------------------------------------------------------

*Design note: the Section 21 breach thresholds (wire 3 up to reinforced bunker 7) and the 5/7 skill-roll targets were graded sensibly — in 1d6 space. Rolled as 1d6 + full Morale with engineer Morale 6, the minimum result was 7 and every threshold in the section, including "designed to resist assault", was met automatically; the only live gate was the under-fire auto-fail (21.2.5). Under the Morale modifier (E.66) every printed threshold is kept unchanged and simply works: a veteran engineer squad (modifier +1) clears wire on 2+ and forces a bunker entrance only on a natural 6. The engineer stat block's "Morale 6–7" is corrected to 6, matching the 21.9 roster's actual values. Morale 7 itself is retained as a printed specialist tier (veteran snipers, senior leaders — modifier +2, added to the 15.2.1a table): Section 20's claim that a Morale 7 sniper "recovers from suppression automatically" remains exactly true under the new arithmetic (1d6 + 2 vs threshold 3).*

E.69  Vehicle Crew Checks — Live Numbers, and the Bail-Out Inversion
--------------------------------------------------------------------

*Design note: every roster vehicle carries crew Morale 5 or 6, so under the old 1d6 + Morale roll the 19.1.2 triggers at thresholds 5 and 6 were auto-passed by the whole roster, the penetrating-hit check at 7 failed only on a natural 1 for regular crews, and the 19.6.6 cascade at 5 was a no-op — Section 19 was state-tracking (consecutive buttoned turns, infantry-within-2-hexes monitoring) feeding checks that could not change an outcome. The bail-out table was also inverted against its own rationale: Pinned at threshold 6 was strictly easier to pass than Suppressed at 8, while the Notes column said isolation "accelerates the decision to bail." Under the Morale modifier (E.66) the triggers renumber to 4/3/2/3/3 (parallel to the infantry scale in 15.1.1), bail-out becomes Suppressed 3 / Pinned 4 — the Pinned check now genuinely the harder one — and the vehicle cascade uses the same threshold 2 as infantry cascade. A side benefit: 19.4.3's previously undefined "crew quality modifier" for capture attempts now has a natural definition — the CREW counter's Morale modifier.*

E.70  Japan's Force Factor — Corrected Direction
------------------------------------------------

*Design note: the Force Morale check triggers when the CI-plus-routing count reaches unit count × factor (15.5.3), so a LOW factor triggers the collapse check earliest — the elite factor of 0.6 correctly lets an elite force absorb 60% losses before its first check. Japan's printed 0.2 therefore made Japanese forces the most brittle in the game (a collapse check after 20% losses, sooner than 1941 Soviets at 0.25) — the exact opposite of the "rarely routed, fanatical holds" characteristic the same row describes; the "threshold almost never reached" annotation shows the factor was written as if low meant resilient. Corrected to 0.8: a 10-unit Japanese force does not face its first collapse check until 8 units are CI or routing, above even elite Western formations, which is the intended encoding of fanatical cohesion. Note for scenario designers: 22.3.3's factor list still spans only 0.3–0.6; national factors outside that band (0.25, 0.45, 0.8) come from this table.*

E.71  Fire Grouping Unified; the Step-Up Rule Bounded
-----------------------------------------------------

*Design note (supersedes E.60, and the "grouping requirement" clause of E.5): v0.9.2 made grouping optional ("may be combined", old 8.3.1) while old 8.8.2 stepped the combined result up once for every additional separate attack that "beat the target's defence". Because the three-dice roll's minimum is 3, any attack at net modifier −3 or better produces at least Suppressed — so "beats the defence" was near-automatic, and splitting fire strictly dominated grouping at every defence value tested: two rFP-7 LMG lines against Defence 8 scored Casualty-or-better 66% grouped but 97.9% split, and five weak separate attacks produced an automatic Broken with no dice relevant. The Long Range Cap had no step-up language, so four capped rFP-2 attacks broke a squad 70.7% of the time — the exact outcome 8.7.2 calls rare. Three changes close this: (1) grouping is now mandatory and universal for a single Fire action — the ⬡h restriction is deleted outright, because the per-unit-calculate-then-sum method (8.3.2) never needed matching intervals (E.5's own analysis showed the restriction was only ever required for the same-hex summation shortcut, which keeps its same-⬡h condition); 8.3.4/8.3.4a and their narrow eligibility window are gone, and a squad's own mixed fire lines combine freely. (2) Separate attacks now arise only across genuinely different resolution paths (declared fire vs reaction fire, sniper deliberate targeting, Interrupts), each paid for with its own AP/RP and fire action. (3) The step-up itself is bounded: only an additional attack whose own result is Pinned or better steps the combined result, at most two step-ups total, and the combined result can never exceed the most severe result any single contributing attack was permitted to inflict — capped fire stays capped. The Resolution Strip is also corrected to be the identity through 7: the old low rows (3→4, 4→5) amplified combined weak fire above its arithmetic sum, contradicting the strip's own compression rationale, and made Resolution FP 3 unreachable for groups. The round-down rule for unlisted sums, which previously existed only in a stray copy of the strip orphaned at the end of Section 21 (now deleted), lives in 8.4.3 and Appendix A where players will actually find it.*

E.72  Finishing the Millimetre Migration
----------------------------------------

*Design note: the AV/PEN system was rescaled from the original 1-point≈10mm scale to real millimetres, but three consumers of the old scale were never converted, and Rule 18.12 itself documented one of them ("the direct millimetre conversion of the original system's flat 'PEN 14'") without fixing the rule players actually use. As written in v0.9.2: every infantry AT weapon in Rule 18.9 bounced off every vehicle in the roster (Panzerfaust "PEN 14" vs a 102.0mm Tiger hull), a Suppressed vehicle's "-2 PEN" penalty was a dead modifier against mm-scale AVs (it meant -20mm), and Rule 18.2's ±3 outcome margins — formerly ±30mm — left a 6mm total Contested window while PEN moves 8-10mm per range band, making 20 of the 22 verification matchups binary auto-pen/bounce and Rules 18.3/18.4 nearly unreachable. All three are converted (18.9 in mm throughout, -20 PEN, ±10mm margins — comparable to real penetration scatter at these thicknesses). The 18.9 HEAT rows also shed their "-1 rFP per 2 hexes" notes: a falloff on rFP is meaningless in a PEN-vs-AV resolution that "always hits", and the accuracy degradation it once represented is modelled by the hard range limits (17.3.3). Finally, 18.12 is re-run following the game's own band-read procedure (17.3.1 — an earlier revision computed PEN at exact ranges, which players never do, so at least three of its printed verdicts contradicted what the table would produce in play), with 17.3.1 now naming the 0m point-blank row explicitly for sub-250m shots. Three verdicts changed under the corrected procedure: T-34 vs Panzer IV H turret at 400 yds (Bounce → Non-penetrating hit), Panzer IV H vs KV-1S turret at 500 yds (Bounce → Non-penetrating hit), and T-70 vs Panzer IV H (Bounce/Auto → Contested/Bounce, using the APBC-family, 45mm-diameter AVs note (e)'s own fix provides).*

E.73  Hit Location Conditioned On Hitting
-----------------------------------------

*Design note: the first build of the Hit Location Monte Carlo (E.58) tallied the raw scatter pattern and classified any sample outside a named zone as "Neither" — including samples that missed the vehicle entirely. But Rule 18.6a only consults this table after the Gunnery Roll has already confirmed a hit and Rules 18.5/18.6 have already produced a Casualty, so the distribution must be conditional on the shot striking the plate. Unconditioned, only ~44% of samples landed within the Tiger hull-front zone extent at 500m (26% at 1000m), so the printed table downgraded 88–99% of penetrating Casualty results to Pinned, and the "Neither band grows with range" behaviour the old 17.7 prose described was an artifact of counting clean misses, not physics. classify_hit_location() now rejection-samples against a per-profile silhouette (the zone geometry's bounding box — the honest conditioning region for exactly the plate area the project has modelled; silhouette_bounds() in formulas.py), and the regenerated hit_location_output.csv shows the corrected picture: a confirmed Tiger hull-front Casualty is a mobility hit ~30–33% of the time, nearly independent of range and attacker crew quality. That near-independence is itself useful intelligence for a future simplification — one row set per profile on a player aid would lose almost nothing — but this change deliberately keeps the table's existing shape and only fixes the distribution it prints.*

E.74  Hidden Information — Concealed Assignment
-----------------------------------------------

*Design note: the covered chart (E.20) solved retroactive tampering — a counter under a cover cannot be swapped after the fact — but not observation at the moment of hiding. As written in v0.9.2 the owning player visibly placed the real counter into a numbered slot, covered visibly-empty slots for the dummies, and moved the real blind marker before the dummies were even placed; a face-to-face opponent learned which number was real by simply watching, and the three-marker uncertainty E.21 describes never existed for a single impulse. The fix is procedural, not componentry: assignment happens out of the opponent's sight (a small screen, the table edge, covers face-down in hand), the whole group of covered slots and the whole group of numbered map markers are each committed simultaneously, and every marker in a group obeys the same placement envelope (anywhere the real unit could legally have reached), so neither chart handling, placement order, nor marker geometry distinguishes real from dummy. The cover still provides the tamper-evidence it always did; concealed simultaneous commitment now provides the secrecy the covers were being credited with.*

E.75  ASSAULT Marker Symmetry and the Exposed Escape Clause
-----------------------------------------------------------

*Design note: two rules disagreed with the marker system they depended on. Old 7.3.4 had fire-then-move place a FIRE 1 marker AND an ASSAULT marker while 6.5.3 said ASSAULT replaces FIRE 1 — and gave the two orderings different remaining rights (fire-then-move forbade further fire; move-then-fire allowed FIRE 2/3) even though both leave the identical marker state, so the distinction depended on unrecorded history. The orderings are now fully symmetric: ASSAULT records one move and one fire whichever came first, remaining fire actions are available in either case, and no FIRE marker accompanies it. Separately, 6.6.1's escape from Exposure ("spends a Move action to reach cover +2") was unreachable — the only route into Exposure is the Assault action, whose marker forbids moving again — and 7.3.5 gave a different duration ("remainder of the reaction window") than 6.6.1 ("end of turn"). Both statements were half-right: Exposure now ends with the unit's own reaction window when the action ends in cover +2 or better (7.3.5's duration, for the case it was written for), and lasts to end of turn otherwise (6.6.1's duration, for a bound that ends in the open). The unreachable Move-escape clause is deleted.*

E.76  Close Assault — Defensive Fire, Stacks, and One Kind of CI
----------------------------------------------------------------

*Design note: Section 9 was written for a duel — one attacker, one defender — while the stacking rules allow three combat units per hex, and it never integrated three things the rest of the system already promised. (1) Rule 6.4's Defensive Fire reaction triggered on a declared close assault but had no slot in Section 9's sequence; 9.1.5 gives it one, in the declaration window, with Suppressed/Pinned on the assaulter cancelling the assault under exactly the Rule 5.5.2 cancellation everything else uses. (2) The standard result table's 23+ result is Broken (BROKEN zone), but 1.3 and 10.5.1 define close-assault CI as Dispersed (different zone, recovery, and capture consequences) — 9.3.6's "(Broken or Dispersed)" hedge showed the ambiguity. 9.1.6 resolves it once for the whole section: any CI inflicted during close assault is Dispersed. (3) "Dominant fire line", used since the first draft of 9.4, is now defined (highest printed rFP — at range 0 every line is at full value, so the printed number is the comparison). The new 9.8 covers stacks with a deliberately small ruleset: one summed attack per side, resolved against the best opposing Defence, results allocated by the receiving player with no doubling-up until everyone has one, per-unit morale and withdrawal, and leaders/weapon counters sharing the hex's fate through the existing administrative-capture rule rather than new machinery. Also closed: the withdrawal eligibility loophole (an ASSAULT marker records a fire but old 9.2.2 only checked for FIRE markers), and the double-jeopardy question of whether a melee Casualty triggers both 9.6 and 15.1 (it triggers 9.6 only).*

E.77  One Ammunition Mechanism; Mortars Against Steel; Fire That Resolves
-------------------------------------------------------------------------

*Design note: three fire-support gaps closed together. (1) Mortar (and by 20.1.3, sniper) ammunition had two mechanisms both claiming to govern total supply: a secret 1d6−1 bonus recorded privately at setup, and the extended ammunition table rolled per mission past base AMO. They cannot coexist — a player holding +5 secret rounds could be forced dry by a first extended-table roll of 1, making the secret bonus meaningless, or vice versa. The extended table wins: it provides hidden, variable supply with zero private bookkeeping and preserves the bluffing 16.3.4 describes. The tungsten plumbing reference in 17.3.2 now points at the same mechanism. (2) Mortars vs vehicles (16.7.8): open-topped and unarmoured vehicles take blast like infantry; closed AFVs take a crew check (threshold 3, 4 for 120mm-class) or button up Suppressed — mortars never touch the Section 18 penetration tables, which matches both the physics at these calibres and the desire to keep indirect fire out of the armour engine. (3) The BURNING hex attack was unexecutable ("no roll — just apply result thresholds to margin": with no roll, the margin against any squad was permanently negative, so burning did nothing). It now rolls the standard dice at Resolution FP 3, cap-exempt, with no cover modifier — the fire is inside the cover. The flamethrower's own summary (21.5.1 "ignores cover") is aligned to its detailed rule (21.5.3, cover halved). Housekeeping in the same pass: 16.4.1 admits to five modes, the delay column names the real calibre classes on the roster (50–60/81–82/120mm), effective ACC ≤ 0 is an automatic disperse rather than a dead roll, and 16.8.2's adjustment ACC is anchored to the mission's effective ACC, mode modifier included.*

E.78  Elevation LOS — Crests as Geometry, Not Terrain
-----------------------------------------------------

*Design note: v0.9.2 printed "Reverse slope +4" as a static hex terrain type, but whether a hex is a reverse slope depends entirely on where the observer stands — the same hex is a forward slope from the other direction. As written, a unit in that hex was immune to all direct fire from every direction (and, since LOS is symmetric, arguably could not fire out), and the LOS rules offered no way for elevated units to see over anything: 4.4.2 blocked LOS through any "hill mass" hex unconditionally while referencing a "crest hex" defined nowhere. The replacement (4.4a) is the minimal relational model: printed elevation levels, crest hexsides between differing levels, blocking when an intervening hex is at or above both endpoints, never-blocking at or below the lower endpoint, and a one-hex crest blind zone for intermediate levels — the ground immediately behind a crest is defiladed from beyond it, which IS the reverse-slope defence, now per-firer instead of absolute. Full continuous blind-zone trigonometry was considered and rejected: the one-hex rule captures the tactical decision (tuck in directly behind the crest or be seen) at zero table arithmetic. "Reverse slope" survives as a named position (4.4.4) keeping its +4 cover against the indirect fire that can still reach it, so 16.7.4's step-down still works unchanged. The undefined "grazing fire" row in 4.3 gains its definition (crossing crest hexsides at the firer's own level, −1 each). In the same pass, 4.3.5's old floor ("minimum 1 regardless of penalties") is aligned with the newer Rule 8.2.5: effective rFP at 0 or less means no contribution — the old floor quietly guaranteed that no amount of smoke or forest could ever fully stop fire, which contradicted both the smoke rules' purpose and 8.2.5.*

E.79  Hexside Terrain — Walls and Hedgerows Defined
---------------------------------------------------

*Design note: walls and hedgerows were priced as crossings in the movement table — clearly linear features — while Section 4 only defined whole-hex terrain, so nothing said which occupant, against which attacker, earned their +2 cover, and Appendix B compounded it by giving hedgerow a flat hex cost of 2 as if it were hex terrain. Rule 4.1.3 defines hexside terrain properly: cover applies only against fire whose line crosses that hexside into the unit's hex (directional cover is the entire point of a wall), it does not stack with the hex's own cover (use the better — a wall along a heavy building adds nothing), movement is a crossing surcharge, and the intervening penalty is per hexside crossed. Hedgerow's movement cost is recast from "2" to "+1 to cross", which leaves the common case arithmetically identical (open hex entered through a hedgerow still costs 2 MP) while behaving correctly for every other hex type behind the hedge.*

E.80  Facing Arcs at Range — 60° Wedges
---------------------------------------

*Design note: 17.5.2 defined the armour arcs only for the six adjacent hexes, and nearly all vehicle gunnery happens at 5–60 hexes — a Tiger at 1,000 yards was in no arc at all. The arcs are now the six 60° wedges radiating through each hexside, extended to any range, which reduces exactly to the old adjacent-hex table at range 1 (so nothing already written changes) and matches how TRAV was already defined (by hexsides, which always extended). A 60° front was chosen over a 120° one deliberately: with a wide front, most long-range engagements resolve on Front armour and flanking manoeuvre barely pays; with a 60° front, oblique fire strikes Side armour at any range, making position and facing a live decision across the whole board — historically the difference between a Sherman platoon dying frontally to a Tiger and killing it from the flank. Spine ties resolve against the target (SIDE over FRONT, REAR over SIDE): the defender oriented their own facing, so ambiguity costs them, not the attacker.*

E.81  AV by Attacker Family; HEAT Reads Its Own Printed Value
-------------------------------------------------------------

*Design note: two related counter-data fixes. First, 17.2.3 sent uncapped AP to the AV-vs-Capped column, and gave Soviet APBC no legal AV at all (the roster's own T-70 fires it) — but the face-hardening correction is family-dependent (a penalty for capped noses, nothing for APBC, a bonus for the plate against uncapped AP), so the Capped figure understated the four face-hardened plates by 30–70% against those attackers. The pipeline's resolve_av() already computes the right numbers (E.72's own T-70 verdict used them); 17.2.3a now prints the footnote table for the four plates, at the same 75mm reference diameter the printed columns already use, and only there — everywhere else the Capped column is genuinely correct for all three families. Second, the at-table HEAT procedure was unexecutable: 17.2.4 asked players to multiply raw plate thickness (deliberately not on the counter) by an interpolated multiplier at an impact angle no rule computes. Its own justification was backwards — HEAT resistance depends only on the plate, making HEAT the one attack that is perfectly pre-resolvable per arc. The pipeline has emitted av_vs_heat_mm per plate from the start; it is now the printed third AV, HEAT attacks read it directly, and 17.2.7's multiplier table is demoted to designer reference.*

E.82  Hit Location Collapsed to One Row Per Profile
---------------------------------------------------

*Design note: the original table was 8 range bands × 5 crew qualities × 2 thresholds per profile — 160 numbers for two vehicles — keyed by the ATTACKER'S crew quality read off the TARGET'S table, built from one representative gun but keyed by any attacker's quality, and undefined when the penetrator was a Panzerfaust (no crew quality exists). E.73's conditioning fix revealed why none of that granularity earned its place: the conditional split moves only a couple of points across the entire grid (Tiger hull-front mobility 30.1–33.2% from 100m to 2500m, near-identical across qualities), because where a confirmed hit lands is a property of the plate's geometry, not of the shot's difficulty. The table is now one threshold pair per profile, computed at a representative mid-range engagement (500m, regular) and printed on the player aid card rather than the counter, and the attacker's identity — vehicle or Panzerfaust — is irrelevant at the table. Four rows now cover what 160 did.*

E.83  Vehicles as Soft Targets, Bogging, and Backing Up
-------------------------------------------------------

*Design note: four dangling vehicle mechanics grounded. (1) The ○— open-top symbol was defined in 17.1 and consumed by nothing; 18.6.2 carried a "−1 HE direct hit" modifier on a table HE had no path to reach; and vehicles have no printed Defence value, so nothing infantry-style could ever be resolved against them. Rule 18.8.5 gives soft and open-topped vehicles a class Defence (6 / 8 — a class constant, deliberately not a new counter stat) against HE, close-range small arms, mortar blast, and grenades; 18.8.6 routes HE against closed AFVs to the Non-Penetrating Hit table (+1 for 105mm+) — suppression, never penetration — and the unreachable −1 row is deleted rather than given a contrived consumer. (2) "Vehicles bog" appeared once, undefined; 17.6.2a makes it a real check (1–2 on entry to dense woods for tracked vehicles, freed on 4+ with a full activation, +1 with a towing neighbour). (3) No reverse-movement rule existed, so a StuG or SU-85 could only leave a firefight by pivoting its thin sides toward the enemy — historically exactly what casemate crews built their tactics around avoiding; 17.6.2b permits backing straight into the rear-wedge hex at double cost.*

E.84  Spotting Rebalanced; FIXED Units Reachable
------------------------------------------------

*Design note: two failures of the hidden system's outer loop. First, spotting succeeded on 1d6 + OBS − CON ≥ 0, so a Spot Action (+3) spotted a stationary unit in a building with certainty and 14.10.4 granted free rolls against EVERY marker in LOS — one 1 AP action swept the board of blinds and dummies, negating the chart, dummy, and CONTACT apparatus (and E.20/E.21's persistent-uncertainty intent) in a single impulse. The threshold is now 4+ and a Spot Action rolls against one chosen marker (further markers cost RP, still with the +3): the same building attempt succeeds 33% per action, so concealment decays under sustained observation instead of evaporating. Second, the CON table leaked truth through dummies — "stationary, not fired +2", "suppressed −1", "fired −3" depend on hidden unit state a dummy does not have, so the announced CON itself revealed whether a marker was real. Every CON modifier is now map-observable (the marker's hex, its watched movement this turn, scenario conditions), making a dummy's CON identical by construction to a real unit's; the fired/suppressed rows are deleted outright because those states cannot belong to a marker still on the map (firing auto-reveals, blast auto-reveals). Third, FIXED units were unreachable: every spot mechanic targets markers and FIXED units have none, and nothing handled an enemy walking into their recorded hex. 14.7.7 closes both: FIXED units cannot be spotted, and an enemy attempting to enter the recorded hex halts short while the ambusher is revealed with its surprise bonus intact. 22.8.5's "FIXED dummy markers" — a concept Section 14 never defined — becomes recorded decoy positions, which is what a scenario designer can actually give the defender.*

E.85  The Guard Economy Gets Its Missing Verbs
----------------------------------------------

*Design note: Rule 11.3.5 demanded 2 guards for 3–4 POW markers while the only way to become a guard was accepting a surrender (one marker on one unit) — the requirement was unsatisfiable, guard duty had no transfer or exit, and a player who consolidated prisoners was locked into escape rolls forever with no legal remedy. Escaped prisoners were worse: the POW marker vanished with "no campaign benefit to captor" and nothing said where the captured counters went, so escapes were pure downside for one side and irrelevant to the other — nobody had a reason to care about the guard rules at all. Three additions close the loop: prisoner groups are defined (POW markers stacked in a hex; guards cover from in-hex or adjacent, one group each), Assume Guard (1 AP) adds or relieves guards, and releasing is free but feeds the same escape table. Escapes now return the captured counters to the owner's BROKEN zone with a white marker — recoverable between scenarios — so guarding matters to the captor (campaign value at stake) and escapes matter to the owner (men coming back). The unruly result's scope is pinned down (the captor's units, in or adjacent, morale and recovery rolls, this turn).*

E.86  Functional Leaders and the Routing State's Precedence
-----------------------------------------------------------

*Design note: "functional leader" gated the AP formula (12.3.1), command status (12.4.1), rout rallies (10.6.6), and Force Morale checks (15.5.4) without ever being defined, and Section 12.9 handled only Casualty-or-worse results on leaders — what a Suppressed or Pinned result did to a leader, particularly one alone in a hex, was silent. 12.3.4 defines functional (on-map; not Eliminated/Evacuated/Captured/Routing) and takes a deliberate middle path for Pinned leaders: their CMD still feeds the AP pool — the battalion's command structure does not evaporate because one officer is face-down in a ditch — but nothing projects: no Rally, no Leader Actions, no CMD added to others' rolls until recovery. 12.9.4 keeps leaders out of the ordinary suppression churn while stacked (results go to combat units; the 12.9.1 allocation exists only for Casualty+) and exposes them fully when alone. On the receiving end of fire, 10.6.10 makes Routing the terminal status it was always described as: placing ROUTING clears SUPPRESSED/PINNED, the -3 Defence penalty is flat and unstackable, further Suppressed/Pinned results are absorbed, and routing units are exempt from Section 15 checks — a unit already fleeing cannot break twice, and its only decision points are the rally rolls.*

E.87  Campaign Framework — Honest TBDs and a Working Outcome Ladder
-------------------------------------------------------------------

*Design note: Section 13 admitted to being framework, but Sections 11 and 22 leaned on it as if it were finished: the campaign branched on five outcome grades no rule produced, 11.6.3 paid out "replacement points" that exist nowhere, the Resupply column resupplied nothing, "campaign turn" was undefined, and 13.5 promised an experience system with no rules behind it. The chosen posture (rather than inventing a full campaign economy without playtest grounding): define exactly what live rules already consume, and mark the rest TBD where players will actually read it. Defined: outcome grades map from the scenario's own end state (Force Morale collapse or double the loser's VP = decisive; other wins marginal; equal VP = draw), and a campaign turn is the interval between consecutive scenarios. Marked TBD in place: Resupply (13.2.2), replacement points (11.6.3's 3-point row is explicitly unavailable), and experience (13.5.2 — printed quality is fixed until designed). The 13.1 zone table is also rewritten to match the rules it summarises: BROKEN includes psychological breaks, off-map routs, and escaped prisoners; DISPERSED matches 10.5.1's face rule and is noted as always empty between scenarios (E.62); CAPTURED includes administrative capture — its dominant route. 13.3 scopes to the BROKEN zone (CAPTURED counters are the enemy's; rolling recovery for them was never intended) and carries the white-marker +1 inline. Intelligence Points become a one-time award per secured POW marker, matching E.15's "capture reward" intent — the per-campaign-turn income snowballed early captures into an ahistorical intelligence annuity.*

E.88  The Worked Scenario Example Now Follows Its Own Section
-------------------------------------------------------------

*Design note: 22.11 is the template scenario designers will copy, and it violated its own section four ways: the platoon leader was counted as a combat unit (against 22.2.2), Force Morale used a flat 0.45 instead of 22.3.3's weighted average (2×0.5+2×0.4 floors to 1, not 2), the setup zones sat 2 hexes apart against 22.9.3's 4-hex infantry minimum, and the printed 1.7:1 quality-adjusted ratio was unreproducible from 22.2.3's multipliers (the real figure is 5.0:3.5 ≈ 1.4:1). All four are recomputed in place with the arithmetic shown, and the honest consequence is kept rather than hidden: at 3–4 units both Force Morale values floor to the minimum, so the first CI triggers a collapse check — small engagements are brittle by construction, noted as such for designers. (22.3.3's factor list spanning only 0.3–0.6 while 15.6 assigns national factors outside that band was already noted in E.70.)*

E.89  A Graduated Long Range Cap
--------------------------------

*Design note: the flat cap (rFP ≤ 3 → maximum Pinned) created a cliff its own Rule 8.7.3 drew attention to: one point of intervening penalty — a crops hex — toggled a firer between "can never inflict a casualty" and the full result table including Broken. The cap is now two bands (rFP 1–2 → maximum Suppressed; 3 → maximum Pinned; 4+ uncapped), which grades the transition and slightly strengthens the cap's own story: fire degraded to a trickle can pin nobody, only keep heads down. Rule 8.8.5's combined-result ceiling follows the highest cap among contributing attacks. The sniper deliberate-targeting exemption (8.7.4) is unchanged.*

E.90  Rout Movement Executes Itself
-----------------------------------

*Design note (amends E.30's framing): E.30 described routing counters as an AP drain the owning player "must manage... spending AP to move it away each turn," but Rule 10.6.3 only applied "each time it is activated" and nothing compelled activation — parking a routing unit was free until end-of-scenario capture, which inverted the intent entirely (a routing unit became a safe way to bank a counter). Rather than force a full activation (which would let rout consume the AP pool of an already-collapsing force — a death spiral on top of a death spiral), rout movement is now self-executing: units not activated by the owner's final pass make their D3 move at no AP cost. The AP option survives as a timing choice — pay to control when in the turn the flight happens (before the enemy can position to exploit it), or pay nothing and let it happen last. Two related clarifications in the same pass: a HIDDEN leader's functions are enumerated (AP contribution and own-hex bonuses only; everything that projects requires visibility — shouting reveals the shouter), and 13.3.1 gives leaders their between-scenario reading of the recovery table (rear face = wounded face), with wounds healing in a Days+ window.*

E.91  Initiative Buys Tempo, Not Resources
------------------------------------------

*Design note: the initiative winner previously collected three benefits from one d6 per turn — acting first in every impulse, winning all reaction timing ties, and +1 RP. Acting first with an equal-or-larger reaction pool is already a strong position; the bonus RP compounded a single hot die into both tempo AND resources, and over a 4-turn scenario a streak of initiative wins could snowball hard for no decision either player made. The +1 RP is removed: initiative now buys tempo only (first action, timing ties), and both RP pools derive identically from AP. Giving the bonus RP to the LOSER (as reactive compensation) was considered and rejected — it inverts the incentive to win the roll and is unintuitive at the table; symmetric pools are the simplest fix that keeps the roll meaningful without letting it compound.*

E.92  The NCO Floor — Leaderless Is Crippled, Not Frozen
--------------------------------------------------------

*Design note: under AP = 1 + ΣCMD, a force whose leaders were all CI dropped to one action and one reaction per turn for the entire remaining scenario, regardless of how many squads still stood — a 6-unit platoon reduced to moving one unit per turn, with no floor and no in-scenario recovery path. If that was a morale-collapse model it duplicated Force Morale's job (Section 15.5 already ends scenarios when a force breaks); as an action economy it produced turns where nothing happens, which is a playability failure rather than a simulation. The NCO floor (5.3.3a) sets leaderless AP at 2 while at least 3 unbroken combat units remain: sergeants keep squads fighting locally even when the platoon net is dead, at half or less of a typical led pool (a single CMD 2 leader alone yields AP 3), so losing every leader remains among the worst things that can happen to a force without freezing the game. Below 3 unbroken units the old AP 1 stands — a remnant of one or two squads genuinely is beyond coordination, and Force Morale has usually ended the scenario by then anyway.*

E.93  The No-Miss Regime Is the Point
-------------------------------------

*Design note: the full-rules review flagged, correctly, that at net modifier ≥ −3 every attack produces at least Suppressed — 100% of the time — including at the system's own calibration anchor (an LMG line vs a squad in the open, net −1). With F2 units firing twice per turn, suppression markers churn constantly and the dice grade only severity. The option of widening the No Effect band was considered and deliberately rejected: it would invalidate Appendix C's verified probability table, every calibration anchor, and the tuning of every threshold set during the redesign — and, more importantly, it would break the model on purpose. At 40 yards per hex and 2–5 minutes per turn, a squad taking aimed automatic-weapons fire at effective range DOES go to ground essentially every time; what varied historically was whether it could still act, which is exactly what the Suppressed/Pinned/Casualty gradient measures. The identity is now stated in the rules themselves (8.5.3a: "fire suppresses, manoeuvre kills") so playtesters read the constant suppression churn as the engine working, not a bug — and so any future retuning of the bands starts from the knowledge that this property was chosen, twice.*

E.94  Correcting the Action Economy — Regular, Assault, and ROF
-----------------------------------------------------------------

*Design note (supersedes E.63 and E.75): E.63 resolved the v0.9.2 contradiction over what 1 AP buys (old 6.1.2's "all actions in one impulse" vs the per-action 6.3 table vs old 6.1.3's once-per-turn limit) with a model — one Move plus up to F# full-effect Fires, tracked by MOVED/FIRE 1-2-3/ASSAULT markers — that resolved the letter of the contradiction but not the designer's actual intent, which E.75 then compounded by making the ASSAULT marker fully order-symmetric. A design conversation on 2026-09-08 established what the game was always meant to do (recorded in full in* ``docs/superpowers/specs/2026-09-07-action-economy-redesign.md``\ *) and this note records the corrected rules and why the earlier fix missed the mark.*

*The corrected model has three parts. First, a unit's turn is either one Regular action at full effect (a full-M# Move, or one Fire at full effective rFP) — ending its turn immediately — or the Assault economy: up to two reduced part-actions (a 1-hex Assault Move, or an Assault Fire at half effective rFP) in either order, tracked by a single ASSAULT marker after the first and MOVED/FIRED after the second. This is what "assault fire, then move, marked moved/fired" always meant — E.63's model instead gave every unit a full-effect Move AND up to F# full-effect Fires per turn with no reduced-rate option at all, which is a materially more generous economy than intended and, worse, gave no mechanical reason to ever choose the weaker "assault" framing over ordinary actions.*

*Second, stationary machine guns are the deliberate exception to "one full-effect action, then done": ROF (Rate of Fire) lets a tripod-deployed HMG fire at full effective rFP three times in a turn and a bipod LMG (or other bipod/light-tripod MG) twice, provided neither has moved that turn — the pre-sighted or range-carded position is what buys the extra bursts. A machine gun that moves drops into the ordinary Assault economy like anyone else, one crewman working it off-hand at half rFP. This is genuinely new content; nothing in v0.9.2 or E.63 distinguished machine gun fire rate from any other unit's, so F3 HMG teams and F3 LMG teams (both printed identically) had no mechanical reason for their shared rate to mean anything different from a rifle squad's F2. ROF is deliberately a rules-text property for now, independent of the printed F# value, pending a full counter-data review — Rule 6.6.6 and Rule 3.3.2 both flag this in place rather than silently reinterpreting a printed stat.*

*Third, reactions (opportunity fire, defensive fire) are momentary and resource-limited rather than governed by a persistent Exposed/Firing Exposed condition. E.75's model had a unit's vulnerability outlive the action that created it — an Exposed unit could be shot at "at any point" until its own reaction window closed, or until end of turn in the open — which is exactly the kind of lingering token the designer wanted gone: "the action draws the fire... it's just a momentary thing." Under the corrected model, a reaction resolves at the Rule 5.5 timing point the triggering action itself creates and is gone once that window closes; the reacting player's only levers are RP and the reacting unit's own remaining part-action or ROF pip. This also does real design work: an assault-moving unit that reaches the open and is not shot at in that instant is not owed a second chance by a lingering marker, and a unit that spends both its part-actions (assault move, then assault fire) is stuck MOVED/FIRED in the open until the marker clears next Recovery Phase — full stop, with no in-between "exposed" bookkeeping. This is what removes skulking by construction rather than by a bolted-on penalty, matching Rule 1.1's original design promise ("skulking behaviour... eliminated by design") more directly than the Exposure system it replaces. Deleting Exposed and Firing Exposed also removes their own leftover inconsistency (Firing Exposed's -1 rFP modifier depended on tracking which position a unit had already fired from, state no marker recorded) rather than requiring a separate fix for it.*

*Housekeeping consequence: the retained moving-target opportunity-fire penalty (-2 rFP, formerly old Rule 6.6.7 and separately restated in Rule 7.5.2) is deduplicated into Rule 7.5 alone, its sole home; Rule 6.6 is repurposed for ROF weapons rather than left as a numbering gap. Voluntary withdrawal (Rule 9.2.2), which reads the marker set to determine whether the defender had "already acted," requires a completely fresh unit (no marker of any kind) — the new markers no longer distinguish a move from a fire once collapsed into ASSAULT, so the previous fire-specific carve-out could not be preserved exactly, and freshness is the right call for a defender's own decision to withdraw. Close assault eligibility (Rule 9.1.2) was drafted the same conservative way in this note's first pass but corrected the same day — see E.95.*

E.95  Close Assault Can Still Be Initiated From ASSAULT — With a Leader
------------------------------------------------------------------------

*Design note (amends E.94's closing paragraph): requiring a completely fresh unit to declare Close Assault was the wrong call for the initiator, unlike the defender's withdrawal decision beside it. The designer's actual intent, confirmed in the same 2026-09-08 conversation that produced the corrected action economy: a unit already carrying the ASSAULT marker (one part-action spent — an Assault Fire or a 1-hex Assault Move) can still initiate a close assault as its second part-action, but only under leader coordination — a leader present in the unit's hex, either directing that unit alone or as part of a multi-unit stack activation (Rule 6.1.1). Without that coordination, an ASSAULT-marked unit's second part-action is limited to an ordinary Assault Move or Assault Fire; it cannot spontaneously charge into melee on its own initiative after already having committed to something else this turn. A completely fresh unit is unaffected and continues to declare Close Assault freely, exactly as before — the leader-coordination requirement applies only to the ASSAULT-marked case. Rules 6.3.2 (the Close Assault row), 6.3.3 (a new Close Assault part-action row), and 9.1.2 (the two-path eligibility test) carry the corrected rule.*

E.96  Marker Consolidation — Deleting OPPORTUNITY
----------------------------------------------------

*Design note: a full-rules review of the physical marker set, following the action-economy correction (E.94–E.95), found the OPPORTUNITY marker to be a leftover from the pre-rewrite design rather than something the corrected rules ever place. Under the old Exposed/Firing Exposed model an opportunity-fire reaction was its own distinct thing, worth flagging separately; under the corrected model (Rule 6.2.3), a reaction resolves by marking the reacting unit exactly as though it had taken that action on its own turn — an ordinary Assault Fire (ASSAULT, or MOVED/FIRED if already ASSAULT-marked) or a ROF pip. Nothing in the current rules text ever calls for an OPPORTUNITY marker to be placed; it survived only in the housekeeping lists (component table, Rule 5.2.2, Rule 6.5.4) that got carried forward unedited. It is removed from all of those lists and from the physical component count. This is a pure deletion, not a rules change — no rule ever depended on it having its own marker distinct from ASSAULT/FIRED/MOVED-FIRED.*

E.97  Marker Consolidation — One Physical Marker for MOVED/FIRED and CARELESS
---------------------------------------------------------------------------------

*Design note: Careless Movement (Rule 7.4) is only ever declared "when spending a Move action" — the Regular Move action of Rule 6.3.2, not the bounded Assault Move part-action of Rule 7.3, which has its own 1-hex cap and is covered separately. Since every Regular action ends a unit's turn as MOVED/FIRED except where its own rule says otherwise, and Rule 7.4 says otherwise for the M#+1 movement allowance without saying otherwise for the end-of-turn marking, a carelessly-moved unit is always MOVED/FIRED for that same turn, at the same time as it is CARELESS. The two markers therefore never need to be shown independently of each other — a unit is never MOVED/FIRED-but-not-CARELESS-when-it-should-be, or CARELESS-but-not-MOVED/FIRED. This makes them one physical component rather than two: a single two-sided marker, front face MOVED/FIRED (the ordinary case), back face CARELESS (which, being placed only alongside MOVED/FIRED, conveys both facts — done for the turn, and -2 CON — from one token). Both faces are removed together in the Recovery Phase like any other action marker (Rule 5.2.2). Rules 3.6 and 7.4.2 carry the consolidated marker; no other rule's timing or eligibility changes.*

E.98  Marker Consolidation — Composite Unit Status Moves to the Roster Sheet
---------------------------------------------------------------------------------

*Design note: the Composite marker (Rule 13.4.4) tracks a campaign-only condition — a unit formed by combining two half-strength counters during a Recovery Window carries -1 Morale until it survives one full scenario without being rendered CI. Unlike every other marker in Section 3.6, this state never changes mid-scenario, is set and cleared only between scenarios, and has no reason to sit on a scenario's physical counter mix at all — it is bookkeeping about which counter a unit currently is, not about anything happening on the map this turn. It is moved off the counter entirely and recorded instead on the unit's roster/OB sheet, the same place quality level and other between-scenario unit state already lives. This removes one physical marker type from the component list with no change to the -1 Morale penalty or its one-scenario clearance condition.*

E.99  Marker Consolidation — CONTACT Collapses to Two States
------------------------------------------------------------

*Design note: Rule 14.8.4 already states that CONTACT markers "have no game effect beyond conveying information age" — the three printed states (FRESH/RECENT/COLD) existed purely to let a player eyeball how stale a piece of intelligence was, not because the game treats a 1-turn-old contact differently from a 2-turn-old one. Since FRESH-vs-RECENT was never a distinction with a rules consequence, it collapses cleanly into one state (CONTACT), leaving COLD as the only functionally distinct state (STALE, about to expire) — a two-sided flip marker instead of a three-state one, with the same three-turn total information lifespan: placed CONTACT-side up, flipped to STALE at the next Recovery Phase, removed at the Recovery Phase after that. Rule 14.8 carries the consolidated marker.*

E.100  Campaign Economy — Resupply and Replacement Points (Rule 13.2.2)
-------------------------------------------------------------------------

*Design note: Rule 13.2.2's Resupply column had stood as pure framework since the campaign rules were drafted — ammunition is already per-scenario (Rule 16.3) and nothing consumed the column's four tiers. Confirmed with the designer: Resupply covers two things. First, clearing EXPENDED strips (Rule 21) on the Partial/half, Full or Extended/all schedule the tier names already implied. Second, a new Replacement Point resource, deliberately not abbreviated "RP" to avoid colliding with in-scenario Reaction Points (Rule 6.2) — spelled out in full everywhere it appears, since it is used far less often than the in-scenario resource it would otherwise be confused with.*

*Rather than invent a separate rebuild procedure, a Replacement Point mitigates a bad 13.3 recovery roll: spent after the roll, it raises that roll's result one tier on the existing table. This reuses the casualty track's own ladder instead of adding a second parallel one, and keeps Replacement Points meaningfully scarce — the baseline is 1 per campaign turn (0 tier-2/Partial, 1 tier-3/Full, 2 tier-4/Extended, per the designer's chosen flat rate), so a side can patch a couple of bad rolls per turn at most, never guarantee full recovery. Two choices were made by default rather than asked, and are flagged here for correction if wrong: Replacement Points do not carry over between campaign turns (a per-turn resource, not a stockpile), and a counter may absorb more than one Replacement Point in the same turn (each spent point is one more tier, with no per-counter cap beyond the recovery table's own ceiling of "returns at full strength").*

E.101  Campaign Economy — Experience Modifier and Unit Promotion (Rule 13.5.2)
---------------------------------------------------------------------------------

*Design note: Rule 1.3 has defined an Experience Modifier (EM) — "a campaign multiplier reflecting combat experience gained or lost" — since the glossary was written, and Rule 19.6.1 promised vehicle crews "the same campaign mechanics" as infantry, but nothing ever specified what EM actually tracked or how it changed. Confirmed with the designer: a unit earns one EM step, moving it one level up the Rule 15.2.1a Quality ladder (Militia → Green → Regular → Veteran/Elite), for every 3 consecutive scenarios it finishes without being rendered CI (broken, dispersed, or captured — Rule 13.1); the streak resets to zero the moment the unit is rendered CI. Promotion caps at Veteran/Elite — Elite specialist (veteran snipers, senior leaders) stays a printed classification, not something earned through play, matching the designer's intent that promotion season ordinary troops up to veteran status without manufacturing hand-picked specialists.*

*EM is defined generically — "any counter with a printed Quality rating" — so it covers vehicle crews under Rule 19.6.1's cross-reference without needing separate vehicle-specific text. This resolves only EM's upward half. Rule 1.3's own "gained or lost" phrasing and Rule 19.6.1's "quality degrades with replacement crew" both name a downward half — losing EM steps, whether from a bad campaign stretch or from crewing a vehicle with replacements — that the designer was not asked about and that remains genuinely undesigned; Rule 13.5.2 flags this explicitly rather than silently treating the glossary's "or lost" as covered.*

E.102  Campaign Economy — EM's Downward Half Remains Undesigned
-----------------------------------------------------------------

*Design note: recorded separately from E.101 because it is a distinct open question, not a footnote to it. Rule 1.3's Experience Modifier is defined as reflecting combat experience "gained or lost," and Rule 19.6.1 states vehicle crew quality specifically "degrades with replacement crew" — both promise a downward mechanic that Rule 13.5.2 does not provide. Two candidate triggers suggest themselves (a bad campaign stretch — repeated CI results — costing a unit an EM step; a vehicle specifically losing its original crew to bailout or casualty and being re-crewed from the replacement pool) but neither was part of what the designer confirmed when EM's upward half was resolved, and inventing either now would be exactly the kind of unrequested mechanic this project's own conventions rule out. Rule 13.5.2's own text flags this in place; treat EM as strictly non-negative — it only ever goes up — until this note is superseded.*

E.103  Generic Branching Campaign Framework (Rule 13.5.3–13.5.7)
--------------------------------------------------------------------

*Design note: Rule 13.5 had stood since the campaign rules were drafted as a single sentence of intent ("scenarios linked by a branching tree structure") plus 13.5.1's outcome-grade mapping, with no actual mechanism for what a "branch" is or how a campaign is authored around one. Confirmed with the designer: this resolves the generic framework only — how a campaign is structured and played — not any specific campaign's actual scenarios, which stay out of scope as campaign-specific authored content the framework supports rather than provides (the same distinction already drawn for the resupply and promotion systems in E.100–E.101).*

*Three structural choices were made deliberately rather than left to guesswork. First, the campaign is technically a directed acyclic graph, not a strict tree — different branches may reconverge on the same later node (13.5.5) — because a strict tree's branch count compounds catastrophically with depth (up to 5 branches per node, at every node, forever), which no realistically-sized scenario booklet could ever author in full; a cycle is still forbidden, so a campaign is always guaranteed to terminate. Second, a node's branch table may group multiple outcome grades onto the same next node at the designer's discretion (13.5.4) rather than mandating a distinct destination for the full five-grade spread every time — this keeps a simple two-or-three-branch campaign exactly as easy to author as a fully five-way one, rather than forcing false precision onto every node. Third, the campaign's overall winner is simply whoever won the terminal scenario (13.5.7), not a running total of victory points across the path — this was the more consistent reading of "the outcome of each scenario... determines which scenario follows," treating the branching structure itself, not a separate scoring system, as what a campaign's momentum already is.*

*The framework deliberately leaves open which side is nominated as a branch table's outcome-grade reference (13.5.6) — a specific campaign's scenarios may swap attacker and defender between nodes, and only that campaign's own design knows which side's grade should route the branch.*
