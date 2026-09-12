Appendix H — Consolidated Unit and Vehicle Roster
====================================================

*This appendix is generated directly from this project's own calculation
tools, in* ``counters/infantry_calc/`` *and* ``counters/armor_calc/``\ *, and
is never hand-edited. Regenerate it with the command* ``PYTHONPATH=counters
python3 counters/generate_roster_appendix.py`` *after re-running either
pipeline, and commit the regenerated file alongside whatever data change
produced it. Full sourcing, confidence notes, and open questions for any
given row live in the underlying* ``data`` *CSV files and the*
``counters/toe/`` *research documents they cite — this appendix intentionally
omits that detail to stay scannable as a single reference table.*

*Vehicle Gunnery Tables (Rule 18.1a) are not included here: a Gunnery Table
depends on the firing vehicle's own Crew Quality (Rule 17.3.6), which is
derived from a vehicle's printed Morale at counter-design time — a
scenario-specific choice this roster does not currently track as structured
data for every vehicle. A scenario's own parameter block states each side's
vehicle crew qualities; look up that gun's full Gunnery Table in the file*
``vehicle_fire_thresholds_output.csv`` *once the crew quality is chosen.*

H.1  Infantry and Weapon Team Roster
----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Unit**
     - **Nation**
     - **Year**
     - **Quality**
     - **Face**
     - **Fire line 1**
     - **Fire line 2**
     - **Fire line 3**
     - **Def**
     - **Mor**
     - **M#**
     - **F#**
     - **G#**
   * - Grenadier Squad
     - Germany
     - 1943.3
     - regular
     - F
     - ─● 7 ⬡4 -1
     - ╌ 3 ⬡5 -1
     - omit (rFP too low)
     - 8
     - 5
     - M2
     - F1
     - G3
   * - Grenadier Squad (reduced)
     - Germany
     - 1943.3
     - regular
     - R
     - ╌ 2 ⬡5 -1
     - —
     - —
     - 6
     - 5
     - M2
     - F1
     - G2
   * - Panzergrenadier Squad
     - Germany
     - 1943.3
     - veteran
     - F
     - ─● 11 ⬡2 -1
     - omit (rFP too low)
     - ≡ 2 ⬡3 -1
     - 9
     - 6
     - M2
     - F1
     - G4
   * - Panzergrenadier Squad (reduced)
     - Germany
     - 1943.3
     - veteran
     - R
     - ╌ 3 ⬡5 -1
     - —
     - —
     - 7
     - 6
     - M2
     - F1
     - G3
   * - MG42 HMG Team
     - Germany
     - 1943.3
     - regular
     - F
     - ═● 9 ⬡6 -1
     - —
     - —
     - 5
     - 5
     - M0
     - F3
     - G1
   * - MG42 HMG Team (reduced crew)
     - Germany
     - 1943.3
     - regular
     - R
     - ═● 8 ⬡6 -1
     - —
     - —
     - 3
     - 5
     - M0
     - F3
     - G1
   * - Guards Rifle Squad
     - Soviet Union
     - 1943.3
     - veteran
     - F
     - ─● 8 ⬡3 -1
     - ╌ 3 ⬡4 -1
     - ≡ 4 ⬡1 -1
     - 8
     - 6
     - M2
     - F1
     - G3
   * - Guards Rifle Squad (reduced)
     - Soviet Union
     - 1943.3
     - veteran
     - R
     - omit (rFP too low)
     - —
     - —
     - 6
     - 6
     - M2
     - F1
     - G2
   * - Rifle Squad (Pattern A)
     - Soviet Union
     - 1943.3
     - regular
     - F
     - ─● 7 ⬡3 -1
     - omit (rFP too low)
     - ≡ 3 ⬡2 -1
     - 8
     - 5
     - M2
     - F1
     - G3
   * - Rifle Squad (Pattern A) (reduced)
     - Soviet Union
     - 1943.3
     - regular
     - R
     - omit (rFP too low)
     - —
     - —
     - 6
     - 5
     - M2
     - F1
     - G2
   * - Rifle Squad (Pattern B)
     - Soviet Union
     - 1943.3
     - regular
     - F
     - ─● 9 ⬡3 -1
     - omit (rFP too low)
     - ≡ 3 ⬡2 -1
     - 8
     - 5
     - M2
     - F1
     - G3
   * - Rifle Squad (Pattern B) (reduced)
     - Soviet Union
     - 1943.3
     - regular
     - R
     - omit (rFP too low)
     - —
     - —
     - 6
     - 5
     - M2
     - F1
     - G2
   * - DP-28 LMG Team
     - Soviet Union
     - 1943.3
     - regular
     - F
     - ─● 7 ⬡3 -1
     - —
     - —
     - 5
     - 5
     - M0
     - F2
     - G2
   * - DP-28 LMG Team (reduced crew)
     - Soviet Union
     - 1943.3
     - regular
     - R
     - ─● 5 ⬡3 -1
     - —
     - —
     - 3
     - 5
     - M0
     - F2
     - G1
   * - Rifle Squad
     - United States
     - 1943.3
     - regular
     - F
     - ─● 5 ⬡3 -1
     - ╌ 8 ⬡2 -1
     - omit (rFP too low)
     - 9
     - 5
     - M2
     - F1
     - G3
   * - Rifle Squad (reduced)
     - United States
     - 1943.3
     - regular
     - R
     - ╌ 6 ⬡2 -1
     - —
     - —
     - 7
     - 5
     - M2
     - F1
     - G2
   * - Rifle Section
     - United Kingdom
     - 1943.3
     - regular
     - F
     - ─● 4 ⬡4 -1
     - ╌ 3 ⬡5 -1
     - omit (rFP too low)
     - 8
     - 5
     - M2
     - F1
     - G3
   * - Rifle Section (reduced)
     - United Kingdom
     - 1943.3
     - regular
     - R
     - ╌ 2 ⬡5 -1
     - —
     - —
     - 6
     - 5
     - M2
     - F1
     - G2
   * - Rifle Squad
     - Japan
     - 1943.3
     - regular
     - F
     - ─● 4 ⬡6 -1
     - ╌ 3 ⬡4 -1
     - —
     - 10
     - 5
     - M2
     - F1
     - G3
   * - Rifle Squad (reduced)
     - Japan
     - 1943.3
     - regular
     - R
     - omit (rFP too low)
     - —
     - —
     - 8
     - 5
     - M2
     - F1
     - G2
   * - Light Machine Gun Squad
     - United States
     - 1943.3
     - regular
     - F
     - ═● 6 ⬡6 -1
     - —
     - —
     - 6
     - 5
     - M0
     - F3
     - G1
   * - Light Machine Gun Squad (reduced crew)
     - United States
     - 1943.3
     - regular
     - R
     - ═● 4 ⬡6 -1
     - —
     - —
     - 4
     - 5
     - M0
     - F3
     - G1
   * - PaK 40 Anti-tank Gun Team
     - Germany
     - 1943.3
     - regular
     - F
     - —
     - —
     - —
     - 6
     - 5
     - M0
     - F2
     - G1
   * - 6pdr Anti-tank Gun Team
     - United Kingdom
     - 1943.3
     - regular
     - F
     - —
     - —
     - —
     - 6
     - 5
     - M0
     - F2
     - G1
   * - 45mm Anti-tank Gun Team
     - Soviet Union
     - 1943.3
     - regular
     - F
     - —
     - —
     - —
     - 6
     - 5
     - M0
     - F2
     - G1
   * - 57mm Anti-tank Gun Team M1
     - United States
     - 1943.3
     - regular
     - F
     - —
     - —
     - —
     - 6
     - 5
     - M0
     - F2
     - G1
   * - Home Guard Squad
     - United Kingdom
     - 1943.3
     - militia
     - F
     - omit (rFP too low)
     - omit (rFP too low)
     - —
     - 4
     - 3
     - M2
     - F1
     - G2
   * - Home Guard Squad (reduced)
     - United Kingdom
     - 1943.3
     - militia
     - R
     - omit (rFP too low)
     - —
     - —
     - 2
     - 3
     - M2
     - F1
     - G1

H.2  Vehicle Armour Roster
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Vehicle**
     - **Profile**
     - **Arc**
     - **AV vs Capped**
     - **AV vs Tungsten**
     - **AV vs HEAT**
     - **Schürzen**
     - **Face-hardened**
   * - Panzer IV Ausf H
     - Hull
     - Front
     - 64.9
     - 69.0
     - 81.2
     - —
     - Yes
   * - Panzer IV Ausf H
     - Hull
     - Side
     - 23.8
     - 25.2
     - 30.0
     - Yes
     - Yes
   * - Panzer IV Ausf H
     - Hull
     - Rear
     - 19.7
     - 20.8
     - 20.4
     - —
     - —
   * - Panzer IV Ausf H
     - Turret
     - Front
     - 78.9
     - 102.5
     - 50.8
     - —
     - —
   * - Panzer IV Ausf H
     - Turret
     - Side
     - 29.7
     - 30.0
     - 30.0
     - Yes
     - —
   * - Panzer IV Ausf H
     - Turret
     - Rear
     - 29.7
     - 30.5
     - 30.3
     - —
     - —
   * - Panzer IV Ausf H
     - Hull
     - Top
     - 9.8
     - 10.0
     - 10.0
     - —
     - —
   * - Panzer IV Ausf H
     - Turret
     - Top
     - 15.8
     - 16.0
     - 16.0
     - —
     - —
   * - Panzer III Ausf M
     - Hull
     - Front
     - 51.4
     - 57.0
     - 75.0
     - —
     - —
   * - Panzer III Ausf M
     - Hull
     - Side
     - 29.7
     - 30.0
     - 30.0
     - Yes
     - —
   * - Panzer III Ausf M
     - Hull
     - Rear
     - 49.8
     - 50.0
     - 50.0
     - —
     - —
   * - Panzer III Ausf M
     - Turret
     - Front
     - 57.8
     - 59.4
     - 58.3
     - —
     - —
   * - Panzer III Ausf M
     - Turret
     - Side
     - 29.7
     - 30.0
     - 30.0
     - —
     - —
   * - Panzer III Ausf M
     - Turret
     - Rear
     - 29.7
     - 30.0
     - 30.0
     - —
     - —
   * - Tiger I Ausf E
     - Hull
     - Front
     - 102.0
     - 102.8
     - 101.5
     - —
     - —
   * - Tiger I Ausf E
     - Hull
     - Side
     - 80.1
     - 80.0
     - 80.0
     - —
     - —
   * - Tiger I Ausf E
     - Hull
     - Rear
     - 80.1
     - 80.0
     - 80.0
     - —
     - —
   * - Tiger I Ausf E
     - Turret
     - Front
     - 143.0
     - 94.6
     - 100.0
     - —
     - —
   * - Tiger I Ausf E
     - Turret
     - Side
     - 80.1
     - 80.0
     - 80.0
     - —
     - —
   * - Tiger I Ausf E
     - Turret
     - Rear
     - 80.1
     - 80.0
     - 80.0
     - —
     - —
   * - Tiger I Ausf E
     - Hull
     - Top
     - 24.7
     - 25.0
     - 25.0
     - —
     - —
   * - Tiger I Ausf E
     - Turret
     - Top
     - 24.7
     - 25.0
     - 25.0
     - —
     - —
   * - StuG III Ausf G
     - Hull
     - Front
     - 87.1
     - 92.0
     - 85.7
     - —
     - —
   * - StuG III Ausf G
     - Hull
     - Side
     - 23.8
     - 25.2
     - 30.0
     - Yes
     - Yes
   * - StuG III Ausf G
     - Hull
     - Rear
     - 29.7
     - 30.0
     - 30.0
     - —
     - —
   * - T-34 Model 1943
     - Hull
     - Front
     - 93.7
     - 145.8
     - 90.0
     - —
     - —
   * - T-34 Model 1943
     - Hull
     - Side
     - 48.9
     - 65.4
     - 58.7
     - —
     - —
   * - T-34 Model 1943
     - Hull
     - Rear
     - 46.7
     - 67.7
     - 56.6
     - —
     - —
   * - T-34 Model 1943
     - Turret
     - Front
     - 55.8
     - 71.9
     - 55.3
     - —
     - —
   * - T-34 Model 1943
     - Turret
     - Side
     - 37.2
     - 39.8
     - 55.3
     - —
     - —
   * - T-34 Model 1943
     - Turret
     - Rear
     - 37.2
     - 39.8
     - 55.3
     - —
     - —
   * - T-34 Model 1943
     - Hull
     - Top
     - 12.0
     - 12.2
     - 20.0
     - —
     - —
   * - T-34/85 (late 1943)
     - Hull
     - Front
     - 93.7
     - 145.8
     - 90.0
     - —
     - —
   * - T-34/85 (late 1943)
     - Hull
     - Side
     - 48.9
     - 65.4
     - 58.7
     - —
     - —
   * - T-34/85 (late 1943)
     - Hull
     - Rear
     - 46.7
     - 67.7
     - 56.6
     - —
     - —
   * - T-34/85 (late 1943)
     - Turret
     - Front
     - 146.0
     - 171.6
     - 93.2
     - —
     - —
   * - T-34/85 (late 1943)
     - Turret
     - Side
     - 73.1
     - 77.1
     - 79.8
     - —
     - —
   * - T-34/85 (late 1943)
     - Turret
     - Rear
     - 35.2
     - 36.1
     - 52.8
     - —
     - —
   * - KV-1S
     - Hull
     - Front
     - 85.2
     - 87.6
     - 82.8
     - —
     - —
   * - KV-1S
     - Hull
     - Side
     - 49.7
     - 49.9
     - 60.0
     - —
     - —
   * - KV-1S
     - Hull
     - Rear
     - 49.7
     - 49.9
     - 60.0
     - —
     - —
   * - KV-1S
     - Turret
     - Front
     - 129.1
     - 154.2
     - 83.3
     - —
     - —
   * - KV-1S
     - Turret
     - Side
     - 68.0
     - 68.0
     - 75.0
     - —
     - —
   * - KV-1S
     - Turret
     - Rear
     - 68.0
     - 68.0
     - 75.0
     - —
     - —
   * - KV-1S
     - Hull
     - Top
     - 20.3
     - 20.5
     - 30.0
     - —
     - —
   * - KV-1S
     - Turret
     - Top
     - 16.5
     - 16.6
     - 30.0
     - —
     - —
   * - SU-85
     - Hull
     - Front
     - 75.5
     - 117.6
     - 78.5
     - —
     - —
   * - SU-85
     - Hull
     - Side
     - 48.9
     - 65.4
     - 58.7
     - —
     - —
   * - SU-85
     - Hull
     - Rear
     - 46.7
     - 67.7
     - 56.6
     - —
     - —
   * - Sherman M4A1 (75mm)
     - Hull
     - Front
     - 76.7
     - 109.2
     - 74.8
     - —
     - —
   * - Sherman M4A1 (75mm)
     - Hull
     - Side
     - 37.7
     - 38.0
     - 38.0
     - —
     - —
   * - Sherman M4A1 (75mm)
     - Hull
     - Rear
     - 37.9
     - 39.1
     - 38.6
     - —
     - —
   * - Sherman M4A1 (75mm)
     - Turret
     - Front
     - 89.0
     - 82.7
     - 89.0
     - —
     - —
   * - Sherman M4A1 (75mm)
     - Turret
     - Side
     - 50.8
     - 51.0
     - 51.0
     - —
     - —
   * - Sherman M4A1 (75mm)
     - Turret
     - Rear
     - 50.8
     - 51.0
     - 51.0
     - —
     - —
   * - Sherman M4A1 (75mm)
     - Hull
     - Top
     - 15.3
     - 15.5
     - 19.0
     - —
     - —
   * - Sherman M4A1 (75mm)
     - Turret
     - Top
     - 24.7
     - 25.0
     - 25.0
     - —
     - —
   * - Sherman M4A3 (76mm)
     - Hull
     - Front
     - 115.5
     - 157.8
     - 93.8
     - —
     - —
   * - Sherman M4A3 (76mm)
     - Hull
     - Side
     - 37.7
     - 38.0
     - 38.0
     - —
     - —
   * - Sherman M4A3 (76mm)
     - Hull
     - Rear
     - 37.9
     - 39.1
     - 38.6
     - —
     - —
   * - Sherman M4A3 (76mm)
     - Turret
     - Front
     - 93.6
     - 116.6
     - 66.3
     - —
     - —
   * - Sherman M4A3 (76mm)
     - Turret
     - Side
     - 50.8
     - 51.0
     - 51.0
     - —
     - —
   * - Sherman M4A3 (76mm)
     - Turret
     - Rear
     - 50.8
     - 51.0
     - 51.0
     - —
     - —
   * - Sherman M4A3 (76mm)
     - Hull
     - Top
     - 18.7
     - 19.0
     - 19.0
     - —
     - —
   * - Sherman M4A3 (76mm)
     - Turret
     - Top
     - 24.7
     - 25.0
     - 25.0
     - —
     - —
   * - Sdkfz 251 half-track
     - Hull
     - Front
     - 14.3
     - 15.5
     - 15.0
     - —
     - —
   * - Sdkfz 251 half-track
     - Hull
     - Side
     - 7.8
     - 8.0
     - 8.0
     - —
     - —
   * - Sdkfz 251 half-track
     - Hull
     - Rear
     - 7.8
     - 8.0
     - 8.0
     - —
     - —
   * - T-70 light tank
     - Hull
     - Front
     - 44.0
     - 69.3
     - 54.5
     - —
     - —
   * - T-70 light tank
     - Hull
     - Side
     - 8.3
     - 8.4
     - 15.0
     - —
     - —
   * - T-70 light tank
     - Hull
     - Rear
     - 8.3
     - 8.4
     - 15.0
     - —
     - —
   * - T-70 light tank
     - Turret
     - Front
     - 30.5
     - 41.9
     - 35.5
     - —
     - —
   * - T-70 light tank
     - Turret
     - Side
     - 8.3
     - 8.4
     - 15.0
     - —
     - —
   * - T-70 light tank
     - Turret
     - Rear
     - 8.3
     - 8.4
     - 15.0
     - —
     - —
   * - T-70 light tank
     - Hull
     - Top
     - 4.9
     - 5.0
     - 10.0
     - —
     - —
   * - Panther Ausf G
     - Hull
     - Front
     - 229.1
     - 299.6
     - 156.1
     - —
     - —
   * - Panther Ausf G
     - Hull
     - Side
     - 59.3
     - 67.8
     - 57.7
     - —
     - —
   * - Panther Ausf G
     - Hull
     - Rear
     - 46.7
     - 54.2
     - 46.2
     - —
     - —
   * - Panther Ausf G
     - Turret
     - Front
     - 249.2
     - 94.6
     - 100.0
     - —
     - —
   * - Panther Ausf G
     - Turret
     - Side
     - 42.6
     - 45.1
     - 49.7
     - —
     - —
   * - Panther Ausf G
     - Turret
     - Rear
     - 44.2
     - 49.3
     - 51.0
     - —
     - —
   * - Panther Ausf G
     - Hull
     - Top
     - 15.8
     - 16.0
     - 16.0
     - —
     - —
   * - Panther Ausf G
     - Turret
     - Top
     - 12.8
     - 13.0
     - 16.0
     - —
     - —
   * - Churchill Mk VII
     - Hull
     - Front
     - 153.1
     - 152.0
     - 152.0
     - —
     - —
   * - Churchill Mk VII
     - Hull
     - Side
     - 95.2
     - 95.0
     - 95.0
     - —
     - —
   * - Churchill Mk VII
     - Hull
     - Rear
     - 50.8
     - 51.0
     - 51.0
     - —
     - —
   * - Churchill Mk VII
     - Turret
     - Front
     - 157.6
     - 156.5
     - 152.0
     - —
     - —
   * - Churchill Mk VII
     - Turret
     - Side
     - 89.4
     - 89.2
     - 95.0
     - —
     - —
   * - Churchill Mk VII
     - Turret
     - Rear
     - 89.4
     - 89.2
     - 95.0
     - —
     - —
   * - Churchill Mk VII
     - Hull
     - Top
     - 12.8
     - 13.0
     - 13.0
     - —
     - —
   * - Churchill Mk VII
     - Turret
     - Top
     - 16.2
     - 16.4
     - 20.0
     - —
     - —
   * - Cromwell Mk IV
     - Hull
     - Front
     - 63.9
     - 64.0
     - 64.0
     - —
     - —
   * - Cromwell Mk IV
     - Hull
     - Side
     - 31.7
     - 32.0
     - 32.0
     - —
     - —
   * - Cromwell Mk IV
     - Hull
     - Rear
     - 31.7
     - 32.0
     - 32.0
     - —
     - —
   * - Cromwell Mk IV
     - Turret
     - Front
     - 69.8
     - 69.7
     - 76.7
     - —
     - —
   * - Cromwell Mk IV
     - Turret
     - Side
     - 37.5
     - 37.7
     - 44.0
     - —
     - —
   * - Cromwell Mk IV
     - Turret
     - Rear
     - 37.5
     - 37.7
     - 44.0
     - —
     - —
   * - Sherman Firefly VC
     - Hull
     - Front
     - 122.8
     - 181.4
     - 91.2
     - —
     - —
   * - Sherman Firefly VC
     - Hull
     - Side
     - 37.7
     - 38.0
     - 38.0
     - —
     - —
   * - Sherman Firefly VC
     - Hull
     - Rear
     - 37.7
     - 38.0
     - 38.0
     - —
     - —
   * - Sherman Firefly VC
     - Turret
     - Front
     - 102.0
     - 102.0
     - 102.0
     - —
     - —
   * - Sherman Firefly VC
     - Turret
     - Side
     - 50.8
     - 51.0
     - 51.0
     - —
     - —
   * - Sherman Firefly VC
     - Turret
     - Rear
     - 61.9
     - 62.0
     - 62.0
     - —
     - —

H.3  Gun Penetration Curves
--------------------------------

*0°-equivalent millimetres by range band (Rule 17.3.1) — read the row for
the ammunition nature actually fired.*

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Gun**
     - **Confidence**
     - **0m**
     - **250m**
     - **500m**
     - **750m**
     - **1000m**
     - **1250m**
     - **1500m**
     - **1750m**
     - **2000m**
     - **2500m**
   * - pziv_75l48_apcbc
     - fitted
     - 137.8
     - 128.4
     - 119.6
     - 111.4
     - 103.7
     - 96.6
     - 90.0
     - 83.8
     - 78.0
     - 67.7
   * - tiger_88_apcbc
     - fitted
     - 151.9
     - 144.5
     - 137.4
     - 130.6
     - 124.2
     - 118.1
     - 112.3
     - 106.7
     - 101.5
     - 91.8
   * - pziii_50l60_apcbc
     - fitted
     - 90.4
     - 79.0
     - 69.0
     - 60.3
     - 52.7
     - 46.0
     - 40.2
     - 35.1
     - 30.7
     - 23.4
   * - t34_76_f34_apc
     - fitted
     - 82.7
     - 77.3
     - 72.2
     - 67.5
     - 63.1
     - 58.9
     - 55.1
     - 51.5
     - 48.1
     - 42.0
   * - t3485_85_d5t_apc
     - fitted
     - 136.0
     - 127.7
     - 119.8
     - 112.5
     - 105.6
     - 99.1
     - 93.0
     - 87.3
     - 81.9
     - 72.1
   * - sherman75_m61_apc
     - fitted
     - 90.7
     - 84.1
     - 77.9
     - 72.2
     - 66.9
     - 62.1
     - 57.5
     - 53.3
     - 49.4
     - 42.5
   * - sherman76_m62_apc
     - fitted
     - 127.1
     - 122.2
     - 117.5
     - 112.9
     - 108.6
     - 104.4
     - 100.4
     - 96.5
     - 92.8
     - 85.8
   * - t70_45l46_apbc
     - interpolated
     - 86.3
     - 71.6
     - 59.3
     - 49.2
     - 40.8
     - 33.8
     - 28.0
     - 23.2
     - 19.3
     - 13.2
   * - panther_75l70_apcbc
     - fitted
     - 179.4
     - 168.7
     - 158.6
     - 149.1
     - 140.2
     - 131.8
     - 124.0
     - 116.6
     - 109.6
     - 96.9
   * - sixpdr_57l50_apcbc
     - fitted
     - 119.2
     - 111.2
     - 103.7
     - 96.7
     - 90.1
     - 84.0
     - 78.4
     - 73.1
     - 68.1
     - 59.2
   * - seventeenpdr_76l55_apcbc
     - fitted
     - 178.6
     - 171.2
     - 164.0
     - 157.2
     - 150.6
     - 144.3
     - 138.3
     - 132.5
     - 127.0
     - 116.6
   * - seventeenpdr_76l55_apds
     - fitted
     - 280.1
     - 267.6
     - 255.7
     - 244.3
     - 233.4
     - 223.0
     - 213.1
     - 203.6
     - 194.5
     - 177.6
   * - pak40_75l46_apcbc
     - fitted
     - 143.8
     - 130.1
     - 117.7
     - 106.4
     - 96.3
     - 87.1
     - 78.7
     - 71.2
     - 64.4
     - 52.7
   * - pak40_75l46_apcr
     - fitted
     - 202.9
     - 181.8
     - 162.8
     - 145.9
     - 130.6
     - 117.0
     - 104.8
     - 93.9
     - 84.1
     - 67.5
   * - usm1_57l50_ap
     - fitted
     - 140.3
     - 124.1
     - 109.7
     - 97.0
     - 85.7
     - 75.8
     - 67.0
     - 59.2
     - 52.4
     - 40.9
   * - sixpdr_57l50_apds
     - fitted
     - 181.8
     - 170.4
     - 159.7
     - 149.6
     - 140.1
     - 131.3
     - 123.0
     - 115.3
     - 108.0
     - 94.8
