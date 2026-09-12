Section 20 — Snipers
====================

Snipers in World War II were not the Hollywood archetype of a lone marksman winning firefights. They were precision instruments used to decapitate enemy leadership, suppress crew weapon operators, and create psychological pressure across entire areas of ground. The knowledge that a sniper was present changed how everyone moved — even people who had not been shot at.

Sniper rules differ from standard infantry fire in three fundamental ways: they target specific individuals rather than hexes, they remain hidden after firing, and they impose psychological suppression on areas rather than individual targets.

20.1  Sniper Counter Design
---------------------------


**20.1.1**  Sniper counters use the triangle symbol (△) and the precision weapon class icon (╌○) on their fire line.

.. container:: rule-guide

   **Why:** A distinct silhouette and fire-line icon let a player recognise a sniper counter at a glance during setup and identification, since snipers follow an entirely different targeting and detection system than every other fire unit on the board.

   **Example:** Scanning the map, a player immediately knows the △ counter with the ╌○ fire line is a sniper — not a scout or an HMG team — and mentally applies deliberate-targeting and detection rules rather than standard fire resolution to it.

**20.1.2**  Standard sniper counter stats:

.. container:: rule-guide

   **Why:** Centralises the sniper's baseline numbers in one reference block so quality and nationality differences (Rule 20.7) can be expressed as deltas from a single known standard, rather than restating the full stat line for every variant.

   **Example:** Alpha's sniper counter reads M1/F1/G0 with fire line ╌○ 3 ⬡6 -1 — one careful hex of movement, one shot, no close assault capability, and a low-volume but precise attack.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Stat**
     - **Value**
     - **Notes**
   * - M#
     - M1
     - Careful movement only — snipers do not run
   * - F#
     - F1
     - One shot per turn — patience and precision
   * - G#
     - G0
     - Snipers do not close assault
   * - Fire line
     - ╌○ 3 ⬡6 -1
     - Low rFP — precision not volume
   * - AMO
     - 4 base + secret bonus
     - Limited shots per scenario
   * - Morale
     - 7 (veteran) or 6 (regular)
     - Snipers are selected troops
   * - Defence
     - 4
     - Small team, hard to spot but lightly equipped


**20.1.3**  Sniper ammunition follows the same system as mortars (Rule 16.3). Base AMO is 4 — certain, with no roll or private record. Past base AMO, roll the extended ammunition table each shot.

.. container:: rule-guide

   **Why:** Reuses the mortar ammunition-tracking mechanism (Rule 16.3) rather than inventing a parallel system, since both units represent scarce, carefully-rationed shots where running dry mid-scenario is a real tactical concern.

   **Example:** Alpha's sniper fires four times without any roll — each is guaranteed. On the fifth shot, the player must roll the extended ammunition table to see whether the sniper still has rounds available.

20.2  Deliberate Targeting
--------------------------


**20.2.1**  Standard fire resolution targets a hex — all units in the hex are at risk and the attacker cannot control which unit takes the casualty result.

.. container:: rule-guide

   **Why:** Establishes the default baseline that deliberate targeting (Rule 20.2.2) is explicitly an exception to — ordinary fire is indiscriminate within a hex, which is precisely what makes a sniper's ability to pick one specific occupant so significant.

   **Example:** A squad fires into a hex containing Squad Bravo and an attached leader — if the result is a casualty, the defending player chooses which counter takes it, not the attacker.

**20.2.2**  Snipers may declare deliberate targeting — naming a specific unit or unit type as the target before rolling. A casualty result or better applies to that specific unit rather than the hex generally.

.. container:: rule-guide

   **Why:** This is the sniper's defining tactical capability — the ability to remove a named, chosen target rather than leaving casualty allocation to the defender — reflecting the real-world practice of aimed, individual-target shooting rather than area suppression.

   **Example:** Alpha's sniper declares deliberate targeting against a leader counter stacked with Squad Bravo before rolling. A casualty result eliminates the leader specifically, even though the squad shares the hex.

**20.2.3**  Deliberate targeting is only available against valid priority targets. Snipers historically focused on high-value targets whose loss degraded enemy effectiveness:

.. container:: rule-guide

   **Why:** Restricting deliberate targeting to a defined priority list keeps snipers a high-value, leadership-and-crew-disrupting tool rather than a generic squad-killer, matching their real historical employment against targets whose loss had outsized effect.

   **Example:** A leader counter (Priority 1) and an HMG team (Priority 2) are both valid deliberate targets in the same hex — the sniper's player chooses which one to name before rolling.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Priority**
     - **Valid deliberate targets**
   * - 1 (highest)
     - Leaders — any leader counter
   * - 2
     - Crew weapon operators — HMG teams, mortar teams, AT gun crews
   * - 3
     - Forward observers calling fire missions
   * - 4
     - Vehicle commanders (unbuttoned vehicle — not Pinned)
   * - 5
     - Radio operators (scenario-defined special unit)


**20.2.4**  Snipers may not use deliberate targeting against regular rifle squads, SMG squads, or LMG teams — these units are too dispersed for a single aimed shot to reliably identify and engage a single man.

.. container:: rule-guide

   **Why:** A dispersed squad has no single identifiable "target" the way a leader or crew-served weapon operator does — this exclusion keeps deliberate targeting a tool against specific individuals rather than a way to guarantee casualties against ordinary infantry.

   **Example:** A sniper cannot declare deliberate targeting against Squad Bravo itself — only against a specific priority-list unit (a leader, crew weapon, etc.) that happens to be stacked with or near it.

**20.2.5**  If a deliberate targeting shot produces Suppressed or Pinned — the round was close but not a hit — the result applies to the hex normally rather than the specific target.

.. container:: rule-guide

   **Why:** A near-miss still has to land somewhere — applying a sub-casualty result to the whole hex reflects that a shot that didn't connect with the named target still had a suppressive effect on everyone nearby, rather than vanishing with no consequence.

   **Example:** Alpha's sniper declares deliberate targeting against a leader and rolls a Pinned result — the leader isn't specifically affected, but every unit in that hex is now Pinned.

**20.2.6**  Long range cap exemption: when deliberate targeting is declared, the long range cap (Rule 8.7) does not apply. Full result thresholds are used regardless of eFP. See Rule 8.7.4.

.. container:: rule-guide

   **Why:** The long range cap (Rule 8.7) exists to prevent unrealistic long-range casualties from ordinary area fire, but a sniper's deliberate, aimed shot is exactly the exception that cap was never meant to constrain — precision compensates for range in a way volume fire cannot.

   **Example:** A sniper at extreme range that would normally be capped to Suppressed-only results under Rule 8.7 can still roll a full Casualty result against a deliberately targeted leader, since the cap simply doesn't apply here.

    *See also: Rule 8.7.4 (Long Range Cap exemption) and Rule 12.9.1a (Leaders — casualty allocation exception) both depend on this rule.*

20.3  Sniper Concealment and Detection
--------------------------------------


**20.3.1**  Snipers begin each scenario as FIXED units (Section 14.7) or HIDDEN — they are never placed openly on the map at scenario start.

.. container:: rule-guide

   **Why:** A sniper visible from the first turn would lose its entire tactical identity — the threat comes precisely from not knowing where the shot will come from, so concealment at setup is not optional flavour but the mechanic the rest of Section 20 depends on.

   **Example:** At scenario start, the defending player places their sniper as a HIDDEN counter rather than openly on the map — the attacker has no idea a sniper is even present until it fires.

**20.3.2**  A sniper that fires is not automatically revealed. Instead the opponent makes a sniper detection roll:

.. container:: rule-guide

   **Why:** Firing is the moment a sniper is most exposed, but muzzle flash and sound don't guarantee a precise fix on the shooter's position — a detection roll models the real chance that even after firing, the sniper's exact location remains unknown.

   **Example:** Alpha's sniper fires at an exposed leader. Rather than automatically flipping the counter face-up, the opposing player now rolls to see whether they can pinpoint where the shot came from.

**20.3.3**  Detection roll: roll 1d6 + all applicable OBS modifiers vs sniper CON value.

.. container:: rule-guide

   **Why:** Framing detection as an opposed roll against the sniper's CON value (rather than a fixed percentage) lets terrain, actions taken, and scenario conditions all shift the odds, so a sniper firing from a bad position is genuinely easier to catch than one firing from deep cover.

   **Example:** A spotting unit with +2 OBS rolls a 4, for a total of 6, against a sniper firing from open ground (CON 5) — the roll meets the CON value and the sniper is detected.

**20.3.4**  Sniper base CON = 5. Modify as follows:

.. container:: rule-guide

   **Why:** Collects every factor that raises or lowers a sniper's concealment into one modifier table, so a player can quickly total up terrain, weather, and firing-history effects into a single CON value for that specific shot.

   **Example:** A sniper firing a normal shot (-3) from dense woods (+3) at night (+3) ends up at CON 5 - 3 + 3 + 3 = 8 — a very difficult detection roll for the opponent to beat.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **CON modifier**
   * - Dense woods or entrenchment
     - +3
   * - Light woods or building
     - +2
   * - Open ground
     - +0
   * - Fired this turn (normal fire)
     - -3
   * - Fired this turn (deliberate target)
     - -2 (more controlled shot, less signature)
   * - Night scenario
     - +3
   * - Smoke per hex intervening between spotter and sniper
     - +2 (same value as Rule 14.9.7)
   * - Fired from same position twice this scenario
     - -2 (position partially known)


*NOTE: the old "stationary, not fired this turn +2" row is deleted — the detection roll only ever occurs because the sniper fired this turn (Rule 20.3.2), so the condition could never hold in the roll it modified.*


**20.3.5**  Detection result:

.. container:: rule-guide

   **Why:** Signals that the CON roll (Rule 20.3.3-20.3.4) resolves into exactly one of two outcomes, keeping the detection procedure a clean binary rather than a graduated result — a sniper is either found or it isn't.

   **Example:** After totaling the detection roll against CON, the outcome falls into one of the two categories described in Rules 20.3.6 and 20.3.7 — nothing in between.

**20.3.6**  Roll meets or exceeds CON: sniper revealed — blind marker removed, counter placed on map at firing position.

.. container:: rule-guide

   **Why:** Once detected, the sniper loses the concealment that made it dangerous — placing the actual counter (rather than leaving a hidden marker) lets the opponent finally bring direct fire, artillery, or assault to bear on a known location.

   **Example:** The detection roll succeeds against Alpha's sniper — its HIDDEN marker is removed and the actual sniper counter is placed at the hex it fired from, now a visible target for return fire.

**20.3.7**  Roll below CON: sniper not detected — place a CONTACT marker (sniper type, crosshair symbol) at the firing position. Sniper remains hidden.

.. container:: rule-guide

   **Why:** Failing to detect the sniper doesn't mean the shot went unnoticed entirely — a CONTACT marker represents the opponent knowing roughly where fire came from without knowing exactly who or what is still there, which is what drives the area suppression effect in Rule 20.5.

   **Example:** The detection roll fails against Alpha's sniper — no counter is revealed, but a crosshair CONTACT marker is placed at the firing hex, and nearby enemy units now suffer the area suppression penalties of Rule 20.5.

20.4  Sniper Repositioning
--------------------------


**20.4.1**  After firing, before the detection roll is made, a sniper may immediately reposition up to M# hexes as a free action. This represents moving to a new position before the opponent can identify the firing point.

.. container:: rule-guide

   **Why:** A free, pre-detection reposition models the practiced sniper habit of "shoot and scoot" — moving immediately after firing was standard doctrine precisely because staying in the firing position invited counter-fire the instant the shot was heard.

   **Example:** Alpha's sniper fires, then immediately moves 1 hex (its M1 allowance) into nearby cover before the opponent even rolls for detection — the detection roll that follows is now made against the new position, not the one that actually fired.

**20.4.2**  The detection roll is made against the sniper's new position CON value, not the firing position.

.. container:: rule-guide

   **Why:** Since the reposition happens before detection (Rule 20.4.1), it would be inconsistent to still roll against the abandoned firing position's cover — the new position is where the sniper actually is when the opponent searches for it.

   **Example:** Alpha's sniper fires from open ground (CON 5 base, -3 for firing = CON 5) then repositions into dense woods — the detection roll uses the woods' +3 modifier, not the open ground the shot was fired from.

**20.4.3**  If the sniper repositions and is not detected, the CONTACT marker is placed at the original firing position — the opponent knows approximately where the shot came from but the sniper has moved.

.. container:: rule-guide

   **Why:** The CONTACT marker represents the opponent's best guess at the sniper's location based on the sound and direction of the shot, which is inherently tied to where the shot was actually fired from — not wherever the sniper has since relocated to.

   **Example:** Alpha's sniper fires from Hex A and repositions to Hex B undetected — the CONTACT marker (and its area suppression effect) is placed at Hex A, even though the sniper itself is now sitting safely in Hex B.

**20.4.4**  A sniper that does not reposition after firing uses the firing position CON for the detection roll.

.. container:: rule-guide

   **Why:** Repositioning (Rule 20.4.1) is optional, not automatic — a player may prefer to stay put if the firing position already offers excellent cover, so the rules must specify what happens to the detection roll when that choice is declined.

   **Example:** Alpha's sniper fires from a fortified building position and chooses not to move — the detection roll uses that building's CON modifier directly, since there is no new position to roll against.

20.5  Psychological Area Suppression
------------------------------------


**20.5.1**  When a sniper CONTACT marker (crosshair) exists anywhere on the map, all units of the side that placed it — the side the sniper is shooting at — within 6 hexes of that marker suffer:

.. container:: rule-guide

   **Why:** This is the mechanical heart of the sniper's psychological effect described in the section's introduction — a single undetected sniper reshapes movement across a wide area, not just at the point of the shot, reflecting how the mere knowledge of a sniper's presence changed unit behaviour historically.

   **Example:** A CONTACT marker sits in the middle of the map. Every enemy unit within 6 hexes of it — even ones nowhere near where the shot actually landed — is affected by the penalties in Rules 20.5.2 and 20.5.3.

**20.5.2**  Movement reduction: all movement at M# -1 (minimum 1).

.. container:: rule-guide

   **Why:** A blanket movement penalty represents troops moving more cautiously — using cover, pausing to check open ground — when they know a sniper might be watching, rather than the game tracking exactly which soldier is exposed to the sniper's field of view.

   **Example:** Squad Bravo normally moves at M4 but is within 6 hexes of an active CONTACT marker, so its move this turn is capped at M3.

**20.5.3**  Double-Timed Movement unavailable: no unit may declare Double-Timed Movement while a sniper CONTACT marker is within 6 hexes.

.. container:: rule-guide

   **Why:** Double-Timed Movement represents units moving with minimal caution for speed — exactly the behaviour a known sniper threat suppresses, since no sensible unit sprints across open ground when a hidden marksman might be watching. Cautious Movement (Rule 7.3a) remains fully available under the same threat — it's the opposite behaviour, and exactly what a sniper threat should encourage.

   **Example:** Squad Bravo would normally declare Double-Timed Movement to cross open ground quickly, but a CONTACT marker sits within 6 hexes — that option is unavailable this turn; Bravo may still take Cautious Movement instead.

**20.5.4**  This represents the historical reality that the mere knowledge of a sniper's presence changed how entire units moved — even soldiers who had not been fired at kept low, moved quickly between cover, and avoided open ground.

.. container:: rule-guide

   **Why:** Explicitly states the historical grounding for Rules 20.5.1-20.5.3 so the area-suppression mechanic reads as a deliberate simulation choice rather than an arbitrary blanket penalty tacked onto the sniper rules.

   **Example:** A veteran squad that has taken no casualties and never been directly fired upon still moves cautiously and avoids open ground the moment a CONTACT marker appears nearby — exactly the historical behaviour this rule models.

**20.5.5**  The psychological suppression applies from the moment the CONTACT marker is placed and persists until the marker is removed (sniper revealed, CONTACT marker ages to COLD and is removed, or sniper is eliminated).

.. container:: rule-guide

   **Why:** Tying the suppression's duration directly to the marker's lifecycle keeps the effect self-contained and unambiguous — a player never has to separately track "how long ago did this sniper fire," only whether the marker is still on the board.

   **Example:** A CONTACT marker placed on Turn 3 continues suppressing nearby movement through Turn 5, until it either ages off the map, the sniper is revealed by a later detection roll, or the sniper is eliminated outright.

20.6  Counter-Sniper Procedures
-------------------------------


**20.6.1**  A revealed sniper is engaged using standard fire resolution. However snipers in cover with high CON are very difficult to neutralise through direct fire alone.

.. container:: rule-guide

   **Why:** Once revealed (Rule 20.3.6), a sniper is just another low-Defence counter for fire-resolution purposes — but its high concealment value means simply spotting it doesn't guarantee a kill, pushing players toward the more effective methods listed in Rule 20.6.2.

   **Example:** Alpha's revealed sniper sits in a dense-woods hex with a high effective CON — small-arms fire into that hex is possible but far less likely to produce a casualty than the area-fire and duel options below.

**20.6.2**  Effective counter-sniper methods:

.. container:: rule-guide

   **Why:** Cataloguing the range of viable counter-sniper responses reinforces that direct fire (Rule 20.6.1) is deliberately the weakest option — historically, snipers were most reliably dealt with through area fire, dedicated counter-sniper fire, or accepting the cost of an assault.

   **Example:** Facing a well-concealed revealed sniper, Alpha's side chooses to call in mortar fire on the suspected position rather than trade small-arms fire with it directly, since area fire doesn't require LOS or a precise hit.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Method**
     - **Procedure**
     - **Effectiveness**
   * - Mortar or artillery fire
     - Area fire on suspected position — no LOS needed
     - Most effective — forces sniper to move or be destroyed
   * - Counter-sniper
     - Opposing sniper declares deliberate target against revealed sniper
     - Precise — one aimed shot
   * - Infantry assault
     - Standard close assault into sniper hex
     - Certain but costly if sniper has support
   * - Direct fire
     - Standard fire resolution vs revealed sniper
     - Possible but cover usually limits results


**20.6.3**  Counter-sniper duel: when both sides have active snipers within range of each other, either may declare deliberate targeting against the opposing sniper. The deliberate targeting rules apply normally. A Casualty result eliminates the opposing sniper. A Pinned result forces the opposing sniper to reposition (free reposition of up to M# hexes, no AP cost).

.. container:: rule-guide

   **Why:** A sniper-vs-sniper duel reuses the same deliberate targeting machinery already established (Rule 20.2.2) rather than inventing a separate system, while the free forced reposition on a Pinned result reflects a sniper who has been shot at scrambling for new cover immediately, without needing to spend an action to do it.

   **Example:** Alpha's sniper and an opposing revealed sniper are both within range of each other. Alpha declares deliberate targeting first and rolls a Pinned result — the opposing sniper is forced to reposition up to its M# hexes for free, without costing it any AP.

20.7  Representative 1943 Sniper Counters
-----------------------------------------


.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit**
     - **Fire line**
     - **AMO**
     - **Morale**
     - **Defence**
     - **Notes**
   * - German sniper team (Scharfschütze) — veteran
     - ╌○ 3 ⬡6 -1
     - 4
     - 7
     - 4
     - Scoped Kar98k or G43
   * - Soviet sniper (veteran)
     - ╌○ 3 ⬡6 -1
     - 4
     - 7
     - 4
     - Scoped Mosin-Nagant — Soviet programme produced many skilled snipers
   * - Soviet sniper (regular)
     - ╌○ 3 ⬡6 -1
     - 4
     - 6
     - 4
     - Lower morale reflects variable programme quality
   * - British sniper (veteran)
     - ╌○ 3 ⬡6 -1
     - 4
     - 7
     - 4
     - Scoped No.4 Mk I(T)
   * - US sniper (regular)
     - ╌○ 3 ⬡6 -1
     - 4
     - 6
     - 4
     - Scoped M1903A4 Springfield
   * - Japanese sniper (veteran)
     - ╌○ 3 ⬡6 -1
     - 4
     - 7
     - 4
     - Scoped Type 97/99 Arisaka — well-documented Pacific theatre marksmen, often fighting from concealed tree or spider-hole positions


*NOTE: All nations use identical fire line values — sniper effectiveness at this scale is determined more by position, patience, and target selection than by weapon differences. Quality differentials are encoded in Morale values and the extended-ammunition rolls past base AMO. A veteran sniper with Morale 7 recovers from suppression automatically and passes detection checks more reliably.*

*Sourcing note (E.149): Martin Pegler's* The Military Sniper Since 1914 *(Osprey Elite 68) independently reconstructs this project's veteran/regular split — a mass but variably-trained Soviet program, a German program rebuilt in direct imitation of Soviet methods after 1941, and a British program neglected between the wars but recovered quickly all read as consistent with the Morale values above. The book also documents a real, uncaptured distinction between US Army snipers (weaker training and equipment) and US Marine Corps snipers (a dedicated school from December 1942, a better-performing rifle/scope pairing) — this project's single "US sniper — regular" row reflects the Army configuration only; a separate Marine Corps veteran-tier row is a well-sourced candidate left open for a future pass, not added here. See* ``counters/toe/military_sniper_pegler_1943.md`` *for full citations.*
