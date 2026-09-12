# Soviet 45mm Anti-Tank Gun M1937 (53-K) — Ballistics-Reuse Question, Crew, 1943 Organizational Context, and Deployment Notes

Research pass only, following the format of `counters/toe/pak40_1943.md` and
`counters/toe/sixpdr_1943.md` (this project's first two towed-AT-gun research
passes). This file gathers cited inputs for fielding the Soviet 45mm M1937
("53-K") as a 1943 "Towed Anti-Tank Gun" roster entry under Rule 17.1a, with
particular attention to the **ballistics-reuse question** the task brief
raised: whether the existing `t70_45l46_apbc` ("45mm 20K L46") curve in
`counters/armor_calc/data/guns.csv`, fitted for the T-70 light tank's own
tank-mounted gun, can be reused directly for the towed 53-K, or whether the
53-K needs its own separately-fitted curve.

`counters/toe/soviet_union_1943.md` (this project's own existing Soviet
research) was checked first, per the task brief. It is explicitly scoped to
the rifle squad/platoon/company only, and while it documents the
battalion-level **Anti-Tank Rifle Platoon** (PTRD/PTRS anti-tank *rifles*,
9 weapons) in detail, it says nothing about the 45mm anti-tank *gun* or the
battalion/division anti-tank-*gun* echelon at all. This file's ground is
genuinely new to the project, not a duplicate of existing coverage.

## Sources

- Wikipedia, "45 mm anti-tank gun M1937 (53-K)" —
  https://en.wikipedia.org/wiki/45_mm_anti-tank_gun_M1937_(53-K) — pulled
  both as rendered text and as raw wikitext (`action=raw`) to check the
  infobox and body prose directly, the same technique used in this project's
  PaK 40 research. Infobox: barrel **2.07 m (46 calibers)**, muzzle velocity
  **760 m/s (2,493 ft/s)**, elevation −8° to 25°, rate of fire 15–20 rpm,
  split-trail carriage, **37,354 units built 1937–1943**, production
  **ceased in 1943**. Body prose: developed as "essentially an improved
  version [of the] 19-K anti-tank gun mounted on a 37 mm 1-K anti-tank gun
  chassis" by designer M.N. Loginov of Plant No. 8, accepted into service
  24 April 1938. Organizational sentence (quoted in full below). Combat
  sentence: guns supplied to Republican Spain, used by the International
  Brigades' British Anti-tank Battery of the XV Brigade from the Battle of
  Brunete onward; on the Eastern Front, "saw service in [the] first stage of
  the German-Soviet War, but their anti-armor capabilities allowed them to
  fight successfully only with German light tanks and armored personnel
  carriers. Early models of the Panzer III and Panzer IV could also be
  knocked out at close range, but this put Soviet artillerymen in greater
  danger." No crew figure appears anywhere in the infobox or body — checked
  directly in the raw wikitext, not just the rendered page.
- Wikipedia, "45 mm anti-tank gun M1932 (19-K)" —
  https://en.wikipedia.org/wiki/45_mm_anti-tank_gun_M1932_(19-K) — the
  53-K's direct predecessor. Gives an **identical** barrel spec to the 53-K
  (2.07 m, 46 calibers, 760 m/s / 2,500 fps for AP) — flagged as a real,
  unresolved oddity below (Confidence Notes), since the 53-K is elsewhere
  described as an "improved version" of the 19-K. Critically for this task's
  ballistics question, this article states directly: **"The gun was
  installed in tanks under the name 45 mm tank gun model 1932 (20-K)"** —
  i.e. Wikipedia's own account of the family history describes the
  tank-mounted 20-K not as a separately-developed gun, but as this exact
  towed-gun design re-mounted for tank use, with a semi-automatic breech
  added in 1934 and "same ammunition" as the towed gun. It further states
  the tank gun "later evolved into the 45 mm tank gun model 1938" (paired
  chronologically with the 53-K M1937 generation of the towed gun), and —
  the single most directly relevant sentence found this session — that
  "during 1941–42, surplus [tank-gun] M1938 barrels were adapted to trailer
  carriages as field anti-tank pieces to replace combat losses," i.e. actual
  tank-gun barrels were physically remounted as towed AT guns during the war.
- Wikipedia, "45 mm anti-tank gun M1942 (M-42)" —
  https://en.wikipedia.org/wiki/45_mm_anti-tank_gun_M1942_(M-42) — the
  53-K's direct sourced successor ("developed as an upgrade of the 45mm
  M1937 (53-K)"), used here as the nearest documented family cross-reference
  for the crew-size and 1943-performance questions the 53-K's own page
  leaves open. Infobox: **crew = 6**; barrel lengthened "20 calibers more
  than the previous one" to 66.3 calibers/2.985 m; muzzle velocity 870 m/s
  (2,854 fps). Body prose, quoted in full: "In 1943, due to its insufficient
  anti-armor capabilities against new German tanks such as the Tiger,
  Panther and Panzer IV Ausf H, the M-42 was partially replaced in mass
  production by the more powerful 57 mm ZiS-2 anti-tank gun," but it
  "remained in production however, as it was quite effective against
  lighter vehicles and could pierce the side armour of the Panther and
  Panzer IV Ausf H." No source found this session gives a citation footnote
  for the crew=6 infobox figure specifically (checked the raw wikitext
  directly) — an uncited infobox number, same confidence tier as several
  other single-source figures already accepted elsewhere in this project's
  TOE files.
- Wikipedia, "T-70" — https://en.wikipedia.org/wiki/T-70 — confirms the
  T-70's gun (the basis of this project's existing `t70_45l46_apbc` row) as
  "45 mm 20K mod. 1932–34 tank gun" in the infobox, but the article's own
  prose instead calls it "a 45-mm L/46 gun Model 38" — a real, minor
  internal inconsistency in Wikipedia's own naming (mod. 1932–34 vs. Model
  38) not resolved this session, though both namings agree on the 46-caliber
  barrel length that matches the 53-K exactly.
- Wikipedia, "Komsomolets" (T-20 armoured tractor) —
  https://en.wikipedia.org/wiki/Komsomolets_(armoured_tractor) — confirms
  this vehicle was "designed to tow light artillery pieces such as the 45mm
  anti-tank gun." Crew/capacity: 2 in the driving compartment (driver,
  commander) plus 6 in the rear troop compartment (the gun's own serving
  crew and ammunition handlers), 8 total; could tow "the weapons themselves
  plus a small quantity of ammunition, usually towed in a limber," with
  capacity to tow two limbers for extra ammunition; max speed 50 km/h,
  range 250 km. Production: "approximately 4,401 T-20 tractors were built
  between 1937 and 1941" — i.e. production had already ended two years
  before this project's 1943 window, meaning any Komsomolets towing a 53-K
  in 1943 would necessarily be a surviving pre-1942-built vehicle from an
  already-attrited pool, not a newly-issued type.
- Wikipedia, "266th Rifle Division" — https://en.wikipedia.org/wiki/266th_Rifle_Division
  — gives a dated snapshot (December 1942, "just before it fought in
  Operation Little Saturn") of a real division's full equipment roster:
  "10,163 officers and men, who were equipped with 7,229 rifles, 931
  submachine guns, 250 light machine guns, 81 heavy machine guns, 188
  mortars, **30 45mm anti-tank guns, and 44 76mm cannon or howitzers**." Used
  below as an independent arithmetic cross-check against the 53-K page's
  own battalion/division organizational figures.
- Wikipedia searches for named Soviet corps/army-level anti-tank artillery
  formations ("Fighter Anti-Tank Artillery Brigade/Regiment/Division," the
  standard English rendering found on Wikipedia for *istrebitelno-
  protivotankovaya artilleriya*/IPTAP) turned up real, named examples —
  8th, 9th, 12th, 13th, 15th, 20th, and 24th Anti-Tank Artillery Brigades
  (attached to the 13th, 11th, 61st, 8th, 5th Shock, and 46th Armies
  respectively, per their army pages); the 1073rd, 1075th, 530th, 437th,
  and 368th Fighter Anti-Tank Artillery Regiments (5th Guards Army, 28th
  Army, 46th Army, and 15th Tank Corps pages); and a "259th separate
  fighter-anti-tank artillery division" (from a search-result snippet
  attached to a person named Ivan Yakovlev — a namesake's Wikipedia article
  was fetched by mistake and did not actually cover this military figure or
  unit; **not independently confirmed beyond the search snippet**). This
  confirms the corps/army/RVGK-level IPTAP tier was real and already a
  named organizational category by 1943, but **no gun-count, battery
  structure, or gun-caliber breakdown for any specific one of these units
  was recoverable this session** — every unit page checked (5th Guards
  Army, 13th Army) lists the brigade/regiment by name only, with no
  composition detail, and the ones checked that do give a "Structure" list
  with these regiments (5th Guards Army) date that list to 1 May 1945, not
  1943.
- Wikipedia, "Battle of Kursk," "Battle of Kursk order of battle," "Battle
  of Prokhorovka," and "Ponyri" — all checked directly for any 45mm-gun-
  specific or IPTAP-specific 1943 narrative. **None of the four contained
  any mention of the 45mm gun, IPTAP, or a named Fighter Anti-Tank Artillery
  unit.** The Kursk order-of-battle article's only relevant general
  statement is that infantry anti-tank teams (not gun crews) were "mostly
  effective against the Ferdinand tank destroyers, which lacked machine
  guns as secondary armament" — a real, dated 1943 Kursk fact, but about
  infantry close-assault teams, not the 45mm gun. This is a genuine gap,
  flagged rather than papered over — see Historical Validation Data below.
- Wikipedia, "Tiger I" — https://en.wikipedia.org/wiki/Tiger_I — checked for
  any mention of the Soviet 45mm gun among weapons capable of threatening
  it. **The 45mm gun is not mentioned anywhere in this article** — only the
  57mm ZiS-2, 76mm F-34, 85mm D-5T, and 122mm D-25T appear as Soviet guns
  discussed in relation to the Tiger. Treated below as indirect corroboration
  of the 45mm gun's inadequacy against heavy German armor, not as a direct
  statement of it (the article simply never brings the 45mm gun up).
- `docs/source/section_18__vehicle_combat_resolution.rst`, note (f) —
  this project's own existing precedent and reasoning for reusing one
  fitted gun curve across multiple closely-related gun-family members
  (KV-1S/ZIS-5 reusing the F-34 curve; SU-85/D-5S reusing the T-34/85's
  D-5T curve; StuG III reusing the Panzer IV's KwK40 curve directly). Quoted
  and applied directly to the 53-K/20-K question below.
- `counters/armor_calc/data/guns.csv`, row `t70_45l46_apbc` — the existing
  fitted curve in question: "45mm 20K L46," ammo_family `apbc`, projectile
  diameter 45mm, **muzzle velocity 2493 fps**, K-factor 3613, confidence
  note "2-pt interpolated fit (Woodman table, Sov 45mm AP — up from 1-pt
  rough anchor)."
- `counters/toe/soviet_union_1943.md` — this project's own existing research,
  checked first per the task brief (see intro above); confirmed to be
  scoped to company-and-below infantry organization only and to not cover
  the 45mm AT gun, the battalion/division AT-gun echelon, or IPTAP at all.

## Ballistics: Reuse `t70_45l46_apbc` Directly — Recommended, No New Curve Needed

**Recommendation: reuse the existing `t70_45l46_apbc` curve directly for the
towed 53-K. No new gun curve, and no new calibration/ballistics research,
is needed.**

The case here is at least as strong as — arguably stronger than — this
project's own existing precedent for this kind of reuse (`section_18.rst`
note (f), the KV-1S/ZIS-5↔F-34, SU-85/D-5S↔D-5T, and StuG III↔KwK40
substitutions). That precedent's own wording sets the bar at "a direct
evolution... with closely comparable ballistic performance." The 53-K/20-K
relationship clears that bar and then some:

1. **The sourced muzzle velocity matches exactly.** The 53-K's own Wikipedia
   infobox gives 760 m/s = **2,493 fps** — the identical number, to the
   foot-per-second, already sitting in `guns.csv`'s `t70_45l46_apbc` row.
   This is not a coincidental near-match the way, say, the PaK 40's two
   790/792 m/s readings were — it is the same published figure.
2. **The barrel length matches exactly**: both the 53-K (towed) and the
   20-K family (tank-mounted, as fitted to the T-70) are independently
   sourced at 46 calibers / 2.07 m.
3. **Wikipedia's own family history describes them as the same gun, not
   merely a "closely comparable" one**: the 19-K/53-K article states
   plainly that "the gun was installed in tanks under the name 45 mm tank
   gun model 1932 (20-K)" — i.e., the tank gun is presented as this towed
   gun re-mounted, with only breech/recoil/carriage engineering changes
   ("semi-automatic breech" added in 1934) and explicitly "same ammunition."
4. **The two roles were literally, physically interchangeable at least once
   during the war**: the same source states that "during 1941–42, surplus
   [tank-gun] M1938 barrels were adapted to trailer carriages as field
   anti-tank pieces to replace combat losses" — meaning actual 20-K tank-gun
   barrels were, at least in this documented case, mounted onto towed
   carriages and fired as 53-K-equivalent guns. This is a stronger, more
   literal basis for curve-sharing than anything cited for the KV-1S/ZIS-5
   precedent, which relies on family resemblance rather than a documented
   literal barrel swap.

**One nuance worth flagging, though it doesn't change the recommendation:**
the 53-K's immediate predecessor, the 19-K (M1932), is given an *identical*
barrel-length/muzzle-velocity spec (2.07 m/46 cal, 760 m/s) on its own
Wikipedia page, even though the 53-K is elsewhere described as "an improved
version" of the 19-K. Read together with the 53-K's own page describing its
improvement as being "mounted on a 37 mm 1-K anti-tank gun chassis" (i.e., a
carriage/mobility change, not a barrel/ballistics change), the likeliest
reading is that the 53-K's real improvement over the 19-K was in carriage
weight and towing characteristics, not muzzle velocity or penetration — but
this was not independently confirmed against a source that states that
reasoning explicitly, and it is also possible the two Wikipedia articles
have simply cross-repeated the same number. **This does not affect the
reuse recommendation**, since the number that matters here (53-K's own
sourced MV) already matches `guns.csv`'s existing figure exactly regardless
of how the 19-K compares.

Also worth flagging for whoever eventually re-runs a fit: `guns.csv`'s own
confidence note for `t70_45l46_apbc` ("Woodman table, Sov 45mm AP") is
already generic to the Soviet-45mm-AP family, not specific to whether its
two calibration points came from 53-K-fired or 20-K-fired test data in the
first place — in other words, this reuse question was implicitly already
answered "yes, they're interchangeable" by whoever built the original T-70
curve; this research pass just makes that reasoning explicit, sourced, and
citable rather than leaving it an unstated assumption.

## Crew Size

**Not directly sourced for the 53-K itself** — checked the article's raw
wikitext directly (not just the rendered infobox) and no crew figure
appears anywhere on the page, the same genuine gap this project has already
hit and flagged for the 6pdr's lack of a British-specific role breakdown.

Two independent lines of family/circumstantial evidence converge on **6**:

- The M-42 — the 53-K's own direct, explicitly-sourced successor/upgrade —
  gives **crew = 6** in its infobox (uncited within the article itself, but
  a specific stated figure, not a guess).
- The Komsomolets armored tractor, the standard 1943-era mechanized tower
  for this exact gun, carries 2 crew of its own (driver, commander) plus
  **6** more men in its troop compartment — independently implying a 6-man
  serving/ammunition-handling crew being transported to the gun position,
  from a source that has nothing to do with the gun's own infobox.

This lands on the same number as the PaK 40 and 6pdr's own converging
6-man figure, but the confidence tier here is genuinely lower than either
of those: this is an inference from a successor gun's infobox plus a prime
mover's troop capacity, not a directly-cited figure for the 53-K M1937
itself. Recommend fielding at 6 for consistency with the project's other
two towed-AT-gun entries, but flag this explicitly as inferred-by-analogy,
not directly sourced, when the roster entry is built.

## 1943 Organizational Context

**Directly quoted from the 53-K's own Wikipedia page:** "Two such guns were
employed as an anti-tank platoon, organic to each rifle battalion.
Additionally twelve guns were in anti-tank battalions of each rifle
division." This gives two organic tiers, both real:

1. **Rifle battalion's own Anti-tank Platoon** — 2 guns per battalion. With
   3 battalions per regiment and 3 regiments per division, this puts
   **18 guns** at the battalion/regimental echelon across a full-strength
   rifle division. (This project's own `soviet_union_1943.md` documents the
   battalion's separate 9-weapon PTRD/PTRS Anti-Tank *Rifle* Platoon in the
   same battalion structure — the 45mm-gun platoon found here is a
   different, additional unit, not the same one under another name.)
2. **Rifle division's own organic Anti-tank Battalion** — 12 guns, a
   divisional-echelon asset separate from the battalion-level platoons
   above (directly parallel to the PaK 40 file's divisional
   Panzerjäger-Abteilung and the 6pdr file's Royal Artillery Anti-Tank
   Regiment — a higher tier holding more guns than the organic small-unit
   allocation).

**Independent arithmetic cross-check, found this session:** 18 + 12 = 30,
which matches exactly the 266th Rifle Division's own real, dated (December
1942) equipment snapshot of **"30 45mm anti-tank guns"** for the whole
division — a genuinely useful corroboration, since it comes from a
completely different Wikipedia article (a specific division's own history)
rather than restating the 53-K page's own claim.

3. **A third, higher tier exists and is real, but its 1943 composition is
   not well-documented in the sources checked this session**: corps/
   army/RVGK-level "Fighter Anti-Tank Artillery" brigades, regiments, and
   (from 1943) at least one separate division — this project's own English-
   language rendering of *istrebitelno-protivotankovaya artilleriya*/IPTAP.
   Multiple real, named examples were found (8th/9th/12th/13th/15th/20th/
   24th Anti-Tank Artillery Brigades; 1073rd/1075th/530th/437th/368th
   Fighter Anti-Tank Artillery Regiments; a 259th separate fighter-anti-tank
   artillery division from 1943), confirming this tier definitely existed
   as a distinct, named category by 1943 — but **no gun-count, battery
   structure, or specific-gun-caliber breakdown for any of these named
   units was found this session**, and none of the Kursk-specific articles
   checked (Battle of Kursk, its order of battle, Battle of Prokhorovka,
   Ponyri) named any of them in a 1943 combat narrative. This is a genuine,
   flagged gap, not a claim that the tier didn't matter at Kursk — it
   almost certainly did, given how central IPTAP anti-tank defense was to
   Soviet Kursk doctrine in the broader secondary literature — but nothing
   citable to that effect was recovered this session.

**Net read, matching the PaK40/6pdr files' own "net read" pattern:** a 53-K
in the field in calendar-1943 could plausibly belong to any of three tiers
— the rifle battalion's own platoon, the rifle division's own AT battalion,
or a corps/army-level Fighter Anti-Tank Artillery Brigade/Regiment — and
all three are confirmed real for 1943. The first two are well-documented
down to gun counts and cross-checked by independent arithmetic; the third
is confirmed to exist by name but not documented in composition detail this
session.

## Crew Quality Tier

**Not found, genuinely — the same conclusion this project's PaK40 and 6pdr
files already reached for their own guns' crews.** No source located this
session made any explicit, citable claim rating Soviet 45mm AT gun crews
(either the organic battalion/division tier or the IPTAP tier) against this
project's own Morale-based quality ladder. A dedicated search for a
commonly-repeated informal claim (that Soviet AT gunners received elevated
pay/decoration status reflecting the hazard and importance of the role, tied
to the "istrebitel"/"destroyer" branch name) returned no matching source
this session — flagged as a real informal claim that circulates in
secondary literature, but genuinely unconfirmed here, not asserted as fact.
Same recommendation as the other two towed-gun files: if the designer wants
this gun's crew rated above/below the project's Regular baseline, that is
currently a design decision, not a sourced fact.

## Historical Validation Data

**No single, dated, named 1943 combat anecdote (a specific engagement,
unit, or officer) was found this session for the 53-K** — a real gap,
matching the same honest conclusion this project's PaK40 file already
reached for its own gun. Four different Kursk-specific Wikipedia articles
(Battle of Kursk, its order of battle, Battle of Prokhorovka, and Ponyri)
were checked directly and none mentioned the 45mm gun, IPTAP, or a named
Fighter Anti-Tank Artillery unit at all.

**What was found instead is a general, sourced statement of the gun's
limitations by 1943** — and, per the task brief's own framing, this is a
genuinely useful finding in its own right, not a consolation prize for a
missing kill story:

- The 53-K's own Wikipedia page states it "saw service in [the] first stage
  of the German-Soviet War, but their anti-armor capabilities allowed them
  to fight successfully only with German light tanks and armored personnel
  carriers. Early models of the Panzer III and Panzer IV could also be
  knocked out at close range, but this put Soviet artillerymen in greater
  danger" — a real, sourced statement of the gun already being
  under-gunned relative to *contemporary* (early-war) medium tanks, before
  the 1943-era Tiger/Panther generation even entered the picture.
- The M-42 (the 53-K's direct successor, itself just a longer-barreled,
  higher-velocity descendant of the same basic round/mount) is explicitly
  stated to have had, by 1943, "insufficient anti-armor capabilities
  against new German tanks such as the Tiger, Panther and Panzer IV Ausf
  H" — a real, sourced statement dated exactly to this project's 1943
  window, for a gun that outperforms the 53-K ballistically (66.3-caliber
  barrel and 870 m/s vs. the 53-K's 46-caliber barrel and 760 m/s). If the
  *better* 45mm gun was already judged inadequate against Tiger/Panther by
  1943, the older, slower 53-K a fortiori shares that limitation, and more
  severely.
- Indirect corroboration: Wikipedia's own "Tiger I" article, in discussing
  which Soviet guns could threaten it, never mentions the 45mm gun at all
  — only the 57mm ZiS-2, 76mm F-34, 85mm D-5T, and 122mm D-25T appear.
  This is silence, not a direct statement, but it is silence in an article
  that otherwise makes a point of naming every Soviet gun considered
  relevant to the Tiger question.
- A separate, real, dated fact worth noting for context (though not
  specifically about the 45mm gun): the 53-K's own page states the "mass
  production of outdated model 1937 guns was stopped in 1943" — meaning a
  1943-dated 53-K roster entry is fielding a gun that was, in that same
  calendar year, being phased out of production in favor of the M-42. Guns
  already in the field (37,354 built in total, 1937–1943) certainly
  remained in widespread front-line service through the year — this is a
  reasonable inference given the scale of existing stock, not a directly
  sourced statement that they did — but this is worth flagging plainly:
  fielding the 53-K specifically (rather than the M-42) for a 1943 scenario
  is historically defensible for most of the year but sits right at the
  gun's own production sunset.

**Recommended framing for this roster entry's validation data, if the
project wants one:** present the M-42/Tiger-Panther statement above as the
honest 1943 "limitation" finding this gun's story actually supports,
explicitly flagged as a general assessment rather than a specific dated
engagement — the same honest choice the PaK40 file made when no specific
kill anecdote could be found for that gun either.

## Deployment/Limbering Notes for Rule 17.1a

The 53-K's **split-trail carriage** (confirmed directly in its own
Wikipedia infobox) is standard towed-AT-gun geometry and fits Rule
17.1a.4's deploy/limber model (M0 deployed/able to fire, mobile/unable to
fire while limbered) without any special-casing needed — the same
conclusion this project already reached for the PaK 40 and 6pdr.

One genuinely distinct, 53-K-specific wrinkle worth flagging: this gun's
standard mechanized prime mover, the Komsomolets (T-20) armored tractor,
was **out of production from 1941 onward** (4,401 built total, 1937–1941).
Any Komsomolets towing a 53-K in this project's 1943 window would
necessarily be a surviving pre-1942-built vehicle from an already-attrited
wartime pool, not a currently-produced type — meaning by 1943, horse-drawn
or man-hauled towing (neither confirmed nor ruled out by any source found
this session, but the more likely default given the shrinking mechanized-
tractor pool) plausibly predominated for an "average" 1943 53-K, in
contrast to the 6pdr file's own finding that the 6pdr's early-war
"Portee"/self-propelled mountings were a genuine but time-boxed phenomenon.
This is the mirror-image situation: here it's the *mechanized* towing
option that was the fading, pre-1943 peak rather than the ascendant 1943
norm. Not confirmed by any source stating this explicitly as a trend —
an inference from the Komsomolets' own bounded production run, flagged as
such.

No other 1943-specific emplacement/displacement-time peculiarity was found
this session — flagged as "nothing notable found," not "confirmed absent,"
matching this project's existing convention for this kind of negative
result.

## Confidence Notes

- **Ballistics reuse (`t70_45l46_apbc` for the towed 53-K):** high
  confidence. The sourced 53-K muzzle velocity (760 m/s / 2,493 fps) matches
  the existing `guns.csv` row's value to the foot-per-second, the barrel
  length (46 calibers) matches exactly, and Wikipedia's own family history
  explicitly describes the tank-mounted 20-K as this exact towed-gun design
  re-mounted with the same ammunition — plus a documented case of literal
  tank-gun-barrel-to-trailer-carriage conversion in 1941–42. This clears
  the bar set by this project's own existing KV-1S/SU-85/StuG III gun-curve-
  reuse precedent with more direct evidence than that precedent itself
  cites.
- **19-K/53-K identical-spec oddity:** flagged, not resolved — the 53-K's
  predecessor (19-K) carries an identical barrel-length/MV figure on its
  own Wikipedia page despite the 53-K being called an "improved" gun
  elsewhere; likeliest explanation (the 53-K's improvement being in
  carriage/mobility, not ballistics) is plausible but not confirmed by a
  source stating it directly. Does not affect the reuse recommendation.
- **Crew size (6):** moderate-to-low confidence — not directly sourced for
  the 53-K itself (checked the raw wikitext directly, genuinely absent),
  inferred from the M-42 successor's infobox and the Komsomolets tractor's
  troop capacity. Lower confidence than the PaK40's single Foss-1977-cited
  figure or the 6pdr's three-independent-site convergence, though it lands
  on the same number as both.
- **Organic battalion (2 guns) + division AT battalion (12 guns) = 18+12=30
  total:** well-established — a direct quote from the 53-K's own Wikipedia
  page, independently cross-checked by a real division's (266th Rifle
  Division) own dated December 1942 equipment snapshot matching the
  arithmetic exactly. One of the cleaner organizational cross-checks found
  across this project's TOE research files to date.
- **Corps/army-level IPTAP tier (Fighter Anti-Tank Artillery Brigades/
  Regiments/Divisions):** the tier's *existence* by 1943 is well-established
  (multiple independently-named real units found), but its internal
  composition (gun counts, battery structure, gun-caliber mix) is
  genuinely not documented in any source checked this session — a real,
  flagged gap, not a claim that the tier is unimportant.
- **Crew quality tier:** not found at all, matching both sibling files'
  own honest conclusions for their respective guns.
- **Historical validation (Kursk-specific anecdote):** genuinely not found
  — four different Kursk-specific Wikipedia articles were checked directly
  and none named the 45mm gun or an IPTAP unit. The general 1943
  "insufficient anti-armor capabilities against Tiger/Panther" finding
  (sourced to the M-42's page, applied a fortiori to the older/slower 53-K)
  is offered as an honest substitute, explicitly flagged as a general
  assessment rather than a specific dated engagement.
- **Komsomolets mechanized-towing note:** the vehicle's own production span
  (1937–1941) is well-sourced; the inference that this made mechanized
  towing increasingly uncommon for the 53-K specifically by 1943 is
  reasonable but not directly stated by any source found this session.

## Open Questions / Gaps for Follow-up

1. No source found this session gives a named-role crew breakdown (a
   "No.1/No.2/.../layer/loader" table) for the 53-K specifically, the same
   kind of gap the 6pdr file flagged for British service — a period
   Soviet artillery manual, if accessed directly, might close this.
2. The apparent 19-K/53-K identical-ballistics-spec discrepancy on
   Wikipedia (see Confidence Notes) was not resolved — worth a direct
   check against a dedicated ordnance reference (e.g. a Russian-language
   *Boepripasy* volume or a Zaloga/Osprey title on Soviet anti-tank
   artillery) if the designer wants it closed rather than flagged.
3. No gun-count/battery-structure breakdown was found for any specific
   named Fighter Anti-Tank Artillery Brigade/Regiment/Division — a
   follow-up with access to Glantz/Ness's *Red Army Handbook* (already
   cited as a source behind this project's own `soviet_union_1943.md`, via
   Kennedy) or a dedicated Soviet-OOB site might close this.
4. No specific, dated, named 1943 combat instance (a particular unit,
   officer, or engagement) involving the 53-K was found — the M-42/Tiger-
   Panther limitation statement is a real, honest substitute but is a
   general assessment, not an anecdote. A source with an actual unit war
   diary, or a dedicated book on Kursk's anti-tank defenses, was not
   accessed this session and is the natural next step.
5. Whether the informal claim that Soviet AT gunners received elevated
   pay/decoration status was ever true, and if so whether it's citable, was
   searched for and not found this session — flagged as unconfirmed folk
   knowledge, not fact, exactly as this project already treats the informal
   "veteran PaK crew specialists" claim in the PaK40 file.
6. The Komsomolets-towing-versus-horse-towing balance specifically for
   1943 (as opposed to the vehicle's general 1937–1941 production window)
   was not directly sourced — flagged as a reasonable inference, not a
   confirmed fact, in the Deployment/Limbering section above.
