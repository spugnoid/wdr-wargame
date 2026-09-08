Section 19 — Vehicle Morale, Bail-Out and Capture
=================================================

Vehicle crews were not immune to morale failure. Isolated inside steel boxes, dependent on infantry support, facing weapons that could destroy them at ranges where they could barely see — crew morale was a genuine tactical factor. This section covers vehicle-specific morale triggers, bail-out procedure, and the treatment of abandoned and captured vehicles.

19.1  Vehicle Morale Checks
---------------------------


**19.1.1**  Vehicle morale checks use the same procedure as infantry: roll 1d6 + the crew's Morale modifier (Rule 15.2.1a) vs break threshold. A leader within command radius adds their CMD rating to the roll.

.. container:: rule-guide

   **Why:** Reuses the exact same morale-check mechanics from Section 15 for vehicle crews rather than a separate system, since a crew's will to keep fighting resolves the same way whether they're infantry or riding in a tank — only the specific triggers (Rule 19.1.2) and outcome (Rule 19.1.4) differ.

   **Example:** A vehicle crew making a morale check rolls 1d6 + its own Morale modifier, with any in-command-radius leader's CMD added — the identical procedure to an infantry unit's morale check (Rule 15.2.1), just applied to a vehicle's crew.

**19.1.2**  Vehicle-specific morale triggers:

.. container:: rule-guide

   **Why:** Gives vehicle crews their own distinct set of morale triggers rather than reusing infantry's exact trigger list, since a tank crew's psychological stresses are genuinely different — internal damage, loss of nearby infantry screening, watching another vehicle brew up — from what tests an infantry squad's resolve.

   **Example:** A vehicle that receives a penetrating hit this turn must make a morale check at threshold 4, even if that hit didn't produce a Casualty result — the sheer shock of being penetrated is itself a trigger, distinct from any of infantry's own trigger conditions (Rule 15.1 table).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Trigger**
     - **Break Threshold**
     - **Notes**
   * - Receives any penetrating hit this turn
     - 4
     - Crew shaken by internal damage
   * - Infantry support eliminated within 2 hexes
     - 3
     - Crew exposed without protection
   * - Adjacent friendly vehicle eliminated
     - 2
     - Witnessing catastrophic kill nearby
   * - Leader vehicle eliminated
     - 3
     - Loss of command
   * - Buttoned up (Pinned) for 2 consecutive turns
     - 3
     - Prolonged isolation and stress


**19.1.3**  Buttoned up isolation: a Pinned (buttoned up) vehicle cannot observe adjacent breaks by friendly vehicles or infantry — the crew cannot see outside. Cascade checks from nearby friendly units breaking do not apply while buttoned up.

.. container:: rule-guide

   **Why:** Exempts a buttoned-up crew from the psychological cascade effect (Rule 15.4) that spreads from watching nearby units break, since a crew sealed inside a closed vehicle genuinely cannot see what's happening outside — cascade specifically requires witnessing the event, and a buttoned-up crew can't.

   **Example:** Squad Bravo breaks near a Pinned (buttoned up) vehicle. That vehicle's crew makes no cascade morale check at all, unlike an unbuttoned vehicle or an infantry unit within LOS, which would have to (Rule 15.4.1).

**19.1.4**  Vehicle morale check failure produces a Bail-out (see Rule 19.2) rather than a Break or Rout. Vehicles do not rout — they are either fighting or abandoned.

.. container:: rule-guide

   **Why:** Gives vehicles their own distinct failure outcome instead of reusing infantry's Break/Rout split (Rule 15.3), since a vehicle crew that loses its nerve doesn't flee on foot inside the vehicle — it abandons the vehicle entirely, which is a fundamentally different physical event with its own procedure (Rule 19.2).

   **Example:** A vehicle crew that fails a morale check doesn't get a ROUTING marker and start fleeing across the map — instead, the crew bails out of the vehicle following the Bail-Out Procedure (Rule 19.2), leaving the vehicle itself behind.

19.2  Bail-Out Procedure
------------------------


**19.2.1**  Bail-out check trigger: during each Recovery Phase, any vehicle that is Suppressed or Pinned must pass a bail-out check.

.. container:: rule-guide

   **Why:** Adds a recurring automatic risk for any degraded vehicle, timed to the same Recovery Phase used for other automatic per-turn checks (Rule 5.2.8) — a crew that's been shaken or isolated doesn't just sit there indefinitely; each turn brings a fresh chance they decide to abandon ship.

   **Example:** A vehicle Suppressed at the end of a turn faces a bail-out check at the very next Recovery Phase, alongside whatever other recovery-related rolls are also happening that phase.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Vehicle status**
     - **Bail-out threshold**
     - **Notes**
   * - Suppressed
     - 3
     - Crew shaken but vehicle functional
   * - Pinned (buttoned up)
     - 4
     - Isolation and immobility accelerate the decision to bail — the harder check


**19.2.2**  Roll 1d6 + the crew's Morale modifier (Rule 15.2.1a) vs threshold. Leader CMD adds to roll as normal.

.. container:: rule-guide

   **Why:** Resolves the bail-out check with the same roll-plus-modifier-and-leader-bonus pattern used everywhere else in the rules, so a player already familiar with morale checks or recovery rolls applies exactly the same procedure here.

   **Example:** A vehicle's bail-out check rolls 1d6 plus the crew's Morale modifier, with any in-command-radius leader's CMD added on top — identical mechanics to a Recovery Phase morale roll, just against a bail-out threshold instead.

**19.2.3**  Success: crew holds. Vehicle status unchanged.

.. container:: rule-guide

   **Why:** Lets a successful bail-out check leave the vehicle exactly as it was, with no lingering effect, since holding firm against the temptation to abandon ship is simply the crew continuing to do their job — nothing new needs to be tracked.

   **Example:** A Suppressed vehicle that passes its bail-out check remains Suppressed exactly as before — the check's only possible effect is the negative one (bailing out), and passing it changes nothing.

**19.2.4**  Failure: crew bails out.

.. container:: rule-guide

   **Why:** States the single, binary consequence of a failed bail-out check plainly, since everything about how a bail-out actually plays out is spelled out in the following steps (Rules 19.2.5-19.2.9) — this rule just names the outcome that triggers all of them.

   **Example:** A vehicle that fails its bail-out check has its crew bail out — the specific mechanical steps that follow from that (Rules 19.2.6-19.2.9) all begin from this one failed roll.

**19.2.5**  Bail-out procedure on failure:

.. container:: rule-guide

   **Why:** Signals that the following rules (19.2.6-19.2.9) are the actual step-by-step mechanical procedure for what happens once a crew bails out — separating the trigger and outcome (Rules 19.2.1-19.2.4) from the specific physical changes to the map that follow.

   **Example:** Once a crew has failed its check and bailed out (Rule 19.2.4), the specific sequence of marker placements and crew handling that follows is exactly what Rules 19.2.6-19.2.9 define.

**19.2.6**  Place an ABANDONED marker on the vehicle counter. The vehicle remains in its hex — it is not removed from the map.

.. container:: rule-guide

   **Why:** Keeps the physical vehicle on the map as a distinct, potentially recoverable object rather than removing it, since an abandoned tank is still a real piece of equipment sitting there — just without a crew to operate it — that either side might later try to reclaim (Rule 19.4).

   **Example:** A vehicle whose crew bails out stays in its hex with an ABANDONED marker on it — it isn't destroyed or removed, just left without anyone to fight it.

**19.2.7**  Place a CREW counter in the same hex. The CREW counter represents the bailed-out crew.

.. container:: rule-guide

   **Why:** Gives the bailed-out crew their own separate physical presence distinct from the vehicle they abandoned, since the crew and the vehicle are now two independent things on the map — the personnel didn't vanish, they're just no longer inside the tank.

   **Example:** When a tank's crew bails out, a CREW counter appears in that same hex representing the men themselves — a distinct piece from the now-abandoned vehicle counter sitting in the same hex.

**19.2.8**  The CREW counter immediately routs using infantry routing rules — moves D3 hexes away from the nearest visible enemy unit. Place ROUTING marker on CREW counter.

.. container:: rule-guide

   **Why:** Treats the bailed-out crew exactly like routing infantry the instant they're outside the vehicle, since fleeing tank crewmen on foot are mechanically no different from any other routing troops — the same forced-flight rules (Section 10.6) apply immediately.

   **Example:** The instant a CREW counter appears, it immediately flees D3 hexes away from the nearest visible enemy, exactly as an infantry unit that just failed a morale check and started routing would (Rule 10.6.3).

**19.2.9**  The CREW counter follows all infantry routing rules (Section 10.6) for subsequent turns including rally attempts.

.. container:: rule-guide

   **Why:** Keeps the bailed-out crew fully inside the existing routing/rally/capture framework for as long as it remains on the map, so there's no separate crew-specific ruleset needed for anything that happens to it after the initial bail-out — Section 10.6 already covers the whole lifecycle.

   **Example:** A bailed-out crew can attempt to rally at a friendly leader (Rule 10.6.6) or during the Recovery Phase (Rule 10.6.7) exactly as any other routing infantry unit would, and is captured under the same rules (Rule 11.2a) if it's still routing when the scenario ends.

19.3  Abandoned Vehicles
------------------------


**19.3.1**  An ABANDONED vehicle counter remains in its hex. It has the following states:

.. container:: rule-guide

   **Why:** Gives an abandoned vehicle three distinct states rather than one generic "abandoned" label, since a functional but crewless tank, a damaged one, and a destroyed one represent genuinely different tactical possibilities — one might be captured intact, another needs repair, and the third is simply gone for good.

   **Example:** A vehicle bailed out while otherwise undamaged sits as a fully functional ABANDONED state, potentially crewable by an enemy CREW counter (Rule 19.4) — a vehicle that later takes a MOB or GUN kill while abandoned instead moves to the worse DAMAGED state.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **State**
     - **Marker**
     - **Condition**
   * - ABANDONED
     - ABANDONED marker
     - Functional vehicle, no crew — can potentially be crewed
   * - DAMAGED
     - ABANDONED + damage marker
     - MOB or GUN kill vehicle with no crew
   * - DESTROYED
     - Counter removed
     - Catastrophically killed — not recoverable


**19.3.2**  An ABANDONED vehicle provides cover to infantry in the same hex (+2 cover — hull defilade) but is not a combat unit.

.. container:: rule-guide

   **Why:** Lets an abandoned vehicle's hulk still serve a tactical purpose — real hull defilade for infantry sheltering behind it — while making clear it can't fight back or take actions itself, since it's an inert obstacle now, not a functioning combat unit.

   **Example:** An infantry squad taking cover in the same hex as an ABANDONED vehicle gets +2 cover from the hull, but that vehicle contributes no fire, no Defence value of its own beyond that bonus, and cannot act.

**19.3.3**  Enemy units can move through an ABANDONED vehicle hex normally. They may attempt to capture it (see Rule 19.4).

.. container:: rule-guide

   **Why:** Treats an abandoned vehicle as passable terrain rather than an obstacle blocking movement, since it's just a hulk with no crew to contest the ground — but leaves the door open for an enemy with the right assets (a CREW counter, Rule 19.4.2) to actually take possession of it rather than just walking past.

   **Example:** An enemy unit can move freely through a hex containing an ABANDONED vehicle as if it weren't there for movement purposes, but that same enemy side could instead spend the effort to attempt formally capturing the vehicle under Rule 19.4.

19.4  Vehicle Capture
---------------------


**19.4.1**  An enemy unit in the same hex as or adjacent to an ABANDONED vehicle may attempt capture by spending 1 AP.

.. container:: rule-guide

   **Why:** Prices a capture attempt at a small, real AP cost so it competes with a side's other actions for the turn, similar to how accepting a Dispersed unit's surrender costs 1 AP (Rule 11.2.1) — taking possession of enemy equipment is a deliberate action, not free.

   **Example:** An enemy unit adjacent to an abandoned tank can spend 1 AP to attempt capture, rather than that being an automatic or free consequence of simply being nearby.

**19.4.2**  Vehicle capture requires a CREW counter of the capturing nation — representing trained vehicle crew waiting for a replacement vehicle. Regular infantry cannot crew an unfamiliar vehicle without specialist training.

.. container:: rule-guide

   **Why:** Restricts vehicle capture to units specifically representing trained crew rather than any nearby infantry, since actually operating a captured vehicle's unfamiliar controls, ammunition, and mechanics requires the kind of specialist knowledge ordinary infantry simply don't have.

   **Example:** A rifle squad adjacent to an abandoned enemy tank cannot attempt to crew it at all — only a CREW counter of the capturing nation, representing trained tank crew, is eligible to try.

**19.4.3**  Capture attempt: move the CREW counter into the vehicle hex (costs 1 AP). Roll 1d6 + the CREW counter's Morale modifier (Rule 15.2.1a) vs threshold 5.

.. container:: rule-guide

   **Why:** Requires the crew to physically occupy the vehicle's hex before attempting to crew it — you can't operate a vehicle from a distance — and gives the attempt genuine uncertainty via a roll, since figuring out an unfamiliar enemy vehicle's controls under combat pressure isn't guaranteed to succeed.

   **Example:** A CREW counter spends 1 AP moving into the abandoned vehicle's hex, then rolls 1d6 plus its own Morale modifier against threshold 5 to see whether the crew successfully gets the vehicle running.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - ≥ 5
     - Vehicle operational next turn at reduced effectiveness: Morale -1, -1 to all fire actions
   * - < 5
     - Vehicle not operational this scenario — crew cannot figure out unfamiliar controls in time


**19.4.4**  Special Beutepanzer (captured equipment) units: some scenarios may include dedicated captured-equipment crew counters that can attempt to crew enemy vehicles at only -1 penalty to the roll instead of the standard difficulty. This is scenario-defined.

.. container:: rule-guide

   **Why:** Reflects the historical fact that some forces (notably German Beutepanzer units) developed genuine specialization in operating captured enemy equipment, giving scenario designers a way to model that specific historical capability with a smaller penalty rather than the standard difficulty every other crew faces.

   **Example:** A scenario featuring German forces with a documented Beutepanzer program can include a specialized crew counter that only takes -1 to its capture roll, reflecting real familiarity with captured Soviet equipment, distinct from an ordinary crew attempting the same capture at standard difficulty.

**19.4.5**  A captured vehicle cannot enter service in the same scenario even if the crewing roll succeeds — the crew needs the remainder of the turn to familiarise with the vehicle. It is available from the following turn onward.

.. container:: rule-guide

   **Why:** Delays a successfully captured vehicle's actual availability by one turn even after a successful roll, reflecting that getting a vehicle running is only the first step — genuinely learning to fight effectively in an unfamiliar machine takes more than the same turn's remaining minutes.

   **Example:** A crew that successfully captures an enemy vehicle on Turn 5 cannot use it in combat until Turn 6 — the success unlocks the vehicle for future use, not immediate action.

19.5  Campaign Treatment of Captured Vehicles
---------------------------------------------


**19.5.1**  Captured vehicles secured at scenario end go to the CAPTURED zone of the campaign track.

.. container:: rule-guide

   **Why:** Extends the same Casualty Track CAPTURED zone concept already used for captured personnel (Rule 13.1) to captured vehicles, so the campaign layer tracks both kinds of captured assets through one consistent system rather than a separate parallel tracker just for equipment.

   **Example:** A vehicle successfully crewed and held by the capturing side at scenario end moves into the CAPTURED zone of the campaign track, the same zone that holds captured personnel counters from Section 11.

**19.5.2**  Between scenarios, roll 1d6 + capturing force maintenance quality:

.. container:: rule-guide

   **Why:** Gives a captured vehicle's long-term usability a real, uncertain outcome driven by the capturing side's own maintenance capability, since keeping foreign equipment running long-term depends heavily on spare parts, trained mechanics, and logistics that vary meaningfully between forces.

   **Example:** Two identical captured vehicles held by forces with different maintenance quality modifiers roll on the same table but with different bonuses — the better-maintained force's vehicle is more likely to end up fully operational than the same equipment in less capable hands.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1–2
     - Non-operational — vehicle cannot be used (parts unavailable, too damaged to repair quickly)
   * - 3–4
     - Operational — available as replacement asset at Morale -1, fire -1
   * - 5–6
     - Fully operational — enters campaign pool at standard stats


**19.5.3**  Different nations had different abilities to operate captured equipment. Germans were notably effective at pressing captured Soviet vehicles into service (Beutepanzer programme). Soviets used captured German equipment less systematically. This is reflected in the maintenance quality modifier — scenario designer assigns appropriate values.

.. container:: rule-guide

   **Why:** Leaves the actual maintenance quality modifier as a scenario-designer choice rather than a fixed universal value, since different nations' real historical capacity for operating captured equipment varied enough that a single hardcoded number couldn't fairly represent both a highly systematic program and a more ad hoc one.

   **Example:** A scenario designer modeling German forces might assign a favorable maintenance modifier reflecting the historical Beutepanzer program, while a scenario featuring a force with less systematic captured-equipment handling would assign a less favorable one for the same Rule 19.5.2 roll.

19.6  Vehicle Experience and Quality
------------------------------------


**19.6.1**  Vehicle crew quality follows the same BTV/EM/MM framework as infantry (Section 1.3 definitions). Quality degrades with replacement crew and builds through combat experience using the same campaign mechanics.

.. container:: rule-guide

   **Why:** Reuses the exact same experience-tracking framework infantry uses (Section 1.3, Rule 13.5.2's EM system) for vehicle crews, so the campaign layer's experience mechanics don't need a separate parallel system just for vehicles — a crew's experience works the same way whether they walk or ride.

   **Example:** A tank crew that survives a CI-free streak of scenarios builds EM and eventually promotes in Crew Quality exactly the way an infantry unit would (Rule 13.5.2a) — the same campaign mechanics, applied to a vehicle crew's roster entry instead of a squad's.

**19.6.2**  Key differences from infantry experience:

.. container:: rule-guide

   **Why:** Flags that despite sharing the same overall framework (Rule 19.6.1), vehicle crews have several genuinely distinct mechanics of their own — the rules that follow (19.6.3-19.6.6) are the specific places where vehicle experience diverges from the infantry baseline.

   **Example:** A player already comfortable with infantry morale and cascade rules still needs to check Rules 19.6.3-19.6.6 specifically, since those are the vehicle-specific exceptions the shared framework doesn't automatically cover.

**19.6.3**  Crew isolation: buttoned-up crews cannot observe cascading morale failures around them. A Pinned vehicle does not receive cascade checks from adjacent infantry or vehicle breaks — the crew is literally blind to surrounding events.

.. container:: rule-guide

   **Why:** Restates Rule 19.1.3's buttoned-up isolation principle here as one of the key differences from infantry experience, since infantry units — even Suppressed or Pinned ones — can still generally see nearby events in a way a sealed, buttoned-up tank crew cannot.

   **Example:** An infantry unit that's Pinned still makes cascade checks when it witnesses a nearby break (subject to LOS, Rule 15.4.1); a Pinned (buttoned up) vehicle makes none at all, regardless of what happens nearby, since its crew simply can't see out.

**19.6.4**  Vehicle condition effect on crew morale: a reliable vehicle counter (scenario-flagged as proven design) adds +1 to all vehicle morale checks. A breakdown-prone vehicle (scenario-flagged) subtracts -1. This represents crew confidence in their equipment — real and historically significant.

.. container:: rule-guide

   **Why:** Gives a crew's trust in their own machine a real mechanical effect on morale, distinct from crew quality itself — a veteran crew in an unreliable vehicle still faces a real morale penalty, since equipment confidence and personnel experience are two separate, independently-real factors.

   **Example:** A scenario flagging a specific vehicle model as historically reliable gives every crew in that vehicle +1 on morale checks; a different scenario flagging a breakdown-prone model applies -1 instead, regardless of how experienced the crew inside otherwise is.

**19.6.5**  Loss of infantry support trigger (Rule 19.1.2) has no infantry equivalent. Combined arms doctrine exists specifically because tank crews were vulnerable without infantry screening against close-range AT threats. The game enforces this doctrine mechanically — tanks that advance without infantry face genuine morale risk.

.. container:: rule-guide

   **Why:** Names one specific trigger from Rule 19.1.2's table (loss of nearby infantry support) as having no infantry counterpart, since infantry units don't experience the same specific vulnerability to being caught alone that tanks do without protective infantry screening against close-range ambushes.

   **Example:** A tank advancing without any friendly infantry within 2 hexes faces a genuine morale trigger the moment that support is lost — an infantry squad in the same isolated position triggers no equivalent check, since that specific vulnerability is purely a vehicle one.

**19.6.6**  Vehicle cascade rule: when a vehicle is eliminated within 2 hexes of another friendly vehicle, the surviving vehicle must make a cascade morale check at threshold 2 (Rule 15.4.2, same as infantry cascade) ONLY if it is not currently Pinned (buttoned up). A Pinned vehicle's crew cannot see the catastrophic kill outside. This asymmetry between buttoned and unbuttoned vehicles is historically accurate and tactically significant.

.. container:: rule-guide

   **Why:** Reuses the infantry cascade mechanic (Rule 15.4.2) rather than inventing a separate vehicle cascade system, while still respecting the buttoned-up visibility exemption established in Rule 19.6.3 — a Pinned crew that can't see surrounding events can't be shaken by a kill it never witnessed.

   **Example:** Alpha (unbuttoned) is parked 1 hex from Squad Bravo's supporting tank when that tank is destroyed — Alpha must make a threshold-2 cascade check. If Alpha had been Pinned (buttoned up) at the moment of the kill, no cascade check would be required at all.

19.7  Representative 1943 Vehicle Counters
------------------------------------------


*Hull/Turret AV and own-gun PEN values below are computed by* `counters/armor_calc/` *(Rule 17.2.5) and reflect the current Hull/Turret AV split, not the flat single-facing figures this table originally showed. This is a compact "at a glance" comparison — Front facing, AV-vs-Capped only, one representative range band. For AV-vs-Tungsten, Side/Rear facings, full range-band PEN, and the full Gunnery Table across every crew quality, see* `roster_output.csv`, `gun_curves_output.csv`, *and* `vehicle_fire_thresholds_output.csv` *in that directory. TRAV, M#, MG fire line, and Morale are unrelated to the armour/gunnery redesign and are carried over unchanged from this table's original values; HE rFP is recomputed fresh from each vehicle's actual gun calibre (Rule 18.8.4) since the previous figures included at least one confirmed error (see note below).*

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Vehicle**
     - **Main Gun**
     - **Hull Front AV**
     - **Turret Front AV**
     - **Gun PEN @ 500m**
     - **TRAV**
     - **M#**
     - **HE**
     - **MG**
     - **Morale**
   * - Panzer IV Ausf H
     - 75mm KwK40 L48
     - 64.9
     - 78.9
     - 119.6
     - 3
     - M3
     - 4
     - 4 ⬡3 -1
     - 6
   * - Panzer III Ausf M
     - 50mm KwK39 L60
     - 51.4
     - 57.8
     - 69.0
     - 3
     - M3
     - 3
     - 4 ⬡3 -1
     - 6
   * - Tiger I Ausf E
     - 88mm KwK36
     - 102.0
     - 143.0
     - 137.4
     - 2
     - M2
     - 4
     - 4 ⬡3 -1
     - 6
   * - StuG III Ausf G
     - 75mm KwK40 L48
     - 87.1
     - — (casemate)
     - 119.6
     - 0
     - M3
     - 4
     - 3 ⬡3 -1
     - 6
   * - T-34 Model 1943
     - 76mm F-34
     - 93.7
     - 55.8
     - 72.2
     - 3
     - M3
     - 4
     - 3 ⬡3 -1
     - 5
   * - T-34/85 (late 1943)
     - 85mm D-5T
     - 93.7
     - 146.0
     - 119.8
     - 3
     - M3
     - 4
     - 3 ⬡3 -1
     - 5
   * - KV-1S
     - 76mm ZIS-5 (modelled on F-34 curve — Rule 18.12(f))
     - 85.2
     - 129.1
     - 72.2
     - 1
     - M2
     - 4
     - 3 ⬡3 -1
     - 5
   * - SU-85
     - 85mm D-5S (modelled on D-5T curve — Rule 18.12(f))
     - 75.5
     - — (casemate)
     - 119.8
     - 0
     - M3
     - 4
     - 3 ⬡3 -1
     - 5
   * - Sherman M4A1 (75mm)
     - 75mm M3 L31
     - 76.7
     - 89.0
     - 77.9
     - 3
     - M3
     - 4
     - 4 ⬡3 -1
     - 6
   * - Sherman M4A3 (76mm)
     - 76mm M1
     - 115.5
     - 93.6
     - 117.5
     - 3
     - M3
     - 4
     - 4 ⬡3 -1
     - 6
   * - Sdkfz 251 half-track
     - — (MG only, no main gun)
     - 14.3
     - — (no turret)
     - —
     - —
     - M4
     - —
     - 3 ⬡3 -1
     - 5
   * - T-70 light tank
     - 45mm 20K L46 (APBC)
     - 44.0
     - 30.5
     - 59.3
     - 3
     - M4
     - 2
     - 3 ⬡3 -1
     - 5

*HE corrections: Tiger I Ausf E's 88mm gun gives HE rFP = ROUND(88/20) = 4 by Rule 18.8.4's own stated formula and worked example ("88mm = 4") — this table previously printed 5, a plain arithmetic error unrelated to the armour redesign, now fixed. Panzer III Ausf M's 50mm gun gives exactly 2.5, a genuine rounding-convention tie; resolved as 3 (round-half-up) for consistency with this project's established convention elsewhere (Excel-style rounding, not Python's round-half-to-even) — previously printed 2, flagged here as a judgement call rather than a silent change.*

*Known gap: Panther Ausf G's real, sourced Hull Front AV (229.1) / Turret Front AV (249.2) and own-gun PEN @ 500m (158.6mm, 75mm KwK42 L70) are already in* `armor_calc` *'s roster output, but this vehicle was never added to this table. Deliberately not added here either — TRAV, M#, and MG fire line for Panther would need real game-design judgement (not just tool output) to set consistently with the rest of this table, and inventing them here would be a guess dressed up as data. Worth a real design pass, not a quiet addition.*

*For the current, correctly-resolved Sherman 76mm vs. Tiger I and T-34/85 vs. Tiger I matchups at 400 yards (both were "contested"/"marginal" under the old system for reasons the new Hull/Turret split now makes explicit), see Rule 18.12(d) — the old flat "PEN value revised" footnote this table previously carried referred to a dice-notation AP PEN format that no longer exists under the current resolution model.*
