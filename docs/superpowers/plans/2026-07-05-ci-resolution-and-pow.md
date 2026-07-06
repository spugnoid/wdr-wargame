# CI Resolution and Prisoner-of-War Status Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give every Dispersed or Routing unit exactly two possible endings by the time a scenario ends — it returns to play, or it is captured — closing a real contradiction between Rule 10.5.4 and Rule 10.7.3/13.3, and an undefined case in Section 10.6 (Routing).

**Architecture:** Rules-text-only change across five existing RST files (`section_10__unit_status.rst`, `section_11__prisoners_and_surrender.rst`, `section_13__campaign_rules.rst`, `appendix_e__design_notes.rst`, `appendix_f__index.rst`). No code changes — no `counters/` package models morale/recovery/capture mechanics, so there is no pipeline, formula, or test suite to touch directly.

**Tech Stack:** Sphinx + reStructuredText, built with `sphinx_rtd_theme`.

## Global Constraints

- Use the exact rule text from `docs/superpowers/specs/2026-07-05-ci-resolution-and-pow-design.md` verbatim — do not paraphrase or "improve" the wording during implementation.
- The new capture mechanism is inserted as a lettered sub-rule (`11.2a`) per this project's existing convention (`18.1a`, `12.9.1a`, `8.3.4a`, `12.6a`) — never renumber `11.3` through `11.6` to make room. The two new *trigger* rules (`10.5.6`, `10.6.9`) are plain next-in-sequence numbers, not lettered, because each is appended after the last existing sub-rule in its own numbered list (10.5.5 and 10.6.8 respectively) rather than inserted between two existing rules.
- Every new/modified rule that references another rule elsewhere gets a `*See also: Rule X.Y (short description)*` note directly beneath it, per Appendix E.59's convention — four-space indent, italic, blank line before and after (match the exact formatting already used at `section_10__unit_status.rst:105` and `section_12__leaders.rst:194`).
- Verify with a strict Sphinx build (`python3 -m sphinx -b html docs/source /tmp/<dir> -W`) after every RST edit — must print `build succeeded.` with zero warnings before moving on.
- After Section 13's trim (Task 2), confirm no stray reference to "Dispersed Recovery" or the removed DISPERSED-zone recovery table survives anywhere in the docs — a leftover reference would silently resurrect the exact contradiction this feature exists to close.
- Re-run `python3 -m pytest counters/ maps/ viz/ -q` before the final commit (expect `171 passed` — unaffected, docs-only change, but this project's established practice is to reconfirm rather than assume).

---

### Task 1: Administrative Capture mechanism and its two triggers

**Files:**
- Modify: `docs/source/section_10__unit_status.rst:103` (reword Rule 10.5.4)
- Modify: `docs/source/section_10__unit_status.rst` (insert new Rule 10.5.6 after 10.5.5)
- Modify: `docs/source/section_10__unit_status.rst` (insert new Rule 10.6.9 after 10.6.8)
- Modify: `docs/source/section_11__prisoners_and_surrender.rst` (insert new Rule 11.2a between the existing 11.2 and 11.3 sections)
- Modify: `docs/source/appendix_e__design_notes.rst` (append new `E.62` note after the existing `E.61` note)

**Interfaces:** None — this is prose/rules text, not code. No functions, types, or signatures are produced or consumed. Task 2 depends on this task only in that its Appendix F index entries reference rule numbers (`11.2a`, `10.5.6`, `10.6.9`) defined here.

- [ ] **Step 1: Reword Rule 10.5.4 and insert new Rule 10.5.6**

In `docs/source/section_10__unit_status.rst`, find this exact block:

```
**10.5.4**  A Dispersed unit that is not captured may attempt to rally during the Recovery Phase: roll 1d6 + Morale - 2 vs threshold 8. On success, the counter returns to play at rear face (reduced strength) in the hex of the friendly RALLY POINT marker with the fewest hexes between it and the hex where this unit's own DISPERSED marker sits (Rule 12.6a), or in the hex where the DISPERSED marker was if no friendly RALLY POINT marker exists anywhere on the map. The DISPERSED marker is removed from its hex either way. On failure, the counter is removed from the Casualty Track permanently for this scenario and the marker is also removed.

    *See also: Rule 12.6a (Rally Point Action).*

**10.5.5**  An enemy unit that occupies or is adjacent to a DISPERSED marker may spend 1 AP to formally capture it (see Section 11).

10.6  Routing
-------------
```

Replace it with:

```
**10.5.4**  A Dispersed unit that is not captured may attempt to rally during the Recovery Phase: roll 1d6 + Morale - 2 vs threshold 8. On success, the counter returns to play at rear face (reduced strength) in the hex of the friendly RALLY POINT marker with the fewest hexes between it and the hex where this unit's own DISPERSED marker sits (Rule 12.6a), or in the hex where the DISPERSED marker was if no friendly RALLY POINT marker exists anywhere on the map. The DISPERSED marker is removed from its hex either way. On failure, the unit is captured (Rule 11.2a) and does not receive another rally attempt this scenario.

    *See also: Rule 11.2a (Administrative Capture), Rule 12.6a (Rally Point Action).*

**10.5.5**  An enemy unit that occupies or is adjacent to a DISPERSED marker may spend 1 AP to formally capture it (see Section 11).

**10.5.6**  A Dispersed unit that has not rallied by the end of the scenario is captured (Rule 11.2a).

    *See also: Rule 11.2a (Administrative Capture).*

10.6  Routing
-------------
```

- [ ] **Step 2: Insert new Rule 10.6.9**

In the same file, find this exact block:

```
**10.6.8**  A routing unit counts toward the force's CI total for Force Morale purposes (see Section 15.4).

10.7  Combat Ineffective
------------------------
```

Replace it with:

```
**10.6.8**  A routing unit counts toward the force's CI total for Force Morale purposes (see Section 15.4).

**10.6.9**  A unit still Routing when the scenario ends is captured (Rule 11.2a).

    *See also: Rule 11.2a (Administrative Capture).*

10.7  Combat Ineffective
------------------------
```

- [ ] **Step 3: Verify Section 10's edits build clean so far**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m sphinx -b html docs/source /tmp/ci_pow_check1 -W 2>&1 | tail -6
```

Expected: last lines end with `build succeeded.` (the `Rule 11.2a` cross-references are plain bold text, not Sphinx `:ref:` roles, so the build will succeed even though `11.2a` doesn't exist yet — that's created in Step 4).

- [ ] **Step 4: Insert Rule 11.2a**

In `docs/source/section_11__prisoners_and_surrender.rst`, find this exact block:

```
**11.2.3**  The accepting unit immediately receives a GUARD marker.

11.3  Guard Requirements
------------------------
```

Replace it with:

```
**11.2.3**  The accepting unit immediately receives a GUARD marker.

11.2a  Administrative Capture
-----------------------------

**11.2a.1**  A Dispersed unit whose rally roll fails (Rule 10.5.4), a Dispersed unit that has not rallied by the end of the scenario (Rule 10.5.6), or a unit still Routing when the scenario ends (Rule 10.6.9), is captured automatically. No enemy unit needs to be present or adjacent, and no AP is spent.

**11.2a.2**  If Dispersed, the counter — already resident in the Casualty Track's DISPERSED zone (Rule 10.5.2) — moves to the CAPTURED zone, and the DISPERSED marker is removed from the map. If Routing, the counter and its ROUTING marker are removed from the map together and the counter moves to the CAPTURED zone. Either way, a POW marker is placed in the hex where the unit was captured.

**11.2a.3**  No GUARD marker is placed. Rule 11.3's guard requirements and Rule 11.4's escape attempts do not apply to a unit captured this way — there is no accepting unit to assign a GUARD marker to, and no guard relationship to escape from.

    *See also: Rule 10.5.4 and Rule 10.5.6 (Dispersed rally failure or timeout), Rule 10.6.9 (still Routing at scenario end).*

11.3  Guard Requirements
------------------------
```

Verify the heading underline length before moving on:

```bash
python3 -c "
t = '11.2a  Administrative Capture'
u = '-----------------------------'
print(len(t), len(u), len(t) == len(u))
"
```

Expected output: `29 29 True`.

- [ ] **Step 5: Append the Appendix E design note**

In `docs/source/appendix_e__design_notes.rst`, find the last line of the file (the end of the existing `E.61` note):

```
*Design note (resolved gap): Rule 3.5.1 caps a hex at 3 combat units, with no exception for a unit returning from the Casualty Track (Rule 3.5.2 exempts only leaders). Under the rule's original "always valid, even under enemy occupation" wording, a Rally Point hex already at that limit when a Dispersed unit's rally roll succeeded had no defined resolution — a gap deliberately left unresolved and flagged here for whoever played it out first. The enemy-occupation change above closes it by construction rather than by patching around it: a marker cannot survive to be a rally destination in a hex the enemy holds, so the stacking-limit collision this note originally flagged can no longer arise.*
```

Append this new section directly after it (with one blank line separating them):

```
E.62  CI Resolution — No Unit Left Undecided at Scenario's End
--------------------------------------------------------------

*Design note: Rule 10.5.4's failure clause ("removed from the Casualty Track permanently for this scenario") and Rule 10.7.3's blanket claim that "CI units are tracked on the Casualty Track and may return to play through between-scenario recovery rolls" could not both be true as written — Rule 13.3's DISPERSED zone recovery table implied real between-scenario odds for exactly the units 10.5.4 said were already gone. Routing units had an even larger gap: Rule 10.6 defined how a unit rallies (10.6.6, 10.6.7) or escapes off-map (10.6.5), but nothing at all for a unit still routing when the scenario simply ends. Rather than patch each gap independently, both are resolved the same way: a Dispersed or Routing unit now has exactly two possible endings by the scenario's close — it returns to play, or it is captured (Rule 11.2a). Administrative capture needs no accepting enemy unit and no AP, extending the abstraction Rule 10.7.2 already established (a CI counter has "ceased to function as a tactical element," not a literal, trackable path of individuals) to how that status resolves — the game does not need to know which enemy unit rounded up which stragglers, only that the unit's fate is settled by the time the guns fall silent. It is deliberately exempt from Rule 11.3's guard requirements and Rule 11.4's escape attempts, both of which assume a live in-scenario guarding relationship that an administratively captured unit, by definition, never has; without that exemption an unguarded prisoner would attempt to escape almost every remaining turn, undoing "captured" almost as soon as it happened.*

*This removes the "Dispersed Recovery" path from Section 13 entirely — the 13.2 Recovery Window table's Dispersed Recovery column, 13.3's DISPERSED zone recovery table, and 13.2.2's narrower "attacker loses ground" capture clause are all superseded, since a Dispersed unit is never left in the Casualty Track at a between-scenario boundary anymore. Broken units are deliberately untouched: a Broken unit still leaves the map to a genuine holding zone with no in-scenario resolution path, so 13.3's between-scenario recovery remains exactly the mechanism it needs. The existing voluntary capture (Rule 11.2, an adjacent enemy unit spending 1 AP to accept a Dispersed unit's surrender) is not made redundant by this — a Dispersed unit can keep re-attempting its rally roll every Recovery Phase until it succeeds or fails once, so an enemy player who wants to deny that chance outright, rather than wait for a possible failure, still has a reason to spend the AP and capture it proactively.*
```

Verify the heading underline length:

```bash
python3 -c "
t = 'E.62  CI Resolution — No Unit Left Undecided at Scenario\'s End'
u = '--------------------------------------------------------------'
print(len(t), len(u), len(t) == len(u))
"
```

Expected output: `62 62 True`.

- [ ] **Step 6: Full strict build verification**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m sphinx -b html docs/source /tmp/ci_pow_check2 -W 2>&1 | tail -6
```

Expected: ends with `build succeeded.` and zero warnings.

- [ ] **Step 7: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add docs/source/section_10__unit_status.rst docs/source/section_11__prisoners_and_surrender.rst docs/source/appendix_e__design_notes.rst
git commit -m "$(cat <<'EOF'
feat: add Administrative Capture for unresolved Dispersed/Routing units

Rule 10.5.4's failure clause ("removed from the Casualty Track
permanently for this scenario") and Rule 10.7.3/13.3's blanket
between-scenario recovery claim could not both be true as written.
Routing had an even larger gap: no defined outcome for a unit still
routing when the scenario simply ends.

New Rule 11.2a resolves both: a Dispersed unit whose rally fails
(10.5.4) or times out (new 10.5.6), or a unit still Routing at
scenario end (new 10.6.9), is captured automatically -- no enemy
unit needed, no AP spent, no GUARD marker or escape-attempt
mechanics apply. Every Dispersed/Routing unit now has exactly two
possible endings by the scenario's close: back in play, or POW.

See docs/superpowers/specs/2026-07-05-ci-resolution-and-pow-design.md
for the full rationale, including why Broken units and Rally Points
are untouched and why the existing voluntary-capture rule (11.2)
still has a purpose alongside this.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

**This task's deliverable is independently testable:** the strict Sphinx build (Step 6) confirms the new/reworded rule text is syntactically valid RST, and a reviewer can confirm the mechanism (11.2a) and its two triggers (10.5.4's reworded failure clause, new 10.5.6, new 10.6.9) are complete and internally consistent without needing Task 2's index/Section-13 cleanup to exist first.

---

### Task 2: Remove superseded Section 13 content and update Appendix F index

**Files:**
- Modify: `docs/source/section_13__campaign_rules.rst` (remove the Dispersed Recovery column from the 13.2 table, remove Rule 13.2.2, remove the DISPERSED zone recovery table from 13.3)
- Modify: `docs/source/appendix_f__index.rst` (five edits: new "Administrative Capture" heading, and updates to "Casualty Track," "POW markers," "DISPERSED zone (Casualty Track)," and "Rout" entries)

**Interfaces:** None — prose/index text only. Consumes rule numbers `11.2a`, `10.5.6`, `10.6.9` from Task 1 (used in the new/updated index lines below).

- [ ] **Step 1: Remove the Dispersed Recovery column from the 13.2 Recovery Windows table**

In `docs/source/section_13__campaign_rules.rst`, find this exact block:

```
.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Recovery Window**
     - **Broken Recovery**
     - **Dispersed Recovery**
     - **Combine Halves**
     - **Resupply**
   * - None
     - No roll
     - No roll
     - No
     - No
   * - Hours
     - No roll
     - Roll at -2
     - No
     - Partial
   * - Days
     - Roll
     - Roll
     - Yes
     - Full
   * - Extended
     - Roll at +1
     - Roll at +2
     - Yes
     - Full + bonus
```

Replace it with:

```
.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Recovery Window**
     - **Broken Recovery**
     - **Combine Halves**
     - **Resupply**
   * - None
     - No roll
     - No
     - No
   * - Hours
     - No roll
     - No
     - Partial
   * - Days
     - Roll
     - Yes
     - Full
   * - Extended
     - Roll at +1
     - Yes
     - Full + bonus
```

- [ ] **Step 2: Remove Rule 13.2.2**

In the same file, find this exact block:

```
**13.2.1**  The scenario outcome modifies the Recovery Window: the losing side's window is reduced one step (Days becomes Hours, Hours becomes None).

**13.2.2**  If the attacker loses ground, their Dispersed counters are vulnerable to capture by the defender during the scenario resolution step.

13.3  Between-Scenario Recovery Rolls
-------------------------------------
```

Replace it with:

```
**13.2.1**  The scenario outcome modifies the Recovery Window: the losing side's window is reduced one step (Days becomes Hours, Hours becomes None).

13.3  Between-Scenario Recovery Rolls
-------------------------------------
```

- [ ] **Step 3: Remove the DISPERSED zone recovery table from 13.3**

In the same file, find this exact block:

```
   * - 7+
     - Returns at full strength
     - Returns as rear face


DISPERSED zone recovery (Hours window or better, at penalty; Days or better, normal):

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Roll**
     - **Result**
   * - 1
     - No recovery — removed from campaign pool
   * - 2–3
     - Returns as rear face
   * - 4–5
     - Returns as rear face
   * - 6–7
     - Returns at full strength
   * - 8+
     - Returns at full strength with +1 Experience step


13.4  Combining Half Squads
---------------------------
```

Replace it with:

```
   * - 7+
     - Returns at full strength
     - Returns as rear face


13.4  Combining Half Squads
---------------------------
```

- [ ] **Step 4: Verify Section 13's edits build clean, and confirm no stray "Dispersed" reference survives**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m sphinx -b html docs/source /tmp/ci_pow_check3 -W 2>&1 | tail -6
grep -n "Dispersed" docs/source/section_13__campaign_rules.rst
```

Expected: build ends with `build succeeded.`; the `grep` prints no output (no matches) — confirming the contradiction this feature closes doesn't resurface as a leftover reference.

- [ ] **Step 5: Add a new "Administrative Capture" index heading**

In `docs/source/appendix_f__index.rst`, find this exact block:

```
**Adjustment fire (mortars)**  ..........  16.8

delay  ..........  16.8.2

new sealed slip required  ..........  16.8.2

**Ammunition (AMO)**  ..........  16.3, 20.1.3
```

Replace it with:

```
**Adjustment fire (mortars)**  ..........  16.8

delay  ..........  16.8.2

new sealed slip required  ..........  16.8.2

**Administrative Capture**  ..........  11.2a

no AP, no enemy unit required  ..........  11.2a.1

exempt from GUARD marker and escape attempts  ..........  11.2a.3

triggers: failed Dispersed rally, unrallied at scenario end, still Routing at scenario end  ..........  10.5.4, 10.5.6, 10.6.9

**Ammunition (AMO)**  ..........  16.3, 20.1.3
```

- [ ] **Step 6: Update the "Casualty Track" entry's CAPTURED zone line**

In the same file, find this exact block:

```
**Casualty Track**  ..........  13.1

BROKEN zone  ..........  10.4

CAPTURED zone  ..........  11.2.2

DISPERSED zone  ..........  10.5
```

Replace it with:

```
**Casualty Track**  ..........  13.1

BROKEN zone  ..........  10.4

CAPTURED zone  ..........  11.2.2, 11.2a

DISPERSED zone  ..........  10.5
```

- [ ] **Step 7: Update the "POW markers" entry**

In the same file, find this exact line:

```
**POW markers**  ..........  11.2.2
```

Replace it with:

```
**POW markers**  ..........  11.2.2, 11.2a
```

- [ ] **Step 8: Update the "DISPERSED zone (Casualty Track)" entry**

In the same file, find this exact block:

```
**DISPERSED zone (Casualty Track)**  ..........  10.5, 13.1

serialised DISPERSED markers  ..........  10.5.2

rally destination (Rally Point)  ..........  10.5.4, 12.6a

**Dummy markers**  ..........  14.4
```

Replace it with:

```
**DISPERSED zone (Casualty Track)**  ..........  10.5, 13.1

serialised DISPERSED markers  ..........  10.5.2

rally destination (Rally Point)  ..........  10.5.4, 12.6a

captured on rally failure or timeout  ..........  10.5.4, 10.5.6, 11.2a

**Dummy markers**  ..........  14.4
```

- [ ] **Step 9: Update the "Rout" entry**

In the same file, find this exact block:

```
**Rout**  ..........  10.6, 15.3.3

D3 defined (1d6, halve, round up)  ..........  1.3

D3 hexes away from enemy  ..........  10.6.3

ROUTING marker  ..........  10.6.2

vs Break  ..........  15.3

**S**
```

Replace it with:

```
**Rout**  ..........  10.6, 15.3.3

D3 defined (1d6, halve, round up)  ..........  1.3

D3 hexes away from enemy  ..........  10.6.3

ROUTING marker  ..........  10.6.2

vs Break  ..........  15.3

captured if still routing at scenario end  ..........  10.6.9, 11.2a

**S**
```

- [ ] **Step 10: Full strict build verification**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m sphinx -b html docs/source /tmp/ci_pow_check4 -W 2>&1 | tail -6
```

Expected: ends with `build succeeded.` and zero warnings.

- [ ] **Step 11: Re-read the four rules together as a first-time reader**

This is the specific consistency check the design spec flagged. Read Rules 10.5.4, 10.5.6, 10.6.9, and 11.2a (in the rendered HTML or the raw RST) back to back and confirm: does exactly one rule govern each event (a failed roll, a timed-out Dispersed unit, a still-Routing unit at scenario end), with no two rules claiming authority over the same event the way old Rule 13.2.2 and new Rule 10.5.6 would have if 13.2.2 hadn't been removed? If any wording still reads ambiguously or redundantly, stop and fix it before proceeding — do not adjust the check to make it pass.

- [ ] **Step 12: Run the test suite as a sanity check**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m pytest counters/ maps/ viz/ -q 2>&1 | tail -3
```

Expected: `171 passed` (unaffected — this task touches no Python code).

- [ ] **Step 13: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add docs/source/section_13__campaign_rules.rst docs/source/appendix_f__index.rst
git commit -m "$(cat <<'EOF'
fix: remove Section 13 recovery paths superseded by Administrative Capture

A Dispersed unit is never left in the Casualty Track at a
between-scenario boundary anymore (Rule 11.2a resolves it in-scenario
either way), so the 13.2 Recovery Window table's Dispersed Recovery
column, Rule 13.2.2's narrower "attacker loses ground" capture clause,
and 13.3's DISPERSED zone recovery table are all dead content --
removed rather than left stale. Broken units and their between-scenario
recovery table are untouched.

Also updates the Appendix F index: a new Administrative Capture
heading, and cross-references added to the Casualty Track, POW
markers, DISPERSED zone, and Rout entries.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

**This task's deliverable is independently testable:** the strict Sphinx build (Step 10), the `grep` check for stray "Dispersed" references (Step 4), and the first-time-reader consistency check (Step 11) together confirm Section 13's trim is complete and the whole feature (Task 1 + Task 2) is free of the exact contradiction it set out to close.

---

## Self-Review Notes

**Spec coverage:** every locked decision in the design spec maps to concrete text in these two tasks — 10.5.4's failure clause reworded to capture (Task 1, Step 1), new 10.5.6 for the "ran out of time" case (Task 1, Step 1), new 10.6.9 for still-Routing-at-scenario-end (Task 1, Step 2), new Rule 11.2a with all three locked mechanics (no AP/no enemy required, moves to CAPTURED zone with a POW marker, no GUARD marker or escape attempts) (Task 1, Step 4), the E.62 design note explaining the resolved contradiction and why Broken/Rally Points/voluntary capture are untouched (Task 1, Step 5), and the Section 13 trim of the Dispersed Recovery column, Rule 13.2.2, and the DISPERSED zone recovery table (Task 2, Steps 1-3), plus the Appendix F index updates (Task 2, Steps 5-9).

**Placeholder scan:** no TBDs — every step shows complete, exact text lifted directly from the design spec, with real underline-length verification commands and real find/replace blocks (not "add a rule" or "remove the table" hand-waving).

**Type/interface consistency:** N/A for this plan (rules text, not code) — but rule-number consistency is verified explicitly: `11.2a` is referenced identically in its own heading, in 10.5.4/10.5.6/10.6.9's cross-references, in the E.62 note, and in all five Appendix F index edits. `10.5.6` and `10.6.9` are referenced identically wherever they appear across both tasks.
