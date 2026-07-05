Section 20 — Snipers
====================

Snipers in World War II were not the Hollywood archetype of a lone marksman winning firefights. They were precision instruments used to decapitate enemy leadership, suppress crew weapon operators, and create psychological pressure across entire areas of ground. The knowledge that a sniper was present changed how everyone moved — even people who had not been shot at.

Sniper rules differ from standard infantry fire in three fundamental ways: they target specific individuals rather than hexes, they remain hidden after firing, and they impose psychological suppression on areas rather than individual targets.

20.1  Sniper Counter Design
---------------------------


**20.1.1**  Sniper counters use the triangle symbol (△) and the precision weapon class icon (╌○) on their fire line.

**20.1.2**  Standard sniper counter stats:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Stat**
     - **Value**
     - **Notes**
   * - M#
     - M1
     - Careful movement only — snipers do not run
   * - F#
     - F1
     - One shot per turn — patience and precision
   * - G#
     - G0
     - Snipers do not close assault
   * - Fire line
     - ╌○ 3 ⬡6 -1
     - Low rFP — precision not volume
   * - AMO
     - 4 base + secret bonus
     - Limited shots per scenario
   * - Morale
     - 7 (veteran) or 6 (regular)
     - Snipers are selected troops
   * - Defence
     - 4
     - Small team, hard to spot but lightly equipped


**20.1.3**  Sniper ammunition follows the same secret bonus system as mortars (Rule 16.3). Base AMO is 4. At scenario setup the owning player secretly rolls 1d6-1 and adds to base AMO. Past base AMO, roll the extended ammunition table each shot.

20.2  Deliberate Targeting
--------------------------


**20.2.1**  Standard fire resolution targets a hex — all units in the hex are at risk and the attacker cannot control which unit takes the casualty result.

**20.2.2**  Snipers may declare deliberate targeting — naming a specific unit or unit type as the target before rolling. A casualty result or better applies to that specific unit rather than the hex generally.

**20.2.3**  Deliberate targeting is only available against valid priority targets. Snipers historically focused on high-value targets whose loss degraded enemy effectiveness:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Priority**
     - **Valid deliberate targets**
   * - 1 (highest)
     - Leaders — any leader counter
   * - 2
     - Crew weapon operators — HMG teams, mortar teams, AT gun crews
   * - 3
     - Forward observers calling fire missions
   * - 4
     - Vehicle commanders (unbuttoned vehicle — not Pinned)
   * - 5
     - Radio operators (scenario-defined special unit)


**20.2.4**  Snipers may not use deliberate targeting against regular rifle squads, SMG squads, or LMG teams — these units are too dispersed for a single aimed shot to reliably identify and engage a single man.

**20.2.5**  If a deliberate targeting shot produces Suppressed or Pinned — the round was close but not a hit — the result applies to the hex normally rather than the specific target.

**20.2.6**  Long range cap exemption: when deliberate targeting is declared, the long range cap (Rule 8.7) does not apply. Full result thresholds are used regardless of effective rFP. See Rule 8.7.4.

    *See also: Rule 8.7.4 (Long Range Cap exemption) and Rule 12.9.1a (Leaders — casualty allocation exception) both depend on this rule.*

20.3  Sniper Concealment and Detection
--------------------------------------


**20.3.1**  Snipers begin each scenario as FIXED units (Section 14.7) or HIDDEN — they are never placed openly on the map at scenario start.

**20.3.2**  A sniper that fires is not automatically revealed. Instead the opponent makes a sniper detection roll:

**20.3.3**  Detection roll: roll 1d6 + all applicable OBS modifiers vs sniper CON value.

**20.3.4**  Sniper base CON = 5. Modify as follows:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **CON modifier**
   * - Stationary, not fired this turn
     - +2
   * - Dense woods or entrenchment
     - +3
   * - Light woods or building
     - +2
   * - Open ground
     - +0
   * - Fired this turn (normal fire)
     - -3
   * - Fired this turn (deliberate target)
     - -2 (more controlled shot, less signature)
   * - Night scenario
     - +3
   * - Fired from same position twice this scenario
     - -2 (position partially known)


**20.3.5**  Detection result:

**20.3.6**  Roll meets or exceeds CON: sniper revealed — blind marker removed, counter placed on map at firing position.

**20.3.7**  Roll below CON: sniper not detected — place a CONTACT marker (sniper type, crosshair symbol) at the firing position. Sniper remains hidden.

20.4  Sniper Repositioning
--------------------------


**20.4.1**  After firing, before the detection roll is made, a sniper may immediately reposition up to M# hexes as a free action. This represents moving to a new position before the opponent can identify the firing point.

**20.4.2**  The detection roll is made against the sniper's new position CON value, not the firing position.

**20.4.3**  If the sniper repositions and is not detected, the CONTACT marker is placed at the original firing position — the opponent knows approximately where the shot came from but the sniper has moved.

**20.4.4**  A sniper that does not reposition after firing uses the firing position CON for the detection roll.

20.5  Psychological Area Suppression
------------------------------------


**20.5.1**  When a sniper CONTACT marker (crosshair) exists anywhere on the map, all friendly units within 6 hexes of that marker suffer:

**20.5.2**  Movement reduction: all movement at M# -1 (minimum 1).

**20.5.3**  Careless movement unavailable: no unit may declare careless movement while a sniper CONTACT marker is within 6 hexes.

**20.5.4**  This represents the historical reality that the mere knowledge of a sniper's presence changed how entire units moved — even soldiers who had not been fired at kept low, moved quickly between cover, and avoided open ground.

**20.5.5**  The psychological suppression applies from the moment the CONTACT marker is placed and persists until the marker is removed (sniper revealed, CONTACT marker ages to COLD and is removed, or sniper is eliminated).

20.6  Counter-Sniper Procedures
-------------------------------


**20.6.1**  A revealed sniper is engaged using standard fire resolution. However snipers in cover with high CON are very difficult to neutralise through direct fire alone.

**20.6.2**  Effective counter-sniper methods:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Method**
     - **Procedure**
     - **Effectiveness**
   * - Mortar or artillery fire
     - Area fire on suspected position — no LOS needed
     - Most effective — forces sniper to move or be destroyed
   * - Counter-sniper
     - Opposing sniper declares deliberate target against revealed sniper
     - Precise — one aimed shot
   * - Infantry assault
     - Standard close assault into sniper hex
     - Certain but costly if sniper has support
   * - Direct fire
     - Standard fire resolution vs revealed sniper
     - Possible but cover usually limits results


**20.6.3**  Counter-sniper duel: when both sides have active snipers within range of each other, either may declare deliberate targeting against the opposing sniper. The deliberate targeting rules apply normally. A Casualty result eliminates the opposing sniper. A Pinned result forces the opposing sniper to reposition (free reposition of up to M# hexes, no AP cost).

20.7  Representative 1943 Sniper Counters
-----------------------------------------


.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit**
     - **Fire line**
     - **AMO**
     - **Morale**
     - **Defence**
     - **Notes**
   * - German sniper team (Scharfschütze) — veteran
     - ╌○ 3 ⬡6 -1
     - 4
     - 7
     - 4
     - Scoped Kar98k or G43
   * - Soviet sniper (veteran)
     - ╌○ 3 ⬡6 -1
     - 4
     - 7
     - 4
     - Scoped Mosin-Nagant — Soviet programme produced many skilled snipers
   * - Soviet sniper (regular)
     - ╌○ 3 ⬡6 -1
     - 4
     - 6
     - 4
     - Lower morale reflects variable programme quality
   * - British sniper (veteran)
     - ╌○ 3 ⬡6 -1
     - 4
     - 7
     - 4
     - Scoped No.4 Mk I(T)
   * - US sniper (regular)
     - ╌○ 3 ⬡6 -1
     - 4
     - 6
     - 4
     - Scoped M1903A4 Springfield


*NOTE: All nations use identical fire line values — sniper effectiveness at this scale is determined more by position, patience, and target selection than by weapon differences. Quality differentials are encoded in Morale values and the AMO secret bonus. A veteran sniper with Morale 7 recovers from suppression automatically and passes detection checks more reliably.*
