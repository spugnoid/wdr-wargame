# Fletcher & Harley (2006), *Cromwell Cruiser Tank 1942-50* — Does It Answer the Cromwell/Churchill Armor Geometry Questions?

Research pass reading Fletcher & Harley, *Cromwell Cruiser Tank 1942-50* (Osprey New
Vanguard 104, 2006), in full (50-page image-only scan, no OCR text layer — read as
images in three batches: pp.1-15, 16-30, 31-45, 46-50), specifically to check whether
it resolves eight open questions about Cromwell and Churchill armor-plate thickness/
angle carried by `counters/toe/british_vehicles_1943.md` (with its 2026-09-12
addendum), `counters/toe/vehicle_top_armor_1943.md`, and the current
`vehicles.csv` rows for `Churchill Mk VII` and `Cromwell Mk IV`.

## Sources

- Fletcher, David & Harley, Richard, *Cromwell Cruiser Tank 1942-50* (Osprey New
  Vanguard 104, 2006) — full 50-page body read directly (image scan).
- Prior project files consulted before this read: `british_vehicles_1943.md` (incl.
  its 2026-09-12 addendum), `vehicle_top_armor_1943.md`, current `vehicles.csv` rows.

## Short answer: this is a production/organizational/service-history monograph, not an
## armor-specification reference — none of the 8 questions get a numeric answer

The book's structure (Genesis → Cavalier Described → Cavalier Production → Enter
Rolls-Royce → Cruiser Mark VIII A27M Cromwell → Marks and Types tables → gun
performance table → Welded Cromwells → Going West → Trials and Tribulations →
Wartime Variants (Command/OP/ARV/AA/Dozer) → A30 Challenger → A30 Avenger →
A34 Comet → post-war/export tables → FV4101 Charioteer → Conclusion → Bibliography →
Colour Plate Commentary → Index) is overwhelmingly about manufacturers, Mark/Type
lineage, WD serial-number ranges, unit assignments, gun/performance tables, and
variant descriptions. It never presents a hull/turret armor-thickness-and-angle
table of the kind Bird & Livingston's *WWII Ballistics* has for other nations. This
mirrors that book's own confirmed absence of Top/Roof armor data (see
`vehicle_top_armor_1943.md`) — a second real monograph, on-topic by title, that
simply does not carry the granular plate geometry this project needs.

The closest the book comes to armor-construction detail is general prose in the
Genesis/Cavalier-Described section (pp.9-11): the hull front and visor plates "were
made up from two thinner plates" bolted together, and the hull sides were "also
double layered... with the Christie suspension units sandwiched between the inner
and outer plates." This describes a lamination/construction *method* shared across
the whole Cavalier/Centaur/Cromwell family, not a per-model thickness-and-angle
figure for any specific plate, and is not tied to a specific mm/degree value in the
text as read. Churchill is not covered in this book at all — it is a strictly
different vehicle family (Vickers-designed infantry tank vs. this book's Christie-
suspension cruiser-tank family), and the book contains no Churchill data whatsoever.

## Findings by Question

**1. Cromwell nose/lower-glacis plate (57mm@20° vs. main 64mm@0° plate) — NOT
RESOLVED.** No distinct nose-plate thickness/angle figure was found anywhere in the
book. The only related content is the general "two thinner plates" lamination note
above, which describes construction method, not a separate angled lower plate. The
57mm@20° vs. 64mm@0° conflict flagged in `british_vehicles_1943.md`'s addendum
remains unresolved by this source.

**2. Churchill middle-glacis plate angle — NOT COVERED.** Churchill is entirely
outside this book's scope; it is not mentioned as a subject anywhere except as a
size/role comparison point implied by the cruiser-vs-infantry-tank design
philosophy discussion in the Genesis section. No Churchill armor data at all.

**3. Cromwell turret front (76.7mm cited to "this book p.12" vs. 64mm from a weaker
source) — NOT RESOLVED, and the citation itself could not be confirmed.** Page 12
falls within the "Cruiser Mark VIII A27M Cromwell" introductory section as read;
it contains general design/production narrative, not a turret-armor thickness
figure. No 76.7mm or 64mm turret-front figure was found on p.12 or anywhere else in
the book. This project's existing `76.7mm` citation to "Fletcher & Harley 2006 p.12"
should be treated as unconfirmed by this direct read — the number may come from a
misattribution, a different edition/printing with different pagination, or a
figure the image-scan legibility obscured. No definitive correction is offered;
the conflict stands exactly as before, now with the added caveat that this read
could not independently verify either side of it.

**4. Cromwell hull side/rear (currently 32mm, flagged as ranging 29-44mm, possibly
two spaced plates) — NOT RESOLVED.** The "sides were also double layered... with
the Christie suspension units sandwiched between the inner and outer plates" note
(Genesis section, ~p.9-11) is suggestive of a spaced/laminated side construction
consistent with the "two spaced plates" theory already flagged as a possibility in
this project's existing notes, but the book gives no thickness figures for either
layer, so it cannot confirm which of the 29-44mm range of secondhand figures is
correct, nor whether 32mm represents one layer or a combined figure.

**5. Cromwell hull top and turret roof — NOT FOUND.** No Top/Roof armor thickness
appears anywhere in the book, consistent with the same clean negative already
confirmed for Bird & Livingston's national AFV tables (`vehicle_top_armor_1943.md`,
Open Question #2, resolved 2026-09-12). This is now a second independent
confirmation that published Osprey/reference-tier sources in this project's
library simply don't carry top-armor figures for Allied cruiser tanks; a technical
manual or a Panzer-Tracts-style detailed-drawings reference remains the more
likely place to find this, not general-history monographs.

**6. Mantlet-weighted treatment geometry for Cromwell/Churchill turret fronts — NOT
PROVIDED.** No mantlet-specific thickness or shape data for either vehicle. The
book's colour-plate commentary (pp.45-47) describes turret *markings and external
stowage* in detail for several named vehicles/variants but never armor geometry.

**7. Crew quality/training bonus — NOT COVERED AS A RATEABLE FIGURE.** The book
contains service-history color commentary (e.g., "The Poles used their armour with
considerable verve. In debatable areas they tended to advance with all guns
blazing..." — Colour Plate Commentary, C2, 1st Polish Armoured Division, p.46) but
this is narrative color, not a quantifiable elite/veteran/regular rating comparable
to the sourced tables this project uses elsewhere (e.g., Bird & Livingston's
Appendix 6). No usable crew-quality bonus for either vehicle.

**8. Real, dated combat anecdote, ideally 1943-44 — PARTIALLY FOUND, with caveats.**
Two combat-relevant vignettes appear in the Wartime Variants / production-history
section (pp.31-45 as read): one describing Cromwell vulnerability to mines, and one
describing a Cromwell that "survived five direct hits from a 75mm PaK 40 at 274m."
**Neither anecdote's exact page number, precise date, or unit was captured with
full confidence during this pass** — the image-scan legibility and the density of
surrounding production-table text made it difficult to pin an exact citation for
these two items specifically, and this file is being honest about that rather than
guessing at a page/date to make the citation look more complete than it is. The
Villers-Bocage engagement (June 1944, 4th County of London Yeomanry, A1/24
Hussars) appears only as an index entry and photo caption reference (index p.48;
Taylor, Daniel, *Villers-Bocage Through the Lens* is listed in the Bibliography),
not as in-text narrative with dated combat detail suitable for direct citation. If
this project wants to use the PaK 40 survival anecdote for a Rule 18.12 entry, it
would need a second, more targeted pass through pp.31-45 specifically hunting for
that citation's exact page and unit, rather than being taken from this summary.

## Confidence Notes

- **High confidence**: the book contains no numeric armor-thickness/angle table for
  either Cromwell or Churchill anywhere in its 50 pages — this was a full read, not
  a sample, across three complete passes.
- **High confidence**: Churchill is entirely absent from this book's scope.
- **Medium confidence**: the "two thinner plates" / "double layered... Christie
  suspension sandwiched" construction notes are accurately paraphrased from the
  Genesis section, but their exact page number was not precisely re-verified in
  this final synthesis and should be treated as "early book, pp.9-11 region" rather
  than a pinned citation.
- **Low confidence**: the two combat anecdotes (mine vulnerability; PaK 40
  survival) are real content in the book, but their exact page/date/unit were not
  captured precisely enough during the read to cite confidently — flagged as
  needing a follow-up targeted re-read if the project wants to use them.

## Open Questions / Gaps for Follow-up

1. All 8 directive questions remain open after this read. This project's Cromwell/
   Churchill armor-geometry gaps are not resolved by any source currently in the
   reference library that has been read directly (WWII Ballistics: no Top/Roof,
   no British national table depth beyond what's already in `vehicles.csv`; this
   Cromwell monograph: no plate-geometry table at all).
2. The Cromwell turret-front 76.7mm citation to "Fletcher & Harley 2006 p.12"
   could not be confirmed by this direct read — worth flagging to whoever
   originally entered that citation, in case it was transcribed from a different
   source or edition.
3. The PaK 40-survival and mine-vulnerability anecdotes are real and potentially
   useful for a future Rule 18.12 entry, but need a dedicated re-read of pp.31-45
   to pin down exact page/date/unit before they can be cited properly.
4. A Panzer-Tracts-style detailed technical reference (not a general-history
   Osprey monograph) is now the more promising lead for Cromwell/Churchill plate
   geometry, by the same pattern already observed for Top/Roof data across two
   consecutive monographs in this project's library.
