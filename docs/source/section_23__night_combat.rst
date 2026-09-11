Section 23 — Night Combat
=========================

Night scenarios collapse visual detection and put a premium on sound, silhouette, and the rare, precious light a side can bring with it. This section finishes the framework Rule 14.11.5 established and left as future work, and adds illumination as a real, biddable resource rather than a fixed scenario condition. It is deliberately built from pieces this system already has — the fire-mission pipeline (Section 16), the CON/OBS spot procedure (Section 14.9), the careless-movement penalty (Section 7.4), and the dispersion-direction table (Rule 16.6.5) — rather than introducing a parallel set of night-only mechanics. Section 20's own note on reuse-by-reference is the model followed here: each affected section carries one short cross-reference rule pointing back to this section for the actual values, rather than a duplicated procedure.

Rule 14.11.5 is superseded by Rule 23.1. See design note E.106.

23.1  Ambient Visibility
------------------------


**23.1.1**  In a night scenario, no visual spot roll (Rule 14.9.5) may be attempted against a marker more than 2 hexes away, regardless of OBS bonuses. This is a hard eligibility gate in front of the spot-roll procedure, not a CON modifier — a marker beyond 2 hexes is never rolled against at all, no matter how the roll would otherwise come out.

.. container:: rule-guide

   **Why:** Firms up 14.11.5's original "1-2 hexes" range into one fixed number, matching the example Section 22's own scenario-design guidelines already give ("Night: visibility 2 hexes") — and makes it a flat gate rather than a CON penalty so a spotter can't buy back distance with a large enough OBS bonus, which would defeat the point of night visibility being genuinely short.

   **Example:** An enemy marker 3 hexes away cannot be spotted visually this turn no matter how many OBS bonuses the spotter stacks — a Spot Action's +3 (Rule 14.10.2) has no effect on a roll that is never attempted in the first place. The same marker at 2 hexes is a normal spot attempt, subject to every usual modifier.

    *See also: Rule 14.9.5 (spot roll triggers), Rule 14.9.6 (spot roll procedure) — both apply exactly as written once a target is within this cap.*

**23.1.2**  Sound spotting's trigger condition (Rule 14.11.1 — no unit has fired within 5 hexes this turn) is unchanged at night. A firefight masks footsteps the same way after dark as it does in daylight.

.. container:: rule-guide

   **Why:** Keeps sound spotting's on/off switch exactly as it already works — night changes how much sound spotting matters (Rule 23.1.3), not when it becomes available in the first place.

   **Example:** A unit firing within 5 hexes turns off sound spotting for the turn at night exactly as it would at midday — the doubled penalties of Rule 23.1.3 never come into play on a turn where sound spotting itself isn't available.

**23.1.3**  Exactly two rows of the CON table (Rule 14.9.7) double at night: moving through dense woods or rubble (-1 becomes -2) and moving carelessly (-2 becomes -4). Every other row — terrain cover, the table's own "Night scenario: +3" row, smoke's +2 — is unaffected.

.. container:: rule-guide

   **Why:** Names the two rows Rule 14.11.5 gestured at without specifying ("sound-based CON penalties") — these are the only two rows in the existing table that are genuinely about noise a unit makes by moving, which is exactly what carries further and matters more once vision has collapsed. Doubling the flat "Night scenario: +3" row itself, or terrain cover, would conflate concealment sources this rule isn't meant to touch.

   **Example:** A unit moving carelessly at night suffers -4 CON (the doubled row) on top of the flat +3 Night scenario CON bonus it would otherwise carry — carelessness is far more dangerous after dark than the same move in daylight, while a unit that hasn't moved or fired keeps its ordinary night concealment untouched.

**23.1.4**  Everything else in the spot-roll procedure — the 4+ threshold (Rule 14.9.6), the full OBS table (Rule 14.9.8), and every RP cost (Rule 14.9.5) — is unchanged at night.

.. container:: rule-guide

   **Why:** Scopes night's effect narrowly to the visibility cap and the two named CON rows, rather than rewriting the spot-roll procedure itself — a night scenario is the same procedure with a shorter leash and louder mistakes, not a different game.

   **Example:** A dedicated Spot Action still costs 1 AP and still grants +3 OBS at night exactly as it does in daylight (Rule 14.10) — nothing about the action itself changes, only whether the target it's used against is close enough, or lit enough, to be a legal target at all.

23.2  Illumination — General
-----------------------------


**23.2.1**  A hex within an active light radius (Rules 23.3-23.5) is treated as daylight for detection purposes: the 2-hex visibility cap (Rule 23.1.1), the "Night scenario: +3" CON row (Rule 14.9.7), and the doubled Rule 23.1.3 sound penalties all stop applying to a spot roll made against a marker in that hex. Normal terrain CON and LOS still apply as usual.

.. container:: rule-guide

   **Why:** Illumination cancels *night* specifically, not concealment in general — a lit hex is exactly as spottable as it would be at midday, no better and no worse, so a unit standing in dense woods under a starshell is still hard to see for the same reason it would be hard to see at noon, just no longer additionally protected by darkness.

   **Example:** A unit in open ground caught inside a starshell's light radius is spotted using the ordinary daylight CON table — no night penalty to the spotter, no 2-hex cap — while a unit in dense woods in that same lit hex still gets its full +3 terrain CON, since illumination never touched that row.

    *See also: Rule 23.1 (the night penalties this rule suspends), Rule 14.9.7 (the CON table these hexes are read from once lit).*

23.3  Illumination Source — Off-Map Starshell
-----------------------------------------------


**23.3.1**  A mortar or off-map artillery fire mission may nominate **Illum** as its round type, alongside HE (Rule 16.7) and Smoke (Rule 16.9), expending 1 AMO from the same pool HE and smoke missions already share (Rule 16.3.2).

.. container:: rule-guide

   **Why:** Reuses the existing ammunition pool rather than opening a separate illumination-round count — a battery that has spent rounds on HE and smoke has that much less illumination left too, the same shared-scarcity logic Rule 16.3.2 already applies between HE and smoke.

   **Example:** A mortar with AMO 8 that has already fired 5 HE and 1 smoke mission has 2 AMO left for anything — including an Illum mission — regardless of how that 2 is eventually spent.

    *See also: Rule 16.3.2 (the shared AMO pool this rule draws from).*

**23.3.2**  An Illum mission uses the identical sealed-slip targeting, delay, accuracy roll, and dispersion procedure as any other mission (Rules 16.4-16.6). Nothing about the mission is trackable before it lands.

.. container:: rule-guide

   **Why:** An illumination round is delivered by the same tube on the same trajectory as an HE or smoke round — there is no reason for its fire-control math to differ, and reusing the pipeline wholesale means a player learns nothing new to call for light.

   **Example:** An Illum mission called via Map Fire suffers the same -2 accuracy penalty and 3-impulse delay an HE Map Fire mission would (Rule 16.4.1) — the round type doesn't change how hard it is to call in.

**23.3.3**  On landing, place an **ILLUM marker** at **step 3** in the landing hex instead of a SMOKE marker. The marker's light radius in hexes equals its current step — no separate radius table is needed.

.. container:: rule-guide

   **Why:** Reuses smoke's own step-track idea (Rule 16.10) rather than inventing a new radius mechanic, and collapses radius and step into the same number so there's exactly one thing to track per marker instead of two.

   **Example:** A freshly-landed ILLUM marker at step 3 lights every hex within 3 hexes of the landing hex; once it fades to step 1 (Rule 23.3.4), only the immediate 1-hex radius remains lit.

**23.3.4**  During each Recovery Phase, roll 1d6 for each ILLUM marker placed by a starshell mission: **1-3 advances it one step** (3→2→1→removed). **4-6 holds** at the current step.

.. container:: rule-guide

   **Why:** A starshell burns out faster than a smoke round lingers — the 1-3/6 fade rate is a real number worth keeping distinct from smoke's own 1-2/6 dissipation roll (Rule 16.10.1) rather than copying it unexamined, since the physical thing (a burning flare on a parachute) genuinely behaves differently from a chemical smoke cloud.

   **Example:** An ILLUM marker at step 3 has a 50% chance of dropping to step 2 on the very next Recovery Phase — noticeably more fragile than a THICK smoke marker's 33% chance of thinning under Rule 16.10.1's roll.

**23.3.5**  A starshell's ILLUM marker drifts per Rule 23.6.

23.4  Illumination Source — Handheld Flare Pistol
----------------------------------------------------


**23.4.1**  A unit or leader equipped with a flare pistol may fire it as its own action: no sealed slip, no delay, no accuracy or dispersion roll. It targets the firing unit's own hex or an adjacent hex, the owning player's choice.

.. container:: rule-guide

   **Why:** A flare pistol is a personal signal weapon fired and seen the instant it's used, not a called-in support asset with its own fire-control chain — the complete absence of slip, delay, and roll is what actually distinguishes it from a starshell mission, not just a smaller radius.

   **Example:** A squad with a flare pistol fires it as its action this impulse; the light appears immediately, in the squad's own hex or an adjacent one of the player's choosing, with no waiting and no chance of the shot going astray.

**23.4.2**  Each equipped leader or unit may fire its flare pistol **twice per scenario**.

.. container:: rule-guide

   **Why:** Caps this to a genuinely scarce, personal resource — unit equipment issued for the scenario, not a repeatable support request — so a flare pistol is a decision saved for the moment it matters most, twice, rather than a tool used freely.

   **Example:** A leader who has already fired their flare pistol twice this scenario cannot fire it a third time even with a fresh, uncommitted action available — the limit is on the equipment, not the AP.

**23.4.3**  The resulting ILLUM marker starts at **step 2** — a smaller radius than a starshell's step 3.

.. container:: rule-guide

   **Why:** A handheld flare is a smaller, closer-range signal than an artillery-delivered starshell, and the printed starting step says so directly without needing a separate radius stat.

   **Example:** A flare pistol's ILLUM marker lights a 2-hex radius the moment it's fired — noticeably tighter than the 3-hex radius a fresh starshell provides.

**23.4.4**  The marker steps down by exactly 1 automatically every Recovery Phase — no roll.

.. container:: rule-guide

   **Why:** Deliberately the opposite trade-off from a starshell: bigger, delayed, and uncertain in duration versus smaller, instant, and perfectly predictable. Two clean uses per scenario, two turns of light each, with no ambiguity about how long either one lasts.

   **Example:** A flare fired at step 2 is reliably at step 1 next Recovery Phase and gone the Recovery Phase after that — a player can plan an action around exactly two turns of light, no dice involved.

**23.4.5**  A handheld flare's ILLUM marker drifts per Rule 23.6.

23.5  Illumination Source — Vehicle Searchlight
---------------------------------------------------


**23.5.1**  A vehicle equipped with a searchlight illuminates a 2-hex radius within whatever arc its TRAV rating currently covers (Rule 17.4.1) — the same arc the vehicle's gun covers, not a separate facing or cone.

.. container:: rule-guide

   **Why:** Reuses the vehicle's existing TRAV arc rather than introducing new facing geometry that exists nowhere else in the rules — a hull- or turret-mounted searchlight sweeps exactly where the gun already can, which is both the simplest rule and the historically sensible one.

   **Example:** A vehicle with TRAV 3 (front hexside and its two neighbours, Rule 17.5's arc table) illuminates radius 2 across that same three-hexside arc — nothing beyond what the gun could already engage this turn.

**23.5.2**  A searchlight has no delay, no fade, and no drift — it is lit for as long as the vehicle keeps it on, and dark the instant the player turns it off.

.. container:: rule-guide

   **Why:** A vehicle searchlight is a switch, not a burning or drifting object — there is nothing to track between turns beyond whether the player currently wants it on.

   **Example:** A player may switch a searchlight on for one impulse to illuminate an advancing enemy and off again the next, with no marker to place, remove, or roll for either way.

**23.5.3**  Using the searchlight automatically reveals the vehicle for that turn, mirroring Rule 14.9.3's "a unit that fires is automatically revealed."

.. container:: rule-guide

   **Why:** A searchlight beam is at least as conspicuous as a muzzle flash — there is no plausible case for a vehicle lighting up the battlefield around it while remaining concealed itself.

   **Example:** A hidden vehicle that switches on its searchlight is revealed at its position immediately, exactly as if it had fired its main gun — the light and the reveal happen together, with no spot roll needed either way.

23.6  Drift
-----------


**23.6.1**  Once per scenario, roll 1d6 on the existing dispersion-direction table (Rule 16.6.5 — 1=North, 2=Northeast, 3=Southeast, 4=South, 5=Southwest, 6=Northwest) to set a single wind direction for the whole scenario.

.. container:: rule-guide

   **Why:** Reuses the exact six-direction table already defined for mortar dispersion rather than inventing a new one, and fixes wind direction once for the scenario rather than re-rolling it, since wind direction doesn't meaningfully change turn to turn at this timescale (Rule 2.2.1) the way an individual round's landing point does.

   **Example:** A scenario's wind roll comes up 3 (Southeast) at setup — every ILLUM marker that drifts this scenario drifts Southeast, using the same compass rose every map already carries for dispersion.

**23.6.2**  Every ILLUM marker still aloft — from a starshell or a handheld flare — drifts 1 hex in the wind direction each Recovery Phase, at the same time as its fade check (Rule 23.3.4's roll or Rule 23.4.4's automatic step-down).

.. container:: rule-guide

   **Why:** Ties drift to the same Recovery Phase moment as fading, so a player checks both facts about a marker in one place rather than tracking two separate timing points for the same token.

   **Example:** An ILLUM marker drifting Southeast moves one hex in that direction and, in the same Recovery Phase, rolls (if a starshell) or automatically steps down (if a flare) — both updates happen together before the next turn begins.

**23.6.3**  A vehicle searchlight (Rule 23.5) does not drift — it is a beam tied to the vehicle, not an airborne object.

.. container:: rule-guide

   **Why:** Drift only makes physical sense for something actually floating on a parachute in the wind — a searchlight beam has no independent position to blow off course, so this rule closes off the one case where drift's logic obviously doesn't apply.

   **Example:** A vehicle's searchlight arc stays exactly where its TRAV rating points it regardless of the scenario's wind direction — only starshell and flare ILLUM markers are ever subject to Rule 23.6.1's roll.
