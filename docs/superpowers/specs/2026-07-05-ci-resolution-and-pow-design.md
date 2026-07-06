# CI Resolution and Prisoner-of-War Status — Design Spec

## Why this exists

Two gaps in the current rules, surfaced together while revising Rally
Points:

- **A real contradiction.** Rule 10.5.4 says a Dispersed unit whose rally
  roll fails has its counter "removed from the Casualty Track permanently
  for this scenario." Rule 10.7.3 says, without exception, "CI units are
  tracked on the Casualty Track and may return to play through
  between-scenario recovery rolls." Rule 13.3 backs 10.7.3 up with a full
  DISPERSED-zone recovery table (odds ranging from "removed from campaign
  pool" to "returns at full strength with +1 Experience"). These cannot
  both be true — either a failed rally ends the unit's story this scenario
  and forever, or it doesn't.
- **An undefined case.** Section 10.6 (Routing) defines how a unit rallies
  back to Normal status (10.6.6, 10.6.7) or escapes off-map to the friendly
  rear (10.6.5, converting to the BROKEN zone) — but says nothing about
  what happens to a unit that is simply still Routing when the scenario
  ends. That unit's fate is currently just unspecified.

This spec resolves both by giving every Dispersed or Routing unit exactly
two possible endings by the time the scenario ends: it returns to play, or
it becomes a prisoner of war. Nothing is left administratively undefined,
and nothing is left contradicting itself.

## Decisions locked

- **Scope: Dispersed and Routing units only.** Broken units are untouched
  and keep Rule 13.3's between-scenario recovery table exactly as it is
  today — a Broken unit already leaves the map to a genuine holding zone
  with no in-scenario resolution path, so between-scenario recovery is
  still the right (and only) mechanism for it.
- **Dispersed units (Rule 10.5.4) — the roll is unchanged.** 1d6 + Morale
  − 2 vs. threshold 8, once per Recovery Phase, using a friendly RALLY
  POINT marker per Rule 12.6a when one exists. Only the outcomes change:
  - **Success** — unchanged, returns to play exactly as today.
  - **Failure** — the unit is captured (new Rule 11.2a) immediately, in
    place of the current "removed... permanently for this scenario"
    wording. It does not get another rally attempt this scenario.
  - **New: still Dispersed at scenario's end.** A unit that disperses too
    late for any further Recovery Phase to occur is also captured (new
    Rule 10.5.6) — the same ending as an explicit roll failure, just
    reached by running out of time instead of failing a roll. This was a
    deliberate choice (not the only option considered): the alternative
    was to give a never-rolled unit one more between-scenario chance since
    "it never really got its shot," but that reintroduces exactly the kind
    of leftover, cross-scenario bookkeeping this spec exists to remove.
    "Still down when the scenario ends" is captured, full stop, regardless
    of why.
- **Routing units (Section 10.6) — also unchanged on both existing
  successful resolutions.** Leader-in-hex rally (10.6.6) and Recovery
  Phase threshold-12 rally (10.6.7) still return the unit to Normal status
  exactly as today. Reaching the friendly map edge (10.6.5) still converts
  it to the BROKEN zone exactly as today — this is an escape, not a
  capture, and Broken is out of scope, so this keeps its existing
  between-scenario recovery chance, unaffected.
  - **New: still Routing at scenario's end (Rule 10.6.9).** A unit that
    never rallied and never reached the friendly edge is captured, same
    mechanism as Dispersed.
- **One capture mechanism, two triggers, defined once.** A new Rule 11.2a
  ("Administrative Capture") states the mechanism a single time — CAPTURED
  zone, POW marker placed, no AP spent, no GUARD marker — and Rules 10.5.4,
  10.5.6, and 10.6.9 each cross-reference it rather than restating it.
  This keeps Section 11 as the one place POW mechanics live, matching how
  the existing voluntary-capture rule already works.
- **The existing voluntary capture (Rule 11.2.1–11.2.2) is untouched and
  still earns its keep.** A Dispersed unit can keep re-attempting 10.5.4
  every Recovery Phase until it either succeeds or fails once — so an
  enemy player who wants to *deny a chance at rally* rather than wait for a
  possible failure still has a reason to spend 1 AP and capture it
  proactively while adjacent. Administrative capture is the fallback for
  units nobody got around to, not a replacement for that tactical choice.
- **No new voluntary-capture mechanic for Routing units.** Rule 11.1.1
  today only allows surrender acceptance against a DISPERSED marker, not a
  Routing counter, and this spec doesn't add one — out of scope, not
  something Rod asked for. A Routing unit's only paths to capture remain
  the automatic ones above.
- **Administrative capture needs no enemy unit present and costs no AP.**
  Rule 10.7.2 already establishes that a CI counter is an abstraction ("has
  ceased to function as a tactical element," not a tracked pile of bodies
  or a literal path of individuals) — this extends the same abstraction to
  resolution. The game doesn't need to know which enemy unit rounded up
  which stragglers, only that the unit's fate is settled by the time the
  guns fall silent.
- **No GUARD marker, and Rule 11.4's escape-attempt mechanic does not
  apply to a unit captured this way.** Both mechanics assume a live,
  in-scenario guarding relationship; an administratively captured unit,
  by definition, has no unit assigned to guard it. Exempting it from
  escape attempts is a deliberate choice, not an oversight: without a
  guard requirement, an unguarded prisoner would otherwise attempt to
  escape essentially every remaining turn, undoing "captured" almost
  immediately. It simply becomes inert for the rest of the scenario —
  consistent with how a DISPERSED marker was already inert before this
  change (Rule 10.5.3: "cannot fire, move, or react... exists solely to
  indicate that men are physically present").
- **Section 13 shrinks as a direct consequence, and this spec removes the
  dead content rather than leaving it stale:**
  - The "Dispersed Recovery" column of the 13.2 Recovery Window table is
    removed. A Dispersed unit is never left in the Casualty Track at a
    between-scenario boundary anymore, so there is no longer anything for
    a between-scenario Dispersed roll to apply to.
  - The "DISPERSED zone recovery" table in Rule 13.3 is removed for the
    same reason.
  - Rule 13.2.2 ("If the attacker loses ground, their Dispersed counters
    are vulnerable to capture by the defender during the scenario
    resolution step") is removed as superseded — it described a narrower,
    outcome-conditional version of exactly what Rule 10.5.6 now does
    unconditionally for every Dispersed unit, win or lose. Keeping both
    would leave two different rules claiming authority over the same
    event.
  - This is a low-stakes trim, not surgery on a locked system: Section 13
    is explicitly marked `[TBD: Campaign rules are not yet fully
    designed... contains the locked framework and placeholder detail]` at
    its own top.
- **Out of scope, noted but not touched: Force Morale CI counting for
  captured units.** Rule 10.7.1 counts Broken, Dispersed, and Routing
  units toward a force's CI total; it's silent on whether a CAPTURED-zone
  unit still counts. That silence predates this spec (voluntary capture,
  Rule 11.2, already created the same question before today) and isn't
  something this spec resolves — flagging it here so it isn't mistaken for
  a gap newly introduced by this change.

## Rule text

**10.5.4** (reworded)

A Dispersed unit that is not captured may attempt to rally during the
Recovery Phase: roll 1d6 + Morale − 2 vs. threshold 8. On success, the
counter returns to play at rear face (reduced strength) in the hex of the
friendly RALLY POINT marker with the fewest hexes between it and the hex
where this unit's own DISPERSED marker sits (Rule 12.6a), or in the hex
where the DISPERSED marker was if no friendly RALLY POINT marker exists
anywhere on the map. The DISPERSED marker is removed from its hex either
way. On failure, the unit is captured (Rule 11.2a) and does not receive
another rally attempt this scenario.

&nbsp;&nbsp;&nbsp;&nbsp;*See also: Rule 11.2a (Administrative Capture),
Rule 12.6a (Rally Point Action).*

**10.5.6** (new, after 10.5.5)

A Dispersed unit that has not rallied by the end of the scenario is
captured (Rule 11.2a).

**10.6.9** (new, after 10.6.8)

A unit still Routing when the scenario ends is captured (Rule 11.2a).

**11.2a Administrative Capture** (new — placed after Rule 11.2's existing
sub-rules 11.2.1–11.2.3, before 11.3 Guard Requirements)

**11.2a.1** A Dispersed unit whose rally roll fails (Rule 10.5.4), a
Dispersed unit that has not rallied by the end of the scenario (Rule
10.5.6), or a unit still Routing when the scenario ends (Rule 10.6.9), is
captured automatically. No enemy unit needs to be present or adjacent, and
no AP is spent.

**11.2a.2** If Dispersed, the counter — already resident in the Casualty
Track's DISPERSED zone (Rule 10.5.2) — moves to the CAPTURED zone, and the
DISPERSED marker is removed from the map. If Routing, the counter and its
ROUTING marker are removed from the map together and the counter moves to
the CAPTURED zone. Either way, a POW marker is placed in the hex where the
unit was captured.

**11.2a.3** No GUARD marker is placed. Rule 11.3's guard requirements and
Rule 11.4's escape attempts do not apply to a unit captured this way —
there is no accepting unit to assign a GUARD marker to, and no guard
relationship to escape from.

&nbsp;&nbsp;&nbsp;&nbsp;*See also: Rule 10.5.4 and Rule 10.5.6 (Dispersed
rally failure or timeout), Rule 10.6.9 (still Routing at scenario end).*

**13.2 Recovery Windows table** (reworded — "Dispersed Recovery" column
removed)

| Recovery Window | Broken Recovery | Combine Halves | Resupply |
|---|---|---|---|
| None | No roll | No | No |
| Hours | No roll | No | Partial |
| Days | Roll | Yes | Full |
| Extended | Roll at +1 | Yes | Full + bonus |

**13.2.2** — removed (superseded by Rule 10.5.6, which resolves every
unrallied Dispersed unit the same way regardless of scenario outcome).

**13.3 Between-Scenario Recovery Rolls** — the "DISPERSED zone recovery"
table and its introductory line are removed in full. The BROKEN zone
recovery table and the Morale-modifier table above it are unaffected.

## Documentation touchpoints

- **Appendix E**: add a new design note (E.62, next available number)
  recording the contradiction this closes, why administrative capture
  needs no enemy unit or AP (extends the existing Rule 10.7.2 abstraction),
  why escape attempts are deliberately exempted, and why Section 13 shrinks
  as a result. Cross-reference Rally Points' own E.61 note where relevant
  (both notes now touch Section 11/CAPTURED-zone mechanics).
- **Appendix F**: add index entries for "Administrative Capture" (→
  11.2a), update the existing "POW markers" entry (currently only
  → 11.2.2) to also point at 11.2a, and update "Dispersed" / "Routing" /
  "Casualty Track" entries to reflect the new capture triggers and the
  removed Section 13 content.
- **Section 1 glossary**: no new marker type is introduced (POW marker
  already exists per Rule 11.2.2); check whether the glossary's POW-marker
  entry, if any, needs a line about the new automatic trigger. Confirm
  against the actual file at plan time rather than assuming here.
- **Cross-reference notes**: apply the Appendix E.59 `*See also*`
  convention at every new link created above (10.5.4 ↔ 11.2a, 10.5.6 ↔
  11.2a, 10.6.9 ↔ 11.2a), at both ends, matching how Rally Points did this
  for 12.6a ↔ 10.5.4.

## Out of scope

- No change to Broken units or Rule 13.3's BROKEN zone recovery table.
- No new voluntary-capture mechanic for Routing units (Rule 11.1.1 stays
  scoped to DISPERSED markers only).
- No change to the Dispersed rally roll's odds, or to Rally Points
  (Rule 12.6a) — this spec only changes what happens on failure/timeout,
  never whether or how easily a unit succeeds.
- No resolution of the pre-existing, unrelated question of whether
  CAPTURED-zone units count toward a force's CI total for Force Morale
  (Rule 10.7.1/15.5) — flagged above, not fixed here.
- No changes to Section 15 (Morale, Break, and Rout) — it defines when a
  unit enters Routing/Broken/Dispersed status, not how that status
  eventually resolves, and this spec only touches resolution.

## Validation approach

- No code changes — this is rules-text only, exactly like Rally Points and
  the mixed-interval fire-grouping change. No `counters/` package models
  morale/recovery/capture mechanics, so no pipeline, formula, or test
  suite is touched.
- Verify with a full Sphinx build (`-b html -W`) after the RST edits, per
  this project's standard practice for every docs change.
- Re-read Rules 10.5.4, 10.5.6, 10.6.9, and 11.2a together as a first-time
  reader before considering this done — specifically checking that no two
  of them claim authority over the same event (the way old 13.2.2 and new
  10.5.6 would have, had 13.2.2 not been removed).
- Confirm Section 13.2's table and 13.3's between-scenario text no longer
  reference "Dispersed" anywhere after the edit — a stray leftover
  reference would silently resurrect the contradiction this spec exists
  to close.
