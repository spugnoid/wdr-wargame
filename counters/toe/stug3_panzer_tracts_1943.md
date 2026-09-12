# Jentz & Doyle, *Panzer Tracts No.8: Sturmgeschütz — s.Pak to Sturmmörser* — Does It Answer StuG III's Top-Armor and Construction Questions?

Research pass reading Thomas L. Jentz (assembled) & Hilary Louis Doyle (scale
prints), *Panzer Tracts No.8: Sturmgeschütz — s.Pak to Sturmmörser* (Darlington
Productions, 1999/2000), pp.8-1 through 8-39 (the full Pz.Sfl.III/Sturmgeschütz
Ausf.A-G and Sturmhaubitze Ausf.G lineage — image-scan, no OCR text layer, read
directly as images). The book continues beyond p.8-39 into other vehicle types
(the title's "s.Pak to Sturmmörser" scope suggests StuG III/IV derivatives,
tank destroyers, and the Sturmmörser Tiger) — not read this pass, since this
project's own open question is specifically about the StuG III gun-tank
lineage (Ausf.A through G), which is fully covered in the pages read.

## Sources

- Jentz, Thomas L. & Doyle, Hilary Louis, *Panzer Tracts No.8: Sturmgeschütz —
  s.Pak to Sturmmörser* (Darlington Productions, copyright 1999/2000) —
  pp.8-1 through 8-39 read directly (image scan, no text layer).
- Prior project files consulted first: `counters/toe/vehicle_top_armor_1943.md`
  (StuG III Ausf G's current top-armor status, "Low-Medium" confidence,
  10-17mm range) and `counters/armor_calc/data/vehicles.csv` (StuG III Ausf G's
  current Hull Front/Side/Rear rows).

## Finding 1: the Ausf.G's 80mm glacis IS a layered 50mm+30mm composite — a real, clear-text answer to an open question

This project's own `vehicles.csv` note for `StuG III Ausf G` Hull Front
explicitly considered and rejected treating the 80mm glacis as a layered
50mm-base+30mm-applique composite "since no source confirms StuG III Ausf G's
specific 80mm glacis was built this way," leaving it unflagged pending a
source that "specifically addresses StuG III's own glacis construction."

**This book is that source.** Page 8-26, introducing the Ausf.G production
model, states plainly (clearly legible body text, not a diagram callout):
**"Frontal armor protection remained at 50 mm base plate with 30 mm
face-hardened plates bolted on."** This is a direct, unambiguous statement
that the Ausf.G's 80mm nominal front is a two-layer construction — a 50mm
base plate with a separately-hardened 30mm appliqué plate bolted to it — not
a single homogeneous 80mm plate. This matches the exact "layered
50mm-base+30mm-applique" construction this project's own note already
considered and correctly declined to guess at without a source. It also
matters for `face_hardened`: only the 30mm applique layer is described as
face-hardened, not the full 80mm thickness, which is a real distinction from
simply marking the whole plate `face_hardened=True` the way the existing
`StuG III Ausf G` Hull Side row already does.

This is corroborated by earlier-page production narrative (p.8-18, Ausf.F/8):
"Sturmgeschuetz Ausf.F (Fgst.Nr.91284 completed by Alkett in early August
1942) with 30 mm plates welded to the basic 50 mm front plates" — confirming
the 50mm-base-plus-30mm-appliqué pattern was already established practice
before the Ausf.G, not a one-off Ausf.G description. Multiple photo captions
across pp.8-15 through 8-29 independently describe "30-mm-thick additional
armor plates bolted to the 50-mm-thick plates" as a running theme across
Ausf.D/E/F/F8/early-G production, strengthening confidence this is a real,
well-documented construction detail, not a single offhand remark.

## Finding 2: Top/Roof armor — the book has per-variant labeled diagrams, but not for the plain-gun Ausf.G specifically, and digit legibility is a real limitation

The book includes a dedicated "Armor Specifications" side-profile diagram
with labeled thickness/angle-from-vertical callouts for the Sturmgeschütz
**Ausf.A** (p.8-6), **Ausf.C-E** (shared diagram, p.8-10), and **Ausf.F/8**
(p.8-23) — each showing the fighting-compartment/superstructure roof as a
raised box at the top of the profile with its own thickness/angle label,
separate from the hull sides and front.

**Reading these labels precisely was not fully possible at this scan's
resolution** — the callout numbers are small, dense, and this is an
honest limitation, not a claim of precision I don't have. My best reading
of the Ausf.F/8 diagram (p.8-23) is that the two raised roof-area boxes are
labeled in the range of **"16mm" at a steep angle (roughly 78-90° from
vertical, i.e. near-flat)** — but I cannot rule out the actual digit being
18 rather than 16, or a different pairing of the visible digits, given
image legibility. This is directionally consistent with (not a precise
confirmation or contradiction of) this project's existing secondary-sourced
10-17mm band for StuG III's superstructure roof — it does not obviously
contradict the existing range, but I would not treat it as a confirmed,
precise correction either.

**Critically, no dedicated "Armor Specifications" diagram exists for the
plain gun-armed Ausf.G** in the pages read — the book jumps from the
Ausf.F/8 diagram (p.8-23) through Ausf.G production/photo narrative
(pp.8-26 through 8-34, several pages of photos and undimensioned scale
outline drawings) directly to a *different* vehicle's spec diagram: the
**Sturmhaubitze (10.5cm-howitzer) Ausf.G** (p.8-35), which shares the
Ausf.G's chassis and superstructure but mounts a different weapon. This is
a real, structural gap in even this authoritative primary source's own
coverage — the specific "gun-armed StuG III Ausf.G" row this project's
roster models never gets its own labeled armor-spec page in this book. The
Ausf.F/8 diagram (immediate predecessor, same base chassis before the
Ausf.G's roof/superstructure changes) and the Sturmhaubitze Ausf.G diagram
(same chassis/superstructure as the gun-armed Ausf.G, different turret-top
weapon fitting) are the closest available proxies, neither an exact match.

Page 8-26's own text confirms the Ausf.G's roof geometry is *more complex*
than earlier variants, not simpler: it introduces "the sloped middle section
of the roof with the raised commander's cupola" as a new Ausf.G-specific
feature — meaning a single flat roof-plate simplification, if ever modeled,
would be a real approximation for this specific variant, similar in kind to
Churchill's already-flagged stepped-glacis complexity, not a clean single
number.

## Finding 3: hull deck/floor — not found in the sections read

No hull-bottom/floor thickness figure was found in the text or diagrams for
any StuG III variant in the pages read. This project's existing 15-16mm
secondary-sourced figure for this plate remains unconfirmed by this pass.

## Finding 4: cross-check of existing Hull Side/Rear (30mm, face-hardened) — not contradicted, not independently re-confirmed with a page-specific citation

The 30mm hull side/rear figure already in `vehicles.csv` is broadly
consistent with the production-history narrative read (30mm appliqué plates
are a running theme, as above), but I did not find a single clean sentence
stating "hull side armor is 30mm" the way the frontal-armor sentence on
p.8-26 was clearly stated. Treat the existing figure as uncontradicted, not
freshly re-verified to a specific page.

## Confidence Notes

- **The 50mm+30mm layered front-armor finding: high confidence.** This is
  clearly legible body text (p.8-26), independently corroborated by
  production narrative and photo captions across multiple earlier pages
  (pp.8-15 through 8-24) describing the same 30mm-bolted-to-50mm pattern for
  the immediately preceding Ausf.D/E/F/F8 variants.
- **Roof thickness readings from the diagrams: low-moderate confidence.**
  A real limitation of this specific scan's resolution, not a claim the
  book lacks this data — the diagrams exist and are structured exactly as
  needed, but I could not read the small numeric callouts with full
  confidence. A higher-resolution scan or a second, more targeted pass
  zoomed on just these diagram regions would likely resolve this.
- **The missing dedicated Ausf.G armor-spec diagram: high confidence** —
  I read pp.8-23 through 8-39 directly and this gap in the book's own page
  sequence is clearly there, not a page I skipped.

## Open Questions / Gaps for Follow-up

1. **A higher-resolution read of pp.8-6, 8-10, 8-23, and 8-35's four
   "Armor Specifications" diagrams**, specifically targeting the roof-area
   callout numbers, would likely settle the StuG III top-armor question
   with real primary-source precision — this pass's resolution wasn't
   sufficient to read them with full confidence.
2. **This project should decide whether to apply the confirmed 50mm+30mm
   layered-front-construction finding** to `StuG III Ausf G`'s Hull Front
   row — this project has an existing formula precedent for exactly this
   kind of layered plate (`layered_plate_effective_thickness()`, already
   used for Panzer III's own hull front per the existing `vehicles.csv`
   note), so applying it here would be consistent with established
   methodology, not a new mechanism.
3. **The plain gun-armed Ausf.G's own roof geometry (a "sloped middle
   section," per p.8-26) was not diagrammed with dimensions anywhere found
   in this pass** — the closest proxies (Ausf.F/8's flatter predecessor
   roof, or the Sturmhaubitze Ausf.G's shared-chassis roof) are each a real
   approximation, not an exact match, if a number is needed before a better
   source is found.
4. **Pages 8-40 onward were not read** (Sturmgeschütz IV, s.Pak derivatives,
   Sturmmörser, and whatever else the book's full title scope covers) — not
   relevant to this project's current StuG III Ausf G question, but flagged
   for completeness in case a future need arises (e.g. if this project ever
   adds StuG IV or another derivative to its roster).
5. **Hull deck/floor thickness was not found** in the pages read.
