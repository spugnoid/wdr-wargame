Section 19 — Vehicle Morale, Bail-Out and Capture
=================================================

Vehicle crews were not immune to morale failure. Isolated inside steel boxes, dependent on infantry support, facing weapons that could destroy them at ranges where they could barely see — crew morale was a genuine tactical factor. This section covers vehicle-specific morale triggers, bail-out procedure, and the treatment of abandoned and captured vehicles.

19.1  Vehicle Morale Checks
---------------------------


**19.1.1**  Vehicle morale checks use the same procedure as infantry: roll 1d6 + vehicle Morale vs break threshold. A leader within command radius adds their CMD rating to the roll.

**19.1.2**  Vehicle-specific morale triggers:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Trigger**
     - **Break Threshold**
     - **Notes**
   * - Receives any penetrating hit this turn
     - 7
     - Crew shaken by internal damage
   * - Infantry support eliminated within 2 hexes
     - 6
     - Crew exposed without protection
   * - Adjacent friendly vehicle eliminated
     - 5
     - Witnessing catastrophic kill nearby
   * - Leader vehicle eliminated
     - 6
     - Loss of command
   * - Buttoned up (Pinned) for 2 consecutive turns
     - 6
     - Prolonged isolation and stress


**19.1.3**  Buttoned up isolation: a Pinned (buttoned up) vehicle cannot observe adjacent breaks by friendly vehicles or infantry — the crew cannot see outside. Cascade checks from nearby friendly units breaking do not apply while buttoned up.

**19.1.4**  Vehicle morale check failure produces a Bail-out (see Rule 19.2) rather than a Break or Rout. Vehicles do not rout — they are either fighting or abandoned.

19.2  Bail-Out Procedure
------------------------


**19.2.1**  Bail-out check trigger: during each Recovery Phase, any vehicle that is Suppressed or Pinned must pass a bail-out check.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Vehicle status**
     - **Bail-out threshold**
     - **Notes**
   * - Suppressed
     - 8
     - Crew shaken but vehicle functional
   * - Pinned (buttoned up)
     - 6
     - Isolation and immobility accelerate decision to bail


**19.2.2**  Roll 1d6 + vehicle Morale vs threshold. Leader CMD adds to roll as normal.

**19.2.3**  Success: crew holds. Vehicle status unchanged.

**19.2.4**  Failure: crew bails out.

**19.2.5**  Bail-out procedure on failure:

**19.2.6**  Place an ABANDONED marker on the vehicle counter. The vehicle remains in its hex — it is not removed from the map.

**19.2.7**  Place a CREW counter in the same hex. The CREW counter represents the bailed-out crew.

**19.2.8**  The CREW counter immediately routes using infantry routing rules — moves D3 hexes away from the nearest visible enemy unit. Place ROUTING marker on CREW counter.

**19.2.9**  The CREW counter follows all infantry routing rules (Section 10.6) for subsequent turns including rally attempts.

19.3  Abandoned Vehicles
------------------------


**19.3.1**  An ABANDONED vehicle counter remains in its hex. It has the following states:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **State**
     - **Marker**
     - **Condition**
   * - ABANDONED
     - ABANDONED marker
     - Functional vehicle, no crew — can potentially be crewed
   * - DAMAGED
     - ABANDONED + damage marker
     - MOB or GUN kill vehicle with no crew
   * - DESTROYED
     - Counter removed
     - Catastrophically killed — not recoverable


**19.3.2**  An ABANDONED vehicle provides cover to infantry in the same hex (+2 cover — hull defilade) but is not a combat unit.

**19.3.3**  Enemy units can move through an ABANDONED vehicle hex normally. They may attempt to capture it (see Rule 19.4).

19.4  Vehicle Capture
---------------------


**19.4.1**  An enemy unit in the same hex as or adjacent to an ABANDONED vehicle may attempt capture by spending 1 AP.

**19.4.2**  Vehicle capture requires a CREW counter of the capturing nation — representing trained vehicle crew waiting for a replacement vehicle. Regular infantry cannot crew an unfamiliar vehicle without specialist training.

**19.4.3**  Capture attempt: move the CREW counter into the vehicle hex (costs 1 AP). Roll 1d6 + crew quality modifier vs threshold 5.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - ≥ 5
     - Vehicle operational next turn at reduced effectiveness: Morale -1, -1 to all fire actions
   * - < 5
     - Vehicle not operational this scenario — crew cannot figure out unfamiliar controls in time


**19.4.4**  Special Beutepanzer (captured equipment) units: some scenarios may include dedicated captured-equipment crew counters that can attempt to crew enemy vehicles at only -1 penalty to the roll instead of the standard difficulty. This is scenario-defined.

**19.4.5**  A captured vehicle cannot enter service in the same scenario even if the crewing roll succeeds — the crew needs the remainder of the turn to familiarise with the vehicle. It is available from the following turn onward.

19.5  Campaign Treatment of Captured Vehicles
---------------------------------------------


**19.5.1**  Captured vehicles secured at scenario end go to the CAPTURED zone of the campaign track.

**19.5.2**  Between scenarios, roll 1d6 + capturing force maintenance quality:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1–2
     - Non-operational — vehicle cannot be used (parts unavailable, too damaged to repair quickly)
   * - 3–4
     - Operational — available as replacement asset at Morale -1, fire -1
   * - 5–6
     - Fully operational — enters campaign pool at standard stats


**19.5.3**  Different nations had different abilities to operate captured equipment. Germans were notably effective at pressing captured Soviet vehicles into service (Beutepanzer programme). Soviets used captured German equipment less systematically. This is reflected in the maintenance quality modifier — scenario designer assigns appropriate values.

19.6  Vehicle Experience and Quality
------------------------------------


**19.6.1**  Vehicle crew quality follows the same BTV/EM/MM framework as infantry (Section 1.3 definitions). Quality degrades with replacement crew and builds through combat experience using the same campaign mechanics.

**19.6.2**  Key differences from infantry experience:

**19.6.3**  Crew isolation: buttoned-up crews cannot observe cascading morale failures around them. A Pinned vehicle does not receive cascade checks from adjacent infantry or vehicle breaks — the crew is literally blind to surrounding events.

**19.6.4**  Vehicle condition effect on crew morale: a reliable vehicle counter (scenario-flagged as proven design) adds +1 to all vehicle morale checks. A breakdown-prone vehicle (scenario-flagged) subtracts -1. This represents crew confidence in their equipment — real and historically significant.

**19.6.5**  Loss of infantry support trigger (Rule 19.1.2) has no infantry equivalent. Combined arms doctrine exists specifically because tank crews were vulnerable without infantry screening against close-range AT threats. The game enforces this doctrine mechanically — tanks that advance without infantry face genuine morale risk.

**19.6.6**  Vehicle cascade rule: when a vehicle is eliminated within 2 hexes of another friendly vehicle, the surviving vehicle must make a cascade morale check at threshold 5 ONLY if it is not currently Pinned (buttoned up). A Pinned vehicle's crew cannot see the catastrophic kill outside. This asymmetry between buttoned and unbuttoned vehicles is historically accurate and tactically significant.

19.7  Representative 1943 Vehicle Counters
------------------------------------------


*Hull/Turret AV and own-gun PEN values below are computed by* `counters/armor_calc/` *(Rule 17.2.5) and reflect the current Hull/Turret AV split, not the flat single-facing figures this table originally showed. This is a compact "at a glance" comparison — Front facing, AV-vs-Capped only, one representative range band. For AV-vs-Tungsten, Side/Rear facings, full range-band PEN, and the full Gunnery Table across every crew quality, see* `roster_output.csv`, `gun_curves_output.csv`, *and* `vehicle_fire_thresholds_output.csv` *in that directory. TRAV, M#, MG fire line, and Morale are unrelated to the armour/gunnery redesign and are carried over unchanged from this table's original values; HE rFP is recomputed fresh from each vehicle's actual gun calibre (Rule 18.8.4) since the previous figures included at least one confirmed error (see note below).*

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Vehicle**
     - **Main Gun**
     - **Hull Front AV**
     - **Turret Front AV**
     - **Gun PEN @ 500m**
     - **TRAV**
     - **M#**
     - **HE**
     - **MG**
     - **Morale**
   * - Panzer IV Ausf H
     - 75mm KwK40 L48
     - 64.9
     - 78.9
     - 119.6
     - 3
     - M3
     - 4
     - 4 ⬡3 -1
     - 6
   * - Panzer III Ausf M
     - 50mm KwK39 L60
     - 51.4
     - 57.8
     - 69.0
     - 3
     - M3
     - 3
     - 4 ⬡3 -1
     - 6
   * - Tiger I Ausf E
     - 88mm KwK36
     - 102.0
     - 143.0
     - 137.4
     - 2
     - M2
     - 4
     - 4 ⬡3 -1
     - 6
   * - StuG III Ausf G
     - 75mm KwK40 L48
     - 87.1
     - — (casemate)
     - 119.6
     - 0
     - M3
     - 4
     - 3 ⬡3 -1
     - 6
   * - T-34 Model 1943
     - 76mm F-34
     - 93.7
     - 55.8
     - 72.2
     - 3
     - M3
     - 4
     - 3 ⬡3 -1
     - 5
   * - T-34/85 (late 1943)
     - 85mm D-5T
     - 93.7
     - 146.0
     - 119.8
     - 3
     - M3
     - 4
     - 3 ⬡3 -1
     - 5
   * - KV-1S
     - 76mm ZIS-5 (modelled on F-34 curve — Rule 18.12(f))
     - 85.2
     - 129.1
     - 72.2
     - 1
     - M2
     - 4
     - 3 ⬡3 -1
     - 5
   * - SU-85
     - 85mm D-5S (modelled on D-5T curve — Rule 18.12(f))
     - 75.5
     - — (casemate)
     - 119.8
     - 0
     - M3
     - 4
     - 3 ⬡3 -1
     - 5
   * - Sherman M4A1 (75mm)
     - 75mm M3 L31
     - 76.7
     - 89.0
     - 77.9
     - 3
     - M3
     - 4
     - 4 ⬡3 -1
     - 6
   * - Sherman M4A3 (76mm)
     - 76mm M1
     - 115.5
     - 93.6
     - 117.5
     - 3
     - M3
     - 4
     - 4 ⬡3 -1
     - 6
   * - Sdkfz 251 half-track
     - — (MG only, no main gun)
     - 14.3
     - — (no turret)
     - —
     - —
     - M4
     - —
     - 3 ⬡3 -1
     - 5
   * - T-70 light tank
     - 45mm 20K L46 (APBC)
     - 44.0
     - 30.5
     - 59.3
     - 3
     - M4
     - 2
     - 3 ⬡3 -1
     - 5

*HE corrections: Tiger I Ausf E's 88mm gun gives HE rFP = ROUND(88/20) = 4 by Rule 18.8.4's own stated formula and worked example ("88mm = 4") — this table previously printed 5, a plain arithmetic error unrelated to the armour redesign, now fixed. Panzer III Ausf M's 50mm gun gives exactly 2.5, a genuine rounding-convention tie; resolved as 3 (round-half-up) for consistency with this project's established convention elsewhere (Excel-style rounding, not Python's round-half-to-even) — previously printed 2, flagged here as a judgement call rather than a silent change.*

*Known gap: Panther Ausf G's real, sourced Hull Front AV (229.1) / Turret Front AV (249.2) and own-gun PEN @ 500m (158.6mm, 75mm KwK42 L70) are already in* `armor_calc` *'s roster output, but this vehicle was never added to this table. Deliberately not added here either — TRAV, M#, and MG fire line for Panther would need real game-design judgement (not just tool output) to set consistently with the rest of this table, and inventing them here would be a guess dressed up as data. Worth a real design pass, not a quiet addition.*

*For the current, correctly-resolved Sherman 76mm vs. Tiger I and T-34/85 vs. Tiger I matchups at 400 yards (both were "contested"/"marginal" under the old system for reasons the new Hull/Turret split now makes explicit), see Rule 18.12(d) — the old flat "PEN value revised" footnote this table previously carried referred to a dice-notation AP PEN format that no longer exists under the current resolution model.*
