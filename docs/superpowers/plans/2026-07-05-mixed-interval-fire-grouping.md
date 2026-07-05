# Mixed-Interval Fire Grouping Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Relax Rule 8.3.4 so units with different `⬡h` values can combine into one fire group while none of them has taken any range falloff yet, replacing an absolute same-`⬡h`-only ban with a narrower, mathematically exact exception.

**Architecture:** Rules-text-only change across three existing RST files (`section_8__fire_combat.rst`, `appendix_e__design_notes.rst`, `appendix_f__index.rst`). No code changes — no `counters/` package models fire resolution, so there is no pipeline, formula, or test suite to touch.

**Tech Stack:** Sphinx + reStructuredText, built with `sphinx_rtd_theme`.

## Global Constraints

- Use the exact rule text from `docs/superpowers/specs/2026-07-05-mixed-interval-fire-grouping-design.md` verbatim — do not paraphrase or "improve" the wording during implementation.
- New rules are inserted as lettered sub-rules (`8.3.4a`) per this project's existing convention (`18.1a`, `12.9.1a`) — never renumber existing rules to make room.
- Every new/modified rule that references another rule elsewhere gets a `*See also: Rule X.Y (short description)*` note directly beneath it, per Appendix E.59's convention — four-space indent, italic, blank line before and after (match the exact formatting already used at `section_8__fire_combat.rst:158`).
- Verify with a strict Sphinx build (`python3 -m sphinx -b html docs/source /tmp/<dir> -W`) after every RST edit — must print `build succeeded.` with zero warnings before moving on.
- Re-run `python3 -m pytest counters/ -q` before committing (expect `140 passed` — unaffected, docs-only change, but this project's established practice is to reconfirm rather than assume).

---

### Task 1: Rule 8.3.4a, reworded 8.3.4/8.8.1, design note, and index entries

**Files:**
- Modify: `docs/source/section_8__fire_combat.rst:52` (Rule 8.3.4), and insert new content after line 56 (after Rule 8.3.6, before the `8.4  Resolution Strip` heading)
- Modify: `docs/source/section_8__fire_combat.rst:166` (Rule 8.8.1)
- Modify: `docs/source/appendix_e__design_notes.rst` (append new `E.60` note after the existing `E.59` note)
- Modify: `docs/source/appendix_f__index.rst:494` (Fire group entry) and `docs/source/appendix_f__index.rst:1068` (Summation rule entry)

**Interfaces:** None — this is prose/rules text, not code. No functions, types, or signatures are produced or consumed.

- [ ] **Step 1: Reword Rule 8.3.4**

In `docs/source/section_8__fire_combat.rst`, find this exact line (currently line 52):

```
**8.3.4**  Units with different ⬡h intervals cannot be combined. Each interval group fires separately and is resolved separately.
```

Replace it with:

```
**8.3.4**  Units with different ⬡h values may combine into a single fire group only under the conditions given in Rule 8.3.4a. Otherwise, units with different ⬡h intervals cannot be combined — each fires as a separate attack (Rule 8.8).
```

- [ ] **Step 2: Insert Rule 8.3.4a after Rule 8.3.6**

In the same file, find this exact block (currently lines 56-58):

```
**8.3.6**  Mathematical proof of the shortcut: for units sharing a hex, the falloff term floor(max(0, range − 1) / h) is identical for every firer — it depends only on range and h. It therefore distributes across the sum: Σ(rFPᵢ − fᵢ × k) = ΣrFPᵢ − (Σfᵢ) × k. The equivalence holds at all ranges, but only when range and intervening terrain are identical for all firers. Units firing from different hexes have different ranges and different sight lines — their effective rFP must be computed per unit before summing (Rule 8.3.2).

8.4  Resolution Strip
```

Replace it with (inserting the new sub-section between 8.3.6 and the 8.4 heading):

```
**8.3.6**  Mathematical proof of the shortcut: for units sharing a hex, the falloff term floor(max(0, range − 1) / h) is identical for every firer — it depends only on range and h. It therefore distributes across the sum: Σ(rFPᵢ − fᵢ × k) = ΣrFPᵢ − (Σfᵢ) × k. The equivalence holds at all ranges, but only when range and intervening terrain are identical for all firers. Units firing from different hexes have different ranges and different sight lines — their effective rFP must be computed per unit before summing (Rule 8.3.2).

8.3.4a  Mixed-Interval Combining
--------------------------------


**8.3.4a.1**  Units with different ⬡h values may form a single fire group provided every combining unit's firing range does not exceed the smallest ⬡h value among them — equivalently, no unit in the group has yet crossed its own first falloff step (Rule 8.2).

**8.3.4a.2**  Because every combining unit is, by this condition, still at its full printed rFP, form the group by summing each unit's full rFP directly — no falloff calculation is required for this group's Resolution FP.

**8.3.4a.3**  The moment any unit's range would exceed its own ⬡h value, that unit can no longer combine by this method. The group reverts to separate attacks (Rule 8.8) for that impulse.

**8.3.4a.4**  This does not extend the same-hex shortcut (Rule 8.3.3), which remains valid only for units sharing both hex and ⬡h. Mixed-interval groups always sum full rFP values directly per 8.3.4a.2.

    *See also: Rule 8.8.1 (separate-attack fallback once any unit crosses its own ⬡h).*

**8.3.4a.5**  Example: a ⬡4 -2 unit (rFP 7) and two ⬡5 -1 units (rFP 5 each) fire at a target 4 hexes away. All three are within their own ⬡h, so they combine: total rFP = 17, resolved as one group. At 5 hexes, the ⬡4 unit has crossed its own interval even though the ⬡5 units haven't — the group can no longer combine. Resolve as two separate attacks instead: the two ⬡5 units combine as usual (same ⬡h), the ⬡4 unit fires alone, and the results combine per Rule 8.8.2.

8.4  Resolution Strip
```

The heading underline for `8.3.4a  Mixed-Interval Combining` must be exactly 32 dashes (the title is 32 characters) — the RST block in Step 2 above already uses 32 dashes, matching. Verify this with:

```bash
python3 -c "
t = '8.3.4a  Mixed-Interval Combining'
u = '-' * 32
print(len(t), len(u), len(t) == len(u))
"
```

Expected output: `32 32 True`. If it prints `False`, count the dashes actually written in the file and correct them to 32 — RST only requires the underline to be *at least* as long as the title, so a longer underline is not a build error, but match it exactly for consistency with the rest of this file's style.

- [ ] **Step 3: Reword Rule 8.8.1**

In the same file, find this exact line (currently line 166, after the Step 2 insertion its line number will have shifted down — locate by text, not line number):

```
**8.8.1**  When two or more separate fire groups attack the same target hex in the same impulse (different ⬡h intervals, or units firing from different hexes that cannot be grouped), resolve each attack separately.
```

Replace it with:

```
**8.8.1**  When two or more separate fire groups attack the same target hex in the same impulse — different ⬡h intervals beyond what Rule 8.3.4a permits, or units firing from different hexes that cannot be grouped — resolve each attack separately.

    *See also: Rule 8.3.4a (mixed-interval combining within the smallest ⬡h's range).*
```

- [ ] **Step 4: Verify the section builds clean so far**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m sphinx -b html docs/source /tmp/mixed_interval_check1 -W 2>&1 | tail -6
```

Expected: last lines end with `build succeeded.` — if a warning appears about the `8.3.4a` heading (e.g. "Title underline too short"), fix the underline length per Step 2's note and re-run.

- [ ] **Step 5: Add the Appendix E design note**

In `docs/source/appendix_e__design_notes.rst`, find the last line of the file (the end of the existing `E.59` note):

```
*Design note: The Section 20/21/22 reorder (moving Snipers and Engineers ahead of Scenario Design Guidelines) surfaced a recurring risk: a rule mentions another rule's concept by name — the Sniper deliberate-targeting exception, say — and only a reader who already knows exactly where to look benefits from the citation. Appendix F's index helps, but only if the reader thinks to go there. The convention adopted going forward: whenever a rule's text depends on or is depended on by a rule elsewhere in the document, add a small indented italic note directly beneath the specific numbered rule — "See also: Rule X.Y (short description)" — at both ends of the reference, not just the end that happens to mention it first. This is applied opportunistically as chapters are touched, not as a one-time retrofit of the whole book; Rule 8.7.4, Rule 12.9.1a, and Rule 20.2 carry the first three notes as a working example.*
```

Append this new section directly after it (with one blank line separating them):

```
E.60  Mixed-Interval Fire Grouping — Bounded by the Smallest ⬡h
---------------------------------------------------------------


*Design note: Rule 8.3.4 originally banned combining fire from units with different ⬡h values outright, even though the ban was only mathematically required for the same-hex shortcut (Rule 8.3.3) — the general per-unit method (Rule 8.3.2) already computes each unit's own falloff independently before summing, so matching ⬡h was never actually necessary there. Two ways to relax it were checked by direct calculation before choosing either: allowing the group only while every unit stays within the smallest ⬡h in the group (so none has taken any falloff yet) produces the exact same sum the general method already gives — zero skew, just a narrower eligibility window. Forcing the whole group onto the smallest unit's degrade curve at any range was also checked and rejected: at range 9, a mixed ⬡4/⬡5 group's true per-unit sum (11) came out 18% higher than the forced-curve number (9), and by range 20 the gap grows to 4x — the longer-⬡h units get punished on a curve steeper than their own printed weapon, purely for being grouped with a faster-degrading one. Rule 8.3.4a adopts the first approach only.*
```

The heading underline for `E.60  Mixed-Interval Fire Grouping — Bounded by the Smallest ⬡h` must be exactly 63 dashes (the title is 63 characters) — the RST block above already uses 63, matching. Verify this with:

```bash
python3 -c "
t = 'E.60  Mixed-Interval Fire Grouping — Bounded by the Smallest ⬡h'
u = '-' * 63
print(len(t), len(u), len(t) == len(u))
"
```

Expected output: `63 63 True`. If it prints `False`, count the dashes actually written in the file and correct them to 63.

Set the underline (`-` characters) to exactly that many characters.

- [ ] **Step 6: Update the Appendix F index — Fire group entry**

In `docs/source/appendix_f__index.rst`, find this exact block:

```
**Fire group**  ..........  1.3, 8.3

grouping by ⬡h interval  ..........  8.3.1

summing rFP and f  ..........  8.3.2
```

Replace it with:

```
**Fire group**  ..........  1.3, 8.3

grouping by ⬡h interval  ..........  8.3.1

mixed-interval combining  ..........  8.3.4a

summing rFP and f  ..........  8.3.2
```

- [ ] **Step 7: Update the Appendix F index — Summation rule entry**

In the same file, find this exact block:

```
**Summation rule (fire groups)**  ..........  8.3, E.5

sum rFP and f, keep h  ..........  8.3.2

valid only within same ⬡h interval  ..........  8.3.4
```

Replace it with:

```
**Summation rule (fire groups)**  ..........  8.3, E.5

sum rFP and f, keep h  ..........  8.3.2

valid within same ⬡h, or mixed ⬡h within the smallest interval  ..........  8.3.4, 8.3.4a
```

- [ ] **Step 8: Full strict build verification**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m sphinx -b html docs/source /tmp/mixed_interval_check2 -W 2>&1 | tail -6
```

Expected: ends with `build succeeded.` and zero warnings.

- [ ] **Step 9: Independently re-verify the worked numbers before committing**

This project's established practice is to re-derive every worked number rather than trust the drafting pass. Run:

```bash
python3 -c "
import math

def eff_rfp(rfp, f, h, rng):
    return rfp - f * math.floor(max(0, rng - 1) / h)

# 8.3.4a.5 worked example: ⬡4 -2 unit (rFP 7), two ⬡5 -1 units (rFP 5 each)
# at range 4 -- none should have fallen off yet.
units = [(7, 2, 4), (5, 1, 5), (5, 1, 5)]
range_ = 4
total = sum(eff_rfp(rfp, f, h, range_) for rfp, f, h in units)
print('Range 4 combined (should be 17, no falloff on anyone):', total)
assert total == 17

# E.60 design note: range 9, true per-unit sum vs forced-smallest-h sum
range_ = 9
true_sum = sum(eff_rfp(rfp, f, h, range_) for rfp, f, h in units)
forced_h = 4
forced_sum = sum(rfp for rfp, f, h in units) - sum(f for rfp, f, h in units) * math.floor(max(0, range_ - 1) / forced_h)
print('Range 9 true sum (should be 11):', true_sum)
print('Range 9 forced-⬡4-curve sum (should be 9):', forced_sum)
assert true_sum == 11 and forced_sum == 9
print('Understatement at range 9:', round((true_sum - forced_sum) / true_sum * 100, 1), '% (should be ~18.2%)')

# range 20
range_ = 20
true_sum = sum(max(0, eff_rfp(rfp, f, h, range_)) for rfp, f, h in units)
forced_sum = sum(rfp for rfp, f, h in units) - sum(f for rfp, f, h in units) * math.floor(max(0, range_ - 1) / forced_h)
print('Range 20 true sum (should be 4, Unit C floored at 0):', true_sum)
print('Range 20 forced-⬡4-curve sum (should be 1):', forced_sum)
assert true_sum == 4 and forced_sum == 1
print('All worked numbers confirmed.')
"
```

Expected: all `assert` statements pass silently, and the final line prints `All worked numbers confirmed.` If any assertion fails, stop and re-check the rule text and design note against the spec before proceeding — do not adjust the verification script to make it pass.

- [ ] **Step 10: Run the test suite as a sanity check**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
python3 -m pytest counters/ -q 2>&1 | tail -3
```

Expected: `140 passed` (unaffected — this task touches no Python code).

- [ ] **Step 11: Commit**

```bash
cd /home/marvin/ClaudeCodeProjects/wdr_repo
git add docs/source/section_8__fire_combat.rst docs/source/appendix_e__design_notes.rst docs/source/appendix_f__index.rst
git commit -m "$(cat <<'EOF'
feat: allow mixed-⬡h fire grouping within the smallest interval

Rule 8.3.4 previously banned combining fire from units with
different ⬡h values entirely, even though the ban was only
mathematically required for the same-hex shortcut (Rule 8.3.3) --
the general per-unit method (Rule 8.3.2) already computes each
unit's own falloff independently before summing, so matching ⬡h
was never actually necessary there.

New Rule 8.3.4a permits combining across ⬡h while every unit in the
group is still within its own first falloff step (equivalently:
range does not exceed the smallest ⬡h among them). Verified this
introduces zero skew -- it's the same sum Rule 8.3.2's general
method already produces. A rejected alternative (force the whole
group onto the smallest unit's degrade curve at any range) was
checked and shown to understate the longer-⬡h units' firepower by
18% at range 9 and 4x by range 20, recorded in the new Appendix
E.60 design note for the historical record.

See docs/superpowers/specs/2026-07-05-mixed-interval-fire-grouping-design.md
for the full design rationale.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

**This task's deliverable is independently testable:** the strict Sphinx build (Step 8) and the worked-number verification (Step 9) together confirm the rule text is syntactically valid RST and the math it describes is correct, without needing any other task to exist first.
