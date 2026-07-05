Section 14 — Hidden Information System
======================================

With Deepest Regret... uses a physical hidden information system to model the fog of war. Units may be in one of three visibility states. The system uses blind markers on the map, a covered chart beside the map, and serialised markers to maintain information integrity without a referee.

14.1  Visibility States
-----------------------


**14.1.1**  Every unit is in one of three visibility states at all times:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **State**
     - **Map Representation**
     - **Chart**
     - **Opponent Knows**
   * - VISIBLE
     - Unit counter placed openly on map
     - Not on chart
     - Unit type, strength, position
   * - HIDDEN
     - Blind marker on map at unit position
     - Counter in covered slot
     - Approximate position, size category only
   * - FIXED
     - No map representation until activated
     - Position on record sheet
     - Nothing — unit not yet on map


14.2  The Hidden Information Chart
----------------------------------


**14.2.1**  Each player has a hidden information chart with numbered slots beside the map. Each slot has a physical cover — a cup, opaque token, or small box.

**14.2.2**  When a unit goes HIDDEN, its counter is placed in a numbered slot on the chart. The cover is placed over the slot. A blind marker with the matching number is placed on the map.

**14.2.3**  Covered slots may not be touched by either player during play except when the rules require revelation. Physical integrity is maintained by the cover, not by trust.

**14.2.4**  When a unit is revealed, its cover is removed, the counter is lifted from the chart and placed on the map, and the blind marker is removed.

14.3  Blind Markers
-------------------


**14.3.1**  Blind markers come in three sizes matching the actual stack footprint of the unit they represent:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Marker Size**
     - **Symbol**
     - **Represents**
   * - Single
     - One dot
     - 1 combat unit
   * - Small stack
     - Two dots
     - 2–3 units
   * - Large stack
     - Three dots
     - 4+ units


**14.3.2**  The owning player must use the correct size marker for the actual stack. A single unit may not hide under a large stack marker.

**14.3.3**  Blind markers show nation colour but no unit type, quality, or stats.

14.4  Dummy Markers
-------------------


**14.4.1**  Dummy markers are blank chart slots with covers — no unit counter underneath. They are physically identical to real blind markers.

**14.4.2**  Dummies must match the size category of the real unit they were spawned from. A single unit spawning dummies produces single-size dummies only.

**14.4.3**  When a spot roll targets a dummy and succeeds, the owning player announces dummy. The dummy marker is removed from the map. The opponent may verify by uncovering the corresponding slot — it is empty.

**14.4.4**  Dummies may be moved independently at a cost of 1 AP per dummy per activation. When the real unit moves during an activation, all dummies in its group may move for free during the same activation.

**14.4.5**  Dummies must follow plausible movement routes — terrain movement costs apply, impassable terrain cannot be crossed, movement cannot exceed the real unit's M# per impulse.

14.5  Going Hidden
------------------


**14.5.1**  A VISIBLE unit may go hidden by spending 1 AP. The unit must be in terrain with cover modifier +2 or higher, or have no enemy unit with LOS to its hex.

**14.5.2**  Going hidden procedure:

**14.5.3**  Place the unit counter in a numbered chart slot and cover it. Place the correct size blind marker at the unit's current map position.

**14.5.4**  Immediately receive a free hidden impulse (see Rule 14.6) before the reaction window opens.

14.6  Free Hidden Impulse
-------------------------


**14.6.1**  When a unit goes hidden — either by spending 1 AP or as a free action after firing from a FIXED position — it immediately receives a free hidden impulse outside the normal AP economy.

**14.6.2**  During the free hidden impulse the owning player, in order:

**14.6.3**  Moves the real blind marker up to M# hexes along any plausible route following terrain movement costs.

**14.6.4**  Places 2 dummy markers at the unit's last spotted position or adjacent hexes.

**14.6.5**  May move each dummy marker up to M# hexes along any plausible route.

**14.6.6**  After the free hidden impulse, the reaction window opens. The opponent may spend RP to attempt spot rolls against any of the three markers.

**14.6.7**  The free hidden impulse represents the brief window of confusion when a unit disappears from view and the opponent cannot determine which way it went.

14.7  FIXED Units
-----------------


**14.7.1**  FIXED units are units assigned to prepared positions before the scenario begins. They have no counter on the map and no blind marker — their position is committed to a scenario record sheet before play starts. Both players must agree that positions are recorded before the scenario begins.

**14.7.2**  A FIXED unit that moves for the first time transitions to HIDDEN status. Its counter is placed on the chart under cover, a blind marker is placed at its recorded position, and it receives a free hidden impulse to spawn dummies and reposition.

**14.7.3**  A FIXED unit that fires without moving may choose one of two options:

**14.7.4**  Option A — Sit tight: the unit is revealed at its recorded position. No dummies spawned. It may go hidden on a subsequent activation by spending 1 AP.

**14.7.5**  Option B — Fire and disperse: after firing resolves, the unit goes hidden as a free action (no AP cost). It receives a free hidden impulse — moves blind marker up to M# hexes and spawns 2 dummies at or adjacent to the firing position. This option may only be taken once per scenario from a FIXED position.

**14.7.6**  The surprise of the first FIXED fire applies a +2 rFP bonus to that fire action, representing the target's unpreparedness. This bonus applies only to the first fire from the FIXED position.

14.8  Contact Markers
---------------------


**14.8.1**  When a spotted unit successfully goes hidden during play, a CONTACT marker is placed at the hex where it was last seen.

**14.8.2**  CONTACT markers advance through three states, one step per Recovery Phase:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **State**
     - **Appearance**
     - **Age**
     - **Meaning**
   * - FRESH
     - Bright marker, solid symbol
     - Current turn
     - Recent intelligence — unit was here this turn
   * - RECENT
     - Dimmed or flipped marker
     - 1 turn old
     - Unit likely has moved from this position
   * - COLD
     - Faded or different colour
     - 2 turns old
     - Outdated — removed end of this Recovery Phase


**14.8.3**  COLD markers are removed at the end of the Recovery Phase in which they become cold.

**14.8.4**  CONTACT markers are not combat units. They have no game effect beyond conveying information age.

14.9  Spotting
--------------


**14.9.1**  Spotting is the process of identifying a hidden or fixed unit. A successful spot roll reveals the unit — its blind marker is removed and its counter is placed on the map.

**14.9.2**  Automatic spotting — no roll required:

**14.9.3**  A unit that fires is automatically revealed at its firing position. No spot roll needed.

**14.9.4**  A unit whose blind marker is entered by an enemy unit is automatically revealed.

**14.9.5**  Spot roll triggers — roll required:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Trigger**
     - **RP Cost**
     - **Notes**
   * - Enemy unit moves carelessly into LOS
     - 0 — free
     - Noise and visibility — no RP required
   * - Opponent spends RP to spot
     - 1
     - Deliberate observation attempt
   * - Unit takes Spot Action
     - 0 — is the action
     - Dedicated observation, +3 OBS bonus
   * - Artillery or mortar impact within 2 hexes of hidden unit
     - 0 — free
     - Blast briefly reveals nearby units


**14.9.6**  Spot roll procedure: roll 1d6, add OBS modifiers, subtract CON modifiers. If result is 0 or greater, the target is spotted.

**14.9.7**  Concealment modifiers (CON) — defender:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **CON Modifier**
   * - Open ground
     - 0
   * - Crops / tall grass
     - +1
   * - Light woods
     - +2
   * - Dense woods
     - +3
   * - Building
     - +2
   * - Entrenchment
     - +3
   * - Stationary, not fired this turn
     - +2
   * - Careful movement (normal move)
     - +0
   * - Careless movement
     - -2
   * - Moving through dense woods or rubble
     - -1 (unavoidable noise)
   * - Fired this turn
     - -3
   * - Suppressed or pinned
     - -1
   * - Night scenario
     - +3
   * - Smoke per intervening hex
     - +2


**14.9.8**  Observation modifiers (OBS) — spotter:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Condition**
     - **OBS Modifier**
   * - Leader present in hex
     - +leader OBS rating
   * - Elevated 1 level above target
     - +1
   * - Elevated 2+ levels above target
     - +2
   * - Binoculars equipment marker
     - +2
   * - Spotter moving this turn
     - -2
   * - Spotter suppressed
     - -2
   * - Dedicated Spot Action this turn
     - +3
   * - Active firefight within 5 hexes this turn
     - Sound spotting impossible — noise overwhelms


14.10  Spot Action
------------------


**14.10.1**  A unit may spend its entire activation on a Spot Action — it takes no other action this impulse.

**14.10.2**  A unit taking a Spot Action gains +3 OBS for all spot rolls this turn.

**14.10.3**  The Spot Action represents deliberate, methodical observation — scanning terrain, watching for movement, listening. Leaders and scouts are particularly effective when taking this action.

**14.10.4**  A unit taking a Spot Action may attempt spot rolls against all hidden markers within its LOS range at no RP cost. Each marker is rolled against separately.

14.11  Sound Spotting
---------------------


**14.11.1**  Sound spotting is only available when no unit has fired within 5 hexes this turn. Active firefight noise drowns out movement sounds entirely.

**14.11.2**  When sound spotting is available, the following CON penalties apply in addition to normal modifiers:

**14.11.3**  Units moving through dense woods or rubble: -1 CON (unavoidable noise — already included in the CON table above).

**14.11.4**  Units moving carelessly: -2 CON (already included — the careless movement penalty covers both visual and audio signature).

**14.11.5**  Night scenarios: sound becomes the primary detection method. Visual spot range is reduced to 1-2 hexes maximum. All sound-based CON penalties are doubled. Full night rules are a separate design task — this rule establishes the framework.

14.12  FIXED Unit Transition Summary
------------------------------------


.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Event**
     - **Transition**
     - **Dummies Spawned**
     - **AP Cost**
     - **Surprise Bonus**
   * - FIXED unit moves
     - FIXED → HIDDEN
     - Yes — free hidden impulse
     - Normal move AP
     - No
   * - FIXED unit fires, sits tight
     - FIXED → VISIBLE
     - No
     - 0
     - +2 rFP first fire only
   * - FIXED unit fires, disperses
     - FIXED → HIDDEN
     - Yes — free disperse
     - 0 (free)
     - +2 rFP first fire only
   * - VISIBLE unit goes hidden
     - VISIBLE → HIDDEN
     - Yes — free hidden impulse
     - 1 AP
     - No
   * - HIDDEN unit revealed by spot
     - HIDDEN → VISIBLE
     - No
     - N/A
     - No
   * - HIDDEN unit fires
     - HIDDEN → VISIBLE
     - No unless rehides
     - 0 to reveal; 1 AP to rehide
     - No
