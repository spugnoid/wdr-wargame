# Vehicle Top (Deck/Roof) Armor — Technical Data, 1943 Roster

Research pass only. No AV/PEN numbers are computed here. This file gathers raw,
cited horizontal top-armor data (hull deck/engine deck/hull roof, and turret
roof where a turret exists) for all 14 vehicles currently in
`counters/armor_calc/data/vehicles.csv`, none of which have any top-armor rows
yet. Existing Hull/Turret Front/Side/Rear data for these vehicles is already
in `vehicles.csv` and is not repeated here.

Per this project's own culture: where no citable figure was found, that is
stated explicitly as **not found** rather than filled in with a plausible-
looking guess. Several figures below are genuinely contested between sources
— both figures are given, with a stated preference and reason, not a silent
average.

## Sources

- Jentz, Thomas L. & Doyle, Hilary L. *Panzer Tracts No. 4: Panzerkampfwagen
  IV — Grosstraktor to Panzerbefehlswagen IV* (p. 50, turret roof
  reinforcement) and *Panzer Tracts No. 4-3: Panzerkampfwagen IV Ausf. H /
  Ausf. J 1943 to 1945* (not accessed directly; corroborating citation on
  tanks-encyclopedia.com). The authoritative primary source for Pz IV
  variants; also exists for Pz III (*Panzer Tracts No. 3-3*) and StuG III
  (*Panzer Tracts No. 8*) but neither of those two volumes' actual page text
  was accessible this session — searched for, not found.
- Jentz, Thomas L. & Doyle, Hilary L. *Germany's Tiger Tanks: D.W. to Tiger I
  — Design, Production & Modifications* (Schiffer, 1993), pp. 8, 16 — cited by
  Wikipedia's "Tiger I" article for the 25mm→40mm turret roof thickening.
- Hart, Stephen. *Sherman Firefly vs Tiger: Normandy 1944* (Osprey, 2007), p.
  17 — secondary corroboration of Tiger's baseline 25mm top armor.
- panzerworld.com, "Pz.Kpfw. Panther" armor table — gives production Panther
  (D/A/G) hull roof and turret roof both as 16mm, contrasted with the
  unbuilt Panther II project's 1 Nov 1943 spec (30mm hull/turret roof).
- Wikipedia, "Panther tank" — https://en.wikipedia.org/wiki/Panther_tank
  (states rear hull top armor as 16mm, citing "Doyle"; no separate turret
  roof line or thickening claim found in retrievable body text).
- Tank Archives (Peter Samsonov), tankarchives.com — several posts:
  - "Panther's Ins and Outs" (transcribing a British Canadian Military HQ
    London technical-intelligence comparison of captured Panther Ausf D/A vs.
    Ausf G, archival ref RG 24 C 2, ~May 1944, via Warspot.net/LAC): states
    the front 30cm of Ausf G's hull roof was thickened to 40mm (was 15mm on
    D/A), floor 26mm (was 18mm).
  - "T-34 Improvements, 1943": 1943 Soviet production-simplification order
    consolidating hull roof plate from a nominal 13–16mm to a standardized
    20mm.
  - "T-34 Protection Trials" (CAMD RF F.38 Op.11355 D.332 L.1-90, Soviet
    commission report dated 25 April 1941): pre-1943 roof plate documented as
    ~16mm ("parts of air intake caps protrude above the 16mm thick roof");
    also the source for the top-armor-penetrated-by-fire incident below.
  - "KV on a Diet" (GOKO Decree #1334ss, 23 February 1942, archival ref
    RGASPI 644-1-22): orders KV-1S's removable roof elements, turret roof,
    and hatches reduced to 30mm as part of the weight-reduction program.
  - "Improved T-34-85 Armour" (GKO Decree #5690s, 20 April 1944, plus a
    Beria/Malyshev/Fedorenko memo): T-34/85 turret wall thickness (front/side,
    not roof) by factory — context only, dated April 1944, outside this
    project's 1943 bracket.
  - "SU-85 Requirements" (CAMD RF 81-12038-246, dated 13 April 1943): states
    SU-85's armor configuration was unchanged from the SU-122 chassis it was
    based on, but does not itself state a roof figure.
- historyofwar.org (Rickard) — full armor tables for Panzer III Ausf M,
  Panzer IV Ausf H, and StuG III Ausf G, each including Top/Bottom rows, but
  none with a specific inline citation beyond a general "further reading"
  reference at the page bottom (Bryan Perrett for Pz III; Stephen Hart for
  Pz IV and StuG III). Treated as weak/secondary throughout.
- tanks-encyclopedia.com — Panzer IV Ausf H and StuG III Ausf G pages,
  corroborating the turret-roof reinforcement claim (Pz IV) and giving a
  10–16mm top-armor range (StuG III) without a citation cleanly attached to
  that specific sentence.
- theshermantank.com — "Medium Tank (M4A1 Mid war)" and "Medium Tank
  M4A3(76)W HVSS" GENERAL DATA/ARMOR spec-sheet PDFs. Per the site author's
  own note, these are his cleaner retyping of the armor data tables printed
  in the back of R.P. Hunnicutt's *Sherman: A History of the American Medium
  Tank* (the site author states Hunnicutt's own printed appendix tables are
  poorly typeset, hence the retype). No independent page number recoverable,
  but the content and format is Hunnicutt's appendix data.
- Wikipedia, "Churchill tank" — https://en.wikipedia.org/wiki/Churchill_tank
  (body text states Mk VII hull top 13.3mm and turret roof 20mm verbatim;
  fresh check this session found neither figure has a direct inline citation
  in the surrounding paragraph, which cites White 1983 generally).
- Wikipedia, "Cromwell tank" — https://en.wikipedia.org/wiki/Cromwell_tank
  (states overall armor range "8mm to 76mm thick" without attributing the
  8mm figure to a specific plate; no turret-roof or hull-top-specific line
  found in the current article at all).
- `counters/toe/british_vehicles_1943.md` (this project, prior session) —
  existing Churchill/Cromwell top-armor figures, re-checked this session (see
  per-vehicle notes below for what changed).
- Wikipedia, "T-34" and "T-70" — https://en.wikipedia.org/wiki/T-34 ,
  https://en.wikipedia.org/wiki/T-70_tank (T-70's "roof and bottom: 10mm"
  line confirmed via raw wikitext fetch to carry **no** `<ref>` tag despite
  being widely repeated across secondary tank wikis).
- Wikipedia, "SU-85" — infobox armor field is itself tagged `{{clarify}}` in
  the raw wikitext (confirmed by direct fetch), i.e. Wikipedia's own editors
  flag that figure as ambiguous.
- panzernet.net and IL-2 Sturmovik: Great Battles museum pages — uncited
  hobby/game-reference sources for KV-1S, included only to document
  disagreement, not trusted as primary.
- armouredfightingvehicle.fandom.com — uncited hobby wiki for Panzer III Ausf
  M, included only to document disagreement; could not be independently
  re-fetched this session (HTTP 402 on retry).

## German Vehicles

### Panzer III Ausf M

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull/superstructure top | 16–18mm (candidate range; historyofwar.org gives Turret Top-Bottom 10mm / Superstructure Top-Bottom 18mm / Hull Top-Bottom 16mm; a hobby wiki gives 10mm roof-front, 15mm roof-back, 18mm turret roof instead) | historyofwar.org (Rickard); fandom hobby wiki (uncorroborated) | **Low — genuinely disputed, treat as TBD** |
| Turret roof | 10mm vs. 18mm — direct disagreement between the two sources above | Same as above | **Low — genuinely disputed, treat as TBD** |

**Not resolved.** Neither source traces to a page number in *Panzer Tracts No.
3-3: Pz.Kpfw.III Ausf.J, L, M & N* (Jentz/Doyle), the actual authoritative
primary source for this variant, which was not accessible this session.
Recommend leaving both plates as an explicit gap in `vehicles.csv` rather
than picking one of the disputed figures.

### Panzer IV Ausf H

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull roof/floor | ~10mm (front hull); tanks-encyclopedia and historyofwar suggest a slightly thicker ~11–12mm zone in places, without cleanly separating front-hull-roof from engine-deck | Wikipedia infobox (cites Chris Conners' *AFV Database*, a secondary aggregator); corroborated in ballpark by tanks-encyclopedia.com and historyofwar.org | **Medium** — three independent sources converge on ~10mm, but none is a page-cited primary source |
| Turret roof | **10mm on early Ausf H production, reinforced mid-production to 16mm and 25mm segments** | **Jentz & Doyle, *Panzer Tracts No. 4*, p. 50** (verified full citation in Wikipedia's own bibliography); independently corroborated by tanks-encyclopedia.com's citation of the dedicated *Panzer Tracts No. 4-3* volume for this exact vehicle | **High** — the single best-cited figure found across this entire research pass |

Recommend modeling the turret-roof change as a real, dated mid-production
event if the ruleset's data model supports sub-variant timing; otherwise use
the reinforced 16–25mm figure as representative of 1943-production Ausf H
(most 1943 output postdates the reinforcement) with a note that early-1943
vehicles may have run the thinner 10mm.

### StuG III Ausf G

Casemate vehicle — no turret, only hull/superstructure roof applies.

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull deck (lower hull) | 15–16mm (historyofwar: 16mm; tanks-encyclopedia's own separate spec table: 15mm) | historyofwar.org; tanks-encyclopedia.com | **Low-Medium** |
| Superstructure (fighting compartment) roof | 10–17mm (tanks-encyclopedia body text: "10 and 16mm"; its own spec table: "10–16mm"; historyofwar: 17mm) | Same as above | **Low-Medium** |

Wikipedia's own StuG III article, despite citing Jentz & Doyle's *Panzer
Tracts No. 8: Sturmgeschütz* elsewhere for other claims, gives **no** roof/top
figure at all. tanks-encyclopedia's 10–16mm figure sits near a citation to
*Panzer Tracts No. 8* but the citation is not clearly re-attached to that
specific sentence — could not confirm the attribution. Treat the whole
10–17mm range as an approximate, secondary-sourced band, not a confirmed
primary-source figure.

### Panther Ausf G

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Turret roof | 16mm — same across Ausf D/A/G, no confirmed thickening for the production tank | panzerworld.com armor table, contrasted against the *unbuilt* Panther II project's 30mm spec (1 Nov 1943 design document) | **Medium-high** — consistent across variant, but no page-numbered primary citation obtained |
| Hull roof, front 30cm strip only | **40mm on Ausf G** (was 15mm on Ausf D/A) | British Canadian Military HQ London technical-intelligence report, ~May 1944, archival ref RG 24 C 2, transcribed by Tank Archives ("Panther's Ins and Outs," citing Warspot.net/LAC) | **High** for this narrow claim — a dated wartime technical-intelligence document, but only covers a 30cm-wide front strip, not the whole hull roof |
| Hull roof, remainder (engine deck) | 16mm (undifferentiated by variant in this source) | Wikipedia, "Panther tank," citing "Doyle" | **Medium** — no page number retrieved, does not confirm this applies specifically to Ausf G vs. D/A |

**Popular claim NOT confirmed:** the widely-repeated idea that Panther's
turret roof was thickened to 30–40mm (often attributed to vulnerability to
aircraft attack) does **not** appear to apply to the actual mobile,
turreted tank. It traces instead to two different things: (1) the never-built
Panther II project's 30mm spec, and (2) the static "Pantherturm"/Panther
bunker fortification (a real Panther turret welded onto a concrete
emplacement for the Atlantic Wall/Gothic Line), whose roof was separately
thickened to 65mm against plunging artillery fire specifically because it
was a fixed target (thearmorylife.com). **Recommend NOT coding a
thickened-turret-roof figure into `vehicles.csv` for the mobile Panther Ausf
G** — current evidence says the production tank turret stayed at 16mm.

This project's own design-spec notes record a prior session's transcription
of Bird & Livingston Ch.14's "Armor Data for Selected Vehicles" table for
Panther (Hull Rear, Turret Side/Rear, Mantlet, Turret Front — all already in
`vehicles.csv`), but **no Top/Roof row was recorded from that pass**, and the
book's actual page text could not be retrieved via web search this session.
Flag as genuinely unconfirmed whether Ch.14 even includes a roof line, not
as "the book doesn't have one."

### Tiger I Ausf E

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull top (roof+floor, undifferentiated) | 25mm | Wikipedia, "Tiger I," citing Jentz & Doyle 1993 pp. 8, 16, and Hart 2007 p. 17 | **High** |
| Turret roof | **25mm, increased to 40mm from March 1944** | Same as above | **High** — specific, dated, dual-sourced (a named primary reference plus a secondary Osprey corroboration) |

Wikipedia's phrasing ("top and bottom armour was 25mm") lumps hull roof and
floor together and does not distinguish front-hull roof (over the driver's
compartment) from the engine deck — treat 25mm as a single figure covering
the whole hull top, not two separately-sourced plates. Since this project's
Tiger I Ausf E row is dated 1943, the pre-March-1944 baseline (25mm turret
roof) is the applicable figure for this specific vehicle/era; the 40mm
figure is real but out of era for this roster entry.

Same Bird & Livingston Ch.14 caveat as Panther: this project's existing
notes on Ch.14's Tiger data reference only the Ch.10 mantlet edge-effect
table, not a Top/Roof row — unconfirmed whether the book's table includes
one.

## Soviet Vehicles

### T-34 Model 1943 (76mm gun)

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull roof | **20mm** | Tank Archives, "T-34 Improvements, 1943," transcribing a 1943 Soviet production-simplification order explicitly consolidating prior 13–16mm roof sheets to a standardized 20mm plate | **Medium-high** — a real, dated archival production order, though not a plate-by-plate spec sheet |
| Turret roof (hexagonal turret) | **Unresolved — do not use either figure found** | One uncited hobby/museum site (il2sturmovik/aergistal) claims 56mm cast, uniform with the turret walls; this conflicts with the general Soviet-turret convention of a much thinner roof plate and with an uncited Wikipedia "20mm" infobox line for the earlier Model 1941 turret | **Low — genuinely uncertain, flag as TBD rather than picking either number** |

Context: a 1941 Soviet armor-trials commission report (CAMD RF F.38
Op.11355 D.332 L.1-90, 25 April 1941) independently confirms the pre-1943
nominal roof was thinner (~16mm — "air intake caps protrude above the 16mm
thick roof"), consistent with the 1943 order's statement that 13–16mm sheets
were being replaced by 20mm ones. This corroborates 20mm as the correct
1943-production figure rather than an artifact of Wikipedia's general 1941-
era infobox rounding.

### T-34/85 (late 1943 variant)

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull roof | **Not found** — candidate figures of 20mm, 16mm, and 15mm circulate across secondary sites, none traceable to an archival document or a specific book page this session | Various uncited secondary/tertiary tank-wiki pages | **Unsourced — do not guess** |
| Turret roof | **Not found** | Same | **Unsourced — do not guess** |

What IS well-sourced for this vehicle, but is turret **wall** thickness (not
roof, and already reflected in `vehicles.csv`'s existing Turret Front/Side
rows) and is dated outside this project's stated 1942-43 era bracket: GKO
Decree #5690s (20 April 1944) documents the original factory #112 turret at
52mm front/sides being superseded by an improved factory #183 turret at
90mm front / 75mm sides. Included here only for context/consistency
checking, not as a top-armor figure.

### T-70 light tank

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull roof and bottom | **10mm** | Wikipedia, "T-70 tank," body text ("roof and bottom: 10mm") | **Medium** — widely repeated verbatim across multiple independent secondary sites (militaryfactory.com, Wargaming wiki, forum posts), suggesting a common real ultimate source (very likely Zaloga & Grandsen, *Soviet Tanks and Combat Vehicles of World War Two*, 1984, given how that book's figures propagate on tank wikis) — but a direct raw-wikitext fetch confirmed this specific sentence carries **no** `<ref>` tag in Wikipedia itself, so the citation chain to a page number could not be closed this session. |
| Turret roof | **Not found** — not reported separately from the hull "roof and bottom" figure anywhere located | — | **Unsourced** |

### KV-1S

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Turret roof and removable hull roof panels | **30mm** | **GOKO Decree #1334ss, 23 February 1942, archival ref RGASPI 644-1-22**, transcribed by Tank Archives ("KV on a Diet") — a genuine dated Soviet government decree ordering the weight-reduction redesign that produced the KV-1S, explicitly specifying "reduction of removable roof elements, turret roof, and hatches to 30mm" | **High** — the single strongest primary-source citation found for any Soviet vehicle in this pass |

**Disagreement:** two uncited hobby/game sources (panzernet.net;
IL-2 Sturmovik: Great Battles museum page) claim a thicker **40mm** for part
of the roof (disagreeing with each other on whether it's the turret roof or
the forward hull roof specifically), with neither citing a source. Prefer
the GOKO decree's 30mm figure — it is a primary archival document directly
about this exact redesign, whereas the 40mm claims are uncorroborated and
internally inconsistent about which plate they even describe.

### SU-85

Casemate vehicle — no turret, only hull/superstructure roof applies.

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull/superstructure roof | **Not found — the weakest-sourced vehicle in this entire research pass** | — | **Unsourced, do not guess** |

Wikipedia's own SU-85 infobox armor field carries a `{{clarify}}` tag in the
raw wikitext — Wikipedia's own editors flag the single armor value given
(45mm) as ambiguous, and that value is stated in body text to refer to the
sloped front plate, not the roof, anyway. Tank Archives' SU-85 articles
(Requirements, Production, Long Awaited Tank Destroyer, Proposed
Modernization) were checked directly; the closest relevant statement
("SU-85 Requirements," CAMD RF 81-12038-246, 13 April 1943) says only that
armor configuration was "unchanged" from the SU-122 chassis it was based on,
without stating a roof number for either vehicle. A secondary web summary
claimed 30mm, but this could not be traced to any specific citable page —
**not used.**

## American Vehicles

### Sherman M4A1 (75mm gun)

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull top | **19.1mm to 12.7mm (0.75in to 0.5in), at 90°–83° from vertical** — a single gradient figure, thicker toward the front, thinning toward the rear/engine deck (Hunnicutt's table format, not split into separately-named sub-rows) | theshermantank.com "M4A1 Mid war" and "M4A1 Early" GENERAL DATA spec sheets, both retyped from R.P. Hunnicutt's *Sherman: A History of the American Medium Tank* appendix tables. Identical across the "Early" and "Mid" (1943-relevant) production spec sheets. | **Medium-high** — content is Hunnicutt's own data, though no independent page number recoverable from a retyped table |
| Turret roof (small 75mm turret) | **25.4mm (1.0in), at 90°** | Same source | **Medium-high** |

No conflicting figures found; other secondary discussion (War Thunder
forums, aggregator sites) independently converges on the same numbers.

### Sherman M4A3 (76mm gun)

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull top | **19.1mm (0.75in), at 83°–90°** | theshermantank.com "M4A3(76)W HVSS" GENERAL DATA spec sheet, same Hunnicutt-derived provenance | **Medium** — see caveat below |
| Turret roof (T23 turret) | **25.4mm (1.0in), at 90°** | Same source | **Medium-high** — consistently 1in/25.4mm across secondary aggregator pages too, no conflicting figure found |

**Caveat:** the specific spec sheet found is labeled for the later,
HVSS-suspension M4A3(76)W; this project's roster vehicle is the earlier
(1943/early-1944), VVSS wet-stowage M4A3(76)W. Suspension type does not
affect hull/turret roof armor — only running gear — so the figures should
carry over, but no VVSS-specific spec sheet was found to independently
confirm the Hull Top / Turret Roof lines are unchanged between the two
sub-variants. Treat as "very likely correct, not independently
double-sourced for the exact 1943 sub-variant."

## British Vehicles

Both vehicles already have top-armor figures in
`counters/toe/british_vehicles_1943.md` (marked "included for completeness
only" there, without a detailed inline citation). This session re-checked
both against the live Wikipedia articles.

### Churchill Mk VII

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull top | **13.3mm** (existing figure, reconfirmed) | Wikipedia, "Churchill tank," body text verbatim: "The hull top [was] 0.525 in (13.3mm)" | **Medium** — figure holds up unchanged on a fresh check, but the surrounding paragraph's citation (White 1983, per a general section reference) is not attached as a direct inline cite to this specific sentence |
| Turret roof | **20mm** (existing figure, reconfirmed) | Wikipedia, "Churchill tank," body text verbatim: "The turret roof was 0.79in (20mm) thick" | **Medium** — same caveat as above |

Downgrade both from the previous file's implied "Fletcher-cited" status to
"reconfirmed in Wikipedia's own prose, but not directly inline-cited to
Fletcher or White specifically for these two roof numbers" — nothing
contradicts the existing figures, but the citation strength for the
roof/top lines specifically is weaker than for the well-cited hull/turret
front-side-rear figures already in `vehicles.csv`.

### Cromwell Mk IV

| Plate | Thickness | Source | Confidence |
|---|---|---|---|
| Hull top | **Not found** — genuine gap, confirmed still missing on a fresh check | — | **Unsourced, do not guess** |
| Turret roof | 20mm figure carried in the existing project file — **could NOT be reconfirmed on the live Wikipedia article this session** | `counters/toe/british_vehicles_1943.md` (prior session); not found in current Wikipedia "Cromwell tank" body text or infobox on a fresh direct fetch | **Downgraded to unverified — flag for follow-up, do not treat as settled** |

Fresh check found Wikipedia's Cromwell article states only that overall
armor ranged "8mm to 76mm thick" without attributing the 8mm figure to any
specific named plate — it is plausible this is the actual hull-top/roof
figure, but since the article does not say so explicitly, **do not backfill
8mm as the hull-top value; it would be an inference, not a citation.** The
existing file's "20mm Turret Roof" for Cromwell could not be traced to
anything in the current live article text — it may derive from a
now-edited-out version of the page, or (a real risk) may have been a
same-as-Churchill copy-paste assumption from a prior session rather than a
genuine Cromwell-specific figure. Recommend treating Cromwell's turret roof
as unconfirmed pending a direct look at Fletcher & Harley (2006), neither
of which is accessible in this environment.

## Historical Top-Armor Penetration by Ground Fire (not aircraft)

One well-documented, on-point incident/finding was located:

- **Tank Archives, "T-34 Protection Trials"** (CAMD RF F.38 Op.11355 D.332
  L.1-90, a Soviet armor-vulnerability commission report dated **25 April
  1941**, examining two production T-34 hulls/turrets): the commission's
  findings state verbatim that *"the roof of the hull needs to be
  reinforced, as it can be penetrated by shells ricocheting off the curved
  turret or broken by HE shells blowing up on the turret."* The same report
  series describes an HE detonation against the lower turret shockwave-
  cracking the ~20mm turret roof and blowing out the turret floor, and
  separately a hit on the rear turret ring breaking through both the
  fighting-compartment roof and turret-bay floor, throwing the turret off
  the hull entirely.
- This is a genuine, archivally-cited **test/analysis** report (a
  vulnerability trial, not a battlefield anecdote), but it is squarely
  on-point for "top armor defeated by HE/artillery-type fire, not aircraft"
  and concerns the T-34 lineage directly (pre-1943 hull, but the same
  hexagonal-turret top-armor design carried into the 1943 model in this
  roster).
- No comparable incident was found for any of the other 13 vehicles within
  the limited search time budgeted for this question. One promising lead
  — a tanks-encyclopedia.com article titled "1942 Combat Damage Analysis of
  the T-34 and T-70 Tanks" — could not be fetched (the site returned HTTP
  403) and was not pursued further per instructions not to chase this hard.
  Worth revisiting if this question becomes a priority later.
- Nothing was found for the German, American, or British vehicles beyond
  general abstract discussion (e.g. Sherman roof vulnerability to top-attack
  weapons in the abstract, on Sherman-fan forums) with no named, sourced
  incident attached.

## Confidence Notes

- **Best-cited figures in this entire pass, safe to use directly:**
  Panzer IV Ausf H turret roof (Jentz & Doyle, *Panzer Tracts No. 4* p.50);
  Tiger I Ausf E hull top and turret roof (Jentz & Doyle 1993 + Hart 2007);
  KV-1S turret roof / removable hull roof panels (GOKO Decree #1334ss, 23
  Feb 1942); T-34 Model 1943 hull roof (Tank Archives' 1943 archival
  simplification order); Panther Ausf G's narrow 40mm front-hull-roof-strip
  claim (dated British wartime technical-intelligence report).
- **Genuinely unresolved — do not guess, flag as TBD in `vehicles.csv`:**
  Panzer III Ausf M (both hull top and turret roof — disputed 2x between
  sources with no primary tiebreaker); StuG III Ausf G (both plates —
  10–17mm range, no clean primary citation); T-34 Model 1943 turret roof
  (56mm claim uncorroborated and inconsistent with normal Soviet turret-roof
  design); T-34/85 (both plates — not found at all); T-70 turret roof (not
  reported separately anywhere); SU-85 (the single weakest-sourced vehicle
  in this whole pass — Wikipedia's own editors flag its one armor figure as
  ambiguous); Cromwell Mk IV hull top (not found) and turret roof (existing
  20mm figure could not be reconfirmed this session — treat as weakened,
  not as still-solid).
- **Popular claim explicitly investigated and NOT confirmed:** Panther's
  turret roof being thickened to 30–40mm on the actual mobile tank — this
  traces instead to the unbuilt Panther II project and/or the static
  "Pantherturm" bunker emplacement, neither of which is the vehicle in this
  roster. Do not code a thickened figure into `vehicles.csv` on the strength
  of this popular claim.
- **Bird & Livingston Ch.14 ("Armor Data for Selected Vehicles"):** this
  project's other files show this table was previously used for Panther and
  Tiger side/rear/mantlet data, but neither this session nor the prior
  session's notes confirm whether the table's own printed page (p.66,
  per `vehicles.csv`'s Panther notes) includes a Top/Roof row at all — the
  book's actual text could not be accessed this session (only prior
  transcriptions in this project's own design-spec notes were available).
  This is a genuine "haven't checked the primary source directly" gap, not
  evidence the book lacks the data.
- **Sherman M4A1/M4A3 top armor:** the best sourcing found (Hunnicutt via
  theshermantank.com's retyped spec sheets) is solid in content but weak in
  exact page-citation terms, since it's a retype rather than a scan of the
  original book pages.

## Open Questions / Gaps for Follow-up

1. *Panzer Tracts No. 3-3* (Pz III), *No. 4-3* (Pz IV, beyond the p.50
   citation already found), and *No. 8* (StuG III) were not directly
   accessible this session — a dedicated look at these (Jentz/Doyle) would
   likely resolve the Panzer III and StuG III top-armor disputes.
2. **RESOLVED 2026-09-12, design note E.134 — a clean negative, not a gap.**
   A direct read of Bird & Livingston's own Ch.14 "Armor Data for Selected
   Vehicles" (the book itself, not a secondhand transcription) found the
   complete German, USA, Soviet, British, and Italian AFV tables (pp.65–74).
   **None of these tables — for any vehicle in this project's roster or
   otherwise — includes a Top/Roof armor row at all.** This is a clean,
   confirmed negative: Panzer III/StuG III/T-34/T-70/SU-85 top armor (items
   1, 3, 4, 6, 7 below) is not answerable from this book, full stop, not
   merely "not yet checked here." Future effort on any of those should go
   straight to the sources those items already name (Panzer Tracts, a
   Zaloga & Grams or Solyankin/Pavlov Soviet title) rather than back to
   this one. See `counters/toe/wwii_ballistics_direct_read_1943.md` for the
   full read.
3. T-34/85's own top armor (both hull and turret roof) is a real, unresolved
   gap — candidate figures exist (15–20mm range) but none traced to a
   citable source. A Zaloga & Grams title or a Solyankin/Pavlov Soviet armor
   encyclopedia volume would likely resolve this; neither was accessible
   this session.
4. SU-85's top armor is entirely unsourced — same recommendation as above
   (a dedicated Soviet SPG reference, not general Wikipedia/Tank Archives
   searching, is probably needed).
5. Cromwell Mk IV's hull top figure remains unfound, and its turret roof
   figure (carried in the existing British vehicles file) could not be
   reconfirmed. **Update 2026-09-12, design note E.137: Fletcher & Harley
   (2006), *Cromwell Cruiser Tank*, has now been read directly, in full
   (50 pages) — a clean negative, not a gap.** This is a production/
   organizational/service-history monograph, not an armor-specification
   reference: it has no hull/turret thickness-and-angle table anywhere,
   for Cromwell or any other vehicle, the same pattern already confirmed
   for *WWII Ballistics*'s Top/Roof gap (item 2 above). It also could not
   confirm this project's own existing "76.7mm, Fletcher & Harley 2006
   p.12" citation for Cromwell's turret front — p.12 as read has no
   armor figure at all, flagged in `vehicles.csv`'s own note as a real,
   unconfirmed citation rather than disproven. Cromwell's hull top/turret
   roof, its nose-plate conflict, and the Churchill/Cromwell mantlet-
   weighted-treatment question all remain open. A Panzer-Tracts-style
   detailed technical reference, not a general-history Osprey monograph,
   is now the more promising lead for British plate geometry, by the
   same pattern observed twice in this project's library. See
   `counters/toe/cromwell_churchill_fletcher_harley_1943.md` for the
   full read.
6. The tanks-encyclopedia.com article "1942 Combat Damage Analysis of the
   T-34 and T-70 Tanks" returned HTTP 403 this session and was not pursued
   — it's a plausible source for more historical top-armor-penetration
   incidents if that question becomes a priority.
7. T-34 Model 1943's turret roof (hexagonal turret) needs a real primary
   source — the two figures found (20mm vs. 56mm) are far enough apart that
   guessing between them would be worse than leaving it blank.
