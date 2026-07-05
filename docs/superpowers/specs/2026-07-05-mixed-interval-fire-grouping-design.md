# Mixed-Interval Fire Grouping — Design Spec

## Why this exists

Rule 8.3.4 currently bans combining fire from units with different `⬡h`
values entirely: "Units with different ⬡h intervals cannot be combined.
Each interval group fires separately and is resolved separately." Mixed-`⬡h`
attacks are instead forced through Rule 8.8 (two separate rolls, combined by
taking the higher result and stepping up once per additional roll that beats
Defence).

Appendix E's existing design note justifies the restriction purely on math
grounds: the falloff formula's floor function doesn't distribute across
different denominators, so the *shortcut* (Rule 8.3.3 — sum rFP and f first,
apply falloff once) breaks with mixed `h`. That's true, but it only applies
to the shortcut. Rule 8.3.2's general method — each unit computes its own
effective rFP independently, then the group sums the results — never needed
matching `h` in the first place. The current rule is stricter than the math
actually requires.

This spec proposes a narrow, mathematically exact relaxation: units with
different `⬡h` may combine, but only while every one of them is still at
full, undegraded rFP.

## Two options considered, one rejected

**Option 1 — combine only while range ≤ the smallest `⬡h` in the group.**
Under this condition, by construction, no unit in the group has crossed its
own first falloff step. The combined rFP is the flat sum of full rFP
values — identical to what Rule 8.3.2's general method already produces.
**This introduces zero mathematical skew.** It's not an approximation; it's
the same number the existing (more tedious) per-unit method would give.
Worked check: a `⬡4 -2` unit (rFP 7) and two `⬡5 -1` units (rFP 5 each) firing
at range 4 — none has fallen off yet, so combined rFP = 7+5+5 = 17, exactly
matching the per-unit sum (7 + 5 + 5, no falloff term for any of them at
this range).

**Option 2 — combine at any range by forcing the whole group onto the
smallest unit's degrade curve.** Rejected. Worked check at range 9 with the
same three units: forcing everyone onto the `⬡4` curve gives
17 − (1+1+2)×floor(8/4) = 17 − 8 = **9**. But each unit's own true effective
rFP at range 9 is 5−1=4, 5−1=4, 7−2×2=3 → true sum = **11**. That's an 18%
understatement, and it gets worse with range: by range 20, forcing the `⬡4`
curve gives 17 − 4×floor(19/4) = 17−16 = **1**, while the true per-unit sum
is 2+2+0 = **4** (Unit C's own formula, 7−2×4, goes negative and floors at
0 rather than firing "negative" rFP) — a 4x understatement. In practice the
Long Range Cap (Rule 8.7) already caps results to Pinned at that range for
either number, so the practical stakes shrink even as the raw skew grows —
the longer-`h` units get penalized on a curve steeper than their own printed
weapon, purely because they were grouped with a faster-degrading one. This
actively misrepresents printed weapon stats rather than simplifying
anything, and is **not adopted**.

## Decision

Adopt Option 1. Units with different `⬡h` may combine into a single fire
group only while every combining unit's firing range does not exceed the
smallest `⬡h` value among them. Beyond that point, the group cannot combine
for that impulse — resolve as separate attacks (Rule 8.8), same as today.

This does not change probability outcomes beyond what grouping-vs-not
already does for same-`⬡h` groups: choosing to combine into one
Resolution-Strip-compressed roll versus firing separately and stepping up
results (Rule 8.8) already produces a different distribution today. Option 1
doesn't introduce a new kind of imbalance — it extends an existing,
accepted tradeoff to a wider (but still narrow, range-bounded) set of cases.

## Rule text

Inserted using this project's existing convention for adding rules without
renumbering what follows (`18.1a`, `12.9.1a`-style lettered sub-rules).

**8.3.4** (reworded) Units with different ⬡h values may combine into a
single fire group only under the conditions given in Rule 8.3.4a. Otherwise,
units with different ⬡h intervals cannot be combined — each fires as a
separate attack (Rule 8.8).

**8.3.4a Mixed-Interval Combining**

**8.3.4a.1** Units with different ⬡h values may form a single fire group
provided every combining unit's firing range does not exceed the smallest
⬡h value among them — equivalently, no unit in the group has yet crossed
its own first falloff step (Rule 8.2).

**8.3.4a.2** Because every combining unit is, by this condition, still at
its full printed rFP, form the group by summing each unit's full rFP
directly — no falloff calculation is required for this group's Resolution
FP.

**8.3.4a.3** The moment any unit's range would exceed its own ⬡h value,
that unit can no longer combine by this method. The group reverts to
separate attacks (Rule 8.8) for that impulse.

**8.3.4a.4** This does not extend the same-hex shortcut (Rule 8.3.3), which
remains valid only for units sharing both hex and ⬡h. Mixed-interval groups
always sum full rFP values directly per 8.3.4a.2.

&nbsp;&nbsp;&nbsp;&nbsp;*See also: Rule 8.8.1 (separate-attack fallback once
any unit crosses its own ⬡h).*

**8.3.4a.5** Example: a ⬡4 -2 unit (rFP 7) and two ⬡5 -1 units (rFP 5 each)
fire at a target 4 hexes away. All three are within their own ⬡h, so they
combine: total rFP = 17, resolved as one group. At 5 hexes, the ⬡4 unit has
crossed its own interval even though the ⬡5 units haven't — the group can no
longer combine. Resolve as two separate attacks instead: the two ⬡5 units
combine as usual (same ⬡h), the ⬡4 unit fires alone, and the results combine
per Rule 8.8.2.

**8.8.1** (reworded) When two or more separate fire groups attack the same
target hex in the same impulse — different ⬡h intervals beyond what Rule
8.3.4a permits, or units firing from different hexes that cannot be
grouped — resolve each attack separately.

&nbsp;&nbsp;&nbsp;&nbsp;*See also: Rule 8.3.4a (mixed-interval combining
within the smallest ⬡h's range).*

## Documentation touchpoints

- **Appendix E**: add a new design note (next available number after E.59)
  recording this decision — the math for both options, why Option 2 was
  rejected, and the "no new kind of imbalance, just a wider eligibility
  window" framing. Follows this project's established pattern of a design
  note per significant rule change.
- **Appendix F**: add index entries for "Mixed-interval combining" /
  "Fire group" pointing at 8.3.4a, matching the project's existing
  indexing thoroughness for Section 8 material.
- **Cross-reference notes**: the two `*See also*` notes above are the rule
  text itself, not a follow-up step — apply the "See also" convention
  (Appendix E.59) at both ends as part of this same change, consistent
  with how it was first introduced.

## Out of scope

- No change to Rule 8.3.3 (same-hex shortcut) or its mathematical proof
  (8.3.6) — both remain exactly as written, valid only for matching `⬡h`.
- No change to Rule 8.8's step-up procedure itself (8.8.2–8.8.4).
- Option 2 is documented above as a rejected alternative (for the historical
  record, same as this project treats other rejected approaches in Appendix
  E) but is not implemented.
- No change to how per-unit modifiers (terrain, exposure, Adjacent Fire
  Bonus) are applied — they already apply per-unit before summing regardless
  of `⬡h`, and nothing here changes that.

## Validation approach

- Re-verify the worked examples in 8.3.4a.5 and the rejected-Option-2 numbers
  above by direct calculation during implementation (matching this project's
  practice of independently re-deriving every worked number before it's
  committed, not just trusting the drafting pass).
- No code changes — this is rules-text only. No `counters/` package models
  fire resolution, so there's no pipeline, formula, or test suite touched by
  this change.
- Verify with a full Sphinx build (`-b html -W`) after the RST edits, per
  this project's standard practice for every docs change.
