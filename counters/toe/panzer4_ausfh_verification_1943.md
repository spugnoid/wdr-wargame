# Perrett & Laurier, *Panzerkampfwagen IV Medium Tank 1936-1945* — Verifying Ausf H's Hull Front

Research pass reading Bryan Perrett (text) & Jim Laurier (cutaway art), *Panzerkampfwagen
IV Medium Tank 1936-1945* (Osprey Fighting Armor of WWII, Military Book Club edition,
1999, revised from the original 1983 *Vanguard 18*), in full (49 pages, image scan, no
OCR text layer), specifically to check the project's existing `Panzer IV Ausf H` Hull
Front figure (80mm@10°, not cast, face_hardened=True), currently flagged in
`vehicles.csv` as "widely-cited figure, not verified vs Panzer Tracts this session."

## Short answer: confirmed, and from an unusually good source — a labeled technical cutaway, not just narrative prose

This book (unlike the last two read this session) is Perrett's own full text, not a
photo-caption album, and it includes a detailed, numbered cutaway diagram of the Ausf H
specifically (pp.26-27, plate "D") with a printed component key giving real armor
callouts — the closest thing to a Panzer-Tracts-style spec diagram found in any book
read this session that wasn't itself a Panzer Tracts volume.

## Finding 1: Hull Front 80mm — confirmed twice, and confirmed as a single integral plate, not layered

**Body text (p.8)** describes the Ausf H's introduction (March 1943) directly: *"this
model not only had integral 80mm armour on the bow, front plate and mantlet, but also
5mm side skirts and a turret girdle as a defence against hollow-charge ammunition."*
The word **"integral"** is doing real work here — it is used specifically to contrast
the Ausf H's front armor against the *preceding* Ausf G's construction, which the same
book describes one paragraph earlier as achieved by *"transferring the saving [from
thinned side armour] to the vehicle's front armour in the shape of 30mm appliqué
plates."* **This is a real, sourced distinction between two Panzer IV variants' front-
armor construction methods**: Ausf G = base plate + 30mm bolt-on appliqué (a layered
composite); Ausf H = a single "integral" 80mm plate from the factory. A photo caption
(p.14) repeats the same characterization: *"The Ausf. H had 80mm integral front
armour."*

**The labeled cutaway diagram (pp.26-27) independently confirms the number twice**, in
two different named locations:
- Callout **1: "Front armour plate 80mm"** (the lower hull glacis).
- Callout **14: "80 mm superstructure armour plate"** (the upper hull front /
  driver's-compartment front, a physically distinct plate from the lower glacis on this
  vehicle's hull design, per the diagram's own separate numbering).

Both plates read 80mm. Neither callout, nor the body text, uses any bolt-on/appliqué/
layered language for the Ausf H specifically — a real, structural absence, not just an
oversight, given the same book uses exactly that language for the Ausf G one page
earlier. **This project's existing single-homogeneous-80mm-plate model for Ausf H's
Hull Front is correct as modeled**, and should NOT be treated with the same layered-
plate correction just applied to StuG III (design note E.138) — that correction was
specific to the Ausf-G-style bolt-on construction, which this book confirms the Ausf H
did not use.

## Finding 2: other plates — three more exact matches from the same cutaway

The same labeled diagram gives three more figures that match this project's existing
`vehicles.csv` data exactly:
- Callout **22/23: "30mm side armour on turret" / "50mm front armour on turret"** —
  matches this project's `Turret Side` (30mm) and `Turret Front` (50mm) rows exactly.
- Callout **50/51: "Side armour upper 30mm" / "Side armour lower 30mm"** — matches this
  project's `Hull Side` (30mm) row exactly.

No hull rear or turret rear figure was legible/labeled in the cutaway's own callout
list (the diagram's pointer lines for those areas were not included in the visible key,
or point to non-armor components) — this project's existing Hull Rear (20mm) and
Turret Rear (30mm) figures are **not contradicted**, simply not independently
re-confirmed by this specific source.

## Finding 3: one genuinely unclear callout, flagged rather than guessed at

Callout **3** in the same cutaway key reads **"20mm armour glasis plate"** (sic —
likely "glacis"). This number does not match any figure currently in this project's
data, and its exact physical location on the vehicle could not be confidently pinned
down from the diagram's pointer lines at this scan's resolution — it sits in the key's
list between "spare track links" (2) and "final drive inspection hatch" (4), suggesting
a position somewhere on the lower front hull, but whether it describes a distinct thin
transition plate, the hull floor/nose underside, or something else entirely was not
resolved this pass. **Not incorporated into any figure change** — flagged honestly as
an unresolved data point rather than guessed at, matching this project's stated
preference throughout this session.

## Finding 4: face-hardening — real, but for a different variant's plate than currently modeled

This project's `vehicles.csv` face_hardened=True for the Ausf H's Hull Front traces (per
an earlier design note this session) to Bird & Livingston Ch.3, which names Panzer IV
Ausf H specifically as retaining face-hardened armor at "thicker plates" beyond a
general 30-50mm 1942 policy bracket. This book's own **p.14** quotes a 1942 British
technical evaluation (Merz & McLellan) of a **captured Ausf E** (not H): *"Hardness
tests were carried out on a number of armour plates and it was concluded that they
were all of machinable quality **with the exception of the spaced armour plate over the
hull machine gun mounting**. The port armour covers and the hull machine gun mounting
were found to be face hardened."* This describes face-hardening localized to **small,
specific components** (the MG mounting and port covers) on an **earlier variant's
original armor**, not a blanket claim about the general glacis plate — a real,
citable, but *different* face-hardening claim than the one already backing this
project's Ausf H figure. The two are not necessarily in conflict (different variants,
different armor generations — the Ausf H's later, thicker 80mm plate could plausibly
have been face-hardened as a separate, later policy decision this 1942-dated Ausf E
evaluation wouldn't capture), but they are not the same claim, and this pass did not
find anything in this book that directly corroborates face-hardening for the Ausf H's
own 80mm integral plate specifically. Recorded as a real nuance, not a contradiction.

## Finding 5: Top/Roof armor — not found in this book either

No hull roof, turret roof, or floor thickness figure appears anywhere in this book's
text or its one detailed cutaway diagram — consistent with the pattern already
established this session (WWII Ballistics, the Cromwell book, the Panzer III photo
album all lacked this data too). This project's existing Panzer IV Top/Roof figures
(`counters/toe/vehicle_top_armor_1943.md`: Hull roof ~10mm medium confidence; Turret
roof 10mm→16mm reinforced, high confidence via a separate, already-cited Panzer Tracts
No.4 p.50 reference) are **not addressed by this pass**, and remain exactly as
previously documented.

## Confidence Notes

- **Hull Front 80mm, integral (not layered) construction: high confidence.** Confirmed
  by body text twice (pp.8, 14) and by the labeled cutaway diagram twice (callouts 1
  and 14) — four independent confirmations within one book, all consistent, and the
  book's own explicit contrast against the Ausf G's bolt-on construction makes this a
  positive, structural finding, not just an absence of contrary evidence.
- **Turret Front/Side, Hull Side: high confidence** — direct, labeled cutaway callouts,
  all three matching this project's existing figures exactly.
- **Callout 3 ("20mm armour glasis plate"): low confidence, unresolved** — a real
  printed figure in the source, but its exact referent could not be confirmed at this
  pass's scan resolution.
- **Face-hardening: moderate confidence that a real, citable face-hardening claim
  exists in this book, low confidence that it directly corroborates this project's
  existing Ausf H claim** — the two describe different variants/plates and were not
  reconciled this pass.

## Open Questions / Gaps for Follow-up

1. Callout 3's "20mm armour glasis plate" should be re-examined with a higher-
   resolution scan or a version of this book with clearer diagram callouts, to
   determine what plate it actually describes and whether it represents a real,
   previously-unknown thin secondary plate on the Ausf H's front hull.
2. Whether the Ausf H's 80mm integral front plate was itself face-hardened (as opposed
   to the Ausf E's earlier, localized face-hardening of the MG mounting/port covers
   only) was not independently confirmed by this book — the existing Bird & Livingston
   Ch.3 citation remains this project's only direct support for that specific claim.
3. Panzer IV's Top/Roof armor gap is untouched by this pass — still resting on the
   existing secondary-sourced (~10mm hull roof) and Panzer-Tracts-cited (turret roof,
   already high confidence) figures documented in `vehicle_top_armor_1943.md`.
