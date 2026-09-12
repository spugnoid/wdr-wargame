# Bird & Livingston, *WWII Ballistics: Armor and Gunnery* — Direct Read (Complete)

Research pass reading this project's own foundational armor-ballistics source
directly for the first time. Bird, Lorrin Rexford & Livingston, Robert D. (2001).
*WWII Ballistics: Armor and Gunnery*. Overmatch Press, Albany, NY. This book is
named in the project's own design spec as one of its two original data sources,
and is cited dozens of times throughout `counters/guns.csv`, `counters/armor_calc/
data/*.csv`, and `counters/toe/*.md` — but until this pass, every single citation
in this project was second-hand, via Wikipedia's quotation of specific tables,
never the book itself. The copy read is a 234-page image-only scan (no OCR text
layer, non-constant page numbering due to unnumbered chart inserts); read by
targeted navigation rather than linear page-by-page, prioritizing the chapters
already load-bearing for this project's own formulas and data.

## Coverage

Two passes, same session (2026-09-12). **Pass 1** read: Introduction, Ch.2 (slope
multipliers, spot-check), Ch.5 (cast deficiency, in full), Ch.6 (Armor Flaws, in
full), Ch.12 (compound angle), Ch.13 (Penetration Data intro, Soviet/K-factor
tables), Ch.14 (USA AFV and Soviet AFV tables only), Ch.18 (Projectile Velocity
Estimation, both K-factor table pages). **Pass 2** read everything pass 1 didn't
reach: Ch.1 (Intro), Ch.3 (Face-Hardened Armor), Ch.4 (High-Hardness Multipliers),
Ch.7 (Shatter Gap), Ch.8 (Special Cast Armor Areas), Ch.9 (Spaced/Layered
Armor/Edge Effects), Ch.10 (Edge Hits on Tiger E Mantlet), Ch.11 (Turret Hit
Probability and Rounded Mantlets), Ch.13 (remainder — UK/German/US/Soviet/Italian
tables in full), Ch.14 (remainder — German/British/Italian AFV tables, completing
the chapter), Ch.15 (DeMarre Equation), Ch.16 (Penetration Probability), Ch.17
(Tactics), Ch.19 (Gun Sight Magnification), Ch.20 (National Physics Lab Equation),
Appendix 5 (General Quality of Panther Armor), Appendices 1–4 and 6–9, and the
Errata Sheets.

**Not reached, either pass** — a genuine remaining gap, not claimed empty:
Appendices 10–19 (printed roughly pp.105–123: gun elevation/descent angle, German
armor acceptance testing, HE accuracy, ballistic tests, Soviet 122mm APBC data,
shot placement, precise slope equations, moving-target accuracy, German slope
curves, firing test validity) and the Bibliography. These are almost entirely
accuracy/dispersion modeling, not armor-thickness or K-factor data — lower
relevance to this project's current mechanics, but unread all the same.

## Finding 1: Real K-factors, for six of this project's seven unsourced-K guns

Printed pp.84–85 (Ch.18) has two full pages titled "BALLISTIC 'K' FACTORS" — a real
per-projectile table, not a formula. Matched against every "K-factor NOT sourced,
constrained least-squares" row in `guns.csv`:

| Project's gun | Project's MV (fps) | Old constrained-search K | Book's row (MV, K) | Verdict |
|---|---|---|---|---|
| `sixpdr_57l50_apcbc` | 2730 | 1495 | "6PR L52 APCBC", 2725, **2722** | Replaced |
| `sixpdr_57l50_apds` | 4000 | 1650 | "6PR APDS", 4000, **2828** | Replaced |
| `seventeenpdr_76l55_apcbc` | 2900 | 1971 | "17 PR APCBC", 2900, **1686** | Replaced |
| `seventeenpdr_76l55_apds` | 3950 | 1514 | "17Pdr APDS", 3950, **1705** | Replaced |
| `pak40_75l46_apcbc` | 2592 | 1954 | "75L46 APCBC", 2600, **2400** | Replaced |
| `pak40_75l46_apcr` | 3248 | 2356 | "75L46 APCR", 3247, **3395** | Replaced |
| `t70_45l46_apbc` | 2493 | 3613 | "45L46 APBC", 2493, **3613** | Exact match — confirms existing value |
| `usm1_57l50_ap` | 2800 | 2400 | — | No matching muzzle velocity in the book's table; still unsourced |

The book's own K-factor formula (printed p.83) — `Velocity(m) = MV × e^(range(m) ×
0.7 × -0.0000001 × K)` — is character-for-character the formula already in
`formulas.py`'s `velocity_at_range()`. The book's stated generic fallback exponent
(used when no fitted curve exists) is **1.4283**, the exact "rough confidence"
constant already hardcoded in `fit_gun_curve()`. Both independently confirmed
against the primary source rather than assumed correct.

Refitting all six replaced guns against their existing calibration data with the
book's own K values produced fits of comparable or better quality to the old
constrained-search guesses (max error changed by well under 0.1 percentage point
in every case — see design note E.133 for exact figures), and every resulting
exponent stayed within the project's own 0.8–3.0 physically-plausible band without
needing to be constrained. Historical sanity checks already in this project's test
suite (17pdr penetrating Tiger I hull front at 1000m; 6pdr's Auto-Pen/Contested/
Bounce progression at 100/500/1000m against the same target; PaK 40 penetrating
T-34 hull front at 500m) all still hold with the new K-factors.

## Finding 2: Ch.6 (Armor Flaws) directly answers the Sherman glacis QC question

`counters/toe/sherman_glacis_qc_1943.md` (an earlier pass this session) searched
multiple secondary sources for a Sherman-specific flaw statement and honestly
concluded none existed (design note E.126). It did — in this project's own primary
source, never read directly until now.

Ch.6 opens (printed p.28) with: **"Prior to October, 1943, American armor
production and quality control permitted flawed armor to occur in many tanks,
which includes almost all 56° glacis Shermans."** It then gives a worked numerical
example directly on the M4A1 (already in this roster): "The M4A1 had an all-cast
hull and mid-glacis armor was 51mm at 53°. Against 75mm APCBC, the M4A1 glacis
middle resistance with medium flaws would equal 51mm × 2.25 slope × 0.86 cast ×
0.93 flaw factor" → ~92mm equivalent, contrasted explicitly against "unflawed 2.5in
[63.5mm] at 47° glacis armor on Shermans produced after October 1943" → ~118mm
equivalent.

Ch.14's own reference table (printed p.69, "USA AFV") makes this concrete with
three separate M4-series glacis columns: **M4A1 (53° Glacis) — "All Flawed Cast"**;
**M4A3 (56° Glacis) — "All Flawed"**; **M4A3 (47° Glacis), 75mm gun — no flaw
label** (the post-fix design). This project's `Sherman M4A1 (75mm)` row was
`51mm@47°`, `cast=True`, no flaw — a hybrid of the book's pre-fix thickness and
post-fix angle, matching neither of its own two documented M4A1/M4A3 configurations,
with no independent citation for the 47° figure recorded anywhere in this project's
history. **Corrected** (design note E.133) to `51mm@53°`, `flaw_severity=medium`,
matching the book's own worked example on this exact vehicle. AV-vs-Capped (75mm
reference diameter) moves from 76.7mm to 79.7mm — the steeper angle's slope benefit
outweighs the flaw penalty, a real recalculation rather than a simple nerf. The
`M4A3 (76mm)` row's 64mm@47° glacis is unaffected and correctly remains unflawed —
it already represents the book's own post-October-1943 redesign.

A reprinted AFV News article ("Sherman Glacis Plate Update" by Phil Dyer) elsewhere
in the book corroborates the October 1943 date from a second angle within the same
volume: 56° fronts on both early cast (M4A1) and early welded hulls, with the
47°-front redesign arriving in 1944 production.

**This also resolves — by superseding — the earlier session's three-phenomenon
analysis in `sherman_glacis_qc_1943.md`.** That analysis was honest given what it
could reach (Livingston's own later internet forum posts, Wikipedia, aggregator
sites) — but the book those forum posts were written about had a fourth phenomenon,
a genuine discrete Sherman-glacis flaw statement with a specific date and a
vehicle-specific worked example, that no secondary source captured. See that file's
own addendum for the full account.

## Finding 3: Cross-validation of existing formulas — all confirmed accurate

- **Cast deficiency multiplier** (`cast_deficiency_multiplier()`, Ch.5 p.26): the
  book's printed formula `0.8063 + T×0.001238 - 0.0002628×D + (T/D)×0.02706` is
  character-for-character identical to `formulas.py`. Exact match, no correction.
- **Flaw multipliers** (Ch.6's "Small/Medium/Large Flaw Multipliers" charts): read
  directly; the values already in `formulas.py`'s `_FLAW_ANCHORS` match the
  charts' plotted curves closely, within normal hand-drawn-chart reading tolerance.
  No correction needed.
- **Tungsten slope multipliers** (`hvap76`/`hvap90`/`apds` in `slope_multiplier()`):
  computed at 30°/60° and compared against the book's "Tungsten Slope Effects"
  charts; all three land within ~5–10% of the charted values, consistent with a
  fitted exponential approximating a hand-drawn curve rather than a real
  discrepancy.

## Finding 4: a historical validation lead for the Soviet F-34, not yet used

Ch.13's general notes (printed p.60) quote correspondence with John Waters stating
the Soviet 76.2mm F-34 (already in this roster) "reportedly failed to penetrate the
Tiger E side hull and turret armor 'even at 200 meters'" in the April 1943 Kubinka
live-fire tests, failing again at 500m/60° or 100m/0° in September 1943 tests. A
real, dated data point that could feed a future Rule 18.12 matchup entry for the
F-34 if one is ever added — not acted on this pass.

## Finding 5 (pass 2): Top/Roof armor is not in this book at all — a clean negative

Pass 1 left open whether the German AFV table (never found) or the rest of Ch.14
might contain Top/Roof rows for Panther, Tiger, Panzer III/IV, StuG III, T-34, T-70,
or SU-85. Pass 2 found and read the complete German AFV table (pp.65–68: Panzer
III E/G/H/J/L/M, Panzer IV D/E/G/H/f1/f2, Panther D/A/G, Tiger E/B — Porsche and
Henschel, Jagdtiger, Jagdpanther, Hetzer, StuG IIIG, StuG IV, JgPz IV) alongside the
USA, Soviet, British, and Italian tables (pp.69–74, completing all four). **None of
these tables, for any vehicle in any nation, includes a Top/Roof armor row.** This
is a clean, confirmed negative — this project's still-open Top/Roof gaps
(`counters/toe/vehicle_top_armor_1943.md`) are not answerable from this book, full
stop, not merely "not yet checked." Future effort on that question should go
directly to Panzer Tracts (Pz III/StuG III) or a dedicated Soviet armor
encyclopedia, not back to this source — recorded as such in
`vehicle_top_armor_1943.md`'s own Open Questions.

## Finding 6 (pass 2): Tiger and Panther mantlet tables — one exact match, one confirmed-accurate-but-incomplete methodology, and a real limitation surfaced

**Ch.10, "Edge Hits on Tiger E Mantlet" (p.42)**, is the actual source table this
project's `vehicles.csv` cites for Tiger's Turret Front override. The 76mm-class row
reads **143mm** — an exact match to this project's existing `av_override_mm=143.0`.
The table also gives every other caliber against the same plate: 57mm→157, 85mm→139
(APBC family) or 142 (AP family), 90mm→139, 100mm→133 (APBC) or 135 (AP), 122mm→119
(APBC) or 121 (AP), 152mm→104 (APBC) or 105 (AP). **This project currently prints
one flat override value (143mm) regardless of the attacking gun's own caliber** —
accurate for the 76mm-class guns it was built around (17pdr, KwK40-class), but a
real, now-quantified approximation for anything else in this roster that might ever
be checked against Tiger's mantlet (the 57mm-class 6pdr would see 157mm, not 143mm
— a 10% difference; an 85mm-class Soviet gun would see 139mm). Recorded in
`vehicles.csv`'s own note as reference data; `resolve_av()`'s override mechanism
would need to accept a caliber-keyed table rather than one flat value to actually
use this — not built this pass, flagged as a real future extension.

**Ch.11, "Turret Hit Probability and Rounded Mantlets" (pp.43–45)**, confirms this
project's Panther angle-probability distribution exactly, to the tenth of a
percent: 65–75°=20.0%, 50–60°=31.2%, 35–45°=24.8%, 20–30°=14.4%, 0–15°=9.6%. But
this chapter gives hit-angle probabilities only, not a Tiger-style pre-computed
combined-resistance table for Panther — this project's own weighted-average
construction (design note E.118) remains the best available treatment, now
confirmed to be built on an accurate input distribution rather than an unverified
one, which is a real confidence upgrade even though the AV figure itself is
unchanged.

**A separate finding independently reconfirms an already-flagged Panther
uncertainty**: Ch.14 (p.66) lists Panther G's "Turret Front: 110c @ 10" as a row
**distinct from** "Mantlet: 100c rounded." Pass 1 already flagged this exact
two-row listing as a possible separate plate the project's 249.2mm mantlet-only AV
might understate; pass 2's independent second read found the same listing again,
ruling out a first-pass misreading. This is now a confirmed, real feature of the
primary source, not an artifact — still not chased down (how the two combine isn't
stated in either read), and still flagged rather than guessed at.

## Finding 7 (pass 2): Appendix 5 answers a different question than expected

Appendix 5, "General Quality of Panther Armor" (pp.93–94), is not the source of
this project's "~50% of production had some flaw severity" claim for Panther's
glacis — that statistic is in Ch.14's own table note (p.66: "About half of Panthers
with flawed glacis armor starting summer 1944"), now cited precisely in
`vehicles.csv` (design note E.134). Appendix 5 instead compares firing-test
penetration ranges against Panther's *non-glacis* areas (upper hull side, front
nose) at Isigny and elsewhere, concluding those areas were "equivalent to U.S. good
quality penetration test plate" — i.e. specifically **not** flawed, unlike the
glacis. A genuinely different, if related, finding — recorded rather than
conflated with the glacis statistic.

One dating wrinkle worth carrying forward: Ch.14's own flaw statistic is pinned to
production "starting summer 1944," while this roster dates Panther Ausf G to 1943
(Ausf G production itself historically began March 1944) — an existing project
convention, not something this pass changed, but the flaw statistic's own dating
sits right at the edge of that convention rather than comfortably inside it.

## Finding 8 (pass 2): two bonus corrections for British vehicles, and a confirmed-correct-but-mis-cited hit-probability table

The British AFV table (p.73) gives two exact angles `counters/toe/
british_vehicles_1943.md` had explicitly flagged as unsourced: **Churchill's lower
nose plate, 140mm at 20°** (resolving that file's own Open Question #3), and a
previously-unknown-to-this-project **Cromwell nose plate, 57mm at 20°** — which
conflicts with a separate, already-flagged weak figure (~25mm) in the same file and
isn't currently modeled as a distinct `vehicles.csv` row at all. See that file's own
2026-09-12 addendum for the full account; neither triggered a `vehicles.csv` value
change this pass (both need a design decision — a fuller multi-plate weighted
treatment for Churchill, and a decision on how to represent Cromwell's apparent
second plate — beyond what this reading pass alone should decide).

Separately, Appendix 6 (p.97) has a named maximum-hit-probability-by-crew-quality
table — Elite 90%, Veteran 85%, Experienced 80%, Regular 75%, Green 65%, Militia
50% — that turns out to be **already correctly used** in this project's own
`crew_quality_hit_cap()` (`formulas.py`), values matching exactly (down to folding
the source's unused "Experienced" band into Veteran, already commented as such).
The only error found was the citation itself: the code comment said "Ch.6/Appendix
7," corrected to "Appendix 6" (design note E.134). A nice independent confirmation
that this table was sourced correctly the first time, even though its citation
wasn't quite right.

## Confidence Notes

- **K-factor table (pp.84–85):** high confidence — a direct primary-source table
  read by the same agent that fitted the curves against it, not a secondhand
  citation. Six of seven target guns matched on muzzle velocity; the seventh
  (US M1 57mm AP Shot M70) simply isn't in this specific table.
- **Ch.6 Sherman finding:** high confidence — the opening sentence and the M4A1
  worked example were both read directly, and independently corroborated within
  the same book by Ch.14's own three-column USA AFV table and the reprinted AFV
  News article.
- **Formula cross-validations (Ch.5, Ch.6 charts, tungsten charts):** high
  confidence for Ch.5 (character-for-character formula match); moderate-high for
  the two chart-reading checks (hand-drawn charts read visually, not a printed
  table of exact values).
- **Pass 2 findings (Ch.10/11 mantlet tables, Ch.14 German/British/Italian AFV
  tables, Appendix 5, Appendix 6):** high confidence — each read directly and, in
  three cases (Tiger's 143mm, Panther's angle distribution, the crew-quality
  hit-probability table), independently confirmed an existing project value
  exactly rather than correcting it.
- **Coverage caveat, updated:** two passes now cover the large majority of the
  book's content-bearing chapters. Appendices 10–19 and the Bibliography remain
  unread — plausible but lower-relevance gaps (dispersion/accuracy modeling, not
  armor thickness or K-factors), not claimed to be checked.

## Open Questions / Gaps for Follow-up

1. **Appendices 10–19 and the Bibliography were not reached by either pass** —
   see the Coverage section above for what these appear to cover. Lower priority
   than what's already been read, since none of it appears to be armor-thickness
   or K-factor data, but a genuine remaining gap.
2. **US M1 57mm's K-factor remains unsourced** — no muzzle velocity in the book's
   own K-factor table matched the AP Shot M70's 2800 fps. The constrained
   least-squares methodology (design note E.129) stands as this row's only
   available approach unless a different source is found.
3. **Tiger's per-caliber mantlet table (Ch.10) is not yet built into the
   pipeline** — `resolve_av()`'s override mechanism only supports one flat value
   per plate; using the right figure for a 57mm or 85mm-class attacker against
   Tiger's mantlet (rather than reusing the 76mm-class 143mm figure) would need a
   caliber-keyed override table, a real but unbuilt extension.
4. **The separate Panther "Turret Front: 110c@10" plate is now confirmed real
   (seen twice, independently) but still not chased down** — how it combines with
   the 100mm mantlet figure isn't stated in either read of Ch.14.
5. **Churchill's middle glacis plate (57mm) still has no angle in any source
   checked** — the lower plate's angle is now known (140mm@20°, this pass), but a
   full 3-plate weighted treatment needs the middle plate's angle too.
6. **Cromwell's apparent second nose plate (57mm@20°, this pass) is not yet
   represented in `vehicles.csv` at all**, and conflicts with an already-flagged
   weak ~25mm figure from a different source — needs a design decision, not just
   more research, on how (or whether) to model it.
7. **A copy of Fletcher & Harley (2006), *Cromwell Cruiser Tank*, is now
   available in the project's reference material** — the natural next book to
   read, given it could resolve the Cromwell nose-plate conflict (#6), Churchill's
   own remaining Open Questions, and the general Churchill/Cromwell
   mantlet-weighted-treatment gap in one pass.
8. **Ch.2's slope-multiplier formulas were only ever spot-checked (pass 1), never
   exhaustively verified** — neither pass did a full read of this chapter's own
   worked examples. Worth doing before treating this project's
   `slope_multiplier()` as fully cross-validated rather than probably-correct.
