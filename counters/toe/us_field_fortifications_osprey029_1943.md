# US Field Fortifications 1941-53 — Gordon L. Rottman (Osprey Fortress 29)

## Sources

- Gordon L. Rottman, *US World War II and Korean War Field Fortifications
  1941-53* (Osprey Fortress 29, 2005), 64pp of content (67pp including
  covers/ad pages). Real extractable text layer, confirmed via `pdftotext`
  — read in full as text via `pdftotext -layout`, all 64 content pages.
  This is the first sourcing pass against Rule 21.7 (Fortification
  Building) and Rule 21.7a (Basic Entrenchment, Any Unit) in
  `section_21__engineers_and_assault_specialists.rst`, which currently has
  **no sourcing file behind it at all** — a real, previously unflagged
  gap, opened by this pass rather than closing an already-logged question.
  Design note E.114 built Rule 21.7a from general reasoning ("real WWII
  infantry dug their own foxholes constantly") with no specific citation;
  this file is the first attempt to check that reasoning, and Rule 21.7's
  turn-count table, against a dedicated source.
- Book scope note: explicitly covers both World War II (1941-45) and the
  Korean War (1950-53), by the author's own framing. Cited page numbers
  below are the book's own printed page footers, not PDF file-index
  numbers, resolved against `pdftotext -layout`'s page-number markers.
  Introduction through "Types of emplacements" (pp.4-46) is WWII-primary
  or era-neutral doctrine/construction material — the manuals it discusses
  (FM 5-15 editions of 1940, 1944, 1949) span the WWII-to-Korea transition
  and are cited accordingly. "Theater specific defenses" (pp.47-53)
  separates cleanly by theater: North Africa, Italy, Northwest Europe, and
  the Pacific sections are WWII; the Korea section (pp.53-56) is flagged
  as Korea-only wherever cited. "The test of battle" (pp.56-61) contains
  one WWII case study (2d Ranger Infantry Battalion at Pointe du Hoe,
  Normandy, June 6-7 1944, pp.57 and 59) and one Korea case study (a
  rifle-company ridge strongpoint, January 1953, pp.59-61) — the Korea
  case study is not used below. The closing "assessment" (p.63) reads as
  WWII-and-Korea-general.

## Findings

### 1. Real historical time figures — a genuine, moderate-confidence affirmation of the game's compression, not a clean negative

The book gives two real, citable time figures for hasty positions, and one
strong qualitative data point for the far end of the scale (elaborate,
"deliberate" positions) that the game's own Fortification tier does not
have an equivalent citable figure for:

- **Hasty positions in general:** "Field fortifications were classified as
  either hasty or deliberate. Hasty positions could be constructed
  quickly, **usually under an hour**, with infantry hand tools. They
  provided minimal protection and made maximum use of existing cover... and
  concealment" (p.31).
- **The most basic hasty position specifically (the skirmisher trench,
  the WWI-era precursor to the foxhole, still discussed as a fallback):**
  "The trench could be dug in **10-12 minutes** in soft soil, providing
  adequate protection from small-arms fire, but not from artillery or
  mortars" (p.31, repeated in a photo caption on the same page).
- **No equivalent citable figure exists for the standard 1944-pattern
  one-/two-man foxhole** (the book's actual period-correct "entrenchment,"
  with a 4-5ft firing step, sump, and 6in.-high parapet, pp.31-32) or for
  a full engineer-built "deliberate" position. The closest the book comes
  is qualitative: "A company remaining in a position for **five or so
  days** could develop a formidable defense. More often, defenses were
  occupied for limited periods, often just overnight" (p.15) — a
  benchmark for what real, thorough field fortification effort looked
  like when time allowed, measured in days, not minutes.
- **Net read against the project's implied figures:** the game's ~4-10
  min (engineer) / ~8-20 min (infantry) entrenchment figures land in
  roughly the same order of magnitude as the book's "under an hour" for
  hasty positions generally and "10-12 minutes" for the crudest scrape —
  a genuine, moderate-confidence affirmation that the entrenchment stage's
  abstraction is not wildly implausible. The full **Fortification** stage
  (an additional 4 engineer turns, ~8-20 more minutes) is a much larger
  compression relative to the "five or so days" benchmark for a truly
  developed position — but the book itself frames that benchmark as the
  exception ("more often... just overnight"), not the norm, and
  explicitly notes that "even though time and resources did not always
  allow these ideal emplacements to be built, they still served as guides"
  (p.25) and that positions were "seldom elaborate or heavily constructed,
  but in most cases they were sufficient for their purpose" (p.63,
  assessment section). This is reported as a real, uncomfortable data
  point, not smoothed over — but it does not by itself justify changing
  Rule 21.7.4's turn counts, since the book's own "five days" figure
  describes a different, more thorough end-state than what a FORT marker
  represents, and the game's stated turn length (2-5 real minutes,
  Rule 2.2.1) is already an explicit abstraction rather than a literal
  clock.

### 2. Engineer vs. ordinary-infantry division of labor — a partial match, and one real tension worth flagging

The book does **not** describe an engineer-vs-infantry skill split shaped
like Rule 21.7a.2's cap (engineers can push a position past basic
Entrenchment; ordinary infantry cannot). Instead it describes a
division of labor by *task type*, not by *depth of the same task*:

- **Infantry built its own fighting positions, at any level of
  elaboration, including over multi-day periods:** "The infantry was
  responsible for planning and constructing its own defenses including
  obstacles. Combat engineers when necessary provided materiel and
  technical assistance. Infantry leaders were trained to establish
  integrated defensive positions and the troops had ample opportunity to
  practice their establishment during field exercises" (p.11). The same
  page describes the attached engineer company's actual habitual role as
  "mainly employed to maintain supply routes, make road repairs, and
  assist with obstacle and mine clearance," with fortification-related
  help limited to "other tasks permitting... rear area facilities such as
  CPs, ASPs, communications centers, and other facilities requiring heavy
  construction" (p.11) — i.e. rear-area and specialist-materiel
  structures, not upgrading a rifle platoon's own forward foxholes into
  a "fortification."
- **The book's closing assessment confirms engineers COULD build
  substantial fortifications, but usually didn't need to for
  front-line infantry positions:** "The US had sufficient engineer,
  equipment, and materiel capabilities to construct substantial field
  fortifications and obstacles when necessary. Most units though relied
  on their own somewhat limited resources for construction tasks.
  Infantry field fortifications, usually occupied for short periods only,
  were seldom elaborate or heavily constructed, but in most cases they
  were sufficient for their purpose" (p.63).
- **This is a genuine, citable tension with Rule 21.7a.2's specific
  framing**, not a contradiction of the general premise that engineers
  have real specialist capability. The rule assumes engineers are the
  ones who physically arrive and push a dug-in infantry position from
  Entrenchment to Fortification; the book's actual division of labor has
  infantry digging and improving their own positions indefinitely (given
  time), with engineers more often doing separate categories of
  work (obstacles, mines, heavy rear-area construction, "materiel and
  technical assistance") rather than taking over a forward foxhole
  personally. **Not applied here** — this doesn't rise to "extremely
  strong, unambiguous justification" for changing 21.7a.2's engineer-only
  cap, since the book also affirms engineers had the *capability* for
  more substantial work the rule's higher tiers represent, and the game
  needs some mechanical way to make engineer presence matter. Flagged for
  the coordinator below as a real nuance, not resolved.
- **Hasty-vs-deliberate is a real, book-native distinction** and does map
  reasonably well onto the project's Entrenchment/Fortification
  progression in spirit, if not in exact engineer/non-engineer terms: "Field
  fortifications were classified as either hasty or deliberate... Deliberate
  positions required more effort and the use of additional construction
  materials... Such positions were continuously improved for as long as
  they were occupied" (p.31). This supports the general idea of a
  multi-stage improvement track (Rule 21.7.4's table), independent of who
  is doing the digging.
- **One inviolate-rule data point supports Rule 21.7a's core premise
  directly:** "Troops in the field seldom had the manual to hand and
  training in building field fortifications was limited, emphasizing
  instead offensive operations and the employment of mobile weapons. **An
  inviolate rule though was that everyone dug in when halted**, usually
  just a simple prone shelter" (p.25). This is a strong, direct affirmation
  of Rule 21.7a's founding premise (E.114) that ordinary infantry dug in
  on their own as a matter of course — though it also suggests the
  *training* gap between infantry and engineers was less about physical
  capability to dig a hole (any soldier could and did) and more about
  materials, technique refinement, and available manuals, a softer
  distinction than the rule's flat turn-count doubling implies.

### 3. "Any fire result stops work, all progress lost" (Rule 21.7.3) — clean negative

No passage in the book describes enemy fire specifically interrupting an
in-progress dig and forcing troops to abandon and restart accumulated
work. This is a clean negative for a citable real-world basis for Rule
21.7.3's specific mechanic. The book's closest related material describes
a different pressure — time and daylight, not enemy fire — forcing
positions to be built incomplete or abandoned unfinished:

- Pacific theater doctrine: if darkness fell before a day's advance halted
  with enough daylight left to dig in, units "found themselves attempting
  to dig foxholes, assign sectors of fire, emplace early warning devices,
  coordinate with adjacent units, register artillery and mortar fires, and
  resupply in the dark" (p.52) — a time-pressure account, not a
  fire-interrupts-work account.
- "Units were supposed to fill their holes when moving on, but time did
  not always permit" (photo caption, p.17) — again a time/resource
  constraint, not an enemy-fire interruption, and describes abandoning a
  position when *leaving* it, not losing progress while building it.
- The Pointe du Hoe case study (Finding 5 below) has the Rangers dig their
  foxholes *before* German attacks began, during a lull — consistent with
  Rule 21.7.1's rule-guide premise that fortification is a preparation-phase
  activity rather than something usable reactively during active combat,
  but not a citation for the specific "any fire result during this turn
  wipes all invested time" mechanic.

### 4. Cover-value / protection-level data — real and quantified, but for a different kind of number than the project's abstract cover bonus

The book gives one genuinely precise, quantified table relevant to
protection levels, but it measures something different from (and
narrower than) the project's Appendix B / Section 4 abstract cover-bonus
scale:

- **"Safe thickness of material" table (p.23)**, based on live-fire
  testing of the US .30-cal M1 ball round (explicitly noted as "slightly
  more powerful than the German 7.92mm, Japanese 7.7mm, and Communist
  7.62mm") at 200 yds against typical fortification construction
  materials — maximum penetration and a recommended safe thickness for
  each: armor plate 0.3in./0.5in. safe; concrete 2in./3in.; brick masonry
  5in./7in.; gravel 8in./10in.; dry sand 12in./14in.; moist sand
  14in./18in.; solid oak 20in./24in.; earth loam 30in./36in.; greasy clay
  60in./72in. (varies greatly). This is a real, small-arms-specific
  penetration/protection figure, not a game-scale cover bonus, but it does
  support the general principle that earth/sandbag construction (this
  project's basic Entrenchment) reliably stops small-arms fire with a
  modest thickness, while true artillery/direct-hit protection (the kind
  implied by Cover +8 "Fortification") requires much more substantial
  construction.
- **Two layers of sandbags provided protection from small arms and
  fragments** (p.23) — a simple, low-effort threshold, consistent with an
  early/basic stage of the project's cover progression.
- **Parapets "required to be at least 3ft thick to protect from small
  arms"** for open-topped fighting positions (p.26) — again a small-arms
  specific figure.
- **A fully-specified cut-and-cover shelter (the deliberate/elaborate end
  of the scale) could have "almost 7ft" of layered overhead cover** when
  "built to full specifications," providing "excellent protection from
  all but direct hits by heavy artillery and bombs" — but "it might be as
  little as 2ft" in practice, with "the degree of protection desired,
  time, and materiel resources" determining how much of the full design
  was actually built (p.26). This supports the *qualitative* direction of
  the project's Entrenchment (+6) → Fortification (+8) jump — a real,
  large step up in protection between "some earth cover" and "protection
  from all but direct hits by heavy artillery" — without giving a number
  translatable into the project's specific +2 cover-point delta.
- **A separate mortar/artillery-caliber-vs-bunker-effectiveness passage**
  (light mortars ineffective against bunkers, medium mortars more
  effective, heavy mortars much more effective, light artillery limited
  effect, medium artillery [150mm+] needed for a high degree of effect
  against well-prepared fortifications, p.26) is flagged as mixed
  WWII/Korea in framing — it appears in the same paragraph as a specific
  note about post-WWII Korean bunkers built "6-8ft thick," and uses
  "Communist" alongside "German" ordnance labels, suggesting the author
  is describing a general principle spanning both wars rather than a
  WWII-only data point. Usable only as loose qualitative support, not a
  precise WWII-dated figure.
- **Net read:** real, quantified protection data exists in this book, but
  it answers "how thick does material need to be to stop a bullet or
  shell fragment" rather than "how much abstract Cover bonus should this
  stage of fortification carry" — the two are not directly convertible
  without a modeling assumption this file does not attempt to supply. No
  citation here is strong enough to justify changing any Cover-value
  number in Appendix B / Section 4 or Rule 21.7.4, and none is proposed.

### 5. A dated, named anecdote — Pointe du Hoe, June 1944 (not 1943, but usable)

- **Best candidate found:** the 2d Ranger Infantry Battalion's defense at
  Pointe du Hoe, Normandy, the night of **June 6-7, 1944** (pp.57, 59) —
  not this project's 1943 baseline, but a real WWII date, as the brief
  allows. After the famous cliff assault, roughly 225 Rangers (companies
  D, E, and F plus a headquarters detachment, joined later by a 23-man
  platoon from Company A, 5th Ranger Battalion) held a position south of
  the battery, with "the Rangers dug their foxholes along the hedgerows.
  One-man foxholes were used, but they were closely spaced" (p.57). The
  position held through two German probing attacks that night before a
  third, heavier attack at 0300 hours penetrated the line at a weakly
  held angle; by dawn only about 90 of the original 225 men were combat
  effective, relieved on D+2 by the 116th Infantry (p.59). The book's own
  analysis attributes the defeat mainly to decentralized command and poor
  communication rather than a fortification failure per se — "The study
  of this small action reinforces the importance of many of the basic
  principles of an effective defense... A lack of centralized command and
  poor communications were key failures" (p.59).
- **Honest caveats on this candidate:** it is dated and unit-attributed
  (2d Ranger Infantry Battalion, specific companies) with an exact date,
  but it is June 1944, not 1943, and its lesson is more about command
  structure than about fortification mechanics specifically — it
  illustrates that dug-in positions were established during a lull before
  contact (consistent with Rule 21.7.1) and that even a hastily
  established, closely-spaced line of foxholes could hold through
  multiple attacks before failing for non-fortification reasons, but it
  is not a clean demonstration of any single Rule 21.7/21.7a mechanic.
- **A weaker, non-anecdotal alternative:** the Driniumor River, New
  Guinea action (112th Cavalry Regiment and elements of the 127th/128th
  Infantry, July 1944, p.51) is dated and unit-attributed but is a
  river-defense-line battle summary, not a foxhole/entrenchment-specific
  story, and was not pursued further here.
- **No 1943-dated combat anecdote was found in this book at all** — the
  book's only other named/dated action is the Korea-era Combat Outpost
  Carson fight (1st Marine Division, May 26, 1953, p.54), explicitly
  outside this project's WWII scope and not used.

### 6. Other findings relevant to Rule 21.7/21.7a mechanics

- **Terrain/cover improvement (Rule 21.7.1) — real support for the
  "irregularity in the ground adds cover" principle underlying Field
  Position (Rubble → Field Position, Rule 21.7.4's table):** "Soldiers
  were taught that any irregularity in the ground, even a fold or dip of
  0.5ft, added to the cover" (p.31), and "irregularly spread and profiled
  parapets made it more difficult for the enemy to detect firers" (p.41)
  — general doctrinal support for treating irregular/improvised cover
  (rubble, folds in terrain) as real, if lesser, protection, consistent
  with Rule 21.7.4's "Rubble → Field position... counts as entrenchment"
  row.
- **Multi-unit combined effort (Rule 21.7.5) — no explicit "N workers
  halve the time" doctrine found**, but the book does document real
  labor-scaling activity: a 27-man ammunition-and-pioneer platoon's tool
  set (250 D-handle shovels, 125 pick-mattocks, and more) "could be
  loaned to rifle companies to increase their field fortification and
  obstacle construction capabilities" (p.13) — consistent with the
  general idea that more hands/tools speed up fortification work, though
  not a citable basis for the specific halving formula.
- **Terrain that defeats digging entirely — a real, uncited-by-this-project
  mechanic worth flagging as a possible future addition, not applied
  here:** "Exceedingly hard, rocky, or frozen ground proved to be
  virtually impossible to dig in with infantry hand tools. Blasting was
  necessary" (sidebar, p.25), with a described procedure (starter hole,
  progressively larger demolition charges) and a specific 1943 detail —
  "0.5 and 1 lb TNT (the latter not available until 1943)" was among the
  standard charge sizes used. This doesn't affect Rule 21.7/21.7a as
  written (which has no terrain-quality modifier), but is worth noting
  for the coordinator as a real, well-documented mechanic (hard/rocky/
  frozen ground blocking hand-tool entrenchment entirely, requiring
  demolitions instead) that this project's fortification rules don't
  currently model at all. Not proposed as a change here — out of this
  file's scope to design a new sub-rule, just flagged as a real gap this
  research surfaced.
- **The FORT-marker "state" concept (Rule 21.7.5) is well supported by
  the book's own hasty/deliberate framing** — positions were
  "continuously improved for as long as they were occupied" (p.31) rather
  than built once and left, matching the marker's role as tracking a
  position's current improvement state rather than a one-time event.

## Confidence Notes

- Real, machine-extractable text layer (confirmed via `pdftotext`), read
  in full via `pdftotext -layout`, all 64 content pages, not sampled or
  image-inspected. High confidence in the transcriptions and page
  attributions above; page numbers were cross-checked against the book's
  own printed page-footer sequence as it appears in the extracted text
  (verified via a full page-marker scan of the extracted text file, not
  estimated from PDF file position).
- This book is a strong genre match for this pass — a construction- and
  doctrine-focused field-fortification reference is exactly the right
  kind of source for Rule 21.7/21.7a's questions, unlike some other
  general-history or photo-compendium sources this project has found to
  be the wrong genre for numeric questions (e.g. `military_sniper_pegler_1943.md`'s
  Finding 3 on AMO, or the Encyclopedia of Weapons of WWII precedent cited
  there). That said, the book still does not give a single figure that
  converts cleanly into "turns required" or "Cover bonus granted" at this
  project's specific scale — its time and protection figures answer
  adjacent, real-world questions (how long does a scrape trench take;
  how thick must earth be to stop a rifle bullet) rather than the game's
  own abstracted units, so findings are reported as order-of-magnitude
  plausibility checks, not direct numeric confirmations.
- Finding 2 (engineer vs. infantry division of labor) is reported as a
  genuine, unresolved tension rather than smoothed into either "confirms
  the rule" or "the rule is wrong" — the book supports both engineers
  having real additional capability (assessment section, p.63) and
  ordinary infantry doing virtually all of their own front-line digging
  in practice (p.11, p.25), and reconciling those two truths into a
  specific engineer-only cap at exactly "beyond basic Entrenchment" is
  this project's own game-design choice, not something the book itself
  states or contradicts directly.
- Finding 5's Pointe du Hoe anecdote is explicitly flagged as June 1944,
  not 1943 — reported honestly per this project's own convention rather
  than rounded off to fit the project's usual 1943 baseline.

## Open Questions / Gaps for Follow-up

1. **Terrain-quality modifier for fortification (Finding 6):** the book
   documents hard/rocky/frozen ground as capable of blocking hand-tool
   entrenchment entirely, requiring demolitions instead — Rule 21.7/21.7a
   has no equivalent terrain-quality gate today. A future pass could
   consider whether this is worth a new sub-rule (e.g., certain terrain
   types blocking or slowing Rule 21.7/21.7a entirely without engineer
   demolition support) — not designed or proposed here, just flagged as a
   real mechanic this research surfaced that the current rule doesn't
   model.
2. **Engineer/infantry division-of-labor tension (Finding 2):** left
   exactly as ambiguous as the book leaves it. A future pass with a
   different source (a period field-fortification manual excerpt, or a
   unit history describing an engineer squad specifically taking over an
   infantry-dug position) could try to find a citation that more directly
   supports or challenges Rule 21.7a.2's specific engineer-only cap on
   Fortification/Reinforced Building/Field Position — not resolved here.
3. **No 1943-dated anecdote found.** The Pointe du Hoe candidate
   (Finding 5) is the strongest usable anecdote from this book, but it is
   June 1944. If the coordinator wants a flavor-text or design-note
   anecdote specifically dated to 1943 for Rule 21.7/21.7a, this book does
   not supply one — a different source would be needed.
4. **No citable numeric basis found for Rule 21.7.3's "any fire result
   loses all progress" mechanic** (Finding 3) — this remains a design
   abstraction with no real-world citation behind it, from this book or
   (per E.114) any prior pass. A training/doctrine manual describing
   digging specifically interrupted by incoming fire (rather than by
   darkness or time constraints, which this book does document) would be
   the more promising lead for a future pass.
5. No changes were made to `units.csv`, any calculation pipeline, or any
   numeric value in Rule 21.7/21.7a as part of this pass — see the
   corresponding design note (E.151) for what was and was not applied to
   the rule text.
