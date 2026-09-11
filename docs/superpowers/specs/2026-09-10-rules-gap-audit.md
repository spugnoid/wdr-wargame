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
