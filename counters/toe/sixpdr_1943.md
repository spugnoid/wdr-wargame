# British Ordnance QF 6-Pounder — Crew, 1943 Organizational Context, and Deployment Notes

Research pass only, scoped narrowly per the task brief: **ballistics are already done**
(`counters/armor_calc/data/guns.csv` row `sixpdr_57l50_apcbc`, MV 2730 fps, K-factor
1495 already fit; see `counters/toe/british_vehicles_1943.md` for the sourced
calibration points behind that fit — not revisited here). This file gathers only
the crew/organizational/TOE facts needed to field the 6pdr as a 1943 British
"Towed Anti-Tank Gun" roster entry under Rule 17.1a, following the format of
`counters/toe/pak40_1943.md` (this project's first towed-AT-gun research pass,
for the German 7.5cm PaK 40).

## Sources

- Wikipedia, "Ordnance QF 6-pounder" — https://en.wikipedia.org/wiki/Ordnance_QF_6-pounder
  — infobox states "Crew: 6" (no inline citation on the infobox line itself,
  consistent with several other independent sites below). Separately, in its
  "United States" service section, gives a detailed **10-man crew** for the
  US Army's own use of the same gun (as the "57 mm Gun M1"): a squad leader,
  a gunner/#1, four cannoneers #2–5, three ammunition bearers #6–8, and a
  driver #9 — cited to *War Department Basic Field Manual FM 23-75, 57-mm Gun
  M1* (1944). This is a real, named, dated US Army manual, but it describes
  **US organization, not British** — flagged below, not conflated with the
  British figure.
- ra39-45.co.uk, "6 pounder Gun" — https://ra39-45.co.uk/guns-equipment/6-pounder-gun
  — a dedicated Royal Artillery 1939–45 reference site; states the gun was
  "served by a crew of 6," consistent with Wikipedia's infobox, but gives no
  further role breakdown (no British-specific No.1/No.2/.../layer/loader
  table was found anywhere this session — see Open Questions).
- Airborne Assault Museum (paradata.org.uk), "Ordnance Quick Firing 6 Pounder"
  — https://paradata.org.uk/content/4663333-ordnance-quick-firing-6-pounder
  — also states "served by a crew of 6"; adds that the gun was adopted for
  airborne use, towed by an Airborne Jeep, and could be flown complete with
  its tow vehicle inside a Horsa glider; gives an effective range of ~1500m
  against early-war German tanks but notes it needed to close to within
  ~100m to threaten a Tiger with standard AP/APCBC shot (APDS, from 1944,
  changed this — already covered in `british_vehicles_1943.md`, not redone
  here).
- The Armourers Bench, "The 6pdr QF Anti-Tank Gun" (28 Apr 2019) —
  https://armourersbench.com/2019/04/28/the-6pdr-qf-anti-tank-gun/ — a
  hobbyist WWII-ordnance blog; states "manned by a six man crew" (third
  independent source agreeing on 6, no role breakdown); separately gives an
  organizational claim (see below) that a Royal Artillery anti-tank regiment
  was "initially used solely by the Royal Artillery's anti-tank regiments
  comprising of four batteries, each with 12 guns" (i.e. 48 guns/regiment),
  and that "by 1944 an infantry division would be equipped with as many as
  78 6pdrs and more than 30 heavier 17pdrs" (combining the divisional RA
  regiment's guns with all the infantry battalions' own AT platoons in that
  division). Also states the gun was mounted on trucks as "Portee" in North
  Africa (like the earlier 2pdr) and that AEC built the Mk I Gun Carrier
  ("Deacon") self-propelled 6pdr mount.
- ra39-45.co.uk, "Anti-Tank Regiments" —
  https://ra39-45.co.uk/organisation/anti-tank-regiments — states each
  infantry division had a single anti-tank regiment, comprising Regimental
  HQ and **three** A/T Batteries, each battery organized as a Battery HQ plus
  **four troops of four 6-pounders** (16 guns/battery, 48 guns/regiment
  before any 17pdr re-equipment) — a real, mild organizational conflict with
  the Armourers Bench figure immediately above (3 batteries × 4 troops × 4
  guns = 48, vs. "four batteries, each with 12 guns" = also 48 total, but a
  different battery/troop subdivision). Both agree on the same total gun
  count per regiment; they disagree on how it was subdivided into
  batteries/troops. Not resolved this session — flagged in Confidence Notes.
  The same page separately confirms the towed 17-pounder only "just started
  to appear" in 1943, with the 6pdr still the standard A/T-regiment weapon
  that year, and that Armoured Division anti-tank batteries (a related but
  distinct establishment) used half-tracks with a winch as gun tractors —
  not directly the infantry-division 6pdr picture, included for contrast only.
- `counters/toe/united_kingdom_1943.md` (**this project's own existing
  research**, already covering the British infantry battalion in detail) —
  checked first per the task brief, and it already documents the **infantry
  battalion's own Anti-tank Platoon** in exactly the level of detail needed:
  three Sections, each of two Detachments, each Detachment fielding **one
  towed 6-pounder plus two Loyd Carriers**, with a Bren for local defence and
  a 2-inch mortar for smoke/illumination — i.e. **6 guns per infantry
  battalion**, cited there to Kennedy's "Organization of the British Infantry
  Battalion 1938 to 1945" (bayonetstrength.uk), itself citing Infantry
  Training Part VI: The Anti-tank Platoon (18 Sep 1943) and the April 1943
  War Establishment II/233/2. This is genuinely new-to-this-file-but-not-new-
  to-the-project ground, exactly parallel to how the PaK40 file found the
  German regimental Anti-tank Company already partly covered by a sibling
  research file. **Not re-derived here — see that file directly.**
- Wikipedia, "Deacon (artillery)" — https://en.wikipedia.org/wiki/Deacon_(artillery)
  — confirms the AEC-built, fully self-propelled 6pdr mount ("Deacon") was
  built from December 1942 (175 built), used "only during the North African
  Campaign from 1942 to 1943," and was "withdrawn at the end of the campaign
  in North Africa" (i.e. by ~May 1943) — real, dated confirmation that the
  self-propelled/portee mobile-mounting era for the 6pdr was a North-African-
  specific, and specifically pre-mid-1943, phenomenon, not something that
  carried forward into Sicily/Italy.
- The Tank Museum (Bovington), several articles on the Robaa Valley action
  and on Tiger 131, cross-checked against tiger1.info and Warfare History
  Network — see Historical Validation Data below for full citation detail
  per anecdote, since the two candidate 1943 anecdotes found this session
  have very different confidence levels and are cited separately there.

## Crew Size

**6 men** — the figure that recurs, consistently and without any found
disagreement, across three independent sites (Wikipedia's infobox, ra39-45.co.uk,
Airborne Assault Museum) plus a fourth informal source (The Armourers Bench).
This is the **same figure already used for the PaK 40** in `pak40_1943.md`
(also 6, there sourced to Foss 1977) — a reassuring cross-check that "6" is a
reasonable, broadly-applicable towed-AT-gun detachment-serving-the-piece figure
for a WWII 57mm/75mm-class gun, not a number specific to one nation's gun.

No source found this session gives a British-specific named-role breakdown
(a "No.1 (gun commander/layer), No.2 (loader)..." table) the way the task
brief hoped for — this is a genuine gap, not an oversight (see Open
Questions). The only detailed, named-role breakdown found for this exact gun
anywhere this session is **American**, not British: the US Army's own field
manual for its own use of the same ordnance (as "57 mm Gun M1") describes a
**10-man crew** — squad leader, gunner (#1), four cannoneers (#2–5), three
ammunition bearers (#6–8), and a driver (#9) — per *FM 23-75* (1944). This
is a real, dated, named primary manual, but it is explicitly US Army
organization (larger, with dedicated ammunition bearers and a driver folded
into the same "crew" headcount) and should **not** be read across to the
British "crew of 6" figure as if they were describing the same thing — the
task brief's own distinction between "men who actually served the gun" and
"the full detachment complement including ammunition/transport personnel"
maps fairly naturally onto this British-6-vs-American-10 gap: the British "6"
almost certainly already means the gun-serving crew only (layer, loader,
etc.), with ammunition supply and prime-mover driving handled separately
(the infantry battalion's own Detachment, per `united_kingdom_1943.md`,
explicitly assigns **two Loyd Carriers** per gun Detachment — i.e. carrier
drivers are a separate, additional complement on top of the 6-man gun crew,
not counted within it), while the American 10-man figure appears to fold
ammunition bearers and the driver into one single "crew" number. Not
confirmed by a source that states this reasoning explicitly — a plausible
reading of the numbers, not a proven one.

## 1943 Organizational Context

Two real, independently well-documented 1943 organizational tiers were
found, closely paralleling the PaK 40 file's "two distinct tiers, both real"
structure for the German gun:

**1. The infantry battalion's own Anti-tank Platoon.** Already fully
documented in this project's own `counters/toe/united_kingdom_1943.md` — do
not duplicate here, just cross-reference: three Sections × two Detachments =
**6 guns per battalion**, each Detachment = 1× 6pdr + 2× Loyd Carrier + a
Bren + a 2-inch mortar, per the April 1943 War Establishment II/233/2 (via
Kennedy/bayonetstrength.uk). This is the organic, battalion-level tier — the
6pdr as the infantry's own integral anti-tank asset, present in every
standard British infantry battalion by spring 1943.

**2. The Royal Artillery Anti-Tank Regiment** — a divisional-troops (or
corps-troops) asset, one regiment normally allotted per infantry division,
separate from and in addition to the battalions' own platoons above. Per
ra39-45.co.uk: Regimental HQ + three A/T Batteries, each of four troops of
four 6pdrs (48 guns/regiment); per The Armourers Bench (a real but
unresolved conflict on the battery/troop subdivision, not the total): four
batteries of 12 guns each (also 48 guns/regiment). Both sources agree 1943
was still predominantly a 6pdr year for these regiments, with the 17pdr
"just start[ing] to appear" (ra39-45.co.uk) — i.e. a 1943-dated roster entry
correctly fields the 6pdr as this tier's standard weapon, not yet
predominantly the 17pdr. **72nd Anti-Tank Regiment, Royal Artillery** is a
specific, real, named example of this tier actually fighting with towed
6pdrs in January 1943 Tunisia (A Battery, Nos. 1 and 2 Troops) — see
Historical Validation Data below.

**A third, narrower context** worth flagging even though it is not the
"standard" 1943 picture: **airborne/airlanding use.** The Airborne Assault
Museum and Warfare History Network both independently describe 6pdrs of the
1st Airlanding Anti-Tank Battery being flown into Sicily by glider for
Operation Fustian (Primosole Bridge, July 1943) — the first time 6pdrs were
delivered into action by air. This is a real, well-documented, in-window
1943 event, but it represents a specialized Airlanding A/T Battery
establishment (different manning/gun-count than either tier above), not the
general infantry-division picture — noted for completeness/flavour, not
recommended as the basis for a general 1943 "Towed Anti-Tank Gun" roster
entry unless the project specifically wants an airborne-flavoured variant.

**Net read, matching the PaK40 file's own "net read" pattern:** a 6pdr in
British service in calendar-1943 could plausibbly belong to *either* of the
two main tiers above — the infantry battalion's own Anti-tank Platoon, or
the divisional Royal Artillery Anti-Tank Regiment — and both are
well-documented, real, and squarely 1943-appropriate. Unlike the PaK 40
file's German case (where the two tiers used different-calibre guns at
different points in 1943), **both British tiers used the identical 6pdr
gun** in 1943, so this ambiguity does not actually complicate fielding a
single "1943 6pdr Towed AT Gun" roster entry the way it did for the PaK 40 —
either organizational story supports the same weapon statistics.

## Crew Quality Tier

**Not found, genuinely — same conclusion as the PaK40 file reached for German
antitank crews.** No source located this session made any explicit,
citable claim about British 6pdr antitank gun crews (whether battalion
Anti-tank Platoon or Royal Artillery Anti-Tank Regiment) being rated
"veteran," "regular," or any other specific quality tier relative to
ordinary line infantry or field artillery. This project's own quality ladder
(Rule 17.3.6 area: Morale 7+ Elite, 6 Veteran, 5 Regular, 3–4 Green, ≤2
Militia) has no obvious anchor point found in the sources this session.

What can be said, honestly hedged: Royal Artillery anti-tank regiments in
1943 (like 72nd A/T Regiment at Robaa Valley) were **standing, trained
Regular Army or converted Territorial Army artillery units**, not hastily
raised or green formations — the Robaa Valley action itself (see below) is
routinely described in the sources found as a case of well-drilled gun-laying
and fire discipline (multiple guns coordinating fire on two separate Tigers,
achieving five separate penetrating hits on the second tank) rather than a
panicked or poorly-handled action. This is suggestive, informally, of at
least "Regular"-tier competence — but it is an inference from one
well-documented action's *outcome*, not a sourced statement about crew
training/quality classification, and should be presented to the designer as
such rather than as a settled fact. Nothing was found either way suggesting
these crews should be rated *above* the project's Regular baseline (i.e. no
source called them "veteran specialists" the way some wargaming lore
informally claims about German PaK crews, and no counter-claim was found
either).

## Historical Validation Data

**Two clearly distinct 1943 candidate anecdotes were found, with very
different confidence levels — flagging the difference explicitly, per this
project's own stated preference for honest hedging over invented detail.**

### Robaa Valley ambush, 31 January 1943, Tunisia — recommended anecdote

Well-documented across three independent sites (Warfare History Network's
"Operation Eilbote," The Tank Museum's "First Tiger I Knocked Out by the
British," and tiger1.info's "Tigers ambushed on the Robaa road"), all
converging on the same core facts:

- **Unit:** A Battery, 72nd Anti-Tank Regiment, Royal Artillery — Nos. 1 and
  2 Troops specifically named. British infantry present: 36 Infantry
  Brigade. Named officer: Lieutenant Stanley Edwards (troop commander).
- **German force:** six Tiger I tanks of 2. Kompanie, schwere
  Panzer-Abteilung 501, under Oberleutnant Löse, escorted by Panzer III tanks.
- **Action:** two 6pdr Mark II guns of No. 2 Troop engaged the leading Tiger
  "from the side" at a range described as "over 500m" (tiger1.info) and
  penetrated it; a third/fourth gun plus two more 6pdrs of No. 1 Troop
  engaged a second Tiger and penetrated its armour **five times**, putting
  it out of action; four accompanying Panzer III tanks were also knocked out.
  One Tiger (chassis/turret numbers "231"/"A2S" per tiger1.info) burned for
  over three hours and was later cut up for armour-sample and technical
  testing at Farnborough; the other, more lightly damaged Tiger was towed
  away and recovered by the Germans.
- **Historical significance, per tiger1.info's own framing:** "the defeat of
  a Tiger by ordinary field guns, for the first time on the Western Front" —
  i.e. this is a genuinely notable, citable, and clean 6pdr-vs-Tiger
  validation case, squarely within the project's 1943 window (31 January
  1943), and it is a **towed** anti-tank-regiment action (not a tank-vs-tank
  engagement, and not contested about which weapon fired the decisive shots
  the way the Tiger 131 case below is).

### Tiger 131 capture, April 1943, Tunisia — found, but explicitly NOT
recommended as a clean towed-6pdr anecdote

This is the single most famous British "6pdr defeats a Tiger" story in
popular literature (it is the tank now displayed at The Tank Museum,
Bovington), and it was the first hit returned by web search — but a careful
read of The Tank Museum's own more recent research (its "A Twist in the
Tale" article and its coverage of Dale Oscroft's research into his father's
2nd Battalion Sherwood Foresters) shows the popular "a towed 6pdr AT gun
jammed the turret" version is **contested by the Museum's own current
account**, not confirmed by it:
- Older/popular version (still repeated on many secondary sites): a 6pdr
  round scraped under the Tiger's 88mm barrel and lodged in the turret ring,
  jamming it, fired by a towed anti-tank gun.
- The Tank Museum's own "A Twist in the Tale" article instead states the
  disabling hit came from "a shell fired from a Churchill" (i.e. a
  **tank-mounted** 6pdr, not a towed AT gun) after testing/analysis.
- The Tank Museum's Dale Oscroft article gives yet a third detail: John
  Oscroft (2nd Sherwood Foresters) fired a **PIAT**, and the Foresters
  "turned around an anti-tank gun which they had captured in the fighting"
  (i.e., possibly a captured **German or Italian** gun, not a British 6pdr)
  and fired it at the Tiger; that same article separately says he was later
  told the disabling shot may have been from "an old French '75'."
- There is also a real, acknowledged date/location discrepancy across
  sources (21 April 1943 at Medjez-el-Bab per the older 48 RTR-centred
  account vs. 24 April 1943 at Point 174/Gueriat el Atach, ~15 miles away,
  per the newer Oscroft-informed account).

**Conclusion: do not use Tiger 131 as this roster entry's validation
anecdote.** It is real, dated, and extremely well-known, but The Tank
Museum's own current research does not actually support "a towed British
6pdr AT gun did it" as the settled account — at least three different guns
(a Churchill's own 6pdr, a captured enemy piece, and a French 75) are each
independently claimed as the one that jammed the turret, by the same
institution's own separate articles. Robaa Valley above is the cleaner,
uncontested choice.

### Secondary/backup context (not fully investigated in depth)

- **El Alamein / "Snipe," 26–27 October 1942** — the single most famous 6pdr
  anti-tank action of the entire war (2nd Battalion, The Rifle Brigade,
  reportedly knocked out 55+ Axis armoured vehicles with dug-in 6pdrs in one
  night action), per The Armourers Bench. **Outside this project's nominal
  1943 window by a few months**, but almost certainly the reason the 6pdr
  already had a strong reputation by the start of 1943 — worth keeping in
  mind as background/flavour even if not used as the dated validation case.
- **Battle of Salerno, 15 September 1943** — per Warfare History Network's
  "Crushing Counterattack at Salerno": during a German counterattack, ten
  AFVs of the Hermann Göring and 16th Panzer divisions overran a British
  D Company position, and "6-pounder anti-tank guns picked off the AFVs one
  by one." This is real, dated, in-window, and a genuine Italy-1943
  alternative to Robaa Valley if a Sicily/Italy-campaign flavour is
  preferred over a Tunisia one — but it was not investigated in the same
  depth this session (no specific unit/officer names or exact AFV types
  were pinned down beyond this summary).

## Deployment/Limbering Notes for Rule 17.1a

Rule 17.1a.4 models a towed AT gun's deploy/limber cycle on Rule 7.6
(HMG/mortar): deployed = M0 and able to fire, limbered = mobile but unable
to fire. This maps cleanly onto **one** of the two ways the 6pdr was
actually fielded in 1943, but not the other — worth flagging explicitly for
whoever builds this roster entry:

- **Conventional towed/dug-in use** (the infantry battalion Anti-tank
  Platoon's Loyd-Carrier-towed guns, and the Royal Artillery Anti-Tank
  Regiment's guns by the time of Sicily/Italy) fits Rule 17.1a.4's
  deploy/limber model perfectly — the Robaa Valley action itself is a
  textbook example of guns emplaced and camouflaged in an ambush position,
  engaging as targets came into range, exactly the tactical picture Rule
  7.6 already represents for an HMG or mortar team.
- **North African desert-war "Portee" mounting** (the gun carried and often
  fired directly from the bed of a truck) and the fully self-propelled
  **AEC "Deacon"** mount were both real, but specifically **early-to-mid-
  1943-and-earlier, North-African-theatre-specific** expedients — Wikipedia's
  "Deacon" article confirms Deacons were "withdrawn at the end of the
  campaign in North Africa" (i.e. by ~May 1943) and were not carried forward
  into Sicily or Italy. A 6pdr fielded this way behaves much more like a
  lightly-armoured vehicle (or an SP gun) than a towed weapon team, and
  **should probably not be represented via Rule 17.1a at all** if a
  specifically-North-African-desert-war 6pdr variant is ever wanted — that
  would need its own vehicle-style counter (M0/no-deploy, some notional AV),
  a different problem than the one Rule 17.1a solves. For a general 1943
  roster entry (as this task is scoped), the conventional towed/dug-in
  picture is by far the better-attested and more broadly applicable choice,
  and Rule 17.1a's existing deploy/limber model needs no special-casing to
  represent it.

No other 1943-specific timing peculiarity (e.g. an unusually fast or slow
historical emplacement/displacement time relative to the HMG/mortar baseline
Rule 7.6 already assumes) was found in any source this session — flag this
as "nothing notable found," not "confirmed absent."

## Confidence Notes

- **Crew size (6):** well-established — three independent sources agree
  with no disagreement found, and it matches the same figure already used
  for the PaK 40 in this project's own sibling research file. High
  confidence for the headline number; the *lack* of a British-specific
  role breakdown is a genuine, separately-flagged gap (see Open Questions),
  not a weakness in the "6" figure itself.
- **US 10-man crew (FM 23-75):** well-established as a real, dated, named US
  Army manual — but explicitly the wrong nation's organization; included
  only as cross-reference color, not as competing evidence against the
  British "6" figure.
- **Infantry battalion Anti-tank Platoon (6 guns/battalion, Loyd-Carrier-
  towed):** already well-established by this project's own existing
  `united_kingdom_1943.md` research (a primary-War-Establishment-derived
  figure, cross-checked against a second independent source there) — not
  re-verified from scratch this session, just cross-referenced, per the
  task brief's own instruction not to duplicate existing coverage.
- **RA Anti-Tank Regiment organization (48 guns/regiment):** the overall
  total (48 guns) is corroborated by two independent sources, but those same
  two sources give genuinely different battery/troop subdivisions (3
  batteries × 4 troops × 4 guns vs. 4 batteries × 12 guns) — a real,
  unresolved minor conflict, flagged rather than silently picking one.
- **72nd Anti-Tank Regiment at Robaa Valley:** well-established — three
  independent sites (a magazine-style history site, a national tank
  museum's own article, and a Tiger-tank-specialist reference site)
  converge on the same regiment, date, location, and broad sequence of
  events, with only minor numeric variation (e.g. exact engagement range,
  "penetrated five times" vs. general "knocked out"). One of the stronger,
  cleaner anecdotes found across this project's TOE research files to date.
- **Tiger 131:** the *event* (a Tiger captured intact in Tunisia, April
  1943, now at Bovington) is extremely well-established; what is genuinely
  **not** established, even by the Tank Museum's own current research, is
  which specific weapon (towed 6pdr AT gun / tank-mounted 6pdr / a captured
  enemy gun / a captured French 75) fired the disabling shot. Treated here
  as a real, documented case of **contested** primary attribution, not
  simply "unclear" — the Museum's own separate articles disagree with each
  other.
- **Salerno 6pdr anecdote:** single-source, moderate confidence — a named,
  dated magazine account, but not independently cross-checked against a
  second source this session, and no specific unit/officer names were
  pinned down.
- **Portee/Deacon phase-out timing:** the specific claim "Deacons withdrawn
  by end of North African campaign, ~May 1943" is well-sourced (Wikipedia,
  which is usually reliable on this kind of order-of-battle/production
  factoid and is consistent with the campaign's own known end date). A
  more granular claim surfaced during search — that specific batteries
  within a named regiment converted from "2 batteries portee + 2 Deacon" to
  "2 batteries towed 6pdr + 2 batteries towed 17pdr" specifically for
  Sicily — could not be traced back to a specific citable page before this
  session's web-search budget was exhausted; **treat that more granular
  claim as unverified** and rely instead on the more general, well-sourced
  Deacon-withdrawal date above.
- **Crew quality tier:** genuinely not found, exactly the same situation the
  PaK40 file already documented for German AT crews — presented here as an
  informal inference from one action's outcome (Robaa Valley), explicitly
  not as a sourced classification.

## Open Questions / Gaps for Follow-up

1. No British-specific named-role crew breakdown (a "No.1/No.2/.../layer/
   loader" table, analogous to the US FM 23-75 breakdown found for the same
   gun in US service) was found for the 6pdr in British Army use — a
   period British gunnery pamphlet (e.g. the Royal Artillery Training
   volumes cited elsewhere in this project's `pak40_1943.md`/`germany_1943.md`
   research for the German side) might close this if accessed directly.
2. The RA Anti-Tank Regiment's exact battery/troop subdivision (3×4×4 vs.
   4×12) was not resolved between the two sources that gave conflicting
   answers — both agree on 48 guns/regiment overall.
3. The more granular "2 batteries portee/2 Deacon → 2 towed 6pdr/2 towed
   17pdr for Sicily" claim surfaced during search but could not be traced
   to a specific citable source before the session's search budget ran out
   — worth re-attempting with a fresh search budget or a direct look at a
   specific regiment's own Wikipedia page (e.g. one of the several
   "Nth Anti-Tank Regiment, Royal Artillery" pages already found to exist)
   if a designer wants that level of Sicily-specific granularity confirmed.
4. No source was found rating 1943 British 6pdr AT gun crews (either tier)
   against this project's own Regular/Veteran/Green/Militia ladder — if the
   designer wants this gun's crew rated anywhere other than the project's
   Regular baseline, that would currently be a design decision, not a
   sourced fact, exactly as the PaK40 file already flagged for its own
   crew-quality question.
5. Tiger 131's true cause-of-jamming remains genuinely contested even in
   The Tank Museum's own current published material — not something this
   session could resolve, and probably not resolvable short of Dale
   Oscroft's full book (*Tiger 131: The Forgotten Battle*), which was not
   accessed this session.
6. The Salerno anecdote (15 September 1943, 6pdrs vs. a Hermann Göring/16th
   Panzer counterattack) was found via only one source and not
   cross-checked — a natural follow-up if the designer prefers an Italy-1943
   anecdote over the recommended Tunisia one.
