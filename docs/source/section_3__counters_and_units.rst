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

**3.2.2**  The front face represents the unit at full establishment strength with all weapons operational.

**3.2.3**  The rear face represents the unit after a step loss. Rear face stats are independently calculated from a reduced TO&E — they are not simply halved front face values.

**3.2.4**  Morale value is identical on both faces. Unit quality does not degrade from a single step loss.

**3.2.5**  Defence value is reduced by 2 on the rear face, to a minimum of 1.

**3.2.6**  Weapon counters (independently crewed weapons) also have two faces: full crew (front) and reduced crew (rear). Reduced crew fire lines reflect degraded rate of fire. The ⬡h interval value is identical on both faces — weapon physics do not change with crew size.

3.3  Action Values
------------------


The upper right corner of each counter shows three action values:

**3.3.1**  M# — Move allowance.  The number of hexes the unit may move per activation. M0 means the unit cannot move in its current state (e.g., a deployed HMG).

**3.3.2**  F# — Fire rate.  The number of fire actions the unit may take per turn.

**3.3.3**  G# — Grenade value.  The unit's effectiveness in the grenade phase of close assault. Used only during close assault resolution (see Section 9).

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit Type**
     - **Standard Action Values**
     - **Notes**
   * - Rifle squad
     - M1 F2 G3
     - 
   * - SMG squad
     - M1 F2 G3
     - 
   * - Panzergrenadier squad
     - M1 F2 G4
     - Higher grenade value reflects assault doctrine
   * - Guards rifle squad
     - M1 F2 G4
     - 
   * - LMG team
     - M1 F3 G2
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
     - M2 F1 G0
     - High mobility, rarely fires directly


3.4  Fire Line Notation
-----------------------


**3.4.1**  A counter may display one, two, or three fire lines depending on the weapon mix of the unit.

**3.4.2**  Each fire line represents a distinct weapon class within the unit.

**3.4.3**  A minimum rFP threshold of 2 is required for a weapon class to appear as a separate fire line. Weapon contributions below this threshold are omitted from the counter.

**3.4.4**  Weapon class icons appear to the left of the rFP value on each fire line:

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
     - Special — see Section TBD


3.5  Stacking Limits
--------------------


**3.5.1**  A maximum of 3 combat units may occupy a single hex at any time.

**3.5.2**  Leaders do not count toward the stacking limit.

**3.5.3**  Independently crewed weapon counters (HMG teams, mortar teams, AT gun teams) do not count toward the stacking limit when stacked beneath their parent squad.

**3.5.4**  Weapon counters that have separated from their parent squad count as a combat unit for stacking purposes.

**3.5.5**  Prisoner markers do not count toward the stacking limit.

3.6  Unit Status Markers
------------------------


Small markers are placed on or beside unit counters to track their current state. All markers are removed during the Recovery Phase at the start of each turn.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Marker**
     - **Meaning**
   * - MOVED
     - Unit has used its move action this turn
   * - FIRE 1
     - Unit has used its first fire action this turn
   * - FIRE 2
     - Unit has used its second fire action this turn
   * - FIRE 3
     - Unit has used its third fire action this turn
   * - ASSAULT
     - Unit has used a move-and-fire or fire-and-move action this turn
   * - OPPORTUNITY
     - Unit has used an opportunity fire reaction this turn
   * - SUPPRESSED
     - Unit is suppressed (see Section 10.2)
   * - PINNED
     - Unit is pinned (see Section 10.3)
   * - MOBILE
     - Weapon counter is limbered and moving; cannot fire
   * - GUARD
     - Unit is guarding prisoners; movement and fire restricted
