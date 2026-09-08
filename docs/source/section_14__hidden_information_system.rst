Section 14 — Hidden Information System
======================================

With Deepest Regret... uses a physical hidden information system to model the fog of war. Units may be in one of three visibility states. The system uses blind markers on the map, a covered chart beside the map, and serialised markers to maintain information integrity without a referee.

14.1  Visibility States
-----------------------


**14.1.1**  Every unit is in one of three visibility states at all times:

.. container:: rule-guide

   **Why:** Anchors the entire hidden-information system to a fixed set of three named states, so every later rule in this section can simply reference VISIBLE, HIDDEN, or FIXED rather than describing degrees of concealment in prose each time.

   **Example:** Alpha starts a scenario deployed openly (VISIBLE), later goes hidden behind a treeline (HIDDEN, Section 14.5), and a different unit is pre-placed in ambush before the scenario even begins (FIXED, Rule 14.7) — every unit on the map is always in exactly one of these three states.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **State**
     - **Map Representation**
     - **Chart**
     - **Opponent Knows**
   * - VISIBLE
     - Unit counter placed openly on map
     - Not on chart
     - Unit type, strength, position
   * - HIDDEN
     - Blind marker on map at unit position
     - Counter in covered slot
     - Approximate position, size category only
   * - FIXED
     - No map representation until activated
     - Position on record sheet
     - Nothing — unit not yet on map


14.2  The Hidden Information Chart
----------------------------------


**14.2.1**  Each player has a hidden information chart with numbered slots beside the map. Each slot has a physical cover — a cup, opaque token, or small box.

.. container:: rule-guide

   **Why:** Gives the hidden-information system a physical, off-map home for concealed counters, since the whole system depends on something in the real world actually hiding information from the opponent — a chart with numbered, physically covered slots is that mechanism.

   **Example:** A player's hidden information chart has numbered slots 1 through however many are needed, each with its own opaque cover, sitting beside the map where the opponent cannot see underneath any of them.

**14.2.2**  When a unit goes HIDDEN, its counter is seated under one of a group of numbered covers **out of the opponent's sight** — behind a small screen, below the table edge, or with the covers face-down in hand — together with the empty covers of any dummies spawned in the same action. The whole group of covered slots is then placed on the chart **simultaneously**. Blind markers with the matching numbers go on the map. The opponent may know which group of numbers belongs together; nothing in the placement may reveal which number holds the counter.

.. container:: rule-guide

   **Why:** Requires the real counter and its dummy covers to be seated together, out of sight, and placed simultaneously — any deviation from this (seating the real unit first, placing covers one at a time) would let an attentive opponent infer which slot is real, defeating the whole system's purpose.

   **Example:** Alpha goes HIDDEN with two dummies spawned in the same action. All three covers are seated behind a screen where the opponent can't watch, then all three are placed on the chart at once — the opponent sees three new covered slots appear together, with no way to tell which one is Alpha.

**14.2.2a**  Concealed seating is what the system's integrity rests on: a counter visibly placed into slot 4 while empty covers go on slots 5 and 6 is not hidden information, whatever the covers claim afterwards. If a seating is accidentally exposed, re-seat the group from scratch out of sight.

.. container:: rule-guide

   **Why:** States plainly that a cover's label means nothing if the seating itself was ever visible — the system's integrity depends entirely on the seating being genuinely concealed, not on trusting the players to not look at what they already saw.

   **Example:** If a player accidentally seats a counter where the opponent glimpses which slot it went into, that group's concealment is compromised — the fix is to re-seat all the group's covers again from scratch, fully out of sight, not to simply continue play as if nothing happened.

**14.2.3**  Covered slots may not be touched by either player during play except when the rules require revelation. Physical integrity is maintained by the cover, not by trust.

.. container:: rule-guide

   **Why:** Enforces the system with a hard physical rule — hands off the covers except when a rule explicitly calls for revelation — rather than relying on players simply agreeing not to peek, since a hidden-information system needs enforceable mechanics, not honor code.

   **Example:** Neither player may lift or shift a covered slot out of curiosity mid-game; a cover only comes off when a specific rule (like a successful spot roll, Rule 14.9.1) says the unit underneath is now revealed.

**14.2.4**  When a unit is revealed, its cover is removed, the counter is lifted from the chart and placed on the map, and the blind marker is removed.

.. container:: rule-guide

   **Why:** Spells out the exact three-step physical procedure for revelation — remove cover, place counter, remove blind marker — so both players perform the same mechanical sequence every time a unit stops being hidden, regardless of what triggered the reveal.

   **Example:** When Alpha is spotted successfully, its cover comes off the chart, its actual counter is placed on the map at its blind marker's hex, and that now-unneeded blind marker is removed from the map.

14.3  Blind Markers
-------------------


**14.3.1**  Blind markers come in three sizes matching the actual stack footprint of the unit they represent:

.. container:: rule-guide

   **Why:** Ties marker size to the real stack it represents so an opponent gets accurate (if limited) information about how much force is hiding under a given marker — the fog of war hides identity and stats, not gross size category.

   **Example:** A single hidden unit uses a one-dot marker; a stack of Alpha and Squad Bravo together hiding in the same hex uses the two-dot small-stack marker instead — the marker's size alone tells the opponent roughly how much is there.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Marker Size**
     - **Symbol**
     - **Represents**
   * - Single
     - One dot
     - 1 combat unit
   * - Small stack
     - Two dots
     - 2–3 units
   * - Large stack
     - Three dots
     - 4+ units


**14.3.2**  The owning player must use the correct size marker for the actual stack. A single unit may not hide under a large stack marker.

.. container:: rule-guide

   **Why:** Closes the obvious exploit of hiding a small force under an intimidating large marker (or vice versa) to mislead the opponent — marker size is required to be truthful information, the one thing about a hidden stack the opponent can actually rely on.

   **Example:** A single unit going hidden must use the single (one-dot) marker — it cannot deliberately use a large-stack (three-dot) marker to bluff the opponent into thinking a bigger force is present.

**14.3.3**  Blind markers show nation colour but no unit type, quality, or stats.

.. container:: rule-guide

   **Why:** Draws the exact line on what a blind marker reveals — which side it belongs to and (via size, Rule 14.3.1) roughly how many units, but nothing about what those units actually are or how good they are, preserving genuine uncertainty about the threat.

   **Example:** An opponent looking at an enemy blind marker can tell it's a German small-stack — but nothing tells them whether it's two rifle squads or a squad and an HMG team, or what quality those units are.

14.4  Dummy Markers
-------------------


**14.4.1**  Dummy markers are blank chart slots with covers — no unit counter underneath. Their covers, slots, and map markers are physically identical to a real hidden unit's, and they are always seated and placed in the same concealed, simultaneous action as the real slot they were spawned with (Rule 14.2.2) — the opponent never observes which member of the group received the counter.

.. container:: rule-guide

   **Why:** Makes a dummy physically indistinguishable from a real hidden unit at every step — same covers, same slots, same map marker, same simultaneous placement — since the moment a dummy looks even slightly different, the whole point of using it to create uncertainty collapses.

   **Example:** An opponent watching Alpha's group of three markers appear on the map cannot tell by looking which one is Alpha and which two are dummies — the covers, chart slots, and blind markers give no physical tell.

**14.4.2**  Dummies must match the size category of the real unit they were spawned from. A single unit spawning dummies produces single-size dummies only.

.. container:: rule-guide

   **Why:** Keeps a dummy's size marker consistent with what the real unit would use (Rule 14.3.1), so the size category itself never gives away which marker in a group is the real one — every marker in the group looks like it could plausibly be that same-sized unit.

   **Example:** A single unit that spawns two dummies produces two single-size (one-dot) dummy markers — never a mismatched large-stack dummy that would stand out as obviously not matching the real unit's size.

**14.4.3**  When a spot roll targets a dummy and succeeds, the owning player announces dummy. The dummy marker is removed from the map. The opponent may verify by uncovering the corresponding slot — it is empty.

.. container:: rule-guide

   **Why:** Gives the opponent a verifiable way to confirm a dummy really is empty, rather than asking them to simply trust the owning player's word — the physical chart slot itself proves the announcement true, keeping the system honest without a referee.

   **Example:** An opponent spends RP to spot a marker and succeeds; the owning player announces it's a dummy and removes it from the map. If the opponent wants proof, they can uncover that marker's chart slot themselves and see it's empty.

**14.4.4**  Dummies may be moved independently at a cost of 1 AP per dummy per activation. When the real unit moves during an activation, all dummies in its group may move for free during the same activation.

.. container:: rule-guide

   **Why:** Prices dummy movement to make maintaining a spread-out deception meaningfully costly on its own, while letting the real unit's own movement carry its dummy group along for free — the group naturally stays together at no extra cost unless the player actively wants to fan them out.

   **Example:** A player who wants two of Alpha's three dummies to peel off in different directions spends 1 AP per dummy to move them independently; if Alpha itself moves normally, its whole dummy group can tag along in that same activation without any extra AP cost.

**14.4.5**  Dummies must follow plausible movement routes — terrain movement costs apply, impassable terrain cannot be crossed, movement cannot exceed the real unit's M# per impulse.

.. container:: rule-guide

   **Why:** Holds dummy movement to the same physical constraints as a real unit's, since a dummy that could cross terrain a real unit couldn't (or move farther than the real unit's M# allows) would give away its unreality by its route alone.

   **Example:** A dummy spawned from a unit with M2 cannot move 4 hexes in one impulse or cross an impassable cliff hex — its movement has to look exactly as constrained as the real unit's would.

14.5  Going Hidden
------------------


**14.5.1**  A VISIBLE unit may go hidden by spending 1 AP. The unit must be in terrain with cover modifier +2 or higher, or have no enemy unit with LOS to its hex.

.. container:: rule-guide

   **Why:** Requires either decent cover or a clean break in LOS before a unit can go hidden, since a unit standing in the open under direct observation has no plausible way to actually conceal itself from a watching enemy — going hidden models a real chance to break contact, not a magic disappearing act.

   **Example:** Alpha in open ground with an enemy unit directly observing it cannot go hidden; Alpha behind light woods (+2 cover, meeting the threshold) or with no enemy LOS to its hex at all can spend 1 AP to attempt it.

**14.5.2**  Going hidden procedure:

.. container:: rule-guide

   **Why:** Signals that the next rule (14.5.3) is the actual step-by-step mechanical procedure for going hidden, keeping the narrower "how to do it" mechanics separate from the eligibility check of Rule 14.5.1.

   **Example:** Once Alpha meets the eligibility conditions of Rule 14.5.1 and spends its 1 AP, the specific chart-and-marker mechanics that follow are what Rule 14.5.3 defines as the actual procedure.

**14.5.3**  Immediately receive a free hidden impulse (see Rule 14.6) before the reaction window opens. The chart seating and all marker placement happen inside that impulse, as one concealed, simultaneous commitment — the counter is never visibly placed into its slot first.

.. container:: rule-guide

   **Why:** Grants the free hidden impulse before the opponent's reaction window can open, so all of the concealment mechanics (Rule 14.6) complete as one atomic, uninterruptible commitment — there's no gap where the opponent could react to a half-completed hiding action and glean information from it.

   **Example:** The instant Alpha's going-hidden action is declared and paid for, it immediately runs through the full free hidden impulse of Rule 14.6 (seating, dummy spawning, marker placement) before the opponent ever gets a reaction window to respond to anything about that specific impulse.

14.6  Free Hidden Impulse
-------------------------


**14.6.1**  When a unit goes hidden — either by spending 1 AP or as a free action after firing from a FIXED position — it immediately receives a free hidden impulse outside the normal AP economy.

.. container:: rule-guide

   **Why:** Makes the hidden impulse free and automatic rather than something requiring further AP, since the concealment mechanics themselves (seating, dummy spawning, marker placement) are the mechanical consequence of already having paid to go hidden — the going-hidden cost was already paid, once, by whichever rule triggered it.

   **Example:** Both a unit spending 1 AP to voluntarily go hidden (Rule 14.5.1) and a FIXED unit going hidden for free after firing (Rule 14.7.5) trigger the same free hidden impulse — no additional AP is spent on the impulse itself in either case.

**14.6.2**  During the free hidden impulse the owning player, out of the opponent's sight, seats the unit counter under one numbered cover and prepares 2 empty (dummy) covers, then commits everything at once:

.. container:: rule-guide

   **Why:** Fixes the dummy count at exactly 2 for a standard free hidden impulse — enough to create real three-way uncertainty (Rule 14.6.7) without requiring an open-ended or player-chosen number of covers that would complicate the simultaneous-placement mechanics.

   **Example:** Every standard free hidden impulse produces exactly 3 covered slots total — the real unit plus 2 dummies — seated together out of sight before anything is placed on the chart.

**14.6.3**  Places all three covered slots on the chart simultaneously (Rule 14.2.2), and places the three matching numbered blind markers on the map simultaneously.

.. container:: rule-guide

   **Why:** Ties the chart-side and map-side placement together as one coordinated, simultaneous act, consistent with Rule 14.2.2's core integrity requirement — nothing about the order or timing of placement may give the opponent a hook to distinguish the real unit from its dummies.

   **Example:** All three chart slots and all three matching numbered map markers appear at the same moment — the opponent never sees, say, the map markers go down first and the chart slots placed a beat later, which could otherwise hint at something.

**14.6.4**  One marker (the owning player knows which; the opponent must not be able to tell) is placed up to M# hexes from the unit's last known position along any plausible route following terrain movement costs; each other marker is placed anywhere the real unit could legally have reached under the same constraint — including its last known position. Because every marker in the group obeys the same placement envelope, marker geometry reveals nothing about which is real.

.. container:: rule-guide

   **Why:** Requires every marker in the group — real and dummy alike — to obey the exact same movement-legality envelope, so a sharp-eyed opponent can't deduce the real unit just by noticing one marker took an implausible or impossible route that only the "cheating" dummies could get away with.

   **Example:** If Alpha has M2, none of its three markers this impulse — real or dummy — can end up more than 2 hexes away along a legal route; an opponent who sees one marker sitting 3 hexes out would know something was wrong, so the rule guarantees that never happens.

*NOTE: earlier drafts placed the real counter into its slot in the open, spawned visibly-empty dummy covers, and moved the real marker before the dummies existed — in face-to-face play the opponent simply watched, and the three-marker uncertainty this system exists to create never existed. Every leak has the same fix: assignment happens out of sight, and everything that could distinguish group members is committed simultaneously under a shared constraint.*

**14.6.5**  May move each dummy marker up to M# hexes along any plausible route.

.. container:: rule-guide

   **Why:** Lets the dummies spread out across the same movement envelope the real unit used (Rule 14.6.4), so the group as a whole plausibly represents several different places the real unit could have gone, rather than all three markers clustering suspiciously in one spot.

   **Example:** Alpha's two dummy markers can each independently move up to Alpha's own M# hexes along their own plausible routes — spreading the three-marker group out to genuinely different, individually-plausible destinations.

**14.6.6**  After the free hidden impulse, the reaction window opens. The opponent may spend RP to attempt spot rolls against any of the three markers.

.. container:: rule-guide

   **Why:** Opens the normal reaction window only after the whole concealment commitment is finished, giving the opponent a real chance to try to pierce the new uncertainty with spot rolls (Section 14.9) — but only once there's actually a completed group of markers to spot against.

   **Example:** Once Alpha's free hidden impulse places all three markers, the opponent's reaction window opens and they may spend RP attempting a spot roll against any one of those three markers, same as against any other hidden marker.

**14.6.7**  The free hidden impulse represents the brief window of confusion when a unit disappears from view and the opponent cannot determine which way it went.

.. container:: rule-guide

   **Why:** States the fictional justification behind the whole mechanic — the moment a unit breaks contact is genuinely chaotic and hard to track, which is exactly the real-world phenomenon the three-marker uncertainty of this section is built to simulate.

   **Example:** When Alpha ducks out of sight behind a treeline, the three resulting markers represent the opponent's genuine uncertainty in that instant about which direction the unit actually went — not just an abstract game mechanic layered on top of a known outcome.

14.7  FIXED Units
-----------------


**14.7.1**  FIXED units are units assigned to prepared positions before the scenario begins. They have no counter on the map and no blind marker — their position is committed to a scenario record sheet before play starts. Both players must agree that positions are recorded before the scenario begins.

.. container:: rule-guide

   **Why:** Gives FIXED the strongest possible concealment — no marker at all, only a written record — since it represents a genuinely prepared ambush position established before the fighting starts, information the opponent has had no chance to observe forming in real time.

   **Example:** A defending player writes down that an HMG team is FIXED in a specific hex before the scenario begins; the opposing player sees no marker there at all until the FIXED unit fires, moves, or is walked into (Rules 14.7.2-14.7.7).

**14.7.2**  A FIXED unit that moves for the first time transitions to HIDDEN status. Its counter is placed on the chart under cover, a blind marker is placed at its recorded position, and it receives a free hidden impulse to spawn dummies and reposition.

.. container:: rule-guide

   **Why:** Converts FIXED's off-map secrecy into the normal HIDDEN marker system the instant a FIXED unit needs to move, since movement requires a physical presence on the map — the transition point is exactly when the unit stops being purely a paper record and becomes something the map (and the opponent) can interact with.

   **Example:** A FIXED unit ordered to relocate transitions to HIDDEN: its counter goes onto the chart under cover, a blind marker appears at its recorded hex, and it immediately gets a free hidden impulse (Section 14.6) to spawn dummies and start moving.

**14.7.3**  A FIXED unit that fires without moving may choose one of two options:

.. container:: rule-guide

   **Why:** Gives a FIXED unit that wants to fire from its prepared position a real choice between staying put openly or firing and immediately trying to vanish again — reflecting that revealing a prepared position by firing doesn't have to mean abandoning concealment forever.

   **Example:** A FIXED HMG team that opens fire can either accept being revealed at its position (Option A, Rule 14.7.4) or fire and then attempt to disperse into hiding again (Option B, Rule 14.7.5) — the owning player picks based on the tactical situation.

**14.7.4**  Option A — Sit tight: the unit is revealed at its recorded position. No dummies spawned. It may go hidden on a subsequent activation by spending 1 AP.

.. container:: rule-guide

   **Why:** Gives the simpler, no-frills option of just accepting full revelation after firing — no dummy overhead, but also no immediate re-concealment; the unit can still try to hide again later, just through the normal paid process (Rule 14.5.1), not for free.

   **Example:** A FIXED unit choosing Sit Tight after firing is placed on the map as an ordinary VISIBLE unit at its recorded hex; if it later wants to go hidden again, that costs the standard 1 AP like any other VISIBLE unit.

**14.7.5**  Option B — Fire and disperse: after firing resolves, the unit goes hidden as a free action (no AP cost). It receives a free hidden impulse — moves blind marker up to M# hexes and spawns 2 dummies at or adjacent to the firing position. This option may only be taken once per scenario from a FIXED position.

.. container:: rule-guide

   **Why:** Rewards a FIXED unit's first shot with a free, no-AP escape into hiding — modeling a well-prepared ambusher firing and immediately displacing — but limits this specific free version to once per scenario, since a unit can't keep exploiting a pristine ambush position indefinitely.

   **Example:** A FIXED unit's very first shot from its prepared position can be followed immediately by Fire and Disperse at no AP cost; if that same unit is later caught in the open again and wants to hide once more, it must use the ordinary paid process (Rule 14.5.1) instead, since the free option is already spent.

**14.7.6**  The surprise of the first FIXED fire applies a +2 rFP bonus to that fire action, representing the target's unpreparedness. This bonus applies only to the first fire from the FIXED position.

.. container:: rule-guide

   **Why:** Rewards the ambush value of a prepared position specifically on its opening shot, since that's the moment the target is genuinely caught unprepared — every subsequent shot from that same position no longer has the element of surprise once the enemy knows something is there.

   **Example:** A FIXED unit's very first fire action, whichever option it later chooses (Rule 14.7.4 or 14.7.5), gets +2 rFP for that one shot; any fire the unit takes afterward, from any position, no longer carries that surprise bonus.

**14.7.7**  A FIXED unit cannot be spotted — it has no marker on the map and nothing for a spot roll to target. It is revealed only by its own fire or movement (Rules 14.7.2–14.7.5), or when an enemy unit attempts to enter its recorded hex: the FIXED unit is revealed immediately as VISIBLE in its hex, and the entering unit halts in the hex it currently occupies with its remaining MP lost — it has walked into a prepared position. The revealed unit's +2 surprise bonus (Rule 14.7.6) still applies to its first fire.

.. container:: rule-guide

   **Why:** Makes FIXED concealment un-spottable by design, since there's genuinely nothing on the map to target a spot roll against — the only ways a FIXED unit's position comes to light are its own choices to move or fire, or an enemy unit's own movement stumbling directly into it.

   **Example:** An opponent cannot spend RP attempting to spot a FIXED unit no matter how good their OBS — but if their unit's move path happens to enter the FIXED unit's exact recorded hex, that FIXED unit is immediately revealed as VISIBLE and the moving unit halts there, its remaining movement lost.

14.8  Contact Markers
---------------------


**14.8.1**  When a spotted unit successfully goes hidden during play, a CONTACT marker is placed CONTACT-side up at the hex where it was last seen.

.. container:: rule-guide

   **Why:** Records the last-known position of a unit that broke contact, giving the opponent a decaying trace of intelligence rather than losing all information about it the instant it goes hidden — real reconnaissance doesn't forget a sighting the moment the target ducks out of view.

   **Example:** After Alpha is spotted and then successfully goes hidden the same turn, a CONTACT marker is placed at the hex where Alpha was last actually seen — that marker, not Alpha's new hidden position, is what the opponent's intelligence reflects.

**14.8.2**  The marker is a two-sided flip token, one flip per Recovery Phase:

.. container:: rule-guide

   **Why:** Gives the CONTACT marker a simple, self-aging mechanism — one flip per Recovery Phase — so its information value decays automatically over a fixed, predictable timeline without needing separate bookkeeping.

   **Example:** A CONTACT marker placed this turn flips to STALE at the very next Recovery Phase, tracking its own age with a simple physical flip rather than a written turn-counter.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **State**
     - **Age**
     - **Meaning**
   * - CONTACT
     - Placed this turn or the last
     - Recent intelligence — unit was here this turn or last
   * - STALE
     - 2 turns old
     - Outdated — removed at the end of this Recovery Phase


**14.8.3**  At the first Recovery Phase after placement, flip the marker to its STALE face. At the following Recovery Phase, remove it. This is the same three-turn information lifespan as before, just two states instead of three — see design note E.99.

.. container:: rule-guide

   **Why:** Fixes the marker's total lifespan at a predictable three turns (fresh, then STALE, then gone) so a player always knows exactly how much longer a given piece of last-known-position intelligence remains relevant before it expires entirely.

   **Example:** A CONTACT marker placed on turn 3 is CONTACT through turn 4, flips to STALE at the turn 5 Recovery Phase, and is removed entirely at the turn 6 Recovery Phase — three turns of informational life from placement to removal.

**14.8.4**  CONTACT markers are not combat units. They have no game effect beyond conveying information age.

.. container:: rule-guide

   **Why:** Makes explicit that a CONTACT marker is pure information with zero mechanical weight otherwise — it can't be attacked, doesn't block movement, and doesn't interact with any combat rule, existing solely to tell a player how recent a sighting was.

   **Example:** A unit can move through, into, or past a hex containing a CONTACT marker exactly as if the marker weren't there — it has no combat stats, occupies no stacking slot, and blocks nothing.

14.9  Spotting
--------------


**14.9.1**  Spotting is the process of identifying a hidden unit's marker. A successful spot roll reveals the unit — its blind marker is removed and its counter is placed on the map (or, for a dummy, announced and removed, Rule 14.4.3). FIXED units cannot be spotted (Rule 14.7.7).

.. container:: rule-guide

   **Why:** Defines spotting as the mechanism by which the hidden-information system's concealment is actually pierced — everything else in this section builds toward or reacts to a successful spot roll, whether the target turns out to be real (revealed to the map) or a dummy (announced and removed, Rule 14.4.3).

   **Example:** A successful spot roll against Alpha's hidden marker converts it back into a normal VISIBLE counter on the map; the same successful roll against one of Alpha's dummy markers instead ends with that marker being announced as fake and removed.

**14.9.2**  Automatic spotting — no roll required:

.. container:: rule-guide

   **Why:** Separates the small set of situations where revelation is guaranteed (Rules 14.9.3-14.9.4) from the larger set requiring an actual roll (Rule 14.9.5) — some actions are simply too conspicuous to leave any chance of remaining concealed.

   **Example:** A unit firing its weapon doesn't get a chance to stay hidden by rolling well — Rule 14.9.3 says firing is automatically revealing, no roll involved at all.

**14.9.3**  A unit that fires is automatically revealed at its firing position. No spot roll needed.

.. container:: rule-guide

   **Why:** Treats the muzzle flash, noise, and smoke of firing as unavoidably revealing, regardless of how good the shooter's concealment might otherwise be — a hidden unit trades its concealment for the ability to actually contribute firepower the moment it shoots.

   **Example:** Alpha, hidden with excellent CON modifiers, fires at an enemy unit and is immediately revealed at its firing position — its high CON never gets tested by a spot roll, because firing bypasses the roll entirely.

**14.9.4**  A unit whose blind marker is entered by an enemy unit is automatically revealed.

.. container:: rule-guide

   **Why:** Makes physical contact with a hidden marker an automatic reveal rather than requiring a roll, since an enemy unit that has literally walked into the same hex would obviously discover whatever's actually there — there's no plausible way concealment survives direct physical contact.

   **Example:** An enemy unit moving into the hex occupied by Alpha's blind marker reveals Alpha immediately and automatically — no spot roll is made, since the enemy is now standing in the same hex.

**14.9.5**  Spot roll triggers — roll required:

.. container:: rule-guide

   **Why:** Lists the specific circumstances that earn a chance at spotting via a roll rather than automatic revelation, ranging from free triggers (careless movement, artillery blast) to a deliberate RP-costing attempt — different levels of exposure or effort produce different-cost opportunities to try.

   **Example:** An enemy unit moving carelessly into LOS gives a free spot-roll attempt at no RP cost, while a player who wants to make a deliberate attempt against a marker that hasn't done anything careless must spend 1 RP for that chance instead.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Trigger**
     - **RP Cost**
     - **Notes**
   * - Enemy unit moves carelessly into LOS
     - 0 — free
     - Noise and visibility — no RP required
   * - Opponent spends RP to spot
     - 1
     - Deliberate observation attempt
   * - Unit takes Spot Action
     - 0 — is the action
     - Dedicated observation, +3 OBS bonus
   * - Artillery or mortar impact within 2 hexes of hidden unit
     - 0 — free
     - Blast briefly reveals nearby units


**14.9.6**  Spot roll procedure: roll 1d6, add OBS modifiers, subtract CON modifiers. If the result is **4 or greater**, the target is spotted.

.. container:: rule-guide

   **Why:** Sets the spot roll as a straightforward opposed-modifier check — spotter's observation bonuses against the target's concealment penalties — with a fixed target number, so every spot attempt in the game resolves the same simple way regardless of what's triggering it.

   **Example:** A spotter with +3 OBS (from a dedicated Spot Action) rolling against a target with +2 CON (light woods) needs a 1d6 result that, after adding 3 and subtracting 2, reaches 4 or better — meaning a raw roll of 3 or higher succeeds.

*NOTE: earlier drafts spotted on 0+, under which a Spot Action (+3 OBS) spotted a stationary unit in a building automatically and swept the board of markers in one action — the hidden system's uncertainty never survived contact with a single 1 AP action. At 4+, that same attempt succeeds 33% of the time per action: concealment decays under observation instead of evaporating.*

**14.9.7**  Concealment modifiers (CON). Every modifier is computable from the **map alone** — the marker's hex, its observed movement history this turn, and scenario conditions — so a dummy's CON is always exactly the CON a real unit under that marker would have, and announcing it reveals nothing (a spot roll against a marker whose owner must consult hidden unit state would itself leak whether the marker is real):

.. container:: rule-guide

   **Why:** Deliberately restricts every CON modifier to information visible on the map itself, since if a modifier ever depended on what's actually under a cover (the hidden unit's own stats), computing or announcing that modifier would itself leak whether a given marker is real or a dummy — the whole table has to be blind-to-identity by design.

   **Example:** A marker sitting in dense woods gets +3 CON whether it's a real unit or a dummy, since "the hex is dense woods" is visible to both players — no step in computing that modifier ever requires looking at what (if anything) is actually seated under the cover.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition (all map-observable)**
     - **CON Modifier**
   * - Marker's hex: open ground
     - 0
   * - Marker's hex: crops / tall grass
     - +1
   * - Marker's hex: light woods
     - +2
   * - Marker's hex: dense woods
     - +3
   * - Marker's hex: building
     - +2
   * - Marker's hex: entrenchment
     - +3
   * - Marker has not moved this turn
     - +2
   * - Marker moved normally this turn
     - +0
   * - Marker moved carelessly this turn
     - -2
   * - Marker moved through dense woods or rubble this turn
     - -1 (unavoidable noise)
   * - Night scenario
     - +3
   * - Smoke per intervening hex
     - +2


*NOTE: "fired this turn" and "suppressed/pinned" no longer appear here — a unit that fires is revealed automatically (Rule 14.9.3) and needs no spot roll, and a hidden unit taking fire results is revealed by the blast rules (Rule 16.7.7); neither state can belong to a marker still on the map.*


**14.9.8**  Observation modifiers (OBS) — spotter:

.. container:: rule-guide

   **Why:** Collects everything about the spotter's own situation — leadership, elevation, equipment, and their own activity — into one table, mirroring the target-side CON table (Rule 14.9.7) so a spot roll's two halves (spotter's advantages, target's concealment) are each computed from a clean, self-contained set of modifiers.

   **Example:** A spotter with a leader present (+leader OBS), elevated one level above the target (+1), and taking a dedicated Spot Action (+3) stacks all three OBS bonuses together for that one roll, on top of whatever the target's CON modifiers subtract.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **OBS Modifier**
   * - Leader present in hex
     - +leader OBS rating
   * - Elevated 1 level above target
     - +1
   * - Elevated 2+ levels above target
     - +2
   * - Binoculars equipment marker
     - +2
   * - Spotter moving this turn
     - -2
   * - Spotter suppressed
     - -2
   * - Dedicated Spot Action this turn
     - +3
   * - Active firefight within 5 hexes this turn
     - Sound spotting impossible — noise overwhelms


14.10  Spot Action
------------------


**14.10.1**  A unit may spend its entire activation on a Spot Action — it takes no other action this impulse.

.. container:: rule-guide

   **Why:** Prices dedicated observation at the cost of the unit's whole activation, so choosing to spot instead of moving or firing is a real tactical tradeoff — a unit committed to watching isn't simultaneously advancing or shooting that same impulse.

   **Example:** A unit taking a Spot Action this impulse cannot also move or fire in the same activation — the entire activation is spent watching, nothing else.

**14.10.2**  A unit taking a Spot Action gains +3 OBS for all spot rolls this turn.

.. container:: rule-guide

   **Why:** Makes the Spot Action's bonus last the rest of the turn rather than just the one immediate roll, since a unit that spends its whole activation watching stays alert and observant for the remainder of that turn, not just for a single instant.

   **Example:** A unit taking a Spot Action this impulse keeps its +3 OBS bonus for any further spot rolls it makes later the same turn (per Rule 14.10.4's rules on additional attempts), not just for the one free roll the action itself grants.

**14.10.3**  The Spot Action represents deliberate, methodical observation — scanning terrain, watching for movement, listening. Leaders and scouts are particularly effective when taking this action.

.. container:: rule-guide

   **Why:** Frames the Spot Action's mechanical bonus in terms of what real deliberate observation looks like, explaining why leaders (who stack their own OBS rating on top, Rule 14.9.8) and scout-type units get particular value from choosing this action over others.

   **Example:** A leader with a high OBS rating taking a Spot Action combines their personal OBS bonus with the action's own +3, making them noticeably more effective at this specific task than an ordinary combat unit doing the same thing.

**14.10.4**  A unit taking a Spot Action chooses **one** marker within its LOS and attempts a spot roll against it at no RP cost. Additional markers this turn require RP (Rule 14.9.5) — the +3 Spot Action bonus applies to those rolls too, but observation is a searchlight, not a floodlight: sweeping a whole treeline takes turns, not one action.

.. container:: rule-guide

   **Why:** Limits the free roll to a single chosen marker per Spot Action, keeping the action from becoming a way to sweep an entire area of markers for free in one impulse — the +3 bonus carries over to further RP-paid attempts that same turn, but each additional marker still costs something.

   **Example:** A unit taking a Spot Action against a treeline hiding three markers gets one free +3 OBS roll against whichever marker it chooses; checking the other two markers that same turn requires spending RP for each additional attempt, even though all three rolls benefit from the same +3 bonus.

14.11  Sound Spotting
---------------------


**14.11.1**  Sound spotting is only available when no unit has fired within 5 hexes this turn. Active firefight noise drowns out movement sounds entirely.

.. container:: rule-guide

   **Why:** Turns sound spotting off entirely once a firefight is loud enough nearby, since gunfire genuinely masks the sound of movement — a mechanism meant to model listening for footsteps and noise has to yield when there's a battle drowning everything else out.

   **Example:** A unit moving carelessly near a hidden marker would normally suffer sound-based CON penalties (Rule 14.11.4), but if any unit fired within 5 hexes that same turn, those specifically sound-based penalties don't apply — the noise of the firefight already covers it.

**14.11.2**  When sound spotting is available, the following CON penalties apply in addition to normal modifiers:

.. container:: rule-guide

   **Why:** Adds sound-specific penalties on top of the normal CON table (Rule 14.9.7) rather than replacing it, since sound spotting is meant to be an additional detection channel available under quiet conditions, not a wholesale alternative to the map-based concealment system.

   **Example:** A unit's normal CON modifiers from terrain and movement (Rule 14.9.7) still apply during a quiet turn; the sound-spotting penalties of Rules 14.11.3-14.11.4 stack on top of those, rather than substituting for them.

**14.11.3**  Units moving through dense woods or rubble: -1 CON (unavoidable noise — already included in the CON table above).

.. container:: rule-guide

   **Why:** Flags that this particular sound penalty is already baked into the main CON table (Rule 14.9.7) rather than being a separate additional deduction — dense woods and rubble are noisy to move through regardless of whether sound spotting specifically is in play.

   **Example:** A unit moving through dense woods already takes the -1 CON noise penalty from the main table whether or not sound spotting conditions (Rule 14.11.1) are currently met — this rule doesn't add a second, separate -1 on top of that.

**14.11.4**  Units moving carelessly: -2 CON (already included — the careless movement penalty covers both visual and audio signature).

.. container:: rule-guide

   **Why:** Confirms the careless-movement penalty already covers both what an observer would see and what they'd hear, so sound spotting doesn't need to apply that same -2 a second time on top of the visual penalty already in the main CON table.

   **Example:** A unit that moves carelessly takes a single -2 CON penalty that already accounts for both the visual exposure and the noise it makes — sound spotting availability doesn't stack an extra penalty for the same careless move.

**14.11.5**  Night scenarios: sound becomes the primary detection method. Visual spot range is reduced to 1-2 hexes maximum. All sound-based CON penalties are doubled. Full night rules are a separate design task — this rule establishes the framework.

.. container:: rule-guide

   **Why:** Shifts detection's whole balance toward hearing rather than sight once visual range collapses at night, doubling sound penalties to make noise the dominant way units actually get spotted — while honestly flagging that the full night-scenario ruleset is still a future design task, not yet complete here.

   **Example:** In a night scenario, a unit moving carelessly (normally -2 CON) suffers -4 CON instead under the doubled sound penalty, while visual detection is capped to spotting only within 1-2 hexes regardless of how good the spotter's OBS is.

14.12  FIXED Unit Transition Summary
------------------------------------


.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Event**
     - **Transition**
     - **Dummies Spawned**
     - **AP Cost**
     - **Surprise Bonus**
   * - FIXED unit moves
     - FIXED → HIDDEN
     - Yes — free hidden impulse
     - Normal move AP
     - No
   * - FIXED unit fires, sits tight
     - FIXED → VISIBLE
     - No
     - 0
     - +2 rFP first fire only
   * - FIXED unit fires, disperses
     - FIXED → HIDDEN
     - Yes — free disperse
     - 0 (free)
     - +2 rFP first fire only
   * - VISIBLE unit goes hidden
     - VISIBLE → HIDDEN
     - Yes — free hidden impulse
     - 1 AP
     - No
   * - HIDDEN unit revealed by spot
     - HIDDEN → VISIBLE
     - No
     - N/A
     - No
   * - HIDDEN unit fires
     - HIDDEN → VISIBLE
     - No unless rehides
     - 0 to reveal; 1 AP to rehide
     - No
