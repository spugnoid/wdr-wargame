Section 11 — Prisoners and Surrender
====================================

11.1  Surrender Conditions
--------------------------


**11.1.1**  A Dispersed unit (represented on the map by a serialised DISPERSED marker) may surrender to an adjacent or same-hex enemy unit.

.. container:: rule-guide

   **Why:** Limits surrender to units already Combat Ineffective via Dispersal (Rule 10.5), since a unit still fighting has no reason to surrender — the DISPERSED marker itself is what makes an enemy unit eligible to be taken prisoner in the first place.

   **Example:** Squad Bravo, now represented by a DISPERSED marker after failing a close-assault morale check, can be approached and formally captured by an adjacent or same-hex enemy unit — a unit that is still Suppressed or Pinned but not Dispersed cannot be surrendered to this way.

**11.1.2**  Dispersed units do not automatically surrender — they may attempt to rally (Rule 10.5.4) or remain in place until acted upon.

.. container:: rule-guide

   **Why:** Keeps a Dispersed unit's fate open until something actually happens to it — it isn't captured just by existing in that state, so both sides have a real window in which rally attempts (Rule 10.5.4) and enemy capture attempts (Rule 11.2) race against each other.

   **Example:** A DISPERSED marker can sit in its hex for a turn or more, still eligible for its owning side's Recovery Phase rally roll, right up until an enemy unit formally accepts its surrender (Rule 11.2.1) or the scenario ends.

11.2  Accepting Surrender
-------------------------


**11.2.1**  A friendly unit may formally accept the surrender of a Dispersed enemy unit by spending 1 AP while in the same hex as or adjacent to the DISPERSED marker.

.. container:: rule-guide

   **Why:** Prices formal capture at 1 AP so it competes with a side's other actions for the same turn — accepting a surrender is a deliberate choice with an opportunity cost, not a free side effect of being near a DISPERSED marker.

   **Example:** Alpha, adjacent to an enemy DISPERSED marker, spends 1 AP to formally accept its surrender rather than spending that same AP on a Fire action elsewhere.

**11.2.2**  On acceptance, the DISPERSED marker is removed from the map and the corresponding counter on the Casualty Track moves to the CAPTURED zone. A POW marker indicating nation and prisoner count is placed in the hex.

.. container:: rule-guide

   **Why:** Converts the abstract DISPERSED marker into a concrete POW marker at the moment of capture, tracking both the counter's new campaign status (CAPTURED zone) and the physical prisoners now present in the hex that need guarding (Rule 11.3).

   **Example:** When Alpha accepts Squad Bravo's surrender, Bravo's DISPERSED marker is replaced by a POW marker showing Bravo's nation and prisoner count, and Bravo's counter on the Casualty Track moves from DISPERSED to CAPTURED.

**11.2.3**  The accepting unit immediately receives a GUARD marker.

.. container:: rule-guide

   **Why:** Automatically obligates the capturing unit to guard duty the instant it accepts a surrender, since prisoners don't guard themselves — this is what puts the new GUARD marker's restrictions (Rule 11.3) into effect right away rather than leaving a gap where prisoners are unguarded by default.

   **Example:** The moment Alpha formally accepts Squad Bravo's surrender, Alpha receives a GUARD marker and immediately falls under Rule 11.3's movement, assault, and fire restrictions for guarding units.

11.2a  Administrative Capture
-----------------------------

**11.2a.1**  A Dispersed unit whose rally roll fails (Rule 10.5.4), a Dispersed unit that has not rallied by the end of the scenario (Rule 10.5.6), a unit still Routing when the scenario ends (Rule 10.6.9), or a wounded leader captured on a second Casualty result (Rule 12.10.2), is captured automatically. No enemy unit needs to be present or adjacent, and no AP is spent.

.. container:: rule-guide

   **Why:** Gives several different unresolved-fate situations from other sections a single, consistent capture rule rather than leaving units in permanent limbo when no enemy happens to be present to formally accept a surrender (Rule 11.2.1) — the game world assumes the unit is picked up eventually, off-screen.

   **Example:** A Dispersed unit whose owning side never gets an enemy unit adjacent to its DISPERSED marker still ends up captured automatically once its rally roll fails, without any enemy AP ever being spent on it.

**11.2a.2**  If Dispersed, the counter — already resident in the Casualty Track's DISPERSED zone (Rule 10.5.2) — moves to the CAPTURED zone, and the DISPERSED marker is removed from the map. If Routing, the counter and its ROUTING marker are removed from the map together and the counter moves to the CAPTURED zone. If a wounded leader captured per Rule 12.10.2, the leader counter is removed from the map and moves to the CAPTURED zone. In every case, a POW marker is placed in the hex where the unit was captured.

.. container:: rule-guide

   **Why:** Spells out the specific bookkeeping for each of the three source situations named in Rule 11.2a.1, since a Dispersed unit, a Routing unit, and a wounded leader each start from a different map/track state and need slightly different marker cleanup to land in the same CAPTURED zone.

   **Example:** A Routing unit that's still fleeing when the scenario ends has both its counter and ROUTING marker removed from the map together and moved to CAPTURED — a different physical cleanup than a Dispersed unit, whose counter was already sitting in the DISPERSED zone and just needs to shift over.

**11.2a.3**  No GUARD marker is placed. Rule 11.3's guard requirements and Rule 11.4's escape attempts do not apply to a unit captured this way — there is no accepting unit to assign a GUARD marker to, and no guard relationship to escape from.

.. container:: rule-guide

   **Why:** Makes clear that administrative capture skips the entire guard/escape subsystem (Rules 11.3-11.4) rather than leaving an unguarded POW marker vulnerable to escape rolls it was never meant to face — there's no capturing unit in this process for the guard relationship to attach to.

   **Example:** A unit captured administratively because its rally roll failed still gets a POW marker in its hex (Rule 11.2a.2), but that marker faces no escape-attempt rolls under Rule 11.4 and no GUARD marker is ever assigned to it — unlike a formally-accepted surrender's POW marker, which does need an assigned guard (Rule 11.2.3).

    *See also: Rule 10.5.4 and Rule 10.5.6 (Dispersed rally failure or timeout), Rule 10.6.9 (still Routing at scenario end), Rule 12.10.2 (wounded leader captured on a second Casualty result).*

11.3  Guard Requirements
------------------------


**11.3.1**  A unit with a GUARD marker is guarding prisoners. The following restrictions apply:

.. container:: rule-guide

   **Why:** Introduces guard duty as a status that comes with real costs (Rules 11.3.2-11.3.4), so assigning a unit to guard prisoners is a genuine tactical tradeoff — that unit's combat effectiveness is now reduced for as long as it keeps its GUARD marker.

   **Example:** Alpha, now carrying a GUARD marker after accepting a surrender, is bound by the movement, assault, and fire restrictions of Rules 11.3.2-11.3.4 for as long as it holds that marker.

**11.3.2**  A guarding unit may not move more than 1 hex per activation.

.. container:: rule-guide

   **Why:** Slows a guarding unit down to reflect that it's managing prisoners, not moving freely — this cap also directly limits how fast prisoners can be marched off-map under escort (Rule 11.5.2), which uses the guard's own movement rate.

   **Example:** Alpha, guarding prisoners, can move at most 1 hex per activation even if its printed Move allowance is higher — the prisoners it's watching slow it down.

**11.3.3**  A guarding unit may not declare close assault.

.. container:: rule-guide

   **Why:** Keeps a guarding unit out of close-quarters combat entirely, since managing prisoners and conducting a close assault are mutually exclusive activities — a unit committed to guard duty isn't available for the game's most aggressive action type.

   **Example:** Alpha, holding a GUARD marker, cannot declare a Close Assault against an adjacent enemy unit even if the tactical situation would otherwise favor it — that option is off the table while guarding.

**11.3.4**  A guarding unit fires at -2 eFP on all fire actions.

.. container:: rule-guide

   **Why:** Penalizes a guarding unit's combat effectiveness across the board, on top of the movement and assault restrictions (Rules 11.3.2-11.3.3) — attention split between watching prisoners and fighting means every fire action suffers, not just the ones directly involving the prisoners.

   **Example:** Alpha's normal eFP against a target is reduced by 2 for every fire action it takes while still carrying its GUARD marker, regardless of what or whom it's firing at.

**11.3.5**  Guard scaling: all POW markers in a single hex form one **prisoner group**. A group of 1–2 POW markers requires 1 guard unit; 3–4 markers require 2 guard units; 5 or more require a dedicated escort element — at least 2 guard units, neither of which may take any offensive action. A guard unit covers a group if it is in the group's hex or adjacent to it; a guard unit counts toward only one group at a time (owning player assigns).

.. container:: rule-guide

   **Why:** Scales guard manpower requirements with prisoner numbers, since a handful of captives needs less watching than a large group — and the largest groups require a fully dedicated escort rather than units splitting attention with other duties, reflecting the real logistics of controlling many prisoners at once.

   **Example:** Three POW markers accumulated in one hex form a single prisoner group needing 2 guard units (per the 3-4 bracket); those two guards can be positioned anywhere in that hex or an adjacent one, as long as the owning player designates them as covering that specific group.

**11.3.6**  Assume Guard action (1 AP): any friendly combat unit in or adjacent to a prisoner group's hex may take a GUARD marker. This is how additional guards are added to meet Rule 11.3.5's scaling, and how guard duty is transferred — the relieved unit may remove its own GUARD marker in the same impulse at no cost once the replacement's marker is placed.

.. container:: rule-guide

   **Why:** Gives guard duty a defined way to both scale up (adding guards to meet Rule 11.3.5's requirements) and hand off (relieving one unit's guard duty with another's) within the normal action economy, so managing a prisoner group over multiple turns doesn't require special-case mechanics.

   **Example:** A single guard unit no longer meets Rule 11.3.5's requirement once a second POW marker joins its group. A second friendly unit spends 1 AP to Assume Guard, and once its marker is placed, the original guard can shed its own GUARD marker for free that same impulse if a swap (not an addition) was intended.

**11.3.7**  Releasing prisoners: a guarding unit may remove its GUARD marker at the start of any friendly impulse at no cost, abandoning its group. An under-guarded or unguarded group makes escape rolls per Rule 11.4 — walking away from prisoners has consequences, but no unit is ever locked into guard duty by the rules.

.. container:: rule-guide

   **Why:** Keeps guard duty fully reversible at will, so a player pressed for combat units can always free one up from guard duty — the cost isn't a rules restriction on releasing, it's the escape risk (Rule 11.4) that an abandoned or under-guarded group now faces.

   **Example:** Alpha drops its GUARD marker for free to rejoin the fight, leaving its prisoner group unguarded; that group now rolls for escape attempts each Recovery Phase (Rule 11.4.2) until someone resumes guarding it.

11.4  Escape Attempts
---------------------


**11.4.1**  Each turn that prisoners are held without the required number of guard units, an escape attempt occurs.

.. container:: rule-guide

   **Why:** Turns Rule 11.3.5's guard-scaling requirement into a real consequence rather than just a suggestion — falling short of the required guard count doesn't just look unsafe, it actually triggers a roll with a chance of losing the prisoners.

   **Example:** A prisoner group of 3 POW markers needs 2 guard units per Rule 11.3.5. If only 1 guard is assigned, that group is under-guarded and triggers an escape attempt every such turn until the guard count is met.

**11.4.2**  Roll 1d6 at the start of the Recovery Phase for each prisoner group (Rule 11.3.5) that lacks its required guard count.

.. container:: rule-guide

   **Why:** Places the escape roll at a fixed point in the turn sequence (the Recovery Phase, alongside other automatic recovery-type rolls, Rule 5.2.8) and scopes it per prisoner group, so a side with several under-guarded groups rolls separately for each one rather than one roll covering everything.

   **Example:** A side with two separate under-guarded prisoner groups rolls 1d6 once for each group at the start of the Recovery Phase — one roll's result has no bearing on the other group's fate.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1–2
     - Prisoners escape — the POW marker is removed and each captured counter it represents returns to the **owning** player's Casualty Track, BROKEN zone, with a white CI cause marker (they got away as scattered men, not a fighting unit) — eligible for between-scenario recovery (Rule 13.3). The captor loses all campaign value.
   * - 3–4
     - Prisoners remain but are unruly — the captor's units in or adjacent to the group's hex suffer -1 to all morale checks and recovery rolls until the end of the current turn
   * - 5–6
     - Prisoners remain quietly


11.5  Escort Procedure
----------------------


**11.5.1**  A guarding unit may escort prisoners off the map by moving toward the friendly rear map edge.

.. container:: rule-guide

   **Why:** Gives a guarding unit a proactive way to permanently resolve its prisoner group (Rule 11.5.4) instead of holding them indefinitely on the battlefield, where they remain vulnerable to escape rolls (Rule 11.4) for as long as the scenario runs.

   **Example:** Rather than parking Squad Bravo on guard duty near the front line for the rest of the scenario, its owning player can instead march the prisoner group toward the friendly rear edge to secure them for good.

**11.5.2**  Prisoners move with the guarding unit at the guard's movement rate (subject to guard movement restrictions in Rule 11.3.2).

.. container:: rule-guide

   **Why:** Ties escort speed to the guard's own already-reduced movement rate (Rule 11.3.2's 1-hex cap) rather than letting prisoners move independently, since the prisoners have no movement of their own — they're only moving because the guard is walking them along.

   **Example:** A guarding unit escorting prisoners moves at most 1 hex per activation (Rule 11.3.2), and the prisoners simply move with it — there's no separate, faster prisoner-movement rate to speed up the trip to the map edge.

**11.5.3**  When the guarding unit reaches the friendly rear map edge with prisoners, both are removed from the map. Prisoners are secured. The guard unit returns to play at the start of the following turn at the map edge.

.. container:: rule-guide

   **Why:** Removes both the guard and its prisoners from the active map once they reach safety, but only temporarily for the guard — the guard unit itself isn't lost, it's just briefly off-map before rejoining the fight, distinct from the prisoners' permanent departure (Rule 11.5.4).

   **Example:** Once Alpha marches its prisoner group off the friendly rear edge, both leave the map that turn; Alpha itself then reappears at the map edge at the start of the next turn, free of its guard duties and available for other actions.

**11.5.4**  Once escorted off-map, prisoners are permanently secured for this scenario. No further guarding is required.

.. container:: rule-guide

   **Why:** Makes off-map escort a genuine resolution rather than a temporary reprieve — once secured, a prisoner group is done for the scenario, no longer subject to escape rolls (Rule 11.4) or requiring any guard unit's continued attention.

   **Example:** A prisoner group successfully escorted off-map generates its campaign value (Rule 11.6) with no further risk — unlike a group still on the map, it can no longer roll to escape, be recaptured, or need reinforcement to meet Rule 11.3.5's guard scaling.

11.6  Campaign Value of Prisoners
---------------------------------


**11.6.1**  Secured prisoner markers (escorted off-map) generate Intelligence Points for the campaign.

.. container:: rule-guide

   **Why:** Gives the whole prisoner-handling subsystem a payoff beyond just removing enemy combat power — successfully securing prisoners feeds directly into the campaign layer, rewarding the effort of guarding and escorting rather than just capturing and abandoning them.

   **Example:** A side that invests the AP and guard units to escort its captured prisoners all the way off-map (Rule 11.5) earns Intelligence Points for the campaign; a side that merely captures prisoners and leaves them exposed to escape rolls (Rule 11.4) never reaches this payoff if they escape first.

**11.6.2**  1 Intelligence Point is awarded per secured POW marker, **once**, at the moment it is secured. Prisoners are interrogated when taken — they are not a renewable resource, and a stockpile of early captures does not compound across a long campaign.

.. container:: rule-guide

   **Why:** Caps Intelligence Point generation to a single one-time award per POW marker, so the mechanic doesn't become an ongoing engine a player could farm by holding prisoners longer or repeatedly interacting with the same marker — the value is extracted once, at securing, and that's it.

   **Example:** Securing a POW marker representing 3 captured personnel awards exactly 1 Intelligence Point, not 3, and holding that same secured group for additional turns generates no further points.

**11.6.3**  Intelligence Points may be spent between scenarios for the following benefits:

.. container:: rule-guide

   **Why:** Gives Intelligence Points a menu of tangible campaign-level uses so earning them (Rules 11.6.1-11.6.2) has a concrete payoff a player can plan around, rather than the points being a purely abstract score.

   **Example:** A side that secured 2 prisoner groups over a scenario has 2 Intelligence Points to spend between scenarios — enough to reveal an enemy unit's starting position (2 points) or to learn two different enemy unit types' quality (1 point each), the player's choice.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Intelligence Point Cost**
     - **Benefit**
   * - 1 point
     - Learn the quality level of one enemy unit type in the next scenario
   * - 2 points
     - Reveal the starting position of one enemy unit in the next scenario
   * - 3 points
     - Gain 1 Replacement Point (Rule 13.2.2a), spent the same way as any other

.. container:: rule-guide

   **Why:** Now that Rule 13.2.2a defines what a Replacement Point actually does, this row is enabled at a flat 1 point rather than the original draft's "equal to the prisoner count" — scaling with prisoner count would let a single lopsided scenario's captures outweigh the flat 1-per-campaign-turn baseline Resupply already provides (Rule 13.2 table), breaking the scarcity that design note E.100 deliberately built in. Confirmed with the designer.

   **Example:** A side spends 3 of its banked Intelligence Points between scenarios to gain 1 Replacement Point, then spends that point after a BROKEN-zone recovery roll exactly as it would spend one issued by Resupply (Rule 13.2.2a) — the source of the point doesn't change how it's used.
