# Unmodeled-Vehicle Survey, 1943 — Crusader, Universal Carrier, US Light Tanks

Research pass reading the last three unread vehicle-adjacent books in
`reference/armor-vehicles/` against an open-ended question that had never
been logged as a tracked gap anywhere in this project: does the library
reveal a real, citable reason to add any of Crusader, Universal Carrier, or
the M3/M5 Stuart family to `counters/armor_calc/data/vehicles.csv`, which
currently has no rows for any of them? This is a completionist sweep, not a
follow-up to a specific open question — see design note E.163.

## Books read

1. Fletcher, David. *Crusader Cruiser Tank 1939-45* (Osprey New Vanguard 14).
   `reference/armor-vehicles/epdf.pub_crusader-cruiser-tank-1939-45.pdf`,
   49pp, image-only scan, read in full via the Read tool's `pages` parameter.
2. Fletcher, David. *Universal Carrier 1936-48: The 'Bren Gun Carrier' Story*
   (Osprey New Vanguard 110).
   `reference/armor-vehicles/epdf.pub_osprey-new-vanguard-110-universal-carrier-1936-48-the-bren-gun-carrier-story.pdf`,
   52pp, image-only scan, read in full.
3. Zaloga, Steven J. *US Light Tanks at War 1941-45* (Concord Armor at War
   7038).
   `reference/armor-vehicles/epdf.pub_armor-at-war-series-wwii-us-light-tanks-at-war-1941-1945.pdf`,
   74pp — catalogued as image-only, but actually carries a real, dense,
   3-page extractable-text Introduction plus a "Preparing for War,"
   "Initial Combat," and theatre-by-theatre prose narrative threaded between
   the photo captions; read in full.

Roster confirmed empty for all three vehicle families before starting:
`grep -i "crusader\|carrier\|stuart\|light tank\|m3\b\|m5\b"
counters/armor_calc/data/vehicles.csv` returns nothing. No existing
`counters/armor_calc/README.md` "Known gaps" line documents a deliberate
scope decision to exclude any of the three — their absence from the roster
appears to be simple historical accident (nobody had checked), not a
recorded design choice this pass is confirming.

## 1. Crusader — Cruiser Tank Mk VI

**Roster verdict: clean negative, no addition proposed.** The book confirms
this project's working assumption directly: Crusader was declared obsolete
alongside the earlier Covenanter and was being withdrawn from front-line gun
tank service through late 1942/early 1943. By the time British armoured
regiments deployed to Tunisia and then Italy, "all British regiments had
handed in their Crusaders and moved into Shermans." Residual use as a *gun
tank* persisted only in isolated pockets into 1943 — a mixed squadron in the
Wiltshire Yeomanry as late as October 1943 still fielded some Crusaders
alongside Shermans and Grants — genuinely secondary, not a role a scenario
designer using this project's rules would need a dedicated counter for.
Crusader's non-gun-tank derivatives (the Crusader III AA, entering
production summer 1943 with Bofors/Oerlikon mounts, and the Crusader
17-pdr gun tractor, used from the Tunisian campaign onward) had longer
service lives, but neither is a direct-fire combat AFV of the kind this
roster models. No `vehicles.csv` row is proposed.

**Bonus check (Cromwell/Churchill armor geometry) — a real, if inapplicable,
positive.** Unlike every other Osprey New Vanguard title tried against the
Cromwell/Churchill plate-geometry questions so far (Fletcher & Harley's own
*Cromwell Cruiser Tank 1942-50*, E.137; Sandars' *British 7th Armoured
Division*, E.162), this book actually contains a genuine hull/turret
plate-thickness diagram: p.9 reproduces two official wartime technical
drawings, headed "MOST SECRET," titled "Covenanter I — Plate Thickness"
(T.D. 5913) and "Crusader III — Plate Thickness" (T.D. 5911), each labeling
individual named plates (front outer/inner, side outer/inner, rear, bottom,
turret roof, etc.) with thickness figures given mostly as fractional-inch
values alongside material-specification codes, plus at least one legible
mm figure (~50mm, visor casting). **This does not resolve either open
Cromwell/Churchill question** — Crusader and Covenanter are earlier,
distinct vehicles in the same Christie-suspension cruiser-tank lineage, not
Cromwell or Churchill themselves, and the book contains no equivalent
diagram for either roster vehicle. It is recorded here as a genuine
break in the previously unbroken "Osprey New Vanguard has no plate
diagrams" pattern, in case a future pass on Crusader/Covenanter-adjacent
armor questions needs it, and cross-referenced from
`counters/toe/cromwell_churchill_fletcher_harley_1943.md`.

**1943-dated anecdotes:** 6th Armoured Division's Crusaders in the Tunisian
campaign (November 1942 into early 1943); the 17th/21st Lancers fielding
six 6-pdr-armed Crusaders during the same campaign. Real, named, dated, but
not detailed enough (no specific action/range/outcome) for a Rule 18.12-style
flavor-text entry.

## 2. Universal Carrier ("Bren Gun Carrier")

**Roster verdict: clean negative, no addition proposed.** The book confirms
this project's working assumption just as directly: the Universal Carrier
was never a combat tank. It is documented exclusively in support/utility
roles — scout carrier, 3-inch mortar carrier, medium-machine-gun carrier,
armoured observation post (artillery spotting) carrier, ambulance, and
generic prime mover/gun tractor — used "by its very nature and ubiquity" in
"dozens of different, unofficial roles" as well. It is not, and was never
intended to be, a direct-fire AFV analogous to any of this project's 14
existing roster vehicles. No `vehicles.csv` row is proposed.

**Bonus check (Cromwell/Churchill armor geometry) — effectively another
clean negative.** The book gives exactly one armor figure, on the Mark II
colour-plate commentary: "Armour thickness 10mm max. 4mm min." — a single
aggregate spec, not a plate-by-plate table, and for a vehicle that is not
part of the Cromwell/Churchill cruiser-tank lineage in the first place (the
Universal Carrier descends from the Carden-Loyd/Bren-carrier line, an
entirely separate design tradition from the Christie-suspension cruiser
tanks). This does not advance either open Cromwell/Churchill question and
is recorded only for completeness.

**1943-dated anecdotes:** two genuine, precisely-captioned colour-plate
items — "Carrier Mark II, 1st Royal Irish Fusiliers, 38th Irish Brigade,
78th Infantry Division, Italy, 1943" and "Universal Carrier Ambulance, 2nd
New Zealand Division, Italy, 1943" — plus a real but undetailed note that
carriers were "tested in 1943 with a device for laying smoke screens" (no
further detail survives, per the book's own text) and that MEE trials in
1943 mounted a PIAT on brackets above a carrier's armour (found impractical:
the loaded projectile dislodged on rough ground). None of these rise to a
flavor-text-ready combat anecdote — they are logistics/support vignettes,
consistent with the vehicle's own documented role.

## 3. US Light Tanks (M2A4/M3/M3A1/M3A3/M5/M5A1 "Stuart" family)

**Roster verdict: a real, citable candidate — flagged for the coordinator,
not added.** This is the one book of the three that changes the picture.
Unlike the brief's working assumption that Stuart-family light tanks saw
only "real but secondary" 1943 use, this book documents extensive,
multi-theater, well-dated 1943 combat:

- **North Africa/Tunisia (Nov 1942 – May 1943):** 1st Armored Division's
  two light tank battalions fought throughout the Tunisian campaign —
  Kasserine Pass (Feb 1943, where the Afrika Korps captured and reused
  several M3s), the M3 "El Diablo" of 1st Battalion, 1st Armored Regiment,
  knocked out in Tunisia in February 1943, M5 light tanks of the 899th Tank
  Destroyer Battalion operating near Maknassy on 8 April 1943, and M3s
  escorting a British supply convoy near El Guettar on 8 April 1943.
- **Pacific theatre (continuing through 1943):** M3/M3A1 light tanks
  supported the Marine Corps and US Army across Guadalcanal (into early
  1943), New Georgia (Marine 9th/10th/11th Defense Platoons providing
  canister-round fire support near Munda airfield, 6 August 1943),
  Bougainville (Marine 3rd Tank Battalion and Army 754th Tank Battalion,
  November 1943), Tarawa (Marine 2nd Tank Battalion's M3A1s, 21-23 November
  1943), and Makin Atoll (Army 193rd Tank Battalion's M3A1s, 20-22 November
  1943).
- **Eastern Front (Lend-Lease, 1942-43):** Soviet-crewed M3/M3A1 Stuarts
  documented in the recapture of Byelgorod, 9 February 1943 (Voronezh
  Front's Kharkov operation), alongside T-34 Model 1943 tanks.
- **Italian theatre (from October 1943):** M5A1 light tanks of the 601st
  Tank Destroyer Battalion crossing the Volturno River, 13 October 1943 —
  the theatre's opening phase, squarely inside this project's 1943 baseline.

The book is also explicit about the tactical *decline* of the type across
1943 — real, citable context if the coordinator does add it: by spring
1943, commanders in North Africa (including Bradley and Patton) "recommended
instead that the role of the light tank be limited to scouting and flank
security," and light tank crew casualty rates in the mixed formations later
in the war ran roughly one-in-three versus one-in-five for medium tank
crews (a summer-1944 figure, cited here for the trend, not claimed as a
1943 statistic). This supports modeling the Stuart, if added, with a
combat role and/or quality caveat rather than as a first-line gun tank —
consistent with how this project's existing German/Soviet light tanks
(Panzer III, T-70) are already positioned in the roster.

**Proposed for the coordinator's decision (not added by this pass):** add
an M3 or M3A1 light tank ("Stuart I/II/III," 1943-appropriate turret/hull
variant) to `vehicles.csv`, on the strength of the documented Tunisian,
Pacific, and Eastern Front 1943 combat record above. This book alone does
not supply hull/turret armor thickness-and-angle figures (see below), so a
dedicated source (a Panzer-Tracts-style US-armor reference, or Hunnicutt's
*Stuart: A History of the American Light Tank*) would be needed before any
row could actually be populated — this pass identifies the *case* for
adding the vehicle, not the plate data to do so.

**Bonus check (Cromwell/Churchill armor geometry) — clean negative, and not
applicable.** This is a pure operational/photo history with no
specification tables of any kind; no hull or turret armor thickness data
for the Stuart family appears anywhere in the book. Not relevant to the
Cromwell/Churchill question regardless (different nation, different
lineage), checked only for completeness per this pass's brief.

## Net effect

Two of three books (Crusader, Universal Carrier) are clean negatives on the
roster question, each independently confirming this project's working
assumption about the vehicle's real-world role rather than complicating it.
The third (US Light Tanks) surfaces a genuine, multi-theater, well-dated
1943 combat case for the Stuart family that this project has never actually
checked before — flagged above for the coordinator, not acted on. The
Cromwell/Churchill armor-geometry bonus check turned up one real exception
to the established "Osprey New Vanguard has no plate diagrams" pattern
(Crusader's own p.9 diagram) but it answers a different vehicle's question,
not this project's two open ones, which remain exactly where E.137 and
E.162 left them.

No `vehicles.csv` row was added, and no rule mechanic was designed.
`reference/CATALOG.md` updated: all three books' rows point to this file
and design note E.163.
