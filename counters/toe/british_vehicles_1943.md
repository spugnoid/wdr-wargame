# British 6-Pounder, 17-Pounder, and Vehicle Armor — Technical Data

Research pass only. No AV/PEN numbers are computed here — that is a separate step
using this project's own `fit_gun_curve` (see `counters/armor_calc/formulas.py`).
This file gathers raw, cited inputs: muzzle velocities, calibration points, and
armor thickness/angle/construction for British 6pdr, 17pdr, Churchill Mk VII, and
Cromwell Mk IV, to fill the gap named in
`docs/superpowers/specs/2026-07-04-armored-combat-penetration-physics-design.md`.

## Sources

- Bird, Lorrin Rexford & Livingston, Robert D. (2001). *WWII Ballistics: Armor and
  Gunnery*. Overmatch Press, Albany, NY. (Not accessed directly this session —
  page numbers below are as cited by Wikipedia, which quotes this book's tables
  verbatim with page refs. This is the SAME book named in this project's own
  design spec as one of its two original data sources, which is a useful
  continuity point.)
- Wikipedia, "Ordnance QF 6-pounder" — https://en.wikipedia.org/wiki/Ordnance_QF_6-pounder
  (raw wikitext pulled directly, table at `Estimated armour penetration (versus
  vertical armour)`, cited to Bird & Livingston 2001 pp. 60, 62)
- Wikipedia, "Ordnance QF 17-pounder" — https://en.wikipedia.org/wiki/Ordnance_QF_17-pounder
  (raw wikitext pulled directly, table `Calculated penetration figures (90
  degrees)`, cited to Bird & Livingston 2001 p. 60; ammunition characteristics
  table cited to *Royal Armoured Corps Training, Vol. III — Armament, Pamphlet
  No 7, SP 17-pr M10*, War Office, July 1952)
- Wikipedia, "Churchill tank" — https://en.wikipedia.org/wiki/Churchill_tank
  (raw wikitext; armor paragraph cites *Churchill – Vehicle History and
  Specifications* [Fletcher]; construction paragraphs cite Fletcher 1993/2019,
  White 1983)
- Wikipedia, "Cromwell tank" — https://en.wikipedia.org/wiki/Cromwell_tank
  (raw wikitext; infobox armor line cites Fletcher & Harley (2006) p. 12; body
  text cites Higgins and Fletcher & Harley (2006) p. 18; a commented-out/unpublished
  "Armour disposition" table in the wiki source cites an archival document
  "Cromwell plate thickness, TD.8401" — flagged below as unverified-by-Wikipedia's-own-editors)
- Wikipedia, "Sherman Firefly" — https://en.wikipedia.org/wiki/Sherman_Firefly
  (cites Bird & Livingston 2001 p. 60 for the same 17pdr figures; confirms no
  detailed hull armor breakdown is readily available there)
- Chamberlain, Peter & Ellis, Chris. *British and American Tanks of World War
  II*, p. 203 (as quoted in the 6-pounder Wikipedia article) — single 30°-obliquity
  data point for 6pdr AP.
- Tank Archives (Peter Samsonov), https://www.tankarchives.com — several posts
  checked: "Penetration Equations" (2014), "17-Pounder: Britain's Long Arm"
  (2016, Soviet trials of a captured 17pdr at Gorohovets proving ground),
  "Penetration: British Edition" (2017, Lulworth comparative trial 31 March 1944),
  "Cromwell Armour" (2017, images only — not machine-readable this session),
  "The Last Cruiser" (2020, Comet-focused, no Cromwell armor numbers).
- historyofwar.org Churchill and Cromwell pages (thin on armor detail, checked
  and largely superseded by the Wikipedia raw-wikitext pulls above).

## 6-Pounder Gun

**Important convention note:** the Bird & Livingston-derived tables below are
explicitly captioned "penetration versus **vertical** armour" — i.e. 0° obliquity
(straight-on hit against a plate mounted vertically), NOT the 30°-from-vertical
convention this project uses for its other guns' calibration rows (see
`gun_calibration.csv`, all of which are angle_deg=30). These 0°-obliquity numbers
are still real, citable, useful data, but they are **not directly interchangeable**
with the existing 30°-obliquity rows without either finding a genuine 30° table
or converting via the project's own angle/effective-thickness formulas. Only one
real 30°-obliquity data point was found for the 6pdr (Chamberlain & Ellis, single
point, tank-gun context) — flagged inline below.

### APC/APCBC
- Muzzle velocity: APCBC (L/50 barrel, British ammunition) — 831 m/s = **2,730 ft/s**.
  (US-made APCBC shell, same gun: 823 m/s = 2,700 ft/s — kept separate below.)
- K-factor: **not found** — no source located states a ballistic K-factor
  (in this project's `V(range) = MV × e^(range × 0.7 × -0.0000001 × K)` sense)
  for the 6pdr. The only "K" concept found in the ballistics literature searched
  is unrelated: Tank Archives' "Penetration Equations" post describes a Soviet/
  German-style DeMarre-Krupp formula where K is an *armor-quality* resistance
  constant (not a velocity-retardation term), with "2400" cited as a generic
  standard-quality-armor value — this is a different parameter in a different
  formula and should not be borrowed in as if it were this project's K-factor.
  Per this project's existing `guns.csv` rows, every other gun's K-factor was
  itself derived by curve-fitting the calibration points (per their
  confidence_note fields, e.g. "5-pt fit, <1.2% error"), not sourced directly —
  so the expectation is that 6pdr/17pdr K-factors will likewise need to be
  fit from the calibration points below, not looked up.
- Calibration points (0° obliquity, "versus vertical armour", British APCBC,
  L/50 barrel; Bird & Livingston 2001 pp. 60/62 via Wikipedia):
  - (100 m, 115 mm, 0°)
  - (500 m, 103 mm, 0°)
  - (1000 m, 90 mm, 0°)
  - (1500 m, 78 mm, 0°)
  - (2000 m, 68 mm, 0°)
- US-made APCBC shell M86, same gun, same source, also 0° obliquity, for
  reference/cross-check only (not the British round):
  - (100 m, 110 mm, 0°), (500 m, 98 mm, 0°), (1000 m, 85 mm, 0°),
    (1500 m, 73 mm, 0°), (2000 m, 64 mm, 0°); MV 823 m/s = 2,700 ft/s.
- Single 30°-obliquity point (different source, tank-gun-mounted AP, not
  APCBC specifically — included for cross-reference, NOT enough alone to fit
  a curve): 81 mm (Mk 3 gun) / 83 mm (Mk 5 gun) at 500 yards (457 m) and 30°
  target angle. Source: Chamberlain & Ellis, *British and American Tanks of
  World War II*, p. 203.

### AP (uncapped, ap_uncapped family per this project's design spec)
Not explicitly requested but found alongside APCBC in the same table and worth
recording since it may be relevant to the early-war 6pdr fit (pre-APCBC issue):
- Muzzle velocity: 892 m/s = **2,930 ft/s** (British AP, L/50 barrel).
- Calibration points (0° obliquity, Bird & Livingston 2001 pp. 60/62):
  (100 m, 135 mm, 0°), (500 m, 112 mm, 0°), (1000 m, 89 mm, 0°),
  (1500 m, 70 mm, 0°), (2000 m, 55 mm, 0°).
- US AP shot M70, same gun: identical penetration figures given in the source
  (135/112/89/70/55 mm at the same ranges) but MV = 853 m/s = 2,800 ft/s.

### APDS (found)
- Muzzle velocity: 1,219 m/s = **4,000 ft/s**. Source notes APDS entered
  service "from March 1944" — outside this project's nominal 1943 vehicle
  era, flag for the designer to decide if it's in scope at all for a 1943 roster.
- K-factor: not found (same situation as APCBC above).
- Calibration points (0° obliquity, Bird & Livingston 2001 pp. 60/62):
  (100 m, 177 mm, 0°), (500 m, 160 mm, 0°), (1000 m, 140 mm, 0°),
  (1500 m, 123 mm, 0°), (2000 m, 108 mm, 0°).

## 17-Pounder Gun

Same 0°-obliquity ("90 degrees" in the source's own heading, meaning the plate
is mounted at 90° to the horizontal, i.e. vertical, hit at normal/0° obliquity)
caveat applies here as for the 6pdr — see note above. This table is unusually
rich: Bird & Livingston give **11 range points** (100 through 3000 m) per
ammunition nature, and separate rows for performance against face-hardened
armor (FHA) vs rolled homogeneous armor (RHA), which is more than this project
needed for any existing gun.

### APCBC
- Muzzle velocity: **884 m/s = 2,900 ft/s** (per the penetration-table header
  in Bird & Livingston, as reproduced by Wikipedia). NOTE: the same Wikipedia
  article's separate ammunition-characteristics table (sourced instead to
  *Royal Armoured Corps Training Vol. III, Pamphlet No 7*, War Office, July
  1952) gives APCBC muzzle velocity as 2,950 ft/s (899 m/s) — a ~50 ft/s
  discrepancy between two tables in the same article, from two different
  primary sources. Flagged; did not resolve which is more authoritative.
- K-factor: **not found** (same situation as the 6pdr — no directly published
  velocity-retardation K located; would need to be fit from the points below).
- Calibration points, vs RHA (Bird & Livingston 2001 p. 60):
  - (100 m, 174 mm, 0°), (250 m, 170 mm, 0°), (500 m, 163 mm, 0°),
    (750 m, 156 mm, 0°), (1000 m, 150 mm, 0°), (1250 m, 143 mm, 0°),
    (1500 m, 137 mm, 0°), (1750 m, 132 mm, 0°), (2000 m, 126 mm, 0°),
    (2500 m, 116 mm, 0°), (3000 m, 107 mm, 0°)
- Parallel row vs face-hardened armor (FHA), same MV, same source — kept
  separate since it's a different target-armor-type, not a different range set:
  (100 m, 187 mm, 0°) … (2000 m, 136 mm, 0°) … (3000 m, 115 mm, 0°) — full
  11-point row available if useful.
- 30°-obliquity cross-reference only (found via secondary aggregation, exact
  primary citation NOT independently confirmed this session — treat as weaker):
  130 mm at 500 m and 119 mm at 1000 m at 30° obliquity. This pair recurs
  across several secondary pages (Company of Heroes wiki, alternatewars.com-style
  aggregators) without a traceable primary citation found this session — flagged
  as single/uncertain-source, do not treat as equal-weight to the Bird &
  Livingston table above.

### AP (uncapped)
- Muzzle velocity: 884 m/s = 2,900 ft/s (same gun/charge as APCBC row).
- Calibration points vs RHA (Bird & Livingston 2001 p. 60):
  (100 m, 200 mm, 0°), (250 m, 190 mm, 0°), (500 m, 175 mm, 0°),
  (750 m, 160 mm, 0°), (1000 m, 147 mm, 0°), (1250 m, 135 mm, 0°),
  (1500 m, 124 mm, 0°), (1750 m, 114 mm, 0°), (2000 m, 105 mm, 0°),
  (2500 m, 88 mm, 0°), (3000 m, 74 mm, 0°)

### APDS (found)
- Muzzle velocity: **1,204 m/s = 3,950 ft/s**.
- K-factor: not found.
- Calibration points vs RHA (Bird & Livingston 2001 p. 60):
  (100 m, 275 mm, 0°), (250 m, 268 mm, 0°), (500 m, 256 mm, 0°),
  (750 m, 244 mm, 0°), (1000 m, 233 mm, 0°), (1250 m, 223 mm, 0°),
  (1500 m, 213 mm, 0°), (1750 m, 204 mm, 0°), (2000 m, 194 mm, 0°),
  (2500 m, 178 mm, 0°), (3000 m, 162 mm, 0°)
- Alternate figures noted in the same Wikipedia article's footnotes (NOT used
  above, flagged as conflicting secondary data): a Bovington Tank Museum
  document (uncited beyond "citation needed") states 187 mm at 500 yards at
  30° obliquity; *Jane's Armour and Artillery 1981–82* gives 231 mm at 1,000
  yards at 30° obliquity. Neither is a 0°/vertical-armor figure, so neither
  is directly comparable to the main table above, but both suggest the "true"
  30°-obliquity APDS performance is considerably below the naive normal-incidence
  numbers, as expected.
- Soviet trial data point (Tank Archives, "17-Pounder: Britain's Long Arm",
  citing CAMD RF archival trial records, Gorohovets proving ground, Sept–Nov
  1944, guns serial #1926 and #5593, 136 rounds fired): 100 mm plate defeated
  at 1,800 m at "flat" (0°) angle and at 1,000 m at 30°; 90 mm plate defeated
  at 2,000 m flat and 1,200 m at 30°; 76 mm plate defeated at 2,200 m flat.
  Muzzle velocities recorded: 908.7 m/s (standard charge) and 930 m/s (Soviet
  increased-charge test). These are pass/fail proving-ground results, not
  penetration-mm-at-range figures, so not directly usable as (range, mm, angle)
  calibration points, but corroborate the ballpark of the APDS-class figures
  above and are a genuinely independent primary-ish source (archival, not
  Bird & Livingston).

## Churchill Mk VII

Used Mk VII specifically (well-documented; this is the mark the project's own
rules text and this task both name). Construction: rolled homogeneous plate
specified as "IT 80", cast sections as "IT 90" (Fletcher, per Wikipedia's
"Churchill – Vehicle History and Specifications" citation). Mk VII hull was
all-welded (A22F); earlier marks were riveted/bolted. Wikipedia's own prose is
explicit and important: **"though this armour was considerably thicker than
its rivals... it was not sloped, reducing its effectiveness."** Treat near-0°
angles below as a real, sourced design characteristic, not a research gap.

| Plate | Thickness (mm) | Angle from vertical | Cast/Rolled | Notes |
|---|---|---|---|---|
| Hull Front (upper) | 152 mm | ~0° (described as "vertical") | Rolled (IT 80) | Uppermost of a 3-plate stepped glacis |
| Hull Front (middle) | 57 mm | described only as "nearly horizontal" — no exact degree value found | Rolled (IT 80) | Small connecting plate between upper/lower glacis pieces; exact angle NOT found this session |
| Hull Front (lower/nose) | 140 mm | described only as "a lower angled piece" — no exact degree value found | Rolled (IT 80) | Same gap as above |
| Hull Side | 95 mm | 0° (vertical, boxy hull over track panniers) | Rolled (IT 80) | |
| Hull Rear | 51 mm | not stated; treat as ~0° consistent with "not sloped" design, unconfirmed | Rolled (IT 80) | |
| Hull Top | 13.3 mm | — | Rolled | included for completeness only |
| Turret Front | 152 mm (150–152 mm depending on source rounding) | not stated as a single flat angle — see note | Cast (IT 90) | Mk VII turret was cast for the 4 walls as one piece, roof welded on separately; "composite construction – cast with top and bottom plates welded into position" per source. Likely needs the same kind of mantlet/turret-front combined-resistance treatment this project already applied to the Tiger (Ch.10-style table) and Panther (Ch.11-style weighted mantlet-angle distribution) — NOT attempted here, flagged as follow-up. |
| Turret Side | 95 mm | 0° (flat cast side) | Cast (IT 90) | single casting for all 4 turret walls |
| Turret Rear | 95 mm | 0° | Cast (IT 90) | same single casting as turret side |
| Turret Roof | 20 mm | — | — | included for completeness only |

## Cromwell Mk IV

Used the "standard/Final Specification" Cromwell hull+turret figures, which
Wikipedia treats as common across marks I–VIII (hull/turret types were
developed somewhat independently of gun-armament marks; Mk IV specifically =
Centaur III hull re-engined with the Rolls-Royce Meteor, 75 mm gun turret,
the single most numerous Cromwell variant at ~1,935 built). Construction:
riveted frame with bolted-on plate on early/non-W-suffix vehicles; all-welded
on BRC&W-built "W-suffix" vehicles (e.g. hull type Dw/Ew), which used the
weight saved by welding to add applique armor instead.

| Plate | Thickness (mm) | Angle from vertical | Cast/Rolled | Notes |
|---|---|---|---|---|
| Hull Front (main/vertical driver's plate) | 64 mm | 0° ("vertical", explicitly NOT sloped like the Sherman glacis) | Rolled, riveted-to-frame (welded on W-suffix vehicles) | Well-established, direct infobox citation: Fletcher & Harley (2006) p.12 |
| Hull Front (lower nose piece) | ~25 mm per one source (see confidence notes — this line comes from a Wikipedia-internal, currently-commented-out table, NOT the article's visible text) | described as "sloped" but no degree value found | Rolled | Single, weakly-sourced figure — see Confidence Notes |
| Hull Front, applique-upgraded (123 vehicles, welded/W-suffix only) | 101 mm (64 mm base + applique) | 0° | Rolled | Fletcher & Harley (2006) p.18 |
| Hull Side | commonly cited as 32 mm; ranges as wide as "29–44 mm" and "14+29 mm (spaced)" appear across sources | 0° (vertical; "two spaced plates" over the suspension per the article's own prose) | Rolled, riveted | See Confidence Notes — real disagreement between sources on the exact figure/whether it's a single or spaced plate |
| Hull Rear | commonly cited 32 mm; one weak source gives "14–32 mm" | 0°, unconfirmed | Rolled | Same caveat as hull side |
| Turret Front | **76.7 mm** (well-cited: Fletcher & Harley 2006 p.12, in the infobox) vs **64 mm** (from the same weakly-sourced commented-out Wikipedia table) vs 76 mm (rounded, seen on several aggregator sites) | not stated; turret described as hexagonal with "an internal mantlet" | Cast, hardened per one secondary source (uncorroborated) | Real source conflict — see Confidence Notes. Prefer 76.7 mm (has a real page citation) over the 64 mm figure. |
| Turret Side | commonly cited ~44–51 mm across sources; one source gives "44–64 mm" | 0° (flat hexagonal turret face) | Cast | |
| Turret Rear | commonly cited ~44 mm | 0° | Cast | |
| Turret Roof | 20 mm | — | — | included for completeness only |

## Sherman Firefly

Not pursued in depth — per the task's own priority order, Churchill and Cromwell
were treated as the priority and both needed enough follow-up searching that
Firefly research capacity was limited. What was confirmed: the Firefly's own
Wikipedia article adds no armor detail beyond the standard Sherman hull specs
already in this project's `vehicles.csv` (e.g. Sherman M4A1/M4A3 rows) plus a
turret-front figure of "89 mm maximum" and a note that the mantlet got "an
additional 13 mm of protection" over the standard Sherman mantlet, with no
angle or cast/rolled breakdown given. If pursued later: the base hull should
reuse whichever existing Sherman hull variant matches the actual Firefly
conversion base (M4, M4 Composite/"Hybrid" with cast front hull, or M4A4 — the
M4A4/Sherman V was the most numerous conversion base per the Firefly article),
and only the turret mantlet and the 17-pounder gun data above are actually new.

## Confidence Notes

- **6pdr AP/APCBC/APDS calibration points (0° obliquity):** well-established —
  single strong source (Bird & Livingston via Wikipedia's direct wikitext,
  which itself gives a specific page citation), internally consistent 5-point
  tables for both British and US ammunition natures.
- **6pdr 30°-obliquity point (81/83 mm @ 500 yd):** single-source (Chamberlain
  & Ellis), only one range point — usable as a sanity check, not as a
  standalone calibration set.
- **17pdr AP/APCBC/APDS calibration points (0° obliquity, vs RHA and vs FHA):**
  well-established — same strong source, unusually complete (11 range points).
  The two conflicting muzzle-velocity figures for APCBC (2,900 vs 2,950 ft/s,
  both from cited primary-ish documents within the same Wikipedia article) are
  a genuine, flagged discrepancy — pick one deliberately rather than silently
  averaging.
- **17pdr 30°-obliquity APCBC/APDS figures found via secondary aggregation
  (130/119 mm APCBC; 204/185 mm APDS):** these numbers recur across several
  low-authority pages but no primary citation could be traced this session —
  treat as uncertain, not equal-weight to the Bird & Livingston table.
- **17pdr Soviet Gorohovets trial data (Tank Archives):** single-source but
  archival-flavored (Peter Samsonov's blog regularly transcribes CAMD RF
  documents); format is pass/fail plate-defeat distances rather than clean
  (range, mm, angle) triples, so treat as corroborating context, not
  calibration-ready data.
- **K-factor for both guns:** genuinely **not found** for either the 6pdr or
  the 17pdr, in any ammunition nature. This is consistent with every existing
  gun row in this project's own `guns.csv`, whose K-factors all carry
  confidence_notes describing them as fitted from calibration points (e.g.
  "5-pt fit, <1.2% error"), not sourced directly from a book. Recommend the
  same approach here: fit K from the calibration points above via
  `fit_gun_curve`, at whichever obliquity convention (0° here, vs 30° for
  every other existing gun) the designer decides to standardize on.
- **0° vs 30° obliquity convention mismatch:** flagged repeatedly above but
  worth restating once, clearly: nearly all the strong (Bird & Livingston)
  calibration data found for both British guns is captioned as 0°-obliquity
  ("vertical armour" / "90 degrees" meaning a vertical plate hit square-on),
  while every existing gun row in this project's `gun_calibration.csv` is at
  30°-obliquity. This is a real methodological decision point for whoever
  does the fitting step, not something resolved in this research pass.
- **Churchill Mk VII overall armor thicknesses (152/95/51 mm) and cast/rolled
  split (IT 80 rolled, IT 90 cast):** well-established, appears consistently
  across the Wikipedia infobox, body text, and multiple secondary sources.
- **Churchill Mk VII exact degree angles for the middle and lower glacis
  plates:** NOT found — only qualitative descriptions ("nearly horizontal",
  "a lower angled piece") were located this session. This is a genuine gap,
  not a guess dressed up as a number.
- **Churchill turret-front combined resistance (single mantlet-style AV
  figure):** not attempted — flagged as needing the same kind of treatment
  already used elsewhere in this project for Tiger/Panther turret fronts.
- **Cromwell hull front main plate (64 mm, vertical) and applique upgrade
  (101 mm, 123 vehicles):** well-established, direct page citations (Fletcher
  & Harley 2006, pp. 12 and 18).
- **Cromwell hull side/rear and turret front/side/rear exact thicknesses:**
  genuinely uncertain — multiple secondary sources disagree with each other
  (turret front alone was seen cited as 64, 76, and 76.7 mm across different
  pages), and the one archival-flavored table found (Wikipedia's own
  commented-out "Armour disposition" section, citing "Cromwell plate
  thickness, TD.8401") was never actually published by Wikipedia's editors —
  it may have been pulled for being unreliable, unverified, or superseded;
  treat it as the weakest tier of source here, included only for completeness
  and cross-reference, not as a resolved figure.
- **Cromwell turret described as "cast hardened steel" for all six plates:**
  single, weak secondary source — not corroborated elsewhere this session.
- **Sherman Firefly:** not researched in depth; nothing above should be taken
  as a considered recommendation beyond "reuse an existing Sherman hull row
  and add the 17pdr gun data already gathered."

## Open Questions / Gaps for Follow-up

1. No K-factor (velocity-retardation constant, this project's specific sense)
   was found published anywhere for the 6pdr or 17pdr in any ammunition
   nature — will need to be fit from the calibration points above.
2. All of the strong 6pdr/17pdr calibration data is at 0° obliquity
   ("vertical armour"), not the 30° convention used for every other gun in
   this project — needs a deliberate decision (find/derive a genuine 30°
   table, or extend the project's methodology to mixed-obliquity calibration).
3. Exact degree angles for the Churchill Mk VII's middle and lower glacis
   plates were not found in accessible sources this session — may need a
   dedicated primary source (Fletcher's Churchill book directly, or an
   Osprey New Vanguard title) not accessible via web search alone.
4. A single combined turret-front/mantlet resistance figure for the Churchill
   Mk VII (analogous to the Tiger and Panther treatments already in this
   project) was not attempted.
5. Cromwell hull side/rear and turret thicknesses have real, unresolved
   disagreement across sources (see Confidence Notes) — would benefit from
   a direct look at Fletcher & Harley (2006), *Cromwell Cruiser Tank*, or the
   Osprey New Vanguard Cromwell/Centaur title, neither of which was accessible
   this session.
6. Sherman Firefly was only lightly touched — a real pass would need the
   specific hull variant(s) actually converted (M4, M4 Composite/Hybrid with
   its cast front hull, and M4A4/Sherman V, the most numerous base) cross-
   referenced against this project's existing Sherman rows in `vehicles.csv`.
7. The 17pdr APCBC muzzle-velocity discrepancy (2,900 vs 2,950 ft/s across two
   differently-cited tables in the same Wikipedia article) was not resolved.

## Addendum, 2026-09-12: Churchill and Cromwell nose-plate angles found in Bird & Livingston's own British AFV table (design note E.134)

A direct read of Bird & Livingston's own British AFV table (p.73 — see
`counters/toe/wwii_ballistics_direct_read_1943.md` for the full read this
addendum draws on) resolved Open Question #3 above and surfaced a new,
conflicting data point for Cromwell's own nose plate.

- **Churchill's lower nose plate**: the book's table gives **140mm at 20°**
  from vertical. This matches the thickness already in this file's own table
  (line "Hull Front (lower/nose)," 140mm) exactly, and supplies the missing
  angle Open Question #3 named directly. This is real, useful data — but note
  it resolves only the *lower* of the two previously-unangled plates; the
  *middle* connecting plate (57mm, "nearly horizontal") still has no angle
  in any source checked, in this session or the earlier one. A full
  hit-distribution/area-weighted treatment of Churchill's stepped glacis
  (comparable to Tiger/Panther's mantlet treatments) still needs that third
  number before it could be built — not attempted this session; `vehicles.csv`
  continues to use the single well-cited 152mm@0° top plate as the Hull
  Front representative, now with the lower plate's angle recorded here as
  known-but-not-yet-incorporated, not as a silent gap.
- **Cromwell's nose plate**: the book's table gives **57mm at 20°** — a real,
  better-sourced figure that **conflicts** with the existing weakly-sourced
  entry in this file's own Cromwell table ("Hull Front (lower nose piece),"
  ~25mm, sourced only to "a Wikipedia-internal, currently-commented-out
  table," already flagged there as weak). The two entries may be measuring
  different things (a genuinely different plate, or a different point on a
  tapered nose casting) rather than being a straightforward correction of one
  by the other — not resolved this session. Separately, this is a plate this
  project's own `vehicles.csv` doesn't model as a distinct row at all: the
  existing `Cromwell Mk IV` `Hull Front` entry (64mm@0°, per Fletcher & Harley
  2006 p.12) represents only the main vertical driver's plate, matching the
  book's own explicit note that this hull was "vertical, explicitly NOT
  sloped like the Sherman glacis" — the 57mm@20° nose piece is evidently a
  separate, additional plate not currently represented anywhere in this
  project's roster. Recorded here as a real, newly-surfaced gap rather than
  decided either way (whether to add it as a second `vehicles.csv` row, fold
  it into a weighted treatment, or leave the single-plate simplification as
  an accepted approximation is a design decision for whoever picks this up).
