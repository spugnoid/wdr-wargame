Section 2 — Game Scale and Conventions
======================================

2.1  Physical Scale
-------------------


**2.1.1**  Tactical scale:  One hex equals 40 yards (approximately 37 metres). This scale is used for squad-level infantry engagements.

.. container:: rule-guide

   **Why:** Fixes the ground truth behind every hex-based range and movement value in the tactical game — without a stated yards-per-hex figure, "range 3" or "MA 4" would have no real-world meaning.

   **Example:** At tactical scale, a target 3 hexes away (Rule 2.3.1) is roughly 120 yards distant — close enough that most small-arms fire lines haven't started falling off yet (Rule 2.4.3).

**2.1.2**  Operational scale:  One hex equals 250 yards, for platoon- and company-level engagements with an armour emphasis. Operational scale is planned as a separate companion manual, developed after this tactical ruleset is finalised — reusing this document's core resolution formulas and procedures, with counters representing larger formations (platoons or equivalent) in place of squads. No operational-scale rules exist in this document; the 250-yard figure is recorded here only to fix what "operational scale" means once that manual is written.

.. container:: rule-guide

   **Why:** Deliberately sequences operational scale behind the tactical ruleset rather than developing them in parallel — every operational-scale formula (movement allowance, range bands, turn duration) would need rederiving from whatever the tactical values finally settle at, the same way Rule 7.1.2's tactical movement allowance is itself derived from real-world marching pace over a game turn. Building it first would mean rebuilding it every time a tactical number changed during this ruleset's own development.

   **Example:** A unit's printed range values don't change between scales, but what they represent does: range 3 at operational scale would cover roughly 750 yards, ground that takes over six tactical-scale hexes to cross — but the formulas that turn that printed range into an actual combat result belong to the companion manual, not this document.

**2.1.3**  All range values on counters are expressed in hexes appropriate to the current map scale.

.. container:: rule-guide

   **Why:** Keeps range values scale-relative rather than fixed, since the same printed range on a counter would mean a very different real-world distance depending on whether it's read on a tactical or (future) operational map (Rules 2.1.1-2.1.2).

   **Example:** A fire line printed with a range-3 falloff step means the same 3 hexes at any scale this system is ever played at — only the real-world distance behind those 3 hexes changes.

*NOTE: Yards are used rather than metres because primary source data for WWII weapons — US, British, and German — is predominantly expressed in yards. Soviet data is in metres, but rounding error at game scale is negligible.*

2.2  Time Scale
---------------


**2.2.1**  One game turn represents approximately 2 to 5 minutes of real time at tactical scale.

.. container:: rule-guide

   **Why:** Anchors the turn as an abstraction of a short, chaotic burst of combat rather than a fixed clock tick — the range (2 to 5 minutes) exists because a turn compresses a variable amount of real action, not a metronome-precise interval.

   **Example:** A single game turn covering Alpha's Fire action, Squad Bravo's movement, and any reactions between them represents that whole exchange happening in roughly 2 to 5 minutes of real time, not a fixed number of seconds per action.

**2.2.2**  The number of turns per scenario is defined in the scenario parameters.

.. container:: rule-guide

   **Why:** Keeps scenario length out of the core rules entirely, since a fair turn count depends on the specific map, forces, and objectives of each scenario rather than any fixed value the rules could state.

   **Example:** A small skirmish scenario might run 6 turns while a larger battle runs 20 — both are valid because each scenario's own parameters set that number, not Section 2.

*[ TBD: Operational scale time per turn to be determined during playtesting. ]*

2.3  Measurement Conventions
----------------------------


**2.3.0**  Hex grid and coordinates: maps use columns of hexes running top to bottom, lettered A, B, C… from the left, and rows numbered 1, 2, 3… from the top. A hex is named by its column letter then its row number — A1, D4, F6. Columns alternate between higher and lower vertical offset, with **odd-lettered columns (A, C, E…) set half a hex lower** than the even columns beside them. Every hex therefore has six neighbours: the hex above it, the hex below it, and two in each adjacent column.

.. container:: rule-guide

   **Why:** Fixes the one convention everything else in the game is measured against. Without a stated column-offset direction, "adjacent" is ambiguous on a hex grid and no range, movement cost, line of sight, or setup zone can be resolved the same way by both players.

   **Example:** On an odd-column-low grid, hex C3's six neighbours are C2 (above), C4 (below), B3 and B4 (to the left), and D3 and D4 (to the right). Hex D3's neighbours are D2, D4, C2, C3, E2 and E3 — the offset runs the other way, because D is an even column.

**2.3.1**  Range equals the number of hex boundaries the line of fire crosses to reach the target. The firer's own hex is not counted. The target's hex is counted.

.. container:: rule-guide

   **Why:** Defines range as boundaries crossed, not hexes occupied, because that's the definition that gives a clean answer at every distance including 0 and 1 (Rules 2.3.2-2.3.3) without special-casing them.

   **Example:** Alpha fires at Squad Bravo two hexes away with one hex directly between them. The line of fire crosses the boundary into that middle hex and then the boundary into Bravo's hex — two boundaries, so range 2.

**2.3.2**  A unit firing at a target in the same hex fires at range 0. Zero boundaries are crossed.

.. container:: rule-guide

   **Why:** Makes same-hex fire the natural zero case of the boundary-crossing definition (Rule 2.3.1) rather than an exception carved out for it.

   **Example:** Alpha and an enemy unit occupy the same hex. No boundary separates them, so Alpha fires at range 0 — the closest range the falloff notation (Rule 2.4) ever applies to.

**2.3.3**  A unit firing at a target in an adjacent hex fires at range 1. One boundary is crossed — the boundary between the firer's hex and the target's hex.

.. container:: rule-guide

   **Why:** Confirms adjacency is range 1, not range 0 — the one point where the boundary-crossing definition is easiest to misread, so it's worth stating explicitly rather than leaving it implied.

   **Example:** Alpha fires at Squad Bravo in the next hex over. Exactly one boundary lies between them, so the shot resolves at range 1, not range 0.

**2.3.4**  Example: firer at A1, target at D1 with B1 and C1 between them. Boundaries crossed: A1/B1, B1/C1, C1/D1 = range 3.

.. container:: rule-guide

   **Why:** Walks the boundary-crossing count (Rule 2.3.1) across a multi-hex line so the counting method is unambiguous even once several hexes separate firer and target, not just at the range-0/range-1 edge cases.

   **Example:** As printed: firer at A1, target at D1, with B1 and C1 in between. The line of fire crosses A1/B1, then B1/C1, then C1/D1 — three boundaries, so the range is 3.

2.4  Notation System
--------------------


With Deepest Regret... uses a specific counter notation for firepower and falloff. Understanding this notation is essential before play.

**2.4.1**  Fire line notation:  Each fire line is expressed as: rFP [icon] ⬡h -f

.. container:: rule-guide

   **Why:** Gives every printed fire line the same four-part shape so a player can read any counter the same way once the notation is learned, instead of needing a different lookup per weapon type.

   **Example:** A rifle squad's printed fire line and a machine gun's printed fire line both follow the same rFP [icon] ⬡h -f layout — only the numbers and icon differ, not the structure.

**2.4.2**  rFP  is the base firepower at range 0-1 before any falloff.

.. container:: rule-guide

   **Why:** Anchors rFP to the closest ranges specifically so every falloff calculation (Rule 8.2) has a fixed, unpenalized starting value to fall off from.

   **Example:** A fire line's printed rFP of 7 is exactly what Alpha rolls with at range 0 or range 1 — falloff (Rule 2.4.4) hasn't started reducing it yet at those ranges.

**2.4.3**  ⬡h  is the hex interval — the number of hexes between each FP reduction step. The value h is printed inside a small hexagon shape on the counter.

.. container:: rule-guide

   **Why:** Separates "how far before FP drops" (⬡h) from "how much it drops by" (-f, Rule 2.4.4) as two independent numbers, since weapons vary in both how quickly and how steeply they lose effectiveness with range.

   **Example:** A fire line printed with ⬡4 loses FP every 4 hexes of range — a weapon printed with ⬡2 instead would lose FP twice as often over the same distance.

**2.4.4**  -f  is the falloff loss — the amount by which rFP decreases at each interval step.

.. container:: rule-guide

   **Why:** Is the other half of the falloff pair with ⬡h (Rule 2.4.3) — together the two values fully describe a weapon's whole range curve from just two printed numbers.

   **Example:** A fire line printed -1 loses exactly 1 FP at each interval step it crosses; a fire line printed -2 on the same ⬡h would fall off twice as fast per step.

**2.4.5**  Example:  A fire line reading 7 ⬡4 -1 means: base FP 7, loses 1 FP for every 4 hexes of range beyond hex 1.

.. container:: rule-guide

   **Why:** Ties all three notation elements (rFP, ⬡h, -f, Rules 2.4.2-2.4.4) together in one worked reading so a player can check their own interpretation of a printed fire line against a known-correct example.

   **Example:** As printed: 7 ⬡4 -1 means base FP 7 at ranges 0-1, dropping to 6 once range passes the first 4-hex interval beyond hex 1, to 5 after the next, and so on.

**2.4.6**  The [icon] preceding the rFP value identifies the weapon class. See Section 3.1 for weapon class icons.

.. container:: rule-guide

   **Why:** Keeps weapon-class identification (which governs things like target-type effectiveness elsewhere in the rules) as a glance-readable icon rather than requiring a name lookup for every fire line on a counter.

   **Example:** Two fire lines with identical rFP ⬡h -f values but different icons represent different weapon classes — the icon, not the numbers, is what tells a player which class-specific rules (Section 3.1) apply.

2.5  Rounding Conventions
--------------------------


**2.5.1**  Unless a specific rule states otherwise, **halve, round down** is this game's standard convention wherever a value is halved (minimum 1 where a rule says so explicitly, e.g. Suppressed movement, Rule 10.1).

.. container:: rule-guide

   **Why:** Sets one default rounding rule so a new halving rule added anywhere in the book doesn't need to restate how to round — silence means round down, and only an explicit minimum overrides that.

   **Example:** A rule that halves Alpha's eFP without mentioning rounding uses round-down by default: an eFP of 5 halves to 2, not 3, unless that rule states a minimum.

**2.5.2**  Rules that use this convention: Suppressed movement (half M#, round down, minimum 1, Rule 10.1), grenade-phase cover (halved, round down, Rule 9.3.5), flamethrower cover (halved, round down, Rule 21.5.3), and Assault Fire (half FPr, round down, Rule 6.3.3).

.. container:: rule-guide

   **Why:** Indexes every halving rule in the book that runs on the standard convention, so a player can confirm at a glance which specific rules 2.5.1 governs rather than hunting for them.

   **Example:** Assault Fire's half-FPr rule (6.3.3) rounds down under 2.5.1's convention; this rule points to it, and to the other three, as the full list of places that convention is already in play.

**2.5.3**  Reaction Points (RP = round(AP / 2), Rule 5.3.4) is a deliberate, separately-made choice and is not affected by this convention — it keeps its own rounding.

.. container:: rule-guide

   **Why:** Flags the one place standard rounding was deliberately not used, so a player doesn't assume 2.5.1's round-down applies universally and misapply it to Reaction Points.

   **Example:** An AP total of 3 converts to RP via round(3 / 2) = round(1.5) = 2 — ordinary round-half-up, not the halve-round-down convention that governs every other halved value in the book.

2.6  The Check
--------------


*Everything in this game that is not fire combat is resolved by a Check. Fire combat keeps its own three-dice procedure (Rule 8.1.6) and is never a Check.*

**2.6.1**  A **Check** is one roll of **1d6**, plus modifiers, against a threshold. Meet or beat the threshold and the Check passes. A natural **1** always fails and a natural **6** always passes, whatever the modifiers.

.. container:: rule-guide

   **Why:** One resolution shape for morale, rally, recovery, spotting, bail-out, breaching, demolition, unjamming, extinguishing, capture and every other non-combat question in the book means a player learns it once and never looks it up again. The natural 1 and 6 keep the arithmetic honest at the extremes — no modifier stack ever makes a Check automatic or impossible, so there is always a reason to roll.

   **Example:** A Pinned squad's Recovery Phase roll, a sniper detection roll, a bail-out check and an engineer's breach attempt are all the same act: roll a d6, add what applies, compare to a number.

**2.6.2**  Standard modifiers. Unless a Check's own rule says otherwise, these apply and nothing else does:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Modifier**
     - **Value**
     - **Source**
   * - Officer within command radius
     - **+ that officer's CMD**
     - Rule 12.2.1 — the largest modifier in the game, and the reason leaders matter
   * - No officer in radius
     - **+1**, the unit's own inherent NCO
     - Rule 12.4.1a. Never added to an officer's CMD — take whichever applies, not both
   * - Unit's own quality
     - + its Morale modifier
     - Rule 15.2.1a
   * - Suppressed
     - −1
     - Rule 10.2
   * - Pinned
     - −2
     - Rule 10.3


.. container:: rule-guide

   **Why:** Fixes one modifier set for every Check so a player is never hunting for which bonuses apply to which roll. Command is deliberately the heaviest term: a CMD 3 officer swings a Check by half the die, which is why a force that loses its leaders does not merely act less often — it starts failing at everything it still tries to do.

   **Example:** A Regular squad (+0) that is Suppressed (−1) but has a CMD 2 officer in radius (+2) rolls 1d6 +1 against the threshold. The same squad with its officer dead falls back on its own NCO and rolls 1d6 +0 — worse, but not helpless.

**2.6.3**  Degree — the **d8**. When a Check needs to know not just whether but *how much*, throw a d8 alongside the d6 and read both from the one throw: the d6 says whether it worked, the d8 says how well, on that rule's own table. A failed Check ignores the d8.

.. container:: rule-guide

   **Why:** Keeps "did it work" and "how well did it work" in a single throw rather than a roll followed by another roll, and gives the d8 a consistent job across the whole book so a player knows what it is for the moment they pick it up.

   **Example:** An engineer places a demolition charge: the d6 says whether the charge was set properly under fire, and the d8 thrown with it says how much of the wall came down.

**2.6.4**  Direction — the **d12**. When a rule needs a direction or a scatter, read the d12 as a clock face centred on the hex in question, with the six hex directions at 12, 2, 4, 6, 8 and 10 o'clock; a reading between two directions takes the lower of the two.

.. container:: rule-guide

   **Why:** A twelve-sided die is a clock, and a hex has six sides — so one throw gives a direction with a built-in bias toward the cardinal ones without a conversion table. Reusing it for every scatter, dispersion and drift in the game means mortar rounds, thrown charges and routing all read the same way.

   **Example:** A mortar round disperses: the d12 comes up 7, which lies between the 6 and 8 o'clock directions, so the round drifts in the 6 o'clock direction.

**2.6.5**  Rolls that are **not** Checks: fire combat resolution (Rule 8.1.6), the vehicle Gunnery Roll (Rule 18.1a.3), and the penetration and damage rolls that follow from them (Rules 18.3, 18.4, 18.6). These keep their own procedures.

.. container:: rule-guide

   **Why:** Combat is the one place where the three dice together are doing deliberate distributional work — the 1d6+1d8+1d12 spread and the result bands of Appendix C are calibrated against each other. Carving combat out keeps the Check simple everywhere else without disturbing the maths the rest of the game is balanced on.

   **Example:** Firing at a squad is not a Check; the squad's morale test after being hit is.
