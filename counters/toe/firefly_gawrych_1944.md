# Sherman VC Firefly — Wojciech J. Gawrych, *Sherman VC Firefly* (Armor PhotoGallery #13)

## Sources

- Wojciech J. Gawrych, *Sherman VC Firefly*, Model Centrum PROGRES, "Armor
  PhotoGallery #13," 78pp. Image-scan PDF, no OCR text layer — read via direct
  page-image inspection, not `pdftotext`.
- A walkaround/modeler's photo-reference book (two preserved museum vehicles:
  Brussels and Axvall) plus a running-text "PhotoHistory" section (pp.63-80).
  Not a combat-narrative or unit-history book.
- This pass targets the same two open questions `firefly_fletcher_2008_1944.md`
  (design note E.142) was dispatched for and could not resolve: the mantlet
  "+13mm" claim's provenance, and the three historical vignettes' (Wittmann
  engagement, Tilly-sur-Seulles, Norrey-en-Bessin) true source.

## Findings

### 1. Mantlet "+13mm" claim — not found (second clean negative)

The mount-evolution text (p.73) covers only the standard M34→M34A1 mount's
pre-Firefly thickening history in general Sherman terms. No dimensioned
Firefly-specific mantlet figure appears anywhere in the book. This project's
existing Turret Front `av_override_mm` (102mm, the M4A1's 89mm plus the sourced
"+13mm" delta) remains **narrowed, not resolved** — a second specific candidate
source has now been read in full and ruled out.

### 2. Three historical vignettes — not found (third clean negative)

The PhotoHistory section (pp.63-80) covers different units/regiments than the
ones named in the vignettes and contains no tactical combat narrative of any
kind. Their true source remains unidentified across all three books checked so
far (Fletcher 1997, this book).

### 3. Hull rear plate angle — new, actionable finding

Caption 54 states the hull rear plate is sloped **20 degrees from vertical**,
specifically on the M4A4/M4A6 hull (the Firefly's donor hull is M4A4). This
project's existing `vehicles.csv` Hull Rear row carried a flat 0-degree angle,
sourced only by inference-by-extension from other Sherman rows (which do not
themselves establish an angle for the M4A4 rear plate specifically). Applied:
angle corrected to 20 degrees; thickness (38mm) remains the pre-existing
inference-by-extension figure, not newly confirmed by this source.

### 4. Other findings (not applied — flavor/cross-check only)

- Base M4 turret casting: 76mm front / 51mm sides+rear / 25mm top (caption
  128) — this is the base casting figure, not a Firefly-specific mantlet
  delta; does not bear on the open Turret Front question.
- Radio bustle box: 64mm rear / 51mm sides / 25mm top-bottom (p.78) — a second
  independent source for the bustle, mildly disagreeing with the project's
  existing 62mm-rear figure (Sherman Minutia). Within plausible rounding/
  measurement-convention variance; not applied, since the existing figure
  already has one specialist citation and this would just substitute one
  single-source figure for another without resolving which is more precise.
- 25mm sponson appliqué plate confirmed, with a build note that it is a
  Chrysler-built M4A4/M4A6 feature specifically, not a universal Firefly trait.
- Ammo stowage: same 77-round total, described with a different positional
  breakdown than Fletcher 1997 — likely the same physical bins described at
  different granularity, not a contradiction.
- Production data: monthly 1944 conversion table, and a 288-Fireflies-by-
  24-June-1944 figure independently corroborating Fletcher 1997's identical
  figure (cross-source agreement, not a new fact).
- False-muzzle-brake disguise measure independently corroborated by a second
  source (Fletcher 1997 already recorded this).

## Confidence Notes

- Findings 1 and 2 are honest non-findings: exhaustive within this book's
  scope (full 78-page read), not evidence the claims are false, only that this
  specific title is not their source.
- Finding 3 (hull rear angle) is a direct, captioned, dimensioned statement in
  a specialist modeler's reference — the kind of source this project treats as
  reliable for individual armor figures even without independent
  corroboration, consistent with how single-specialist-source figures (e.g.
  the radio bustle 51mm/62mm figures) have been treated elsewhere in this file
  history.
- This is the second Firefly-specific book read this session (after Fletcher
  1997) to independently corroborate the 288-by-24-June-1944 figure —
  increasing confidence in that number for scenario-design use, though it
  remains flavor/context rather than an armor-stat question.

## Open Questions

1. Mantlet "+13mm" claim's true source remains unidentified — two candidate
   books (Fletcher 1997, this book) now ruled out. The 2008 Osprey New
   Vanguard 141 (Fletcher) remains the next best candidate, still unread.
2. The three historical vignettes' true source remains unidentified — same two
   candidates ruled out.
3. Hull rear plate thickness (38mm) is still unconfirmed for the M4A4
   specifically — only the angle was resolved by this pass.
4. Radio bustle rear thickness has two disagreeing specialist figures (62mm
   Sherman Minutia vs. 64mm this book) — not resolved, flagged for a future
   pass if a third source becomes available.
