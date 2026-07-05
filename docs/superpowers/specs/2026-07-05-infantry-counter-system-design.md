# Infantry Counter System and Shared Quality Core — Design Spec

## 1. Why this exists

"With Deepest Regret..." currently derives infantry/support-weapon counter values (rFP, Defence, Morale, M#/F#/G#) from an external spreadsheet (`wdr_infantry_counter_designer_v2.xlsx`, kept on Rod's Desktop, outside this repo) — the same role manual calculation used to play for vehicle armor/gunnery values before this session's sister work built `counters/armor_calc/`. That spreadsheet is not a loose collection of guesses: it implements a real, internally consistent algorithm (weapon rate-of-fire, weighted by a per-weapon-class suppression factor and a per-unit quality multiplier, log-compressed into the small-integer rFP scale printed on counters), calibrated against one anchor unit (German Grenadier squad, 1943, Regular quality, MG42 LMG → rFP 7) and already includes a 12-row pilot roster (German and Soviet infantry, 1943) with per-row source citations (Nafziger OOB, TM-E 30-451, STAVKA TO&E 1943, HDv 130) and a verification-status column (ANCHOR / PRELIMINARY / CROSS-CHECKED / PRIMARY SOURCE) — the same "flag your confidence, don't present a guess as a citation" discipline this project's vehicle work already holds itself to.

This phase ports that spreadsheet's algorithm into a tested Python package, `counters/infantry_calc/`, mirroring `armor_calc`'s conventions (CSV-driven data, tested formulas, precomputed reference output), and extracts a small shared "quality tier" module so that vehicle crew quality and infantry unit quality — two systems that turned out to already use nearly the same five-tier vocabulary — become one source of truth for what a tier name means, rather than two independently-evolving concepts that happen to share labels.

## 2. Decisions locked this session

Reached through direct questions, not assumed:

- **Replaces the spreadsheet, doesn't just cross-check it.** Mirrors how `armor_calc` superseded manual vehicle-stat calculation: the spreadsheet's own algorithm and roster data become the ported, tested source; the `.xlsx` file becomes historical reference, not the live tool.
- **Shared calculation core, not just a shared style.** A new `counters/quality/` package holds the one thing genuinely common to both domains — the quality-tier *concept* (five ordered labels: Elite/Veteran/Regular/Green/Militia). The *effect* of a tier stays entirely domain-specific: a vehicle crew's quality caps a hit probability (`crew_quality_hit_cap()`, unchanged); an infantry unit's quality multiplies weapon RPM, Defence, and Morale (`quality_multipliers()`, new). Forcing these into one shared formula would conflate two different mechanics that only happen to use the same five names.
- **`armor_calc`'s existing `CrewQuality` gets refactored now, not deferred.** `CrewQuality`/`ALL_CREW_QUALITIES` move to `counters/quality/tiers.py` as `Quality`/`ALL_QUALITIES`; `armor_calc.formulas` re-exports `CrewQuality` as an alias so no existing import in `armor_calc` or its tests has to change. This is a pure extraction — no behavior change to `armor_calc`, verified by its existing test suite passing untouched.
- **Scope: infantry squads and their organic support-weapon teams only.** Matches exactly what the spreadsheet covers (rifle/grenadier squads, integral MG/LMG teams). Towed artillery (real guns not mounted on a vehicle, e.g. a PAK40) is explicitly deferred to a future pass that would reuse `armor_calc`'s existing gun-curve-fitting machinery — not built this phase. Grenades and satchel charges are **not** in scope for a new conversion algorithm: grenades already resolve via a fixed G# value on the counter (Rule 9.3, a manually-assigned design constant, not something derived from a real-world weapon spec), and satchel charges are narrative equipment tied to the Engineer's existing DEMO capability (Rule 22.3), not a distinct derived stat.
- **Militia tier (infantry) is a computed extrapolation, explicitly flagged as such.** The spreadsheet only defines four tiers (Green/Regular/Veteran/Elite) — Militia doesn't exist in it. Continuing the same multiplicative step Regular→Green already uses (BTV×0.6, EM×0.9, MM×0.9) one tier further gives Green→Militia: **BTV=0.36, EM=0.81, MM=0.81** (combined ≈0.236, versus Green's 0.486) — a real calculation, not a citation, and documented as a game-balance estimate to be sanity-checked once real Militia-tier units (Volkssturm, opolcheniye-type formations) are added to the roster.
- **Considered and rejected: unifying `GunCurveFit.confidence` with the infantry roster's verify-status column.** `GunCurveFit.confidence` (rough/interpolated/fitted) measures numerical fit quality — how many data points, was it a real least-squares fit. The roster's ANCHOR/PRELIMINARY/CROSS-CHECKED/PRIMARY-SOURCE measures historical-provenance confidence — was this checked against a primary document. These are different axes of uncertainty (a curve can be well-fitted to historically-shaky data, or vice versa); kept as two separate concepts rather than forced into one enum.

## 3. Architecture

### 3.1 Package layout

```
counters/
  quality/                    -- NEW: shared core
    __init__.py
    tiers.py                  -- Quality Literal type, ALL_QUALITIES tuple
    tests/test_tiers.py
  armor_calc/                 -- EXISTING, refactored (pure extraction)
    formulas.py                -- CrewQuality = quality.tiers.Quality (re-exported alias);
                                   ALL_CREW_QUALITIES = quality.tiers.ALL_QUALITIES;
                                   crew_quality_hit_cap() unchanged
  infantry_calc/               -- NEW, mirrors armor_calc's shape
    __init__.py
    formulas.py                 -- weapon_rfp(), fire_interval_hexes(), unit_defence(),
                                    unit_morale(), quality_multipliers(), suppression factors
    pipeline.py                  -- load_weapons(), load_units(), write_infantry_roster_csv()
    data/
      weapons.csv                 -- one row per weapon: name, class, cyclic/practical RPM, max range
      units.csv                   -- one row per unit-variant/face: nation, type, year, quality,
                                     manpower, weapon loadout, source citation, verify status
    tests/
      test_formulas.py
      test_pipeline.py
    infantry_roster_output.csv    -- precomputed: one row per unit face, all derived stats
```

### 3.2 Shared quality core (`counters/quality/tiers.py`)

```python
Quality = Literal["elite", "veteran", "regular", "green", "militia"]
ALL_QUALITIES: tuple[Quality, ...] = ("elite", "veteran", "regular", "green", "militia")
```

That is the entire module's public surface — a type and an ordered tuple. No functions live here; each domain's own effect-function (armor's hit-probability cap, infantry's RPM/Defence/Morale multipliers) stays in its own package, parameterized by this shared type.

### 3.3 Infantry algorithm (`counters/infantry_calc/formulas.py`)

Ported directly from the spreadsheet's own `QUICK REF` sheet (already a clean, self-documented specification of its own formulas):

```python
WeaponClass = Literal["rifle", "lmg", "hmg", "smg", "at_rifle", "pistol"]

_SUPPRESSION_FACTOR: dict[WeaponClass, float] = {
    "rifle": 1.0, "lmg": 1.4, "hmg": 1.8, "smg": 0.6, "at_rifle": 0.8, "pistol": 0.4,
}

_QUALITY_MULTIPLIERS: dict[Quality, tuple[float, float, float]] = {
    # (BTV, EM, MM) -- Base Training Value, Experience Modifier, Morale Modifier
    "elite":   (1.30, 1.20, 1.20),
    "veteran": (1.15, 1.10, 1.10),
    "regular": (1.00, 1.00, 1.00),   # anchor tier
    "green":   (0.60, 0.90, 0.90),
    "militia": (0.36, 0.81, 0.81),   # extrapolated (see §2), not sourced
}

BASE_K = 47       # normalization divisor; anchor: GREN 43 MG42 LMG -> rFP 7
LOG_BASE = 1.35   # log-compression base
HEX_YDS = 40      # yards per hex at tactical scale
MIN_RFP = 2       # fire lines below this rFP are omitted from the counter

def weapon_rfp(count: int, practical_rpm: float, weapon_class: WeaponClass, quality: Quality) -> int:
    """rFP for one weapon entry on a unit's loadout.

    rFP = MAX(0, ROUND(LOG(qual_adj_rpm / BASE_K) / LOG(LOG_BASE), 0))
    where qual_adj_rpm = count * practical_rpm * suppression_factor(weapon_class) * combined_quality
    and combined_quality = BTV * EM * MM for the given quality tier.

    Source: this project's own infantry-counter-design spreadsheet (v2) --
    a calibrated game-design formula, not a primary military document.
    Anchored to one worked example: GREN 43's MG42 LMG (count=1,
    practical_rpm=300, class=lmg, quality=regular) -> rFP 7, the same role
    Bird & Livingston's worked examples play for armor_calc's sourced
    formulas, just design-authored rather than externally sourced.
    """

def fire_interval_hexes(max_range_yds: float, rfp: int) -> int | None:
    """Interval (hexes) between falloff steps for this weapon's fire line.

    h = MAX(1, ROUND(max_range_hexes / rfp, 0))
    max_range_hexes = ROUND(max_range_yds / HEX_YDS, 0)

    Returns None (printed as "-" on the counter) if rfp is 0.
    """

def unit_defence(manpower: int, quality: Quality) -> tuple[int, int]:
    """(front_defence, rear_defence).

    front = MAX(1, ROUND((manpower / 2) * BTV, 0)) + 3
    rear = MAX(1, front - 2)
    """

def unit_morale(quality: Quality) -> int:
    """Morale = ROUND(((BTV + MM) / 2) * 5, 0) -- identical on front and rear face."""

def quality_multipliers(quality: Quality) -> tuple[float, float, float]:
    """(BTV, EM, MM) for the given tier -- the infantry-domain lookup, parallel
    to armor_calc's crew_quality_hit_cap()."""
```

### 3.4 Data pipeline (`counters/infantry_calc/pipeline.py`)

Mirrors `armor_calc.pipeline`'s exact shape:

- `load_weapons(path: pathlib.Path = DATA_DIR / "weapons.csv") -> list[WeaponRow]` — one row per weapon (name, class, cyclic RPM, practical RPM, max range yards), transcribed from the spreadsheet's weapon entries: MG42 (LMG bipod and HMG tripod variants), Kar98k, Mosin-Nagant, PPSh-41, MP40, DP-28.
- `load_units(path: pathlib.Path = DATA_DIR / "units.csv") -> list[UnitRow]` — one row per unit-variant/face, columns mirroring the spreadsheet's `UNIT ROSTER` sheet: unit ID, nation, unit type, year bracket, face (F/R), quality tier, manpower (full/reduced), weapon loadout (references into `weapons.csv` by name + count), primary source citation, verify status (ANCHOR/PRELIMINARY/CROSS-CHECKED/PRIMARY SOURCE), historical notes. The pilot data is the spreadsheet's existing 12-row roster (German Grenadier/Panzergrenadier/MG42-team, Soviet Guards-rifle/Rifle/DP-28-team, front and rear faces, all 1943), transcribed verbatim including its existing citations.
- `write_infantry_roster_csv(weapons: list[WeaponRow], units: list[UnitRow], out_path: pathlib.Path) -> None` — computes every derived value per unit-face (rFP per weapon class, Defence, Morale, fire-line notation string) and writes `infantry_roster_output.csv`, the same "precomputed reference table" pattern as every `armor_calc` output.

**Implemented and tested** (`counters/quality/tiers.py`: `Quality`, `ALL_QUALITIES`; `armor_calc/formulas.py`: `CrewQuality`/`ALL_CREW_QUALITIES` now alias the shared type, its own 99-test suite unaffected; `infantry_calc/formulas.py`: `weapon_rfp`, `fire_interval_hexes`, `unit_defence`, `unit_morale`, `quality_multipliers`, `suppression_factor`; `infantry_calc/pipeline.py`: `load_weapons`, `load_units`, `write_infantry_roster_csv`, wired into `main()`), cross-checked against the source spreadsheet's own computed values for all 12 pilot-roster rows. 99 total tests passing across `counters/quality/`, `counters/armor_calc/`, and `counters/infantry_calc/`. A real regression was found and fixed during implementation: `armor_calc`'s and `infantry_calc`'s documented pipeline invocation (`python3 -m counters.X.pipeline`) stopped working once `formulas.py` began importing the shared `quality` package via an absolute import requiring `counters/` itself on `sys.path` — corrected to `PYTHONPATH=counters python3 -m X.pipeline` in both packages' docstrings and READMEs.

## 4. Validation approach

1. **Formula validation**: the spreadsheet's own worked example — GREN 43's MG42 LMG (count=1, practical_rpm=300, class=lmg, quality=regular) → `weapon_rfp(...) == 7` — is the first regression test, playing the same role Appendix 15's worked example played for `shot_displacement_m`.
2. **Full-roster cross-check**: all 12 of the spreadsheet's existing roster rows (both faces) get reproduced exactly, since the spreadsheet already shows its own computed rFP/Defence/Morale values for each — this is a real, checkable validation against known-correct output, not a leap of faith.
3. **`armor_calc` regression**: after the `CrewQuality`/`Quality` extraction, `armor_calc`'s full existing test suite (99 tests as of the hit-location merge) must still pass unchanged — confirms the refactor is behavior-neutral.

## 5. Out of scope this phase (explicit, not implied)

- Towed artillery / support guns not mounted on a vehicle (e.g. PAK40, field howitzers) — a future pass reusing `armor_calc`'s existing gun-curve-fitting machinery, not built now.
- Grenades and satchel charges as a *derived* stat — both already resolve via fixed, manually-assigned values (G# on the counter; the Engineer's DEMO capability), not something this system needs to compute from real-world weapon specs.
- Nations/year-brackets beyond the spreadsheet's existing 12-row pilot (Germany and Soviet Union, 1943 only) — scaling to the rest of the roster (other nations, other years, American/British infantry) is future work, same "pilot then scale" shape as the vehicle hit-location system.
- M#/F#/G# derivation — these are manually-assigned design constants in the spreadsheet (defaults 2/2/3, with noted overrides for specialists), not computed from any formula. Ported as flat data, not derived values.

## 6. Open items — flagged honestly, not resolved here

- **Militia tier's BTV/EM/MM (0.36/0.81/0.81) is an extrapolation, not a calibrated value.** No real Militia-tier unit exists in the roster yet to check it against. Worth revisiting once one is added (e.g. late-war Volkssturm, 1941 Soviet opolcheniye).
- **Whether the shared `Quality` core should eventually grow beyond a bare type** (e.g. a shared "which tiers exist and what do they mean narratively" description used by both domains' documentation) is left for whenever a third domain (artillery crews, aircrew, etc.) might want the same tier vocabulary — not needed by only two domains.
- **The spreadsheet's own `AA` column (raw, unrounded rFP) versus the printed rounded rFP**: the spreadsheet preserves the unrounded value ("Amber = raw rFP UNROUNDED — preserve, rounding decisions tracked here") for its own auditability. Whether `infantry_calc` should likewise expose an unrounded intermediate value (not just the final `int`) is left to implementation-time judgment — the plan should decide based on whether any test needs to assert against the unrounded figure the way the spreadsheet's own designer apparently wanted to.
