# Rules Gap Audit — 2026-09-10

Full-project sweep for rules sections left stubbed, TBD, or never actually
finished, plus a few things that appear to have simply never been raised —
not just things the document itself already admits to. Triaged by what's
actually blocking a complete ruleset vs. what's legitimately deferred to
playtesting or a later scope expansion.

Method: grepped `docs/source/*.rst` for TBD/stub/deferred-work language,
read every hit in context, cross-checked Appendix E's design-note history
(E.1–E.105) against the current rule text those notes claim to have
resolved, and checked the counter-data tool READMEs (`counters/*_calc/`)
for their own documented scope gaps. Not everything Appendix E once flagged
as open is still open — most of the historical TBDs (campaign economy,
EM, Force Morale factors, the action-economy rewrite) turned out to already
be resolved in both the design notes *and* the rule text. What follows is
what's actually still open as of this commit.

## Update — 2026-09-11

Two of the four "still open" items below are resolved as of this update,
plus two decisions confirmed:

- **Operational scale** (was Triage #1): not a gap after all — it's a
  deliberately sequenced future manual. See "Resolved: Operational scale"
  below.
- **Weather** (was Triage #2): implemented as new Section 24, the same way
  Night Combat was implemented from Section 23. See "Resolved: Weather"
  below.
- **F# vs. ROF** (was Triage #3): confirmed — they're the same stat, merged.
  See "Resolved: F# and ROF merged" below.
- **Replacement Point flat rate**: confirmed as correct — no change needed,
  the hedge language in Rule 11.6.3's rule-guide is removed.
- **Appendix F index staleness**: not fixed further right now, per
  instruction — noted as a known-imperfect state to revisit later rather
  than a dedicated pass today. The explanation below stands as the record
  of what the problem actually is for whenever that pass happens.

The counter-data roster-gaps explanation from the first request is also
expanded below, and a new, larger item opens as of this update: **nation
TOEs (Tables of Organization and Equipment)** are now the explicitly
agreed prerequisite for any further counter-data work — see "New: Nation
TOE compilation" below.

### Resolved: Operational scale — deferred to a companion manual, confirmed

This was never actually a gap in the sense the other items are — it was an
open question about intent, and now it's answered. Confirmed: operational
scale (~250 yd/hex, larger formations — platoons or whatever the final
counter grain turns out to be — replacing squad-level counters) is a
planned **separate companion manual**, built only once this tactical
ruleset is finished, and reusing this document's core resolution formulas
and procedures rather than a parallel system built from scratch. That's
why it was pushed back rather than cut outright: the intent is real, the
sequencing is deliberate.

Rule 2.1.2 is rewritten to say this directly instead of silently carrying
an unused `[OPS]` tag, and the inline `[OPS]`-tag convention itself is
retired (design note E.107) — a future companion manual will define its
own scope rather than tag individual rules inside this one. Nothing about
the tactical ruleset changed; this was a documentation and index fix
(Rule 2.1.2, 2.1.3, Appendix E E.107, Appendix F index), not new rules
content. No further action needed here until you're actually ready to
scope that manual.

### Resolved: Weather — new Section 24

Rain/Mud, Snow, and Fog, each a **fixed scenario condition** (declared once
at setup, like Night — not a mid-scenario weather track, which was
explicitly considered and deferred as separate, larger scope). Built the
same way Section 23 was: reusing existing machinery rather than a parallel
system.

What each one actually does, in plain terms:
- **Rain/Mud**: visibility capped at 3 hexes (same hard-gate mechanism as
  Night's 2-hex cap — can't spot or declare fire beyond it, full stop, no
  amount of OBS buys it back). Tracked vehicles get the existing dense-woods
  bog check (Rule 17.6.2a) in *every* hex, not just dense woods — a tank
  can now get stuck crossing open ground in the rain, which is the actual
  historical rasputitsa problem. Infantry pay +1 movement point per hex on
  top of normal terrain cost — slower, but no risk of literally getting
  stuck the way a vehicle can.
- **Snow**: same 3-hex visibility cap as Rain/Mud (deliberately shared —
  see below). Both infantry *and* vehicles pay +1 MP/hex, but there's no
  bog check — deep snow slows everyone down fairly evenly without trapping
  a tank the specific way wet mud does.
- **Fog**: the harshest cap, 1 hex — thicker than even Night's darkness in
  game terms, since ground fog can be more completely blinding at close
  range than ambient night light. Fog also adds +2 CON (concealment) to a
  unit's own hex, the one weather effect that gets this treatment, because
  fog genuinely hides a standing target the way darkness does — rain and
  snow don't do that the same way, they just obscure the space in between.
  Fog also reuses Night's exact "got lost in the dark" movement-risk check
  (Rule 7.7), because fog causes the same landmark-loss disorientation
  night does and doesn't already have a cost/risk mechanic covering that
  the way Rain/Mud and Snow do.

One deliberate simplification, flagged in design note E.108: Rain/Mud and
Snow share one visibility number (3 hexes) instead of each getting its own
tuned figure. What actually distinguishes them in play is what happens to
your feet and tracks (bog risk vs. flat cost), not a second precipitation
constant nobody asked to have separately calibrated.

Also generalized while doing this: Rule 8.11 (fire eligibility) was
Night-specific yesterday; today it's stated once, generically, for any
active visibility cap (Night, Fog, Rain/Mud, or Snow) — the same
consolidation instinct as design note E.71, once the same shape of rule
was needed a third and fourth time. Rule 7.7 (movement risk) was *not*
generalized the same way — it's invoked by Fog specifically (Rule 24.4.3)
but deliberately not by Rain/Mud or Snow, since those already have their
own distinct movement penalty and doubling up would tax the same weather
twice for no reason.

Also fixed in passing: the **BOGGED marker** (Rule 17.6.2a) turned out to
have never been added to either the Section 1 component list or the
Appendix F index, despite existing as a real rule since well before this
session — the same category of oversight as yesterday's stale Initiative
index entry. Added both.

### Resolved: F# and ROF merged — confirmed, one stat now

Confirmed: they were always meant to be the same thing. Rule 3.3.2 (the
printed F# stat) now reads directly from Rule 6.6.2's mount-type table
instead of being a separate, unconsulted number — 1 for the great
majority of units, 2 for a bipod/light-tripod MG or a deployed mortar, 3
for a tripod HMG. Design note E.109 has the full record.

Two concrete corrections fell out of actually merging them rather than
just declaring them merged in the abstract:
- The **LMG team's** example stats printed F3, contradicting its own
  bipod mount's real ROF of 2 — a bug that could only survive while the
  two stats were tracked separately. Now F2, matching its own table.
- Every **ordinary (non-MG) unit** — rifle squad, SMG squad,
  Panzergrenadier squad, Guards rifle squad, engineer squad — printed F2
  with nothing behind that number beyond "not 1 or 3." These are now F1,
  the actual "any other unit" value from Rule 6.6.2.
- **Mortars** were the one addition, not a correction: they'd never been
  on Rule 6.6.2's table at all despite already printing F2 while deployed,
  so a "Mortar, deployed: ROF 2" row was added to give that existing
  value an actual source rather than silently dropping mortars to F1 along
  with the ordinary-unit corrections.

Snipers, leaders, and vehicle-mounted weapons were already correct under
the merged definition. This resolves the concept and the specific
examples already in the document's own text — it is explicitly **not**
the full counter-data review Rule 6.6.6 used to describe (assigning a
real stationary rate of fire to every unit in an eventual complete
roster). That's sequenced behind the TOE compilation below, so those
calls get made from real organizational data.

### New: Nation TOE compilation — in progress

Confirmed direction: before any further counter-data work (new nations,
new unit types, resolving the rest of Rule 6.6.6's table), the project
needs real Tables of Organization and Equipment (TOE) — the actual
historical rifle squad/platoon/company structure and weapon complement,
cited to real sources — for every nation the rules already reference but
never fully worked up: Germany, Soviet Union, United States, United
Kingdom, and Japan. Scope confirmed: all five nations, one representative
year (1943, matching how the game already frames itself) per nation,
squad through company echelon (organic weapons plus company-level heavy
weapons — HMG/mortar/AT teams), delivered as human-readable cited
Markdown docs rather than structured data — something to read and
sanity-check before any pipeline touches it.

Set up `counters/toe/` (with its own README explaining scope and how it
relates to the existing `counters/infantry_calc/` sourcing) and dispatched
five parallel research agents, one per nation, each instructed to use
real web research and cite actual sources rather than work from memory,
following the dispatching-parallel-agents pattern (five genuinely
independent research tasks, no shared state). All five landed as
`counters/toe/germany_1943.md`, `soviet_union_1943.md`,
`united_states_1943.md`, `united_kingdom_1943.md`, and `japan_1943.md`,
reviewed in full.

**Quality: consistently strong across all five.** Each is grounded in
real period sources (official T/O&E and War Establishment documents,
period US intelligence handbooks like TM-E 30-451/30-480, or careful
secondary compilations that themselves transcribe primary archival
tables), cites everything with enough detail to trace back, and is
explicit throughout about confidence — well-established vs. single-source
vs. approximated, never presenting a guess as settled fact. Each also
independently found and flagged real internal inconsistencies in its own
source material (e.g. one US secondary source blurring 1943/1944 figures,
a Japanese source describing a different-echelon machine gun count) rather
than silently picking one number.

**Two findings worth flagging now, not just filed:** both TOE docs found
a direct conflict between their sourced research and this project's own
existing "PRELIMINARY"-status game data in `counters/infantry_calc/data/units.csv`:
- **Germany:** every source checked (including a primary 1943 US Army
  translation of an actual German squad-training manual) agrees the squad
  leader carried a machine pistol (MP38/40), and the late-1943 9-man squad
  had *two* submachine guns. The existing `GER_GREN_1943.3_F` row has
  *zero* — 1 MG42 + 8 Kar98k, no SMG at all.
- **Soviet Union:** the existing `SOV_GDSRIF_1943.3_F` row models a
  "Guards Rifle Squad" with 4× PPSh-41 submachine guns, sourced only to
  "STAVKA TO&E 1943." The research (working from actual Red Army *shtat*
  documents) found no distinct Guards-specific squad organization at
  all — Guards/line differences show up at company level and above, and
  no line or Guards squad in 1943 carried more than 1-2 SMGs.

Neither doc edited `units.csv` — both were explicitly scoped to research
only, flagging the conflict rather than resolving it, since translating
real organizational facts into game-balance numbers is a deliberately
separate, later step (same posture as the F#/ROF merge above).

### Update — 2026-09-11 (same day): ran the TOEs through `infantry_calc`

Both flagged discrepancies above are now resolved (design note E.111):
- **Germany:** the Grenadier Squad gains its documented MP40 (squad
  leader) and its manpower corrects 9→10. The MG42 LMG slot itself is
  untouched — the system's calibration anchor is intact.
- **Soviet Union:** the Guards Rifle Squad's loadout now matches the
  standard Rifle Squad exactly (no sourced basis for a distinct Guards
  loadout existed) — the Guards designation is carried entirely by the
  veteran quality tier now, which the formulas already treat as a
  distinct multiplier. A third, smaller bug fell out of the same check:
  the standard Rifle Squad's own manpower was 10 against a sourced 9-man
  squad; corrected.

Also applied the F#/ROF merge (E.109) to the actual counter-data pipeline,
which had only been applied to the rulebook's illustrative examples until
now: every ordinary squad's f_number 2→1, and the DP-28 team's 3→2 (a
bipod LMG team is F2, not F3 — a real latent bug the merge exposed).

Added 8 new rows (US Rifle Squad + Light Machine Gun Squad, UK Rifle
Section, Japan Rifle Squad, each front/rear) and 9 new weapons, with
practical RPM and range figures web-verified per weapon (recorded in
`counters/infantry_calc/README.md`, since `weapons.csv` has no source
column of its own).

**One discrepancy deliberately left unresolved:** the Panzergrenadier
Squad's real loadout (2 LMG + 1 Panzerschreck, per KStN 1114) differs
substantially from the single LMG currently modeled — flagged in the
row's own notes rather than folded in, since the TOE research itself
expressed lower confidence on that unit's exact personnel reconciliation.

**One finding worth a deliberate look, not a bug:** the new US Light
Machine Gun Squad (M1919A4) computes to rFP 6, well below the German
MG42 HMG Team's rFP 9 — a real, sourced gap (the M1919A4's practical rate
of fire is under half the MG42's), not a copy-paste error, but a
meaningful game-balance difference between two otherwise-parallel
counters worth confirming is the intended flavor.

Full test suite: 150 passing (up from 139), including new coverage for
every added/corrected row. `infantry_roster_output.csv` regenerated.

## Already fixed in this pass

1. **Night Combat (new Section 23).** Rule 14.11.5 stubbed in a
   night-detection framework and explicitly deferred the rest ("Full night
   rules are a separate design task"). A complete DRAFT spec already
   existed (`docs/superpowers/specs/2026-09-09-night-combat-design.md`,
   status: pending your review) but had never been turned into actual rule
   text. Implemented in full: Section 23 (ambient visibility, illumination
   general rule, three illumination sources — starshell/flare
   pistol/searchlight — and drift), plus the six cross-reference rules it
   requires (7.7, 8.11, 9.3.2a, 12.2.4, 16.3.2 extended, new 16.9a),
   Appendix E note E.106, Appendix F index entries, and the index.rst
   toctree. Builds clean under `sphinx -W`. **This is a draft pending your
   review, same as the spec it implements — nothing here is final.**

2. **Stale "replacement points TBD" note (Rule 11.6.3) — explained in more
   depth.** The chain of events: Rule 11.6's Intelligence Point spending
   table was drafted with a 3-point option ("gain bonus replacement points
   equal to the prisoner count") back when Replacement Points themselves
   didn't exist as a mechanism yet, so the row was marked TBD and disabled.
   Replacement Points were later designed and implemented in Rule 13.2.2a
   (design note E.100) — but that was a change to Section 13's campaign
   economy, made without anyone circling back to Section 11's spending
   table to check whether it could now be turned on. That's the actual
   bug: two sections both touch the same concept, one got updated and the
   other didn't, and nothing would have caught the mismatch short of
   someone actually reading both side by side (which is what this audit
   did).

   The fix has two parts. First, mechanically un-stubbing it: the row now
   grants a real Replacement Point via Rule 13.2.2a instead of pointing at
   nothing. Second, a judgment call I made that you should look at: the
   original draft said "equal to the prisoner count" — i.e., scale with
   however many POW markers you secured — but Rule 13.2.2a's whole design
   intent (per E.100) is that Replacement Points stay *scarce*, capped at
   1 per campaign turn from ordinary Resupply specifically so a side can
   patch a couple of bad recovery rolls at most, never guarantee full
   recovery. If this one Intelligence-spend could hand out a point *per
   prisoner*, a single good capture scenario could hand a side more
   Replacement Points in one shot than the entire rest of the campaign's
   Resupply income combined — that seemed likely to undermine the scarcity
   Rule 13.2.2a was specifically built to protect. So I wrote it as a flat
   1 point per purchase instead (costing 3 Intelligence Points, same as
   before) and flagged it inline in the rule's own Why-block as **my**
   default, not something you'd actually signed off on — if you want it to
   scale with prisoner count after all, or want a different flat number,
   that's a one-line change to Rule 11.6.3, not a structural one.

3. **Stale Appendix F index entry.** The index still listed Initiative as
   granting "+1 RP to winner" — removed by design note E.91 (initiative
   buys tempo, not resources) but never scrubbed from the index. Fixed.
   I did not do a full line-by-line audit of the 1,274-line index against
   every superseding design note (see Triage #4 below) — this was caught
   incidentally while placing the new Section 23 entries.

## Triage — real, still-open gaps

### 1. F# vs. ROF reconciliation (Rule 6.6.6) — explained in more depth
**Priority: medium. Needs counter-data work, not just prose.**

Here's the actual mechanism of the problem, not just that it exists.
Every infantry/weapon counter has a printed F# (fire actions per turn) —
a rifle squad might be F2, an HMG team F3. Separately, Rule 6.6 defines
ROF (Rate of Fire) for *stationary* tripod/bipod machine guns: a tripod
HMG gets ROF 3, a bipod LMG gets ROF 2, full stop — a fixed number from a
mount-type table (Rule 6.6.2), completely independent of whatever F# is
printed on that same counter. Rule 6.6.1 says this outright: "F# is not
consulted by this rule." So right now, an HMG counter's printed F# is
just... never read by anything. It looks like a real stat. It isn't one.

Why this is a real problem and not just cosmetic: under the corrected
action economy (design note E.94), F# used to mean "how many full-effect
fire actions this unit gets per turn," which made an HMG's printed F3 and
a rifle squad's printed F2 both meaningful, comparable numbers. Now a
rifle squad doesn't have F#-limited fire at all (Rule 6.3.1's Regular/
Assault split governs it instead), and an HMG's actual fire rate comes
from the ROF table, not its printed F#. So F# is dead ink specifically on
the counters where a player would most expect it to matter. A new player
reading an HMG counter has every reason to think F3 means something and
no way to know it's vestigial without already having read Rule 6.6.1's
fine print.

What "fixing" this actually requires: someone has to go through every
counter in the roster and decide, unit by unit, whether its printed F#
should be deleted (if it's an ROF weapon and F# is genuinely meaningless),
kept as-is (if it's a non-ROF unit where F# still does real work), or
redefined as something else entirely (maybe F# should mean the ROF value
itself, so the two numbers merge into one). That's a counter-data
decision across the whole roster, not a rules-paragraph fix — the same
shape of work the `armor_calc` tool did for penetration values, just for
this one stat instead. Not something to draft blind; needs your call on
which of those three outcomes is intended before anyone touches counter
data.

### 2. Appendix F index may have more staleness than the one instance found — explained in more depth
**Priority: low, but worth a dedicated pass.**

The concrete pattern that produced the one stale entry I found (Initiative
still listed as granting "+1 RP to winner," a bonus design note E.91
removed): a design note changes a rule's *text*, but Appendix F's index
is a separate, hand-maintained 1,274-line file that has to be edited
*again*, by hand, to match. Nothing enforces that the second edit happens
— there's no build check, no cross-reference test, nothing but a human
remembering to do it. I only caught the Initiative one because I happened
to be reading that exact part of the index anyway (placing the new Night
Combat entries nearby) and the wording jumped out.

Since this session started, the design-note history includes at least
five distinct superseding chains where a rule's actual mechanical content
changed after the index was presumably already written to match the
*earlier* version: E.60→E.71 (fire grouping rules), E.63/E.75→E.94→E.95→
E.105 (the action economy, rewritten twice more after its first fix),
E.102→E.104 (Experience Modifier's downward half), and E.91 (the
Initiative case I already found). I did not check whether any of the
other four left similar debris — I fixed the one I tripped over, not the
category. A dedicated pass would mean: for each of those design notes,
read what it actually changed, then check every corresponding Appendix F
line still says the same thing. That's a mechanical, checklist-shaped
task — good candidate for a fresh session or a scripted diff, not
something that needs design judgment.

### 3. Component list quantities are almost entirely TBD (Rule 1.2)
**Priority: low — mostly legitimate.** Nearly every physical-component
row reads "TBD," and the section header itself says final quantities
await playtesting — this is honest, not neglected, for print-run
decisions like counter-sheet count. But two rows already show a better
pattern ("TBD — suggest 20 per scenario" for fire mission slips, "TBD —
quantity to match maximum likely dispersed units per scenario" for
DISPERSED markers) — a useful, low-effort follow-up would be converting
more of the marker-quantity rows (RALLY POINT, ROUTING, CONTACT, BLIND/
DUMMY markers, etc.) to the same "TBD, suggest N per scenario" form using
Section 22's own typical-scenario-size guidance, rather than leaving them
bare TBD. Not urgent.

### 4. Counter-data roster gaps (tooling, not rules text) — explained in more depth
**Priority: low/ongoing — already self-documented in the tools' own READMEs,
gathered here so it's visible alongside the rules-text gaps instead of
buried in `counters/*_calc/README.md`.**

The two calculation pipelines (`armor_calc`, `infantry_calc`) are what
actually generate the printed stat values on counters — AV/PEN curves,
Gunnery thresholds, fire-line notations — from sourced historical data,
rather than hand-guessed numbers. What they cover today is a fraction of
what a finished game needs:

- **`armor_calc`** has run 13 vehicles through the full pipeline (roster,
  penetration curves, Gunnery thresholds, Hit Location tables). No British
  guns or vehicles have been modelled at all yet — not "modelled roughly,"
  literally not in the pipeline, which is why Section 17's own intro
  already flags it. Two smaller, more specific loose ends inside the tool
  itself: the pre-October-1943 Sherman glacis quality-control issue (a
  documented, real manufacturing defect that would affect that plate's
  effective protection) is a candidate for the flaw-multiplier system but
  hasn't been sourced to a specific citation yet; and `av_override_mm`, a
  manual by-hand value used for a handful of plates that aren't a single
  flat thickness at a single angle (the Tiger's mantlet, the Sherman's gun
  mount), is a stopgap the tool's own README says should become a real
  geometric area-weighting calculation if more vehicles turn out to need
  the same treatment.
- **`infantry_calc`** is explicitly a pilot: 6 unit types, 2 nations
  (German, Soviet), 1943 only. Every American, British, and any other
  nation's infantry statline, plus every other year of the war, is
  unbuilt — not wrong, just not attempted yet. Towed artillery (PAK40s,
  field howitzers — guns not mounted on a vehicle) is explicitly called
  out as out of scope for this tool, but the README notes it would reuse
  `armor_calc`'s own gun-curve-fitting math rather than needing a third
  pipeline built from scratch. Grenades and satchel charges are fixed,
  hand-assigned values rather than derived stats — flagged in the README,
  but this one's a deliberate, reasonable call (there's no ballistics
  curve to fit for a grenade), not a gap to close.
- Zooming out from either tool individually: **the whole game is
  currently a 1943 slice.** Every roster table in the rules text says
  "representative 1943" on its own label, which is exactly why nobody
  flagged this as a TBD anywhere — it doesn't read as an omission, it
  reads as the stated scope. But scope stated once at the start of the
  project and never revisited isn't the same as a scope decision anyone
  actually confirmed recently. Worth a deliberate check: is 1943-only
  still the intended final scope, or was multi-year coverage always the
  eventual goal and it just hasn't come up again since the initial
  framing?

## Not gaps (checked and ruled out)

- Campaign economy (Section 13), Experience Modifier upward and downward
  halves, generic branching framework — all fully resolved (E.100–E.104)
  and implemented in the rule text itself, not just the design notes.
- Minefields — looked incomplete from the component list alone
  ("Minefield hex overlays" TBD) but Section 21.4 fully defines placement
  cost, mine-strike rolls, the engineer exemption, and clearing — this one
  was already done.
- Force Morale factors, action economy, close assault stacking, hit
  location, spotting rebalance — all had open questions at some point in
  Appendix E's history, all resolved by later notes and current rule text.

## Update — 2026-09-11 (part 2): what having 5 nations now surfaces

Both commits from today's work (Night Combat/Weather/F#-ROF merge, and
the TOE compilation/counter-data pass) are pushed to `origin/main`. This
is a fresh sweep of what's outstanding as of that push, prompted directly
by "what else is outstanding or missing" — checked against current repo
state, not recalled from earlier in this doc.

### New: the rulebook's own example rosters are now lopsided

Now that infantry_calc covers 5 nations, several of the rulebook's own
illustrative rosters only cover 2-4 of them — a genuine inconsistency
that didn't exist before today, because before today Germany and the
USSR really were the only nations with real data behind them:

- **Section 15.6 (National Morale Characteristics)** has rows for
  Germany (x2 periods), USSR (x2 periods), US, and Japan — **no United
  Kingdom row at all**, despite the UK now having a fully-sourced TOE and
  being cited elsewhere in the rules (engineers, snipers, weapons). A UK
  force today falls back to the generic quality-based factor table
  (Rule 22.3.3) with no national flavor, unlike every other nation.
- **Section 12.11 (Representative Leader Counters)** — German and Soviet
  only. No US, UK, or Japanese leader counters exist anywhere in the
  document.
- **Section 16.2 (Representative Mortar Counters)** — German and Soviet
  only, despite the TOE research now describing the US 60mm M2, UK
  2-inch and 3-inch mortars, and Japan's Type 89 grenade discharger in
  real detail.
- **Section 20.7 (Sniper Counters)** — has German, Soviet (x2), British,
  and US. Missing Japan (a historically significant gap — Japanese
  snipers were a well-documented Pacific-theater factor).
- **Section 21.9 (Engineer Counters)** — has German (x2), Soviet (x2),
  British, and US. Missing Japan.

None of this is a bug from today's work — these rosters were always
illustrative examples, not meant to be exhaustive, and adding a nation to
`infantry_calc` doesn't obligate the rulebook to add matching leader/
sniper/engineer/mortar examples. But the asymmetry is now visible in a
way it wasn't before, and closing it (at least for UK/Japan, the two
nations missing from the most tables) is a natural, well-scoped follow-up
now that the TOE docs exist to source it from.

### Flagged during the counter-data pass, still open

- **Panzergrenadier Squad's real loadout** (2 LMG + 1 Panzerschreck per
  `counters/toe/germany_1943.md`, KStN 1114) differs substantially from
  the single LMG currently in `units.csv` — deliberately not corrected
  because the source research itself had lower confidence on that unit's
  exact personnel reconciliation. Needs either a decision to accept the
  research as-is and correct it, or a follow-up pass to firm up the
  headcount question first.
- **Soviet "Pattern B" squad** (2x DP-28, 5 rifles, same 9 men and 2
  PPSh-41 as the modeled "Pattern A") is documented in the TOE research
  as equally common but not modeled as its own counter — a candidate
  addition, not a correction.
- **US Light Machine Gun Squad's rFP (6) vs. German MG42 HMG Team's (9)**
  — a real, sourced gap (the M1919A4's practical rate of fire is under
  half the MG42's), flagged for a deliberate look rather than assumed
  correct or wrong.

### Unchanged from before today (still genuinely open)

- **Vehicle roster**: `armor_calc` still has no British guns or vehicles
  modelled — unaffected by today's work, which only touched
  `infantry_calc`. British tanks (Cromwell, early Churchill) appear in
  the rules' general movement-class tables but have no AV/PEN/Gunnery
  treatment.
- **Year-band coverage**: every nation's TOE and counter data is a single
  1943 snapshot. Section 15.6 itself already references other periods
  (Germany 1941-42/1944-45, USSR 1941/1943+) that have no organizational
  or counter data behind them at all.
- **Component list quantities** (Rule 1.2) — still almost entirely TBD;
  unchanged, still legitimately deferred to playtesting.
- **Appendix F index staleness** — left open per explicit instruction,
  not re-checked today.
- **Towed artillery** (PAK40, US 57mm/British 6-pounder/etc. as infantry-
  facing AT guns rather than vehicle-mounted guns) — still out of scope
  for both calc tools.

### Not gaps — explicitly deferred, not missing

- Operational scale — confirmed as a deliberately sequenced future
  companion manual (E.107), not an open item.
- Weather changing mid-scenario — explicitly considered and deferred as
  separate, larger scope than what was asked (E.108).
- Night Combat's own out-of-scope list (moon-phase visibility tiers,
  vehicle IR/thermal sighting, a blind/double-blind CP role, [OPS]
  interaction) — all flagged in E.106 as deliberate, bounded exclusions.

## Update — 2026-09-11 (part 3): closed four of the five roster gaps

Design note E.112 has the full record. Closed:

- **Section 15.6** — added a UK national morale row (factor 0.45).
- **Section 12.11** — added Platoon Leader (Regular) for US, UK, and
  Japan, deliberately identical to the existing Soviet row (leader
  competence is quality-tier-driven, not nation-specific by design).
  Broadened the section's intro text, previously scoped to "the 1943
  Eastern Front test scenarios."
- **Section 20.7** — added a Japanese veteran sniper.
- **Section 16.2** — added US 60mm M2, UK 2-inch, UK 3-inch, and the
  Japanese Type 89 grenade discharger, with real web-verified max-range
  figures. Two genuinely interesting, sourced findings, not just filled-
  in blanks: the US 60mm's range rivals German/Soviet *medium* mortars
  despite being a light squad weapon (traded off against a real, longer
  minimum range); the UK 3-inch's 1943 "Long Range" propellant upgrade
  genuinely outranges German/Soviet medium mortars of the same year.
  ACC/AMO/rFP for all four are estimated by analogy to this table's
  existing rows (there's no calculation pipeline behind Section 16.2 the
  way `infantry_calc` backs Section 3) — flagged as a lower confidence
  tier than the range figures.

**Left at lower confidence, deliberately:** Section 21.9 gets a Japanese
Engineers row, but marked as a rough estimate pending its own dedicated
TOE-style research pass — a quick check surfaced real facts about IJA
combat engineering (fortification/tunnelling work, man-portable
flamethrowers) but nothing at the organizational depth the other four
nations' infantry TOEs received. Printing a flagged estimate was judged
better than leaving Japan the only nation missing from this table, but
it shouldn't be read as settled the way the other rows are — **still a
real open item**, just a labeled one now instead of an absence.

**Bug fixed in passing:** the German veteran Pioneer squad printed the
same Morale (6) as the regular row above it, breaking the veteran-gets-
+1 pattern every other paired row in the document follows. Corrected to
7. Found while adding the Japan row directly beneath it.

## Update — 2026-09-11 (part 4): two overlooked rules mechanics, found and fixed

Asked directly "are there any rules overlooked" — a different question
from stubs/TBDs/rosters (already covered above). Dispatched a fresh-eyes
review scoped explicitly to exclude everything already known. It found
two real gaps, both confirmed against actual rule text before being
reported (not just plausible-looking), and both are now fixed. Design
note E.113 has the full record.

**1. Close Assault had no mutual-elimination rule for the Grenade Phase.**
Rules 9.3.6/9.3.7 each cover one side alone being wiped out; nothing
covered both at once, even though the phase is explicitly simultaneous.
The confirming evidence was already in the document: Rule 9.4.7 exists
purely to patch this same hole one phase later (Entry Fire), and its own
rule-guide says so outright. Fixed with a new Rule 9.3.8, mirroring
9.4.7 exactly, worded generically enough to also cover Rule 9.8 stacks
without a separate patch.

**2. Nothing let infantry attack a vehicle at close quarters — the
satchel-charge case had no procedure at all.** More evidence was already
sitting in the document than the first gap: Rule 18.9's own weapons
table has always listed an AT grenade bundle and a magnetic mine at "0
hex — same hex only," which only makes sense if infantry can end up
sharing a hex with an enemy vehicle — but nothing said how, or what
happens next. Rule 18.8.6 compounded this, crediting "engineer attacks
(Section 21)" as one of four ways a closed AFV takes damage, when
Section 21's only vehicle-capable action is the flamethrower. (Checked
and ruled out first: Rule 18.8.5's soft-target fire looked like a
candidate fix but is explicitly scoped to open-topped/unarmoured
vehicles only — not the closed-AFV case actually in question.)

Fixed with a new Rule 18.9a, which connects two systems that already
existed rather than building a third: Close Assault (Rule 9.1) can now
be declared against a vehicle-only hex, keeping its existing declaration
gate (leader present, Suppressed/Pinned exclusion, the reduced-face
check, Defensive Fire) but substituting a single PEN-vs-AV exchange —
resolved through Section 18's own infantry-AT machinery, not Section 9's
infantry-vs-infantry dice thresholds. Targets Rear arc (same "point-blank
means the weak point" principle as the flamethrower and Molotov rules)
and is simultaneous with the vehicle's own MG fire (reusing Overrun's
already-established precedent for exactly this situation). Rule 18.8.6's
cross-reference is corrected to name this rule and the flamethrower
specifically, rather than a "Section 21" citation that was only ever a
quarter true.

Both fixes build clean under `sphinx -W`.

## Update — 2026-09-11 (part 5): genre comparison against ASL and similar games

Asked "anything else ASL or other games address that we haven't." Checked
10 genre-standard tactical-wargame features against actual current rule
text. Most of ASL's famous exhaustiveness turned out to be deliberate,
defensible minimalism already matching this project's own stated design
philosophy (weapon jamming, vehicle bypass movement, a distinct "Human
Wave" mass-assault bonus, pre-registered defensive fire for direct-fire
guns — all confirmed absent and judged not worth the added bookkeeping).
Water crossings and rubble/craters are partial-by-design, consistent with
patterns already used elsewhere in this document.

Three were real, and the designer asked all three fixed (design note
E.114 has the full record):

- **Building floors were a phantom mechanic** — Rule 7.2 charged MP for
  climbing floors, but "floor" appeared nowhere else in the document; the
  cost had no consequence at all. Fixed by making floor-to-floor movement
  its own action (a new Change Floor entry, Rule 6.3.2, 1 AP per floor)
  rather than an MP line item, which also gave the document a natural
  place to hang a real consequence: a unit on an upper floor now gets the
  existing Elevated OBS bonus (Rule 14.9.8) when spotting.
- **Only engineers could dig in** — genuinely odd for a project this
  invested in historical grounding, since ordinary WWII infantry dug
  foxholes constantly without engineer support. New Rule 21.7a extends
  Rule 21.7's entrenchment procedure to any unit, at double the
  engineer's time and capped below what deeper fortification work
  requires — a specialist stays meaningfully better, not just present.
- **Vehicle hulls had no between-scenario recovery** — vehicle *crews*
  already had full campaign treatment (EM, quality, re-crewing), but a
  DAMAGED or ABANDONED hull had no path back into the campaign at all.
  New Rule 13.3.2 reuses Rule 13.3's existing recovery table exactly the
  way Rule 13.3.1 already does for leaders (relabeling columns, not
  building a second table), and routes a recovered hull through the
  crew mechanics that already exist rather than inventing new ones.

All three build clean under `sphinx -W`.

## Update — 2026-09-11 (part 6): the 4 confirmed-absent features, added as optional modules; complexity tiers; page count

Asked to incorporate the four ASL-standard features E.113 had confirmed
absent (weapon jamming, vehicle Bypass movement, a mass-assault bonus,
pre-registered direct fire) — explicitly as labeled optional chrome, not
folded into the base rules — and to set up a Base/Standard/Advanced
complexity-tier structure. Design note E.115 has the full record.

**Four new modules**, each following Rule 18.2a's (Shatter Gap) existing
"(Optional Rule)" header convention exactly, each reusing existing
numbers rather than inventing new ones:
- **Weapon Malfunction (Rule 8.12)** — reuses the attack's own dice
  (natural 1-and-1 on the d6/d8, ~2.1% of shots); infantry-carried
  automatic weapons only, vehicle guns untouched.
- **Pre-Registered Defensive Fire (Rule 8.13)** — reuses Rule 16.4.1's
  2-hex mortar registration limit and Rule 18.1a.7's existing follow-up-
  shot band-shortening mechanic.
- **Bypass Movement (Rule 17.6a)** — a vehicle can skirt a hex's
  obstacles (open-ground MP cost, no bog check) at the cost of no cover
  and no Overrun eligibility from that hex.
- **Mass Assault (Rule 9.8a)** — successive close assaults against the
  same hex in one turn apply a cumulative Defence penalty (-1 each,
  capped at -3, resetting per turn) — deliberately not a stacking-cap
  change, to avoid double-modeling the same idea two ways.

**New Appendix G (Rules Complexity Tiers)** classifies every section as
Base (needed for a complete game), Standard (the depth most groups will
settle into), or Advanced (pick-and-choose optional modules, each
labeled in its own rule text) — plus a single-table menu of every
Advanced module in the document, old and new.

**Page count estimate**, given directly to the user in this session
(not written into the rules themselves, since it's a production
question, not a rules question): current player-facing content
(Sections 1-24 + Appendices A-D/F/G, excluding Appendix E's ~23,750
words of designer-only commentary) is **~117,000 words**. At a
realistic modern hobby-wargame layout density (~550-650 words/page,
this project's prose runs far more explanatory per rule than ASL's
terse style, so ASL's own ~1,000 words/page density doesn't apply),
that's roughly **195-215 pages of body text**. Only one actual diagram
exists in the whole document today (the Section 7 movement SVG) despite
at least 15-20 genuinely spatial concepts that would need one in a
finished, polished edition (elevation/crest LOS, vehicle facing arcs,
dispersion-direction compass, turn/close-assault sequence flowcharts,
vehicle hit-location silhouettes, a full counter/marker legend, a sample
scenario map walkthrough) — budgeted at roughly **12-15 additional
pages**, plus **3-4 pages** of front-matter overhead (title page, table
of contents). **Total estimate: roughly 210-260 pages**, central estimate
**~230 pages**. This is a planning estimate, not a layout — no new
diagrams were produced in this pass; the existing `maps/` SVG tool would
need real extension work (it currently renders flat hex-grid scenes only
— 2 terrain types, 2 factions — not vehicle silhouettes or flowcharts)
before most of the budgeted diagrams could actually be generated.

## Update — 2026-09-11 (part 7): cleared two counter-data backlog items; version bumped

Resolved the two items E.111 had deliberately left open (design note
E.116):

- **Panzergrenadier Squad** corrected to 2x MG42 LMG + MP40 leader per
  `counters/toe/germany_1943.md`'s KStN 1114 citation (confirmed at
  platoon level — 6 LMG / 3 squads = 2 each). Its organic Panzerschreck
  deliberately gets no weapon-loadout slot in `infantry_calc` — it
  already resolves correctly through the existing infantry AT weapons
  table (Rule 18.9), which uses PEN-vs-AV, not this pipeline's rFP
  formula. The previous loadout (1 MG42 + 6 MP40, cited only to
  "Nafziger OOB," no KStN reference) may have described the separate,
  still-unverified armored/SPW company variant instead — flagged as a
  candidate for its own future row rather than assumed simply wrong.
- **Soviet Rifle Squad (Pattern B)** added as a full sibling to the
  existing squad (now relabeled Pattern A) — 2x DP-28 instead of 1x, a
  real documented variant covering the other half of a platoon's four
  squads, not a hypothetical addition.

Test suite: 152 passing (up from 150). `infantry_roster_output.csv`
regenerated; builds clean under `sphinx -W`.

**Also**: bumped `docs/source/conf.py`'s version to 0.9.8, covering this
entire session's rules-content changes (no prior commit this session had
touched it — there's no automated trigger and no written policy for
when to bump, which is itself worth knowing for next time). Added a
short code comment recording that it's a manual per-session patch
counter with no semver contract beyond that.

**Still open**: proper TOE-depth research for Japan's combat engineers
(the Section 21.9 roster row is still a flagged rough estimate) —
research dispatched, not yet returned as of this entry.

## Update — 2026-09-11 (part 8): Japan's engineers don't fit this table — resolved by removing the row, not filling it in

The dispatched research (`counters/toe/japan_engineers_1943.md`) came
back with a finding bigger than a confidence problem: it's a genuine
organizational scale mismatch, not a documentation gap. Confirmed
against a primary source (TM-E 30-480, directly quoted): Imperial
Japanese Army combat engineers were concentrated in a division-level
engineer regiment, sub-allotted by **whole company** (~250 men, "one to
each infantry regiment," TM-E's own words) to supporting infantry —
there is no sourced IJA unit smaller than a company that plays the role
a German/Soviet/British/US engineer *squad* plays in Section 21.9's
table. Below platoon (~50 men, itself thinly documented), no manpower or
equipment breakdown exists in the source at all.

**Resolution: the Japanese Engineers row is removed, not corrected.**
Printing a squad-scale stat line for something that didn't organizationally
exist at squad scale would misrepresent a real difference between armies
as a missing data point — exactly the failure mode this project's own
"honest TBD" posture exists to avoid. Section 21.9 now carries a prose
note explaining why Japan is absent and naming the real reason, plus a
documented fallback for a scenario designer who genuinely needs IJA
combat-engineer capability at the squad scale: stat a Rifle Squad with
DEMO added (well-documented IJA equipment) but without the building-
assault bonuses, which represent a doctrine no source documents for
Japan at that scale. Design note E.117 has the full record.

Two secondary corrections fell out of the same research: the removed
row's "no BRDG" claim was wrong (TM-E documents a real, if smaller-scale,
IJA assault-bridging capability — man-portable bridges, pontons,
trestle bridges, a prefabricated steel truss bridge), and the Type 93/100
flamethrower's organizational home (engineers vs. dedicated chemical
troops) is genuinely ambiguous in the primary source itself, flagged as
unresolved rather than smoothed over.

Also fixed in the same pass: two RST markup bugs in the new content
(bold nested inside an already-italicized paragraph, which docutils
doesn't support and silently mis-renders rather than erroring cleanly)
that only surfaced on a full clean rebuild — `sphinx -W` had reported
them as warnings-as-errors, caught before commit. Builds clean now.

## Update — 2026-09-11 (part 9): British 6pdr/17pdr and Churchill/Cromwell — the last major nation-coverage gap

Section 17's own intro text had said "no British guns modelled yet"
since `armor_calc`'s original build-out. Closed: the 6-pounder and
17-pounder guns, plus Churchill Mk VII and Cromwell Mk IV (the two
vehicles that mount them at the roster's 1943 baseline), are now in the
roster with full sourcing.

The two source PDFs the rest of this project's ballistics data came
from are gitignored and weren't present in this environment — a real
constraint, not a shortcut. A dispatched research pass
(`counters/toe/british_vehicles_1943.md`) found the same book's (Bird &
Livingston 2001) calibration data quoted directly, with page citations,
inside Wikipedia's own articles on both guns — a defensible but
one-step-removed sourcing chain, flagged as such in every new row's
`confidence_note`.

**No published K-factor exists for either gun**, unlike every other row
in `guns.csv`. Treating K as a free parameter and searching for the
best power-law fit against the (unusually rich — 5 to 11 point)
calibration data found a numerically excellent but physically absurd
solution for the 6pdr first (K≈253, exponent=15.8, when every other gun
in the file has an exponent of 1.2–1.8) — caught before being accepted,
and fixed by constraining the search to a physically-plausible exponent
band (0.8–3.0). Final accepted values: 6pdr APCBC K=1495 (exponent
2.67), 17pdr APCBC K=1971 (exponent 1.24 — inside the band without the
constraint needing to bind), 17pdr APDS K=1514 (exponent 1.72), all
fitting their own calibration data to well under 0.5% error. This is a
new, explicitly lower-confidence methodology tier than every other gun
in the roster, documented as such rather than presented at equal
confidence.

**Two historical sanity checks, now permanent regression tests**: the
17pdr's well-documented ability to kill a Tiger I frontally at combat
range holds exactly (150.6mm PEN at 1000m vs. Tiger's 102.0mm Hull
Front AV-vs-Capped clears the Rule 18.2 Automatic-Penetration threshold
comfortably). The 6pdr's opposite reputation — effective only at very
short range — holds with more precision than expected: Automatic
Penetration at 100m, merely Contested by 500m, a clean Bounce by 1000m.

Churchill and Cromwell armor data both carry open source conflicts
(Churchill's stepped-glacis lower-plate angles unsourced; Cromwell's
hull side/rear and turret front thicknesses genuinely disagree across
sources by several mm) — resolved by preferring the better-cited figure
and flagging the disagreement in `vehicles.csv`'s own notes, the same
convention already used for the Panzergrenadier's ambiguous headcount
(part 7). APDS is sourced as entering British service March 1944,
technically outside the 1943 baseline era — the gun curve is built and
tested regardless, fielding it is left to the designer's own call.

Design note E.118 has the full record. Updated `counters/armor_calc/README.md`'s
"Known gaps" section and Section 17's intro text (now flags Sherman
Firefly, not "no British guns," as the remaining British-side gap).

Test suite: 110 passing (up from 102) — 5 new gun-curve tests including
both historical sanity checks (`test_formulas.py`), 3 new vehicle-loading
tests (`test_pipeline.py`). Full `sphinx -W` clean rebuild confirmed
after fixing one new instance of the same asterisk-adjacent-to-backtick
RST nesting failure documented in part 8 (a stray `*` immediately
followed by a backtick with no separating space, inside an
already-open italic span — fixed by matching the already-working
pattern elsewhere in this document exactly: always put a space between
a closing `*` and the inline-literal backtick that follows it).

## Update — 2026-09-11 (part 10): three rules gaps found by actually playing a scenario, fixed

Asked to build a map, set up a combined-arms engagement, and play a
few turns to see how the rules actually perform — a different kind of
QA pass than any prior part of this session, which had all been
text-only audits. Built "Counterattack at Oktyabrsky," a Panzer IV/
T-34 extension of the rulebook's own Farmhouse at Prokhorovka scenario
(Rule 22.11), grounded in real, cited terrain from the actual 12 July
1943 morning (Oktyabrsky State Farm, the 15-foot anti-tank ditch at
the base of Hill 252.2, the rail embankment). Played 4 of 6 turns with
every combat roll made live (1d6+1d8+1d12 / 1d6 via Python `random`),
delivered as an artifact with the map, order of battle, full turn log,
and findings.

Three genuine rules gaps surfaced — none wrong on the page, all
invisible to a text-only read because they only bite when a player
actually needs the missing piece mid-turn:

**Vehicle move-then-fire was never stated as its own rule.** Section
6.3.1 gives infantry a strict Move-OR-Fire choice per turn. Vehicles
obviously don't work that way, and two existing rules already assumed
the reader knew it (17.4.2's TRAV−1-if-moved penalty; an aside buried
in 18.1a.9) without ever stating the actual entitlement. Fixed with
new Rule 17.4.1a (one Move action and one Fire action per turn, either
order, moving doesn't end a vehicle's turn) and a one-line cross-
reference at 6.3.1a.

**No terrain type existed for a real anti-tank ditch.** Appendix B's
"Ditch / Sunken Road" is walkable by everyone, including vehicles —
there was nothing for the kind of ditch Soviet tanks are documented
driving straight into at Prokhorovka, and the playtest scenario had to
invent a Special Condition to model it. Fixed with new Rule 4.1.3a:
identical cover/movement cost to Ditch / Sunken Road for infantry, but
impassable to every vehicle class except at a marked crossing point
(reusing the same impassable-except-at-crossings pattern River/Cliff
already has in Rule 17.6.2's table).

**Railway embankments turned out not to be a gap at all.** They
seemed to fit neither the terrain table nor the elevation/crest system
(Rule 4.4a), which reads as hill-specific in its own examples — but
the crest/blind-zone/grazing-fire mechanics already work for any level
change, hill or not. Fixed with new Rule 4.4a.1a, which just says so:
a raised linear feature is assigned a higher elevation level than its
surroundings, no new terrain type or numbers needed.

All three: design note E.119, Appendix F index entries, `sphinx -W`
clean rebuild (double-checked the new design-note prose byte-for-byte
for the same asterisk-adjacent-to-backtick nesting failure as part 8 —
clean this time). None used the optional-module treatment — each
closes a real gap in the base game, not an added layer of chrome.

## Update — 2026-09-11 (part 11): Top Armour and Sidehill Exposure — a new Advanced module, two research passes deep

A follow-on design conversation from the same playtest, not the play
itself: what happens to a tank sitting broadside across a sidehill,
hit by a shot roughly perpendicular to the slope's fall line? The
whole hull rolls with the ground — Side armor straightens toward
vertical (loses its slope protection), and the deck's plane rotates
enough that the same shot can graze the normally invulnerable top
edge instead. Confirmed as distinct from trunnion cant (a firer-side
aiming effect, not a target-armor effect) and from the existing
elevation modifiers (Rule 4.5, which is about firer/target height
difference, not the target's own ground tilt). Built as a new
Advanced (Optional Rule) module on the designer's call.

**This exposed a bigger gap first: no vehicle in the roster had a Top
armor profile at all**, and Section 16 flatly said "mortars never roll
on the Section 18 penetration tables" — top armor had never mattered
to anything. Two research passes ran before any rule text was
written:

- **Vehicle top/deck armor thickness** (`counters/toe/vehicle_top_armor_1943.md`):
  usable, cited data for 9 of 14 roster vehicles (Panzer IV's turret
  roof reinforcement is the single best-cited figure in the pass —
  Jentz & Doyle, *Panzer Tracts No. 4*, p.50; Tiger, KV-1S, T-34's
  hull roof, Panther, both Shermans, Churchill also usable). The rest
  — Panzer III, StuG III, T-34/85, T-70's turret roof, SU-85,
  Cromwell — came back genuinely unsourced or too disputed, and were
  left blank rather than guessed at, same convention as
  `hardness_table.csv`'s missing nations. One popular claim was
  checked and debunked: Panther's turret roof was never actually
  thickened to 30-40mm on the real tank — that traces to the unbuilt
  Panther II project and a static bunker variant.
- **Mortar/artillery HE vs. top armor** (`counters/toe/mortar_vs_top_armor_research.md`):
  the designer initially asked for mortars to be able to attack top
  armor outright. The research came back against a general
  penetration capability — a naval-ordnance caliber-fraction formula
  only clears WWII deck thickness for the heaviest mortars against the
  thinnest decks; no citable incident of a mortar penetrating a tank
  roof was found (even checking Michael Wittmann's Tiger, which turned
  out to be a Firefly or rocket kill, not a mortar); and every
  casualty study checked (ORO-T-117, British 21st Army Group ORS, the
  Dupuy Institute) puts HE/mortar fire at 3-13% of tank losses against
  AP gunfire's dominant share, with doctrine describing mortars as a
  suppression/button-up tool throughout. Presented with this, the
  designer chose the historically-scoped version over the stronger
  mechanic they'd originally asked for.

**What got built, once the research was in hand:**

- Rule 17.2a (Top Armour) — a printed Hull/Turret Top AV, modelled
  flat (vertical_deg=0) rather than through the normal slope-multiplier
  machinery, since both trigger mechanisms below only ever need the
  plate's worst-case near-perpendicular resistance.
- Rule 18.2c (Sidehill Exposure) — Broadside-to-Slope condition
  (Side arc facing a crest hexside, attacker on the low side) resolves
  the hit against whichever of Side AV or Top AV is lower, reusing two
  already-printed numbers instead of inventing a reduction percentage.
- Rule 17.6b (Hull-Down Position) — added alongside it on the
  designer's explicit insistence ("we absolutely need hull down"): a
  stationary vehicle at a crest hexside makes its Hull completely
  untargetable from the low side, the flip side of the same geometry.
- Rule 16.7.8a (Heavy Mortar/Artillery vs. Top Armour) — the
  historically-scoped mortar mechanic: 120mm-class+ HE gets a narrow
  1-in-6 mobility-kill check (an implied engine-deck/grille hit), never
  a PEN-vs-AV roll, never anything for lighter ordnance.

Design note E.120, Appendix G/F updated (new module registered), all
four rules cross-checked byte-for-byte for the part-8/part-10 asterisk-
adjacent-to-backtick RST failure — clean this time, no fix needed.
Test suite: 114 passing (up from 110), including coverage that Tiger's
Hull Top loads dramatically weaker than its Hull Side (the whole point
of the module) and that every unsourced vehicle correctly has no Top
rows at all.

## Update — 2026-09-11 (part 12): F# and ROF fully consolidated — one name, not just one number

Asked directly: consolidate F# and ROF, pick one, eliminate the other,
globally. E.109 (much earlier in this session) had already resolved
the two down to one *number* — the printed counter stat and the
rules-text "Rate of Fire" concept had always been the same fact, just
tracked independently until that note merged them. What E.109 left
standing was two *names* for that one number: "F#" at the points a
rule addressed the printed stat directly, "ROF" everywhere the prose
described the underlying capability ("a stationary weapon firing under
ROF," an "ROF-greater-than-1 weapon," an "ROF pip").

F# is the name that survives — it's what's physically printed on the
counter, in the same abbreviation family as every other table-side stat
(rFP, M#, G#, CMD, OBS). Every live occurrence of "ROF" across Sections
1, 3, 6, 7, 8, 16, and 21, and Appendix F's index, is replaced with the
grammatically-adapted F# equivalent ("ROF weapon" → "F#-capable
weapon," "non-ROF economy" → "F1," and so on). Section 6.6's own
rule-guide text, which used to narrate *why* F# and ROF were being
merged, is simplified now that there's nothing left to merge.

Design note E.109 itself, and the handful of `counters/infantry_calc`
CSV row notes and one test docstring that cite it by name, are
deliberately untouched — dated historical records of a decision made
when two names genuinely were in play, same as every other design note
in this project. Rewriting them to erase the terminology they were
actually resolving would falsify the record, not clarify it.

New design note E.121. Prose-only change — no rule, number, or CSV
value moved. `sphinx -W` clean (design-note prose double-checked for
the same asterisk-adjacent-to-backtick nesting failure from parts 8/10
— clean). Test suite unaffected: 162 passing.

## Update — 2026-09-11 (part 13): the old term retired from the historical record too, not just live rules

Part 12 consolidated every *live rule's* phrasing down to F# alone, but
left the appendix's own account of that work naming the term F# used
to share duality with. Told directly: that's not enough — the term
shouldn't appear anywhere in the project at all, including in a design
note that explains a consolidation happened. Went further:

- Rule 6.6.6 (whose entire content was a pointer back to that now-
  unwanted history) is deleted outright, not reworded — nothing left
  for it to say once the naming question itself is gone.
- Every design note that had named the old term in passing — E.94,
  E.96, E.109, E.111, E.113 — is reworded to describe what was
  actually decided (F# tied to a single mount-type table, specific
  counter values corrected against it) without narrating a two-names
  story at all.
- E.121 itself is replaced in place with a note describing this final
  retirement, obliquely, rather than continuing to name what was
  retired.
- The two `counters/infantry_calc/data/units.csv` row notes and the
  one test docstring that cited the old term by name are also reworded.

This document (the session's own working log, not the rulebook) is
deliberately left alone above this entry — it's dated development
history a player never reads, not something the "doesn't exist,
don't mention it" instruction was aimed at. `sphinx -W` clean, 162
tests passing (prose/comment-only, no rule or value changed).

## Update — 2026-09-11 (part 14): Sherman Firefly closes the roster's most-flagged single gap

Asked to pick a backlog item and run it. Picked Sherman Firefly —
flagged as a known gap since armor_calc's original build-out (README,
Section 17's intro, E.118), and the 17-pdr gun curve already existed
from the British-vehicles pass, needing only the vehicle side.
Dispatched research (`counters/toe/sherman_firefly_1944.md`) before
touching any data.

**First departure from the 1943 baseline, done honestly.** Firefly
entered British service ~Jan 1944, combat debut Normandy June 1944 —
dated era="1944" rather than stretched to fit 1943.

**Three real findings shaped the data:**
- Standard conversion base was the M4A4 hull — welded, not riveted as
  assumed going in — and M4A4 production ended before the Sherman
  family's large-hatch glacis upgrade, so Firefly's hull front is the
  earlier, steeper small-hatch plate (51mm@56°), distinct from the
  existing M4A3(76mm) row's large-hatch 64mm@47°.
- Turret is the standard M4 casting, reused and modified (recoil
  system, mantlet, radio bustle, loader's hatch) — three sources agree
  no wall-thickness change accompanied the conversion, so Turret Side
  reuses the existing M4A1 figure (51mm) directly.
- The radio relocation added a real, separately-sourced armoured
  bustle box to the turret rear (51mm sides / 62mm rear, Sherman
  Minutia) — Turret Rear = 62mm, a genuine improvement over the base
  51mm wall, not a guess.

**The mantlet needed a judgement call, flagged rather than guessed
through.** The one well-cited figure (Fletcher's Osprey monograph, via
a Wikipedia footnote) is "+13mm of protection" over the standard
Sherman mantlet — but Wikipedia's own uncited "89mm maximum" infobox
figure coincidentally matches this project's existing M4A1 mantlet
override exactly, and the research explicitly warned against treating
that coincidence as confirmation (different kinds of quantities: a
flat uncited max vs. a pre-weighted hit-distribution average). Resolved
as a documented stand-in: M4A1's own 89mm override + the sourced
+13mm = 102mm, not a fresh re-weighting (no source data available for
that) and explicitly not the coincidentally-matching 89mm.

**Left genuinely open:** hull side/rear (38mm, inferred by extension
from the other two Sherman rows, not M4A4-specific-confirmed), and
APDS availability timing for Firefly units specifically — real
disagreement between the project's existing general "March 1944" date
and an uncorroborated "August 1944" Firefly-specific claim. A scenario
at the actual June 1944 combat debut should treat Firefly as
APCBC-only until this firms up.

New design note E.122. README and Section 17 intro updated (Firefly
no longer listed as a gap; the intro's stale gap-pointer now names
towed anti-tank guns instead). `sphinx -W` clean (checked the new
note for the same asterisk-adjacent-to-backtick nesting failure from
parts 8/10/12 — caught and fixed one instance before it shipped).
Test suite: 118 passing (up from 114).

## Update — 2026-09-11 (part 15): PaK 40 — the roster's first towed anti-tank gun

Continued picking off the backlog: towed anti-tank guns, the gap
Section 17's own intro pointed at after part 14 closed out Firefly.
Picked the PaK 40 (the single most-named example across this
project's own prior text -- infantry_calc's README, and Rule 6.6.6
before its removal). Dispatched research
(`counters/toe/pak40_1943.md`) before writing any rule.

**Rules question came first, and turned out small.** A towed gun is
a crew-served weapon team on defence (no armour, no Hull/Turret --
ordinary Section 8 fire against its own Defence when targeted,
deploy/limber like an HMG or mortar) but a vehicle gun on offence
(the Gunnery Roll and PEN-vs-AV comparison were never actually
specific to being turret-mounted -- they only ever depend on the
gun's own ballistics and the target's armour). New Rule 17.1a says
exactly that, plus a new F# table row (deployed = F2, same logic as
a planted mortar). Almost nothing needed inventing.

**No vehicles.csv row needed at all** -- a genuine first. The
Gunnery Table and PEN line come entirely from guns.csv/
gun_calibration.csv; vehicles.csv only ever supplied the *target's*
armour, never the shooter's ballistics. A gun with no armour of its
own simply has nothing to put there.

**Data followed the now-familiar British-guns pattern:** real
calibration data (a period German ordnance document, cross-checked
within 1-2mm by a second independent source), no stated K-factor.
Constrained least-squares fit hit the *exact same degenerate shape*
as the 6pdr before it -- unconstrained search finds K=223 with
exponent=25.75 for PzGr 39, rejected the same way. Constrained fit:
K=1954 (PzGr 39 APCBC, max error 2.06%, a bit looser than this
project's 5-point vehicle-gun fits for having one fewer point),
K=2356 (PzGr 40 APCR, max error 0.66% -- first real use of the
hvap76 stand-in family for a German gun).

**Left open, not guessed:** PzGr 40's muzzle velocity has a real
~3% discrepancy between sources (used the one matching its own
calibration data); no source gives PaK 40 crews a quality tier, and
the exact 1943 date the standard divisional battalion (as opposed to
a separately-named "heavy" variant) converted from 50mm to 75mm guns
wasn't pinned down.

Historical validation via the in-project cross-check the research
recommended: PzGr 39 auto-penetrates T-34 hull front at 500m,
consistent with Wikipedia's summary that the PaK 40 was "effective
against almost every Allied tank" of the war.

New design note E.123. infantry_calc/README updated (towed AT guns
moved from "explicitly out of scope" to "now partially in scope").
`sphinx -W` clean (caught and fixed two asterisk-adjacent-to-backtick
instances before shipping, same recurring failure mode as parts
8/10/12/14). Test suite: 121 passing (up from 118).

## Update — 2026-09-11 (part 16): Appendix H — a generated roster, working through the backlog "in logical order"

Asked to build out the remaining backlog in logical order. Started
with the item flagged the session before: "eventually all the units
and counter stats will need to be in an appendix." Built it same day
rather than deferring further.

New script `counters/generate_roster_appendix.py` reads the already-
computed `infantry_calc`/`armor_calc` output CSVs directly and writes
`docs/source/appendix_h__consolidated_roster.rst` whole — never hand-
edited, same pattern this project already uses for its own CSV
outputs and for `maps/pipeline.py`'s generated diagrams, one layer
further up.

Real scope decision made explicitly rather than silently: vehicle
Gunnery Tables aren't included. A Gunnery Table needs a specific
Crew Quality, derived from a vehicle's own printed Morale -- a value
`vehicles.csv` doesn't track as structured data at all (every crew-
quality assignment so far, e.g. the Oktyabrsky playtest's veteran
Panzer IV crews, was a scenario-time choice, never roster data).
Printing one here would mean inventing Morale values roster-wide --
flagged as a real follow-up instead, in both the appendix's own
preamble and project memory.

New design note E.124. Project memory updated (the "eventually build
this" note now says "built same day, here's how to keep it in sync").
No test changes -- documentation generator, not a calculation change.
`sphinx -W` clean, table row counts verified against source CSVs
(22 infantry / 103 vehicle plates / 14 guns).

## Update — 2026-09-11 (part 17): Firefly earns its place in Rule 18.12's historical matchup table

Continuing "build these out in logical order." The Sherman Firefly
(E.122) was added with historical validation data already gathered
in `counters/toe/sherman_firefly_1944.md` but never used -- three
real vignettes where a 17pdr-armed Firefly beat a German heavy the
standard Shermans in this roster can't. Closed that loop rather than
leaving it as unused research-file prose.

Only one of the three vignettes was solid enough for a table row: the
Wittmann engagement (Saint-Aignan-de-Cramesnil, 8 August 1944 --
Trooper Joe Ekins credited with all three Tiger kills his troop could
see), converging across four independent sources on unit/date/range.
The other two (Tilly-sur-Seulles, Norrey-en-Bessin) are single-sourced
with no range or arc given -- would have meant inventing a range to
get a row, not done.

Band-read the existing Rule 18.12 procedure against Firefly's already-
built roster row and Tiger I's existing one: ~700m reads the 500m
band, 17pdr APCBC PEN 150.6mm vs Tiger Hull Front 102.0mm (Automatic
Penetration, 48.6mm clear) and Turret Front 143.0mm (Contested, 7.6mm
over) -- consistent with three kills in one action without needing
the mantlet to cooperate.

New design note E.125. No test or data changes -- documentation-only
extension of an existing verification table using values already
computed by the existing pipelines. `sphinx -W` clean, checked the
new section's rendered HTML for the usual asterisk/backtick nesting
bug (none found).

## Update — 2026-09-11 (part 18): Sherman glacis QC flaw -- researched, honestly not modelled

Dispatched research on this project's own named-but-unsourced gap:
"pre-Oct-1943 Sherman glacis QC issues" as a second `flaw_multiplier`
candidate (README, `counters/armor_calc/README.md`). Result is a
partial non-finding, written up in full at
`counters/toe/sherman_glacis_qc_1943.md`.

Three real but distinct phenomena turned up, none matching the
README's implied single dateable defect: (1) a real cast-vs-rolled
ballistic deficiency for the M4A1, but already modelled separately
via `cast_deficiency_multiplier` -- adding flaw_severity here would
double-count it; (2) a general US-wide armor-quality limitation
through November (not October) 1943, unquantified and not Sherman-
glacis-specific; (3) a real small-hatch weld-seam shot-trap problem,
corrected March-June 1943, but a geometry issue (closer to
`av_override_mm` territory) that doesn't apply to either Sherman row
in the current roster -- the M4A3 already models the post-fix design.

No source gives "October 1943" specifically, and nothing gives a
Sherman-specific defect-rate comparable to Panther's sourced ~50%
figure. README corrected to describe the actual finding; new design
note E.126 documents the dead end. No `flaw_severity` applied to
either Sherman row -- an honest non-finding, not a forced guess.
No test or data changes. `sphinx -W` clean, checked the new note's
rendered HTML for the asterisk/backtick nesting bug (none found).

## Update — 2026-09-11 (part 19): British 6pdr -- this roster's second towed anti-tank gun

Continuing "build these out in logical order." The 6pdr was the
cheapest remaining backlog item -- its gun curve
(`sixpdr_57l50_apcbc`) already existed in `guns.csv` from the earlier
British-vehicles work and was already printed in Appendix H, unused
by any counter. Only crew/TOE facts needed research (full detail in
`counters/toe/sixpdr_1943.md`).

Crew size: 6, matching PaK 40 exactly, converging across four
independent British sources. Two real coexisting 1943 organizational
tiers found (infantry battalion Anti-tank Platoon, divisional Royal
Artillery Anti-Tank Regiment). Recommended anecdote for a future Rule
18.12 entry: the Robaa Valley ambush, Tunisia, 31 January 1943 (72nd
A/T Regiment RA) -- deliberately not the more famous but contested
"Tiger 131" story, whose own attribution (towed 6pdr vs. tank-mounted
6pdr vs. captured gun vs. French 75) is disputed even in the Tank
Museum's current research.

Genuine finding, not previously called out clearly: neither the PaK
40 nor the 6pdr has ever been given a printed weapon-team stat block
(Defence/Morale/M#/F#, Rule 17.1a.1) -- the infantry_calc pipeline
only derives those for RPM-based small-arms weapon teams via
weapons.csv, a shape that doesn't fit an HE-firing gun crew. Recorded
as shared infrastructure work in `counters/infantry_calc/README.md`
rather than invented ad hoc for one gun.

New design note E.127 (caught and fixed one asterisk-adjacent-to-
backtick nesting bug during its own write-up, same recurring class as
prior parts). No test or data changes -- ballistics and appendix entry
already existed; this session's work is the TOE research file and
documenting the stat-block gap. `sphinx -W` clean.

## Update — 2026-09-11 (part 20): closing the towed-gun stat-block gap for both PaK 40 and 6pdr

E.127 flagged, but didn't fix, a real shared gap: neither the PaK 40
nor the 6pdr had a printed weapon-team stat block (Defence/Morale/
M#/F#, Rule 17.1a.1). Closed it same day rather than leaving it as a
named follow-up.

No new formula needed -- `unit_defence()`/`unit_morale()` already
derive purely from `manpower_full`/`quality`, with no dependency on a
unit having an actual weapon slot. Added `GER_PAK40_1943.3_F` and
`UK_6PDR_1943.3_F` to `infantry_calc/data/units.csv` with all three
weapon slots blank (correct: a towed gun's real attack goes through
armor_calc's PEN/Gunnery Table and Rule 18.8.4's flat HE formula, not
this pipeline's RPM-based small-arms model). Both rows: manpower_full
6 (sourced, converging independently for both guns), quality=regular
(an explicitly-hedged inference, not sourced, for either) -- both
compute Defence 6 / Morale 5 / M0 / F2.

Two things left as open questions rather than guessed at: G# has no
formula anywhere in this project (every row's G# is designer-
assigned) -- both new rows use G1 by analogy to this roster's tripod
HMG teams. Neither row has a reduced/rear face -- Rule 17.1a describes
no degraded-crew mechanic for a towed gun, unlike HMG/mortar teams,
so none was invented.

New design note E.128. Appendix H regenerated (24 infantry rows, up
from 22). Both READMEs (infantry_calc, armor_calc-adjacent) updated
to reflect the closed gap. New test
(`test_towed_at_gun_teams_have_no_fire_lines_but_do_have_defence_and_morale`)
plus two hardcoded row-count assertions bumped 22->24. Test suite:
172 passing (up from 171). Caught and fixed one more asterisk-
adjacent-to-backtick nesting bug while writing E.128. `sphinx -W`
clean. Project memory updated with the new row count.

## Update — 2026-09-11 (part 21): two more towed guns -- Soviet 45mm (free reuse) and US 57mm (needed its own fit)

Continuing "build these out in logical order." Dispatched research in
parallel for this roster's third and fourth towed anti-tank guns.

Soviet 45mm M1937 (53-K): clean, free curve reuse. Sourced MV (760 m/s
/ 2493 fps) matches the existing t70_45l46_apbc curve (fitted earlier
this session for the T-70's tank gun) to the foot-per-second, barrel
length matches exactly, and Wikipedia's own family history describes
the tank gun as this exact towed design re-mounted with the same
ammunition -- stronger evidence than this project's own existing
KV-1S/SU-85/StuG III curve-reuse precedent. No new calibration data
needed. Crew size (6) is this roster's weakest-sourced convergence --
inferred only from a successor gun's uncited infobox and a tow
tractor's troop capacity, not stated for the 53-K itself.

US 57mm Gun M1: NOT a free reuse, despite being a licence-built copy
of the British 6pdr on the identical L/50 barrel. In 1943 it fired
only uncapped AP Shot M70, not the capped APCBC round already fitted
as sixpdr_57l50_apcbc -- a real ammo-family difference (ap_uncapped,
not capped) that flips the sign of the face-hardening correction
(0.80x for capped -- a liability; 1.303x for uncapped AP -- a bonus).
Fitted a new curve (usm1_57l50_ap, K=2400, 0.58% max error, this
project's first fielded use of ap_uncapped) from a real Tank Archives
calibration table. Checked against Panzer IV H's face-hardened hull
front: the M1's 1943 ammunition is only Contested at 500-750m and
Bounces beyond 1000m -- a genuine, physically-grounded illustration
of why the US Army wanted the capped shell that arrived in 1944, not
a design choice. guns.csv flagged so this 1943-specific row is never
reused for a 1944+ entry (use sixpdr_57l50_apcbc instead by then).
Crew size for this gun is genuinely unresolved (10/6/5, three
conflicting sources) -- used 6 for cross-gun consistency, flagged
in-row as not the best-sourced figure for this specific gun.

New design note E.129. Both guns got units.csv rows following E.128's
exact stat-block shape (SOV_45MMAT_1943.3_F, US_57MMAT_1943.3_F).
Appendix H regenerated (26 infantry rows, 15 guns). New tests:
TestUS57mmM1GunCurveFit (armor_calc) and
TestUS57mmAgainstFaceHardenedPlate (the Panzer IV finding); the
shared towed-gun stat-block test now covers all four guns. Test
suite: 174 passing (up from 172).

While writing E.129, hit and fixed several instances of the
recurring asterisk/backtick RST nesting bug -- and, while chasing
those down, also found and fixed two PRE-EXISTING leaks unrelated to
today's edits (a stray "TO**&**E" bold-marker leak in an old design
note, and a stray literal double-backtick pair around
`counters/infantry_calc/` in the Japan-engineers note). Root-caused
the nesting bug precisely this time rather than just pattern-matching
on "asterisk touching backtick": docutils requires every inline
markup start/end-string to satisfy its own preceded-by/followed-by
whitespace rules independently, and an already-open italic run makes
every nested code span's boundaries fail those rules unless explicitly
closed-and-reopened around it (with or without a `\ ` escaped-space,
depending on whether a visible space is wanted there). `sphinx -W`
clean; verified via a full-document scan (not just the new section)
for literal double-backtick pairs and suspicious asterisk contexts,
not just the new section, given how many notes were touched this
session.

## Update — 2026-09-12 (part 22): PaK 40 crew-quality/fielding-date follow-up -- narrowed, not closed

Continuing with bounded backlog items (per user direction after a
check-in: keep going with items that don't need a new rule/architecture
decision). Dispatched a follow-up on PaK 40's two remaining open
questions from its original research (E.123).

Crew quality: still not found, a fourth consecutive "not found" across
every towed gun fielded this session -- itself a real pattern, not a
per-gun gap. One useful negative result: the one "Panzerjager crew
training" claim findable via casual/AI-assisted search turned out to
be about self-propelled tank-destroyer crews, not towed-gun crews --
recorded as a branch-conflation trap for next time. quality=regular
stands, unchanged, still an explicitly-hedged default. One real,
unread lead flagged for later: Forczyk's *Panzerjager vs KV-1* has a
confirmed training-of-combatants section.

Fielding date: narrowed but not closed. The Nafziger Collection (cross-
corroborated across three independent mirrors) indexes Panzerjager/
anti-tank authorized-strength documents dated 1/15/25 October and 1
November 1943, including one captioned "12x 75mm PAK" and another
titled "Infantry Tank Destroyer Company" -- consistent with the
standard division's antitank company converting from 50mm to 75mm on
paper in October 1943, about six weeks after the already-known 1
September 1943 TM-E snapshot. Falls short of confirmed: only the
Collection's index was accessible, not the KStN documents' own
content, so the gun caliber is inferred from titles, not read
directly.

New design note E.130, matching the honest-non-finding treatment
already used for the Sherman glacis QC flaw (E.126). No data or test
changes -- research-only follow-up. `sphinx -W` clean, verified no
markup nesting leaks on the first build (applying the fix pattern now
recorded in project memory).

## Update — 2026-09-12 (part 23): Militia tier's first real unit -- British Home Guard, plus a genuine finding

Continuing with bounded backlog items. Dispatched research for a real
historical Militia-quality unit to finally exercise this project's
Militia tier (defined in quality/tiers.py since early on, never used
by any roster row).

Investigated three candidates. German Volkssturm: the single most
explicit quantified low-training claim found (some units committed
after 10-14 days' instruction), but 13 months outside the 1943 window
(formed Oct 1944) and no squad-scale TOE recoverable, only a
battalion headcount. Soviet opolcheniye: worse on both counts -- 2
years outside the window, and the "militia" designation itself was
transitional, divisions redesignated as ordinary Rifle/Guards
divisions within weeks to months, so no honestly-dated 1943
opolcheniye unit exists at all.

Adopted: British Home Guard, 1943 -- the only candidate needing no
chronological stretch, and an already-covered nation. Militia
classification is an honest inference from structural/doctrinal facts
(static local-defense doctrine, 1942 compulsory enrolment of 42-51
year-olds to fill under-strength units), not a stated historian's
classification -- flagged as such. New rows UK_HOMEGUARD_1943.3_F/_R:
an 8-man squad (1 BAR + 7 P17 Enfield rifles, a new weapons.csv row
using the same generic bolt-action rate as Kar98k/Springfield/Mosin).

Building it surfaced a genuine, un-massaged finding: both weapon lines
round down to 0 rFP under the log-compressed weapon_rfp() formula at
Militia's (uncalibrated) multiplier and are omitted -- this squad
prints NO fire lines at all. Not a data error (a tripod HMG, or 3+
LMGs together, still clears the floor at Militia) but a real
consequence of pairing this specific, sourced composition with an
admittedly-extrapolated quality constant. Recorded plainly rather than
fixed by inflating the weapon count -- left for the designer to judge
whether a Militia unit that can only occupy ground and fight in Close
Assault is a legitimate design outcome or a sign the constant needs
recalibrating.

New design note E.131. Appendix H regenerated (28 infantry rows, up
from 26). New test capturing the finding
(test_militia_home_guard_squad_prints_no_fire_lines_at_all) plus
row-count bumps (weapons 16->17, units 26->28). Test suite: 175
passing (up from 174). `sphinx -W` clean -- caught and fixed one more
asterisk-adjacent-to-backtick leak, first try this time using the
pattern now recorded in project memory.

Also note: the dispatched research agent for this task had an
internal mishap mid-session (briefly confused about which task it was
working on, then a separate/earlier instance of it overwrote its own
finished output file with an unverifiable competing draft carrying
invented page citations) -- the agent caught this itself, discarded
the unverifiable version, and restored its own properly-sourced work
with a provenance note explaining what happened. Surfaced here for
visibility, not because it affected the final research quality.

## Update — 2026-09-12 (part 24): checking our own work against purchased reference material

Rod added a small folder of purchased reference material (MicroMark/
Mark Bevis Canadian Army TOE lists, C3A and C28/C29, plus the full
MicroMark sales catalogue) specifically to see how this project's own
research holds up against an independent, professionally-compiled
source. Reviewed and cross-checked against existing project work.

Result: three research passes' worth of prior work (British vehicles,
17pdr APDS, Sherman Firefly) held up without correction. One real gap
found and closed:

1. **6pdr APDS was missing from guns.csv despite already being sourced.**
   Both Canadian documents list 6pdr APDS as standard 1944-45 ammo.
   counters/toe/british_vehicles_1943.md already had a full 5-point
   0-deg calibration table for it (Bird & Livingston 2001), gathered
   during the original British-vehicles pass but never carried into
   guns.csv. Fitted now: sixpdr_57l50_apds, K=1650, exponent 2.26
   (comfortably inside the physically-plausible band), 0.22% max
   error -- the tightest fit of any unpublished-K gun in this roster.
   Same March-1944-service-entry in-scope caveat as the 17pdr's own
   APDS row.

2. **17pdr APDS fielding-date discrepancy flagged, not resolved.** Our
   existing row says "March 1944" (War Office pamphlet). The Canadian
   C3A document instead says "Oct 1944" for that specific unit. Both
   could be true (general service-entry vs. this unit's actual issue
   date) -- recorded in guns.csv's confidence note rather than picked.

3. **Firefly-per-squadron ratio escalation** (a real, dated finding
   from C28/C29: ~25% Firefly per troop in July-Aug 1944, "all but one
   Squadron had 11x Firefly tanks" by Dec 1944) added as an addendum
   to counters/toe/sherman_firefly_1944.md -- scenario-design flavor,
   not a stat change.

New design note E.132. Also recommends the MicroMark catalogue's
German infantry-division lists (G63-G70, "German Infantry Division,
1943, all theatres") as a plausible, cheap next lead for the still-open
PaK 40 fielding-date question (E.130) -- division-level TOE lists of
this kind typically include the organic anti-tank battalion's exact
composition, per both Canadian examples reviewed here.

Appendix H regenerated (16 guns, up from 15). New test
TestSixPdrAPDSGunCurveFit. Test suite: 176 passing (up from 175).
`sphinx -W` clean on the first build (markup nesting fix pattern from
memory applied correctly). Note: the purchased reference PDFs
themselves are not committed -- `*.pdf` is already gitignored, correctly
keeping paid third-party content out of the repo.

## Update — 2026-09-12 (part 25): reading this project's own foundational source directly, for the first time

Rod obtained a copy of Bird & Livingston (2001), *WWII Ballistics: Armor
and Gunnery* -- one of this project's own two original data sources,
cited dozens of times throughout guns.csv/vehicles.csv/counters/toe/*.md,
but until now only ever cited secondhand via Wikipedia. Dispatched a
background agent to read the 234-page image-only scan directly,
prioritizing K-factors, the flaw-multiplier chapter, and cross-validation
of existing formulas.

**Finding one: real K-factors for six of seven unsourced-K guns.** Pages
84-85 have a genuine per-projectile K-factor table. Matched and replaced:
6pdr APCBC (1495->2722), 6pdr APDS (1650->2828), 17pdr APCBC
(1971->1686), 17pdr APDS (1514->1705), PaK 40 APCBC (1954->2400), PaK 40
APCR (2356->3395) -- all six upgraded from this project's lowest
confidence tier (constrained least-squares guesses) to real sourced
values. The Soviet 45mm's own constrained-search K (3613) matched the
book's table exactly -- independent validation the earlier methodology
wasn't just getting lucky. US M1 57mm's AP Shot M70 has no matching MV in
this table, remains unsourced. The book's own K-factor formula and
generic fallback exponent (1.4283) both matched formulas.py exactly.
Refitting all six against existing calibration data: comparable or
better fits, all exponents unconstrained-plausible, every existing
historical sanity check still holds.

**Finding two, more consequential: Ch.6 directly answers the Sherman
glacis QC question this session called an honest non-finding (E.126).**
Ch.6 opens with the exact sentence and date that research pass searched
for and couldn't find: "Prior to October, 1943, American armor
production and quality control permitted flawed armor to occur in many
tanks, which includes almost all 56 degree glacis Shermans." A worked
example follows directly on the M4A1: 51mm at 53 degrees, medium flaws,
vs. the unflawed post-fix 63.5mm@47deg redesign. Cross-confirmed by
Ch.14's own three-column M4-series table. This project's Sherman M4A1
row (51mm@47deg, no flaw) matched neither of the book's own documented
configurations -- a hybrid with no independent citation for the 47deg
figure. Corrected to 51mm@53deg, flaw_severity=medium (AV-vs-Capped:
76.7mm -> 79.7mm). Checked against both existing Rule 18.12 matchups
involving this vehicle -- both remain comfortably unaffected (guns clear
the old AV by 40mm+). M4A3(76mm)'s 64mm@47deg row is unaffected and
correctly stays unflawed. Addendum recorded in
sherman_glacis_qc_1943.md itself (not rewritten) explaining what
happened: the earlier pass was honest given secondary sources only;
reading the primary source directly isn't optional once a copy exists.

**Finding three: every existing formula cross-validated, no corrections
needed.** Cast-deficiency formula (Ch.5) character-for-character
identical to formulas.py. Flaw-multiplier and tungsten slope charts
(Ch.6, Ch.16) match within normal chart-reading tolerance. Bonus unused
lead: a 1943 Kubinka test record of the Soviet F-34 failing to
penetrate Tiger E side armor "even at 200 meters" -- a real historical
validation point not yet built into Rule 18.12.

Not reached this pass: Appendix 5 ("General Quality of Panther Armor"),
the German AFV table in Ch.14 (could hold Top/Roof data for this
roster's remaining top-armor gaps), and roughly half of Ch.14 overall --
flagged as the natural next read, not claimed to contain nothing.

New design note E.133, new research file
counters/toe/wwii_ballistics_direct_read_1943.md. Six K-factors replaced
in guns.csv, one vehicle plate corrected in vehicles.csv, three test
classes updated (TestBritishGunCurveFits, TestPAK40GunCurveFits,
TestSixPdrAPDSGunCurveFit) with sourced-not-guessed docstrings. Appendix
H and all armor_calc outputs regenerated. Test suite: 176 passing,
unchanged in count -- a correctness pass, not a coverage pass.
`sphinx -W` clean.

## Update — 2026-09-12 (part 26): finishing the WWII Ballistics read

Continuing directly from part 25. Dispatched a second background agent to
read everything the first pass didn't reach: Ch.1, 3, 4, 7, 8, 9, 10, 11,
the remainder of Ch.13/14, 15, 16, 17, 19, 20, Appendices 1-9, and the
Errata sheets.

**Most valuable single result: a clean negative.** Top/Roof armor is not
in this book at all -- for any vehicle, any nation. The full German AFV
table (Panzer III/IV, Panther, Tiger, derivatives, pp.65-68) was found
and read, alongside the completed USA/Soviet/British/Italian tables
(pp.69-74). None has a Top/Roof row for anything. This closes off this
project's still-open Panzer III/StuG III/T-34/T-70/SU-85 top-armor gaps
as a line of inquiry against this specific source -- future effort
should go straight to Panzer Tracts or a Soviet armor encyclopedia.
Recorded in vehicle_top_armor_1943.md so nobody re-checks this book for
that question again.

Tiger's mantlet table (Ch.10, p.42): 76mm-class row reads 143mm, an
exact match to the existing av_override_mm. The table also has other
calibers -- 57mm-class (this project's own 6pdr) reads 157mm, a real
10% difference this roster has no mechanism to apply, since
resolve_av()'s override path only stores one flat value per plate.
Recorded as reference data; building a caliber-keyed override table is
a real but unbuilt extension.

Panther's angle-probability distribution (Ch.11, pp.43-45) matches
exactly to the tenth of a percent -- confirms this project's own
weighted-average construction (E.118) rests on an accurate input. The
"Turret Front: 110c@10" second-plate finding from pass one was
independently reconfirmed, ruling out a misread; still not resolved.

Appendix 5 answers a different question than expected: not the source
of Panther's "~50% flawed glacis" statistic (that's Ch.14 p.66, now
cited precisely), but a separate finding that Panther's non-glacis
areas were explicitly unflawed. A dating wrinkle surfaced: the flaw
statistic is pinned to production "starting summer 1944," while this
roster dates Panther Ausf G to 1943 -- an existing convention, not
changed here, but worth knowing.

Two British-vehicle gaps closed via the British AFV table (p.73):
Churchill's long-missing lower-nose angle (140mm@20deg). One new gap
opened: a Cromwell nose-plate figure (57mm@20deg) never modeled before,
conflicting with an already-flagged weak ~25mm figure elsewhere --
recorded as an open design question in british_vehicles_1943.md's new
addendum, not resolved.

A citation error caught on an already-correct value: crew_quality_hit_cap()
was sourced correctly (exact match) but cited "Appendix 7" instead of
the actual Appendix 6. Fixed.

Genuinely unread: Appendices 10-19 and the Bibliography (~pp.105-123,
mostly dispersion/accuracy modeling) -- lower priority, not claimed
empty. Next natural book: Fletcher & Harley's Cromwell Cruiser Tank,
already in the reference folder, directly relevant to the Cromwell/
Churchill questions this pass reopened.

New design note E.134. No numeric vehicles.csv values changed this pass
-- every correction was a citation, a caveat, or newly-recorded
reference data. No armor_calc output regeneration needed. Test suite
unchanged at 176 passing. `sphinx -W` clean (one more asterisk-adjacent-
backtick leak caught and fixed).

## Update — 2026-09-12 (part 27): a third look at PaK 40 crew quality -- same branch-conflation trap, same honest answer

Scanned the designer's growing reference collection for the best-fitting
candidate to close the PaK 40's still-open crew-quality/fielding-date
questions (E.130). Bryan Perrett's *Sturmartillerie & Panzerjager
1939-45* (Osprey New Vanguard 034) looked like the strongest match found
all session -- a whole-war history of the exact branch name. Read in
full (48 pages).

Answers neither question. The book's own "Panzerjager" means the
self-propelled tank-destroyer vehicle family (Marder/Nashorn/Elefant/
Jagdpanther/Jagdtiger), never the towed PaK 40 as its own weapon system
-- the towed gun appears exactly once, bolted onto a Marder III. This
is precisely the branch-conflation trap E.130's own research already
flagged as a risk, caught immediately from the table of contents rather
than after wasted effort.

One real, inapplicable finding: p.11 gives a genuine, quotable
crew-quality claim ("Assault artillerymen were all volunteers...elite
of their service," 325 German Crosses in Gold, 140 Knight's Crosses) --
but for Sturmgeschutz (assault gun) crews, a different branch this
roster already has a StuG III row for. Recorded as a future lead, not
applied -- this project's vehicle roster has no crew-quality field at
all yet (a separate, already-flagged Appendix H gap). Three dated StuG
III combat anecdotes (Leningrad Sept 1941, Rzhev Aug-Sept 1942) also
found, flagged as a future Rule 18.12 candidate, unrelated to PaK 40.

GER_PAK40_1943.3_F's quality=regular survives a third consecutive
research pass unsourced. Forczyk's *Panzerjager vs KV-1* (in the
reference collection, still unread) remains the best unexploited lead.

New design note E.135, new research file
counters/toe/pak40_sturmartillerie_panzerjager_book_1943.md, pointer
added to GER_PAK40_1943.3_F's own units.csv row. No numeric data
changes, no test count change (176 passing). `sphinx -W` clean on the
first build.

## Update — 2026-09-12 (part 28): PaK 40, fourth try -- real progress, still not a clean answer

Read Forczyk's *Panzerjager vs KV-1: Eastern Front 1941-43* (80 pages)
-- E.135's own recommended next step. Unlike Perrett's book, this one
is genuinely about towed guns (PaK 36/38/40 vs KV-1/KV-2, 1941-43).
Both open questions moved forward, neither closed cleanly.

Crew quality: p.45 gives real, on-topic evidence -- "the Panzerjager
were considered an elite... a large proportion of veterans" as of June
1941. But p.47 documents a morale collapse against KV-1/T-34 that only
partly recovered with PaK 40 arrivals in mid-1942, and p.74-75
documents 45% losses among 1941-42 3.7cm PaK guns -- meaning much of
any 1943 crew would be replacement-draft, not the original hand-picked
cadre. quality=regular KEPT, not upgraded -- a considered decision
informed by better evidence, not an unweighed default.

Fielding date: p.70 gives a quantified answer instead of a date -- even
at Kursk, July 1943, a typical division had only 5-8 heavy PaK guns
against 12 5cm and 40 3.7cm guns. This completes rather than
contradicts the earlier Nafziger "October 1943" lead: those KStN
revisions changed what a division was entitled to, not what it already
had. Real scenario-design implication recorded in infantry_calc/README.md:
a historically accurate 1943 division should field mostly PaK 38 with
a small PaK 40 "heavy platoon" -- PaK 38 flagged as the natural next
towed-gun candidate, not built this pass.

Bonus: a genuine internal contradiction within the one book (spec sheet
says Crew: 8, prose describes a 6-role crew matching this project's
existing figure exactly) -- not resolved. Still no dated towed-PaK-40
anecdote found, a fourth pass reaching the same conclusion.

New design note E.136. No numeric guns.csv/vehicles.csv changes --
crew-quality reasoning and scenario guidance only. Test suite unchanged
at 176 passing. `sphinx -W` clean on the first build.

## Update — 2026-09-12 (part 29): Cromwell/Churchill -- the most-cited unread source turns out empty

Read Fletcher & Harley's *Cromwell Cruiser Tank 1942-50* in full (50
pages, image scan) -- the single most-cited-but-unread source in this
project's history (the existing Cromwell turret-front figure, 76.7mm,
already carries a "p.12" citation to this exact book).

Clean negative, same pattern as WWII Ballistics: this is a production/
organizational/service-history monograph, never a hull/turret
thickness-and-angle table for Cromwell, for anything. Churchill isn't
in the book at all (different vehicle family).

One concrete result: the existing "76.7mm, Fletcher & Harley 2006 p.12"
citation could not be confirmed -- p.12 as read has no armor figure at
all. Doesn't disprove 76.7mm (could be a different edition's
pagination, or the citation may trace to Wikipedia's own infobox
rather than a verified direct read) but is no longer strong evidence
over the uncited 64mm alternative it was preferred over. Flagged in
vehicles.csv's own note.

A real construction detail found but not resolving anything: hull
front/sides described as "made up from two thinner plates," Christie
suspension "sandwiched between the inner and outer plates" -- circumstantial
support for the already-flagged "two spaced plates" theory on Cromwell's
hull side/rear, no thickness figures given.

Two possible anecdotes spotted (mine vulnerability; a Cromwell
surviving five PaK 40 hits at 274m) but not pinned down precisely
enough to cite -- flagged for a dedicated re-read, not fabricated.

Net: Cromwell/Churchill armor geometry is now confirmed unanswerable
by either of the two most obviously-named sources in the library. A
Panzer-Tracts-style detailed technical reference, not another
general-history Osprey monograph, is the more promising remaining
lead -- the same conclusion reached twice now.

New design note E.137. One citation caveat added to vehicles.csv, no
numeric changes. vehicle_top_armor_1943.md updated. Test suite
unchanged at 176 passing. `sphinx -W` clean (two more asterisk-nesting
leaks caught and fixed).

## Update — 2026-09-12 (part 30): Panzer Tracts delivers -- just not on the question it was fetched for

Read Jentz & Doyle's *Panzer Tracts No.8: Sturmgeschutz* (63 pages,
image scan, StuG III's full Ausf.A-G lineage) -- the exact type of
detailed technical reference the last two design notes both
independently pointed to.

**Real correction landed, on a different question.** StuG III Ausf G's
Hull Front is a layered composite, stated directly in the primary
source (p.8-26): "50 mm base plate with 30 mm face-hardened plates
bolted on" -- this project's own vehicles.csv note had explicitly
declined to guess at exactly this construction absent a source. Applied
the same layered_plate_effective_thickness() methodology already used
for Panzer III's own hull front, but with the hardened layer on the
opposite side (StuG III's thinner bolted applique is hardened, not the
thicker base). Effective thickness: 64.2mm (down from flat 80mm).
AV-vs-Capped: 87.1mm -> 64.0mm, a real 23mm reduction. Checked against
the roster's only StuG III Rule 18.12 matchup -- unaffected, StuG III
is the shooter there, not the target.

**The question it was actually fetched for -- Top/Roof armor -- narrowed
but didn't close.** The book has exactly the right diagram structure
(labeled "Armor Specifications" side-profiles with roof callouts) for
Ausf.A/C-E/F-8 -- but never for the plain gun-armed Ausf.G this roster
models; the page sequence jumps straight to a different vehicle's
diagram (the howitzer-armed Sturmhaubitze Ausf.G). A best-effort read
of the closest proxy (Ausf.F/8) suggested ~16mm, consistent with but
not confirming the existing 10-17mm band -- scan resolution wasn't
sharp enough on the small callout digits. A higher-resolution re-read
of the same four diagram pages is now the clear next step.

New design note E.138, new test TestStuGIIILayeredHullFront.
vehicle_top_armor_1943.md and vehicles.csv updated. Appendix H
regenerated (row count unchanged, one figure corrected). Test suite:
177 passing (up from 176). `sphinx -W` clean (one more asterisk-in-
book-title nesting leak caught and fixed).

## Update — 2026-09-12 (part 31): Panzer III's top armor -- a plausible candidate, ruled out

A generically-named "Panzer III" title in the reference collection
looked worth trying given Panzer Tracts No.8's success one book ago.
It wasn't the right book: Culver's *Panzer III in Action*
(Squadron/Signal, 1972) is a photo-caption album whose own
introduction states "there is no text to speak of." Read in full (48
pages) -- no armor-thickness data of any kind, for any plate, anywhere.
Confirmed NOT to be, or cite, Panzer Tracts No. 3-3 (Jentz & Doyle),
which remains the genuinely best-named and still-inaccessible source
for this gap.

One circumstantial, non-numeric corroboration: a caption independently
confirms bolt-on face-hardened applique armor was added to Panzer III
in response to the British 6pdr, consistent with (but not refining)
the project's existing layered-plate treatment. One real, dated
anecdote surfaced incidentally: Hauptmann Peter Frantz's StuG III unit
destroyed 43 T-34s near Stanowoje, 14 March 1943 -- specific and dated
but not detailed enough (no gun/range given) for a Rule 18.12 entry
without more work.

New design note E.139. No data or test changes -- a clean negative,
ruling out one plausible candidate. vehicle_top_armor_1943.md updated.
`sphinx -W` clean on the first build (avoided the recurring book-title-
in-italics leak this time by not nesting emphasis around book titles).

## Update — 2026-09-12 (part 32): Panzer IV Ausf H -- the first book this session to just confirm everything

Read Perrett & Laurier's *Panzerkampfwagen IV Medium Tank 1936-1945*
(49 pages, image scan) to check the long-flagged "widely-cited figure,
not verified vs Panzer Tracts this session" caveat on Ausf H's Hull
Front (80mm@10deg, face-hardened).

Confirmed, with a labeled technical cutaway diagram -- the closest
thing to a Panzer-Tracts-style spec diagram found in any non-Panzer-
Tracts book this session. Four figures matched exactly: Hull Front
80mm, Turret Front 50mm, Turret Side 30mm, Hull Side 30mm. Hull Front's
confirmation includes a real, useful negative: body text explicitly
calls the Ausf H's 80mm "integral," contrasted against the preceding
Ausf G's 30mm bolt-on appliqué construction -- meaning the layered-
plate correction just applied to StuG III (E.138) does NOT apply here,
this is genuinely a single factory plate.

Two loose ends recorded honestly rather than smoothed over: the
book's own face-hardening evidence describes a captured Ausf E's MG
mounting specifically, not the Ausf H's own glacis -- not a
contradiction of the existing Bird & Livingston-sourced claim, just
not an independent re-confirmation of it either. And one unresolved
diagram callout ("20mm armour glasis plate") doesn't match anything in
this project's data and couldn't be located precisely at this scan's
resolution -- flagged, not guessed at.

New design note E.140. No numeric vehicles.csv changes -- four
citation upgrades. No armor_calc regeneration needed. Test suite
unchanged at 177 passing. `sphinx -W` clean on the first build.
