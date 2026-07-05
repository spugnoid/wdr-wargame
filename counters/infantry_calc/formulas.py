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
