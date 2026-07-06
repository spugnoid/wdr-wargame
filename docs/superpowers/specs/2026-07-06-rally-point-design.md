# Rally Point Action — Design Spec

## Why this exists

A Dispersed unit (Rule 10.5) is already the most severe non-permanent
casualty state short of capture: its counter leaves the map entirely for
the Casualty Track, and only a serialised DISPERSED marker remains,
representing scattered survivors physically present in the hex. Rule 10.5.4
already lets that unit attempt a rally roll during the Recovery Phase — but
on success, it has always returned to play in the exact hex where it
dispersed. Meanwhile, the existing leader Rally Action (Rule 12.6) is
explicitly scoped to Suppressed or Pinned units only (Rule 12.6.1) — a
leader currently has zero mechanical ability to help a Dispersed unit at
all. This spec adds that ability: a leader can designate a rendezvous point
in advance, so that scattered survivors have somewhere better than "exactly
where they scattered" to reassemble — matching real small-unit doctrine,
where a designated rally point is precisely for troops who get separated
from their unit.

## Decisions locked

- **A new leader action, costing 1 AP** — matches every other leader
  capability in this game (Inspire, Rally, Direct Fire, Coordinate Assault
  all cost 1 AP). A leader spends 1 AP to place a RALLY POINT marker in
  their current hex.
- **One active Rally Point per leader.** Placing a new one removes that
  same leader's previous one. No unlimited accumulation, no map clutter
  from a long scenario.
- **The marker is independent once placed** — it does not require the
  placing leader to remain nearby, survive, or stay in the game. It is not
  removed if that leader is later hit, wounded, or eliminated.
- **Always valid once placed**, for the rest of the scenario, regardless of
  what happens to that hex afterward — including the enemy occupying or
  controlling it later. No reachability, line-of-sight, or
  enemy-interception check is ever made against it.
- **Fully abstracted travel.** The DISPERSED marker itself never moves —
  it stays exactly where the unit dispersed, exactly as today. Only the
  *returning* counter, on a successful Rule 10.5.4 roll, is placed at the
  Rally Point's hex instead of the dispersal hex. No new movement
  allowance, no pathfinding, no per-turn tracking for DISPERSED markers —
  this game does not track marker movement anywhere else in the system,
  and this addition doesn't start.
- **Nearest Rally Point wins**, by plain hex distance — not tied to a
  specific leader/formation, not filtered by terrain or line of sight. If
  no friendly Rally Point exists anywhere on the map, Rule 10.5.4 falls
  back to exactly its current behavior (return where the unit dispersed).
  Ties between equally-near Rally Points are the owning player's choice,
  matching how this ruleset already resolves an analogous tie elsewhere
  (leader-hit allocation, Rule 12.9.1a: "owning player applies result... of
  their choice").
- **No change to the recovery roll itself.** Rule 10.5.4's roll stays
  exactly 1d6 + Morale − 2 vs. threshold 8, with no leader bonus of any
  kind — even though this surfaced a real, pre-existing asymmetry (ordinary
  Suppressed/Pinned recovery gets a CMD-adjacency bonus per Rule 5.2.6;
  Dispersed rally never has). Deliberately not closed here — this feature
  is scoped to *where* a unit reappears, not *whether* it does; a roll-odds
  change is a distinct, separable idea for later if wanted.

## Rule text

Inserted using this project's existing convention for adding rules without
renumbering what follows (`18.1a`, `12.9.1a`, `8.3.4a`-style lettered
sub-rules) — placed directly after the existing Rally Action (12.6), before
Direct Fire Coordination (12.7), so 12.7 through 12.11 are untouched.

**12.6a Rally Point Action**

**12.6a.1** A leader spending 1 AP places a RALLY POINT marker in their
current hex. A leader may have only one active RALLY POINT marker at a
time — placing a new one removes any previous RALLY POINT marker placed by
that same leader.

**12.6a.2** A RALLY POINT marker is not tied to the leader's continued
presence or survival — it remains a valid marker on the map even if the
placing leader later moves away, becomes a casualty, or is removed from
play.

**12.6a.3** A RALLY POINT marker, once placed, remains a valid destination
for the rest of the scenario regardless of subsequent events in that hex,
including enemy occupation.

&nbsp;&nbsp;&nbsp;&nbsp;*See also: Rule 10.5.4 (Dispersed units rally to
the nearest RALLY POINT marker, not necessarily where they dispersed).*

**12.6a.4** If two or more RALLY POINT markers are equally nearest (measured
in hexes from the hex where the Dispersed unit's own DISPERSED marker
currently sits) when Rule 10.5.4 is resolved, the owning player chooses
which one applies.

**10.5.4** (reworded) A Dispersed unit that is not captured may attempt to
rally during the Recovery Phase: roll 1d6 + Morale − 2 vs. threshold 8. On
success, the counter returns to play at rear face (reduced strength) in the
hex of the friendly RALLY POINT marker with the fewest hexes between it and
the hex where this unit's own DISPERSED marker sits (Rule 12.6a), or in the
hex where the DISPERSED marker was if no friendly RALLY POINT marker
exists anywhere on the map. The DISPERSED marker is removed from its hex
either way. On failure, the counter is removed from the Casualty Track
permanently for this scenario and the marker is also removed.

&nbsp;&nbsp;&nbsp;&nbsp;*See also: Rule 12.6a (Rally Point Action).*

## Documentation touchpoints

- **Appendix E**: add a new design note (next available number after the
  highest currently used) recording this decision — the pre-existing gap
  it closes (leaders had zero mechanical effect on Dispersed units), why
  travel is fully abstracted (matches this project's existing
  no-marker-movement-tracking convention), and why the roll bonus idea was
  deliberately deferred rather than folded in.
- **Appendix F**: add an index entry for "Rally Point" pointing at 12.6a
  and its sub-rules, and update the existing "Dispersed" and "Rally
  (leader)" entries to cross-reference it.
- **Cross-reference notes**: the two `*See also*` notes above are part of
  the rule text itself, applying the Appendix E.59 convention at both ends,
  consistent with how it was first introduced.
- **Section 1 glossary**: check whether other marker types (DISPERSED,
  MOVED, CONTACT, etc.) have their own glossary entries; if that's the
  established pattern, add one for RALLY POINT to match. If markers
  generally aren't glossary terms in this project, skip it — a
  plan-level detail to confirm against the actual file, not a locked
  decision here.

## Out of scope

- No bonus to the Dispersed recovery roll itself (Rule 10.5.4's odds are
  completely unchanged) — a separable future idea, not this one.
- No physical movement or pathfinding for the DISPERSED marker between the
  dispersal hex and the Rally Point.
- No reachability, line-of-sight, or enemy-occupation check against a
  placed Rally Point, ever.
- No per-leader-formation tracking (which unit "belongs" to which leader)
  — the nearest-Rally-Point rule needs none.
- No expiration, duration, or scenario-setup-only restriction on Rally
  Points — they can be placed anytime during play and last until that
  leader replaces their own marker (never automatically, never by any
  other cause).
- No new leader-counter iconography or printed stat changes — this is a
  new available action, not a new counter attribute.

## Validation approach

- No code changes — this is rules-text only, exactly like the
  mixed-interval fire-grouping change. No `counters/` package models
  morale/recovery mechanics, so no pipeline, formula, or test suite is
  touched.
- Verify with a full Sphinx build (`-b html -W`) after the RST edits, per
  this project's standard practice for every docs change.
- Re-verify the rule text doesn't introduce an ambiguity the way the
  mixed-interval fire-grouping rule initially did (stating the same
  condition two inconsistent ways) — read 12.6a and the reworded 10.5.4
  together as a first-time reader before considering this done.
