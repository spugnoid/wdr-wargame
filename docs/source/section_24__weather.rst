Section 24 — Weather
====================

Section 22's own scenario-design checklist has always told designers to note "Night, weather, restricted terrain, off-map assets" as special conditions — but until this section, weather was never actually a rule a designer could invoke. This section closes that gap the same way Section 23 finished Night Combat: by declaring exactly what a scenario's weather does, once, at setup, and reusing existing machinery (the visibility-cap idiom of Rule 23.1.1, the terrain movement-cost table's own additive idiom, and the bog check of Rule 17.6.2a) rather than building a parallel system.

A scenario declares exactly one Weather condition in its scenario parameters, fixed for the whole scenario: **Clear** (the default — no effect, nothing in this section applies), **Rain/Mud**, **Snow**, or **Fog**. See design note E.108.

24.1  Weather — General
------------------------


**24.1.1**  A scenario's Weather condition, once declared, applies for the scenario's entire duration. It does not change turn to turn.

.. container:: rule-guide

   **Why:** Matches how Night is already handled (Rule 2.2, scenario parameters) rather than adding a weather track that shifts mid-game — a rolling, changing weather system is real future-work territory, but a fixed condition set at setup is the version that was actually asked for, and it keeps Weather exactly as easy to author as Night already is.

   **Example:** A scenario designer declares Rain/Mud in the scenario parameters. Every turn of that scenario is played under Rain/Mud's effects (Rule 24.2) — there is no roll or event that changes it to Clear or to a different condition partway through.

**24.1.2**  A scenario may declare a Weather condition together with a night setting (Rule 23.1). Where both impose a visibility cap, use whichever cap is more restrictive (the fewest hexes). Illumination (Rule 23.2) cancels Night's own contribution as normal, but never cancels a Weather condition's cap — a starshell does not burn through fog or driving rain the way it cuts through plain darkness.

.. container:: rule-guide

   **Why:** Night and Weather are independent conditions that can plausibly co-occur (a foggy dawn attack, a night action in the rain), so this rule states the one thing that actually needs deciding when they do — which cap wins — rather than leaving it ambiguous. The illumination carve-out prevents an absurd result: light doesn't restore visibility that a physical medium like fog or rain is blocking, only visibility that darkness itself was withholding.

   **Example:** A night scenario with Fog declared has a 2-hex Night cap (Rule 23.1.1) and a 1-hex Fog cap (Rule 24.4.1) both active; the more restrictive 1-hex Fog cap governs. A starshell overhead lights the hex for Night purposes, but the Fog cap still applies there — the fog doesn't clear just because a flare is burning above it.

    *See also: Rule 23.1 (Night's own visibility cap), Rule 23.2 (Illumination).*

24.2  Rain and Mud
-------------------


**24.2.1**  Visual spot range is capped at **3 hexes** under Rain/Mud, under the same terms as Rule 23.1.1 — a hard eligibility gate in front of the spot-roll procedure, not a CON modifier, and it also gates fire declaration (Rule 8.11) exactly as Night's cap does.

.. container:: rule-guide

   **Why:** Reuses Night's own visibility-cap mechanism wholesale rather than inventing a second way to express the same idea — only the number differs, because sustained rain obscures less completely than full darkness or thick fog, while still meaningfully shortening the battlefield.

   **Example:** A unit may not declare fire at, or attempt a visual spot roll against, a target 4 hexes away in Rain/Mud, regardless of OBS bonuses — the same flat gate Night's Rule 23.1.1 already establishes, at a longer 3-hex range.

    *See also: Rule 8.11 (fire eligibility, which this cap also gates).*

**24.2.2**  A tracked vehicle entering any hex under Rain/Mud is subject to the bog check of Rule 17.6.2a, exactly as if every hex were dense woods for that purpose. This is in addition to, not instead of, the existing dense-woods bog check (a tracked vehicle entering an actual dense-woods hex in Rain/Mud still only rolls once).

.. container:: rule-guide

   **Why:** Reuses the exact mechanic Rule 17.6.2a already built rather than a new one — the historical rasputitsa (mud season) problem was precisely that ground vehicles could bog down anywhere, not only in terrain already classified as difficult, so the existing bog check's trigger condition widens to "any hex" without changing the check itself in any way.

   **Example:** A tank crossing open ground under Rain/Mud rolls the same 1d6 bog check (1-2 bogs, Rule 17.6.2a) it would only otherwise face entering dense woods — getting a BOGGED marker, M0, still able to fight, freed the same way any bogged vehicle is freed.

**24.2.3**  Infantry pay **+1 MP** to enter any hex under Rain/Mud, on top of the hex's normal terrain cost (Rule 7.2).

.. container:: rule-guide

   **Why:** Foot movement through mud is markedly slower without the same risk of getting flatly stuck a heavy vehicle faces — a flat cost surcharge (the same additive idiom Rule 4.1.3 already uses for hedgerow crossings) captures that without adding a chance-based mechanic infantry don't need.

   **Example:** A squad with M2 crossing open ground (normally 1 MP/hex) under Rain/Mud pays 2 MP per hex instead, reaching only 1 hex this activation instead of the usual 2.

24.3  Snow
----------


**24.3.1**  Visual spot range is capped at **3 hexes** under Snow — the same Precipitation Visibility figure as Rain/Mud (Rule 24.2.1), under the identical terms.

.. container:: rule-guide

   **Why:** Falling or blowing snow obscures the battlefield in roughly the same way sustained rain does, and the distinction that actually matters for play is what the ground itself does underfoot (Rule 24.3.2), not a separately-tuned visibility number for a second precipitation type — a deliberate simplification, the same call E.82 made when one Hit Location row turned out to cover what a much larger table used to.

   **Example:** A unit may not declare fire or attempt a visual spot roll beyond 3 hexes under Snow, identically to Rain/Mud (Rule 24.2.1) — the two conditions share one visibility number by design.

**24.3.2**  Both infantry and vehicles pay **+1 MP** to enter any hex under Snow, on top of the hex's normal terrain cost. Unlike Rain/Mud, Snow does not trigger the Rule 17.6.2a bog check.

.. container:: rule-guide

   **Why:** Deep snow slows everyone down fairly uniformly, which a flat surcharge captures cleanly, but it doesn't trap a tracked vehicle the way wet mud does — giving Snow its own distinct movement profile (a cost, not a risk) rather than reusing Mud's bog check keeps the two precipitation types mechanically distinguishable by what actually happens on the ground, not just by name.

   **Example:** A tank with M4 (vehicle movement allowance) under Snow spends 4 MP to move 3 open-ground hexes (1 base + 1 Snow surcharge, per hex) instead of the usual 4 hexes — slower, but never at risk of the BOGGED marker Rain/Mud's mud can inflict on it.

24.4  Fog
---------


**24.4.1**  Visual spot range is capped at **1 hex** under Fog — the most restrictive of this section's visibility caps, under the same terms as Rule 24.2.1.

.. container:: rule-guide

   **Why:** Thick ground fog obscures more completely than rain, snow, or even full darkness (Night's own ambient +3 CON row still leaves some sky glow and silhouette to work with) — the 1-hex figure is a wargame-design convention reflecting that severity rather than a number cited to a specific primary source, in the same spirit as design note E.57's Schürzen figure.

   **Example:** A unit may not declare fire or attempt a visual spot roll beyond 1 hex under Fog — even an adjacent-but-one target is untouchable by anything but sound spotting (Rule 14.11) or a lucky automatic reveal (Rule 14.9.3-14.9.4).

**24.4.2**  A unit's hex gains **+2 CON** under Fog, added to the Rule 14.9.7 CON table alongside the existing Night row. Fog does not affect movement cost and does not trigger the Rule 17.6.2a bog check.

.. container:: rule-guide

   **Why:** Fog, like Night, genuinely conceals a stationary unit from a distance beyond simple terrain cover — this is the one weather effect that earns a CON bonus rather than being fully captured by the hard visibility cap alone, since even a spotter within the 1-hex cap is looking through haze that ordinary daylight CON values don't account for. Fog is purely a visibility phenomenon underfoot as well as overhead — it doesn't churn the ground the way rain or snow does, so it carries none of Rule 24.2-24.3's movement effects.

   **Example:** A unit standing in open ground under Fog gets +2 CON on top of whatever terrain cover its hex provides — a meaningful concealment boost even though open ground itself grants none, but two full points less than the +3 Night's own row grants, since some residual ambient visibility still exists in daylight fog that full darkness removes entirely.

**24.4.3**  A Move or Assault Move under Fog that takes a unit beyond the 1-hex cap from where it started, and not through a lit hex (Rule 23.2), is subject to the same movement-risk check as Night (Rule 7.7).

.. container:: rule-guide

   **Why:** Fog causes the same landmark-loss disorientation night does, with no separate ground-condition penalty (Rule 24.3.2's kind of cost) already representing the difficulty — so it reuses Rule 7.7's exact check rather than adding a second one. Rain/Mud and Snow do not get this same check: their difficulty is already represented by Rules 24.2.2-24.2.3 and 24.3.2, and stacking a disorientation roll on top would tax the same condition twice.

   **Example:** A unit moving 3 hexes under Fog with no lit hex along the way rolls Rule 7.7's check exactly as it would at night — on failure, it stops 2 hexes short despite paying for the full move. A unit moving the same distance under Rain/Mud never makes this roll at all; its difficulty is already priced into Rule 24.2.2's bog check and Rule 24.2.3's movement surcharge.

    *See also: Rule 7.7 (the movement-risk check this rule invokes).*
