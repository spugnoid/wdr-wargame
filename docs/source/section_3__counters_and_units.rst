Section 3 — Counters and Units
==============================

3.1  Counter Types
------------------


Each unit type is identified by a geometric symbol on the counter face. The following symbols are used:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Symbol**
     - **Unit Type**
   * - [X] — Rectangle with X
     - Rifle squad
   * - [·] — Rectangle with dot
     - SMG squad
   * - [—] — Rectangle with line
     - LMG team
   * - (—) — Oval with line
     - HMG team / crewed weapon
   * - ◆ — Diamond
     - Leader
   * - △ — Triangle
     - Sniper team
   * - [→] — Rectangle with arrow
     - Anti-tank rifle team
   * - △· — Triangle with dot
     - Mortar team
   * - [≋] — Rectangle with waves
     - Flamethrower team
   * - ○ — Circle
     - Vehicle / AFV


3.2  Counter Faces
------------------


**3.2.1**  Each infantry counter has two faces: full strength (front) and reduced strength (rear).

.. container:: rule-guide

   **Why:** Gives every infantry counter a built-in, physical way to represent a step loss — flip the counter — instead of needing a separate marker or paper track to record reduced strength.

   **Example:** Alpha starts a scenario at full strength, front face up. After taking a step loss, the counter is flipped to its rear face for the rest of the game (unless restored) — no extra components needed.

**3.2.2**  The front face represents the unit at full establishment strength with all weapons operational.

.. container:: rule-guide

   **Why:** Establishes the front face as the unit's baseline stats — every other face and every degraded state in the game is defined relative to this one.

   **Example:** Alpha's printed front-face fire line, Move allowance, and Defence value are what the unit uses in every calculation until something (a step loss, a status effect) changes its state.

**3.2.3**  The rear face represents the unit after a step loss. Rear face stats are independently calculated from a reduced TO&E — they are not simply halved front face values.

.. container:: rule-guide

   **Why:** Prevents rear-face stats from being derived by a simple halving formula, since a unit missing a specific weapon or personnel slot loses capability unevenly — the actual reduced organization is what determines the numbers, not an arbitrary fraction of the full-strength ones.

   **Example:** A rifle squad's rear face doesn't automatically show half its front-face rFP — it shows whatever the squad's actual reduced TO&E (say, missing its automatic rifleman) produces, which may be more or less than half.

**3.2.4**  Morale value is identical on both faces. Unit quality does not degrade from a single step loss.

.. container:: rule-guide

   **Why:** Separates physical capability (which degrades with a step loss) from will to fight (which doesn't) — a unit that's lost a man is weaker in firepower but not automatically more likely to break.

   **Example:** Alpha's Morale value stays the same after flipping to its rear face — only its combat-relevant stats like Defence (Rule 3.2.5) and fire lines change.

**3.2.5**  Defence value is reduced by 2 on the rear face, to a minimum of 1.

.. container:: rule-guide

   **Why:** Reflects a reduced unit's smaller size and thinner defensive posture as a flat, easy-to-apply penalty rather than requiring a fresh Defence calculation for every rear face.

   **Example:** A unit with a front-face Defence of 3 shows a rear-face Defence of 1 (3 − 2); a unit with a front-face Defence of 2 also shows 1, since the −2 floors at the stated minimum rather than going to 0.

**3.2.6**  Weapon counters (independently crewed weapons) also have two faces: full crew (front) and reduced crew (rear). Reduced crew fire lines reflect degraded rate of fire. The ⬡h interval value is identical on both faces — weapon physics do not change with crew size.

.. container:: rule-guide

   **Why:** Draws the line between what crew size affects (how fast and how much the weapon fires — rFP and rate of fire) and what it doesn't (the weapon's physical range characteristics — ⬡h, Rule 2.4.3), since a smaller crew slows a gun down but doesn't change its ballistics.

   **Example:** An HMG team's rear (reduced-crew) face prints a lower rFP than its front face, but both faces print the same ⬡h interval — a two-man crew doesn't make the gun's rounds fall off differently with range than a full crew would.

3.3  Action Values
------------------


The upper right corner of each counter shows three action values:

**3.3.1**  M# — Move allowance.  The number of hexes the unit may move per activation. M0 means the unit cannot move in its current state (e.g., a deployed HMG).

.. container:: rule-guide

   **Why:** Makes M0 a normal, expected value rather than an error case — a unit's mobility is a state, and a deployed heavy weapon simply has zero of it until redeployed.

   **Example:** A deployed HMG team prints M0 F3 G1 — it can still fire and use grenades in an assault, but cannot move until it's limbered (switching to its M1 F0 G0 mobile profile).

**3.3.2**  F# — Fire rate.  The number of fire actions the unit may take per turn. *Interim note: a unit's actual turn structure (one full-effect fire, or two reduced Assault fires, or — for a stationary machine gun — repeated full-effect fire under ROF) is governed by Rule 6.3/6.6, not by this printed value. F# predates that rule and is not currently consulted by it; reconciling the two is a planned counter-data review.*

.. container:: rule-guide

   **Why:** Documents F# honestly as a legacy printed value that the current action-economy rules (6.3/6.6) don't actually read, rather than silently pretending it's still authoritative — a player consulting a counter shouldn't be misled about what governs its turn structure today.

   **Example:** A rifle squad's printed F2 doesn't mean "exactly two fires, no more, no less" under the current rules — its actual options (one full Fire, two Assault Fires, etc.) come from Rule 6.3/6.6, and F2 is not consulted to decide between them.

**3.3.3**  G# — Grenade value.  The unit's effectiveness in the grenade phase of close assault. Used only during close assault resolution (see Section 9).

.. container:: rule-guide

   **Why:** Scopes G# tightly to one specific step of one specific procedure (the grenade phase of close assault, Section 9) so it doesn't get confused with the unit's general firepower stats, which come from its fire lines instead.

   **Example:** A Panzergrenadier squad's G4 only matters once a close assault reaches its grenade phase — it plays no role in that squad's ordinary ranged Fire actions, which use its printed fire line and rFP instead.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit Type**
     - **Standard Action Values**
     - **Notes**
   * - Rifle squad
     - M2 F2 G3
     - 
   * - SMG squad
     - M2 F2 G3
     - 
   * - Panzergrenadier squad
     - M2 F2 G4
     - Higher grenade value reflects assault doctrine
   * - Guards rifle squad
     - M2 F2 G4
     - 
   * - LMG team
     - M2 F3 G2
     - Sustained fire capability
   * - HMG team (deployed)
     - M0 F3 G1
     - Cannot move while deployed
   * - HMG team (mobile)
     - M1 F0 G0
     - Cannot fire while mobile
   * - Sniper team
     - M1 F1 G0
     - One careful shot per turn
   * - Leader
     - M3 F1 G0
     - High mobility, rarely fires directly


3.4  Fire Line Notation
-----------------------


**3.4.1**  A counter may display one, two, or three fire lines depending on the weapon mix of the unit.

.. container:: rule-guide

   **Why:** Lets a mixed-weapon unit's counter reflect its actual armament honestly — a squad carrying both a rifle and an LMG needs two separate fire lines because the weapons have different falloff characteristics, not one averaged-together line.

   **Example:** A rifle squad with only rifles prints one fire line; a squad that also carries an LMG prints two — one per weapon class it fields in meaningful numbers (Rule 3.4.3).

**3.4.2**  Each fire line represents a distinct weapon class within the unit.

.. container:: rule-guide

   **Why:** Keeps each weapon class's own falloff notation (Section 2.4) separate rather than merging different weapons' ranges and firepower into one misleading combined line.

   **Example:** A unit's rifle fire line and its LMG fire line each carry their own rFP ⬡h -f values — Rule 8.1.1a already covers how both lines contribute to the same Fire action without merging their numbers.

**3.4.3**  A minimum rFP threshold of 2 is required for a weapon class to appear as a separate fire line. Weapon contributions below this threshold are omitted from the counter.

.. container:: rule-guide

   **Why:** Keeps counters readable by leaving off weapon contributions too small to matter on their own, rather than cluttering every counter with a fire line for every pistol and grenade a unit's personnel might individually carry.

   **Example:** A squad's individual sidearms contribute rFP well under 2 — that contribution doesn't get its own fire line and is simply absent from the counter, not folded into another line.

**3.4.4**  Weapon class icons appear to the left of the rFP value on each fire line:

.. container:: rule-guide

   **Why:** Makes weapon class identifiable at a glance from the icon alone (Rule 2.4.6), without needing to read the numeric rFP ⬡h -f values first to guess what kind of weapon they belong to.

   **Example:** Seeing a ─● icon on a fire line tells a player it's an LMG bipod weapon before they even check its rFP or ⬡h — the icon and the class are a fixed one-to-one mapping.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Icon**
     - **Weapon Class**
     - **Typical ⬡h interval**
   * - ╌  (single dash)
     - Rifle (bolt/semi-auto)
     - ⬡4 to ⬡5
   * - ≡  (triple dash)
     - SMG / submachine gun
     - ⬡1
   * - ─● (dash-dot)
     - LMG bipod
     - ⬡3 to ⬡5
   * - ═● (double dash-dot)
     - HMG tripod
     - ⬡6
   * - ╌○ (dash-circle)
     - Sniper / precision rifle
     - ⬡6 to ⬡8
   * - ──► (dash-arrow)
     - Anti-tank rifle
     - ⬡4 to ⬡6
   * - ▲  (triangle)
     - Mortar
     - Special — see Section 16 (Mortars and Smoke)


3.5  Stacking Limits
--------------------


**3.5.1**  A maximum of 3 combat units may occupy a single hex at any time.

.. container:: rule-guide

   **Why:** Caps how much combat power can pile into one hex, which keeps a single successful attack from being able to wipe out an unlimited concentration of force and forces a player to spread out to mass firepower.

   **Example:** Alpha, Squad Bravo, and a third combat unit can share a hex; a fourth combat unit cannot join them there until one of the three leaves, regardless of how much room the map hex represents.

**3.5.2**  Leaders do not count toward the stacking limit.

.. container:: rule-guide

   **Why:** Lets a leader accompany a full stack of combat units for its command benefits without displacing one of them, since a leader represents an attached individual rather than an additional fighting formation competing for the same hex.

   **Example:** Alpha, Squad Bravo, and a third combat unit already fill a hex to its 3-unit limit; a leader can still join that same hex without violating Rule 3.5.1.

**3.5.3**  Independently crewed weapon counters (HMG teams, mortar teams, AT gun teams) do not count toward the stacking limit when stacked beneath their parent squad. A weapon counter's **parent squad** is the friendly squad it is currently stacked with; if stacked with more than one squad, the owning player designates which is the parent. Parenthood transfers simply by stacking with a different friendly squad.

.. container:: rule-guide

   **Why:** Treats a crewed weapon as traveling with its supporting squad rather than as an independent stacking slot, as long as that relationship is clear — the parent-squad designation exists specifically to resolve which squad "hosts" the weapon when more than one candidate is present.

   **Example:** An HMG team stacked with Squad Bravo doesn't count against the hex's 3-unit limit as long as Bravo is its parent; if the HMG later moves to stack with a different friendly squad instead, that squad becomes its new parent.

**3.5.4**  Weapon counters that have separated from their parent squad count as a combat unit for stacking purposes.

.. container:: rule-guide

   **Why:** Closes the loophole that a weapon team without a parent squad nearby (Rule 3.5.3) would otherwise stack for free — once it's on its own, it occupies a stacking slot like any other combat unit.

   **Example:** An HMG team left behind when Squad Bravo advances is no longer stacked beneath a parent squad, so it now counts as one of the hex's 3 permitted combat units in its own right.

**3.5.5**  Prisoner markers do not count toward the stacking limit.

.. container:: rule-guide

   **Why:** Keeps captured personnel from competing with combat units for stacking room, since a prisoner marker represents disarmed troops under guard rather than a fighting force.

   **Example:** A hex already at its 3-unit combat limit can still hold a prisoner marker under guard (Section 11) without needing to remove one of the combat units first.

3.6  Unit Status Markers
------------------------


Small markers are placed on or beside unit counters to track their current state. Action markers (ASSAULT, FIRED 1/2/3, MOVED/FIRED, CARELESS) are removed during the Recovery Phase at the start of each turn; status markers (SUPPRESSED, PINNED, and the like) persist until removed by their own rules — a recovery roll, a rally, or the condition ending (Rules 5.2.2–5.2.4).

FIRED 1/2/3 is one physical component: a rotating dial marker showing "1", "2", or "3", not three separate chits. MOVED/FIRED and CARELESS are likewise one physical component — a two-sided marker — since Careless Movement (Rule 7.4) is only ever taken as a Regular Move action, which always ends the unit's turn; a unit is never MOVED/FIRED-without-CARELESS-info-loss and CARELESS-without-MOVED/FIRED at once, so a unit is never in a state needing both faces shown simultaneously (Rule 7.4.2). See design notes E.96–E.97.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Marker**
     - **Meaning**
   * - ASSAULT
     - Unit has taken one Assault part-action this turn; one remains (Rule 6.3.3)
   * - FIRED 1
     - Stationary ROF-greater-than-1 weapon has fired once this turn (Rule 6.6)
   * - FIRED 2
     - Fired twice this turn
   * - FIRED 3
     - Fired three times this turn (tripod HMG only)
   * - MOVED/FIRED
     - Unit is done for the turn — no further movement or fire (Rule 6.7 covers remaining defensive rights). Front face of the shared MOVED/FIRED-CARELESS marker.
   * - CARELESS
     - Unit moved M#+1 hexes this turn and suffers -2 CON for the remainder of it (Rule 7.4). Reverse face of the shared MOVED/FIRED-CARELESS marker — always accompanies MOVED/FIRED, never appears alone.
   * - SUPPRESSED
     - Unit is suppressed (see Section 10.2)
   * - PINNED
     - Unit is pinned (see Section 10.3)
   * - MOBILE
     - Weapon counter is limbered and moving; cannot fire
   * - GUARD
     - Unit is guarding prisoners; movement and fire restricted
