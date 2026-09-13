# World War II Infantry Tactics: Company and Battalion — Dr Stephen Bull (Osprey Elite 122)

## Sources

- Dr Stephen Bull, *World War II Infantry Tactics: Company and Battalion*
  (Osprey Elite 122, 2005), 67pp. Real, confirmed extractable text layer
  (verified via `pdftotext -layout`, not an image scan) — read in full via
  `pdftotext -layout`, cross-checked page-by-page against the PDF's own
  form-feed page breaks to recover accurate printed page numbers. Cited
  page numbers below are the book's own printed page footers, not PDF
  page indices.
- Book scope note: this is a general (German/British/US), multi-theatre
  company/battalion-echelon doctrine and tactics reference — explicitly
  the second half of a two-part study, the companion squad/platoon volume
  being *World War II Infantry Tactics: Squad and Platoon* (Osprey Elite
  105, not held in this library). Same author as
  `jungle_warfare_rottman_1943.md`'s source (E.152) — filed here for the
  first time against this project's own core Sections 5-9 (Regular/Assault
  action economy, fire resolution, Close Assault) and Section 22
  (scenario design), rather than a terrain or roster question. This is a
  **validation/refinement pass against existing core mechanics**, not a
  new-unit-type or gap-closing thread — no `units.csv` row was ever a
  candidate outcome of this pass.
- Covers company/battalion attack doctrine (German, British, US),
  machine-gun support, mortars, mines, anti-tank tactics 1939-42 and
  1943-45, infantry AT guns, motorized infantry (Panzergrenadiers/US
  Armoured Infantry/British motor battalions), and tank/infantry
  co-operation, plus eight full-page colour plates (A-H) with a detailed
  prose commentary section ("The Plates," pp.60-64) explaining each.

## Findings

This pass checked the book against all six prompted areas. It speaks
directly and substantively to five of them; the sixth (turn/impulse
pacing) is addressed only thinly, reported as a near-clean-negative rather
than stretched.

### 1. Company/battalion attack doctrine — real, detailed support for the base-of-fire/maneuver-element shape behind Rule 6.3.3 and Rule 8.3

The book gives a genuinely strong, cross-national match for the general
shape of this project's fire-and-maneuver design, at multiple echelons,
though (as expected of a doctrine reference) never in this project's own
abstract "1 hex bound / half eFP" units.

- **German doctrine names the pin-then-assault sequence explicitly, in
  three phases** (p.7): *Niederhalten* ("pinning down the enemy with the
  lead elements, up to a company in strength, with support from machine
  guns and mortars, while reconnaissance was completed and assault units
  were deployed"), *Blenden* ("'dazzling' the defenders with shooting and
  smoke, denying them observation, and hampering their firing"), and
  *Niederkampfen* ("winning the fire fight and beating down the enemy,
  culminating in the actual assault into the enemy position"). This is a
  real, named, doctrinal pin-suppress-then-close sequence — the same
  overall shape as this project's fire-resolution-then-Close-Assault
  pipeline, though it describes company-level phases unfolding over an
  entire engagement, not a single unit's two-part-action turn.
- **The clearest single passage in the whole book is the US Army's own
  explicit statement of the design principle Rule 6.3.3/8.3 exist to
  model** (p.14, quoting *Infantry Battalion*, 1944): "the battalion
  attacks by combining fire and manoeuvre to close with the enemy...
  Fire weakens the enemy by inflicting casualties and neutralises his
  elements by forcing them to take cover... Through manoeuvre, the
  battalion increases its fire effect by decreasing range... by
  manoeuvre, also, the battalion advances its attacking echelon close
  enough to the hostile position to permit their assault to be made with
  hand grenades and the bayonet." Fire and maneuver are explicitly
  separate functions here, exactly as the Assault economy's two part-actions
  are — this is doctrine independently describing the same two-function
  split this project's mechanic already encodes.
- **A real base-of-fire/maneuver-element split at platoon level**, matching
  Rule 8.3's fire-group concept (units combining fire onto one target
  while others move): the British Plate G commentary (pp.62-63, "British
  Platoon Attack on Strongpoint, 1944," closely copied from the manual
  *Infantry Training* 1944) names No.1 Section explicitly as "**the fire
  section for this attack**" — it "bring[s] the target under heavy and
  sustained Bren and small arms fire, and smoke bombs from the 2in mortar.
  They will remain in these positions throughout the attack, firing until
  the assault sections are just short of the objective" — while No.2 (the
  "cut-off section," reinforced with a PIAT crew and attached assault
  pioneers) and No.3 (the "clearing section") maneuver forward under that
  covering fire to breach the wire and close with the objective. This is a
  clean, named, textbook example of exactly the division of labour Rule
  8.3's fire-grouping and Rule 6.3.3's Assault economy jointly represent —
  some units fire (and, per Rule 8.3, combine their fire into one group),
  while others bound forward — though real doctrine assigns this split
  *between* sub-units of a platoon, not *within* one unit's own two-part
  turn the way Rule 6.3.3 does for a single activated unit.
- **The US battalion-level equivalent** (Plate E commentary, pp.61-62,
  "US Battalion Attack, 1944-45"): A Co is "the main assault company,"
  supported by the fire of the Heavy Weapons Company "past its flanks and
  overhead"; B Co, "masked by smoke," puts in "a secondary 'holding'
  attack to pin down the defenders by fire"; C Co "waits in support."
  As the assault develops, "B Co fights its holding action, laying down
  fire to pin down the defenders... preventing them from attacking the
  flank of the assault companies," while "Hvy Wpns Co... 'displaces' to
  follow the assault companies" — a real, named example of fire (B Co,
  Hvy Wpns Co) covering maneuver (A Co, then C Co passing through to
  outflank).
- **A single-unit-level parallel closest to Rule 6.3.3's own alternating
  Assault Move/Assault Fire shape**, and the pass's clearest, most direct
  hit on the "fire suppresses" design identity (see Finding 3 below): the
  Panzergrenadier half-track's own tactics (p.50) — "the half-track could
  also operate 'fire and movement', dashing from cover to cover while
  engaging with its MGs... short bursts fired on the move were intended to
  **force the enemy under cover and suppress his return fire**." This is
  a single vehicle/squad alternating movement and reduced/opportunistic
  fire within one continuous action, doctrinally stated to aim at
  suppression rather than casualties — the shape (though not the specific
  numbers) Rule 6.3.3's Assault Move/Assault Fire pairing abstracts.
- **A real, if much shorter, "short rush" bound figure**, not directly
  convertible to this project's 1-hex (40-yard) Assault Move but a genuine
  data point on real small-unit rush distances: the British "pepperpot"
  method (p.9) had sections break into three sub-groups that "advance
  independently, running about 20 yards before dropping down again,"
  intended to present "only fleeting and dispersed targets." Real
  individual-rush bounds (≈20 yards) are shorter than this project's
  abstract 1-hex/40-yard Assault Move bound, which is unsurprising — the
  game's bound represents an entire unit's activation, not one soldier's
  single dash, and 20 yards is well within the margin the abstraction is
  entitled to compress.
- **Verdict: the general two-function (fire/maneuver) shape behind Rule
  6.3.3 and Rule 8.3 holds up well and gains genuine, repeated, named
  doctrinal support across three armies and two echelons.** No specific
  number (the 1-hex bound, the half-eFP halving, or Rule 8.3's per-unit
  falloff-then-sum method) is confirmed or contradicted by this book —
  as expected, no tactics manual quantifies its own abstraction the way a
  wargame must — but the underlying design choice to split a unit's
  action into a reduced move and a reduced fire, and to let units combine
  fire into groups while others move, is not merely unfalsified but
  actively mirrored by real doctrine at every echelon this book covers.

### 2. Real frontage/spacing/depth figures for standard (non-jungle) terrain — a genuine Section 22 lead, parallel to `jungle_warfare_rottman_1943.md`'s Finding 6

Section 22 currently has no unit-frontage or spacing guidance of any kind
for a standard (non-jungle) map — only force ratios (22.2), terrain
density bands (22.4), turn-limit estimates (22.5), and setup-zone
*separation* minimums (22.9.3, which govern distance *between* the two
sides, not how one side's own units should be spaced across a map). This
book supplies real, repeatable, citable company/battalion-echelon
frontage and depth figures that a scenario designer could use to lay out
a historically plausible map — the standard-terrain equivalent of Finding
6's jungle-specific "no linear front line" doctrine and Australian
unit-spacing figures.

- **Battalion attack frontages, both sides:** German battalion attacks
  "were frequently made on a narrow frontage of 400 to 1,000 metres" with
  a specific point of main effort, the *Schwerpunkt* (p.7). The US
  equivalent: "a battalion was capable of delivering 'a powerful attack'
  on a frontage of 500 to 1,000 yards" (p.14). At this project's own
  tactical scale (40 yards/hex, per Section 22.1's Scale example), these
  convert to roughly **11-27 hexes** (German) and **12.5-25 hexes** (US)
  of battalion frontage — real, if rough, figures a designer could use to
  size a map for a battalion-scale assault scenario, distinct from (and
  larger than) the worked Farmhouse-at-Prokhorovka example's 6×6 hex
  skirmish map.
- **Echelon depth and control measures:** "The distance between echelons"
  (leading and second/reserve echelons within a US battalion attack) was
  "commonly 100 to 200 yards" (p.14) — roughly **2.5-5 hexes**. Phase
  lines, used to control a US battalion's advance, were "commonly 1,000
  to 2,000 yards apart" under normal visibility (p.14) — roughly **25-50
  hexes**, a figure large enough to sanity-check that this project's
  smaller scenario maps represent a single bound of a much larger
  advance, not a full phase-line-to-phase-line movement.
- **Defensive spacing, in-depth (anti-tank), and all-round protection at
  the small-unit level:** late-war German AT-nest doctrine recommended AT
  teams "about 150 yards apart, in two staggered lines, throughout the
  defensive position" (≈3.75 hexes), engaging armour at "no more than 75
  yards" (≈2 hexes) once it penetrated between nests (p.46) — a real
  defense-in-depth figure, not merely a linear one. Separately, an AT
  gun's own position was to be sited "within company localities, and
  close to a platoon post for all-round protection" (p.48) since the
  detachment would have "little chance" against infantry attack alone —
  direct evidence that individual weapon positions relied on nearby
  infantry for close protection, a real texture point for scenario setup
  (a lone AT gun on a map without infantry support nearby is historically
  implausible). The Plate C2 commentary ("Reinforced squad position,"
  p.61) gives a concrete perimeter figure: an outer ring of "barbed wire
  and anti-tank mines would typically ring the position about 50 yards
  out from the trenches" (≈1.25 hexes) and the position was "designed to
  be defensible against attack from almost any direction, the weapons
  being turned as required" — genuine all-round-defense doctrine at
  squad/platoon scale.
- **A real, if partial, complication for the jungle thread's own "no
  linear front line" finding:** at the *company/battalion* echelon
  specifically, this book's Plate H2 commentary ("Reinforced battalion
  position," p.63, copied from the US Handbook on German Military Forces,
  March 1945) describes a genuinely **linear** arrangement, not an
  all-round one: "Three company strongpoints forward, in line;
  headquarters co-located with fourth company, level with the artillery
  area." Standard (non-jungle) battalion defense in this source is
  organized as a recognizable front line of forward company positions
  with a reserve/HQ echelon behind it — the opposite emphasis from
  Rottman's jungle-specific "there will seldom, if ever, be a time when a
  definite line will separate the area under friendly control from that
  in the hands of the enemy" (E.152's Finding 6). All-round defense in
  *this* book operates at the individual strongpoint/squad level (Plate
  C2, above) within an overall linear battalion framework, not as a
  substitute for a front line the way jungle doctrine describes. This is
  reported as a genuine, useful nuance for any future Section 22
  addition, not a contradiction of E.152's finding — the two books are
  describing different terrain regimes, and a future "unit spacing/no
  linear front" addition to Section 22 should distinguish jungle
  scenarios (where the front genuinely dissolves) from standard-terrain
  ones (where a recognizable, linear company-strongpoint front line with
  a reserve echelon behind it is itself the norm this book documents).

### 3. "Fire suppresses, manoeuvre kills" (Rule 8.5.3a) — the strongest, most explicit support found in this entire research thread

This book gives this project's single best piece of doctrinal evidence
yet for its own stated core design identity. The p.14 quotation given in
full under Finding 1 states, almost point for point, the same division
Rule 8.5.3a claims for its dice mechanics: **fire's job is to inflict
casualties on some men and force the rest to ground ("neutralises...by
forcing them to take cover"), while it is maneuver's job to actually close
with and destroy/capture the position** ("by manoeuvre... the battalion
advances its attacking echelon close enough... to permit their assault to
be made with hand grenades and the bayonet"). The Panzergrenadier
half-track passage (p.50, Finding 1) makes the same point in miniature and
even more explicitly names the intent: fire "on the move" was there "to
force the enemy under cover and **suppress** his return fire," not
primarily to kill. The German fire-fight's own three-phase structure
(p.7) reads the same way: two of its three phases (*Niederhalten*,
*Blenden*) are explicitly about pinning/dazzling — denying the enemy's
ability to fight back — with the actual destruction/capture reserved for
the third phase (*Niederkampfen*) after the fire fight is already won.
No passage in this book treats fire alone as expected to annihilate a
defending position without a subsequent physical assault — every attack
description in the book, German, British, and US alike, treats fire as
the enabling/suppressing function and the physical advance to contact as
the decisive one. **This validates Rule 8.5.3a's core claim cleanly and
directly — this is not a hedged or comparative finding, it is as close to
a clean positive as this research thread has produced for any single
mechanic.**

### 4. Reserve/reaction-force doctrine — real support for the underlying principle, but at a different echelon than Rule 6.4's Interrupt

The book gives genuine, repeated doctrine on holding back and committing
a reserve, most explicitly in the same p.14 passage: "it was desirable to
hold back a reserve to exploit enemy weakness, or to strike the final
blow. Depending on the information available, this could vary from a
single platoon up to two whole companies. Perhaps the most common
arrangement was to commit one company each to the main and secondary
attacks, keeping the third back to reinforce the main thrust or turn a
flank." Plate E's commentary (p.62) shows this in action: C Co "waits in
support," then, once A Co has broken in, "has come forward and passed
through A Co, wheeling right to outflank the enemy line" — reserve
committed at a chosen moment to exploit an opportunity created by the
main attack.

This is real, genuine validation of the *principle* behind holding back
combat power and committing it reactively at a decisive moment — the same
spirit Rule 6.4's Interrupt mechanic expresses. But it should be reported
honestly as validating that principle at a **different, coarser echelon**
than Interrupt operates at. The book's reserve doctrine is a
battalion-commander-level decision made once (or a few times) per
engagement, about committing an entire held-back company or platoon at a
chosen operational moment. Rule 6.4's Interrupt is a fine-grained,
per-impulse tactical reaction available to any eligible unit, spending RP
to seize a single action out of turn. Both share the underlying
"hold strength back, commit it when it matters most" logic, but this book
does not speak to — and this pass does not claim it speaks to — the
specific unit-level, impulse-by-impulse mechanics Rule 6.4 encodes. This
is reported as a real, positive, but partial and echelon-mismatched
finding, not a precise validation of Interrupt's own procedure.

### 5. Turn/impulse pacing (Rule 2.2.1, Rule 7.1.2) — thin, close to a clean negative

This book gives almost nothing usable for sanity-checking this project's
2-5 minute turn / 20-25 second impulse scale. The only figure found with
any bearing on real-time pacing is a preparation-phase estimate, not an
in-contact action-pacing one: German battalion attacks were "expected to
take no more than 40 minutes from striking an obstruction to the assault"
(p.7) — a real, dated figure, but describing the whole reconnaissance
-to-assault preparation phase of an entire battalion attack, an
operationally much coarser unit of time than this project's single
2-5-minute game turn or 20-25-second impulse. It neither confirms nor
meaningfully complicates Rule 2.2.1/7.1.2's tactical-scale figures — the
two describe different scales of the same battle (an hours-long
preparation phase vs. a single bound within the fire fight that follows
it), and treating the 40-minute figure as evidence either way would be
stretching it past what it actually measures. **Reported as a genuine,
honest near-miss: this book was not the right source for this specific
question**, the same way `jungle_warfare_rottman_1943.md` reported a
clean negative on its own Japanese-sniper sub-question rather than
straining to manufacture a result.

### 6. Dated 1943 combat anecdotes for future flavor-text/design-note use

- **Ortona, December 1943** (p.61, Plate D1 commentary, "'The Killing
  Ground': German street fighting in defence, 1943"): "based on positions
  held by German paratroops around a single square in the Italian city of
  Ortona, encountered by 1st Canadian Division in December 1943; but it
  is representative of German tactics for urban defence on all fronts."
  A real, dated, named-unit (1st Canadian Division), named-place (Ortona)
  anecdote, squarely within this project's 1943 baseline and at exactly
  the company/battalion echelon this pass targets.
- Two Normandy machine-gun anecdotes were also found and are worth
  recording for future use despite falling just outside the 1943 window
  (both 1944): Lt Sydney Jary (B Coy, 4th Bn Somerset Light Infantry)
  recalling a stalled advance near Mont Pincon under concentrated Spandau
  fire from "about twelve machine guns firing at one time" (p.16); and
  Pte W. Evans, 1st Royal Norfolks, describing a German pillbox machine
  gun cutting down his company in a Normandy cornfield (p.16). Both are
  named, dated to the year, and vivid, but 1944 rather than 1943 — flagged
  per this project's own established practice (E.151's Pointe du Hoc
  precedent) of recording a real, useful anecdote honestly with its date
  caveat intact rather than silently rounding it into the target year.

## Confidence Notes

- Real, confirmed text layer (not an image scan) — read via
  `pdftotext -layout`, and cross-checked against the PDF's own page
  breaks to recover genuine printed page numbers rather than PDF page
  indices, avoiding the off-by-N citation risk a straight `-layout` dump
  would otherwise carry for a book with this many unnumbered plate pages
  interleaved with numbered text pages. High confidence in the
  transcriptions and page attributions above.
- This is a strong genre match for every question this pass asked except
  Q5 (turn/impulse pacing) — a company/battalion tactics-and-doctrine
  reference is exactly the right kind of source for "how did real
  fire-and-maneuver actually happen," and it delivered accordingly.
  Q5's near-miss is reported as a genre/scale mismatch specific to that
  one question, not a mark against the book generally.
- Finding 1's "validates the shape, not the numbers" verdict is
  deliberate and should not be read as understating the result — no
  tactics manual could confirm an abstract hex-bound or eFP-halving
  figure, and this pass does not claim the book does. What it does claim,
  with real textual support, is that the two-function fire/maneuver split
  itself (not merely "realistic," but independently and repeatedly
  described by three different armies' own doctrine) is a sound
  abstraction to be encoding at all.
- Finding 2's frontage/depth figures are reported as real and citable but
  rough — "commonly," "usually," and range-based ("400 to 1,000 metres")
  throughout, in the same spirit as E.151's and E.152's own qualitative/
  comparative evidence, not as precise numbers ready to drop into a rule
  table without a scenario designer's own judgment.
- Finding 3 is reported as this pass's strongest result and is not
  hedged — the p.14 quotation is about as direct a match for Rule
  8.5.3a's own stated design identity as a real doctrine source is likely
  to produce.
- Finding 4's echelon-mismatch caveat is deliberate, not a hedge to avoid
  a stronger claim — Interrupt (Rule 6.4) and battalion-level reserve
  doctrine really do operate at different granularities, and conflating
  them would overstate what this book supports.

## Open Questions / Gaps for Follow-up

1. **PROPOSAL FOR COORDINATOR REVIEW — NOT ADDED.** Section 22 has no
   unit-frontage, echelon-depth, or defense-in-depth spacing guidance for
   *standard* (non-jungle) terrain at all, the same gap
   `jungle_warfare_rottman_1943.md`'s Finding 6 already flagged for
   jungle terrain specifically. If the coordinator wants to pursue a
   future Section 22 addition, this file's Finding 2 supports (not
   proves) a table roughly along these lines, clearly labeled as drawn
   from rough, "commonly"-qualified doctrinal figures rather than a
   precise source table:
   - Battalion attack frontage: ~400-1,000m (German) / 500-1,000 yards
     (US) → roughly 11-27 hexes at this project's 40-yard scale.
   - Echelon/bound depth within an attack: ~100-200 yards (≈2.5-5 hexes).
   - Defense-in-depth AT-nest spacing: ~150 yards apart in staggered
     lines, engaging at ≤75 yards once penetrated (≈3.75 hexes / ≤2
     hexes) — a genuine defense-*in-depth* figure, distinct from a purely
     linear defense.
   - Squad/platoon all-round perimeter radius: ~50 yards (≈1.25 hexes)
     from a position's own trenches to its outer wire/mine ring.
   - A genuine complication for any Section-22 addition inspired by
     E.152's jungle "no linear front" finding: this book's own
     standard-terrain battalion defense (Plate H2, p.63) is explicitly
     linear at the company-strongpoint echelon (three companies forward
     in line, one back with HQ), with all-round defense appearing only
     at the individual strongpoint level — any future guidance should
     distinguish "jungle: no linear front at any echelon" from
     "standard terrain: linear at battalion echelon, all-round at
     strongpoint echelon" rather than generalizing E.152's jungle finding
     to all terrain types.
   This is a genuinely larger design decision than this documentation
   pass should make unilaterally, per this pass's own brief — not
   designed or added here.
2. **No change proposed to Rule 6.3.3, Rule 8.3, Rule 8.5.3a, or Rule
   6.4.** All four mechanics were checked directly against this book and
   held up — three (6.3.3/8.3's shape, 8.5.3a) with strong, explicit
   textual support, one (6.4/reserve doctrine) with real but
   echelon-mismatched support, reported honestly as such rather than
   forced into a tighter parallel than the source actually gives.
3. **Rule 2.2.1/Rule 7.1.2's turn/impulse scale** remains uncited by any
   source found in this pass, the same open state it was in before this
   pass began. A future pass looking specifically for real accounts of
   how many discrete fire-and-movement bounds a company/platoon actually
   executed within a short, clocked span of real time (rather than a
   whole-attack preparation estimate, which is what this book supplies)
   would need a different kind of source — a small-unit action report or
   after-action account with its own explicit timestamps, not a general
   tactics-doctrine reference of this book's type.
4. The companion squad/platoon volume this book explicitly references as
   its own first half — *World War II Infantry Tactics: Squad and
   Platoon* (Osprey Elite 105) — is not held in this library and was not
   read. It is a plausible future candidate if this project ever wants to
   check squad-level (rather than company/battalion-level) doctrine
   specifically, though most of that ground is already covered by this
   project's existing national TOE files.
5. No changes were made to `units.csv`, `weapons.csv`, or any numeric
   value in Sections 5-9 or Section 22 as part of this pass — see the
   corresponding design note (E.160) for what was and was not applied to
   the rule text.
