Appendix G — Rules Complexity Tiers
====================================

This appendix sorts the rules into three tiers — **Basic**, **Standard**, and **Advanced** — so a group can choose how much of the system to bring to the table without hunting through 24 sections to work that out for themselves. Nothing here changes what any rule says; it only labels how essential each part is to a complete, satisfying game.

G.1  What Each Tier Means
--------------------------

**Basic** is everything needed to play a complete game to a fair, historically plausible result: the resolution engine (fire combat, close assault, morale), the action economy (AP/RP, leaders, the Regular/Assault split), core unit and terrain rules, and enough scenario structure to set one up. A group playing Basic rules only is playing the real game, not a simplified preview of it — nothing in Basic is a placeholder for something "more real" in a higher tier.

**Standard** adds the tactical depth and historical texture most groups will want once Basic rules feel comfortable: specialist unit types (snipers, engineers), support weapons (mortars/smoke), vehicles and their own combat system, the hidden-information system's core (blind markers, basic spotting), and prisoner handling. This is the tier most ongoing groups will settle into as their normal way of playing — richer than Basic, not yet chasing edge-case simulation fidelity.

**Advanced** is optional chrome: modules that add real simulation detail or historical nuance at a real cost in table overhead, meant to be adopted individually, not as a block. Every Advanced-tier rule that lives inside an otherwise Basic or Standard section is explicitly labeled **"(Optional Rule)"** in its own header, with an *"If this module is in use for the scenario"* line marking exactly where it begins — nothing at Advanced tier is silently assumed. A scenario (or a whole campaign) states in its own parameters which Advanced modules, if any, are in play; players never have to guess.

.. container:: rule-guide

   **Why:** Naming three tiers up front — rather than just scattering "(Optional Rule)" labels through the text — gives a new group an actual on-ramp: play Basic, add Standard once it clicks, and treat every Advanced module as a separate, independent decision rather than an all-or-nothing "full rules" switch the way some tactical wargames present their own advanced content.

   **Example:** A group's first game uses Basic rules only — no vehicles, no snipers, no hidden units — and plays a complete, fair scenario. Their second game adds Standard-tier vehicles and mortars because the scenario calls for combined arms. Their fifth game adds the Weapon Malfunction module (Rule 8.12) because they specifically want that texture, while still skipping Night Combat (Section 23) entirely because no scenario they're playing needs it.

G.2  Tier by Section
----------------------

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Section**
     - **Tier**
     - **Notes**
   * - 1 — Introduction and Components
     - Basic
     -
   * - 2 — Game Scale and Conventions
     - Basic
     -
   * - 3 — Counters and Units
     - Basic
     -
   * - 4 — Terrain
     - Basic
     - Elevation/LOS core (4.4a.1–4.4a.4) is Basic; grazing fire (4.4a.5) is Standard
   * - 5 — Turn Structure
     - Basic
     -
   * - 6 — Actions and Reactions
     - Basic
     - Includes F#-capable weapons (Rule 6.6) — central to how MG counters already work, not an add-on
   * - 7 — Movement
     - Basic
     - Careless Movement (Rule 7.4) is Standard — a real tactical option, not required to play
   * - 8 — Fire Combat
     - Basic
     - Weapon Malfunction (8.12) and Pre-Registered Defensive Fire (8.13) are Advanced (Optional Rule)
   * - 9 — Close Assault
     - Basic
     - Close Assault Against a Vehicle (9.1/18.9a) is Standard (needs vehicles); Mass Assault (9.8a) is Advanced (Optional Rule)
   * - 10 — Unit Status
     - Basic
     -
   * - 11 — Prisoners and Surrender
     - Standard
     -
   * - 12 — Leaders
     - Basic
     - CMD feeds the AP formula directly (Rule 5.3.3) — not a bolt-on system
   * - 13 — Campaign Rules
     - Advanced
     - An entire optional layer for linked-scenario play; irrelevant to a single scenario
   * - 14 — Hidden Information System
     - Standard / Advanced
     - Blind markers and basic spotting (14.1–14.3, 14.9) are Standard; Dummy markers, CONTACT aging, and FIXED-unit ambushes (14.4, 14.6–14.8, 14.7) are Advanced
   * - 15 — Morale, Break, and Rout
     - Basic
     -
   * - 16 — Mortars and Smoke
     - Standard
     - Heavy Mortar/Artillery vs. Top Armour (16.7.8a) is Advanced (Optional Rule)
   * - 17 — Vehicles: Counter Design and Movement
     - Standard
     - Bypass Movement (17.6a), Top Armour (17.2a), and Hull-Down Position (17.6b) are Advanced (Optional Rule)
   * - 18 — Vehicle Combat Resolution
     - Standard
     - Shatter Gap (18.2a), Schürzen (18.2b), Sidehill Exposure (18.2c), and per-vehicle Hit Location (18.6a) are Advanced — each already scoped as optional or partial-coverage in its own rule text
   * - 19 — Vehicle Morale, Bailout, and Capture
     - Standard
     -
   * - 20 — Snipers
     - Standard
     -
   * - 21 — Engineers and Assault Specialists
     - Standard
     - Basic Entrenchment (21.7a) is available to any unit at Standard tier — it does not require the rest of Section 21's specialist capabilities
   * - 22 — Scenario Design Guidelines
     - Basic
     - Needed to set up any scenario at all, including a Basic-only one
   * - 23 — Night Combat
     - Advanced
     - An entire optional scenario-condition module
   * - 24 — Weather
     - Advanced
     - An entire optional scenario-condition module


**G.2.1**  A scenario's own parameters (Rule 22.x) state which tier it assumes and which specific Advanced modules, if any, are active — a scenario designer is free to write a Basic-only scenario, a Standard scenario with two specific Advanced modules bolted on, or anything between.

.. container:: rule-guide

   **Why:** Keeps the tier decision where every other scenario-specific decision already lives — the scenario's own parameter block — rather than requiring a separate, document-wide "ruleset version" a group has to agree on before they can even pick a scenario.

   **Example:** A scenario's parameter block might read "Standard tier; Advanced modules in use: Weapon Malfunction (8.12), Night Combat (Section 23)" — telling both players exactly what's live before a single counter is placed, with every other Advanced module (Bypass Movement, Mass Assault, Weather, the full Campaign layer) understood to be off.

G.3  The Complete List of Advanced (Optional Rule) Modules
---------------------------------------------------------------

Every module below carries its own "(Optional Rule)" header and an "If this module is in use for the scenario" line at the point it begins in the main text — this list exists only so a group can see the full menu in one place.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Module**
     - **Rule**
     - **What it adds**
   * - Shatter Gap
     - 18.2a
     - A kinetic round can shatter and fail to penetrate despite favorable numbers
   * - Schürzen
     - 18.2b
     - Standoff skirt armour defeats HEAT specifically, never kinetic rounds
   * - Weapon Malfunction
     - 8.12
     - Automatic weapons can jam under fire and need field repair
   * - Pre-Registered Defensive Fire
     - 8.13
     - A stationary weapon can pre-range up to two hexes for a real accuracy bonus
   * - Bypass Movement
     - 17.6a
     - A vehicle can skirt a hex's obstacles instead of driving through them
   * - Mass Assault
     - 9.8a
     - Successive close assaults against the same hex wear the defender down
   * - Top Armour
     - 17.2a
     - Prints a Hull/Turret Top AV where sourced, for use by Sidehill Exposure below
   * - Hull-Down Position
     - 17.6b
     - A stationary vehicle at a crest hexside makes its Hull untargetable from the low side
   * - Sidehill Exposure
     - 18.2c
     - A vehicle broadside across a slope can be hit on its weaker Side or Top AV, whichever is lower
   * - Heavy Mortar/Artillery vs. Top Armour
     - 16.7.8a
     - 120mm-class+ HE has a small chance to mobility-kill a closed AFV via its engine deck, never a full penetration
   * - Night Combat
     - Section 23
     - Ambient visibility, illumination, and their knock-on effects across other sections
   * - Weather
     - Section 24
     - Rain/Mud, Snow, and Fog as fixed scenario conditions
   * - Campaign Rules
     - Section 13
     - Linked scenarios, between-scenario recovery, unit experience and promotion


.. container:: rule-guide

   **Why:** A single menu of every optional module, cross-referenced back to its actual rule, so a group deciding "what should our house style include" can scan one table instead of searching the whole document for "(Optional Rule)" headers.

   **Example:** A group that wants historical grit without extra bookkeeping might adopt Weapon Malfunction and Shatter Gap but skip Bypass Movement and Mass Assault entirely — every module on this list is independent of every other one, and a scenario can mix and match freely.
