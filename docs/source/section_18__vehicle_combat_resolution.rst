Section 18 — Vehicle Combat Resolution
======================================

Vehicle combat uses a dedicated resolution sequence that determines whether a round penetrates armour and what damage results. The sequence integrates with the existing fire resolution system — the same dice, the same result bands, the same graduated damage philosophy.

18.1  Resolution Sequence Overview
----------------------------------


**18.1.1**  When a weapon fires at a vehicle, resolve in this order:

.. container:: rule-guide

   **Why:** Fixes vehicle combat's resolution into one strict, numbered sequence so both players always resolve a shot the same six steps in the same order, regardless of how complex the underlying penetration math gets — the sequence itself never varies.

   **Example:** Every vehicle-vs-vehicle shot, whatever gun or ammunition is involved, works through the same six steps (Rules 18.1.2-18.1.7) in the same order — Gunnery Roll first, damage application last, always.

**18.1.2**  Step 1: Gunnery Roll. Roll to determine whether the round hits the target at all and, if so, whether it strikes the Hull or Turret profile. See Rule 18.1a. **If the result is a Miss, resolution ends here — the round has no further effect.**

.. container:: rule-guide

   **Why:** Puts the hit-or-miss question first and lets a Miss short-circuit the whole rest of the sequence, since there's no point calculating arcs, PEN, or damage for a shot that never connected at all.

   **Example:** A Gunnery Roll that comes up Miss ends resolution immediately — the attacker doesn't proceed to Step 2 or any later step, since nothing further needs to happen.

**18.1.3**  Step 2: Determine arc. Identify whether the attacker is in the target's front, side, or rear arc **of whichever profile (Hull or Turret) the Gunnery Roll selected in Step 1.** Use the corresponding AV value from that profile — AV-vs-Capped or AV-vs-Tungsten, matching the ammunition nature fired (Rule 17.2.3).

.. container:: rule-guide

   **Why:** Determines the arc specifically against whichever profile the Gunnery Roll already picked, not some separate averaged concept — the Hull's own facing arc and the Turret's own facing arc (via any TRAVERSED marker, Rule 17.5.5) can point in different directions on the same vehicle.

   **Example:** If the Gunnery Roll selected the Turret profile, the attacker's arc is determined relative to the turret's own facing (via its TRAVERSED marker, if any) — not the hull's facing arrow, even if those two happen to differ.

**18.1.4**  Step 3: Check TRAV. Confirm target vehicle's TRAV rating allows it to be engaged this turn. If TRAV is insufficient to cover the attacker's hex, the vehicle cannot return fire this impulse.

.. container:: rule-guide

   **Why:** Checks whether the target vehicle can even shoot back at this point in the sequence, since a target caught in an arc its own gun can't currently cover (Rule 17.4) is genuinely unable to return fire this impulse — this step is about the target's return capability, not the incoming shot's own resolution.

   **Example:** A TRAV 1 vehicle already facing forward that's engaged from its rear arc cannot traverse far enough to return fire this impulse — Step 3 confirms that limitation before any return-fire question comes up.

**18.1.5**  Step 4: Calculate effective PEN at range — read the printed PEN line for the ammunition nature fired at the actual range band (Rule 17.3.1).

.. container:: rule-guide

   **Why:** Reads the attacking round's actual penetrating power straight off its printed PEN line at the real range band, since that number — already computed from sourced ballistics (Rule 17.3.7) — is exactly what the later comparison against AV needs.

   **Example:** A gun firing Tungsten ammunition at 750m reads its printed Tungsten PEN value at the 750m band (or the next lower band if 750m isn't itself printed) — that becomes the effective PEN carried into Step 5.

**18.1.6**  Step 5: Check Shatter Gap and Schürzen if applicable (Rules 18.2a, 18.2b — optional/situational), then compare effective PEN to target AV and determine penetration outcome (Rule 18.2).

.. container:: rule-guide

   **Why:** Applies the two situational modifiers (Shatter Gap, Schürzen) before the core PEN-vs-AV comparison, since both of them change the effective numbers going into that comparison rather than adjusting its result afterward — order matters here.

   **Example:** A HEAT attack against a Schürzen-protected side arc has its effective PEN halved (Rule 18.2b.2) before comparison, not after — the halved value is what actually gets compared to the target's AV in the Rule 18.2 outcome table.

**18.1.7**  Step 6: Apply result using the vehicle damage table.

.. container:: rule-guide

   **Why:** Closes the sequence with a single final step — applying whatever damage table the penetration outcome pointed to — so every shot, however it resolved, ends the same way: reading off and applying a damage result.

   **Example:** A shot that resolved as a Full Penetration in Step 5 proceeds here to the Full Penetration Damage table (Rule 18.6), while a Contested roll that came up Partial Penetration instead proceeds to the Partial Penetration table (Rule 18.5) — different tables, same final step in the sequence.

18.1a  Gunnery Roll
--------------------


**18.1a.1**  Every vehicle-mounted gun counter prints a Gunnery Table: a Miss Threshold and a Hull Threshold for each range band, already calculated for that vehicle's own Crew Quality (Rule 18.1a.2). No separate lookup, chart, or calculation is required at the table — read the row for the actual range.

.. container:: rule-guide

   **Why:** Pre-bakes crew quality directly into each vehicle's own printed thresholds, the same design philosophy as the rest of Section 17-18's printed values — a player just reads two numbers off the counter for the actual range, with no calculation step of their own.

   **Example:** A player firing a specific gun at a specific range simply reads that gun's own printed Miss and Hull thresholds for that range band and rolls — the crew-quality adjustment behind those numbers was already applied when the counter was designed.

*Example (88mm KwK36, Regular crew — the actual computed rows from* ``vehicle_fire_thresholds_output.csv``):*

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Range**
     - **Result**
   * - 100m
     - Roll < 12: Miss. Roll 12–13: Turret. Roll ≥ 14: Hull.
   * - 250–500m
     - Roll < 12: Miss. Roll 12–14: Turret. Roll ≥ 15: Hull.
   * - 750m
     - Roll < 13: Miss. Roll 13–15: Turret. Roll ≥ 16: Hull.
   * - 1000m
     - Roll < 16: Miss. Roll 16–17: Turret. Roll ≥ 18: Hull.
   * - 1500m
     - Roll < 21: Miss. Roll 21: Turret. Roll ≥ 22: Hull.
   * - 2000m
     - Roll < 25: Miss. Roll 25: Turret. Roll ≥ 26: Hull.
   * - 2500m+
     - Automatic miss. No roll required.


**18.1a.1a**  Blank thresholds: a band with no printed Miss Threshold is an **automatic miss** (the shot is beyond the dice combination's resolution floor). A band with a Miss Threshold but no Hull Threshold means every hit at that range strikes the **Turret** — at extreme range only the taller profile presents. The Gunnery Table prints its own band set (typically 100/250/500/750/1000/1500/2000/2500m); the PEN lines use Rule 17.3.1's bands — the two are read independently.

.. container:: rule-guide

   **Why:** Gives blank cells in the Gunnery Table a real, deliberate meaning rather than an error state — a range too far for any roll to succeed becomes an automatic miss, and a range where only the taller Turret profile is realistically visible simply never rolls Hull, reflecting genuine long-range engagement geometry.

   **Example:** A vehicle's Gunnery Table showing no Hull Threshold at 1500m means every hit that range achieves strikes the Turret — the target's lower hull profile isn't a realistic target to hit at that distance.


**18.1a.2**  Crew Quality is derived from the firing vehicle's own Morale value (Rule 17.3.6): Morale 7+ = Elite, Morale 6 = Veteran, Morale 5 = Regular, Morale 3–4 = Green, Morale 2 or less = Militia. This is fixed at counter-design time, not chosen or looked up during play.

.. container:: rule-guide

   **Why:** Restates Rule 17.3.6's Morale-to-Crew-Quality mapping here specifically because it's the value that determined the printed Gunnery Table numbers a player is about to use — fixed permanently at design time so there's never a question of which quality tier applies mid-game.

   **Example:** A vehicle counter printed with Morale 5 has Regular Crew Quality baked into its Gunnery Table forever — nothing that happens to the vehicle during play changes which crew-quality tier its printed thresholds reflect.

**18.1a.3**  Roll 1d6+1d8+1d12 (the same combination used for every other fire attack, Rule 8.5.1) and compare to the Miss Threshold and Hull Threshold for the actual range to target, using the next lower printed range band if the exact range falls between two listed bands.

.. container:: rule-guide

   **Why:** Reuses the game's one universal dice combination (Rule 8.5.1) for the Gunnery Roll rather than introducing a separate roll type just for vehicle combat, keeping the game's whole fire-resolution system built on the same underlying randomness.

   **Example:** A Gunnery Roll and an ordinary infantry Fire action both roll the same 1d6+1d8+1d12 combination — only the target numbers and outcome table differ between the two.

**18.1a.4**  If the roll is below the Miss Threshold, the round misses. No further resolution — the round has struck terrain, passed over the target, or otherwise failed to connect.

.. container:: rule-guide

   **Why:** Ends resolution cleanly at the first failure point, since a shot that missed the target entirely has nothing further to determine — no profile, no arc, no damage — matching Step 1's own instruction in Rule 18.1.2.

   **Example:** A roll below the Miss Threshold simply means the round didn't connect at all — no further table or roll follows, the attack simply had no effect this impulse.

**18.1a.5**  If the roll meets or exceeds the Hull Threshold, the round strikes the target's Hull profile. If the roll is at or above the Miss Threshold but below the Hull Threshold, the round strikes the Turret profile instead. Proceed to Rule 18.1.3 using the indicated profile. Casemate vehicles (TRAV 0, no separate turret) always resolve against Hull regardless of roll — see Rule 17.1.2.

.. container:: rule-guide

   **Why:** Uses the same roll to decide both whether the shot connects and which profile it hits, since a single roll naturally produces a range of outcomes — a very high roll representing a solid, centered hit (Hull, typically the harder target to actually connect with cleanly) and a marginal hit landing on the more exposed Turret.

   **Example:** A roll that clears the Hull Threshold sends the shot against the target's Hull profile; a roll that only clears the lower Miss Threshold instead sends it against the Turret — but a casemate vehicle with no separate turret always resolves against Hull either way.

**18.1a.6**  Crossing target: if the target vehicle has a MOVED marker this turn and the attacker's line of fire falls in the target's Side arc, read the Gunnery Table one range band longer than the actual range (e.g. a shot at 750m against a crossing target uses the 1000m row instead).

.. container:: rule-guide

   **Why:** Makes a moving vehicle genuinely harder to hit from the side rather than adjusting the odds with a flat modifier — reading a longer, harder-to-hit range band captures that a vehicle crossing an attacker's field of fire is a fleeting, difficult shot, using the same table rather than a separate calculation.

   **Example:** A vehicle that moved this turn, engaged from the side at an actual range of 750m, has that shot resolved using the Gunnery Table's 1000m row instead — a strictly harder threshold, reflecting the difficulty of hitting a crossing target.

**18.1a.7**  Follow-up shot: if the firing unit's previous fire action this turn targeted the same vehicle and the firing unit has not moved since, read the Gunnery Table one range band shorter than the actual range (minimum: the shortest printed band). If both Rule 18.1a.6 and 18.1a.7 apply to the same shot, apply the crossing adjustment first, then the follow-up adjustment, to the resulting band.

.. container:: rule-guide

   **Why:** Rewards a stationary gun re-engaging the exact same target with an easier effective range band, since a crew that already has the target ranged in and hasn't had to reposition genuinely shoots more accurately on a repeat shot — and fixes the order of operations for the rare case where both adjustments apply to the same shot.

   **Example:** A stationary gun firing a second shot at the same vehicle it already engaged this turn reads its Gunnery Table one band shorter than the actual range; if that same target is also crossing (Rule 18.1a.6), the crossing adjustment lengthens the band first, and only then does the follow-up adjustment shorten the resulting band.

**18.1a.8**  A Gunnery Roll is not required for anti-infantry fire (Rule 18.8), infantry anti-tank weapons (Rule 18.9), or Overrun (Rule 18.11) — those retain their existing resolution procedures unchanged.

.. container:: rule-guide

   **Why:** Scopes the entire Gunnery Roll mechanism to vehicle-vs-vehicle gunnery specifically, leaving anti-infantry fire, infantry AT weapons, and Overrun to their own already-established resolution procedures — those situations don't involve one vehicle's gun trying to hit another vehicle's armor profile, so the Gunnery Roll's hit/profile question doesn't apply.

   **Example:** A tank firing its MG at infantry uses ordinary fire resolution (Section 8) against infantry Defence, with no Gunnery Roll involved at all — the Gunnery Roll is reserved for gun-vs-vehicle engagements.

**18.1a.9**  Rule 7.5.2's existing −2 rFP penalty for opportunity fire against a moving target does not stack with Rule 18.1a.6 when the target is a vehicle — the Gunnery Roll's own crossing-target adjustment replaces it for vehicle targets specifically (Rule 7.5.2a states this same exception from the movement side). Rule 7.5.2 continues to apply exactly as written when the target is infantry.

.. container:: rule-guide

   **Why:** Prevents double-penalizing a moving vehicle target with both the general moving-target rFP penalty and the vehicle-specific crossing-target band adjustment, since both mechanisms exist to model the same underlying difficulty — hitting a moving target — and applying both would overstate that difficulty for vehicles specifically.

   **Example:** Opportunity fire against a moving vehicle target applies only the Gunnery Table's crossing-target band shift (Rule 18.1a.6), not also the ordinary -2 rFP moving-target penalty; that same opportunity fire against moving infantry still applies the standard -2 rFP penalty exactly as Rule 7.5.2 always has.

    *Note: vehicles use their own MOVED marker (Rule 18.1a.6) tracking whether they have moved this turn — a simpler, unchanged concept distinct from the infantry MOVED/FIRED marker of Rule 6.5.1, which the Section 17-19 vehicle rules do not use.*

*NOTE: The Gunnery Roll reuses the exact 1d6+1d8+1d12 combination already rolled for every other attack in the game rather than introducing new dice. Below the dice combination's resolution floor (rarer than about 0.17%, the probability of rolling the single maximum value), a shot is an automatic miss rather than requiring an unrollable threshold.*

*NOTE: The crossing-target and follow-up-shot adjustments (18.1a.6–18.1a.7) trade some numerical precision for reusing the same printed table under all circumstances — no second table, no arithmetic, no die-roll modifier to remember.*

18.2  Penetration Outcomes
--------------------------


Compares effective PEN (Rule 17.3.1) against the AV of the profile and arc selected by the Gunnery Roll (Rule 18.1a).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **Outcome**
     - **Proceed to**
   * - Effective PEN ≥ AV + 10
     - Automatic penetration — no roll needed
     - Full penetration damage table
   * - Effective PEN ≥ AV
     - Contested — roll 1d6
     - Penetration roll table
   * - Effective PEN < AV
     - Non-penetrating hit — roll 1d6
     - Non-penetrating hit table
   * - Effective PEN < AV − 10
     - Bounce — no effect
     - No further resolution


*NOTE: the ±10mm margins restore the width the outcome bands had before the millimetre migration (the original ±3 was in the old 1-point≈10mm scale and was never rescaled — a 6mm total window against PEN values that move 8–10mm per range band made nearly every matchup a binary auto-penetration or bounce, and Rules 18.3/18.4 almost never fired). ±10mm is comparable to real penetration scatter at these armour thicknesses and keeps the Contested and Non-penetrating bands live at exactly the ranges where engagements were historically uncertain.*


18.2a  Shatter Gap (Optional Rule)
----------------------------------


*If this module is in use for the scenario:*

**18.2a.1**  Before applying Rule 18.2, check Shatter Gap if all of the following hold: (a) the firing ammunition is Capped, Uncapped AP, or Soviet APBC nature (not Tungsten/APDS, not HEAT); (b) the attacking gun's printed calibre (mm) does not exceed the target's AV in the profile/arc being hit.

.. container:: rule-guide

   **Why:** Scopes Shatter Gap to exactly the ammunition natures and calibre-to-armor ratio where the real phenomenon actually occurs — a projectile that shatters on impact rather than penetrating is specific to certain nose shapes and specific ratios of shell diameter to plate thickness, not a universal risk for every shot.

   **Example:** A Tungsten round never checks Shatter Gap at all, regardless of calibre or target armor — condition (a) excludes it outright, since Shatter Gap is specifically a kinetic-AP-family phenomenon.

*NOTE: condition (b) is a deliberate at-table simplification of the sourced eligibility ratio (shatter applies from T/D ≥ 0.8, i.e. calibre up to 1.25× AV). The simplified test exempts a narrow band of shots the source says could shatter (e.g. an 88mm gun against an 80mm plate); the calculation tool implements the full ratio — see* ``shatter_gap_failure`` *in* ``counters/armor_calc/formulas.py``.*

**18.2a.2**  If 18.2a.1's conditions hold, look up the target's AV on the Shatter Gap Table (player aid card) to find its Shatter Window — a lower and upper PEN value.

.. container:: rule-guide

   **Why:** Derives the specific PEN range where shattering occurs from the target's own AV, since the phenomenon depends on the relationship between the round's energy and the plate's resistance — a window keyed to AV captures that relationship without a separate calculation at the table.

   **Example:** A target with a given AV has a specific Shatter Window looked up from the player aid card — a different target AV produces a different window, since the shatter phenomenon shifts with the plate's own resistance.

**18.2a.3**  If effective PEN falls within the Shatter Window (inclusive), the shot is forced to a Non-Penetrating Hit (Rule 18.4), regardless of what Rule 18.2 would otherwise indicate. Proceed directly to 18.4 — do not consult 18.2 or 18.3 for this shot.

.. container:: rule-guide

   **Why:** Overrides whatever the normal PEN-vs-AV comparison would have produced when the shot falls inside the shatter window, since a projectile shattering on impact fails to penetrate regardless of how favorable the raw numbers otherwise looked — the physical reality of the round breaking apart takes precedence over the arithmetic.

   **Example:** A shot whose effective PEN would normally qualify as an Automatic Penetration under Rule 18.2, but which falls inside the target's Shatter Window, is instead forced to Non-Penetrating Hit — the shatter phenomenon overrides the numbers.

**18.2a.4**  If effective PEN falls outside the Shatter Window (either below it, or above it), resolve normally via Rule 18.2 — Shatter Gap does not apply.

.. container:: rule-guide

   **Why:** Confirms Shatter Gap only intervenes within its specific window, not universally — a shot too weak or too powerful for the shatter phenomenon to matter resolves through the ordinary PEN-vs-AV comparison unaffected.

   **Example:** A shot whose effective PEN is well above the target's Shatter Window (comfortably exceeding it) resolves through Rule 18.2 normally, likely as an Automatic Penetration — the round is powerful enough that the shatter risk simply doesn't apply at that PEN level.

*NOTE: This can only ever make an otherwise-favorable shot worse, never better — it has no effect on shots where PEN < AV already.*

18.2b  Schürzen (Standoff Skirt Armour)
----------------------------------------


**18.2b.1**  A vehicle counter with a Schürzen marker on a given Hull or Turret Side arc has standoff skirt armour protecting that arc against HEAT specifically.

.. container:: rule-guide

   **Why:** Marks Schürzen as a printed, arc-specific feature rather than a blanket vehicle-wide bonus, since real standoff skirt armor was historically mounted only on specific arcs of specific vehicles — the marker records exactly which arcs actually had it.

   **Example:** A vehicle counter with a Schürzen marker only on its Hull Side arc gets no protection benefit on its Turret Side or Rear arcs — the marker is precise about which arc the historical skirt armor actually covered.

**18.2b.2**  Before comparing effective PEN to AV (Rule 18.2), if the attack (a) uses HEAT ammunition of any kind — gun-fired HEAT round, Panzerfaust, Bazooka, PIAT — and (b) targets a Side arc bearing a Schürzen marker, halve the attacking weapon's effective PEN (round down) before proceeding.

.. container:: rule-guide

   **Why:** Models standoff armor's real mechanism — detonating a shaped charge early, before it reaches the main plate — as a straightforward PEN reduction applied before the normal comparison, since that's functionally what standoff armor does to a HEAT jet's effectiveness.

   **Example:** A Panzerfaust with 140mm PEN striking a Schürzen-protected Side arc has its effective PEN halved to 70mm (round down) before that value is ever compared against the target's AV-vs-HEAT.

**18.2b.3**  Schürzen has no effect on Capped, Uncapped AP, Soviet APBC, or Tungsten/APDS attacks, and no effect on any arc other than the marked Side arc.

.. container:: rule-guide

   **Why:** Limits Schürzen's protection strictly to HEAT attacks against the specific marked arc, since standoff armor's real defensive mechanism (premature shaped-charge detonation) simply doesn't work against solid kinetic rounds or against arcs the historical skirt plates didn't actually cover.

   **Example:** A Tungsten round striking that same Schürzen-marked Side arc gets no PEN reduction at all — the marker's benefit applies exclusively to HEAT-family attacks, never to kinetic ones.

18.2c  Sidehill Exposure (Optional Rule)
--------------------------------------------

*If this module is in use for the scenario:*

*Design note: a vehicle sitting broadside across a sidehill, engaged by a shot arriving roughly perpendicular to the slope's fall line, doesn't present its plates the way the printed AVs assume — the whole hull has rolled with the ground. Its Side plate straightens toward vertical (losing whatever slope protection it had), and its deck's plane rotates enough that the same shot can graze across the normally near-invulnerable top edge instead. This module captures both without inventing a new roll or a new modifier number, reusing the crest-hexside geometry already established for elevation LOS (Rule 4.4a.1) and the target's own printed Top AV where one exists (Rule 17.2a). See design note E.120.*

**18.2c.1**  Broadside-to-Slope: before comparing PEN to AV (Rule 18.2), check whether the target is Broadside-to-Slope to this shot — all of the following must hold: (a) the Gunnery Roll (Rule 18.1a) selected a Side arc, on either profile; (b) that Side arc's hexside is also a crest hexside of the target's own hex (Rule 4.4a.1); (c) the attacker is on the low side of that hexside.

.. container:: rule-guide

   **Why:** Scopes the condition tightly to the exact geometry the phenomenon actually requires — a Side-arc hit, specifically across the one hexside where the ground itself changes level, from specifically the downhill direction — rather than a vague "on a slope" trigger that would apply far more often than the real effect does.

   **Example:** A tank sitting with its side facing a ridge crest, engaged by an enemy positioned below that same crest, is Broadside-to-Slope; that same tank engaged from its front, or from a direction with no crest hexside at all, is not.

**18.2c.2**  If 18.2c.1 holds and the struck profile has a printed Top AV (Rule 17.2a) matching the ammunition family fired, resolve the hit against whichever of that profile's Side AV or Top AV is lower, instead of Side AV alone. If the struck profile has no printed Top AV, resolve normally against Side AV — Broadside-to-Slope has no effect on an unmodelled plate.

.. container:: rule-guide

   **Why:** Lets the attacker exploit whichever of the two real, already-printed numbers is actually weaker, rather than inventing a separate reduction percentage — the whole point of the sidehill condition is that the defender's own printed Side and Top figures were never both meant to apply to the same shot at once, and the worse of the two is what the round genuinely finds.

   **Example:** A Tiger sitting Broadside-to-Slope is hit on its Hull Side arc: printed Hull Side AV-vs-Capped is 80mm, printed Hull Top AV-vs-Capped is 25mm — the shot resolves against 25mm, not 80mm, because the sidehill condition means the round is grazing the exposed deck edge, not striking the tough side plate square-on.

18.3  Contested Penetration Roll
--------------------------------


**18.3.1**  When effective PEN equals or exceeds AV but is less than AV + 3, roll 1d6:

.. container:: rule-guide

   **Why:** Gives the narrow band where PEN and AV are closely matched a genuine roll rather than a fixed outcome, since real close-margin shots historically produced mixed results — sometimes bouncing, sometimes partially or fully penetrating — reflecting real variance in impact angle and plate quality within nominally identical armor.

   **Example:** A shot whose effective PEN just barely reaches or slightly exceeds the target's AV rolls 1d6 rather than automatically succeeding — even a "sufficient" shot in this narrow band has genuine uncertainty.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
     - **Proceed to**
   * - 1–2
     - Bounce — round deflects
     - No further resolution
   * - 3–4
     - Partial penetration
     - Partial penetration damage table
   * - 5–6
     - Full penetration
     - Full penetration damage table


18.4  Non-Penetrating Hit
-------------------------


**18.4.1**  A round that strikes but cannot penetrate may still affect the crew through spalling, concussion, and psychological shock. Roll 1d6:

.. container:: rule-guide

   **Why:** Gives a non-penetrating hit a small but real chance of consequence rather than treating it as a complete non-event, since a heavy round striking armor without breaking through can still genuinely rattle the crew inside through concussion and spalling, even without the armor being defeated.

   **Example:** A round that fails to penetrate still rolls 1d6 for crew effect — most results mean nothing happened, but a high roll can still Suppress the vehicle's crew even though the armor held.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1–4
     - No effect — round bounces harmlessly
   * - 5–6
     - Crew shock — vehicle Suppressed


18.5  Partial Penetration Damage
--------------------------------


**18.5.1**  A partially penetrating round causes significant crew disturbance and possible damage. Roll 1d6:

.. container:: rule-guide

   **Why:** Gives a partial penetration a meaningfully worse range of outcomes than a mere non-penetrating hit (Rule 18.4), since a round that actually broke through some armor — even without fully entering the crew compartment — does real, sometimes serious damage, up to and including a genuine Casualty result.

   **Example:** A partially penetrating round's roll can range from crew shock all the way up to component damage (a vehicle Casualty) — a strictly more dangerous spread of outcomes than the mostly-harmless non-penetrating hit table.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1–2
     - Crew shock — vehicle Suppressed
   * - 3–4
     - Crew pinned — vehicle Pinned (buttoned up)
   * - 5–6
     - Component damage — vehicle Casualty (owning player chooses MOB or GUN kill)


18.6  Full Penetration Damage
-----------------------------


**18.6.1**  A fully penetrating round enters the crew compartment and causes serious damage. Roll 1d6 and apply modifiers:

.. container:: rule-guide

   **Why:** Gives Full Penetration the widest and most dangerous outcome range of any damage table, up to outright vehicle Elimination, since a round that fully enters the crew compartment has genuinely defeated the armor entirely — this is the point where the worst possible outcomes become live.

   **Example:** A full penetration's modified roll can land anywhere from crew shock (Suppressed) up through a Catastrophic kill — a much wider and worse range of possible outcomes than a partial penetration's table (Rule 18.5.1) allows.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Modified Roll**
     - **Result**
   * - 1
     - Crew shock — vehicle Suppressed
   * - 2–3
     - Crew pinned — vehicle Pinned (buttoned up)
   * - 4–5
     - Component damage — vehicle Casualty
   * - 6+
     - Catastrophic kill — vehicle Eliminated


**18.6.1a**  A natural 6 on the damage roll is always a Catastrophic kill, regardless of modifiers. A round inside the fighting compartment can find ammunition or fuel no matter how experienced the crew — negative modifiers shift the odds, they do not confer immunity.

.. container:: rule-guide

   **Why:** Guarantees every full penetration at least some minimum chance of a catastrophic outcome no matter how many negative modifiers stack against it, since a round genuinely inside the crew compartment can always get unlucky and find ammunition or fuel — no amount of crew skill makes elimination truly impossible.

   **Example:** A veteran-crewed vehicle with the -1 modifier still suffers a Catastrophic kill on a natural roll of 6, even though its modified total might otherwise never reach the elimination threshold — the natural-6 floor bypasses the modifier entirely.

*NOTE: without this rule, the veteran-crew modifier (-1) made Elimination arithmetically impossible for any gun under 88mm firing non-HEAT ammunition at a veteran-crewed vehicle (maximum modified roll 5) — a Sherman 76, T-34/85, or SU-85 could never destroy a German vehicle outright, while historically 75mm-class penetrations brewed up tanks routinely. The natural-6 floor gives every full penetration a minimum 1-in-6 chance of a kill.*

**18.6.2**  Full penetration modifiers applied to the damage roll:

.. container:: rule-guide

   **Why:** Shifts the full-penetration damage roll based on real factors that affect how catastrophic a penetration actually is — bigger warheads and larger calibres tend to do more damage once inside, veteran crews are better trained at damage control and escape, and an already-damaged vehicle has less redundancy left to absorb a second hit.

   **Example:** A very large calibre HEAT round (+1 for HEAT, +2 for 122mm+) striking an already-damaged vehicle (+1) stacks all three modifiers onto its roll, making a Catastrophic kill considerably more likely than the same penetration against a fresh, veteran-crewed vehicle (-1).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **Modifier**
   * - HEAT warhead (Panzerfaust, PIAT, Bazooka, HEAT round)
     - +1
   * - Large calibre round (88–120mm)
     - +1
   * - Very large calibre round (122mm+)
     - +2
   * - Crew quality veteran or elite
     - -1 (experienced crew better at surviving hits)
   * - Vehicle already damaged (on rear face)
     - +1


18.6a  Hit Location
--------------------


**18.6a.1**  Whenever Rule 18.5.1 or 18.6.1 produces a "Component damage — vehicle Casualty" result, roll 1d6+1d8+1d12 (the same combination used for every other attack, Rule 8.5.1) against the target vehicle's own Hit Location Table (Rule 17.7) for the profile that was hit (Hull or Turret, per the Gunnery Roll's own determination, Rule 18.1a — Hull for infantry AT weapons, Rule 18.9). One threshold pair per profile covers every range and attacker.

.. container:: rule-guide

   **Why:** Only triggers the hit-location roll for the specific "Component damage" outcome from the damage tables, since that's the one result genuinely ambiguous between MOB kill and GUN kill — other outcomes (Suppressed, Pinned, Eliminated) already fully determine themselves without needing a further location check.

   **Example:** A partial penetration rolling "Crew pinned" needs no hit-location roll at all — only if that same table instead rolled "Component damage" would this rule's hit-location procedure come into play to decide MOB versus GUN kill.

**18.6a.2**  If the roll is below the Neither Threshold, the hit landed somewhere non-critical — downgrade the result from Casualty to Pinned (Rule 18.7) instead. The round penetrated, but nothing essential was destroyed.

.. container:: rule-guide

   **Why:** Gives the hit-location roll a genuine third outcome — not every penetrating hit finds something worth destroying, so a low roll downgrades what would have been a Casualty result into a lesser Pinned status, reflecting a hit that did real damage but missed anything mission-critical.

   **Example:** A "Component damage" result that then rolls below the Neither Threshold on the hit-location check ends up as Pinned rather than the originally-indicated Casualty — the penetration happened, but nothing vital was hit.

**18.6a.3**  If the roll is at or above the Mobility Threshold, the hit is a MOB kill. If the roll is at or above the Neither Threshold but below the Mobility Threshold, the hit is a GUN kill.

.. container:: rule-guide

   **Why:** Splits the remaining roll range between the two possible Casualty outcomes using a single pair of thresholds, so the same roll that already determined "something critical was hit" (clearing the Neither Threshold) also determines exactly which critical system it was.

   **Example:** A roll that clears the Neither Threshold but falls short of the Mobility Threshold produces a GUN kill; a roll that clears the higher Mobility Threshold instead produces a MOB kill — one roll, two thresholds, three possible outcomes total including Rule 18.6a.2's Neither case.

**18.6a.4**  This rule applies only to Front-arc hits on vehicles whose Hit Location Table has actually been built (Tiger I Ausf E and Sherman M4A1 (75mm), this edition) — this edition's tables cover only that arc. Side- and Rear-arc hits on these vehicles, and all hits on any other vehicle, use Rule 17.1.1's owning-player judgement call instead.

.. container:: rule-guide

   **Why:** Restates the scope limit already established in Rule 17.7.1 here specifically where the hit-location roll procedure lives, since this is the moment a player needs to know whether to roll or simply choose — Front-arc hits on the two covered vehicles roll, everything else still falls back to judgment.

   **Example:** A Sherman M4A1 hit in its Front arc rolls against its printed Hit Location Table; that same Sherman hit in its Side or Rear arc, or any hit on a vehicle without a printed table at all, still uses the owning player's own judgment call instead.

*NOTE: This can only ever make an outcome different from what free choice would have picked — it has no effect on whether a Casualty occurs in the first place (Rule 18.5/18.6 are unchanged), only on which specific outcome follows one. A hit that resolves to "Neither" is a real, sourced consequence of this system, not an edge case being carved out: it reflects that not every penetrating hit finds something critical to destroy.*


18.7  Vehicle Damage States
---------------------------


**18.7.1**  Vehicle damage states mirror infantry status bands for system consistency:

.. container:: rule-guide

   **Why:** Maps vehicle damage onto the same conceptual ladder as infantry status (Suppressed, Pinned, Casualty, Broken) so a player already familiar with infantry rules can apply the same intuition to vehicles, even though the specific mechanical effects differ to fit a vehicle's own capabilities.

   **Example:** A vehicle's Suppressed state parallels an infantry unit's Suppressed status conceptually (a temporary combat-effectiveness hit), even though its specific mechanical penalties — reduced PEN, halved movement, a bail-out check — are vehicle-specific rather than the infantry rFP/movement penalties of Rule 10.2.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **State**
     - **Infantry equivalent**
     - **Effect on vehicle**
   * - Suppressed (crew shock)
     - Suppressed
     - Fires at -20 PEN (mm) and -2 rFP. Moves at half M#. Bail-out check each Recovery Phase.
   * - Pinned (buttoned up)
     - Pinned
     - MG only at -4. Cannot move. -2 OBS. Cannot spot hidden units. -1 morale checks. Bail-out check each Recovery Phase.
   * - Casualty — MOB KILL
     - Casualty (rear face)
     - M0. Can still fire all weapons. Flip counter to MOB KILL rear face.
   * - Casualty — GUN KILL
     - Casualty (rear face)
     - MG only. Can still move at full M#. Flip counter to GUN KILL rear face.
   * - Eliminated
     - Broken
     - Vehicle destroyed. Counter removed to BROKEN zone.


18.8  Anti-Infantry Fire
------------------------


**18.8.1**  Vehicles fire against infantry using their MG fire line or HE capability. Both use standard fire resolution (Section 8) against infantry Defence values.

.. container:: rule-guide

   **Why:** Keeps a vehicle's anti-infantry fire on the same ordinary fire-resolution system used everywhere else (Section 8) — the whole point of the Gunnery Roll and armor-penetration mechanics is for gun-vs-vehicle engagements, not for a tank shooting at infantry.

   **Example:** A tank firing its MG at an infantry squad rolls fire combat exactly as any other MG fire line would (Section 8), comparing against the squad's Defence and cover — no Gunnery Roll or penetration table is involved.

**18.8.2**  MG fire: uses MG rFP ⬡h -f notation, resolves against infantry defence + cover. The standard close-range bonuses apply: +3 rFP at range 0 (same hex, Rule 8.9.2), +2 rFP at range 1 (adjacent, Rule 8.9.1).

.. container:: rule-guide

   **Why:** Treats a vehicle's MG exactly like any other MG fire line, complete with the usual close-range bonuses, since the weapon and its resolution mechanics don't change just because it happens to be mounted on a vehicle rather than carried by infantry.

   **Example:** A vehicle's mounted MG firing at an adjacent infantry unit gets the same +2 rFP close-range bonus (Rule 8.9.1) that any infantry MG team would get firing at the same range.

**18.8.3**  HE fire: uses the flat HE rFP value. No falloff — HE effectiveness is constant regardless of range. Cover modifier applies but is reduced by 1 step (same as mortar indirect fire against buildings and reverse slopes).

.. container:: rule-guide

   **Why:** Gives HE fire the same flat, range-independent lethality as mortar blast (Rule 16.7.5) and applies the same reduced-cover treatment against certain protected positions (Rule 16.7.4), since a tank's HE shell striking a target behaves physically the same way a mortar round's blast does.

   **Example:** A tank's HE fire against a target in a building applies that building's cover reduced by one step, just as a mortar's blast effect would against the same target in the same position (Rule 16.7.4).

**18.8.4**  HE rFP derivation formula (resolved in spreadsheet): HE rFP = round(gun calibre in mm / 20). Examples: 37mm = 2, 75mm = 4, 88mm = 4, 105mm = 5, 122mm = 6.

.. container:: rule-guide

   **Why:** Derives a gun's HE effectiveness directly from its calibre with a simple formula, so every gun's printed HE rFP has a consistent, explicable basis rather than being independently chosen per weapon — a bigger shell reliably carries more explosive filler and thus more anti-infantry effect.

   **Example:** As printed: a 75mm gun's HE rFP is round(75/20) = round(3.75) = 4, and an 88mm gun's is round(88/20) = round(4.4) = 4 — two different calibres landing at the same HE rFP because the formula rounds them to the same result.

**18.8.5**  Fire against vehicles as soft targets: open-topped vehicles (the ○— symbol, Rule 17.1) and unarmoured (soft) vehicles can be attacked by HE, MG/small-arms fire (range 0–1 only), mortar blast (Rule 16.7.8), and grenades as if they were infantry, using a class Defence value — no per-vehicle stat is printed:

.. container:: rule-guide

   **Why:** Treats genuinely unprotected or lightly-protected vehicles like infantry for targeting purposes, since a soft-skinned truck or an open-topped half-track offers essentially the same vulnerability profile as troops in the open — one shared class Defence value avoids needing a bespoke stat printed on every such vehicle.

   **Example:** A soft-skinned truck caught by small-arms fire at range 1 is attacked exactly as an infantry unit would be, using the printed class Defence of 6 (Rule 18.8.5 table) rather than any vehicle-specific armor value — it has none to check.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Vehicle class**
     - **Defence vs soft-target fire**
   * - Truck / soft vehicle
     - 6
   * - Open-topped armoured vehicle (○—)
     - 8


A Casualty result or better eliminates a soft vehicle; against an open-topped armoured vehicle it is a vehicle Casualty (Rule 18.6a applies if a table exists, else Rule 17.1.1).

**18.8.6**  HE direct fire against a **closed** AFV never rolls on the penetration tables: resolve one roll on the Non-Penetrating Hit table (Rule 18.4), at +1 for guns of 105mm and larger — blast and concussion can suppress a crew but not open the tank. Damage to closed AFVs comes only through AP/HEAT penetration (Rule 18.2), overrun (18.11), Molotovs (18.10), and close-range infantry attacks (Rule 18.9a — includes engineer-specific weapons such as the magnetic mine, and the flamethrower's own vehicle rule, Rule 21.5.8).

.. container:: rule-guide

   **Why:** Blocks HE from ever penetrating a closed, armored vehicle's armor, since real high-explosive rounds don't reliably breach solid armor the way dedicated AP or HEAT rounds do — the best HE can do to a buttoned-up tank is rattle the crew, never actually damage the vehicle itself.

   **Example:** A large-calibre HE round fired directly at a closed AFV rolls once on the Non-Penetrating Hit table (with a +1 bonus if 105mm or larger) — no matter how big the shell, it cannot produce a Casualty or Elimination result against that closed vehicle through this rule alone.

18.9  Infantry Anti-Tank Weapons
--------------------------------


Infantry AT weapons do not use the Gunnery Roll (Rule 18.1a.8) — they always hit if fired within range and resolve directly against the target's Hull profile (front arc of engagement).

*[ TBD: Penetration values below are preliminary. Verify against primary sources before treating as final. ]*

**Decided: infantry AT weapons do not get a Gunnery Roll.** Three reasons, not just one: (1) these weapons are already deliberately designed around a range constraint, not an accuracy constraint (Appendix E.42) — Panzerfaust's flat, always-penetrating PEN value is a considered choice modelling "the operator must close to suicidally short range to guarantee a kill," and a hit/miss roll on top of that would blunt the exact tension the weapon is built around; (2) the vehicle Gunnery Roll's thresholds were calibrated against real data (Appendix 17's British O.B. Investigation No.659 study) — no comparable calibration data exists for infantry-fired AT weapons, so any hit-probability figure here would be invented, not sourced, unlike everything else this session has added; (3) these are already single, climactic, high-stakes actions (an exposed AT gunner takes one shot) — layering a second roll on top adds bookkeeping without a clear payoff for the moment it represents.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Weapon**
     - **PEN**
     - **Range**
     - **Notes**
   * - Rifle (all types)
     - 0
     - —
     - No AT capability
   * - LMG / HMG
     - 10 mm
     - 0–1 hex
     - Light vehicles only at point blank
   * - AT rifle (Boys, PzB 39)
     - 30 mm, −10 per 2 hexes beyond hex 1
     - 0–8 hex
     - Light armour only — ineffective vs medium tanks
   * - Panzerfaust 30
     - 140 mm (flat)
     - 0–2 hex
     - Hard range limit. Single shot — EXPENDED strip placed after use.
   * - Panzerfaust 60
     - 140 mm (flat)
     - 0–4 hex
     - Hard range limit. Single shot — EXPENDED strip placed after use.
   * - Panzerfaust 100
     - 140 mm (flat)
     - 0–6 hex
     - Hard range limit. Single shot — EXPENDED strip placed after use.
   * - Panzerschreck (RPzB 54)
     - 120 mm (flat)
     - 0–6 hex
     - Reloadable HEAT — flat PEN inside the hard range limit.
   * - PIAT
     - 100 mm (flat)
     - 0–6 hex
     - British. Reloadable HEAT — flat PEN inside the hard range limit.
   * - Bazooka M1A1
     - 90 mm (flat)
     - 0–8 hex
     - US. Reloadable HEAT — flat PEN inside the hard range limit.
   * - AT grenade bundle
     - 40 mm (flat)
     - 0 hex
     - Same hex only — Close Assault Against a Vehicle, Rule 18.9a.
   * - Magnetic mine (Hafthohlladung)
     - 60 mm (flat)
     - 0 hex
     - Engineer unit required. Same hex only — Rule 18.9a.
   * - Molotov cocktail
     - Special
     - 0–1 hex
     - Rear arc only. Engine fire on 4–6. See Rule 18.10.


*NOTE: PEN values in this table are 0°-equivalent millimetres, the same scale as every AV and gun PEN in the game (the pre-migration point values, 1 point ≈ 10mm, appeared here unconverted through v0.9.2 — under which every weapon on this list bounced off every vehicle in the roster). The HEAT weapons' accuracy degradation is modelled entirely by their hard range limits (Rule 17.3.3), not by a falloff on PEN — the old "-1 rFP per 2 hexes" notes were left over from a resolution path these weapons no longer use.*


**18.9.1**  EXPENDED strip: when a single-shot AT weapon is fired, place an EXPENDED strip over the weapon band on the infantry counter. The band is covered for the remainder of the scenario. The strip is a reusable component — same width as all support weapon bands.

.. container:: rule-guide

   **Why:** Marks a single-shot weapon as permanently used up with a simple physical cover on the counter, since a Panzerfaust genuinely cannot be reloaded once fired — the EXPENDED strip is a durable, reusable component doing the same job across every support weapon that has a one-time-use band.

   **Example:** A squad's Panzerfaust band gets covered with an EXPENDED strip the moment it's fired — for the rest of the scenario, that band is simply unavailable, with no further tracking needed than glancing at the counter.

**18.9.2**  Panzerfaust, Bazooka, and PIAT are HEAT weapons for the purposes of Rule 18.2b (Schürzen) — halve their effective PEN against a Side arc bearing a Schürzen marker, same as any other HEAT attack.

.. container:: rule-guide

   **Why:** Confirms explicitly that infantry-carried shaped-charge weapons trigger the same standoff-armor protection as gun-fired HEAT rounds, since their underlying physics (a shaped-charge jet) is identical regardless of whether the weapon is vehicle-mounted or shoulder-fired.

   **Example:** A Panzerfaust fired at a Schürzen-protected Side arc has its 140mm PEN halved to 70mm before comparison, exactly as a gun-fired HEAT round would in the same situation (Rule 18.2b.2).

18.9a  Close Assault Against a Vehicle
------------------------------------------

*Design note: Rule 18.9's own table has always listed the AT grenade bundle and magnetic mine at "0 hex — same hex only," implying an infantry unit can end up sharing a hex with an enemy vehicle to use them — but nothing ever said how it gets there or what happens once it does. Rule 18.8.6 has likewise always credited "engineer attacks (Section 21)" as one of the four ways a closed AFV takes damage, when the only vehicle-capable engineer action that actually exists is the flamethrower (Rule 21.5.8). This rule closes both gaps at once, reusing Close Assault's own declaration machinery and Overrun's already-established simultaneous-fire principle rather than building a parallel system. See design note E.113.*

**18.9a.1**  A unit may declare Close Assault (Rule 9.1) against a hex containing only enemy vehicles — the same declaration requirements apply (a leader present, Rule 9.1.2; not Suppressed/Pinned, Rule 9.1.3; the reduced-face nerve check, Rule 9.1.3a; Defensive Fire, Rule 9.1.5). A vehicle cannot throw grenades back or hold a firing line the way an infantry defender can, so the Grenade Phase and Entry Fire Phase (Rules 9.3-9.4) do not apply — this rule replaces both with a single exchange.

.. container:: rule-guide

   **Why:** Reuses Close Assault's existing declaration gate (leader coordination, Suppressed/Pinned exclusion, the reduced-face check, the defender's one chance at Defensive Fire) rather than inventing a second gate for the vehicle case, since the decision to close on an enemy position at grenade range is the same tactical moment whether that position holds infantry or a tank — only what happens once the attacker arrives differs.

   **Example:** Squad Alpha, with a leader present and a magnetic mine still unexpended, declares Close Assault against an adjacent hex containing a single enemy tank and no infantry. The declaration costs 1 AP exactly as any other Close Assault would; the defending player may still spend 1 RP on Defensive Fire before the exchange below resolves.

**18.9a.2**  The assaulting unit selects one weapon eligible at 0-hex range from Rule 18.9's table (an AT grenade bundle; a magnetic mine, engineer unit required; or any other carried weapon whose printed range band includes 0 hexes) and resolves it against the vehicle's Rear arc AV — closing to point-blank range means approaching from whatever angle exposes the weakest armor, the same principle already established for the flamethrower (Rule 21.5.8) and the Molotov cocktail (Rule 18.10.1). This resolves as an ordinary infantry AT attack (Rule 18.9): no Gunnery Roll, flat PEN vs AV.

.. container:: rule-guide

   **Why:** Sends the actual damage resolution through Section 18's existing PEN-vs-AV machinery rather than Section 9's infantry-vs-infantry dice-and-threshold system, since a satchel charge or mine breaching armor and a grenade duel suppressing riflemen are physically different events that already have their own correct resolution procedures — this rule's job is only to connect Close Assault's declaration to the right one.

   **Example:** Alpha's magnetic mine (60mm PEN, flat) resolves against the tank's Rear AV exactly as if fired at range 0 under Rule 18.9 — no Gunnery Roll, no hit-location ambiguity beyond what Rule 18.6a already provides for a Casualty result.

**18.9a.3**  Simultaneously, the target vehicle may fire its hull or coaxial MG (if any) at the assaulting unit at range 0, resolved as ordinary anti-infantry fire (Rule 18.8) — the same simultaneous-exchange principle already established for Overrun's pre-entry defensive fire (Rule 18.11.2). A vehicle under direct point-blank assault does not simply wait to be attacked.

.. container:: rule-guide

   **Why:** Reuses Overrun's own precedent for exactly this situation — infantry and a vehicle in point-blank contact — rather than treating the vehicle as a passive target for the one moment closest to a real melee this system has for it.

   **Example:** The same instant Alpha's mine resolves against the tank's rear, the tank's hull MG fires back at Alpha at range 0 under ordinary anti-infantry fire rules — neither side sees the other's result before its own is already committed.

**18.9a.4**  If the vehicle is eliminated or immobilised (a Casualty result or worse), the assault succeeds — apply Rule 9.3.6 (the attacker enters the hex; no further phase occurs). Otherwise the assaulting unit — if it survived the vehicle's return fire — withdraws to its original hex: an intact enemy vehicle still holds the ground, and there is no reason to remain exposed at point-blank range for another impulse.

.. container:: rule-guide

   **Why:** An infantry unit closing on a tank has one purpose — disable it — and no reason to occupy its hex if that fails, unlike infantry-vs-infantry close assault where holding the contested hex is itself the point; withdrawing automatically avoids inventing a reason for the attacker to just stand next to a still-functioning tank until the next impulse.

   **Example:** Alpha's mine bounces (a Bounce or Non-Penetrating Hit result) and Alpha itself survives the tank's return MG fire. Alpha withdraws to its original hex at the end of the exchange — the tank remains where it was, undamaged and still holding the contested hex.

    *See also: Rule 18.9 (the weapon table this rule resolves against), Rule 21.5.8 (the flamethrower's parallel rear-arc treatment), Rule 18.11.2 (Overrun's simultaneous-fire precedent).*

18.10  Molotov Cocktail
-----------------------


**18.10.1**  The Molotov cocktail can only target the engine deck — rear arc only, range 0-1 hex.

.. container:: rule-guide

   **Why:** Restricts the Molotov to the one place it could realistically be thrown to good effect — a tank's rear engine deck at very close range — since it's an improvised, thrown weapon with no ability to defeat frontal or side armor and no meaningful range beyond arm's reach.

   **Example:** An infantry unit adjacent to a vehicle's rear can throw a Molotov at its engine deck; that same unit standing adjacent to the vehicle's front or side has no legal Molotov target at all — the weapon simply doesn't work from those arcs.

**18.10.2**  On landing: roll 1d6. On 1-3: no effect (fire suppressed or misses engine). On 4-6: engine fire — vehicle Pinned immediately.

.. container:: rule-guide

   **Why:** Gives an improvised weapon like a Molotov real but unreliable odds — better than half the time it fails to actually catch the engine on fire, reflecting how genuinely hit-or-miss a thrown bottle of flaming liquid is against a moving armored target.

   **Example:** A Molotov thrown at a vehicle's engine deck starts an engine fire on a roll of 4, 5, or 6 — a coin-flip-ish chance, not a guaranteed effect, for what is fundamentally an improvised weapon.

**18.10.3**  Each subsequent Recovery Phase while engine fire is active: roll 1d6. On 1-3: crew extinguishes fire — remove Pinned status. On 4-5: fire continues — vehicle remains Pinned. On 6: fire spreads — roll on the Full Penetration Damage table (Rule 18.6.1) with a +1 modifier; its full range of outcomes (Suppressed through Eliminated) applies.

.. container:: rule-guide

   **Why:** Turns an ongoing engine fire into a recurring risk each Recovery Phase rather than a one-time effect, since a real vehicle fire genuinely can be extinguished, can smolder on, or can spread catastrophically — and a spreading fire reaching the Full Penetration Damage table means even an improvised Molotov carries some real chance of ultimately destroying the vehicle.

   **Example:** A vehicle Pinned by an engine fire rolls again each Recovery Phase: most results either clear the fire or leave it burning (still Pinned), but a roll of 6 escalates all the way to the Full Penetration Damage table — meaning even a Molotov's fire can, rarely, end in the vehicle's outright Elimination.

18.11  Overrun
--------------


Overrun's pre-entry defensive fire does not use the Gunnery Roll (Rule 18.1a.8) — resolved as described below instead. **Decided, and simpler than it first appeared**: this was never really an independent design fork. Pre-entry defensive fire is infantry firing AT weapons at the approaching vehicle (Rule 18.9's domain), which doesn't use the Gunnery Roll at all per that rule's own decision above — Overrun's exemption follows directly from it, not as a separate choice. The vehicle's simultaneous MG fire at the infantry was already outside the Gunnery Roll's scope too (Rule 18.1a.8 exempts anti-infantry fire generally, Rule 18.8). There is no point in Overrun's resolution where a vehicle fires at another vehicle, so there was never a real occasion for the Gunnery Roll to apply here in the first place.

**18.11.1**  A vehicle may declare an overrun when moving into a hex occupied by enemy infantry. The vehicle must have sufficient MP remaining to enter the hex.

.. container:: rule-guide

   **Why:** Frames Overrun as an aggressive movement declaration into an occupied hex rather than a ranged attack, since it models a vehicle physically driving into a position to crush or scatter defenders directly — the MP requirement ensures the vehicle can actually complete the entry, not just start it.

   **Example:** A vehicle with enough remaining MP to enter an enemy-occupied hex can declare an overrun into it; a vehicle with insufficient MP left cannot declare one against that hex this activation.

**18.11.2**  Pre-entry defensive fire: before the vehicle enters the hex, the defending infantry may spend 1 RP to fire AT weapons at the approaching vehicle. This is resolved at range 1 (adjacent). Vehicle fires MG simultaneously at infantry.

.. container:: rule-guide

   **Why:** Gives defending infantry one last chance to strike the vehicle before it actually arrives in their hex, with both sides firing simultaneously — the defenders' desperate AT shot and the vehicle's own suppressive MG fire both happen in the same moment, neither side getting to react to the other's outcome first.

   **Example:** As a vehicle closes in for an overrun, the defending infantry spends 1 RP to fire their AT weapon at it while the vehicle's MG fires back at the infantry — both resolve together, before the vehicle has actually entered the hex.

**18.11.3**  After pre-entry fire resolves, the defending infantry must pass a morale check at threshold 5 or immediately rout.

.. container:: rule-guide

   **Why:** Tests whether the defenders can psychologically withstand a vehicle bearing down on their position after the pre-entry exchange, since having an armored vehicle physically closing on your hex is a serious morale test independent of whatever the pre-entry fire actually accomplished.

   **Example:** Infantry that survives the pre-entry fire exchange unharmed still must pass this morale check — surviving the shooting doesn't automatically mean holding your ground against an oncoming tank.

**18.11.4**  If infantry routs: vehicle enters hex unopposed.

.. container:: rule-guide

   **Why:** Lets a successful overrun complete cleanly once the defenders break and flee, since routing infantry (Section 10.6) is no longer a combat-effective obstacle to the vehicle's entry — there's nothing left in the hex still capable of resisting.

   **Example:** Infantry that fails its Rule 18.11.3 morale check and routs immediately clears the way — the vehicle simply enters the now-vacated hex without further opposition.

**18.11.5**  If infantry holds: vehicle enters hex. Both sides are now in the same hex. Close combat continues each subsequent impulse — infantry fires AT weapons at range 0, vehicle fires MG at range 0. No cover modifiers apply. Range 0 bonus (+3 rFP) applies to the vehicle MG. Both sides resolve simultaneously.

.. container:: rule-guide

   **Why:** Turns a successful morale check into ongoing point-blank close combat rather than stopping the vehicle outside the hex, since holding infantry that doesn't rout is now sharing a hex with an enemy vehicle at the closest possible range — a genuinely desperate, simultaneous fight neither side can easily disengage from.

   **Example:** Infantry that holds against the overrun continues trading fire with the vehicle every subsequent impulse at range 0, with no cover protecting either side and the vehicle's MG getting its full close-range bonus — both sides keep resolving simultaneously until someone breaks or the vehicle withdraws.

**18.11.6**  Vehicle withdrawal from overrun hex: costs the vehicle's full remaining M# to exit. The vehicle is considered to have used its entire activation withdrawing.

.. container:: rule-guide

   **Why:** Makes disengaging from a close-combat overrun hex expensive — the vehicle's entire remaining movement, using up its whole activation — since extracting from point-blank range under fire genuinely isn't a quick or free maneuver.

   **Example:** A vehicle locked in overrun close combat that wants out must spend its full remaining M# just to exit the hex, consuming the rest of that activation entirely — it cannot withdraw and then also do something else that same turn.

18.12  Historical Matchup Verification
--------------------------------------


**Re-run against the current system, following the game's own reading procedure.** Each matchup reads PEN at the next lower printed range band exactly as Rule 17.3.1 directs players to (an earlier revision of this table computed PEN at exact ranges — a procedure the players never use — which produced three verdicts the table itself would contradict at the table), applies the ±10mm outcome margins of Rule 18.2, and checks against **both** the target's Hull and Turret AV-vs-Capped independently — the single blended "Front AV" this table originally validated no longer exists as a concept. Panzerfaust rows use the flat 140mm PEN now printed in Rule 18.9 (the direct millimetre conversion of the original system's flat "PEN 14", not a re-sourced value); infantry AT weapons resolve against Hull only, never Turret (no Gunnery Roll). This table checks penetration outcome only, the same scope the original table had — it does not check Gunnery Roll hit probability, which was separately calibrated against real data during that mechanism's own build (Rule 18.1a).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Matchup**
     - **Range**
     - **Arc**
     - **Hull result**
     - **Turret result**
     - **Historical verdict**
   * - Sherman 75mm vs Tiger I
     - 200 yds
     - Front
     - Bounce
     - Bounce
     - Cannot penetrate — correct ✓
   * - Sherman 75mm vs Tiger I
     - 40 yds
     - Front
     - Bounce
     - Bounce
     - Cannot penetrate at any range — correct ✓
   * - Sherman 75mm vs Tiger I
     - 320 yds
     - Side
     - Contested
     - Contested
     - Penetrates side armour — largely correct, see note (a)
   * - Tiger I 88mm vs Sherman M4A1
     - 600 yds
     - Front
     - Auto penetration
     - Auto penetration
     - Guaranteed kill at this range — correct ✓
   * - Panzer IV H vs T-34 Model 1943
     - 320 yds
     - Front
     - Auto penetration
     - Auto penetration
     - Uncertain results historically — see note (b)
   * - T-34 Model 1943 vs Panzer IV H
     - 400 yds
     - Front
     - Auto penetration
     - Non-penetrating hit
     - Cannot reliably penetrate the turret, hull now vulnerable — see note (c)
   * - T-34 Model 1943 vs Panzer IV H
     - 120 yds
     - Front
     - Auto penetration
     - Contested
     - Can penetrate at close range — correct ✓, more decisively than before
   * - T-34/85 vs Tiger I
     - 400 yds
     - Front
     - Auto penetration
     - Bounce
     - Marginal threat — correct ✓, and now shows *why*: see note (d)
   * - Panzerfaust 60 vs T-34 Model 1943
     - 80 yds
     - Front
     - Auto penetration
     - N/A — resolves vs Hull only (Rule 18.9)
     - Devastatingly effective — correct ✓
   * - Panzerfaust 60 vs Tiger I
     - 80 yds
     - Front
     - Auto penetration
     - N/A — resolves vs Hull only (Rule 18.9)
     - Penetrates all 1943 armour — correct ✓
   * - Sherman 76mm vs Tiger I
     - 400 yds
     - Front
     - Auto penetration
     - Bounce
     - Capable but not guaranteed — correct ✓, and now shows *why*: see note (d)


**Notes on genuine changes from the original (pre-rebuild) table:**

**(a) Sherman 75mm vs Tiger I side, 320 yds** — the original table called this "Auto penetration." Under the band-read procedure (320 yds ≈ 293m reads the 250m row: PEN 84.1mm) against AV 80.1mm (both Hull and Turret side share the figure), the shot clears AV by 4mm — inside the ±10mm Contested window of Rule 18.2. "Penetrates side armour" is still the correct story, just "very likely, roll needed" rather than "guaranteed."

**(b) Panzer IV H vs T-34 Model 1943, 320 yds** — the most substantive change. The original table called this "Contested," matching a "results were historically uncertain" narrative. The rebuilt KwK40 L48 gun curve — fitted to 5 independent historical data points at <1.2% error, the highest-confidence curve in the roster — puts PEN at 126.8mm against a 93.7mm Hull AV and 55.8mm Turret AV: a comfortable, unambiguous Automatic Penetration against both profiles, not a coin-flip. This is not obviously a regression: the long-barrelled 75mm L48 (KwK40) on the Panzer IV H was specifically prized by German crews for being able to reliably defeat T-34 frontal armour at real combat ranges, unlike the earlier short-barrelled 75mm it replaced — arguably the rebuilt system's more decisive result is the more historically accurate one, and the original "uncertain" calibration may have undersold the L48's real capability. Flagged for Rod's own judgement rather than silently resolved either way.

**(c) T-34 Model 1943 vs Panzer IV H, 400 yds** — the original table called this "Non-penetrating" outright. The rebuilt system splits it: Hull is now Automatic Penetration (PEN 74.9mm vs. Hull AV 64.9mm), Turret remains a clean Bounce (vs. 78.9mm). The Hull figure dropped from the original system's blended AV specifically because of this session's face-hardened-armour work (Rule 17.2, §17 of the design spec) — Panzer IV H's hull front and side were historically face-hardened, and face-hardening is a *liability* against capped rounds once the attacking cap protects the round's nose from the shattering mechanism face-hardening relies on. **Resolved**: the Soviet 76mm F-34's BR-350A round was flagged as a possible `ap_uncapped` candidate (Russian ammunition is often generally described as lacking AP caps) — checked directly against Woodman's "Tank Armament in World War Two" table (the same source already calibrating this gun's own curve), which explicitly labels this exact round "Sov 76mm APC" (Armor-Piercing **Capped**). The general "Russian ammunition lacked caps" claim appears to describe older ammunition (the plain BR-350, fired from 1930s-era 76.2mm guns) rather than the improved "A"-suffix BR-350A the wartime F-34 actually fired. `ammo_family=capped` stands as correctly sourced, not merely assumed — this matchup's numbers are unchanged.

**(d) T-34/85 vs Tiger I (400 yds) and Sherman 76mm vs Tiger I (400 yds)** — both originally called "Contested"/"marginal"/"not guaranteed." The rebuilt system reveals *why* that framing was historically right, in a way the old blended AV couldn't show: the Hull is a clean Automatic Penetration in both cases, while the Turret (Tiger's real, edge-effect-derived 143mm mantlet figure, Rule 17.2's Ch.10 data) is a clean Bounce. "Not guaranteed" was never about any single shot being marginal against its own target — it was always about *which profile* the shot would land on, which is exactly what the Gunnery Roll (Rule 18.1a) now resolves explicitly instead of burying it inside one averaged number.

**Extended coverage: the five vehicles the original table never tested.** The original 11 matchups only ever exercised Tiger I, Panzer IV H, T-34 (both marks), and both Shermans. Panther, KV-1S, SU-85, T-70, and StuG III had never been checked against a historical matchup at all. Extending the same methodology:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Matchup**
     - **Range**
     - **Arc**
     - **Hull result**
     - **Turret result**
     - **Historical verdict**
   * - Sherman 75mm vs Panther
     - 200 yds
     - Front
     - Bounce
     - Bounce
     - Correct ✓ — Panther's frontal invulnerability to the standard Sherman 75mm is one of the best-documented facts of the 1944 tank war
   * - Sherman 76mm vs Panther
     - 200 yds
     - Front
     - Bounce
     - Bounce
     - Correct ✓ — the upgunned Sherman's M62 APC (123.5mm) closes the gap considerably but still falls well short of Panther's ~230-250mm glacis/mantlet, consistent with accounts that 76mm Shermans still generally could not beat Panther frontally
   * - Panther vs Sherman M4A1
     - 800 yds
     - Front
     - Auto penetration
     - Auto penetration
     - Correct ✓ — and notably still an automatic kill at long range (800yds), matching the KwK42 L70's reputation for out-ranging Allied tank guns entirely
   * - Panzer IV H vs T-70
     - 500 yds
     - Front
     - Auto penetration
     - Auto penetration
     - Correct ✓ — unsurprising given T-70's thin armour, included mainly to confirm the light-tank case behaves as expected at both profiles
   * - T-70 vs Panzer IV H
     - 200 yds
     - Front
     - Contested
     - Bounce
     - Plausible ✓ — see note (e); T-70's 45mm APBC has only a contested chance against the glacis at point-blank and cannot beat the turret at its own small calibre
   * - KV-1S vs Panzer IV H
     - 300 yds
     - Front
     - Auto penetration
     - Non-penetrating hit
     - Plausible ✓ — see note (f)
   * - Panzer IV H vs KV-1S
     - 500 yds
     - Front
     - Auto penetration
     - Non-penetrating hit
     - Plausible ✓ — see note (f); KV-1S's hull was thinned relative to the original KV-1 for speed, but its turret protection was largely retained (band-read PEN 128.4 vs turret AV 129.1 — a rattling near-miss, not a clean deflection)
   * - SU-85 vs Tiger I
     - 400 yds
     - Front
     - Auto penetration
     - N/A — casemate, no turret
     - Correct ✓ — SU-85 was specifically fielded to give Soviet forces a weapon that could threaten German heavies at moderate range
   * - SU-85 vs Panther
     - 300 yds
     - Front
     - Bounce
     - N/A — casemate, no turret
     - Correct ✓ — SU-85's 85mm could not reliably beat Panther's glacis frontally at any practical range, a documented limitation that led to the later SU-100
   * - StuG III vs T-34 Model 1943
     - 500 yds
     - Front
     - Auto penetration
     - N/A — casemate, no turret
     - Correct ✓ — StuG III's long 75mm made it one of the most effective German tank-killers of the war, consistent with a decisive result at moderate range
   * - T-70 (weakest gun in roster) vs Sdkfz 251
     - 1000 yds
     - Front
     - Auto penetration
     - N/A — open-top, no turret
     - Correct ✓ — the weakest gun in the roster, at unusually long range, still trivially defeats the half-track's 14.3mm armour. Included only to confirm the last untested roster vehicle behaves as expected; no real ambiguity to resolve here


**(e) T-70 vs Panzer IV H — a real methodology bug caught and fixed during this extension, not a subtle judgement call.** The first pass of this matchup compared T-70's 45mm APBC gun against Panzer IV's `av_vs_capped_mm` roster column — which would have been wrong. That column bakes in the face-hardening correction for a **Capped**-family attacker (Rule 17.2.3) specifically; T-70's 45mm fires Soviet APBC ammunition, an entirely different nose shape, for which face-hardening does not apply the same way (`face_hardened_multiplier("apbc") = 1.0`, a documented gap — no correction rather than a wrong one). Recomputing Panzer IV's front plates for a 45mm APBC attacker (bypassing the mismatched column, and at the attacker's own calibre rather than the roster's 75mm reference diameter) gives Hull 83.9mm and Turret 106.6mm — against a band-read PEN of 86.3mm (200 yds reads the 0m row), a Contested Hull shot and a clean Turret Bounce under the ±10mm margins. **Fixed since this table was first written.** `VehiclePlateRow.resolve_av()` in `counters/armor_calc/pipeline.py` was hardcoded to the Capped family — it now takes an explicit `family` parameter (defaulting to "capped", so `write_roster_csv`'s printed columns are unaffected). A future matchup or validation script needing the correct AV for an APBC or uncapped-AP attacker should call `resolve_av(diameter, hardness_table, family="apbc")` directly rather than reading `av_vs_capped_mm` off the roster CSV. The printed counter still shows only two AV columns (vs. Capped, vs. Tungsten) — APBC and uncapped AP remain rare enough as attacker families that a third and fourth printed column isn't warranted, consistent with the "least granular means necessary" design principle (§2) — but the underlying tool can no longer silently give a wrong answer when one is actually needed for a specific check. Regression tests cover the family parameter in `tests/test_pipeline.py`.

**(f) KV-1S matchups borrow gun curves, not vehicle-specific ones.** KV-1S historically mounted the 76.2mm ZIS-5 gun, not the F-34 this table uses — but ZIS-5 is a direct evolution of F-34 with closely comparable ballistic performance, and no separate ZIS-5 curve has been fitted in this roster. Similarly, SU-85's 85mm D-5S gun is modelled using the T-34/85's D-5T curve — the same gun family, tank- vs. self-propelled-mounted. StuG III's matchup uses Panzer IV's KwK40 curve directly, which is not an approximation — StuG III Ausf G by this point mounted the identical 7.5cm StuK 40 L/48. These substitutions are reasonable but unverified against separately-sourced data for the specific gun models named — flagged rather than presented as equally certain to the guns with their own fitted curves.

**Third extension: the Sherman Firefly's arrival.** Firefly was added to the roster this session (`counters/toe/sherman_firefly_1944.md`) specifically to mount the 17-pounder in a Sherman hull — its historical claim to fame is beating German heavies the standard 75mm/76mm Sherman never could. One real, well-cross-referenced engagement exists to check that claim against:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Matchup**
     - **Range**
     - **Arc**
     - **Hull result**
     - **Turret result**
     - **Historical verdict**
   * - Sherman Firefly (17pdr APCBC) vs Tiger I
     - 700 m
     - Front
     - Auto penetration
     - Contested
     - Plausible ✓ — see note (g)

**(g) Sherman Firefly vs Tiger I — the Wittmann engagement, 8 August 1944.** Trooper Joe Ekins's Firefly (A Squadron, 1st Northamptonshire Yeomanry) is credited with destroying all three Tigers of the 101st SS Heavy Panzer Battalion's 3rd/HQ Company his troop could see during the Saint-Aignan-de-Cramesnil action, including Michael Wittmann's — one of the best-corroborated small-unit tank actions of the war, converging across four independent secondary sources. The engagement range itself wobbles by roughly 100m across tellings (~700m per a cited fire order, ~730m per another account) — 700m is used here since both readings fall in the same printed band. At the 500m band (700m reads the next lower printed band per Rule 17.3.1) the 17pdr APCBC line reads PEN 150.6mm — a clean Automatic Penetration against Tiger I's 102.0mm Hull Front (48.6mm over, far outside the ±10mm margin of Rule 18.2), but only a Contested result against the 143.0mm Turret Front (7.6mm over, inside the margin) — Tiger's mantlet/turret-front-bar combination (Rule 17.2's Ch.10 edge-effect table) remains the hard target it is against every other gun in this roster. This is consistent with, not a stretch from, the real outcome: three kills in one action is a decisive result, and this table's Hull/Turret split shows *why* it was decisive — Ekins didn't need a mantlet shot to win, the hull alone was a guaranteed kill at this range, exactly the capability gap the 17pdr was built to close. No claim is made about which plate the real rounds actually struck; the vignette's own sourcing doesn't specify hit location, only outcome.
