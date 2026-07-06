# Rally Point Action Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a new leader action (Rally Point) that gives Dispersed units a designated rendezvous hex to return to on a successful recovery roll, instead of always reappearing where they dispersed.

**Architecture:** Rules-text-only change across three existing RST files (`section_12__leaders.rst`, `section_10__unit_status.rst`, `appendix_e__design_notes.rst`, `appendix_f__index.rst`). No code changes — no `counters/` package models morale/recovery mechanics, so there is no pipeline, formula, or test suite to touch.

**Tech Stack:** Sphinx + reStructuredText, built with `sphinx_rtd_theme`.

## Global Constraints

- Use the exact rule text from `docs/superpowers/specs/2026-07-06-rally-point-design.md` verbatim — do not paraphrase or "improve" the wording during implementation.
- The new rule is inserted as a lettered sub-rule (`12.6a`) per this project's existing convention (`18.1a`, `12.9.1a`, `8.3.4a`) — never renumber `12.7` through `12.11` to make room.
- Every new/modified rule that references another rule elsewhere gets a `*See also: Rule X.Y (short description)*` note directly beneath it, per Appendix E.59's convention — four-space indent, italic, blank line before and after (match the exact formatting already used at `section_8__fire_combat.rst:158` and `section_20__snipers.rst`'s Rule 20.2.6 note).
- "Nearest" Rally Point is always measured from the hex where the Dispersed unit's own DISPERSED marker sits — never leave a "nearest to what?" ambiguity in the rule text (this exact class of bug was caught and fixed during the design spec's own self-review).
- Verify with a strict Sphinx build (`python3 -m sphinx -b html docs/source /tmp/<dir> -W`) after every RST edit — must print `build succeeded.` with zero warnings before moving on.
- Re-run `python3 -m pytest counters/ maps/ viz/ -q` before committing (expect `171 passed` — unaffected, docs-only change, but this project's established practice is to reconfirm rather than assume).

---

### Task 1: Rule 12.6a, reworded 10.5.4, design note, and index entries

**Files:**
- Modify: `docs/source/section_12__leaders.rst` (insert new `12.6a` section between the existing `12.6` and `12.7` headings)
- Modify: `docs/source/section_10__unit_status.rst:103` (Rule 10.5.4)
- Modify: `docs/source/appendix_e__design_notes.rst` (append new `E.61` note after the existing `E.60` note)
- Modify: `docs/source/appendix_f__index.rst` (DISPERSED zone entry and the Rally section entries)

**Interfaces:** None — this is prose/rules text, not code. No functions, types, or signatures are produced or consumed.

- [ ] **Step 1: Insert Rule 12.6a between the existing 12.6 and 12.7 headings**

In `docs/source/section_12__leaders.rst`, find this exact block (the end of the existing Rule 12.6 table and the start of Rule 12.7):

```
   * - CMD 3 / Elite
     - 2
     - Near-automatic suppressed recovery; Pinned usually succeeds


12.7  Direct Fire Coordination
------------------------------
```

Replace it with (inserting the new sub-section between the 12.6 table and the 12.7 heading):

```
   * - CMD 3 / Elite
     - 2
     - Near-automatic suppressed recovery; Pinned usually succeeds


12.6a  Rally Point Action
-------------------------


**12.6a.1**  A leader spending 1 AP places a RALLY POINT marker in their current hex. A leader may have only one active RALLY POINT marker at a time — placing a new one removes any previous RALLY POINT marker placed by that same leader.

**12.6a.2**  A RALLY POINT marker is not tied to the leader's continued presence or survival — it remains a valid marker on the map even if the placing leader later moves away, becomes a casualty, or is removed from play.

**12.6a.3**  A RALLY POINT marker, once placed, remains a valid destination for the rest of the scenario regardless of subsequent events in that hex, including enemy occupation.

    *See also: Rule 10.5.4 (Dispersed units rally to the nearest RALLY POINT marker, not necessarily where they dispersed).*

**12.6a.4**  If two or more RALLY POINT markers are equally nearest (measured in hexes from the hex where the Dispersed unit's own DISPERSED marker currently sits) when Rule 10.5.4 is resolved, the owning player chooses which one applies.

12.7  Direct Fire Coordination
------------------------------
```

Note the heading underline for `12.6a  Rally Point Action` must be exactly 25 dashes, matching the title's 25 characters (`12.6a  Rally Point Action` with the double space already used throughout this file for its other headings, e.g. `12.6  Rally Action`). The block above already has 25 dashes — verify with:

```bash
python3 -c "
t = '12.6a  Rally Point Action'
u = '-------------------------'
print(len(t), len(u), len(t) == len(u))
"
```

Expected output: `25 25 True`.

- [ ] **Step 2: Reword Rule 10.5.4**

In `docs/source/section_10__unit_status.rst`, find this exact line:

```
**10.5.4**  A Dispersed unit that is not captured may attempt to rally during the Recovery Phase: roll 1d6 + Morale - 2 vs threshold 8. On success, the counter returns to play at rear face (reduced strength) and the DISPERSED marker is removed from the hex. On failure, the counter is removed from the Casualty Track permanently for this scenario and the marker is also removed.
```

Replace it with:

```
**10.5.4**  A Dispersed unit that is not captured may attempt to rally during the Recovery Phase: roll 1d6 + Morale - 2 vs threshold 8. On success, the counter returns to play at rear face (reduced strength) in the hex of the friendly RALLY POINT marker with the fewest hexes between it and the hex where this unit's own DISPERSED marker sits (Rule 12.6a), or in the hex where the DISPERSED marker was if no friendly RALLY POINT marker exists anywhere on the map. The DISPERSED marker is removed from its hex either way. On failure, the counter is removed from the Casualty Track permanently for this scenario and the marker is also removed.

    *See also: Rule 12.6a (Rally Point Action).*
```

- [ ] **Step 3: Verify the two sections build clean so far**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m sphinx -b html docs/source /tmp/rally_point_check1 -W 2>&1 | tail -6
```

Expected: last lines end with `build succeeded.` — if a warning appears about the `12.6a` heading (e.g. "Title underline too short"), fix the underline length per Step 1's note and re-run.

- [ ] **Step 4: Add the Appendix E design note**

In `docs/source/appendix_e__design_notes.rst`, find the last line of the file (the end of the existing `E.60` note):

```
*Design note: Rule 8.3.4 originally banned combining fire from units with different ⬡h values outright, even though the ban was only mathematically required for the same-hex shortcut (Rule 8.3.3) — the general per-unit method (Rule 8.3.2) already computes each unit's own falloff independently before summing, so matching ⬡h was never actually necessary there. Two ways to relax it were checked by direct calculation before choosing either: allowing the group only while every unit stays within the smallest ⬡h in the group (so none has taken any falloff yet) produces the exact same sum the general method already gives — zero skew, just a narrower eligibility window. Forcing the whole group onto the smallest unit's degrade curve at any range was also checked and rejected: at range 9, a mixed ⬡4/⬡5 group's true per-unit sum (11) came out 18% higher than the forced-curve number (9), and by range 20 the gap grows to 4x — the longer-⬡h units get punished on a curve steeper than their own printed weapon, purely for being grouped with a faster-degrading one. Rule 8.3.4a adopts the first approach only.*
```

Append this new section directly after it (with one blank line separating them):

```
E.61  Rally Points — A Destination, Not a Roll Bonus
----------------------------------------------------


*Design note: Before this rule, a leader had zero mechanical ability to help a Dispersed unit — the existing Rally Action (Rule 12.6) is explicitly scoped to Suppressed or Pinned units only. Rally Points close that gap narrowly: they change where a successful Rule 10.5.4 roll sends the returning unit, not whether or how easily it succeeds. The roll itself stays exactly 1d6 + Morale − 2 vs. threshold 8, with no leader bonus of any kind — even though this surfaced a real, pre-existing asymmetry (ordinary Suppressed/Pinned recovery already gets a CMD-adjacency bonus, Rule 5.2.6, that Dispersed rally has never had). That asymmetry is deliberately not closed here; a roll-odds change is a distinct, separable idea for later. Travel to the Rally Point is fully abstracted — the DISPERSED marker never moves, and nothing tracks a path between the dispersal hex and the Rally Point — matching how this project already avoids marker-movement bookkeeping everywhere else in the system. A placed Rally Point is always a valid destination for the rest of the scenario, even if the enemy later occupies that hex, for the same reason: nothing is tracked moving through the intervening hexes, so there is nothing for the enemy to intercept.*
```

Verify the heading underline length the same way as Step 1:

```bash
python3 -c "
t = 'E.61  Rally Points — A Destination, Not a Roll Bonus'
u = '----------------------------------------------------'
print(len(t), len(u), len(t) == len(u))
"
```

Expected output: `52 52 True`. If it prints `False`, count the dashes actually written in the file and correct them to 52 — RST only requires the underline to be *at least* as long as the title, so a longer underline is not a build error, but match it exactly for consistency with the rest of this file's style.

- [ ] **Step 5: Update the Appendix F index — DISPERSED zone entry**

In `docs/source/appendix_f__index.rst`, find this exact block:

```
**DISPERSED zone (Casualty Track)**  ..........  10.5, 13.1

serialised DISPERSED markers  ..........  10.5.2

**Dummy markers**  ..........  14.4
```

Replace it with:

```
**DISPERSED zone (Casualty Track)**  ..........  10.5, 13.1

serialised DISPERSED markers  ..........  10.5.2

rally destination (Rally Point)  ..........  10.5.4, 12.6a

**Dummy markers**  ..........  14.4
```

- [ ] **Step 6: Update the Appendix F index — Rally section entries**

In the same file, find this exact block:

```
**Rally action (leader)**  ..........  12.6

mid-turn recovery at RAL threshold  ..........  12.6.2

**RAL threshold (leader)**  ..........  12.6.4
```

Replace it with:

```
**Rally action (leader)**  ..........  12.6

mid-turn recovery at RAL threshold  ..........  12.6.2

**Rally Point (leader action)**  ..........  12.6a

destination for Dispersed units  ..........  10.5.4, 12.6a

one per leader, replaces previous  ..........  12.6a.1

valid regardless of later enemy control  ..........  12.6a.3

**RAL threshold (leader)**  ..........  12.6.4
```

- [ ] **Step 7: Full strict build verification**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m sphinx -b html docs/source /tmp/rally_point_check2 -W 2>&1 | tail -6
```

Expected: ends with `build succeeded.` and zero warnings.

- [ ] **Step 8: Re-read 12.6a and the reworded 10.5.4 together as a first-time reader**

This is the specific ambiguity check the design spec flagged. Read the rendered HTML (or the raw RST) for both rules back to back and confirm: is there exactly one way to determine which Rally Point a Dispersed unit goes to, with no room to read "nearest" as relative to anything other than the hex the DISPERSED marker sits in? If any wording still reads ambiguously, stop and fix it before proceeding — do not adjust the check to make it pass.

- [ ] **Step 9: Run the test suite as a sanity check**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m pytest counters/ maps/ viz/ -q 2>&1 | tail -3
```

Expected: `171 passed` (unaffected — this task touches no Python code).

- [ ] **Step 10: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add docs/source/section_12__leaders.rst docs/source/section_10__unit_status.rst docs/source/appendix_e__design_notes.rst docs/source/appendix_f__index.rst
git commit -m "$(cat <<'EOF'
feat: add Rally Point leader action for Dispersed units

The existing leader Rally Action (Rule 12.6) is explicitly scoped to
Suppressed or Pinned units only -- leaders had zero mechanical
ability to help a Dispersed unit at all. New Rule 12.6a lets a
leader spend 1 AP to place a RALLY POINT marker in their current
hex (one active per leader, independent of that leader's later
survival, always a valid destination once placed).

Rule 10.5.4's existing Dispersed recovery roll is completely
unchanged (1d6 + Morale - 2 vs threshold 8, no leader bonus) --
what changes is where a successful roll sends the unit: to the
nearest friendly Rally Point instead of always back to the
original dispersal hex, falling back to today's behavior if no
Rally Point exists anywhere on the map.

See docs/superpowers/specs/2026-07-06-rally-point-design.md for
the full design rationale, including why a roll-odds bonus and
marker movement/pathfinding were both deliberately left out of
this narrower scope.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

**This task's deliverable is independently testable:** the strict Sphinx build (Step 7) and the first-time-reader ambiguity check (Step 8) together confirm the rule text is syntactically valid RST and unambiguous about which Rally Point applies, without needing any other task to exist first.

---

## Self-Review Notes

**Spec coverage:** every locked decision in the design spec maps to concrete text in this task — new leader action costing 1 AP (12.6a.1), one active per leader (12.6a.1), marker independent of leader survival (12.6a.2), always valid once placed (12.6a.3), nearest-by-hex-distance with an explicit reference point (10.5.4, 12.6a.4), tie-break to owning player's choice (12.6a.4), no roll bonus (10.5.4 unchanged, called out explicitly in the E.61 note), fully abstracted travel (E.61 note), and the two `*See also*` cross-references applying the E.59 convention at both ends.

**Placeholder scan:** no TBDs — every step shows complete, exact text lifted directly from the design spec, with real underline-length verification commands (not "add a heading" hand-waving).

**Type/interface consistency:** N/A for this plan (rules text, not code) — but rule-number consistency is verified explicitly: `12.6a` is referenced identically in the new rule's own heading, in 10.5.4's rewording, in the Appendix F index entries, and in the E.61 design note. `10.5.4` is referenced identically in 12.6a.3's cross-reference and the Appendix F index entries.
