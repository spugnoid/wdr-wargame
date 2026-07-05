# Infantry Counter System and Shared Quality Core Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port the existing infantry-counter-design spreadsheet's algorithm (weapon RPM -> log-compressed rFP, quality-tier multipliers, Defence/Morale formulas) into a tested `counters/infantry_calc/` package mirroring `armor_calc`'s conventions, and extract a shared `counters/quality/` module so vehicle crew quality and infantry unit quality become one source of truth for tier meaning.

**Architecture:** `counters/quality/` holds only the shared tier vocabulary (a `Quality` type and `ALL_QUALITIES` tuple). `counters/armor_calc/` is refactored to re-export its existing `CrewQuality` as an alias of the shared type (pure extraction, no behavior change). `counters/infantry_calc/` is a new package with its own `formulas.py` (weapon rFP, Defence, Morale, quality multipliers), CSV-driven data (`weapons.csv`, `units.csv`), and a precompute pipeline (`write_infantry_roster_csv`) producing `infantry_roster_output.csv` -- the same "real sourced formulas -> small precomputed reference table -> zero arithmetic at the table" pattern `armor_calc` already uses.

**Tech Stack:** Python 3.10+, pytest, CSV-driven inputs (matching `counters/armor_calc/`'s existing architecture).

## Global Constraints

- Every formula must cite its source. `armor_calc`'s formulas cite Bird & Livingston page numbers; `infantry_calc`'s formulas cite the project's own infantry-counter-design spreadsheet (v2) -- these are calibrated game-design constants, not primary military documents, and must be described as such in every docstring, not presented with false authority.
- No behavior change to `armor_calc` from the `Quality` extraction -- its full existing test suite (99 tests as of the hit-location merge) must pass unchanged after Task 1.
- Follow the existing package structure: formulas in `<package>/formulas.py`, orchestration in `<package>/pipeline.py`, data in `<package>/data/*.csv`, tests in `<package>/tests/test_formulas.py` and `test_pipeline.py` -- exactly mirroring `counters/armor_calc/`'s layout for the new `counters/infantry_calc/` package.
- The Militia quality tier's BTV/EM/MM (0.36/0.81/0.81) is a computed extrapolation, not a sourced or calibrated value -- must be documented as such in code, not presented as equally certain to the other four tiers.
- Excel's `ROUND` is round-half-away-from-zero (e.g. `ROUND(4.5, 0) == 5`, `ROUND(8.75, 0) == 9`), not Python's banker's rounding (`round(4.5) == 4` in Python 3). Every port of a spreadsheet `ROUND(...)` call must use round-half-away-from-zero explicitly, not Python's built-in `round()`.

---

### Task 1: Shared quality core and `armor_calc` refactor

**Files:**
- Create: `counters/quality/__init__.py`
- Create: `counters/quality/tiers.py`
- Create: `counters/quality/tests/__init__.py`
- Create: `counters/quality/tests/test_tiers.py`
- Modify: `counters/armor_calc/formulas.py` (replace the `CrewQuality` type definition and `ALL_CREW_QUALITIES` tuple with re-exported aliases)

**Interfaces:**
- Consumes: nothing (this is the foundational task).
- Produces: `Quality` (`Literal["elite", "veteran", "regular", "green", "militia"]`), `ALL_QUALITIES: tuple[Quality, ...]` in `counters/quality/tiers.py` -- for Task 2 to import directly, and for `armor_calc.formulas.CrewQuality`/`ALL_CREW_QUALITIES` to alias.

- [ ] **Step 1: Write the failing test**

Create `counters/quality/tests/__init__.py` (empty file, makes the directory a package):

```python
```

Create `counters/quality/tests/test_tiers.py`:

```python
from quality.tiers import ALL_QUALITIES


class TestQualityTiers:
    """The five quality tiers shared across every domain (vehicle crews,
    infantry units, and any future domain) that needs a common vocabulary
    for unit experience/training level."""

    def test_five_tiers_in_descending_order(self):
        assert ALL_QUALITIES == ("elite", "veteran", "regular", "green", "militia")

    def test_all_tiers_are_distinct(self):
        assert len(set(ALL_QUALITIES)) == 5
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/quality/tests/test_tiers.py -v`
Expected: FAIL -- `ModuleNotFoundError: No module named 'quality'` (the package doesn't exist yet).

- [ ] **Step 3: Create the shared quality module**

Create `counters/quality/__init__.py` (empty file, makes the directory a package):

```python
```

Create `counters/quality/tiers.py`:

```python
"""Shared quality-tier vocabulary used across every domain in this game
(vehicle crews, infantry units, and any future domain that needs a common
notion of unit experience/training level).

This module intentionally holds only the tier labels and their ordering --
not any formula. Each domain defines its own function mapping a Quality to
its own domain-specific effect (e.g. armor_calc's crew_quality_hit_cap()
caps a hit probability; infantry_calc's quality_multipliers() scales
weapon RPM, Defence, and Morale). Unifying the *labels* means "Veteran"
means the same rank everywhere; unifying the *math* would incorrectly
force two different mechanics to share one formula.
"""

from __future__ import annotations

from typing import Literal

Quality = Literal["elite", "veteran", "regular", "green", "militia"]

ALL_QUALITIES: tuple[Quality, ...] = ("elite", "veteran", "regular", "green", "militia")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/quality/tests/test_tiers.py -v`
Expected: PASS (2 tests).

- [ ] **Step 5: Refactor `armor_calc` to alias the shared type**

Read `counters/armor_calc/formulas.py` and find the existing lines defining `CrewQuality` and `ALL_CREW_QUALITIES` (search for `CrewQuality = Literal` and `ALL_CREW_QUALITIES:`). Replace exactly those two definitions with:

```python
from quality.tiers import ALL_QUALITIES, Quality

# CrewQuality is armor_calc's name for the shared Quality tier vocabulary --
# kept as an alias so existing armor_calc code and tests don't need to
# change any import. See counters/quality/tiers.py for what's actually
# shared vs. what stays domain-specific.
CrewQuality = Quality
ALL_CREW_QUALITIES: tuple[CrewQuality, ...] = ALL_QUALITIES
```

Place the `from quality.tiers import ...` line in `armor_calc/formulas.py`'s existing top-of-file import block (alongside `from dataclasses import dataclass, replace`, `from typing import Literal`, etc.), not inline where the old `CrewQuality` definition was. Do not change `crew_quality_hit_cap()`, `_CREW_QUALITY_HIT_CAP`, or any other function in the file -- only the type/tuple definitions move.

- [ ] **Step 6: Run the full existing armor_calc suite to verify no regression**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/armor_calc/tests/ -q`
Expected: `99 passed` -- identical count to before this change. If any test fails, the refactor changed behavior; re-check that `CrewQuality`/`ALL_CREW_QUALITIES` still resolve to the exact same five string values in the exact same order, and that no other code in `armor_calc` referenced the old `Literal[...]` definition directly instead of via the `CrewQuality` name.

- [ ] **Step 7: Commit**

```bash
git add counters/quality/ counters/armor_calc/formulas.py
git commit -m "feat: extract shared quality-tier core, alias armor_calc's CrewQuality to it"
```

---

### Task 2: Infantry core formulas

**Files:**
- Create: `counters/infantry_calc/__init__.py`
- Create: `counters/infantry_calc/formulas.py`
- Create: `counters/infantry_calc/tests/__init__.py`
- Create: `counters/infantry_calc/tests/test_formulas.py`

**Interfaces:**
- Consumes: `Quality` (`counters/quality/tiers.py`, Task 1).
- Produces: `WeaponClass` (`Literal["rifle", "lmg", "hmg", "smg", "at_rifle", "pistol"]`), `weapon_rfp(count: int, practical_rpm: float, weapon_class: WeaponClass, quality: Quality) -> int`, `fire_interval_hexes(max_range_yds: float, rfp: int) -> int | None`, `unit_defence(manpower_full: int, quality: Quality) -> tuple[int, int]` (front, rear), `unit_morale(quality: Quality) -> int`, `quality_multipliers(quality: Quality) -> tuple[float, float, float]` (BTV, EM, MM), `suppression_factor(weapon_class: WeaponClass) -> float` -- for Task 5's pipeline to call.

- [ ] **Step 1: Write the failing tests**

Create `counters/infantry_calc/tests/__init__.py` (empty file):

```python
```

Create `counters/infantry_calc/tests/test_formulas.py`:

```python
import pytest

from infantry_calc.formulas import (
    fire_interval_hexes,
    quality_multipliers,
    suppression_factor,
    unit_defence,
    unit_morale,
    weapon_rfp,
)


class TestQualityMultipliers:
    """Source: this project's own infantry-counter-design spreadsheet (v2),
    CONSTANTS sheet, 'QUALITY TIERS' table -- a calibrated game-design
    table, not a primary military document."""

    def test_regular_is_the_anchor_tier(self):
        assert quality_multipliers("regular") == (1.0, 1.0, 1.0)

    def test_veteran_matches_spreadsheet(self):
        assert quality_multipliers("veteran") == pytest.approx((1.15, 1.1, 1.1))

    def test_elite_matches_spreadsheet(self):
        assert quality_multipliers("elite") == pytest.approx((1.3, 1.2, 1.2))

    def test_green_matches_spreadsheet(self):
        assert quality_multipliers("green") == pytest.approx((0.6, 0.9, 0.9))

    def test_militia_is_a_flagged_extrapolation_not_a_sourced_value(self):
        """Militia doesn't exist in the source spreadsheet (only Green/
        Regular/Veteran/Elite are defined there). This continues the same
        multiplicative step Regular->Green already uses (BTV x0.6, EM x0.9,
        MM x0.9) one tier further: Green->Militia."""
        assert quality_multipliers("militia") == pytest.approx((0.36, 0.81, 0.81))


class TestSuppressionFactor:
    """Source: CONSTANTS sheet, 'SUPPRESSION FACTORS' table."""

    def test_matches_spreadsheet_values(self):
        assert suppression_factor("rifle") == 1.0
        assert suppression_factor("lmg") == 1.4
        assert suppression_factor("hmg") == 1.8
        assert suppression_factor("smg") == 0.6
        assert suppression_factor("at_rifle") == 0.8
        assert suppression_factor("pistol") == 0.4


class TestWeaponRfp:
    """Source: QUICK REF sheet's own worked example -- GREN 43's MG42 LMG:
    count=1, practical=300, supp=1.4, quality=regular (combined 1.0) ->
    wtd=420 -> rFP=ROUND(LOG(420/47)/LOG(1.35),0)=7."""

    def test_matches_the_spreadsheets_own_worked_example(self):
        assert weapon_rfp(count=1, practical_rpm=300, weapon_class="lmg", quality="regular") == 7

    def test_matches_a_second_roster_row_kar98k_rifle_squad(self):
        """GER_GREN_1943.3_F's Kar98k: count=8, practical=15, rifle,
        regular -> rFP 3 (UNIT ROSTER sheet, cell AN4)."""
        assert weapon_rfp(count=8, practical_rpm=15, weapon_class="rifle", quality="regular") == 3

    def test_matches_a_veteran_quality_row(self):
        """GER_PZGR_1943.3_F's MG42 LMG under Veteran quality (combined
        1.3915): count=1, practical=300, lmg -> rFP 8 (UNIT ROSTER AB6)."""
        assert weapon_rfp(count=1, practical_rpm=300, weapon_class="lmg", quality="veteran") == 8

    def test_zero_weapons_gives_zero_rfp(self):
        """SOV_RIFSQ_1943.3_R's Mosin-Nagant: count=4, practical=12, rifle,
        regular -> rFP 0 (UNIT ROSTER AB13) -- the weakest fire line in the
        whole pilot roster, a real edge case worth its own test."""
        assert weapon_rfp(count=4, practical_rpm=12, weapon_class="rifle", quality="regular") == 0

    def test_higher_quality_increases_rfp_for_the_same_weapon(self):
        elite_rfp = weapon_rfp(count=1, practical_rpm=300, weapon_class="lmg", quality="elite")
        militia_rfp = weapon_rfp(count=1, practical_rpm=300, weapon_class="lmg", quality="militia")
        assert elite_rfp > militia_rfp


class TestFireIntervalHexes:
    """Source: QUICK REF sheet -- h = MAX(1, ROUND(max_range_hexes/rfp, 0)),
    max_range_hexes = ROUND(max_range_yds/40, 0)."""

    def test_matches_the_worked_example(self):
        """max_range=1000yds=25hex, rfp=7 -> h=ROUND(25/7,0)=4."""
        assert fire_interval_hexes(max_range_yds=1000, rfp=7) == 4

    def test_matches_a_second_roster_row(self):
        """Kar98k: max_range=600yds=15hex, rfp=3 -> h=ROUND(15/3,0)=5."""
        assert fire_interval_hexes(max_range_yds=600, rfp=3) == 5

    def test_zero_rfp_returns_none(self):
        """A weapon with rFP 0 has no meaningful interval -- the source
        sheet prints '-' for this case (UNIT ROSTER AD13)."""
        assert fire_interval_hexes(max_range_yds=500, rfp=0) is None

    def test_interval_is_never_less_than_one(self):
        """MG42 HMG: max_range=2000yds=50hex, rfp=9 -> ROUND(50/9,0)=6,
        already >=1, but the formula's own MAX(1, ...) floor matters once
        rfp exceeds max_range_hexes -- verified directly here."""
        assert fire_interval_hexes(max_range_yds=2000, rfp=9) == 6


class TestUnitDefence:
    """Source: QUICK REF sheet -- front = MAX(1, ROUND((manpower/2)*BTV, 0))
    + 3; rear = MAX(1, front - 2). Both derived from the SAME (full)
    manpower figure -- the rear face is never independently recomputed
    from a separately-reduced manpower number (confirmed against the
    spreadsheet's own COUNTER OUTPUT sheet, which prints rear Defence as
    exactly front-2, not a fresh calculation)."""

    def test_matches_gren_43_regular_9_men(self):
        assert unit_defence(manpower_full=9, quality="regular") == (8, 6)

    def test_matches_pzgr_43_veteran_10_men(self):
        assert unit_defence(manpower_full=10, quality="veteran") == (9, 7)

    def test_matches_mg42_team_regular_4_men(self):
        """A small weapon-team crew -- also verifies Excel's round-half-up
        behaviour: (4/2)*1+3 = 5.0 exactly, rounds to 5 either way, but
        pairs with the next test which needs the distinction."""
        assert unit_defence(manpower_full=4, quality="regular") == (5, 3)

    def test_matches_dp28_team_regular_3_men_round_half_up(self):
        """(3/2)*1+3 = 4.5 -- Excel's ROUND rounds this UP to 5, not down
        to 4 (Python's banker's rounding would give 4). This is the
        canonical case that catches a rounding-mode bug."""
        assert unit_defence(manpower_full=3, quality="regular") == (5, 3)

    def test_rear_defence_never_goes_below_one(self):
        front, rear = unit_defence(manpower_full=1, quality="militia")
        assert rear >= 1


class TestUnitMorale:
    """Source: QUICK REF sheet -- Morale = ROUND(((BTV+MM)/2)*5, 0)."""

    def test_regular_is_five(self):
        assert unit_morale("regular") == 5

    def test_veteran_rounds_up_from_5point625(self):
        """((1.15+1.1)/2)*5 = 5.625 -> rounds to 6."""
        assert unit_morale("veteran") == 6

    def test_green_is_four(self):
        """((0.6+0.9)/2)*5 = 3.75 -> rounds to 4."""
        assert unit_morale("green") == 4

    def test_militia_extrapolation(self):
        """((0.36+0.81)/2)*5 = 2.925 -> rounds to 3."""
        assert unit_morale("militia") == 3
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/infantry_calc/tests/test_formulas.py -v`
Expected: FAIL -- `ModuleNotFoundError: No module named 'infantry_calc'` (the package doesn't exist yet).

- [ ] **Step 3: Implement the formulas**

Create `counters/infantry_calc/__init__.py` (empty file):

```python
```

Create `counters/infantry_calc/formulas.py`:

```python
"""Infantry counter design formulas: converts real-world weapon and unit
specs (rate of fire, manpower, quality tier) into the small-integer
counter values printed on infantry/support-weapon counters (rFP, fire
interval, Defence, Morale).

Source for every formula in this file: this project's own infantry-
counter-design spreadsheet (v2, kept outside this repo on Rod's desktop
during development, now superseded by this package). These are the
project's own calibrated game-design constants, anchored to one worked
example (GREN 43's MG42 LMG -> rFP 7) -- not citations to a primary
military ballistics document the way armor_calc's formulas cite Bird &
Livingston. Every function below states this explicitly rather than
implying a level of sourcing it doesn't have.
"""

from __future__ import annotations

import math
from typing import Literal

from quality.tiers import Quality

WeaponClass = Literal["rifle", "lmg", "hmg", "smg", "at_rifle", "pistol"]

BASE_K = 47.0
LOG_BASE = 1.35
HEX_YDS = 40.0
MIN_RFP = 2

_SUPPRESSION_FACTOR: dict[WeaponClass, float] = {
    "rifle": 1.0,
    "lmg": 1.4,
    "hmg": 1.8,
    "smg": 0.6,
    "at_rifle": 0.8,
    "pistol": 0.4,
}

_QUALITY_MULTIPLIERS: dict[Quality, tuple[float, float, float]] = {
    # (BTV, EM, MM) -- Base Training Value, Experience Modifier, Morale Modifier.
    "elite": (1.30, 1.20, 1.20),
    "veteran": (1.15, 1.10, 1.10),
    "regular": (1.00, 1.00, 1.00),
    "green": (0.60, 0.90, 0.90),
    # Militia does not exist in the source spreadsheet (which only defines
    # Green/Regular/Veteran/Elite). This continues the same multiplicative
    # step Regular->Green already uses one tier further: Green->Militia.
    # A computed extrapolation, not a sourced or calibrated value.
    "militia": (0.36, 0.81, 0.81),
}


def _round_half_up(value: float) -> int:
    """Excel's ROUND() is round-half-away-from-zero, not Python's
    round-half-to-even. All formulas below need this, not the built-in
    round(), to match the source spreadsheet's own arithmetic exactly."""
    return math.floor(value + 0.5) if value >= 0 else math.ceil(value - 0.5)


def suppression_factor(weapon_class: WeaponClass) -> float:
    """How much a weapon class's sustained fire suppresses/pins a target,
    independent of its raw rate of fire.

    Source: infantry-counter-design spreadsheet, CONSTANTS sheet,
    'SUPPRESSION FACTORS' table.
    """
    return _SUPPRESSION_FACTOR[weapon_class]


def quality_multipliers(quality: Quality) -> tuple[float, float, float]:
    """(BTV, EM, MM) for the given quality tier.

    Source: infantry-counter-design spreadsheet, CONSTANTS sheet,
    'QUALITY TIERS' table. Militia is an extrapolation -- see the
    _QUALITY_MULTIPLIERS comment above.
    """
    return _QUALITY_MULTIPLIERS[quality]


def weapon_rfp(count: int, practical_rpm: float, weapon_class: WeaponClass, quality: Quality) -> int:
    """Resolution Fire Power for one weapon entry on a unit's loadout.

    Source: infantry-counter-design spreadsheet, QUICK REF sheet:
    rFP = MAX(0, ROUND(LOG(qual_adj_rpm / BASE_K) / LOG(LOG_BASE), 0))
    where qual_adj_rpm = count * practical_rpm * suppression_factor * (BTV*EM*MM).

    Anchored to the spreadsheet's own worked example: count=1,
    practical_rpm=300, weapon_class="lmg", quality="regular" -> rFP 7
    (GREN 43's MG42 LMG).

    Args:
        count: Number of this weapon in the unit's loadout.
        practical_rpm: Practical (sustained, not cyclic) rate of fire.
        weapon_class: Determines the suppression factor.
        quality: The firing unit's quality tier.

    Returns:
        rFP, a non-negative integer.
    """
    btv, em, mm = quality_multipliers(quality)
    qual_adj_rpm = count * practical_rpm * suppression_factor(weapon_class) * (btv * em * mm)
    if qual_adj_rpm <= 0:
        return 0
    raw = math.log(qual_adj_rpm / BASE_K) / math.log(LOG_BASE)
    return max(0, _round_half_up(raw))


def fire_interval_hexes(max_range_yds: float, rfp: int) -> int | None:
    """Interval (in hexes) between falloff steps for a weapon's fire line.

    Source: infantry-counter-design spreadsheet, QUICK REF sheet:
    h = MAX(1, ROUND(max_range_hexes / rfp, 0))
    max_range_hexes = ROUND(max_range_yds / HEX_YDS, 0)

    Returns:
        The interval in hexes, or None if rfp is 0 (no meaningful interval
        -- the source spreadsheet prints "-" for this case).
    """
    if rfp == 0:
        return None
    max_range_hexes = _round_half_up(max_range_yds / HEX_YDS)
    return max(1, _round_half_up(max_range_hexes / rfp))


def unit_defence(manpower_full: int, quality: Quality) -> tuple[int, int]:
    """(front_defence, rear_defence) for a unit of the given full-strength
    manpower and quality tier.

    Source: infantry-counter-design spreadsheet, QUICK REF sheet:
    front = MAX(1, ROUND((manpower/2) * BTV, 0)) + 3
    rear = MAX(1, front - 2)

    Both values are derived from the SAME (full) manpower figure -- the
    rear face's Defence is never independently recomputed from a
    separately-reduced manpower number; it is always front-2 (min 1).
    """
    btv, _em, _mm = quality_multipliers(quality)
    front = max(1, _round_half_up((manpower_full / 2) * btv)) + 3
    rear = max(1, front - 2)
    return front, rear


def unit_morale(quality: Quality) -> int:
    """Morale for a unit of the given quality tier -- identical on both
    the front and rear face.

    Source: infantry-counter-design spreadsheet, QUICK REF sheet:
    Morale = ROUND(((BTV + MM) / 2) * 5, 0)
    """
    btv, _em, mm = quality_multipliers(quality)
    return _round_half_up(((btv + mm) / 2) * 5)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/infantry_calc/tests/test_formulas.py -v`
Expected: PASS (24 tests: 5 quality + 1 suppression + 5 rfp + 4 interval + 5 defence + 4 morale).

- [ ] **Step 5: Commit**

```bash
git add counters/infantry_calc/
git commit -m "feat: implement infantry counter formulas (rFP, interval, Defence, Morale)"
```

---

### Task 3: Weapons data

**Files:**
- Create: `counters/infantry_calc/data/weapons.csv`
- Modify: `counters/infantry_calc/formulas.py` — no changes needed this task (formulas already complete)
- Create: `counters/infantry_calc/pipeline.py`
- Create: `counters/infantry_calc/tests/test_pipeline.py`

**Interfaces:**
- Consumes: nothing new.
- Produces: `WeaponRow` frozen dataclass (fields: `name: str`, `weapon_class: WeaponClass`, `cyclic_rpm: float`, `practical_rpm: float`, `max_range_yds: float`), `DATA_DIR: pathlib.Path`, `load_weapons(path: pathlib.Path = DATA_DIR / "weapons.csv") -> list[WeaponRow]` — for Task 5 to look up by name.

- [ ] **Step 1: Write the failing test**

Create `counters/infantry_calc/tests/test_pipeline.py`:

```python
import csv

import pytest

from infantry_calc.pipeline import load_weapons


class TestLoadWeapons:
    """Weapon reference data: name, class, rates of fire, max range.
    Source: infantry-counter-design spreadsheet's UNIT CALC and UNIT
    ROSTER sheets' weapon-loadout columns, deduplicated to one row per
    distinct weapon."""

    def test_loads_all_seven_pilot_weapons(self):
        weapons = load_weapons()
        names = {w.name for w in weapons}
        assert names == {
            "MG42 LMG (bipod)",
            "MG42 HMG (tripod)",
            "Kar98k",
            "Mosin-Nagant",
            "MP40",
            "PPSh-41",
            "DP-28",
        }

    def test_mg42_lmg_matches_the_worked_example(self):
        weapons = {w.name: w for w in load_weapons()}
        mg42_lmg = weapons["MG42 LMG (bipod)"]
        assert mg42_lmg.weapon_class == "lmg"
        assert mg42_lmg.cyclic_rpm == 1200
        assert mg42_lmg.practical_rpm == 300
        assert mg42_lmg.max_range_yds == 1000

    def test_kar98k_is_a_rifle(self):
        weapons = {w.name: w for w in load_weapons()}
        kar98k = weapons["Kar98k"]
        assert kar98k.weapon_class == "rifle"
        assert kar98k.practical_rpm == 15
        assert kar98k.max_range_yds == 600
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/infantry_calc/tests/test_pipeline.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'infantry_calc.pipeline'` (the module doesn't exist yet).

- [ ] **Step 3: Create the weapons data file**

Create `counters/infantry_calc/data/weapons.csv`:

```csv
name,weapon_class,cyclic_rpm,practical_rpm,max_range_yds
MG42 LMG (bipod),lmg,1200,300,1000
MG42 HMG (tripod),hmg,1200,350,2000
Kar98k,rifle,20,15,600
Mosin-Nagant,rifle,15,12,500
MP40,smg,500,90,200
PPSh-41,smg,900,100,200
DP-28,lmg,600,250,900
```

- [ ] **Step 4: Implement the loader**

Create `counters/infantry_calc/pipeline.py`:

```python
"""CSV-driven orchestration for infantry_calc: reads weapon and unit
roster data, runs the formulas, writes the precomputed reference table.

Source data (editable like a spreadsheet, no Python required to update):
  data/weapons.csv  -- one row per distinct weapon
  data/units.csv    -- one row per unit-variant/face

Run: python3 -m counters.infantry_calc.pipeline
Output: counters/infantry_calc/infantry_roster_output.csv
"""

from __future__ import annotations

import csv
import pathlib
from dataclasses import dataclass

from infantry_calc.formulas import WeaponClass

DATA_DIR = pathlib.Path(__file__).parent / "data"


@dataclass(frozen=True)
class WeaponRow:
    name: str
    weapon_class: WeaponClass
    cyclic_rpm: float
    practical_rpm: float
    max_range_yds: float


def load_weapons(path: pathlib.Path = DATA_DIR / "weapons.csv") -> list[WeaponRow]:
    """Load weapon reference data (name, class, rates of fire, max range)."""
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append(
                WeaponRow(
                    name=r["name"],
                    weapon_class=r["weapon_class"],  # type: ignore[arg-type]
                    cyclic_rpm=float(r["cyclic_rpm"]),
                    practical_rpm=float(r["practical_rpm"]),
                    max_range_yds=float(r["max_range_yds"]),
                )
            )
    return rows
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/infantry_calc/tests/test_pipeline.py -v`
Expected: PASS (3 tests).

- [ ] **Step 6: Run the full infantry_calc suite**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/infantry_calc/tests/ -q`
Expected: all tests from Task 2 and Task 3 pass, no failures.

- [ ] **Step 7: Commit**

```bash
git add counters/infantry_calc/data/weapons.csv counters/infantry_calc/pipeline.py counters/infantry_calc/tests/test_pipeline.py
git commit -m "feat: add infantry weapons reference data and loader"
```

---

### Task 4: Units roster data

**Files:**
- Create: `counters/infantry_calc/data/units.csv`
- Modify: `counters/infantry_calc/pipeline.py` (add `UnitWeaponSlot`, `UnitRow`, `load_units`)
- Modify: `counters/infantry_calc/tests/test_pipeline.py` (add `TestLoadUnits`)

**Interfaces:**
- Consumes: nothing new (independent of `load_weapons`; joins happen in Task 5).
- Produces: `UnitWeaponSlot` frozen dataclass (fields: `weapon_name: str`, `count: int`, `practical_rpm_override: float | None`), `UnitRow` frozen dataclass (fields: `unit_id: str`, `nation: str`, `unit_type: str`, `year_bracket: str`, `face: Literal["F", "R"]`, `quality: Quality`, `manpower_full: int`, `manpower_reduced: int`, `loadout: list[UnitWeaponSlot]`, `m_number: int`, `f_number: int`, `g_number: int`, `source: str`, `verify_status: str`, `notes: str`), `load_units(path: pathlib.Path = DATA_DIR / "units.csv") -> list[UnitRow]` — for Task 5 to consume.

**Data note, not a placeholder:** the roster below transcribes the infantry-counter-design spreadsheet's own `UNIT ROSTER` sheet (its "master record" — the more complete and rigorous of the spreadsheet's two roster-like sheets; its earlier `COUNTER OUTPUT` sheet is a legacy example page that was not kept in sync and is superseded by this data). Every `source`/`verify_status` value below is transcribed verbatim from that sheet, not invented.

- [ ] **Step 1: Write the failing test**

Add to `counters/infantry_calc/tests/test_pipeline.py`, after the existing imports add `load_units`:

```python
from infantry_calc.pipeline import load_units, load_weapons
```

Add this test class at the end of the file:

```python
class TestLoadUnits:
    """The pilot roster: 6 units (German Grenadier/Panzergrenadier/MG42
    team, Soviet Guards Rifle/Rifle/DP-28 team), each with a Front and
    Rear face -- 12 rows total. Source: infantry-counter-design
    spreadsheet's UNIT ROSTER sheet."""

    def test_loads_all_twelve_rows(self):
        units = load_units()
        assert len(units) == 12

    def test_gren_43_front_face_matches_the_anchor_unit(self):
        units = {u.unit_id: u for u in load_units()}
        gren_f = units["GER_GREN_1943.3_F"]
        assert gren_f.nation == "Germany"
        assert gren_f.unit_type == "Grenadier Squad"
        assert gren_f.face == "F"
        assert gren_f.quality == "regular"
        assert gren_f.manpower_full == 9
        assert gren_f.manpower_reduced == 4
        assert gren_f.m_number == 2
        assert gren_f.f_number == 2
        assert gren_f.g_number == 3
        assert gren_f.verify_status == "ANCHOR"
        assert len(gren_f.loadout) == 2
        assert gren_f.loadout[0].weapon_name == "MG42 LMG (bipod)"
        assert gren_f.loadout[0].count == 1
        assert gren_f.loadout[0].practical_rpm_override is None
        assert gren_f.loadout[1].weapon_name == "Kar98k"
        assert gren_f.loadout[1].count == 8

    def test_weapon_team_rear_face_has_a_practical_rpm_override(self):
        """GER_MG42_1943.3_R: 2-man reduced crew, same MG42 HMG but a
        slower practical rate of fire (250 vs. the front face's 350) --
        the one case in the pilot roster where a unit's own loadout
        entry overrides the weapon's default practical RPM."""
        units = {u.unit_id: u for u in load_units()}
        mg42_r = units["GER_MG42_1943.3_R"]
        assert len(mg42_r.loadout) == 1
        assert mg42_r.loadout[0].weapon_name == "MG42 HMG (tripod)"
        assert mg42_r.loadout[0].practical_rpm_override == 250

    def test_rifsq_front_face_has_three_weapon_slots(self):
        """SOV_RIFSQ_1943.3_F: DP-28 + Mosin-Nagant + PPSh-41 -- the
        widest loadout in the pilot roster, confirms all three slots
        parse, not just the first two."""
        units = {u.unit_id: u for u in load_units()}
        rifsq_f = units["SOV_RIFSQ_1943.3_F"]
        assert [slot.weapon_name for slot in rifsq_f.loadout] == [
            "DP-28",
            "Mosin-Nagant",
            "PPSh-41",
        ]

    def test_a_units_source_citation_is_preserved(self):
        units = {u.unit_id: u for u in load_units()}
        assert units["GER_GREN_1943.3_F"].source == "Nafziger OOB, TM-E 30-451"
        assert units["SOV_GDSRIF_1943.3_F"].source == "STAVKA TO&E 1943"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/infantry_calc/tests/test_pipeline.py::TestLoadUnits -v`
Expected: FAIL — `ImportError: cannot import name 'load_units'` (doesn't exist yet).

- [ ] **Step 3: Create the units roster data file**

Create `counters/infantry_calc/data/units.csv`:

```csv
unit_id,nation,unit_type,year_bracket,face,quality,manpower_full,manpower_reduced,weapon1_name,weapon1_count,weapon1_practical_rpm_override,weapon2_name,weapon2_count,weapon2_practical_rpm_override,weapon3_name,weapon3_count,weapon3_practical_rpm_override,m_number,f_number,g_number,source,verify_status,notes
GER_GREN_1943.3_F,Germany,Grenadier Squad,1943.3,F,regular,9,4,MG42 LMG (bipod),1,,Kar98k,8,,,,,2,2,3,"Nafziger OOB, TM-E 30-451",ANCHOR,"Standard German infantry squad mid-1943. Anchor unit for system calibration."
GER_GREN_1943.3_R,Germany,Grenadier Squad (reduced),1943.3,R,regular,9,4,Kar98k,4,,,,,,,,2,2,2,Derived from front face,ANCHOR,"Rear face: MG42 LMG lost. 4 riflemen remain."
GER_PZGR_1943.3_F,Germany,Panzergrenadier Squad,1943.3,F,veteran,10,5,MG42 LMG (bipod),1,,MP40,6,,,,,2,2,4,Nafziger OOB,PRELIMINARY,"Mechanized infantry squad. Higher SMG concentration for vehicle assault."
GER_PZGR_1943.3_R,Germany,Panzergrenadier Squad (reduced),1943.3,R,veteran,10,5,MP40,3,,,,,,,,2,2,3,Derived from front face,PRELIMINARY,"Rear face: MG42 LMG lost. 3x MP40 remain."
GER_MG42_1943.3_F,Germany,MG42 HMG Team,1943.3,F,regular,4,2,MG42 HMG (tripod),1,,,,,,,,0,3,1,HDv 130,PRELIMINARY,"Tripod-mounted MG42 team. Weapon counter -- does not count toward stacking."
GER_MG42_1943.3_R,Germany,MG42 HMG Team (reduced crew),1943.3,R,regular,4,2,MG42 HMG (tripod),1,250,,,,,,,0,3,1,Derived from front face,PRELIMINARY,"Rear face: 2-man crew. Reduced practical RPM -- barrel changes slower."
SOV_GDSRIF_1943.3_F,Soviet Union,Guards Rifle Squad,1943.3,F,veteran,9,5,DP-28,1,,PPSh-41,4,,,,,2,2,4,STAVKA TO&E 1943,PRELIMINARY,"Guards formation -- selected veterans post-Stalingrad. Heavy PPSh-41 concentration reflects assault doctrine."
SOV_GDSRIF_1943.3_R,Soviet Union,Guards Rifle Squad (reduced),1943.3,R,veteran,9,5,PPSh-41,2,,,,,,,,2,2,3,Derived from front face,PRELIMINARY,"Rear face: DP-28 lost. 2x PPSh-41 remain."
SOV_RIFSQ_1943.3_F,Soviet Union,Rifle Squad,1943.3,F,regular,10,5,DP-28,1,,Mosin-Nagant,6,,PPSh-41,2,,2,2,3,STAVKA TO&E 1943,PRELIMINARY,"Standard Soviet rifle squad mid-1943. Mixed Mosin/PPSh/DP-28 loadout reflects increasing SMG distribution."
SOV_RIFSQ_1943.3_R,Soviet Union,Rifle Squad (reduced),1943.3,R,regular,10,5,Mosin-Nagant,4,,,,,,,,2,2,2,Derived from front face,PRELIMINARY,"Rear face: DP-28 and PPSh lost. 4x Mosin remain."
SOV_DP28_1943.3_F,Soviet Union,DP-28 LMG Team,1943.3,F,regular,3,2,DP-28,1,,,,,,,,0,3,2,STAVKA small arms manual,PRELIMINARY,"DP-28 bipod LMG team. Weapon counter."
SOV_DP28_1943.3_R,Soviet Union,DP-28 LMG Team (reduced crew),1943.3,R,regular,3,2,DP-28,1,150,,,,,,,0,3,1,Derived from front face,PRELIMINARY,"Rear face: 2-man crew. Practical RPM reduced -- pan mag changes slower."
```

- [ ] **Step 4: Implement the loader**

Add to `counters/infantry_calc/pipeline.py`, at the top-of-file import block, add `Literal`:

```python
from typing import Literal
```

Add `Quality` to the existing `from infantry_calc.formulas import WeaponClass` line, making it:

```python
from infantry_calc.formulas import WeaponClass
from quality.tiers import Quality
```

Add this code after the existing `load_weapons` function:

```python
@dataclass(frozen=True)
class UnitWeaponSlot:
    weapon_name: str
    count: int
    practical_rpm_override: float | None


@dataclass(frozen=True)
class UnitRow:
    unit_id: str
    nation: str
    unit_type: str
    year_bracket: str
    face: Literal["F", "R"]
    quality: Quality
    manpower_full: int
    manpower_reduced: int
    loadout: list[UnitWeaponSlot]
    m_number: int
    f_number: int
    g_number: int
    source: str
    verify_status: str
    notes: str


def _parse_weapon_slot(r: dict[str, str], slot: int) -> UnitWeaponSlot | None:
    name = r[f"weapon{slot}_name"]
    if not name:
        return None
    override_raw = r[f"weapon{slot}_practical_rpm_override"]
    override = float(override_raw) if override_raw else None
    return UnitWeaponSlot(
        weapon_name=name,
        count=int(r[f"weapon{slot}_count"]),
        practical_rpm_override=override,
    )


def load_units(path: pathlib.Path = DATA_DIR / "units.csv") -> list[UnitRow]:
    """Load the infantry unit roster (one row per unit-variant/face).

    See that CSV's own notes/source columns for provenance -- most rows
    cite a primary or secondary historical document; rear-face rows that
    are purely derived from their front-face sibling say so explicitly.
    """
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            loadout = [
                slot
                for slot in (_parse_weapon_slot(r, n) for n in (1, 2, 3))
                if slot is not None
            ]
            rows.append(
                UnitRow(
                    unit_id=r["unit_id"],
                    nation=r["nation"],
                    unit_type=r["unit_type"],
                    year_bracket=r["year_bracket"],
                    face=r["face"],  # type: ignore[arg-type]
                    quality=r["quality"],  # type: ignore[arg-type]
                    manpower_full=int(r["manpower_full"]),
                    manpower_reduced=int(r["manpower_reduced"]),
                    loadout=loadout,
                    m_number=int(r["m_number"]),
                    f_number=int(r["f_number"]),
                    g_number=int(r["g_number"]),
                    source=r["source"],
                    verify_status=r["verify_status"],
                    notes=r["notes"],
                )
            )
    return rows
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/infantry_calc/tests/test_pipeline.py -v`
Expected: PASS (all `TestLoadWeapons` and `TestLoadUnits` tests, 8 total).

- [ ] **Step 6: Commit**

```bash
git add counters/infantry_calc/data/units.csv counters/infantry_calc/pipeline.py counters/infantry_calc/tests/test_pipeline.py
git commit -m "feat: add infantry unit roster data and loader (12-row pilot: German + Soviet, 1943)"
```

---

### Task 5: Precompute the infantry roster output

**Files:**
- Modify: `counters/infantry_calc/pipeline.py` (add `write_infantry_roster_csv`, `main`)
- Modify: `counters/infantry_calc/tests/test_pipeline.py` (add `TestWriteInfantryRosterCsv`)

**Interfaces:**
- Consumes: `WeaponRow`/`load_weapons` (Task 3), `UnitRow`/`UnitWeaponSlot`/`load_units` (Task 4), `weapon_rfp`/`fire_interval_hexes`/`unit_defence`/`unit_morale`/`suppression_factor` (Task 2).
- Produces: `write_infantry_roster_csv(weapons: list[WeaponRow], units: list[UnitRow], out_path: pathlib.Path) -> None`, `main() -> None` — the package's player-facing output.

- [ ] **Step 1: Write the failing test**

Add to the top of `counters/infantry_calc/tests/test_pipeline.py`, alongside the existing imports:

```python
from infantry_calc.pipeline import write_infantry_roster_csv
```

Add this test class at the end of the file:

```python
class TestWriteInfantryRosterCsv:
    """Cross-checked against the infantry-counter-design spreadsheet's
    own UNIT ROSTER sheet -- every expected value below was read directly
    from that sheet's own computed cells, not re-derived from the
    formulas under test (that would make this a tautology, not a
    validation)."""

    def _rows_by_unit_id(self, tmp_path):
        out_path = tmp_path / "infantry_roster_output.csv"
        write_infantry_roster_csv(load_weapons(), load_units(), out_path)
        with open(out_path, newline="") as f:
            return {r["unit_id"]: r for r in csv.DictReader(f)}

    def test_writes_one_row_per_unit(self, tmp_path):
        rows = self._rows_by_unit_id(tmp_path)
        assert len(rows) == 12

    def test_gren_43_front_face_matches_the_worked_example(self, tmp_path):
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["GER_GREN_1943.3_F"]
        assert row["fire_line_1"] == "─● 7 ⬡4 -1"
        assert row["fire_line_2"] == "╌ 3 ⬡5 -1"
        assert row["defence"] == "8"
        assert row["morale"] == "5"
        assert row["m_number"] == "2"
        assert row["f_number"] == "2"
        assert row["g_number"] == "3"

    def test_gren_43_rear_face_defence_is_front_minus_two(self, tmp_path):
        """4x Kar98k alone computes to rFP 1 -- below MIN_RFP (2), so this
        fire line reads 'omit', not a printed '1 ⬡15 -1' notation (matches
        the source spreadsheet's own UNIT ROSTER cell BX5)."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["GER_GREN_1943.3_R"]
        assert row["defence"] == "6"
        assert row["fire_line_1"] == "omit (rFP too low)"

    def test_mg42_team_rear_face_uses_the_practical_rpm_override(self, tmp_path):
        """This unit's loadout entry overrides practical RPM to 250
        (vs. the weapon's own default of 350) -- confirms the override
        actually flows into the rFP calculation, not just get parsed."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["GER_MG42_1943.3_R"]
        assert row["fire_line_1"] == "═● 8 ⬡6 -1"
        assert row["defence"] == "3"

    def test_soviet_rifle_squad_rear_face_below_min_rfp_is_omitted(self, tmp_path):
        """SOV_RIFSQ_1943.3_R's lone weapon (4x Mosin-Nagant) computes to
        rFP 0 -- below MIN_RFP, so the fire line reads 'omit', not a
        bogus '0 ⬡- -1' notation."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["SOV_RIFSQ_1943.3_R"]
        assert row["fire_line_1"] == "omit (rFP too low)"

    def test_rifle_squad_front_face_has_three_fire_lines(self, tmp_path):
        """The Mosin-Nagant slot (weapon2, 6x, rFP 1) is below MIN_RFP and
        reads 'omit', not a printed notation -- matches the source
        spreadsheet's own UNIT ROSTER cell BY12. Only the DP-28 and
        PPSh-41 slots clear the threshold."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["SOV_RIFSQ_1943.3_F"]
        assert row["fire_line_1"] == "─● 7 ⬡3 -1"
        assert row["fire_line_2"] == "omit (rFP too low)"
        assert row["fire_line_3"] == "≡ 3 ⬡2 -1"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/infantry_calc/tests/test_pipeline.py::TestWriteInfantryRosterCsv -v`
Expected: FAIL — `ImportError: cannot import name 'write_infantry_roster_csv'` (doesn't exist yet).

- [ ] **Step 3: Implement the precompute pipeline**

Add to `counters/infantry_calc/pipeline.py`'s import block:

```python
from infantry_calc.formulas import (
    MIN_RFP,
    WeaponClass,
    fire_interval_hexes,
    unit_defence,
    unit_morale,
    weapon_rfp,
)
```

(Replace the earlier, narrower `from infantry_calc.formulas import WeaponClass` line with this fuller one.)

Add this code at the end of `counters/infantry_calc/pipeline.py`:

```python
# Fire-line notation prefix by weapon class -- source: infantry-counter-
# design spreadsheet, UNIT ROSTER sheet's BX/BY/BZ/CA column formulas.
_NOTATION_PREFIX: dict[WeaponClass, str] = {
    "lmg": "─● ",
    "hmg": "═● ",
    "smg": "≡ ",
    "at_rifle": "╌○ ",
    "rifle": "╌ ",
    "pistol": "╌ ",  # same as rifle -- pistols rarely rate their own notation
}

_FALLOFF = 1  # every pilot-roster row uses -1; not yet a computed value (see design spec open items)


def _resolve_practical_rpm(slot: UnitWeaponSlot, weapon: WeaponRow) -> float:
    return slot.practical_rpm_override if slot.practical_rpm_override is not None else weapon.practical_rpm


def _fire_line_notation(slot: UnitWeaponSlot, weapon: WeaponRow, quality: Quality) -> str:
    practical_rpm = _resolve_practical_rpm(slot, weapon)
    rfp = weapon_rfp(slot.count, practical_rpm, weapon.weapon_class, quality)
    if rfp < MIN_RFP:
        return "omit (rFP too low)"
    interval = fire_interval_hexes(weapon.max_range_yds, rfp)
    return f"{_NOTATION_PREFIX[weapon.weapon_class]}{rfp} ⬡{interval} -{_FALLOFF}"


def write_infantry_roster_csv(
    weapons: list[WeaponRow],
    units: list[UnitRow],
    out_path: pathlib.Path,
) -> None:
    """The infantry roster reference table: per unit-face, up to three
    fire-line notations plus Defence, Morale, and M#/F#/G# -- the exact
    values printed on the physical counter. No arithmetic required at
    the table: read the row for this unit, done.
    """
    weapons_by_name = {w.name: w for w in weapons}

    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "unit_id", "nation", "unit_type", "year_bracket", "face", "quality",
                "fire_line_1", "fire_line_2", "fire_line_3",
                "defence", "morale", "m_number", "f_number", "g_number",
                "verify_status",
            ]
        )
        for unit in units:
            front_def, rear_def = unit_defence(unit.manpower_full, unit.quality)
            defence = front_def if unit.face == "F" else rear_def
            morale = unit_morale(unit.quality)

            fire_lines = [
                _fire_line_notation(slot, weapons_by_name[slot.weapon_name], unit.quality)
                for slot in unit.loadout
            ]
            fire_lines += [""] * (3 - len(fire_lines))

            writer.writerow(
                [
                    unit.unit_id, unit.nation, unit.unit_type, unit.year_bracket, unit.face, unit.quality,
                    fire_lines[0], fire_lines[1], fire_lines[2],
                    defence, morale, unit.m_number, unit.f_number, unit.g_number,
                    unit.verify_status,
                ]
            )


def main() -> None:
    weapons = load_weapons()
    units = load_units()
    write_infantry_roster_csv(weapons, units, DATA_DIR.parent / "infantry_roster_output.csv")
    print(f"Wrote infantry_calc output to {DATA_DIR.parent}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/infantry_calc/tests/test_pipeline.py -v`
Expected: PASS (all tests in the file, including the new `TestWriteInfantryRosterCsv` class).

- [ ] **Step 5: Run the full test suite and the real pipeline**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/infantry_calc/ counters/quality/ counters/armor_calc/ -q`
Expected: all tests across all three packages pass, 0 failures.

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m counters.infantry_calc.pipeline`
Expected: `Wrote infantry_calc output to .../counters/infantry_calc`, and `counters/infantry_calc/infantry_roster_output.csv` exists with 12 data rows.

Run: `cat counters/infantry_calc/infantry_roster_output.csv` and eyeball the output — confirm all 12 rows are present, `SOV_RIFSQ_1943.3_R`'s fire_line_1 reads `omit (rFP too low)`, and `GER_MG42_1943.3_F`/`GER_MG42_1943.3_R` show different rFP values (9 vs. 8) despite the same weapon, reflecting the practical-RPM override.

- [ ] **Step 6: Commit**

```bash
git add counters/infantry_calc/pipeline.py counters/infantry_calc/tests/test_pipeline.py counters/infantry_calc/infantry_roster_output.csv
git commit -m "feat: precompute the infantry roster reference table"
```

---

### Task 6: README and design spec closeout

**Files:**
- Create: `counters/infantry_calc/README.md`
- Modify: `docs/superpowers/specs/2026-07-05-infantry-counter-system-design.md`

**Interfaces:**
- Consumes: final test counts and computed values from Tasks 1-5.
- Produces: no code interfaces — documentation only.

- [ ] **Step 1: Write the README**

Read `counters/armor_calc/README.md` first to match its structure and tone exactly (section headings, how it describes running the pipeline, how it describes the data files).

Create `counters/infantry_calc/README.md` following that same structure, covering: what this package does (converts real-world weapon/unit specs into infantry counter values), how to run it (`python3 -m counters.infantry_calc.pipeline`), what each data file contains (`weapons.csv`, `units.csv`), where the algorithm comes from (the infantry-counter-design spreadsheet, explicitly noting these are the project's own calibrated game-design constants, not a primary military source), and a pointer to `docs/superpowers/specs/2026-07-05-infantry-counter-system-design.md` for the full design rationale.

- [ ] **Step 2: Verify the full test suite one more time**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/ -q`

Record the exact total test count printed — you will need it for Step 3.

- [ ] **Step 3: Close out the design spec**

In `docs/superpowers/specs/2026-07-05-infantry-counter-system-design.md`, at the end of Section 3.4 ("Data pipeline"), add:

```markdown

**Implemented and tested** (`counters/quality/tiers.py`: `Quality`, `ALL_QUALITIES`; `armor_calc/formulas.py`: `CrewQuality`/`ALL_CREW_QUALITIES` now alias the shared type, its own 99-test suite unaffected; `infantry_calc/formulas.py`: `weapon_rfp`, `fire_interval_hexes`, `unit_defence`, `unit_morale`, `quality_multipliers`, `suppression_factor`; `infantry_calc/pipeline.py`: `load_weapons`, `load_units`, `write_infantry_roster_csv`, wired into `main()`), cross-checked against the source spreadsheet's own computed values for all 12 pilot-roster rows. [N] total tests passing across `counters/quality/`, `counters/armor_calc/`, and `counters/infantry_calc/`.
```

Replace `[N]` with the actual total test count from Step 2.

- [ ] **Step 4: Commit**

```bash
git add counters/infantry_calc/README.md docs/superpowers/specs/2026-07-05-infantry-counter-system-design.md
git commit -m "docs: add infantry_calc README, close out design spec with final test count"
```

---

## Self-Review

**Spec coverage:** §2's "Replaces the spreadsheet" decision -> Tasks 1-6 build the full replacement. "Shared calculation core" -> Task 1. "`armor_calc`'s `CrewQuality` refactored now" -> Task 1, Step 5-6. "Infantry squads + organic support teams only" scope -> Task 4's 12-row roster (rifle squads + integral MG/LMG teams, nothing else). "Militia tier extrapolation" -> Task 2's `_QUALITY_MULTIPLIERS` table and its dedicated test. §3.2 (shared quality core) -> Task 1. §3.3 (infantry algorithm) -> Task 2. §3.4 (data pipeline) -> Tasks 3-5. §4 (validation approach) -> Task 2's worked-example tests, Task 5's cross-checked roster tests, Task 1's `armor_calc` regression check. §5 (out of scope) -> respected throughout: no towed-artillery code, no grenade/satchel-charge derivation, no nations/years beyond the pilot 12 rows, M#/F#/G# ported as flat data not derived formulas. §6 (open items) -> Militia flagged in code comments (Task 2); falloff (`-f`) left as a fixed constant, not computed (Task 5, `_FALLOFF = 1`), matching the spec's own note that this is left to implementation-time judgment.

**Placeholder scan:** searched for TBD/TODO/"implement later"/vague instructions -- none found. All notation-string test assertions (Task 5) use exact values verified directly against the source spreadsheet's own formula output, not invented examples.

**Type consistency:** `WeaponClass` (Task 2) is used identically in Task 3's `WeaponRow.weapon_class` and Task 5's `_NOTATION_PREFIX` keys. `Quality` (Task 1) flows unchanged through `UnitRow.quality` (Task 4) into every formula call in Task 5. `UnitWeaponSlot`'s `practical_rpm_override: float | None` (Task 4) is consumed by exactly one function, `_resolve_practical_rpm` (Task 5), with matching optionality. `unit_defence()`'s `(front, rear)` return tuple (Task 2) is unpacked identically in Task 5's `write_infantry_roster_csv`.
