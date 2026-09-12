# Sherman Firefly — Technical Data (1944 addition, outside the 1943 baseline)

Research pass only. No AV/PEN numbers are computed here. This file gathers raw,
cited inputs for a **1944-dated** roster entry: the British 17-pounder conversion
of the M4 Sherman (Sherman VC on an M4A4/"Sherman V" hull, or Sherman IC on an
M4 Composite hull). The vehicle entered British service ~January 1944 and first
saw combat in Normandy from June 1944 — it is deliberately dated/labeled as a
1944 addition, not folded into this project's usual 1943 roster.

Scope note: the 17-pounder gun itself (APCBC and APDS) is **already fully
modeled** in `guns.csv`/`gun_calibration.csv` (`seventeenpdr_76l55_apcbc`,
`seventeenpdr_76l55_apds`). This file only covers the vehicle side (hull/turret
armor, ammunition availability timing, and historical validation data) — see
also `counters/toe/british_vehicles_1943.md`'s existing (admittedly thin)
"Sherman Firefly" section and its own Confidence Notes/Open Questions, which
flagged this exact follow-up as needed (its own item 6).

## Sources

- Wikipedia, "Sherman Firefly" — https://en.wikipedia.org/wiki/Sherman_Firefly
  (raw wikitext infobox pulled directly; "Design"/"Armament"/"Service" sections
  read in full, with footnote-to-reference tracing done this session)
- Fletcher, David (2008). *Sherman Firefly*. Osprey New Vanguard 141. ISBN
  978-1-84603-277-6. (Not accessed directly — this is the specific source
  Wikipedia's Firefly article cites [ref 5] for the "+13 mm mantlet" claim; a
  specialist single-subject monograph, the strongest single citation chain
  traced this session, but only reached at second hand via Wikipedia's own
  footnote, not read directly. **Correction, 2026-09-12, design note E.142:
  a PDF in the project's reference material labeled "Sherman VC M4A4
  Firefly (David Fletcher)" was read directly this session and turned out
  NOT to be this book — its own copyright page reads 1997, publisher
  Darlington Productions ("Military Ordnance Special No. 19"), a different,
  earlier Fletcher title on the same subject. This 2008 Osprey New Vanguard
  141 book remains unread and is still the best candidate for the "+13mm"
  claim's real source — see the addendum below for what the 1997 title
  actually contained.**)
- Wikipedia, "M4 Sherman variants" — https://en.wikipedia.org/wiki/M4_Sherman_variants
  (M4A4/"welded, lengthened hull" description, Chrysler A57 multibank engine,
  M4 Composite cast-front/welded-rear description)
- Wikipedia, "M4 Sherman" — https://en.wikipedia.org/wiki/M4_Sherman (raw
  wikitext infobox, used only as a cross-check that the Firefly infobox's
  "89 mm maximum" turret-front figure is NOT a copy-pasted generic Sherman
  number — the base M4 Sherman infobox instead gives a wide 12.7–177.8 mm
  "depending on location and variant" range, so the Firefly's 89 mm figure
  is at least Firefly-specific text, even though it carries no citation of
  its own)
- The Sherman Tank Site (theshermantank.com):
  - "The Firefly VC" variant page — https://www.theshermantank.com/the-sherman-tank-variant-page-pages-for-each-type-of-sherman-tank/the-firefly-vc/
  - "small hatch hull" category page — https://www.theshermantank.com/category/small-hatch-hull/
  - "#3 The Sherman Variants: The Design Matures" — https://www.theshermantank.com/sherman/the-sherman-variants-the-design-matures/
  - This is a well-regarded enthusiast/reference site that draws heavily and
    explicitly on R.P. Hunnicutt's *Sherman: A History of the American Medium
    Tank*, but the specific pages fetched this session did not themselves
    reproduce Hunnicutt's own numeric tables verbatim — treat as
    Hunnicutt-informed secondary, not a direct primary quote, except where
    noted.
- Sherman Minutia (the.shadock.free.fr), a specialist Sherman-modeling
  reference site, credited in its own text to researchers Kurt Laughlin and
  Adrian Barrel:
  - "Sherman Firefly tanks" — http://the.shadock.free.fr/sherman_minutia/firefly_tank/index.html
  - "Sherman Firefly turrets" — http://the.shadock.free.fr/sherman_minutia/firefly_turret/firefly_turret.html
  - Source of the specific radio-bustle-box thickness figures (51 mm sides /
    62 mm rear) and of the "muzzle brake, not a barrel counterweight" and
    "modified M34A1 mount" findings below.
- RC Universe forum thread ("Sherman Glacis angle question") and TheMiniaturesPage
  thread ("Why Do We Never Hear About the Sherman's Sloped Glacis?"), used only
  to corroborate the "56° small-hatch / 47° large-hatch, both measured from
  vertical" terminology convention — forum-level corroboration, not a primary
  citation, flagged accordingly below.
- AK-Interactive, Tasca/Asuka kit reviews (modelingmadness.com,
  perthmilitarymodelling.com, track-link.com, scalehobbyist.com) — used only
  for the turret "cast cheek armour" feature, cross-referenced across five
  independent hobby/review pages that agree with each other on the mechanism
  and timing (a general Sherman-turret "Quickfit" casting change, not a
  Firefly-specific one — see §2 below).
- Web-search synthesis (unnamed underlying pages, could not be individually
  re-traced this session) for the "APDS did not appear in Firefly stowage
  until August 1944" claim and for a "700 m vs 800 yd" range comparison on the
  Wittmann engagement — flagged explicitly as weaker, aggregator-level
  evidence wherever used below.

## 1. Hull variant: M4A4 ("Sherman V") confirmed as the standard conversion base

**Confirmed, multiple corroborating sources:** the M4A4 hull was the standard/most
numerous Firefly conversion basis. The Sherman Tank Site's dedicated Firefly VC
page states it was "the most common version of the Firefly since it was the
Brits[']  most numerous lend-lease Sherman." Sherman Minutia's Firefly page
lists three conversion bases — Sherman I (M4) → Sherman Ic, Sherman I Hybrid
(M4 Composite) → Sherman Ic Hybrid, Sherman V (M4A4) → Sherman Vc — and treats
the letter suffix "c" as simply meaning "17-pdr armed," implying the M4A4-based
Vc as the headline/default naming. A small number of Canadian-built Grizzly
(M4A1-based) Fireflies were also built, per Wikipedia, but used for training
only and never saw combat.

**Not resolved this session:** an exact numeric breakdown of how many of the
total ~2,100–2,200 converted Fireflies (total itself described by one source
as inconsistent across documents — "contradictory totals" was the language
used) were M4A4 vs. M4 vs. M4 Composite based. No source found this session
gives a percentage or count split by hull type.

### Hull front / glacis: small-hatch, NOT large-hatch

The Sherman Tank Site's "small hatch hull" category page states explicitly:
**"The A4 version never got the improved large hatch hull or T23 turret with
the M1 gun."** M4A4 production ran only 1942–September 1943, entirely within
the small-hatch production era. This means the Firefly's M4A4-based hull glacis
is the **earlier, small-hatch riveted/welded glacis, not the later large-hatch
one** — distinct from this project's existing "Sherman M4A3 (76mm)" row, whose
64 mm@47° glacis is explicitly the *later*, large-hatch, wet-stowage-era plate.

Per forum-level corroboration (RC Universe, TheMiniaturesPage — both citing
the "56°/47° from vertical" convention, not independently re-verified against
Hunnicutt's own tables this session): the small-hatch glacis is commonly
described as **51 mm (2 in) at 56° from vertical** ("the 56-degree hull"),
vs. the later large-hatch glacis at **64 mm (2.5 in) at 47° from vertical**
("the 47-degree hull," thickened specifically to compensate for the shallower,
less-protective angle needed to fit the larger new hatches). This is internally
consistent with the project's own existing M4A3(76mm) row (64 mm@47°) being the
*large-hatch* case — so by that same logic, the Firefly/M4A4's *small-hatch*
figure should be **51 mm at 56° from vertical**, not 47°.

**Flagged for whoever builds the CSV row:** the project's existing "Sherman
M4A1 (75mm)" row also uses a "47°" figure (51 mm@47°, cast), but that is a cast
rounded-nose hull, not a welded small-hatch plate hull — the "47°" there is a
separate simplification for the curved cast glacis's representative angle, from
a different construction method and (presumably) different original sourcing.
Do not assume the Firefly's small-hatch 56° figure and the M4A1's cast 47°
figure should match just because both are "early Sherman" hulls — they appear
to be genuinely different numbers for genuinely different hull constructions,
per the sources checked this session.

**Construction — welded, not riveted:** Wikipedia's "M4 Sherman variants"
article and the Sherman Tank Site both describe the M4A4 hull as **welded**
("welded, lengthened hull," per Wikipedia). This is worth flagging explicitly
because a "riveted, Chrysler multibank engine" framing was floated as this
task's own starting assumption — the sources found this session do not support
"riveted" as the M4A4's hull construction. (A distinct, much smaller batch of
the very earliest M4 — not M4A4 — hulls used riveted glacis-plate jointing in
1942; this is a different vehicle and does not appear to be what most Firefly
conversions, which used M4A4 hulls, were built from.) Flagged as a correction
against the task's framing rather than a confirmed "riveted" figure.

### Hull side / hull rear

**Not independently confirmed for the M4A4 specifically** in any source found
this session. All sources checked describe hull side/rear armor only in
general "standard Sherman" terms (commonly 38 mm / 1.5 in), without calling out
the M4A4 by name. Given that this figure is already identical across both of
this project's existing Sherman rows (M4A1: 38 mm side, 38 mm rear; M4A3:
38 mm side, 38 mm rear) and is consistently repeated across every general
secondary source checked, treating **38 mm side / 38 mm rear** as very likely
correct for the M4A4-based Firefly as well — but this is an inference by
extension from the pattern already in this project's own data plus general
Sherman literature, not a source that names the M4A4 specifically. Genuinely
open, not a settled figure.

## 2. Turret modifications: standard M4 turret, reused (not redesigned)

All three main sources checked (Wikipedia, Sherman Tank Site indirectly,
Sherman Minutia's dedicated Firefly-turret page) independently converge on the
same story: the **standard M4 Sherman turret casting was retained and modified**,
not replaced with a new design. Sherman Minutia's turret page states this
directly: "The standard M4 Sherman turret was quite heavily modified to fit
with British requirements," and lists exactly four changes:

1. The 75 mm gun replaced by the 17-pdr, with "a particular recoil system,
   designed especially for the Sherman turret" (Wikipedia's Design section adds
   detail: recoil cylinders were shortened and moved to both sides of the gun,
   and the gun cradle itself was shortened — engineering work credited in
   Wikipedia's account to "Kilbourn").
2. **A new mantlet, fitted to a "slightly modified M34A1 gun mount"** (Sherman
   Minutia) — i.e. this is explicitly described as a modification of the
   existing M34A1 mount (an enlarged opening for the larger barrel), not an
   all-new mount, with only the mantlet plate itself newly designed.
3. **The rear "bustle" armored box**, added to house the radio moved out of the
   hull.
4. **A new loader's hatch** cut into the turret roof, because the 17-pdr's
   larger breech/recoil system impeded the loader's ability to exit through
   the commander's hatch.

**Turret front/side/rear wall thickness itself: no source found this session
claims this changed from the base Sherman turret.** None of the three
enumerated-changes lists above (Wikipedia's or Sherman Minutia's) includes a
turret-wall thickness change. This project already has two existing
Sherman turret entries at Turret Side/Rear = 51 mm (M4A1 and M4A3 rows,
identical figure across both despite one small/one large turret) — nothing
found this session contradicts reusing that same 51 mm figure for the
Firefly's turret side/rear, since the underlying casting is the same M4 turret
family.

### Mantlet: "+13 mm" over the standard Sherman mantlet — the best-cited single
number in this research pass

Wikipedia's Design section states: "The Firefly had no armour or mobility
advantages over the normal Sherman tank beyond the additional 13 mm of
protection added to its mantlet." This carries an actual footnote (ref [5])
tracing to **Fletcher, David (2008), *Sherman Firefly*, Osprey New Vanguard
141** — a specialist single-subject monograph, and the single best-attributed
claim found in this entire research pass (even though the book itself was only
reached at second hand via Wikipedia's footnote, not read directly).

**Important caution, flagged explicitly for whoever builds the CSV row:** the
Firefly's Wikipedia infobox separately lists "89 mm maximum (turret front)" —
**with no citation attached to that specific infobox line**. This number is
coincidentally identical to this project's own existing `av_override_mm=89`
value for the "Sherman M4A1 (75mm)" turret front. **These are almost certainly
not the same kind of quantity and should not be treated as confirming each
other:**
- This project's 89 mm (M4A1 row) is a *pre-resolved, weighted-average*
  effective AV from a full mantlet hit-distribution table (Ch.8), accounting
  for where shots land across the mantlet's varying thickness.
- Wikipedia's 89 mm (Firefly infobox) is presented as a flat, uncited
  "maximum" raw thickness figure, with no angle, no construction note, and no
  distribution/weighting behind it — and no stated relationship to the "+13 mm"
  claim elsewhere in the same article (a standard Sherman mantlet + 13 mm would
  need to be compared against a separately-sourced pre-conversion baseline to
  reach 89 mm, and that baseline isn't stated anywhere in the article).

Reusing 89 mm unmodified for the Firefly's turret front — on the theory that
"it happens to match the existing M4A1 number" — would be treating a
coincidence as confirmation. A properly sourced Firefly turret-front AV would
need either (a) a genuine mantlet hit-distribution re-weighting for the new,
larger, differently-shaped 17-pdr mantlet casting (the same kind of exercise
already done for the M4A1's Ch.8 table), or (b) an explicit, deliberate
decision to reuse the M4A1 approach as a stand-in despite the mantlet shape
having changed — but that should be a documented modeling choice, not an
accidental copy-paste.

### Radio bustle box: a new armored structure, not a thinning of the existing
turret rear

Sherman Minutia gives specific numbers for the bustle box itself: **sides
51 mm thick, rear 62 mm thick** ("The sides from the box are 51mm thick, and
the rear is 62mm thick. Top plates come in different versions..."). This is a
genuinely new armored structure bolted/welded onto the existing turret rear —
not a report of the original turret rear wall being thinned to make room for
it. Notably, 51 mm sides on the bustle happen to match this project's existing
Turret Side/Rear = 51 mm figure for the base Sherman turret, and 62 mm rear is
if anything *thicker* than that baseline — so nothing found this session
suggests the radio relocation came at the cost of reduced protection anywhere
on the turret.

### Counterweight vs. muzzle brake: likely a popular conflation, not confirmed
as a distinct feature

An initial broad web search returned a claim that "the armoured box (bustle)
... acted as a counterweight for the longer, heavier gun" — i.e. the counterweight
claim in general web discussion refers to the **rear bustle mass**, not a
separate device on the barrel. Sherman Minutia's dedicated turret page (a more
specialist source) instead describes, from period photographs, a genuine **17-pdr
muzzle brake** fitted to the gun ("The last photo shows the typical 17 Pdr
muzzle brake") — a recoil-reduction device, not an armor/balance counterweight.
**No source found this session confirms a distinct external steel counterweight
ring or collar fitted forward on the barrel**, as opposed to (a) the rear
bustle acting as the tank's own overall balance/counterweight mass and (b) the
muzzle brake. The "external counterweight on the barrel" framing floated in
this task's own brief may be a popular conflation of the muzzle brake with a
counterweight — flagged as genuinely unconfirmed, not chased down further this
session.

### Turret side "cheek armor" bulge: found, but flagged as a DISTRACTOR — not
a Firefly-specific feature

Cross-referenced across five independent hobby/kit-review pages (AK-Interactive,
Tasca/Asuka kit reviews on modelingmadness.com, perthmilitarymodelling.com,
track-link.com, scalehobbyist.com), which agree with each other: some Sherman
turrets have a cast (or, on earlier turrets, welded-on applique) "cheek" bulge
on the turret side, added because the standard turret's internal firing-control
linkage/traverse mechanism required grinding away interior wall material at
that spot, thinning it locally. This was addressed first with welded applique
patches, then (from roughly summer 1943) cast directly into new turret
castings — described by these sources as **general standard-M4-turret
production evolution, not something introduced by the 17-pdr conversion**.
Firefly turrets simply inherited whichever turret-casting generation (with or
without the cheek feature already present) happened to be converted. **This is
not evidence of a Firefly-specific turret side armor change** — flagged here
explicitly so it isn't mistakenly folded into "Firefly turret modifications."

## 3. Ammunition natures: APCBC confirmed available from introduction; APDS
timing for Firefly units specifically is a genuine, unresolved gap

**APCBC:** already fully modeled (`seventeenpdr_76l55_apcbc`); nothing found
this session changes that gun-side data, and it was the Firefly's principal
round from its January 1944 introduction through Normandy. Wikipedia gives
APCBC performance as "163 mm (6.4 in) of armour at 500 m (550 yd) and 150 mm
(5.9 in) at 1,000 m (1,100 yd)" — consistent in ballpark with the Bird &
Livingston-derived APCBC calibration points already in `gun_calibration.csv`
via `british_vehicles_1943.md`'s research.

**APDS:** this project's existing research (`british_vehicles_1943.md`) already
states, for the 17-pdr generally, that APDS "entered service 'from March 1944'"
per Bird & Livingston. For the Firefly **specifically**, sources found this
session genuinely disagree and none is strongly sourced:
- Wikipedia's Firefly article itself only says APDS "was rare until the
  post-war period" — no specific 1944 date at all, and arguably in tension
  with the general March 1944 service-entry date already on file.
- A web-search synthesis (underlying page(s) not individually re-traced this
  session) claimed APDS "did not appear in Firefly stowage until August 1944" —
  i.e. two months after the Firefly's Normandy combat debut in June 1944.
  This is weaker, aggregator-level evidence, not tied to a named primary or
  specialist source.
- No source found this session ties a specific date, order, or unit record to
  APDS reaching **Firefly-equipped units** in particular (general accounts
  more often describe towed 17-pdr anti-tank guns receiving APDS first).

**Practical implication for a 1944 roster entry, stated plainly since the
underlying date is unresolved:** a Firefly modeled at its June 1944 Normandy
debut should almost certainly be treated as **APCBC-only**; APDS availability
should be treated as, at best, a mid-to-late-1944 addition to the same vehicle
entry (somewhere between the March 1944 general 17-pdr service-entry date
already on file and an unconfirmed August 1944 Firefly-specific claim) —
genuinely not pinned down closer than that this session.

## 4. Historical validation data (Firefly 17-pdr vs. Tiger/Panther)

All three vignettes below come from Wikipedia's Firefly "Service" section;
none was independently cross-checked against a named primary source (unit war
diary, AAR) or against Fletcher's Osprey monograph directly this session, even
though that same book is cited elsewhere in the same Wikipedia article for the
mantlet claim — flagged as a worthwhile, but not yet done, follow-up.

- **Saint-Aignan-de-Cramesnil / Gaumesnil, 8 August 1944 — the Wittmann
  engagement.** A Firefly of A Squadron, No. 3 Troop, 1st Northamptonshire
  Yeomanry, gunner Trooper (later Sergeant) Joe Ekins, engaged seven Tiger Is
  of the 3rd/HQ Company, 101st SS Heavy Panzer Battalion (Michael Wittmann's
  unit); Ekins is credited with destroying all three Tigers his troop could
  see, including Wittmann's, in this action. **Range: reported inconsistently
  across tellings even within this session's own sources** — one account gives
  "some 800 yards," another (citing an order from a Captain Boardman) gives
  "seven-hundred meters" as the range at which the Tigers were sighted when
  the order to fire was given. These two figures (~730 m vs. 700 m) are close
  enough that they may just be the same shot described in yards vs. meters,
  not a real disagreement — but this was not conclusively resolved this
  session. Popular accounts elsewhere sometimes cite much longer ranges for
  this engagement; **no source found this session substantiates a multi-
  kilometer range claim** — flagged as likely conflation with a different
  engagement or simply unconfirmed, not chased down further this session. This
  is the best-cross-referenced candidate found for a sanity-check row (converges
  across Wikipedia, TracesOfWar, Warfare History Network, and Key Military on
  the same unit/date/approximate range), analogous to this project's existing
  17-pdr-vs-Tiger historical-matchup entry, though the exact range still
  genuinely wobbles by ~1̃00 m across tellings.
- **Tilly-sur-Seulles, 14 June 1944.** Sergeant Harris's Firefly "knocked out
  the lead Panther with his first shot, and the other with his second," at a
  reported range of 800 m (870 yd).
- **Norrey-en-Bessin, 9 June 1944.** Trooper A. Chapman, credited (per
  Wikipedia) to the "6th Canadian Armoured Regiment," "quickly knocked out
  five Panthers with just six rounds." No range given in the source checked.

## Confidence Notes

- **M4A4 as the standard/most numerous Firefly conversion base:** well-
  corroborated across independent sources (Sherman Tank Site, Sherman Minutia,
  Wikipedia), though no exact hull-type breakdown by count was found.
- **Small-hatch (not large-hatch) glacis for the M4A4/Firefly hull:** the
  "M4A4 never got the large-hatch hull" claim is a direct quote from a single
  dedicated source (Sherman Tank Site); the associated 51 mm/56°-from-vertical
  figure itself is corroborated only at forum level (RC Universe, TMP), not
  against a page-cited primary (e.g. Hunnicutt directly) this session — treat
  the *which glacis generation* finding as solid, and the *exact mm/degree
  pairing* as probable-but-not-independently-page-cited.
- **Welded (not riveted) M4A4 hull construction:** corroborated across two
  independent sources (Wikipedia, Sherman Tank Site); offered as a correction
  to this task's own starting framing.
- **Hull side/rear = 38 mm for the M4A4/Firefly:** not independently confirmed
  for the M4A4 by name in any source this session — inferred from the pattern
  already consistent across this project's own two existing Sherman rows plus
  general secondary literature. Genuinely an inference, not a citation.
- **Turret reused/modified rather than redesigned, and no turret wall-thickness
  change found:** well-corroborated across three independent sources
  (Wikipedia, Sherman Tank Site, Sherman Minutia) all giving the same short
  list of what actually changed (gun/recoil, mantlet, bustle, hatch) with no
  wall-thickness item among them.
- **"+13 mm" mantlet figure:** the single best-cited number in this research
  pass — a direct footnote to a specialist single-subject Osprey monograph
  (Fletcher 2008), even though reached only via Wikipedia's citation, not read
  directly.
- **Wikipedia's uncited "89 mm maximum (turret front)" infobox figure:**
  genuinely weak (no citation) and its relationship to the +13 mm claim, and
  to this project's own pre-existing 89 mm M4A1 av_override figure, is
  unresolved — flagged repeatedly above specifically to prevent an accidental
  copy-paste reuse of a coincidentally-matching number.
- **Bustle box thickness (51 mm sides / 62 mm rear):** single specialist source
  (Sherman Minutia), not cross-checked against a second independent source
  this session, but that source is a well-regarded, detail-oriented Sherman
  modeling reference that names its own contributors (Kurt Laughlin, Adrian
  Barrel) — treated as reasonably reliable but single-sourced.
- **Barrel counterweight vs. muzzle brake:** genuinely unresolved — the more
  specialist source (Sherman Minutia) describes a muzzle brake and a rear-mass
  counterweight (the bustle), not a barrel-mounted counterweight; a distinct
  external barrel counterweight, as sometimes described in popular accounts, is
  NOT confirmed this session.
- **"Cheek armor" turret bulge:** well-corroborated across five hobby/kit-review
  sources as a general Sherman-turret production feature unrelated to the
  Firefly conversion specifically — confident this is a distractor, not a
  Firefly-specific finding, though the underlying sources are all hobby-kit-review
  tier rather than a specialist history text.
- **APDS timing for Firefly units specifically:** genuinely unresolved, with
  real disagreement between an unconfirmed "August 1944" aggregator claim and
  Wikipedia's vaguer "rare until post-war" framing, on top of the already-flagged
  general "March 1944" 17-pdr service-entry date from this project's existing
  research.
- **Wittmann-engagement combat details (unit, date, general outcome):**
  well-corroborated across four independent secondary sources; the **exact
  engagement range** is the one genuinely soft detail, varying by roughly
  100 m across tellings even within this session's own sources, with unrelated
  much-longer-range popular claims elsewhere not substantiated here.
- **Tilly-sur-Seulles and Norrey-en-Bessin vignettes:** single-sourced to
  Wikipedia's own "Service" section this session; not independently
  cross-checked against Fletcher's book or a primary unit record, despite that
  book being accessible (at least in part) to Wikipedia's own editors per its
  citation elsewhere in the same article.

## Open Questions / Gaps for Follow-up

1. Exact hull-type breakdown (M4A4 vs. M4 vs. M4 Composite counts) of the
   ~2,100–2,200 total Fireflies converted was not found this session.
2. M4A4-specific hull side/rear armor thickness (assumed 38 mm/38 mm by
   extension from this project's other Sherman rows) was not independently
   confirmed by a source naming the M4A4 specifically.
3. The small-hatch glacis's exact 51 mm/56°-from-vertical pairing was only
   corroborated at forum level this session — a direct look at Hunnicutt's own
   tables (not accessible via the pages fetched this session) would firm this
   up, the same way `british_vehicles_1943.md` flagged wanting direct access
   to Fletcher's Cromwell/Churchill books for similar reasons.
4. Firefly-specific APDS availability timing is unresolved between the
   project's existing "March 1944" general 17-pdr date and an unconfirmed
   "August 1944" Firefly-specific claim — a genuine gap, not a considered
   recommendation either way.
5. Whether a genuine external barrel counterweight (as opposed to the muzzle
   brake and the rear bustle mass) existed on the Firefly is unconfirmed.
6. The relationship (if any) between Wikipedia's uncited "89 mm maximum"
   Firefly turret-front infobox figure and this project's own pre-existing
   M4A1 89 mm av_override_mm value is unresolved — needs a deliberate decision
   (redo the mantlet hit-distribution weighting for the Firefly's own mantlet
   shape, or explicitly choose to reuse the M4A1 methodology as a documented
   stand-in) rather than an accidental match-up.
7. The Wittmann/Saint-Aignan-de-Cramesnil engagement's exact range (700 m vs.
   800 yd vs. unrelated, unsubstantiated much-longer popular claims) was not
   fully resolved — worth a dedicated look at Fletcher's Osprey Firefly
   monograph or a primary unit record if this engagement is used as this
   vehicle's headline historical-matchup sanity check.
8. None of the three Wikipedia "Service" section combat vignettes were
   cross-checked against Fletcher (2008) directly, despite that book being the
   article's own best-attested source elsewhere — worth doing if this document
   is revisited.

## Addendum, 2026-09-12: Firefly-per-squadron ratio (scenario-design note, not a stat change)

Cross-checking against purchased Canadian Army TOE reference material (MicroMark/
Mark Bevis, Lists C28/C29, "Canadian 4th Armoured Division, Jul 1944-Jan 1945")
surfaced a dated Firefly-proliferation detail this file didn't previously capture:
per-troop Firefly counts within a Sherman squadron rose sharply over the second half
of 1944, not a flat ratio.

- **July-August 1944**: 4 Troops per Squadron, each "3x Sherman V, 1x Sherman
  Firefly Vc" — 1 Firefly per 4-tank troop (25%).
- **August 1944 onward**: 4 Troops @ "2x Sherman V, 1-2x Sherman Firefly Vc," plus
  a fifth troop of "3x Firefly Vc (by Dec 1944)" — roughly doubling to a
  majority-Firefly troop mix within a squadron.
- **By December 1944**: "all but one Squadron had 11x Firefly tanks" (per the
  source's own Note (i)) — i.e. most squadrons in this specific division were
  majority-Firefly by year's end, a dramatic escalation from the July landing
  ratio four months earlier.

This is real, dated, and specific to one division (4th Canadian Armoured), not
independently confirmed against a second unit's TOE this session — treat as a
single-source data point, not a general claim about every Sherman-equipped
formation's Firefly ratio. Not a rules or stat change: this project models one
Firefly counter and one standard-Sherman counter, and a scenario's Firefly count
is already a scenario-design choice (Rule 22, scenario OOB), not something
Section 17/18's stats need to encode. Recorded here as a genuinely useful,
dated data point for whoever writes a late-1944 scenario and wants historically
grounded proportions rather than an arbitrary guess — a July 1944 scenario should
field far fewer Fireflies per squadron than a December 1944 one.

## Addendum, 2026-09-12: reading the (wrong, but real) Fletcher book directly (design note E.142)

A PDF in the project's reference material labeled "Sherman VC M4A4 Firefly
(David Fletcher)" was read directly this session, specifically to resolve the
mantlet "+13mm" claim's provenance and the three historical vignettes' sourcing.
It turned out to be a different Fletcher title than assumed above — its own
copyright page reads 1997, publisher Darlington Productions ("Military Ordnance
Special No. 19"), not the 2008 Osprey New Vanguard 141 book Wikipedia's own
footnote names. The 2008 book remains unread. What the 1997 book actually
contains:

- **The mantlet "+13mm" claim is NOT in this book, at all.** Its entire mantlet
  discussion (p.3) is functional/descriptive only (M34A1-style mount, co-axial
  Browning, No.43 sight) with zero armor-thickness figures — two close-up photos
  and two line drawings of the mantlet, none dimensioned. This project's
  existing turret-front `av_override_mm` (the M4A1's own 89mm plus the sourced
  "+13mm" delta) continues to carry its existing uncertainty flag — **narrowed,
  not resolved**: one specific, highly plausible candidate source has now been
  read in full and ruled out. The 2008 Osprey title remains the best next
  candidate if the real source is ever tracked down.
- **None of the three historical vignettes (Wittmann engagement, Tilly-sur-
  Seulles, Norrey-en-Bessin) appear anywhere in this book.** A full 24-page read
  found zero named combat incidents of any kind — this is a pure technical/photo
  monograph, not a narrative unit history. Their real source remains
  unidentified; this specific title is now ruled out as a candidate.
- **APDS timing**: this book gives "summer of 1944" (p.5) — broader than, but
  consistent with, the already-flagged unconfirmed "August 1944" claim. Also
  newly noted: the same source states APDS "proved to be wildly inaccurate at
  anything over 1,000 yards" even after it became available — a real
  operational caveat, not a new project gap (PEN and to-hit are already
  separate mechanics here).
- **Ammunition stowage (77 rounds) independently confirmed with full positional
  detail** (p.4): 5 ready-use + 20 horizontal under the turntable + 20 vertical
  in a floor bin + 18 at 40° under the turret floor + 14 in the redundant
  hull-MG-gunner's old position = 77 exactly, matching the figure already in
  this file.
- **New, not previously recorded**: turret ring dimensions (56.0" inner / 69.0"
  outer diameter); a detailed Firefly production/fielding timeline (War Office
  requirement raised from 2,100 to 3,100 by Jan 1945; 288 on strength in
  Normandy by 24 June 1944; 699 converted by 31 July 1944) and a per-division
  Firefly-holdings table for 21st Army Group at end of June 1944 (7th Armoured
  36, 11th Armoured 36, Guards Armoured 36, Polish 1st Armoured 25) — useful
  scenario-design context, not an armor-stat question; and real period
  countermeasures against the Firefly's conspicuous long gun (painting the
  outer barrel a lighter color, fitting a false muzzle brake partway down the
  barrel, in Italy driving with the real gun reversed and a dummy 75mm tube on
  the turret rear, using an ordinary 75mm Sherman as a "stalking horse" to draw
  fire first) — genuine flavor material, not tied to any current rule.

Full detail, page citations, and confidence notes in
`counters/toe/firefly_fletcher_2008_1944.md` (filename kept from the original
task despite the book turning out to be the 1997 title, not the 2008 one — see
that file's own header for the correction).
