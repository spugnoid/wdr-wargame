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
