# Hit Location and Crew Position System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the current free "owning player chooses MOB kill vs. GUN kill" narrative judgment call (Rule 17.1.1) with a real, sourced determination — implement Bird & Livingston Appendix 15's shot-scatter mathematics, apply it to real per-vehicle zone geometry for two pilot vehicles (Tiger I, Sherman M4A1), and wire the result into a single new die roll at the point a Casualty result occurs.

**Architecture:** Design-time Monte Carlo precomputation, same pattern as every other mechanic built this session (Gunnery Roll, Shatter Gap, HEAT reference table): real sourced formulas + real per-vehicle data → small precomputed player-facing table → one roll at the table, zero arithmetic. Appendix 15's closed-form displacement equations (not its raw dice table) get validated against the book's own worked examples first, then combined with Monte-Carlo-sampled zone geometry to produce a Mobility/Gun/Neither percentage split per (vehicle, profile, range band, crew quality), converted to dice-roll thresholds using the same 1d6+1d8+1d12 machinery already built for the Gunnery Roll.

**Tech Stack:** Python 3.10+, numpy, pytest, CSV-driven data (matching `counters/armor_calc/`'s existing architecture), Sphinx/RST for the rulebook.

## Global Constraints

- Every formula must cite its source (chapter/page) and be validated against a real worked example before being trusted with new data — no untested formulas ship.
- Vehicle-specific data (zone geometry) not backed by either project source (Bird & Livingston, John D. Salt's compilation) must be flagged in its own CSV notes field as general historical knowledge, not silently presented as equally certain to cited data.
- No new arithmetic at the table: every player-facing artifact is a single die roll against a printed threshold, same as the Gunnery Table and Shatter Gap Table.
- Follow the existing package structure exactly: formulas go in `counters/armor_calc/formulas.py`, orchestration in `counters/armor_calc/pipeline.py`, source data in `counters/armor_calc/data/*.csv`, tests in `counters/armor_calc/tests/test_formulas.py` and `test_pipeline.py`.
- A correction to the design spec: `docs/superpowers/specs/2026-07-04-hit-location-and-crew-position-design.md` cites the existing free-choice rule as "Rule 18.7.1" — it is actually **Rule 17.1.1** (confirmed directly against `docs/source/section_17__vehicles_counter_design_and_movement.rst:62`). Task 8 corrects this.

---

### Task 1: Appendix 15 displacement formula

**Files:**
- Modify: `counters/armor_calc/formulas.py` (add new functions near the end, after `layered_plate_effective_thickness`)
- Test: `counters/armor_calc/tests/test_formulas.py` (add new test class)

**Interfaces:**
- Produces: `shot_displacement_m(dice_score: float, hit_pct: float) -> float` — displacement in metres along one axis, for later tasks to call twice per sample (once for vertical, once for lateral).

- [ ] **Step 1: Write the failing tests**

Add to `counters/armor_calc/tests/test_formulas.py`, in the import block at the top, add `shot_displacement_m` to the existing `from armor_calc.formulas import (...)` list (alphabetical position, after `rounded_mantlet_angle_distribution` and before `shatter_gap_failure`).

Then add this test class (place it after `class TestLayeredPlateInContact:` and before `class TestPartialFaceHardening:`):

```python
class TestShotDisplacement:
    """Appendix 15 p.117-118: dice score + hit% -> displacement in metres
    along one axis. Validated against the chapter's own worked examples
    before being trusted with new zone-geometry data."""

    def test_matches_worked_example_85pct_dice66(self):
        """'Assume hit score against 2m x 2m target is 85 vertical, and
        corresponding dice score for vertical shot placement is 66... The
        ratio of the dice and hit scores equals 0.948/1.38, or 0.7m.'"""
        displacement = shot_displacement_m(dice_score=66.0, hit_pct=85.0)
        assert displacement == pytest.approx(0.7, abs=0.05)

    def test_matches_worked_example_95pct_dice22(self):
        """'For 95% accuracy and a roll of 22... shot placement is 0.2m
        above aim point' (vertical axis)."""
        displacement = shot_displacement_m(dice_score=22.0, hit_pct=95.0)
        assert displacement == pytest.approx(0.2, abs=0.05)

    def test_matches_worked_example_95pct_dice50(self):
        """Same worked example, lateral axis: 'roll of 50... results in a
        shot placement 0.4m left of aim point.'"""
        displacement = shot_displacement_m(dice_score=50.0, hit_pct=95.0)
        assert displacement == pytest.approx(0.4, abs=0.05)

    def test_higher_dice_score_means_larger_displacement(self):
        """A higher percentile roll is further from the aim point --
        monotonicity check independent of the exact worked-example
        tolerances above."""
        small = shot_displacement_m(dice_score=10.0, hit_pct=85.0)
        large = shot_displacement_m(dice_score=90.0, hit_pct=85.0)
        assert large > small

    def test_higher_hit_pct_means_tighter_dispersion(self):
        """A higher overall hit% implies tighter shot bunching -- the same
        dice score should produce a SMALLER displacement at higher hit%."""
        tight = shot_displacement_m(dice_score=50.0, hit_pct=95.0)
        loose = shot_displacement_m(dice_score=50.0, hit_pct=20.0)
        assert tight < loose
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m pytest counters/armor_calc/tests/test_formulas.py::TestShotDisplacement -v`
Expected: FAIL with `ImportError` or `NameError` — `shot_displacement_m` does not exist yet.

- [ ] **Step 3: Implement the formula**

Add to `counters/armor_calc/formulas.py`, after the `layered_plate_effective_thickness` function (search for `return max(floor, min(raw, ceiling))` to find the end of that function):

```python
def _appendix15_a_value(score: float) -> float:
    """The "A" value from Appendix 15's shot-placement equations.

    Source: Bird & Livingston Appendix 15, p.117. Two different meanings
    depending on what "score" represents (the equations are identical,
    only the interpretation differs): fed a percentile dice score (0-99),
    it is "the number of standard deviations that the shot varies by,
    assuming a normal distribution." Fed a hit percentage (0-100) instead,
    it is "the inverse of the standard deviation for the hit probability
    against a 2m target distance."
    """
    if score <= 80:
        return math.exp(-22.7614) * math.exp(18.416 * score**0.05)
    return math.exp(0.193090) * math.exp(2.665e-21 * score**10.25)


def shot_displacement_m(dice_score: float, hit_pct: float) -> float:
    """Displacement (metres, unsigned magnitude) from the aim point along
    one axis (vertical or lateral), given a percentile dice score (0-99)
    and the hit percentage along that same axis against a 2m x 2m
    reference target.

    Source: Bird & Livingston Appendix 15, p.117-118. "Divide 'A' figure
    for dice score by 'A' figure for step 1 hit score to determine shot
    placement relative to aim location." Validated against the chapter's
    own three worked examples (0.7m @ 85%/dice66, 0.2m @ 95%/dice22, 0.4m
    @ 95%/dice50) -- see test_formulas.py::TestShotDisplacement.

    Args:
        dice_score: A percentile roll, 0-99 (or 0-100; the source's own
            "00 means 100" convention for its raw dice table does not
            apply here since this is the closed-form equation, not the
            table).
        hit_pct: The hit percentage (0-100) along this axis against a 2m
            reference target -- from vertical_lateral_hit_pct(), not the
            shot's raw overall hit%.

    Returns:
        Displacement magnitude in metres. Caller applies a random sign
        (direction) separately -- this function is direction-agnostic.
    """
    dice_a = _appendix15_a_value(dice_score)
    hit_a = _appendix15_a_value(hit_pct)
    return dice_a / hit_a
```

Add `import math` to the top of `formulas.py` if not already present (check the existing import block first — the file currently imports `numpy as np` but may not import the standard library `math` module).

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest counters/armor_calc/tests/test_formulas.py::TestShotDisplacement -v`
Expected: PASS (5 tests). If the worked-example tests fail outside the `abs=0.05` tolerance, do not adjust the tolerance to force a pass — first re-check the four constants (`-22.7614`, `18.416`, `0.193090`, `2.665e-21`) against the source image at `pdf_pages/pg-... ` (Appendix 15, printed p.117-118) for a transcription error, since the exponents involved are large enough that a small constant error produces a large displacement error.

- [ ] **Step 5: Run the full test suite to confirm no regressions**

Run: `python3 -m pytest counters/armor_calc/tests/ -q`
Expected: all previously-passing tests still pass, plus the 5 new ones (80 + 5 = 85 total, assuming no other changes since the last session checkpoint).

- [ ] **Step 6: Commit**

```bash
git add counters/armor_calc/formulas.py counters/armor_calc/tests/test_formulas.py
git commit -m "feat: implement Appendix 15 shot-displacement formula, validated against 3 worked examples"
```

---

### Task 2: Table 1 hit%-split lookup

**Files:**
- Modify: `counters/armor_calc/formulas.py`
- Test: `counters/armor_calc/tests/test_formulas.py`

**Interfaces:**
- Consumes: nothing from Task 1 (independent formula).
- Produces: `vertical_lateral_hit_pct(overall_hit_pct: float) -> tuple[float, float]` — `(vertical_hit_pct, lateral_hit_pct)`, for Task 3 to call once per shot.

- [ ] **Step 1: Write the failing tests**

Add `vertical_lateral_hit_pct` to the `test_formulas.py` import list (alphabetical position, after `slope_multiplier` and before... check exact alphabetical placement against the existing list).

Add this test class after `TestShotDisplacement`:

```python
class TestVerticalLateralHitPct:
    """Appendix 15's Table 1, 'Simplified Hit Probability Breakdown,
    Stationary Target' -- splits an overall hit% into separate vertical
    and lateral hit% against a 2m x 2m reference target."""

    def test_matches_table_exactly_at_listed_rows(self):
        """Spot-check several of the 19 listed rows directly, no
        interpolation involved."""
        assert vertical_lateral_hit_pct(95.0) == (95.0, 98.0)
        assert vertical_lateral_hit_pct(50.0) == (65.0, 80.0)
        assert vertical_lateral_hit_pct(5.0) == (15.0, 35.0)

    def test_interpolates_between_listed_rows(self):
        """62.5 sits exactly halfway between the table's 60 and 65 rows
        (60 -> vertical 70/lateral 85; 65 -> vertical 70/lateral 90) --
        vertical is flat across this interval so must return exactly 70,
        lateral must land exactly halfway at 87.5."""
        vertical, lateral = vertical_lateral_hit_pct(62.5)
        assert vertical == pytest.approx(70.0)
        assert lateral == pytest.approx(87.5)

    def test_clamps_below_lowest_listed_value(self):
        """The table only goes down to 5% overall hit -- below that,
        clamp to the lowest row rather than extrapolating or erroring."""
        assert vertical_lateral_hit_pct(1.0) == vertical_lateral_hit_pct(5.0)

    def test_clamps_above_highest_listed_value(self):
        """The table only goes up to 95% overall hit."""
        assert vertical_lateral_hit_pct(99.0) == vertical_lateral_hit_pct(95.0)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest counters/armor_calc/tests/test_formulas.py::TestVerticalLateralHitPct -v`
Expected: FAIL — `vertical_lateral_hit_pct` does not exist yet.

- [ ] **Step 3: Implement the lookup table**

Add to `counters/armor_calc/formulas.py`, directly after `shot_displacement_m`:

```python
# Appendix 15's "SIMPLIFIED HIT PROBABILITY BREAKDOWN, STATIONARY TARGET"
# table (p.116-117), transcribed in ascending order for interpolation.
# (overall_hit_pct, lateral_hit_pct, vertical_hit_pct)
_HIT_PCT_BREAKDOWN: list[tuple[float, float, float]] = [
    (5, 35, 15), (10, 40, 25), (15, 45, 35), (20, 50, 40), (25, 55, 45),
    (30, 60, 50), (35, 65, 55), (40, 70, 55), (45, 75, 60), (50, 80, 65),
    (55, 85, 65), (60, 85, 70), (65, 90, 70), (70, 95, 75), (75, 95, 80),
    (80, 95, 85), (85, 98, 85), (90, 98, 90), (95, 98, 95),
]


def vertical_lateral_hit_pct(overall_hit_pct: float) -> tuple[float, float]:
    """Split an overall hit percentage into separate vertical and lateral
    hit percentages against a 2m x 2m reference target.

    Source: Bird & Livingston Appendix 15 p.116-117, "Simplified Hit
    Probability Breakdown, Stationary Target" table. Linearly interpolated
    between the table's 19 listed rows; clamped at both ends (the table
    only covers 5-95% overall hit).

    Args:
        overall_hit_pct: Overall hit probability, 0-100.

    Returns:
        (vertical_hit_pct, lateral_hit_pct).
    """
    x = min(max(overall_hit_pct, _HIT_PCT_BREAKDOWN[0][0]), _HIT_PCT_BREAKDOWN[-1][0])
    for (x0, lat0, vert0), (x1, lat1, vert1) in zip(_HIT_PCT_BREAKDOWN, _HIT_PCT_BREAKDOWN[1:]):
        if x0 <= x <= x1:
            frac = 0.0 if x1 == x0 else (x - x0) / (x1 - x0)
            vertical = vert0 + frac * (vert1 - vert0)
            lateral = lat0 + frac * (lat1 - lat0)
            return vertical, lateral
    # Unreachable given the clamp above, but keeps the type checker honest.
    return _HIT_PCT_BREAKDOWN[-1][2], _HIT_PCT_BREAKDOWN[-1][1]  # pragma: no cover
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest counters/armor_calc/tests/test_formulas.py::TestVerticalLateralHitPct -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Run the full test suite**

Run: `python3 -m pytest counters/armor_calc/tests/ -q`
Expected: 89 passed (85 + 4).

- [ ] **Step 6: Commit**

```bash
git add counters/armor_calc/formulas.py counters/armor_calc/tests/test_formulas.py
git commit -m "feat: digitize Appendix 15's vertical/lateral hit-percentage breakdown table"
```

---

### Task 3: HitZone geometry type and Monte Carlo classification

**Files:**
- Modify: `counters/armor_calc/formulas.py`
- Test: `counters/armor_calc/tests/test_formulas.py`

**Interfaces:**
- Consumes: `shot_displacement_m(dice_score: float, hit_pct: float) -> float` (Task 1), `vertical_lateral_hit_pct(overall_hit_pct: float) -> tuple[float, float]` (Task 2).
- Produces: `HitZone` frozen dataclass (fields: `name: str`, `classification: Literal["mobility", "gun", "neither"]`, `x_min: float`, `x_max: float`, `y_min: float`, `y_max: float`), `classify_hit_location(zones: list[HitZone], overall_hit_pct: float, n_samples: int = 20000, rng: np.random.Generator | None = None) -> dict[str, float]` — for Task 6 to call once per (vehicle, profile, range band, crew quality).

- [ ] **Step 1: Write the failing tests**

Add `HitZone` and `classify_hit_location` to the `test_formulas.py` import list.

Add this test class after `TestVerticalLateralHitPct`:

```python
class TestHitLocationClassification:
    """Monte Carlo classification of where a hit lands within a target
    profile's zone geometry, given the shot's overall hit probability."""

    def _single_zone_covering_everything(self, classification):
        return [HitZone(name="whole area", classification=classification,
                         x_min=-999.0, x_max=999.0, y_min=-999.0, y_max=999.0)]

    def test_single_zone_covering_everything_gets_100_percent(self):
        zones = self._single_zone_covering_everything("mobility")
        result = classify_hit_location(zones, overall_hit_pct=85.0, n_samples=2000,
                                        rng=np.random.default_rng(1))
        assert result["mobility"] == pytest.approx(100.0, abs=0.5)
        assert result["gun"] == pytest.approx(0.0, abs=0.5)
        assert result["neither"] == pytest.approx(0.0, abs=0.5)

    def test_no_zones_at_all_is_always_neither(self):
        result = classify_hit_location([], overall_hit_pct=85.0, n_samples=2000,
                                        rng=np.random.default_rng(1))
        assert result["neither"] == pytest.approx(100.0, abs=0.5)

    def test_result_percentages_sum_to_100(self):
        zones = [
            HitZone(name="gun zone", classification="gun", x_min=-0.5, x_max=0.5, y_min=-0.3, y_max=0.4),
            HitZone(name="mobility zone", classification="mobility", x_min=-1.5, x_max=1.5, y_min=-0.6, y_max=-0.3),
        ]
        result = classify_hit_location(zones, overall_hit_pct=70.0, n_samples=5000,
                                        rng=np.random.default_rng(2))
        assert sum(result.values()) == pytest.approx(100.0, abs=0.01)

    def test_converges_across_independent_seeds(self):
        """Two independent runs with different seeds must agree within a
        small tolerance -- proof the sample count is high enough to be
        stable, not just internally consistent with itself."""
        zones = [
            HitZone(name="gun zone", classification="gun", x_min=-0.5, x_max=0.5, y_min=-0.3, y_max=0.4),
            HitZone(name="mobility zone", classification="mobility", x_min=-1.5, x_max=1.5, y_min=-0.6, y_max=-0.3),
        ]
        result_a = classify_hit_location(zones, overall_hit_pct=70.0, n_samples=20000,
                                          rng=np.random.default_rng(10))
        result_b = classify_hit_location(zones, overall_hit_pct=70.0, n_samples=20000,
                                          rng=np.random.default_rng(20))
        for key in ("mobility", "gun", "neither"):
            assert result_a[key] == pytest.approx(result_b[key], abs=2.0)

    def test_tighter_dispersion_at_higher_hit_pct_concentrates_on_center_zone(self):
        """A small central gun zone should catch a much higher share of
        hits at a high (tight-dispersion) hit% than at a low one."""
        zones = [
            HitZone(name="gun zone", classification="gun", x_min=-0.3, x_max=0.3, y_min=-0.3, y_max=0.3),
        ]
        tight = classify_hit_location(zones, overall_hit_pct=95.0, n_samples=20000,
                                       rng=np.random.default_rng(3))
        loose = classify_hit_location(zones, overall_hit_pct=20.0, n_samples=20000,
                                       rng=np.random.default_rng(3))
        assert tight["gun"] > loose["gun"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest counters/armor_calc/tests/test_formulas.py::TestHitLocationClassification -v`
Expected: FAIL — `HitZone` and `classify_hit_location` do not exist yet.

- [ ] **Step 3: Implement the type and classification function**

Add to `counters/armor_calc/formulas.py`, directly after `vertical_lateral_hit_pct`. First confirm `Literal` is already imported from `typing` (it is, used elsewhere in this file for `AmmoFamily` and `FlawSeverity`) — no new import needed for that. Add:

```python
@dataclass(frozen=True)
class HitZone:
    """One named region of a target profile's hit-location geometry.

    Coordinates are metres, centred on the profile's aim point (its own
    centre of mass) -- x is lateral (negative = left), y is vertical
    (negative = below aim point), matching Appendix 15's own convention.

    Attributes:
        name: Human-readable label (e.g. "driver", "transmission").
        classification: "mobility" (engine/transmission/final-drive),
            "gun" (turret ring/gun/breech/ammunition stowage), or
            "neither" (crew position with no adjacent critical system).
        x_min, x_max, y_min, y_max: This zone's bounding box, metres.
    """

    name: str
    classification: Literal["mobility", "gun", "neither"]
    x_min: float
    x_max: float
    y_min: float
    y_max: float


def _find_zone(zones: list[HitZone], x: float, y: float) -> HitZone | None:
    for zone in zones:
        if zone.x_min <= x <= zone.x_max and zone.y_min <= y <= zone.y_max:
            return zone
    return None


def classify_hit_location(
    zones: list[HitZone],
    overall_hit_pct: float,
    n_samples: int = 20000,
    rng: np.random.Generator | None = None,
) -> dict[str, float]:
    """Monte Carlo classification of where a Casualty-tier hit lands
    within a target profile, given the shot's overall hit probability.

    Source: Bird & Livingston Appendix 15. Samples many percentile dice
    rolls through shot_displacement_m() (itself validated against the
    chapter's own worked examples) to build a real (dx, dy) scatter
    pattern, then tallies which zone each sample lands in. Monte Carlo
    rather than analytic integration -- robust to irregular zone shapes,
    and its convergence is directly testable (see
    test_converges_across_independent_seeds) in a way a hand-derived
    integral would not be.

    Any (x, y) not covered by an explicit zone is implicitly "neither" --
    zones do not need to tile the plausible scatter area exhaustively by
    construction, the function does it for them.

    Args:
        zones: The target profile's zone geometry.
        overall_hit_pct: This shot's overall hit probability (0-100),
            already computed by hit_probability() for the actual gun/
            range/crew-quality combination -- not re-derived here.
        n_samples: Monte Carlo sample count. 20000 keeps independent runs
            within about 2 percentage points of each other (see the
            convergence test) -- a design-time cost, not a table-time one.
        rng: Optional seeded generator, for reproducible tests. A fresh
            generator is created if not given.

    Returns:
        {"mobility": pct, "gun": pct, "neither": pct}, summing to 100.0.
    """
    if rng is None:
        rng = np.random.default_rng()
    vertical_hit_pct, lateral_hit_pct = vertical_lateral_hit_pct(overall_hit_pct)

    vertical_rolls = rng.uniform(0.0, 99.0, n_samples)
    lateral_rolls = rng.uniform(0.0, 99.0, n_samples)
    vertical_signs = rng.choice([-1.0, 1.0], n_samples)
    lateral_signs = rng.choice([-1.0, 1.0], n_samples)

    counts = {"mobility": 0, "gun": 0, "neither": 0}
    for i in range(n_samples):
        dy = vertical_signs[i] * shot_displacement_m(vertical_rolls[i], vertical_hit_pct)
        dx = lateral_signs[i] * shot_displacement_m(lateral_rolls[i], lateral_hit_pct)
        zone = _find_zone(zones, dx, dy)
        counts[zone.classification if zone is not None else "neither"] += 1

    total = float(n_samples)
    return {k: 100.0 * v / total for k, v in counts.items()}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest counters/armor_calc/tests/test_formulas.py::TestHitLocationClassification -v`
Expected: PASS (5 tests). If `test_converges_across_independent_seeds` is flaky (fails intermittently outside `abs=2.0`), increase `n_samples` in that test to 50000 rather than loosening the tolerance further — the point of the test is proving real convergence.

- [ ] **Step 5: Run the full test suite**

Run: `python3 -m pytest counters/armor_calc/tests/ -q`
Expected: 94 passed (89 + 5).

- [ ] **Step 6: Commit**

```bash
git add counters/armor_calc/formulas.py counters/armor_calc/tests/test_formulas.py
git commit -m "feat: add HitZone geometry type and Monte Carlo hit-location classification"
```

---

### Task 4: Tiger I Ausf E Front-arc zone geometry

**Files:**
- Create: `counters/armor_calc/data/hit_zones.csv`
- Test: `counters/armor_calc/tests/test_pipeline.py` (new test class)
- Modify: `counters/armor_calc/pipeline.py` (add loader)

**Interfaces:**
- Consumes: `HitZone` (Task 3).
- Produces: `HitZoneRow` frozen dataclass (fields: `vehicle: str`, `profile: str`, `arc: str`, `zone: HitZone`), `load_hit_zones(path: pathlib.Path = DATA_DIR / "hit_zones.csv") -> list[HitZoneRow]` in `pipeline.py` — for Task 6 to group by (vehicle, profile) and pass to `classify_hit_location`.

**Provenance note for this task's data**: neither project source (Bird & Livingston, John D. Salt's compilation) provides interior vehicle layout diagrams — confirmed directly this session. The coordinates below come from general historical/technical knowledge of Tiger I's well-documented layout (front-mounted transmission and final drives, driver front-left, radio operator/hull-MG front-right, three-man turret with the gun/mantlet centred), not a project-source citation. This is flagged explicitly in the CSV's own notes column, not left implicit — a higher-stakes flag than similar external-knowledge notes elsewhere in this project, since it drives an actual gameplay outcome (MOB vs. GUN kill) rather than an AV number.

- [ ] **Step 1: Write the failing test**

Add to `counters/armor_calc/tests/test_pipeline.py`:

```python
class TestHitZoneLoading:
    """Session finding (design spec, hit-location system): neither project
    source provides interior vehicle layout diagrams -- hit_zones.csv is
    built from general historical knowledge, flagged as such in its own
    notes column, not project-source-cited the way most other roster data
    is."""

    def test_tiger_hull_front_zones_load_and_cover_expected_classifications(self):
        rows = load_hit_zones()
        tiger_hull_zones = [r.zone for r in rows if r.vehicle == "Tiger I Ausf E" and r.profile == "Hull" and r.arc == "Front"]
        classifications = {z.classification for z in tiger_hull_zones}
        assert "mobility" in classifications  # front-mounted transmission
        assert "neither" in classifications  # driver/radio-operator positions
        assert len(tiger_hull_zones) >= 3

    def test_tiger_turret_front_zones_have_no_mobility_zone(self):
        """No vehicle's turret contains a mobility-critical component --
        the transmission/engine/final-drive are always in the hull."""
        rows = load_hit_zones()
        tiger_turret_zones = [r.zone for r in rows if r.vehicle == "Tiger I Ausf E" and r.profile == "Turret" and r.arc == "Front"]
        classifications = {z.classification for z in tiger_turret_zones}
        assert "mobility" not in classifications
        assert "gun" in classifications  # mantlet/gun itself
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest counters/armor_calc/tests/test_pipeline.py::TestHitZoneLoading -v`
Expected: FAIL — `load_hit_zones` does not exist yet, and `data/hit_zones.csv` does not exist yet.

- [ ] **Step 3: Create the CSV data file**

Create `counters/armor_calc/data/hit_zones.csv`:

```csv
vehicle,profile,arc,zone_name,classification,x_min_m,x_max_m,y_min_m,y_max_m,notes
Tiger I Ausf E,Hull,Front,driver,neither,-0.9,-0.2,-0.3,0.3,"General historical knowledge, not project-source-cited: Tiger's driver seated front-left of hull centreline."
Tiger I Ausf E,Hull,Front,radio operator / hull MG,neither,0.2,0.9,-0.3,0.3,"General historical knowledge: radio operator/hull machine-gunner seated front-right, mirroring the driver."
Tiger I Ausf E,Hull,Front,transmission and final drive,mobility,-1.5,1.5,-0.6,-0.3,"General historical knowledge: Tiger (like most WW2-era German and American medium/heavy tanks) used a front-mounted transmission and final drive, engine at rear, driveshaft under the crew floor -- a hull front hit is genuinely a mobility risk, not just a crew risk."
Tiger I Ausf E,Turret,Front,mantlet and gun,gun,-0.5,0.5,-0.3,0.4,"General historical knowledge: Tiger's 88mm gun and mantlet centred on the turret front."
Tiger I Ausf E,Turret,Front,gunner and loader positions,neither,-1.1,-0.5,-0.4,0.4,"General historical knowledge: turret crew positions flanking the gun -- no mobility-critical or ammunition-critical systems directly behind the turret front plate for a Tiger (main ammunition stowage is hull-sponson-based, not reachable from a Front-arc hit on this profile)."
Tiger I Ausf E,Turret,Front,commander position,neither,0.5,1.1,-0.4,0.4,"General historical knowledge: commander's station on the opposite side of the gun from the loader."
```

- [ ] **Step 4: Implement the loader**

Add to `counters/armor_calc/pipeline.py`. First add `HitZone` to the existing `from .formulas import (...)` block (alphabetical position). Then add, after the `VehiclePlateRow` class and its methods (search for the end of `resolve_av_heat`, right before `def _parse_optional_float`):

```python
@dataclass(frozen=True)
class HitZoneRow:
    vehicle: str
    profile: str  # "Hull" or "Turret"
    arc: str  # "Front" only, this phase
    zone: HitZone


def load_hit_zones(path: pathlib.Path = DATA_DIR / "hit_zones.csv") -> list[HitZoneRow]:
    """Load per-vehicle hit-location zone geometry.

    See that CSV's own notes column for provenance -- neither project
    source provides interior vehicle layout diagrams, so this data is
    general historical knowledge, not project-source-cited.
    """
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append(
                HitZoneRow(
                    vehicle=r["vehicle"],
                    profile=r["profile"],
                    arc=r["arc"],
                    zone=HitZone(
                        name=r["zone_name"],
                        classification=r["classification"],  # type: ignore[arg-type]
                        x_min=float(r["x_min_m"]),
                        x_max=float(r["x_max_m"]),
                        y_min=float(r["y_min_m"]),
                        y_max=float(r["y_max_m"]),
                    ),
                )
            )
    return rows
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m pytest counters/armor_calc/tests/test_pipeline.py::TestHitZoneLoading -v`
Expected: PASS (2 tests).

- [ ] **Step 6: Run the full test suite**

Run: `python3 -m pytest counters/armor_calc/tests/ -q`
Expected: 96 passed (94 + 2).

- [ ] **Step 7: Commit**

```bash
git add counters/armor_calc/data/hit_zones.csv counters/armor_calc/pipeline.py counters/armor_calc/tests/test_pipeline.py
git commit -m "feat: add Tiger I Front-arc hit-location zone geometry and loader"
```

---

### Task 5: Sherman M4A1 Front-arc zone geometry

**Files:**
- Modify: `counters/armor_calc/data/hit_zones.csv` (append rows)
- Test: `counters/armor_calc/tests/test_pipeline.py` (extend `TestHitZoneLoading`)

**Interfaces:**
- Consumes: `HitZoneRow`, `load_hit_zones` (Task 4). No new interfaces produced — same loader handles both vehicles' rows.

**Provenance note**: same as Task 4 — general historical knowledge, not project-source-cited. Sherman M4A1 was deliberately chosen as the pilot's second vehicle specifically because it is the **dry-stowage** variant: main gun ammunition stored in hull side sponsons above the tracks, not the later wet-stowage armored floor bins — the historically infamous "Ronson" ammunition-fire vulnerability. This is a real, well-documented case where ammunition location specifically mattered, and a meaningful test of whether the mechanic captures something historically true.

- [ ] **Step 1: Write the failing test**

Add to `TestHitZoneLoading` in `test_pipeline.py`:

```python
    def test_sherman_hull_front_zones_include_sponson_ammo_as_gun_classified(self):
        """Sherman M4A1 is the dry-stowage variant -- ammunition in hull
        side sponsons, not yet relocated to armoured wet-stowage floor
        bins. Ammunition counts as 'gun' classification (design spec:
        'Gun: turret ring, gun/breech, ammunition stowage within the
        profile')."""
        rows = load_hit_zones()
        sherman_hull_zones = [r.zone for r in rows if r.vehicle == "Sherman M4A1 (75mm)" and r.profile == "Hull" and r.arc == "Front"]
        classifications = {z.classification for z in sherman_hull_zones}
        assert "mobility" in classifications  # front transmission housing
        assert "gun" in classifications  # sponson-stored ammunition
        assert "neither" in classifications  # driver/bow-gunner positions

    def test_sherman_turret_front_zones_have_no_mobility_zone(self):
        rows = load_hit_zones()
        sherman_turret_zones = [r.zone for r in rows if r.vehicle == "Sherman M4A1 (75mm)" and r.profile == "Turret" and r.arc == "Front"]
        classifications = {z.classification for z in sherman_turret_zones}
        assert "mobility" not in classifications
        assert "gun" in classifications
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest counters/armor_calc/tests/test_pipeline.py::TestHitZoneLoading -v`
Expected: FAIL — the two new tests fail (no Sherman rows in `hit_zones.csv` yet); the pre-existing Tiger tests in the same class still pass.

- [ ] **Step 3: Append Sherman M4A1 rows to the CSV data file**

Append to `counters/armor_calc/data/hit_zones.csv` (do not modify the Tiger rows already there):

```csv
Sherman M4A1 (75mm),Hull,Front,driver,neither,-0.7,-0.15,-0.3,0.3,"General historical knowledge, not project-source-cited: M4A1 driver seated front-left."
Sherman M4A1 (75mm),Hull,Front,bow gunner,neither,0.15,0.7,-0.3,0.3,"General historical knowledge: bow machine-gunner seated front-right, mirroring the driver."
Sherman M4A1 (75mm),Hull,Front,transmission and final drive,mobility,-1.1,1.1,-0.6,-0.25,"General historical knowledge: Sherman's large, distinctive cast/welded transmission and final-drive housing bolted to the front of the hull -- an iconic, well-documented feature of the type."
Sherman M4A1 (75mm),Hull,Front,sponson ammunition stowage (dry stowage),gun,-1.35,-1.05,-0.2,0.3,"General historical knowledge: M4A1 is the pre-wet-stowage dry variant -- main gun ammunition stored in hull side sponsons above the tracks, the historically infamous 'Ronson' fire-vulnerability arrangement later fixed by wet stowage on other Sherman variants (see Sherman M4A3 (76mm) in this roster, already noted as wet-stowage-era)."
Sherman M4A1 (75mm),Hull,Front,sponson ammunition stowage (dry stowage),gun,1.05,1.35,-0.2,0.3,"Mirrors the opposite sponson -- see note on the -1.35/-1.05 zone."
Sherman M4A1 (75mm),Turret,Front,mantlet and gun (M34 mount),gun,-0.4,0.4,-0.3,0.4,"General historical knowledge: Sherman's 75mm gun and M34 gun mount/mantlet centred on the turret front."
Sherman M4A1 (75mm),Turret,Front,gunner and loader positions,neither,-0.9,-0.4,-0.4,0.4,"General historical knowledge: turret crew positions flanking the gun."
Sherman M4A1 (75mm),Turret,Front,commander position,neither,0.4,0.9,-0.4,0.4,"General historical knowledge: commander's station opposite the loader."
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest counters/armor_calc/tests/test_pipeline.py::TestHitZoneLoading -v`
Expected: PASS (4 tests total in this class).

- [ ] **Step 5: Run the full test suite**

Run: `python3 -m pytest counters/armor_calc/tests/ -q`
Expected: 98 passed (96 + 2).

- [ ] **Step 6: Commit**

```bash
git add counters/armor_calc/data/hit_zones.csv counters/armor_calc/tests/test_pipeline.py
git commit -m "feat: add Sherman M4A1 Front-arc hit-location zone geometry (dry-stowage pilot case)"
```

---

### Task 6: Precompute the Hit Location Table and write it to CSV

**Files:**
- Modify: `counters/armor_calc/pipeline.py`
- Test: `counters/armor_calc/tests/test_pipeline.py` (new test class)

**Interfaces:**
- Consumes: `load_hit_zones()` (Task 4), `classify_hit_location()` (Task 3), the existing `load_gun_curves()` and `hit_probability()`/`roll_threshold_for_probability()`/`_DICE_CDF_GE` (already in `formulas.py` from the Gunnery Roll work), `ALL_CREW_QUALITIES` (already imported in `pipeline.py`).
- Produces: `HitLocationThresholds` frozen dataclass (fields: `neither_threshold: int | None`, `gun_threshold: int | None`), `write_hit_location_reference_csv(hit_zones, curves, out_path, representative_gun_id="pziv_75l48_apcbc")` function, `hit_location_output.csv`. Wired into `main()`.

**Scoping decision, not deferred silently**: this pilot uses a single **representative attacking gun** (the roster's 75mm KwK40, `pziv_75l48_apcbc` — already the project's default reference-attacker diameter for AV-vs-Capped elsewhere) to compute the hit% that drives scatter width, rather than building a separate table per attacking gun. This mirrors the existing `diameter_mm=75.0` representative-attacker convention already used for the AV columns. A real per-gun table is a reasonable future expansion once the pilot validates the mechanic — not built now. This is noted in the design spec's decision log (Task 8), not just in code comments.

- [ ] **Step 1: Write the failing test**

Add to `test_pipeline.py`:

```python
class TestHitLocationReferenceCsv:
    def test_writes_a_row_per_vehicle_profile_range_band_crew_quality(self, tmp_path):
        from armor_calc.pipeline import load_gun_curves, load_hit_zones, write_hit_location_reference_csv

        hit_zones = load_hit_zones()
        curves = load_gun_curves()
        out_path = tmp_path / "hit_location_output.csv"
        write_hit_location_reference_csv(hit_zones, curves, out_path)

        with open(out_path, newline="") as f:
            rows = list(csv.DictReader(f))

        vehicles_profiles = {(r["vehicle"], r["profile"]) for r in rows}
        assert ("Tiger I Ausf E", "Hull") in vehicles_profiles
        assert ("Tiger I Ausf E", "Turret") in vehicles_profiles
        assert ("Sherman M4A1 (75mm)", "Hull") in vehicles_profiles
        assert ("Sherman M4A1 (75mm)", "Turret") in vehicles_profiles
        assert len(rows) > 0

    def test_tiger_turret_never_produces_a_mobility_threshold(self, tmp_path):
        """No roll should ever be able to land on 'mobility' for a profile
        whose zone geometry has no mobility-classified zone at all --
        confirms the threshold conversion correctly reflects a real 0%
        rather than defaulting to some nonzero placeholder."""
        from armor_calc.pipeline import load_gun_curves, load_hit_zones, write_hit_location_reference_csv

        hit_zones = load_hit_zones()
        curves = load_gun_curves()
        out_path = tmp_path / "hit_location_output.csv"
        write_hit_location_reference_csv(hit_zones, curves, out_path)

        with open(out_path, newline="") as f:
            rows = [r for r in csv.DictReader(f) if r["vehicle"] == "Tiger I Ausf E" and r["profile"] == "Turret"]
        assert len(rows) > 0
        for r in rows:
            assert float(r["mobility_pct"]) == pytest.approx(0.0, abs=0.5)
```

Add `import csv` and `import pytest` at the top of `test_pipeline.py` if not already present (check the existing imports — `pytest` should already be imported given the file has `@pytest.mark`-style usage elsewhere; `csv` needs adding if this is the first use of it in this test file).

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest counters/armor_calc/tests/test_pipeline.py::TestHitLocationReferenceCsv -v`
Expected: FAIL — `write_hit_location_reference_csv` does not exist yet.

- [ ] **Step 3: Implement the precomputation and CSV writer**

First, add to `counters/armor_calc/formulas.py` (near `VehicleFireThresholds`, since it's the same pattern):

```python
@dataclass(frozen=True)
class HitLocationThresholds:
    """The two numbers printed per vehicle/profile/range/crew-quality row:
    roll the 1d6+1d8+1d12 sum against them to resolve Neither / Gun /
    Mobility in one roll, same pattern as VehicleFireThresholds resolves
    Miss / Turret / Hull.

    Attributes:
        neither_threshold: Roll below this = Neither (downgrades the
            Casualty result to Pinned, Rule 18.6a). None if every
            possible roll clears "neither" (i.e. neither_pct rounds to 0).
        gun_threshold: Roll at or above this = Mobility kill. Between
            neither_threshold and this (exclusive) = Gun kill. None if no
            roll can reach "mobility" specifically (e.g. a turret profile
            with no mobility-classified zone at all).
    """

    neither_threshold: int | None
    gun_threshold: int | None


def hit_location_thresholds(zone_split: dict[str, float]) -> HitLocationThresholds:
    """Convert a Mobility/Gun/Neither percentage split (from
    classify_hit_location) into the two dice-roll thresholds a player
    compares their 1d6+1d8+1d12 roll against.

    Args:
        zone_split: {"mobility": pct, "gun": pct, "neither": pct}, as
            returned by classify_hit_location().

    Returns:
        HitLocationThresholds ready to print and roll against.
    """
    hit_or_better_pct = zone_split["gun"] + zone_split["mobility"]
    neither_t = roll_threshold_for_probability(hit_or_better_pct)
    gun_t = roll_threshold_for_probability(zone_split["mobility"])
    return HitLocationThresholds(neither_threshold=neither_t, gun_threshold=gun_t)
```

Then, in `counters/armor_calc/pipeline.py`, add `HitLocationThresholds`, `classify_hit_location`, `hit_location_thresholds` to the `from .formulas import (...)` block. Add this function after `write_vehicle_fire_thresholds_csv`:

```python
def write_hit_location_reference_csv(
    hit_zones: list[HitZoneRow],
    curves: dict[str, GunCurveFit],
    out_path: pathlib.Path,
    representative_gun_id: str = "pziv_75l48_apcbc",
) -> None:
    """The Hit Location Table: per vehicle, per profile (Hull/Turret), per
    range band, per crew quality, the two thresholds that resolve
    Neither/Gun/Mobility in one roll when a Casualty result occurs
    (Rule 18.6a).

    Uses a single representative attacking gun (default: the roster's
    75mm KwK40) to compute the hit% that drives scatter width, rather
    than a separate table per attacking gun -- the same simplification
    already used for the AV-vs-Capped columns (diameter_mm=75.0
    representative attacker). A real per-gun table is a reasonable future
    expansion, not built in this pilot -- see design spec open items.
    """
    bands = [100, 250, 500, 750, 1000, 1500, 2000, 2500]
    fit = curves[representative_gun_id]

    zones_by_vehicle_profile: dict[tuple[str, str], list[HitZone]] = {}
    for row in hit_zones:
        zones_by_vehicle_profile.setdefault((row.vehicle, row.profile), []).append(row.zone)

    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["vehicle", "profile", "crew_quality", "range_m", "mobility_pct", "gun_pct", "neither_pct",
             "neither_below", "mobility_at_or_above"]
        )
        for (vehicle, profile), zones in zones_by_vehicle_profile.items():
            for quality in ALL_CREW_QUALITIES:
                for range_m in bands:
                    hit_pct = hit_probability(fit.muzzle_velocity_fps, fit.k_factor, range_m, quality)
                    split = classify_hit_location(zones, hit_pct)
                    thresholds = hit_location_thresholds(split)
                    writer.writerow(
                        [
                            vehicle, profile, quality, range_m,
                            round(split["mobility"], 1), round(split["gun"], 1), round(split["neither"], 1),
                            thresholds.neither_threshold, thresholds.gun_threshold,
                        ]
                    )
```

Add `hit_probability` to the existing `from .formulas import (...)` block in `pipeline.py` if not already present (check first — it may already be imported for the Gunnery Roll's own table-writing function).

Finally, wire it into `main()` — add near the end, after `write_vehicle_fire_thresholds_csv(curves, DATA_DIR.parent / "vehicle_fire_thresholds_output.csv")`:

```python
    hit_zones = load_hit_zones()
    write_hit_location_reference_csv(hit_zones, curves, DATA_DIR.parent / "hit_location_output.csv")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest counters/armor_calc/tests/test_pipeline.py::TestHitLocationReferenceCsv -v`
Expected: PASS (2 tests).

- [ ] **Step 5: Run the full test suite and the real pipeline**

Run: `python3 -m pytest counters/armor_calc/tests/ -q`
Expected: 100 passed (98 + 2).

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo && python3 -m counters.armor_calc.pipeline`
Expected: `Wrote all armor_calc outputs to .../counters/armor_calc`, and a new `counters/armor_calc/hit_location_output.csv` file exists.

Run: `cat counters/armor_calc/hit_location_output.csv | head -20` and eyeball the results — confirm Tiger's Turret rows show `mobility_pct` at or near 0.0 for every row (no mobility zone in that profile), and Sherman's Hull rows show a non-trivial `gun_pct` (the sponson ammunition zones) rather than 0.

- [ ] **Step 6: Commit**

```bash
git add counters/armor_calc/formulas.py counters/armor_calc/pipeline.py counters/armor_calc/tests/test_pipeline.py
git commit -m "feat: precompute the Hit Location Table for the pilot vehicles"
```

---

### Task 7: Rulebook integration

**Files:**
- Modify: `docs/source/section_17__vehicles_counter_design_and_movement.rst`
- Modify: `docs/source/section_18__vehicle_combat_resolution.rst`
- Modify: `docs/source/section_1__introduction_and_components.rst`
- Modify: `docs/source/appendix_e__design_notes.rst`

**Interfaces:**
- Consumes: the actual precomputed numbers from `hit_location_output.csv` (Task 6) as the illustrative example values in the rule text's example table.
- Produces: no code interfaces — this task is rulebook text only.

- [ ] **Step 1: Rewrite Rule 17.1.1 to remove the free choice**

In `docs/source/section_17__vehicles_counter_design_and_movement.rst`, replace:

```
**17.1.1**  Vehicle counters have two rear faces representing damage states: MOB KILL (mobility killed — M0, can still fire) and GUN KILL (gun destroyed — MG only, can still move). When a vehicle takes a Casualty result, the owning player chooses which rear face applies based on the most plausible damage given the shot geometry.
```

with:

```
**17.1.1**  Vehicle counters have two rear faces representing damage states: MOB KILL (mobility killed — M0, can still fire) and GUN KILL (gun destroyed — MG only, can still move). When a vehicle takes a Casualty result, roll against the Hit Location Table (Rule 18.6a) to determine which rear face applies — this is no longer a free narrative choice.
```

- [ ] **Step 2: Add a new "17.7 Hit Location" section describing the printed table**

In `docs/source/section_17__vehicles_counter_design_and_movement.rst`, add this new section at the end of the file (after the existing `17.6 Vehicle Movement` section and its terrain-cost table):

```

17.7  Hit Location
-------------------


**17.7.1**  Vehicles with a Hit Location Table printed (Tiger I Ausf E and Sherman M4A1 (75mm), this edition — see Rule 18.6a) resolve MOB kill vs. GUN kill by roll rather than free choice. Vehicles without a printed Hit Location Table continue to use the owning player's judgement call (Rule 17.1.1) until their own table is built.

**17.7.2**  The table gives a Neither Threshold and a Mobility Threshold for each range band and crew quality, already resolved for the specific attacking gun class used to build it. No calculation is required at the table — read the row for the actual range and the firing vehicle's own Crew Quality (Rule 18.1a.2).

*Example format (values illustrative, drawn from this session's actual computed output for Tiger I's Hull profile, Regular crew — see* `hit_location_output.csv` *for the full table):*

.. list-table::
   :header-rows: 1

   * - Range
     - Result
   * - 100–750m
     - Roll below Neither Threshold: Neither (Casualty downgrades to Pinned). Roll at or above Mobility Threshold: MOB kill. Between the two: GUN kill.
   * - 1000m+
     - Same procedure, using that range band's own printed thresholds — dispersion widens with range, so the Neither band grows.

```

- [ ] **Step 3: Add the new "18.6a Hit Location" procedural rule**

In `docs/source/section_18__vehicle_combat_resolution.rst`, add this new section directly after Rule 18.6.2 (the full-penetration damage-roll modifiers table) and before `18.7 Vehicle Damage States`:

```

18.6a  Hit Location
--------------------


**18.6a.1**  Whenever Rule 18.5.1 or 18.6.1 produces a "Component damage — vehicle Casualty" result, roll 1d6+1d8+1d12 (the same combination used for every other attack, Rule 8.5.1) against the target vehicle's own Hit Location Table (Rule 17.7) for the profile that was hit (Hull or Turret, per the Gunnery Roll's own determination, Rule 18.1a) and the actual range to target.

**18.6a.2**  If the roll is below the Neither Threshold, the hit landed somewhere non-critical — downgrade the result from Casualty to Pinned (Rule 18.7) instead. The round penetrated, but nothing essential was destroyed.

**18.6a.3**  If the roll is at or above the Mobility Threshold, the hit is a MOB kill. If the roll is at or above the Neither Threshold but below the Mobility Threshold, the hit is a GUN kill.

**18.6a.4**  Vehicles without a printed Hit Location Table use Rule 17.1.1's owning-player judgement call instead — this rule only applies to vehicles whose table has actually been built (Tiger I Ausf E and Sherman M4A1 (75mm), this edition).

*NOTE: This can only ever make an outcome different from what free choice would have picked — it has no effect on whether a Casualty occurs in the first place (Rule 18.5/18.6 are unchanged), only on which specific outcome follows one. A hit that resolves to "Neither" is a real, sourced consequence of this system, not an edge case being carved out: it reflects that not every penetrating hit finds something critical to destroy.*

```

- [ ] **Step 4: Add new definitions to Section 1.3**

In `docs/source/section_1__introduction_and_components.rst`, add these new definitions immediately after the existing **Schürzen** definition (the last one added during the earlier rulebook integration pass):

```

**Hit Location Table —**  A per-vehicle table (Rule 17.7) giving the Neither/Mobility dice-roll thresholds used to resolve MOB kill vs. GUN kill vs. a downgrade to Pinned, whenever a Casualty result occurs. Rule 18.6a.

**Mobility zone —**  A hit-location zone containing a mobility-critical component (engine, transmission, final drive). A roll landing here produces a MOB kill.

**Gun zone —**  A hit-location zone containing the gun, breech, turret ring, or on-board ammunition stowage. A roll landing here produces a GUN kill.

```

- [ ] **Step 5: Add a new Appendix E design note**

In `docs/source/appendix_e__design_notes.rst`, add this new entry at the end of the file (after `E.57`, the Schürzen design note from the earlier rulebook integration pass):

```

E.58  Hit Location — Precomputed Scatter, Not a Live Roll-and-Diagram
------------------------------------------------------------------------


*Design note: Bird & Livingston's Appendix 15 "Shot Placement System" gives real dice-to-displacement mathematics but no per-vehicle component diagrams — the book's own worked example determines what a hit struck by eyeballing a diagram, which does not exist for any vehicle in this project. Two ways to use the sourced math were considered: have players roll the dice live and consult a printed vehicle diagram each time a Casualty occurs, or precompute the distribution once per vehicle/profile/range/crew-quality and print a single small threshold table, the same "zero lines" pattern used for the Gunnery Table and the Shatter Gap Table elsewhere in this system. The precomputed approach was chosen — real per-vehicle zone geometry (driver, gunner, loader, commander, engine, transmission, ammunition, fuel, each independently positioned and classified Mobility/Gun/Neither) feeds a Monte Carlo simulation of the sourced scatter equations once, at design time, rather than requiring a diagram lookup at the table every time a tank is hit. A genuine finding surfaced by modelling real zone geometry rather than a flat Front=crew/Rear=mobility assumption: Tiger (and most WW2-era German and American medium/heavy tanks) mounted the transmission at the front of the hull with the engine at the rear, so a Hull Front hit is a real mobility risk, not just a crew risk — a cruder abstraction would have missed this. The pilot deliberately covers only two vehicles (Tiger I, Sherman M4A1) and only their Front arc — Sherman M4A1 chosen specifically as the dry-stowage variant, since its sponson ammunition placement is a historically real case where location mattered (the "Ronson" reputation), a meaningful test of whether the mechanic captures something true rather than being mechanically elaborate for its own sake. Vehicles without a built Hit Location Table keep the original free-choice rule (17.1.1) until their own table exists — this is an incremental replacement, not a flag day.*

```

- [ ] **Step 6: Verify the Sphinx build stays clean**

Run: `cd /home/marvin/ClaudeCodeProjects/wdr_repo/docs && pip install --quiet sphinx 2>&1 | tail -3` (installs Sphinx if not already present in this environment, matching how it was done earlier this session)

Run: `python3 -m sphinx -b dummy source /tmp/hitloc_sphinx_check -W 2>&1 | tail -15`
Expected: `build succeeded.` with zero warnings.

Run: `rm -rf /tmp/hitloc_sphinx_check`

- [ ] **Step 7: Commit**

```bash
git add docs/source/section_17__vehicles_counter_design_and_movement.rst docs/source/section_18__vehicle_combat_resolution.rst docs/source/section_1__introduction_and_components.rst docs/source/appendix_e__design_notes.rst
git commit -m "feat: wire Hit Location system into the rulebook (Rules 17.1.1, 17.7, 18.6a)"
```

---

### Task 8: Update the design spec with final results and correct the citation error

**Files:**
- Modify: `docs/superpowers/specs/2026-07-04-hit-location-and-crew-position-design.md`

**Interfaces:**
- Consumes: everything from Tasks 1-7 (final test counts, actual computed numbers from `hit_location_output.csv`).
- Produces: no code interfaces — this task closes out the design spec's own decision log, matching the pattern used throughout the sister spec (`2026-07-04-armored-combat-penetration-physics-design.md`) of appending an "implemented and tested" note to each section as work completes.

- [ ] **Step 1: Correct the Rule 18.7.1 citation error**

In `docs/superpowers/specs/2026-07-04-hit-location-and-crew-position-design.md`, find the line in Section 1 that reads:

```
Today, when a shot produces a Casualty result (Rule 18.5/18.6), the owning player freely chooses whether it's a MOB kill or a GUN kill, justified narratively ("based on the most plausible damage given shot geometry" — Rule 18.7.1).
```

Replace `Rule 18.7.1` with `Rule 17.1.1` (confirmed directly against the rulebook source during planning — this was a citation error in the original spec, not a rules change).

- [ ] **Step 2: Append implementation results to Section 3**

At the end of Section 3.4 ("Player-facing surface"), add:

```

**Implemented and tested** (`formulas.py`: `shot_displacement_m`, `vertical_lateral_hit_pct`, `HitZone`, `classify_hit_location`, `HitLocationThresholds`, `hit_location_thresholds`; `data/hit_zones.csv`: Front-arc zone geometry for both pilot vehicles; `pipeline.py`: `load_hit_zones`, `write_hit_location_reference_csv`, wired into `main()`), 15 new regression tests across `test_formulas.py` and `test_pipeline.py`, all passing (100 total). Rulebook updated: Rule 17.1.1 rewritten, new Rule 17.7 and Rule 18.6a added, Section 1.3 definitions extended, Appendix E.58 added. Verified with a real Sphinx build (`sphinx-build -b dummy -W`), zero warnings.
```

- [ ] **Step 3: Record the actual computed numbers as a concrete finding**

Open `counters/armor_calc/hit_location_output.csv` and read the actual computed values for Tiger I Ausf E and Sherman M4A1 (75mm), both profiles, at the 500m range band, Regular crew quality. Add a new subsection at the end of the spec:

```markdown

## 7. Pilot results — real numbers, not just a working mechanism

Computed values at 500m, Regular crew quality (illustrative — see `hit_location_output.csv` for the full table across all range bands and crew qualities):

| Vehicle | Profile | Mobility % | Gun % | Neither % |
|---|---|---|---|---|
| Tiger I Ausf E | Hull | [fill in from actual CSV output] | [fill in] | [fill in] |
| Tiger I Ausf E | Turret | 0.0 (no mobility zone) | [fill in] | [fill in] |
| Sherman M4A1 (75mm) | Hull | [fill in] | [fill in] | [fill in] |
| Sherman M4A1 (75mm) | Turret | 0.0 (no mobility zone) | [fill in] | [fill in] |

Both vehicles' Turret profiles correctly show 0% Mobility — no vehicle's turret contains a mobility-critical component, and the classification pipeline reflects a real absence rather than defaulting to some nonzero placeholder (confirmed by `test_tiger_turret_never_produces_a_mobility_threshold`). Sherman's Hull profile shows a materially higher Gun percentage than Tiger's, driven directly by the sponson ammunition zones specific to the dry-stowage pilot case — the concrete result the Sherman pilot choice was meant to test for.
```

Replace each `[fill in from actual CSV output]` / `[fill in]` placeholder with the real number read from the CSV in this step — this document must not be committed with literal placeholder text left in it; the table must contain the actual computed percentages before this task is considered done.

- [ ] **Step 4: Update the open items section**

In Section 6 ("Open items"), add a new bullet at the end:

```
- **Scaling beyond the pilot.** This pass covers 2 of 13 roster vehicles and Front arc only. Expanding to the rest of the roster (and to Side/Rear arcs) means: (a) building real zone geometry for 11 more vehicles, general historical knowledge each time, not a quick copy-paste; (b) deciding whether the single-representative-attacker-gun simplification (Task 6) still holds once a genuinely diverse set of attacking guns is in play, or whether a full per-gun table becomes necessary; (c) re-checking whether Side/Rear arc geometry (tracks become visible, engine bay fully exposed from Rear) meaningfully changes the zone classifications rather than just repositioning them.
```

- [ ] **Step 5: Verify the file reads cleanly end to end**

Read the full updated spec file back and confirm: no `[fill in]` placeholder text remains anywhere, the Rule citation now says 17.1.1 not 18.7.1, and the new Section 7 numbers are internally consistent with what `hit_location_output.csv` actually contains (spot-check at least one row by hand).

- [ ] **Step 6: Commit**

```bash
git add docs/superpowers/specs/2026-07-04-hit-location-and-crew-position-design.md
git commit -m "docs: close out hit-location design spec with final pilot results, fix Rule 17.1.1 citation"
```

---

## Self-Review

**Spec coverage**: §1 (why/source findings) — covered by Task 1-2's docstrings citing the same findings. §2 (decisions) — every locked decision maps to a task: full rigor → Tasks 1-5; MOB/GUN replacement not new categories → Task 7's Rule 18.6a scope; full crew/component layout → Tasks 4-5's zone lists; pilot vehicles/Front-only → Tasks 4-5; formula not raw table → Task 1; Monte Carlo not integration → Task 3; center-of-mass only → implicit in the coordinate system (Task 3's `HitZone`, no aim-point parameter exists to vary). §3.1-3.4 (architecture) — Tasks 1, 2, 3, 6 respectively. §4 (validation) — formula validation in Task 1, Monte Carlo convergence in Task 3, historical sanity check folded into Task 6 Step 5's manual eyeball plus Tasks 4-5's classification-presence tests. §5 (out of scope) — respected throughout (no Side/Rear geometry, no other vehicles, no aim-point parameter, no new damage categories beyond Neither→Pinned). §6 (open items) — zone provenance flagged in every CSV row's notes column (Tasks 4-5); Front-arc generalization concern is inherent to the scope (not generalized beyond Front in this plan); crew-quality table size accepted as-is per the spec's own reasoning; Neither→Pinned rule implemented exactly as decided (Task 7 Step 3).

**Placeholder scan**: the two `[fill in from actual CSV output]` markers in Task 8 Step 3 are intentional and self-resolving — the task's own Step 3 instructions require replacing them with real computed numbers before the step is complete, and Step 5 explicitly re-verifies none remain. This is different from a plan leaving a placeholder unresolved; it is the plan directing the implementer to compute and insert a real value that cannot be known until Tasks 1-6 have actually run.

**Type consistency check**: `HitZone` (Task 3) is consumed identically in Task 4/5 (`HitZoneRow.zone: HitZone`) and Task 6 (`zones_by_vehicle_profile: dict[tuple[str, str], list[HitZone]]`). `classify_hit_location`'s return type `dict[str, float]` with keys `"mobility"/"gun"/"neither"` is used consistently in Task 3's own tests, Task 6's `hit_location_thresholds()`, and Task 6's CSV column names (`mobility_pct`, `gun_pct`, `neither_pct`). `shot_displacement_m(dice_score, hit_pct)` signature matches between Task 1's definition and Task 3's two call sites (vertical and lateral). `HitLocationThresholds` field names (`neither_threshold`, `gun_threshold`) match between Task 6's dataclass definition and its use in `write_hit_location_reference_csv`.

---

Plan complete and saved to `docs/superpowers/plans/2026-07-04-hit-location-and-crew-position.md`. Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**
