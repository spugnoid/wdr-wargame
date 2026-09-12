# Bird & Livingston, *WWII Ballistics: Armor and Gunnery* — First Direct Read

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

Read: Introduction, Ch.2 (slope multipliers, spot-check), Ch.5 (cast deficiency,
in full), **Ch.6 (Armor Flaws, in full)**, Ch.12 (compound angle), Ch.13
(Penetration Data intro, Soviet/K-factor tables), Ch.14 (USA AFV and Soviet AFV
tables), Ch.18 (Projectile Velocity Estimation, both K-factor table pages).

**Not reached this pass** — genuine gaps for a follow-up read, not claimed to be
checked: Appendix 5 ("General Quality of Panther Armor," printed p.93), the German
AFV table in Ch.14 (Panther/Tiger/Panzer III/IV/StuG III), and explicit Top/Roof
armor rows for Panther/Tiger/T-34/T-70/SU-85 (the two Ch.14 tables actually read —
USA AFV, Soviet AFV — don't have Top/Roof rows at all; they may exist elsewhere in
Ch.14's roughly 14 printed pages, unreached this pass).

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
- **Coverage caveat:** this was a targeted, prioritized read of a 234-page book,
  not a cover-to-cover pass. Chapters/appendices not reached (Appendix 5, the
  German AFV table, roughly half of Ch.14) may contain further corrections or
  data this project hasn't yet applied.

## Open Questions / Gaps for Follow-up

1. **Appendix 5 ("General Quality of Panther Armor," p.93) and the German AFV
   table in Ch.14** were not reached this pass — the German AFV table in
   particular could plausibly contain Top/Roof rows or K-factor-adjacent data for
   Panther, Tiger, Panzer III/IV, and StuG III that would help close this
   project's still-open top-armor gaps (`counters/toe/vehicle_top_armor_1943.md`).
2. **The remainder of Ch.14** (roughly half its ~14 printed pages) was not read —
   worth a dedicated follow-up specifically hunting for Top/Roof armor rows on any
   vehicle, which neither of the two tables checked this pass had at all.
3. **US M1 57mm's K-factor remains unsourced** — no muzzle velocity in the book's
   own K-factor table matched the AP Shot M70's 2800 fps. The constrained
   least-squares methodology (design note E.129) stands as this row's only
   available approach unless a different source is found.
4. **Ch.2's slope-multiplier formulas were spot-checked, not exhaustively
   verified** — a fuller read of this chapter's own worked examples (beyond the
   single check done this pass) would be worth doing before treating this
   project's `slope_multiplier()` as fully cross-validated rather than
   probably-correct.
