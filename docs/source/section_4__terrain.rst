Section 4 — Terrain
===================

4.1  Terrain Types
------------------


**4.1.1**  Each hex is assigned a terrain type. The terrain type determines the cover modifier it provides to units occupying it and any LOS penalty it applies to fire passing through it.

.. container:: rule-guide

   **Why:** Ties one terrain type to two separate effects — defensive cover for the occupant and a fire penalty for anyone shooting through it — so a single map symbol drives both halves of terrain's tactical impact without needing separate occupancy and transit tables.

   **Example:** A hex of dense woods both gives Alpha, if standing in it, strong cover (Rule 4.2) and degrades any fire line that has to pass through that same hex to reach a target beyond it (Rule 4.3).

**4.1.2**  A hex may contain only one terrain type for game purposes. When a hex contains mixed terrain, the dominant terrain type is used.

.. container:: rule-guide

   **Why:** Keeps every hex resolvable with a single cover/LOS lookup rather than requiring a blended calculation whenever real terrain would plausibly mix (a treeline at a field's edge, scattered rubble near a building) — one dominant type per hex is a deliberate simplification, not an oversight.

   **Example:** A hex mapped as mostly open ground with a few scattered trees is treated as open ground for cover and LOS purposes — the minor tree cover doesn't get its own partial modifier.

**4.1.3**  Hexside terrain: walls, fences, and hedgerows are linear features printed on **hexsides**, not hexes. A hexside feature provides its cover modifier only against fire whose line of fire crosses that hexside into the unit's hex — a squad behind a wall is protected from the field beyond it, not from fire coming through its own gate side. Hexside cover does not stack with the hex's own terrain cover: use the better of the two. Crossing a hexside feature costs movement per the Rule 7.2 table; its intervening-fire penalty applies once per such hexside the line of fire crosses (Rule 4.3).

.. container:: rule-guide

   **Why:** Models linear obstacles as directional protection tied to a specific hexside rather than as blanket hex cover, since a wall genuinely only shields against fire from the side it faces — treating it as ordinary hex terrain would wrongly protect a defender from every direction at once.

   **Example:** Alpha, defending behind a wall, gets its +2 cover (Rule 4.2) against Squad Bravo firing from across the wall, but gets no benefit from that same wall against a different enemy firing from Alpha's own side of it.

4.2  Cover Modifiers
--------------------


Cover modifiers are added to the defender's Defence value when resolving fire combat. They represent the protection afforded by the terrain the target occupies. The open ground baseline is +0.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Terrain**
     - **Cover Modifier**
     - **Notes**
   * - Open ground
     - +0
     - Baseline — troops going prone
   * - Crops / tall grass
     - +1
     - Concealment, minimal protection
   * - Wall / fence (hexside — Rule 4.1.3)
     - +2
     - Only vs fire crossing that hexside; not cumulative with hex cover
   * - Hedgerow / bocage (hexside — Rule 4.1.3)
     - +2
     - Only vs fire crossing that hexside; not cumulative with hex cover
   * - Light woods / orchard
     - +3
     - Scattered trees and undergrowth
   * - Ditch / sunken road
     - +3
     - Natural defilade
   * - Dense woods
     - +4
     - Heavy vegetation and tree mass
   * - Building — light (wood/plaster)
     - +4
     - Structural cover
   * - Rubble
     - +4
     - Irregular cover, hard to suppress
   * - Building — heavy (stone/brick)
     - +5
     - Significant structural protection
   * - Entrenchment / foxhole
     - +6
     - Purpose-built field fortification
   * - Fortification / bunker
     - +8
     - Reinforced permanent structure


4.3  Intervening Terrain
------------------------


**4.3.1**  Terrain hexes that the line of fire passes through between the firer's hex and the target's hex impose a per-hex penalty to the attacker's effective rFP.

.. container:: rule-guide

   **Why:** Applies terrain's degrading effect to the shot itself, separately from the target's own cover (Rule 4.2) — a bad line of sight through woods weakens the attack regardless of what the target is standing in.

   **Example:** Alpha fires through a hex of light woods at Squad Bravo standing in open ground. Bravo gets no cover bonus from the woods (it isn't in that hex), but Alpha's effective rFP is still reduced for having fired through it.

**4.3.2**  The firer's hex and the target's hex are not counted as intervening terrain.

.. container:: rule-guide

   **Why:** Keeps the target's own terrain doing its job as cover (Rule 4.2) rather than being double-counted as an intervening penalty too — occupied terrain protects the occupant, it doesn't also degrade the attack a second way.

   **Example:** Squad Bravo standing in dense woods gets that terrain's cover bonus against incoming fire, but the dense-woods hex Bravo occupies is never itself totaled as one of the intervening hexes crossed to reach it.

**4.3.3**  The total intervening penalty is calculated as: penalty per hex × number of hexes of that terrain type crossed.

.. container:: rule-guide

   **Why:** Scales the penalty with exposure — crossing more hexes of the same obstructing terrain compounds the degradation, since a longer stretch of woods or smoke blocks more of the shot than a single hex would.

   **Example:** A fire line crossing two hexes of crops (-1 per hex) takes a total penalty of -2, not the flat -1 it would take for crossing just one such hex.

**4.3.4**  Multiple terrain types may be crossed. Calculate separately for each terrain type and sum.

.. container:: rule-guide

   **Why:** Lets a firing line cross a genuinely mixed intervening path — crops then woods then a hedgerow — with each terrain type's own per-hex penalty (Rule 4.3 table) counted correctly rather than forcing one uniform rate across the whole line of fire.

   **Example:** A line of fire crossing one hex of light woods (-2) and one hedgerow hexside (-1) takes a combined penalty of -3, each terrain type's penalty calculated on its own hexes and then added together.

**4.3.5**  Effective rFP can be driven to 0 or below by accumulated penalties. A fire line at 0 or less contributes nothing and cannot attack (Rule 8.2.5) — dense woods and layered smoke can genuinely stop fire.

.. container:: rule-guide

   **Why:** Confirms that terrain penalties (Rules 4.3.1-4.3.4) aren't merely a soft discount but can zero out a shot entirely, so a firer contemplating a line through heavy obstruction should expect the possibility of no effect at all, not just a weaker one.

   **Example:** A weak fire line crossing two hexes of dense woods (-3 each, so -6 total) can easily be reduced to 0 or below — at that point Rule 8.2.5 says the fire line contributes nothing and that firer cannot attack along it.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Intervening Terrain**
     - **rFP Penalty Per Hex**
   * - Open ground
     - 0
   * - Crops / tall grass
     - -1
   * - Hedgerow / bocage (per hexside crossed — Rule 4.1.3)
     - -1
   * - Light woods
     - -2
   * - Dense woods
     - -3
   * - Smoke (one hex)
     - -3
   * - Building (firing through)
     - -2
   * - Crest hexside crossed at the firer's own level (grazing fire, Rule 4.4a.5)
     - -1


4.4  Line of Sight
------------------


**4.4.1**  Line of sight (LOS) is required to fire at a target. LOS is traced from the centre of the firer's hex to the centre of the target's hex.

.. container:: rule-guide

   **Why:** Sets the geometric baseline every LOS ruling in this section builds on — a single center-to-center line, not a cone or an edge-to-edge check, so blocking terrain (Rules 4.4.2-4.4a) has one consistent path to test against.

   **Example:** Whether an intervening hill hex blocks Alpha's shot at Squad Bravo depends on whether that hex lies on the straight center-to-center line between Alpha's hex and Bravo's — not on whether any part of the hex is near that line.

**4.4.2**  LOS is blocked entirely by the following when it lies in an intervening hex:

.. container:: rule-guide

   **Why:** Separates the small set of terrain that blocks LOS completely from the larger set that merely degrades fire (Rule 4.3) — a firer needs to know before rolling any dice whether a shot is possible at all, not just how penalized it would be.

   **Example:** A solid building hex with no marked windows between Alpha and Squad Bravo blocks the shot entirely — Alpha cannot fire at Bravo along that line no matter how much penalty it might otherwise be willing to accept.

**Higher ground —**  Any hex whose elevation level exceeds the levels of both the firer's and the target's hexes (see Rule 4.4a for elevation LOS in full)

**Cliff —**  A cliff-face hex

**Solid building —**  A building hex not designated as having windows or breaches in the relevant direction

**4.4.3**  Dense woods and other non-blocking terrain degrade fire through the per-hex penalty system (Rule 4.3) but do not block LOS entirely unless three or more consecutive hexes of dense woods intervene.

.. container:: rule-guide

   **Why:** Distinguishes "hard to see through" from "impossible to see through" — most obstructing terrain only weakens a shot (Rule 4.3), and only an unusually deep, consecutive stretch of the densest terrain crosses the line into an outright block.

   **Example:** Two consecutive hexes of dense woods between Alpha and its target degrade the shot but don't block it outright; a third consecutive dense-woods hex in that same line would push it past the threshold into a fully blocked LOS.

**4.4.4**  Reverse slope is a **position relative to a firer**, not a terrain type: a unit is on a firer's reverse slope when Rule 4.4a.4 denies that firer LOS to it across a crest. Such a unit cannot be targeted by that firer's direct fire at all; indirect fire (mortars, Section 16) may target it, and it receives +4 cover against indirect fire in that position (reduced per Rule 16.7.4). The same unit may be fully visible to a different firer on its own side of the crest — always evaluate per firer.

.. container:: rule-guide

   **Why:** Frames reverse slope as a relationship between two specific hexes rather than a fixed map label, since the same ground can be dead space to one firer across a hill and completely open to a different firer on the same side of it — the crest LOS math (Rule 4.4a.4) has to be re-checked per firer, not looked up once per hex.

   **Example:** Squad Bravo sits just behind a crest, invisible to Alpha's direct fire on the far side and only reachable there by indirect fire with +4 cover — but a friendly unit sharing Bravo's own side of the crest sees and can be seen by Bravo normally.

4.4a  Elevation and LOS
-----------------------


**4.4a.1**  Every hex has an elevation level printed on the map: level 0 (ground) unless marked higher. A **crest hexside** is any hexside between two hexes of different elevation levels.

.. container:: rule-guide

   **Why:** Gives elevation a precise, printed value and names the specific boundary (the crest hexside) where it changes, since every rule that follows in this subsection — blocking, blind zones, grazing fire — depends on being able to point at exactly where a level change occurs.

   **Example:** A hex printed as level 1 sitting next to a level-0 hex has a crest hexside between them; that specific hexside is what Rule 4.4a.5's grazing-fire penalty and Rule 4.4a.4's blind-zone rule both key off.

**4.4a.2**  An intervening hex whose level is **equal to or higher than the higher** of the firer's and target's levels blocks LOS (Rule 4.4.2). Two units on top of the same hill see each other normally — hexes at their shared level on the hill mass between them block per this rule only if higher than both.

.. container:: rule-guide

   **Why:** Keeps two units standing on the same high ground able to see each other normally, since the hill mass between them is at their own level, not above it — only terrain that actually rises above both endpoints earns the outright block.

   **Example:** Alpha and Squad Bravo both stand on a level-2 plateau with more level-2 ground between them. That intervening ground doesn't block their LOS to each other, since it's equal to, not higher than, both their levels.

**4.4a.3**  An intervening hex at or below the **lower** endpoint's level never blocks LOS by elevation (its terrain may still degrade or block fire under Rules 4.3/4.4.2 — a unit two levels up still cannot see through a solid building).

.. container:: rule-guide

   **Why:** Separates elevation blocking from terrain blocking as two independent checks — low ground can never hide a target by elevation alone, but it can still contain a building or dense woods that blocks or degrades the shot for ordinary terrain reasons.

   **Example:** A level-0 hex between a hilltop firer and a level-0 target never blocks LOS just for being low ground — but if that same hex contains a solid building, Rule 4.4.2 still blocks the shot on terrain grounds.

**4.4a.4**  Crest blind zone: an intervening hex at an **intermediate** level (higher than the lower endpoint, lower than the higher endpoint) blocks LOS only to lower-level hexes **adjacent to it on the far side** — the ground immediately behind a crest is defiladed from observers beyond it. Lower-level hexes farther from the crest are visible over it. An intermediate hex adjacent to the higher unit never blocks (the unit looks over its own near crest).

.. container:: rule-guide

   **Why:** Models the real dead ground directly behind a ridgeline — a slope blocks the observer's view only into the pocket immediately behind it, not the whole area beyond, since terrain farther back rises back into view over the crest.

   **Example:** As worked in Rule 4.4a.6: a level-2 firer looking past an intermediate level-1 hex cannot see into the level-0 hex immediately behind that hex on the far side (the blind zone), but can see a level-0 hex farther beyond it.

**4.4a.5**  Grazing fire: LOS traced at the firer's own level that crosses one or more crest hexsides (skimming a ridge line between same-level positions) suffers -1 effective rFP per crest hexside crossed (Rule 4.3 table).

.. container:: rule-guide

   **Why:** Penalizes a shot that skims along uneven ground at the firer's own level, since a line of fire threading a ridge's ups and downs is realistically harder to keep clear than one crossing flat terrain, even when nothing outright blocks it.

   **Example:** Alpha's shot at a same-level target crosses two crest hexsides along the way. That's a -2 effective rFP grazing-fire penalty (Rule 4.3 table), on top of any other intervening-terrain penalties on the same line.

**4.4a.6**  Example: A fires from a level-2 hilltop at B on level 0, five hexes away, with a level-1 hex three hexes out along the line. B is visible (level 0, not adjacent to the level-1 hex on the far side). C, in the level-0 hex directly behind the level-1 hex, is in the crest blind zone — invisible to A, on A's reverse slope (Rule 4.4.4), and targetable by A's side only with indirect fire. C sees and fights normally against anything on its own side of the crest.

.. container:: rule-guide

   **Why:** Walks the elevation-LOS rules (4.4a.2-4.4a.4) through one concrete layout so a player can check their own understanding of blind zones and reverse slope against a known-correct worked case, rather than reasoning through the abstract rules cold.

   **Example:** As printed: A on a level-2 hilltop can see B on level 0 five hexes away (not adjacent to the intervening level-1 hex on the far side), but cannot see C directly behind that level-1 hex — C is in the blind zone, on A's reverse slope, reachable only by indirect fire from A's side.

4.5  Elevation Combat Modifiers
-------------------------------


**4.5.1**  Units firing from a higher elevation than their target receive a bonus to effective rFP.

.. container:: rule-guide

   **Why:** Rewards holding the high ground with a direct firepower bonus, on top of whatever LOS advantages elevation already grants (Rule 4.4a) — height doesn't just help a unit see, it helps its shots hit harder.

   **Example:** Alpha firing from one level higher than Squad Bravo gets +1 effective rFP (Rule 4.5 table) added on top of its base fire line's value at that range.

**4.5.2**  Units firing at a target on higher ground treat the target's terrain cover as one step higher than printed.

.. container:: rule-guide

   **Why:** Reflects that shooting uphill at a defender is doubly hard — the target's own terrain cover (Rule 4.2) is compounded by the attacker's disadvantageous angle, so elevation penalizes the low firer on both the attack roll and the target's effective protection.

   **Example:** Squad Bravo defending in light woods (+3 cover) one level above Alpha is treated as if in the next-higher cover bracket (+4, as if in dense woods or a light building) for Alpha's shot, even though Bravo's printed terrain cover value hasn't changed.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **Modifier**
   * - Firer 1 elevation level higher than target
     - +1 effective rFP
   * - Firer 2 or more levels higher than target
     - +2 effective rFP
   * - Target 1 level higher than firer
     - +1 to target cover modifier
   * - Target 2 or more levels higher than firer
     - +2 to target cover modifier
