Section 10 — Unit Status
========================

10.1  Status Levels
-------------------


Units may be in one of the following status levels at any time. Status is tracked with markers placed on the counter.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Status**
     - **Movement**
     - **Fire**
     - **Reaction**
     - **Defence**
   * - Normal
     - Full M#
     - Full F#
     - Full
     - Normal
   * - Suppressed
     - Half M# (round down, minimum 1)
     - At -2 rFP
     - At -1 rFP
     - -2
   * - Pinned
     - No movement
     - At -4 rFP
     - Cannot react
     - -3
   * - Routing
     - D3 hexes away from enemy per activation
     - Cannot fire
     - Cannot react
     - -3
   * - Broken
     - N/A — counter removed
     - N/A
     - N/A
     - N/A
   * - Dispersed
     - N/A — counter on Casualty Track, DISPERSED marker in hex
     - N/A
     - N/A
     - N/A


10.2  Suppressed
----------------


**10.2.1**  A Suppressed unit has its movement halved, fires at -2 rFP, and reacts at -1 rFP.

.. container:: rule-guide

   **Why:** Bundles three separate penalties — movement, fire, and reaction — into a single status so one bad result (being Suppressed) has a broad, felt effect across everything the unit tries to do, not just one narrow stat.

   **Example:** A Suppressed Alpha with M2 moves at M1 (round down, Rule 2.5.1), fires at -2 rFP below its normal effective rFP, and reacts at -1 rFP if it spends RP — all three penalties apply from the same single status marker.

**10.2.2**  A Suppressed unit's effective Defence is reduced by 2.

.. container:: rule-guide

   **Why:** Adds a defensive penalty on top of the offensive and mobility ones (Rule 10.2.1), since a unit already reacting to being shot at is also a softer target — Suppressed compounds a unit's vulnerability rather than only slowing it down.

   **Example:** Squad Bravo with a printed Defence of 3, once Suppressed, defends at an effective 1 (3 − 2) against further incoming fire until the status clears.

**10.2.3**  Suppressed status is removed during the Recovery Phase if the unit passes a recovery roll (Rule 5.2.4) or a leader successfully rallies it (Section 12).

.. container:: rule-guide

   **Why:** Gives Suppressed exactly two removal paths — the automatic Recovery Phase roll and an active leader rally — so a player always knows precisely what it takes to clear the status, rather than it fading on its own over time.

   **Example:** Alpha, Suppressed at the end of one turn, either passes its 1d6+Morale roll against threshold 3 in the next Recovery Phase (Rule 5.2.4), or has a leader spend an action to rally it away earlier (Section 12) — there's no third way for the marker to come off.

**10.2.4**  A Suppressed unit that receives a second Suppressed result is upgraded to Pinned.

.. container:: rule-guide

   **Why:** Escalates repeated suppression into a worse status rather than letting a second Suppressed result simply do nothing to an already-Suppressed unit — a unit under continued fire keeps getting worse off, not stuck at one static penalty.

   **Example:** Squad Bravo, already Suppressed, is fired on again and suffers another Suppressed result. Instead of remaining Suppressed, it is upgraded straight to Pinned (Rule 10.3) — a strictly worse status.

10.3  Pinned
------------


**10.3.1**  A Pinned unit cannot move and fires at -4 rFP.

.. container:: rule-guide

   **Why:** Makes Pinned a strictly harsher version of Suppressed's mobility and fire penalties (Rule 10.2.1) — no movement at all rather than halved, and a steeper rFP cut — matching Pinned's role as the next status up the severity ladder.

   **Example:** A Pinned unit with M2 cannot move at all this turn, unlike a merely Suppressed unit which could still move at half rate — and its fire suffers -4 rFP instead of Suppressed's -2.

**10.3.2**  A Pinned unit cannot spend RP for opportunity fire or other reactions.

.. container:: rule-guide

   **Why:** Removes reactive capability entirely rather than just penalizing it (compare Suppressed's -1 rFP reaction penalty, Rule 10.2.1) — a Pinned unit is treated as too suppressed to respond to anything happening around it at all.

   **Example:** A Pinned unit cannot spend RP on Opportunity Fire even against an enemy unit moving right past it in plain sight — Rule 10.3.2 rules that reaction out entirely, not just at a penalty.

**10.3.3**  A Pinned unit's effective Defence is reduced by 3.

.. container:: rule-guide

   **Why:** Steps the Defence penalty up from Suppressed's -2 (Rule 10.2.2) to -3, consistent with Pinned being the more severe status across every one of its effects, not just movement and fire.

   **Example:** Alpha with a printed Defence of 4, once Pinned, defends at an effective 1 (4 − 3) — a steeper cut than the same unit would take merely Suppressed.

**10.3.4**  Pinned status is removed during the Recovery Phase if the unit passes a recovery roll at threshold 10 (Rule 5.2.4).

.. container:: rule-guide

   **Why:** Sets a much higher recovery threshold than Suppressed's 3 (Rule 5.2 table), reflecting that shaking off being Pinned is meant to be genuinely hard without leadership help, not a near-automatic roll.

   **Example:** A regular unit (Morale modifier +0) needs a roll of 10 or better on 1d6 to clear Pinned unaided — effectively impossible without a leader's CMD bonus (Rule 5.2.6) added to the roll.

**10.3.5**  A Pinned unit that receives a Suppressed result remains Pinned (Pinned is worse than Suppressed; the result is absorbed).

.. container:: rule-guide

   **Why:** Prevents a worse status from ever being downgraded by a lesser one landing on top of it — Suppressed can only make things worse for a unit that isn't already at least that bad, never better or unchanged for one that's already Pinned.

   **Example:** A Pinned unit hit by fire that would normally cause Suppressed simply stays Pinned — the weaker result has no additional effect, similar to how Routing absorbs Suppressed/Pinned results (Rule 10.6.10).

10.4  Broken
------------


**10.4.1**  A Broken unit has been rendered Combat Ineffective. Its counter is removed from the map and placed in the BROKEN zone of the Casualty Track.

.. container:: rule-guide

   **Why:** Takes a Broken unit off the map entirely rather than leaving a degraded counter behind, since Broken represents a unit that has stopped functioning as a fighting force — unlike Dispersed (Rule 10.5), there's no marker left in the hex to represent lingering presence.

   **Example:** Once Alpha becomes Broken, its counter comes off the map completely and moves to the BROKEN zone of the Casualty Track — the hex it occupied is simply empty afterward.

**10.4.2**  A unit may become Broken through two distinct paths:

.. container:: rule-guide

   **Why:** Distinguishes the two different reasons a unit can become Broken — because it's physically used up (Rule 10.4.3) or because it psychologically gives out (Rule 10.4.4) — since the CI cause marker color and recovery odds (Rule 10.4.6) depend on which path occurred.

   **Example:** Two units can both end up Broken and off the map, but one got there by taking a final casualty on its rear face while the other got there by failing a morale check — the rules that follow track which happened via the marker color.

**10.4.3**  Physical break — the unit takes a final Casualty result while already on its rear face. Place a red CI cause marker in the unit's Casualty Track slot.

.. container:: rule-guide

   **Why:** Marks a break caused by actual attrition (a casualty result with no further face to reduce to) distinctly in red, since physical losses don't get the psychological-break recovery bonus (Rule 10.4.6) — the men are genuinely used up, not merely scattered.

   **Example:** A unit already on its rear face that suffers another Casualty result has nowhere further to reduce, so it breaks physically — its Casualty Track slot gets a red marker, not white.

**10.4.4**  Psychological break — the unit fails a morale check (see Section 15). Place a white CI cause marker in the unit's Casualty Track slot.

.. container:: rule-guide

   **Why:** Marks a break caused by morale failure distinctly in white, since a unit that broke psychologically rather than through physical losses is more likely to be reconstituted later (Rule 10.4.6's +1 recovery bonus) — the personnel are largely intact, just shaken.

   **Example:** A unit at full strength that fails a Section 15 morale check breaks even without having taken a step loss — its Casualty Track slot gets a white marker, reflecting that its men are still largely there, just combat-ineffective for now.

**10.4.5**  A Broken unit is placed face up if it was at full strength when broken, face down if it was on its rear face.

.. container:: rule-guide

   **Why:** Preserves the unit's strength state on the Casualty Track using the counter's own two faces, so if it's later reconstituted (Rule 10.7.3), the game already knows whether it returns at full or reduced strength without needing a separate record.

   **Example:** A full-strength unit broken by a psychological failure (Rule 10.4.4) sits face up on the Casualty Track; a unit already on its rear face when it physically broke (Rule 10.4.3) sits face down, keeping that reduced-strength information visible.

**10.4.6**  A Broken unit may not be rallied during the current scenario. It is available for between-scenario recovery rolls with a +1 bonus if the CI cause marker is white (psychological break).

.. container:: rule-guide

   **Why:** Makes Broken permanent for the rest of the current scenario — unlike Suppressed, Pinned, or Routing, there's no in-scenario recovery path — while still allowing psychologically-broken units a better chance of returning between scenarios, since their personnel weren't physically lost.

   **Example:** A unit broken this scenario stays off the map for its remainder no matter what; between scenarios, a white-marker (psychological) break gets +1 on its recovery roll (Section 13), while a red-marker (physical) break rolls at the normal rate.

10.5  Dispersed
---------------


**10.5.1**  A Dispersed unit has been rendered Combat Ineffective by close assault or melee morale failure. Its counter moves immediately to the DISPERSED zone of the Casualty Track in its current state — front face up if full strength when dispersed, rear face up if reduced.

.. container:: rule-guide

   **Why:** Gives close-assault and melee morale failure a distinct outcome from ranged-fire morale failure (Broken, Rule 10.4) — a unit scattered in melee isn't gone, just disorganized, which is why it gets its own recovery path (Rule 10.5.4) that Broken units don't.

   **Example:** A unit that fails morale during a close assault becomes Dispersed rather than Broken — its counter moves to the DISPERSED zone (preserving its current face) instead of the BROKEN zone, since it may yet rally back into the fight.

**10.5.2**  A serialised DISPERSED marker (e.g. GER-01, SOV-02) is placed in the hex where the unit was dispersed. The matching numbered box on the Casualty Track holds the unit's counter, linking map marker to counter unambiguously.

.. container:: rule-guide

   **Why:** Keeps a physical trace of a Dispersed unit on the map, unlike Broken (Rule 10.4.1) which removes the counter entirely — the serial number lets both players trace exactly which off-map counter a given map marker corresponds to, with no ambiguity when several units disperse in the same game.

   **Example:** Alpha, dispersed in hex C4, leaves a marker reading "GER-01" there; the Casualty Track's box numbered "GER-01" holds Alpha's actual counter, so anyone checking either location can find the other unambiguously.

**10.5.3**  The DISPERSED marker is not a combat unit. It cannot fire, move, or react. It exists solely to indicate that men are physically present in that hex.

.. container:: rule-guide

   **Why:** Makes clear the marker is inert bookkeeping, not a weakened unit still capable of acting — this prevents confusion with genuinely reduced but still-functioning units, and makes explicit what it can be used for (Rule 10.5.5's capture) versus what it cannot (anything a normal combat unit does).

   **Example:** An enemy unit can move adjacent to and capture a DISPERSED marker (Rule 10.5.5), but the marker itself never fires back, moves away, or reacts to that approach — it has no combat capability of its own.

**10.5.4**  A Dispersed unit that is not captured may attempt to rally during the Recovery Phase: roll 1d6 + Morale modifier (Rule 15.2.1a) vs threshold 5. On success, the counter returns to play at rear face (reduced strength) in the hex of the friendly RALLY POINT marker with the fewest hexes between it and the hex where this unit's own DISPERSED marker sits (Rule 12.6a), or in the hex where the DISPERSED marker was if no friendly RALLY POINT marker exists anywhere on the map. The DISPERSED marker is removed from its hex either way. On failure, the unit is captured (Rule 11.2a) and does not receive another rally attempt this scenario.

.. container:: rule-guide

   **Why:** Gives a Dispersed unit one real chance per turn to fight its way back in at a nearby rally point, at reduced strength, rather than leaving it dispersed forever or returning it at full strength for free — rallying costs a step, reflecting the men who don't make it back.

   **Example:** Squad Bravo's DISPERSED marker sits 3 hexes from one friendly RALLY POINT marker and 6 from another. On a successful rally roll, Bravo's counter returns to play at rear face in the nearer rally point's hex; on failure, Bravo is captured with no further rally attempts this scenario.

    *See also: Rule 11.2a (Administrative Capture), Rule 12.6a (Rally Point Action).*

**10.5.5**  An enemy unit that occupies or is adjacent to a DISPERSED marker may spend 1 AP to formally capture it (see Section 11).

.. container:: rule-guide

   **Why:** Lets an alert enemy grab dispersed personnel before they can rally, giving both sides a real race between the friendly rally attempt (Rule 10.5.4) and the enemy's capture opportunity — presence and initiative near a DISPERSED marker matter.

   **Example:** An enemy unit that moves adjacent to Squad Bravo's DISPERSED marker can spend 1 AP to formally capture it immediately, denying Bravo's side any further chance at the Recovery Phase rally roll.

**10.5.6**  A Dispersed unit that has not rallied by the end of the scenario is captured (Rule 11.2a).

.. container:: rule-guide

   **Why:** Closes out any Dispersed unit still unresolved when the scenario ends, so no unit is left in permanent limbo — if it hasn't rallied and hasn't been formally captured already, the scenario's end forces the same outcome.

   **Example:** A unit still sitting as a DISPERSED marker on the final turn, having failed or not yet attempted its rally roll, is simply counted as captured once the scenario concludes.

    *See also: Rule 11.2a (Administrative Capture).*

10.6  Routing
-------------


**10.6.1**  A routing unit is one that has failed a morale check and has a clear escape path. It has not yet left the map but is fleeing and no longer combat effective.

.. container:: rule-guide

   **Why:** Distinguishes Routing from the other morale-failure outcomes (Broken, Dispersed) by requiring an actual escape path — a unit that fails morale but has nowhere to flee ends up Broken or Dispersed instead, since Routing specifically models men running somewhere.

   **Example:** A unit that fails a morale check with open, cover-heavy ground behind it becomes Routing and flees across the map; the same failed check for a unit surrounded with no clear path out would instead follow Rule 10.4 or 10.5.

**10.6.2**  Place a ROUTING marker on the unit. The unit remains on the map as a counter.

.. container:: rule-guide

   **Why:** Keeps a routing unit visible and trackable as a real counter on the map, unlike Broken (removed entirely, Rule 10.4.1) — a routing unit is still physically present and fleeing, which matters for both players tracking where it goes.

   **Example:** Alpha, now Routing, keeps its counter on the map with a ROUTING marker attached — an opponent can still see and potentially intercept it as it flees, unlike a Broken unit which simply vanishes from the map.

**10.6.3**  A routing unit must move D3 hexes directly away from the nearest visible enemy unit each time it is activated. Movement follows the most cover-heavy route available.

.. container:: rule-guide

   **Why:** Makes rout movement directional and somewhat random rather than fully player-controlled, since fleeing troops aren't calmly picking the tactically optimal route — they're running away from the nearest threat, seeking whatever cover is available along that general direction.

   **Example:** Alpha routs with an enemy unit visible to its north. Its move rolls D3 and it flees roughly southward, taking whatever cover-heavy path in that direction is available, rather than the player choosing Alpha's exact destination freely.

**10.6.3a**  Rout movement is self-executing: when the owning player passes for the final time in the Action Phase (Rule 5.6.2), every friendly routing unit that was not activated this turn immediately makes its Rule 10.6.3 move at no AP cost — fleeing men do not wait for orders, and a routing counter can never simply be parked. Activating a routing unit earlier in the turn (1 AP) remains legal to control **when** in the turn it moves; the flight itself is not optional.

.. container:: rule-guide

   **Why:** Closes the loophole of simply never activating a routing unit to keep it motionless in a convenient hex — its flight happens one way or another, either under the player's chosen timing (for 1 AP) or automatically for free once the player is done passing for the turn.

   **Example:** A player with a routing unit they'd rather not move spends no AP on it and passes out the rest of their turn; that routing unit still makes its D3-hex flight move automatically and for free once the final pass occurs (Rule 5.6.2) — it was never actually optional to skip.

**10.6.4**  A routing unit cannot fire, cannot react, and cannot be used for any action except movement.

.. container:: rule-guide

   **Why:** Strips a routing unit down to pure flight — no fighting, no reacting — since a unit that has broken and run is modeled as entirely focused on escape, unlike Pinned (Rule 10.3) which at least retains a (heavily penalized) ability to fire.

   **Example:** A routing unit passed directly by an enemy squad cannot spend RP for Opportunity Fire against it, and cannot be declared into a Fire action even voluntarily — its only legal action is the forced flight movement of Rule 10.6.3.

**10.6.5**  A routing unit that reaches the friendly map edge is removed from the map and placed in the BROKEN zone of the Casualty Track with a white CI cause marker.

.. container:: rule-guide

   **Why:** Gives Routing a clean escape outcome — reaching safety off the friendly edge converts the unit to Broken with the psychological-break marker, since it survived but is no longer part of the current scenario, matching the recovery-bonus logic of Rule 10.4.6.

   **Example:** A routing unit that flees all the way to the friendly map edge leaves play and joins the BROKEN zone with a white marker, eligible for the psychological-break recovery bonus between scenarios (Rule 10.4.6).

**10.6.6**  A routing unit that reaches a hex containing a functional friendly leader may attempt an immediate rally: roll 1d6 + Morale modifier (Rule 15.2.1a) vs the leader's RAL value + 1. Success removes the ROUTING marker and the unit resumes normal status. Failure — the unit continues routing. Rallying a routing unit is as hard as rallying a pinned one, but a good leader in the path of the rout is far better odds than the Recovery Phase roll (Rule 10.6.7, threshold 6).

.. container:: rule-guide

   **Why:** Rewards a leader positioned in a routing unit's flight path with an immediate rally chance rather than making the unit wait for the next Recovery Phase — a leader who happens to be exactly where the rout is heading can stop it right there.

   **Example:** A routing unit flees directly into a hex containing a leader with RAL 4. It rolls immediately against a threshold of 5 (4 + 1) rather than waiting for the Recovery Phase's flat threshold of 6 (Rule 10.6.7) — a meaningfully better chance if that leader's RAL is strong.

**10.6.7**  During the Recovery Phase, routing units may attempt to rally at threshold 6 (roll 1d6 + Morale modifier ≥ 6, Rule 15.2.1a). A leader within command radius adds their CMD rating to this roll. Without a leader, a regular unit (modifier +0) rallies from rout only on a roll of 6 — routed troops rarely recover themselves; leaders bring them back.

.. container:: rule-guide

   **Why:** Gives every routing unit a fallback rally chance each Recovery Phase even without the lucky positioning Rule 10.6.6 requires, but keeps the odds deliberately harsh for a leaderless unit — routing is meant to be difficult to reverse without active leadership.

   **Example:** A leaderless regular routing unit needs to roll exactly a 6 on 1d6 each Recovery Phase to rally — only about a 17% chance per attempt — while a nearby leader's CMD rating meaningfully improves those odds.

**10.6.8**  A routing unit counts toward the force's CI total for Force Morale purposes (see Section 15.4).

.. container:: rule-guide

   **Why:** Treats a routing unit as effectively lost for the force's overall morale accounting even though its counter is still physically on the map (Rule 10.6.2) — it isn't fighting, so it shouldn't count as intact strength when Force Morale is assessed.

   **Example:** A side's Force Morale calculation (Section 15.4) counts a routing unit the same way it would count a Broken or Dispersed one, even though the routing unit's counter still sits on the map fleeing.

**10.6.9**  A unit with a ROUTING marker (Rule 10.6.2) still on the map when the scenario ends is captured (Rule 11.2a).

.. container:: rule-guide

   **Why:** Resolves any routing unit that never reached safety (Rule 10.6.5) or rallied (Rules 10.6.6-10.6.7) by the time the scenario ends, mirroring how an unresolved Dispersed unit is handled (Rule 10.5.6) — no unit is left in permanent limbo when the game concludes.

   **Example:** A unit still fleeing with a ROUTING marker on the final turn, having neither reached the map edge nor rallied, is simply counted as captured once the scenario ends.

**10.6.10**  Routing supersedes Suppressed and Pinned. When a ROUTING marker is placed, remove any SUPPRESSED or PINNED marker — the -3 Defence penalty of the Routing state (Rule 10.1) is flat and never stacks with other status penalties. A routing unit that receives a further Suppressed or Pinned result absorbs it with no additional effect (compare Rule 10.3.5); a Casualty result applies normally (step loss, or CI if already reduced). Routing units make **no** further Section 15 morale checks — a unit already fleeing cannot break twice; its remaining decision points are the rally rolls of Rules 10.6.6 and 10.6.7.

.. container:: rule-guide

   **Why:** Keeps status effects from stacking into an unmanageable pile of penalties once a unit is already routing — Routing is the worst status a unit can be in short of CI, so anything lesser just gets absorbed rather than adding on top, the same absorption logic Pinned already applies to Suppressed (Rule 10.3.5).

   **Example:** A routing unit hit by fire that would normally Suppress or Pin it simply keeps routing with no further penalty; if that same fire instead causes a Casualty result, the step loss (or CI) applies normally, since Casualty isn't a status effect being absorbed.

    *See also: Rule 11.2a (Administrative Capture), Rule 15.5.7 (Force Morale collapse is a scoring abstraction and does not itself place a ROUTING marker or trigger this rule).*

10.7  Combat Ineffective
------------------------


**10.7.1**  The term Combat Ineffective (CI) refers collectively to units in Broken or Dispersed status. Routing units count as CI for Force Morale purposes but remain on the map.

.. container:: rule-guide

   **Why:** Defines CI as an umbrella term spanning two genuinely different statuses (Broken and Dispersed) so other rules — Force Morale, campaign recovery — can refer to "CI" once instead of repeatedly listing both statuses, while still flagging Routing's special dual nature (counts for Force Morale, but stays on the map).

   **Example:** A side's CI total for Force Morale purposes (Section 15.4) adds up its Broken units, its Dispersed units, and its Routing units together, even though only the first two have actually left the map.

**10.7.2**  A CI result does not necessarily mean the unit's personnel are all killed. Historically, approximately 25% of WWII infantry casualties were killed in action; the remainder were wounded, captured, or dispersed. A CI counter represents a unit that has ceased to function as a tactical element, not a pile of corpses.

.. container:: rule-guide

   **Why:** Grounds the CI abstraction in the historical reality that most WWII infantry losses weren't deaths, which is what justifies CI units being recoverable at all (Rule 10.7.3) rather than permanently removed from the campaign — a CI unit represents disorganization and loss of function, not annihilation.

   **Example:** A unit that goes CI this scenario isn't treated as wiped out for campaign purposes — most of its personnel are assumed wounded, scattered, or captured rather than dead, which is exactly why Section 13's between-scenario recovery rolls exist for it.

**10.7.3**  CI units are tracked on the Casualty Track and may return to play through between-scenario recovery rolls depending on the Recovery Window (Section 13). Psychological breaks (white marker) recover at +1 to the roll.

.. container:: rule-guide

   **Why:** Gives CI status a path back into the campaign rather than making it permanent, with the recovery odds distinguishing physical losses from psychological ones (Rule 10.4.6) — a unit that broke mentally but is largely intact comes back somewhat more easily than one that took real physical losses.

   **Example:** A unit Broken with a white (psychological) CI cause marker gets +1 on its between-scenario recovery roll compared to an otherwise identical unit Broken with a red (physical) marker, reflecting that the white-marker unit's personnel are more likely to still be there to reconstitute.
