Section 2 — Game Scale and Conventions
======================================

2.1  Physical Scale
-------------------


**2.1.1**  Tactical scale:  One hex equals 40 yards (approximately 37 metres). This scale is used for squad-level infantry engagements.

.. container:: rule-guide

   **Why:** Fixes the ground truth behind every hex-based range and movement value in the tactical game — without a stated yards-per-hex figure, "range 3" or "MA 4" would have no real-world meaning.

   **Example:** At tactical scale, a target 3 hexes away (Rule 2.3.1) is roughly 120 yards distant — close enough that most small-arms fire lines haven't started falling off yet (Rule 2.4.3).

**2.1.2**  Operational scale:  One hex equals 250 yards, for platoon- and company-level engagements with an armour emphasis. Operational scale is planned as a separate companion manual, developed after this tactical ruleset is finalised — reusing this document's core resolution formulas and procedures, with counters representing larger formations (platoons or equivalent) in place of squads. No operational-scale rules exist in this document; the 250-yard figure is recorded here only to fix what "operational scale" means once that manual is written. See design note E.107.

.. container:: rule-guide

   **Why:** Deliberately sequences operational scale behind the tactical ruleset rather than developing them in parallel — every operational-scale formula (movement allowance, range bands, turn duration) would need rederiving from whatever the tactical values finally settle at, the same way Rule 7.1.2's tactical movement allowance was itself derived from impulse timing. Building it first would mean rebuilding it every time a tactical number changed during this ruleset's own development.

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

   **Why:** Confirms adjacency is range 1, not range 0 — the detail Rule 2.3.4's note flags as having been wrong in early rulebook printings, so it's worth stating explicitly rather than leaving it implied.

   **Example:** Alpha fires at Squad Bravo in the next hex over. Exactly one boundary lies between them, so the shot resolves at range 1, not range 0.

**2.3.4**  Example: firer at A1, target at D1 with B1 and C1 between them. Boundaries crossed: A1/B1, B1/C1, C1/D1 = range 3.

.. container:: rule-guide

   **Why:** Walks the boundary-crossing count (Rule 2.3.1) across a multi-hex line so the counting method is unambiguous even once several hexes separate firer and target, not just at the range-0/range-1 edge cases.

   **Example:** As printed: firer at A1, target at D1, with B1 and C1 in between. The line of fire crosses A1/B1, then B1/C1, then C1/D1 — three boundaries, so the range is 3.

*NOTE: This definition was corrected in v0.6.1. The original wording (v0.1–v0.6) stated 'inclusive of neither' which implied adjacent range = 0 — inconsistent with the stated adjacent range of 1. The boundary-crossing definition is unambiguous and consistent with all examples throughout the rules.*

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

**2.5.2**  Rules already using this convention before it was stated here: Suppressed movement (half M#, round down, minimum 1, Rule 10.1), grenade-phase cover (halved, round down, Rule 9.3.5), flamethrower cover (halved, round down, Rule 21.5.3), and Assault Fire (half eFP, round down, Rule 6.3.3).

.. container:: rule-guide

   **Why:** Is a retroactive index confirming that every halving rule already in the book, written before this convention was formalized, already matched it — so stating the convention here changed no existing numbers, only made the shared rule explicit.

   **Example:** Assault Fire's half-effective-rFP rule (6.3.3) was already round-down before 2.5.1 existed; this rule just points to it as proof the convention isn't a retroactive change to that math.

**2.5.3**  Reaction Points (RP = round(AP / 2), Rule 5.3.4) is a deliberate, separately-made choice and is not affected by this convention — it keeps its own rounding.

.. container:: rule-guide

   **Why:** Flags the one place standard rounding was deliberately not used, so a player doesn't assume 2.5.1's round-down applies universally and misapply it to Reaction Points.

   **Example:** An AP total of 3 converts to RP via round(3 / 2) = round(1.5) = 2 — ordinary round-half-up, not the halve-round-down convention that governs every other halved value in the book.
