# British Army Commandos — Organization, Training, and Weapons — Scope-Flagged Research (and a Mislabeled-Source Finding)

## Sources

- The file supplied for this pass is
  `reference/epdf.pub_osprey-no10-inter-allied-commando-1942-45-britains-secret-commando-elite-64.pdf`,
  whose **filename** claims it is Ian Sutherland's *No.10 (Inter-Allied)
  Commando 1942-45* (Osprey Elite 64). **It is not.** Every one of its 65
  pages was read visually (image-only scan, zero extractable text
  confirmed via `pdftotext` beforehand) in four ~20-page batches, and the
  book's actual cover, ISBN (1 85532 579 9), and author credit are for a
  completely different Osprey Elite 64 title: Mike Chappell's *Army
  Commandos 1940-1945*, a general organizational/operational history of
  the whole British Army Commando force, not a unit history of No.10
  Commando specifically. This is reported as a finding in its own right,
  not smoothed over — see Scope Verdict below for why it changes this
  pass's answer to the coordinator's central methodological question.
- Cross-referenced against a direct grep of `docs/source/*.rst` and
  `counters/infantry_calc/data/units.csv`, confirming the brief's premise:
  "Rangers" and "Commando" appear in this project only as bare elite
  exemplars in Section 15.5.2's Force Morale factor table and Section
  22.3.3's scenario-difficulty table ("Elite (SS, Guards, Rangers,
  airborne)" / "Entirely elite (SS, Guards, airborne, Rangers)") — zero
  actual unit type, TOE, or roster row for either nation.
- Cross-referenced against `us_airborne_zaloga_1943.md` (E.153) and
  `german_airborne_quarrie_1943.md` (E.154) as the closest prior-pass
  templates — this is the same shape of investigation (opening a new
  unit-type thread for a bracketed elite exemplar that has never had a
  dedicated source read against it).

## Scope Verdict: The Actual Book Is a General Commando Reference, Not a No.10-Specific Unit History — a Better Match Than Expected, With One Real Cost

The task brief anticipated a narrow-unit-history caveat (a book about one
unusual multinational Commando, not general Commando doctrine) and asked
this pass to check that honestly. The actual finding inverts that
caveat entirely:

- **The book delivered is the general reference**, covering the whole
  Army Commando organization from its June 1940 founding (Churchill's
  directive to Dudley Clarke) through 1946 disbandment: formation,
  training doctrine, a chronological raid narrative (Lofoten, Vaagso,
  St Nazaire, Dieppe, Bruneval, North Africa), Special Service
  Brigade/Group order-of-battle charts at three different dates, a full
  unit-by-unit appendix (No.1 through No.52 Commando, the Middle East
  Commando, No.62/SSRF, the SBS), and dedicated uniform/equipment/weapons
  plates with commentary. This is exactly the kind of general
  organizational source E.153/E.154 had for Airborne (two, in fact — a US
  and a German Battle Orders volume) and that this project's Commando
  thread has been missing entirely.
- **The cost:** because the actual book is not about No.10 Commando, its
  coverage of this project's assigned angle — No.10 (Inter-Allied)
  Commando and X Troop specifically — is minimal. See the dedicated
  section below; the honest answer to that specific sub-question is a
  near-total negative, not a partial one.
- **Net effect on the coordinator's real question** ("can a Commando book
  answer the general unit-type question, or only partially?"): this
  particular book answers the *general* question about as well as a
  single source reasonably could — real troop/section organization,
  real training-standard documentation, real weapons/equipment detail,
  a full unit roster. It does **not** deliver the specific X
  Troop/No.10 flavor content the brief was scoped around, because that
  specific book was never actually in hand. Whether this constitutes
  "the Commando gap now has one solid book behind it" (matching Airborne's
  eventual two-book state) or still needs a second source is addressed in
  Open Questions.

## Organizational Findings — Troop/Section-Level Breakdown, Genuinely Dated 1943

Unlike both Airborne books (E.153/E.154), which had real 1943 revisions
attested only in prose and never reproduced as a standalone table, this
book's most detailed organization chart is captioned, in the book's own
words, **"Order of battle, 1943 Commando (460 all ranks)"** (p.29) — an
explicitly 1943-dated, full troop/section/sub-section breakdown, the best
scope match of any TOE pass in this project's history to date:

| Echelon | Composition |
|---|---|
| Commando HQ | CO (Lt-Colonel), 2IC (Major), Adjutant, RSM, HQ personnel, and a signals troop |
| Commando (whole) | HQ + 5 rifle Troops + 1 Heavy Weapons Troop (39 all ranks) — 460 all ranks total |
| Troop | Captain, Troop Sergeant Major, Medical Orderly, runner + 2 Sections |
| Section | 31 all ranks: Subaltern, Sergeant, runner + 2 Sub-Sections |
| Sub-Section | Lance-Sergeant, Corporal, 2 Lance-Corporals, 10 Privates |
| Heavy Weapons Troop (39 all ranks) | a 3-inch Mortar Section + a Medium Machine Gun Section |

This is a genuinely different structural shape from every infantry
roster row already in this project: no separate weapons platoon
integrated into the rifle-troop chain the way `united_states_1943.md`'s
company-level Weapons Platoon works — instead a single dedicated Heavy
Weapons Troop (mortars and medium/Vickers-type MGs) sits alongside, not
beneath, the five rifle Troops, at Commando level. The book gives no
per-Troop or per-Section organic-weapon inventory beyond this
(no confirmed count of Bren guns, PIATs, or similar per Section) — a real
gap, the same kind `german_airborne_quarrie_1943.md` (E.154) flagged for
the missing Fallschirmjäger Gruppe table. The earlier "ten Troops of
50 men, later six Troops of 3 officers/62 men" structure (p.7, late-1940
reorganisation) and three separate wartime "Order of battle" charts
(Nov 1940-early 1941; 1941-1943; 1943-1945 Special Service Group) show the
overall Commando/Brigade echelon expanding and reorganizing repeatedly —
the Troop/Section/Sub-Section table above is the single most granular,
explicitly-1943-dated snapshot the book gives, and is not contradicted by
those other charts (which describe higher echelons at different dates).

A real organizational/doctrinal shift is separately and explicitly
dated to early 1943 in the book's own Introduction (p.3): **"In early
1943 the role of this raiding force was changed to one of assault
infantry"** — i.e., by this project's own 1943 baseline year, Commandos
were already transitioning from small-scale raiders to a heavier
"light/assault infantry" role fighting alongside conventional formations,
a genuinely useful data point for the Force Morale / scenario-difficulty
tables' "elite" framing (see Quality Tier section below).

## Quality Tier / Selection & Training Findings

The book documents the Commando selection and training regime in real,
citable detail — comparable in strength to the Airborne pass's jump-school
findings and the Sniper pass's dedicated-school findings:

- **All-volunteer recruitment**, drawn from "a cross-section of the corps
  and regiments" of the British Army, men "seeking action, adventure and
  an escape from the boredom of conventional service" (p.4).
- **A real selection/washout mechanism**: commanding officers were chosen
  from volunteers, then chose their own officers, who in turn chose their
  own men; "misfits were soon 'returned to unit'" (RTU) — an active
  quality filter, not just a volunteer intake (p.8).
- **A reproduced, numbered 17-point training doctrine** ("Commando
  Catechism," laid down by Lt.Col. Newman, No.2 Commando, pp.8-9),
  covering: mental alertness/independent tactical judgement; physical
  fitness sufficient to "cover at great speed... distances of five to
  seven miles in fighting order"; cliff and mountain climbing; unarmed
  combat; day/night seamanship and boatwork; night navigation/compass
  work; map reading and route memorising; W/T (radio) proficiency;
  demolitions, Bangalore torpedoes, and booby-trap construction; street
  fighting and urban clearance; driving "motorcycles, cars, lorries,
  tracked vehicles, trains and motorboats"; fieldcraft, foraging, and
  extended bivouac survival; first aid including gunshot-wound dressing.
- **A dedicated central training depot**: after initial unit-level
  training and a spell run through the Scottish "Irregular Warfare
  School" (established May 1940), Commando training was centralized at
  **Achnacarry** in the Scottish Highlands ("Commando Basic Training
  Centre," p.13, p.30) under Lord Louis Mountbatten's 1941-42
  reorganization. Named graduates of the earlier Irregular Warfare School
  cited by the book: David Stirling (founder of the SAS) and Mike Calvert
  (later the "Chindit" leader) — real evidence the Commando training
  pipeline seeded other elite formations, not just its own ranks.
- **A real, quantified elite-tier density claim distinct from training
  narrative**: "Commando units had a higher establishment of snipers than
  normal infantry battalions" (p.58) — a directly comparable finding to
  the sniper-tier work in `military_sniper_pegler_1943.md` (E.149/E.150),
  though this book gives no specific per-Troop sniper count.
- **A real, dated, explicit quality caveat, not a clean "always elite"
  picture**: covering the North Africa (Torch) landings, November 1942
  through April 1943, the book states plainly that Commandos "soon found
  themselves embroiled as line infantry in the battles that followed...
  Fighting without heavy weapons or the administrative back-up of line
  infantry, Commandos sustained such casualties that by the time they
  were withdrawn from the line in April 1943, their total strength was
  down to 150 men" (p.29) — named units (No.1 and No.6 Commando), a real
  1943-dated anecdote, and a genuine parallel to the Airborne pass's
  parachute/glider split and the German Airborne pass's "diluted late-war
  division" finding: elite status here is tied to being used in the
  raiding/specialist role Commandos were trained and equipped for, not a
  flat "always performs better" property once misused as ordinary line
  infantry.

**On the specific US Rangers/British Commando training-link question the
task asked to check plainly: this book does not document it.** It
mentions US Rangers exactly once, as a co-belligerent force at Dieppe
(August 1942, not 1943): "Most of the troops involved were to come from
the 2nd Canadian Division... detachments from No.3 Commando, No.4
Commando, the recently-formed Royal Marine A Commando, No.10
(Inter-Allied) Commando and the United States Rangers" (p.23), and
afterward that "the French Commandos and American Rangers attached to
British units gave a good account of themselves" (p.25). That is the
book's entire Ranger content — real, but establishing only a
co-deployment fact, not a training pipeline. **No statement anywhere in
this book says US Rangers trained at, or were modeled on, a British
Commando depot or methodology** — a clean negative on that specific
claim, reported plainly rather than backfilled from outside knowledge,
per this pass's own instructions. (Separately, and worth flagging for a
future pass rather than treated as sourced here: this same book's own
back cover lists a companion Osprey Elite title, *No.13 US Army Rangers
1942-87*, as an existing Elite series volume — not currently in this
project's `reference/` library — a concrete, named candidate for the
dedicated Rangers-side follow-up this thread would need, exactly
mirroring how the Airborne thread needed a second, nation-specific book.)

## Weapons/Equipment Findings

The book gives real, specific small-arms and equipment detail, including
one genuinely mechanically-relevant logistics fact:

- **Sidearm/SMG standardization on a single pistol caliber**: the Thompson
  submachine-gun (.45in, 10.5 lbs, 20-round box or 50-round drum, "the
  favoured Commando weapon") and the Colt M1911 .45 automatic pistol
  (2.5 lbs, 7-round magazine) were both chambered in the same .45 ACP
  round, deliberately: **"The common .45-inch A.C.P. round limited the
  types of small arms ammunition carried by Commandos to two. (As opposed
  to the four carried by some British units.)"** (p.58) — a real,
  citable, quantified logistics/ammunition-diversity distinction from
  standard infantry, not present in any prior TOE file in this project.
- **The De Lisle Commando carbine** (p.58): a modified Lee-Enfield action
  firing .45 ACP through an integral 13-baffle suppressor, "permitted
  silent killing out to 400 yards" — a genuinely distinct weapon type
  with no equivalent anywhere in this project's current weapons data.
- **The Vickers 'K' gas-operated machine gun** (pp.58-60): originally an
  RAF aerial-combat weapon, adapted by Commando units to a bipod-mounted
  ground light-machine-gun role; 96-round drum magazine, cyclic rate
  "over 1,000 rounds per minute... could produce a greater volume of fire
  than the standard Bren... but could not compete with the Bren's
  accuracy" — an explicit volume-vs-accuracy tradeoff weapon unique to
  Commando/airborne-adjacent units in this book, again with no equivalent
  in this project's current weapons data.
- **Sniper rifles**: the Rifle No.3 Mark 1* (T) — a scoped .303
  Pattern-1914 action with 3x telescope — was standard-issue to Commando
  snipers "until No.4 sniper rifles became available in 1942" (p.58),
  after which the No.4(T) took over; both are already-known WWII British
  sniper rifle types, not a new one, but the book's higher-establishment
  claim (above) is the load-bearing quality-tier point.
- **Edged weapons as a real identity marker**: the Fairbairn-Sykes
  fighting knife (multiple patterns across the war, ~13in) and its 16in
  "No.2 pattern" variant nicknamed the "Roman sword" or "Smatchet,"
  plus several patterns of knuckle-duster fighting knives — well
  documented but flavor/identity equipment, not firepower-relevant.
- No systematic difference from standard British infantry equipment is
  claimed for rifles themselves — Commandos "utilised the full range of
  British infantry weapons, and were trained to use those of their
  enemies" (p.57); the real equipment distinctiveness is concentrated in
  sidearm/SMG standardization, the two specialist weapons above, and
  raiding-specific gear (Bergen rucksack, toggle-rope, inflatable
  life-belt), not the basic rifle.

## Mechanically Distinct: Amphibious/Small-Boat Raiding Insertion, and Reduced Ammunition-Type Diversity (Flagged, Not Designed)

Per this pass's own constraint, nothing below is designed as a rule —
flagged for the coordinator only, the same way E.153 flagged airborne
drop-scatter and E.154 flagged container-delivered weapons:

- **Seaborne raiding insertion is the book's central, load-bearing
  subject, not an incidental detail**: virtually every operation
  narrated (Lofoten, Vaagso, St Nazaire, Dieppe, the Bruneval
  radar raid's beach extraction, the Rhine crossing) depends on a
  specific insertion/extraction method — assault landing craft (LCA,
  35 fully-equipped troops), motor launches, submarine-launched folboats
  (the Rommel raid, the SBS), or a purpose-rammed obsolete destroyer
  (St Nazaire) — with real, repeated failure modes documented (Guernsey,
  July 1940: a raiding force had to swim for it when the sea worsened
  and left non-swimmers behind; the Lofoten and St Nazaire raids both
  describe substantial craft losses to enemy fire during withdrawal).
  This project's Section 6-24 movement/entry rules make no distinction
  between a unit that walks onto the map and one that arrives by small
  boat under fire — the same shape of gap E.153 flagged for airborne
  drop dispersion, but for a different insertion method and a unit
  whose entire raison d'être (unlike airborne) is this insertion type,
  not just its entry.
- **The two-ammunition-type sidearm/SMG standardization** (above) is a
  real, quantified logistics distinction, but this project's rules do not
  currently model ammunition-type diversity as a mechanic at all for any
  unit — flagged as a fact, not a candidate mechanic, since there is no
  existing system for it to plug into.
- **The Commando Order** (Hitler's directive of 18 October 1942,
  reproduced in full on p.28: captured Commandos "will be ruthlessly
  exterminated... to the last man") is documented with a real, dated,
  named consequence within this book's own text — two officers who led
  the December 1942 Glomfjord, Norway raid were shot under the order
  after capture, and Sark-raid reprisals are also described. This is a
  genuinely distinct historical capture/no-quarter risk specific to
  raiding-type units that this project's rules do not model for any unit
  (no differential surrender/capture consequence exists in Sections
  6-24) — flagged exactly as the coordinator's brief requested, with no
  mechanic proposed.

## 1943-Dated Findings (Anecdotes and a Real Coverage Gap)

Honestly reported: **this book's narrative detail is heavily
front-loaded onto 1940-42** (the raiding era — Lofoten, Vaagso, Bruneval,
St Nazaire, Dieppe are all narrated in named, dated, multi-page detail).
Coverage of 1943-45 compresses sharply into brief unit-by-unit appendix
summaries and order-of-battle charts, a real asymmetry worth flagging
rather than papering over — the opposite of the Airborne pair, whose
best material (Sicily, Salerno) was itself 1943-dated and narrated in
detail.

The best 1943-dated, named, citable finds from this pass:

1. **The explicitly-dated "1943 Commando (460 all ranks)" order-of-battle
   chart itself (p.29)** — see Organizational Findings; genuinely usable
   as this project's first real within-1943 Commando organizational
   citation.
2. **North Africa, November 1942 - April 1943**: No.1 and No.6 Commando,
   landed as part of the Torch invasion force, fought as improvised line
   infantry through the Tunisian campaign and were withdrawn in April
   1943 reduced from full strength to 150 men (p.29) — named units,
   dated, and a real quality-tier caveat (see above).
3. **Early 1943, doctrinal turning point**: the book's own Introduction
   states the raiding force's role "was changed to one of assault
   infantry" in early 1943 (p.3) — a real, dated organizational-shift
   statement, not a specific raid anecdote, but directly citable.
4. Weaker, unnarrated mentions only: "In 1943 No.3 Commando fought in
   Sicily and Italy" and "No.9 Commando went on to fight in the Italian
   campaign, in Greece and in the Aegean" (p.45-46) — real but not
   developed beyond a single summary sentence each; not usable as
   stand-alone flavor-text anecdotes without further research.

## X Troop and No.10 (Inter-Allied) Commando Specifically: A Clean, Near-Total Negative

This is the task's most direct casualty of the mislabeled source. The
entire book's treatment of No.10 (Inter-Allied) Commando is one paragraph
in the unit-by-unit appendix (p.46), reproduced here in full because
there is nothing else to draw on:

> "In August 1940 attempts to raise a No.10 Commando from the troops in
> Northern Command met with a poor response and those volunteers that had
> come forward were posted to other Commandos. In early 1942 an
> Inter-Allied Commando was formed which eventually grew to include a
> Free French Troop, a Dutch Troop, an 'X' or 3rd Troop of men from
> eastern European countries, a Belgian Troop, a Norwegian and Danish
> Troop, a Polish Troop, a Yugoslavian Troop, and a further troop of Free
> Frenchmen. Although commanded by a British lieutenant-colonel their
> amazing record forms no part of the story of the British Army
> Commandos. Sufficient to salute their courage and their achievements in
> battle, both alongside their British comrades and in the clandestine
> operations and raids they carried out behind enemy lines."

That is the complete X Troop content in this book: **X Troop is
described only as "men from eastern European countries"** — the book
does not mention that X Troop was specifically composed of German and
Austrian refugees (most of them Jewish), that they served under assumed
British identities, or that this was done specifically because of the
extreme personal risk of summary execution under the Commando Order if
captured and identified as German nationals in British uniform. No dates,
no named individuals, no operations, no organizational detail of any
kind is given for No.10 Commando specifically — a clean negative, not a
partial one. The famous X Troop story this pass was briefed to expect is
simply not in this book; the book's own text (quoted above) explicitly
disclaims covering it ("forms no part of the story of the British Army
Commandos" — a line about the general-history book's own self-defined
scope, ironically confirming why the actually-titled *No.10 (Inter-Allied)
Commando* book would be the correct source and this one is not it).

## Confidence Notes

- The organizational chart (Troop/Section/Sub-Section headcounts) is a
  direct reproduction of the book's own captioned diagram, explicitly
  dated 1943 in its own caption — high confidence, and a genuine
  improvement in scope-match over both Airborne TOE passes.
- The training-doctrine list (the 17-point "Commando Catechism") is a
  direct verbatim reproduction of a real wartime document the book
  itself reproduces in full, attributed to a named officer (Lt.Col.
  Newman) — high confidence as a real primary-adjacent source, though
  the book does not give this document its own precise date beyond
  "later" than the unit's original 1940 formation.
- The two-ammunition-type logistics claim and the Vickers 'K'/De Lisle
  carbine weapons details are stated in the book's own prose, not
  inferred — high confidence for what they say.
- The North Africa 150-men casualty figure and April 1943 withdrawal date
  are stated plainly in the book's own text — high confidence.
- The X Troop finding is a negative result (an absence), not a positive
  claim requiring separate verification — but is reported with the same
  rigor as a positive finding, per this pass's own instructions.
- The mislabeled-file finding (this PDF's filename vs. its actual cover
  and content) was confirmed visually against the book's own cover page,
  copyright page (ISBN 1 85532 579 9), and back-cover author biography
  (Mike Chappell) — this is a certainty, not a judgment call.

## Open Questions

1. **The genuine No.10 (Inter-Allied) Commando / X Troop source (Ian
   Sutherland's Osprey Elite 64, the book this file's source PDF was
   mislabeled as) was never actually read this pass** — a direct,
   actionable follow-up: acquiring and reading the correctly-titled book
   would close the X Troop/No.10-specific half of this thread the same
   way `german_airborne_quarrie_1943.md` closed the German half of the
   Airborne thread.
2. **The US Rangers side of this project's bracketed "Rangers/Commando"
   exemplar remains completely unresearched** — this pass found only a
   single co-deployment mention (Dieppe, 1942) and no training-pipeline
   documentation. The book's own back cover names a concrete, existing
   candidate source (*US Army Rangers 1942-87*, Osprey Elite 13) not
   currently in this project's `reference/` library. Until a Rangers-side
   book is read, this project's Commando/Ranger gap is at best half
   addressed — a real asymmetry with the Airborne thread, which now has
   a book for each of its two nations.
3. **No per-Troop or per-Section organic-weapon inventory** (Bren gun
   counts, PIAT/anti-tank provision, small-arms mix below the
   Section level) was found in this book at any date — a real gap in the
   source itself, parallel to the missing German Fallschirmjäger Gruppe
   table E.154 flagged.
4. The amphibious/small-boat insertion mechanic and the Commando Order
   capture-risk mechanic are both flagged as real, evidenced candidates
   for a future dedicated design pass (see Mechanically Distinct section)
   but are explicitly not designed here, on the same footing as the
   jungle-terrain-type and drop-scatter proposals E.152/E.153 left open.
5. No `units.csv` row was added for a Commando squad/section of any kind
   — see the top-level design note (E.155) for why this constraint was
   followed even though the Troop/Section/Sub-Section headcount data here
   is comparably well-sourced to the Airborne pass's squad data.
6. Whether this project should treat the Commando/Ranger gap as "now has
   one solid book" (matching the state Airborne was in after E.153 alone)
   or as still needing the Rangers-side book before being considered on
   equal footing with Airborne's now-two-book state is a real, open
   judgment call for the coordinator — this file does not resolve it,
   only lays out the evidence on both sides (see Scope Verdict).
