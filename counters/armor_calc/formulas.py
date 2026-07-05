"""Sourced ballistics formulas.

Every formula here is transcribed from one of two sources and cited by
chapter/page so a reviewer can check it against the original:

  - "ww2pen3.pdf" -- John D. Salt's cross-checked compilation of ~50 published
    WW2 penetration sources, plus British WO facing/hit-probability data.
  - "WWII Ballistics: Armor and Gunnery" (Bird & Livingston, 2nd ed.) -- the
    DeMarre equation, slope-multiplier formulas by projectile nose shape,
    cast/face-hardened/high-hardness/flaw multipliers, compound-angle math.

Units: all thicknesses and diameters are in millimetres, velocities in feet
per second (matching the source book's own convention), angles in degrees,
ranges in metres, unless a parameter name says otherwise.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, replace
from typing import Literal

import numpy as np
from numpy.typing import NDArray

from quality.tiers import ALL_QUALITIES, Quality

AmmoFamily = Literal["capped", "apbc", "ap_uncapped", "hvap90", "hvap76", "apds"]


def velocity_at_range(muzzle_velocity_fps: float, k_factor: float, range_m: NDArray | float) -> NDArray:
    """Velocity at range from muzzle velocity and the ballistic K-factor.

    Source: Bird & Livingston Ch.18, p.83.

    Args:
        muzzle_velocity_fps: Muzzle velocity, feet per second.
        k_factor: Ballistic "K" factor for this projectile (source's own table).
        range_m: Range in metres. May be an array.

    Returns:
        Velocity at range, feet per second.
    """
    range_m = np.asarray(range_m, dtype=float)
    result: NDArray = muzzle_velocity_fps * np.exp(range_m * 0.7 * -0.0000001 * k_factor)
    return result


def flight_time(muzzle_velocity_fps: float, k_factor: float, range_m: float) -> float:
    """Approximate flight time to range: range / average of muzzle and terminal velocity.

    A first-order approximation (true flight time integrates velocity over
    the whole trajectory), but sufficient to unify the hit-probability model
    below across guns of very different velocity -- see base_hit_probability().
    """
    v_range = float(velocity_at_range(muzzle_velocity_fps, k_factor, range_m))
    v_avg_ms = (muzzle_velocity_fps + v_range) / 2 / 3.2808  # fps -> m/s
    return range_m / v_avg_ms


# Fitted from Bird & Livingston Appendix 17 (British O.B. Investigation No.659,
# 28 Dec '44): first-shot Head-On (~stationary-target) hit% for 75mm APCBC,
# 17pdr APCBC, and 6pdr APCBC at 400/800/1200/1600/2000 yards -- 15 points
# total. Plotted against flight time (not range), these collapse cleanly onto
# one monotonic curve across all three guns despite very different
# velocities, confirming the source's own claim that flight time is the
# unifying variable. Fit: Hit% = 100 * exp(-(flight_time/tau)^p). Mean
# absolute error across the 15 calibration points: 5.7 percentage points
# (max 12.4pp) -- reasonable given the source's own data reflects genuine
# crew-performance variability, not a clean physical law.
_HIT_PCT_TAU = 1.4785
_HIT_PCT_P = 2.3483


def base_hit_probability(flight_time_s: float) -> float:
    """First-shot hit probability (%) against a stationary/head-on target,
    before crew-quality cap or target-movement modifier.

    Universal across guns -- see module comment above _HIT_PCT_TAU.
    """
    return 100.0 * np.exp(-(flight_time_s / _HIT_PCT_TAU) ** _HIT_PCT_P)


# CrewQuality is armor_calc's name for the shared Quality tier vocabulary --
# kept as an alias so existing armor_calc code and tests don't need to
# change any import. See counters/quality/tiers.py for what's actually
# shared vs. what stays domain-specific.
CrewQuality = Quality

# Source: Bird & Livingston Ch.6/Appendix 7. Caps maximum hit probability by
# crew quality, modelling human factors (fear, fatigue, stress) that a pure
# ballistic dispersion model doesn't capture, particularly at short range.
_CREW_QUALITY_HIT_CAP: dict[CrewQuality, float] = {
    "elite": 0.90,
    "veteran": 0.85,  # "Experienced" (0.80 in the source) has no separate
    "regular": 0.75,  # band here -- folded into Veteran, since the game's
    "green": 0.65,  # Morale stat is integer-valued and doesn't have room
    "militia": 0.50,  # for a sixth tier without new granularity.
}


def crew_quality_hit_cap(quality: CrewQuality) -> float:
    """Maximum hit probability (0-1) for this crew-quality tier."""
    return _CREW_QUALITY_HIT_CAP[quality]


ALL_CREW_QUALITIES: tuple[CrewQuality, ...] = ALL_QUALITIES


def crew_quality_from_morale(morale: int) -> CrewQuality:
    """Maps the game's existing Morale stat to a crew-quality hit-cap tier.

    Design choice (not sourced): Elite=Morale 7+, Veteran=6, Regular=5,
    Green=3-4, Militia<=2. Reuses the stat already printed on every unit
    rather than adding a new field.
    """
    if morale >= 7:
        return "elite"
    if morale == 6:
        return "veteran"
    if morale == 5:
        return "regular"
    if morale >= 3:
        return "green"
    return "militia"


# Source: Bird & Livingston Appendix 17 p.121, "ratio of Direct-Crosser% /
# Head-On%" -- nearly gun-independent (checked across 75mm/17pdr/6pdr APCBC,
# which agree within a few percentage points at every range), so this is one
# universal table rather than a per-gun one, same pattern as the HEAT
# reference table. Keyed by range in metres (source gives yards).
_YD_TO_M = 0.9144
_CROSSING_RATIO_FIRST_SHOT: dict[float, float] = {
    400 * _YD_TO_M: 0.91,
    800 * _YD_TO_M: 0.57,
    1200 * _YD_TO_M: 0.46,
    1600 * _YD_TO_M: 0.37,
    2000 * _YD_TO_M: 0.37,
}
_CROSSING_RATIO_FOLLOWUP: dict[float, float] = {
    400 * _YD_TO_M: 0.99,
    800 * _YD_TO_M: 0.80,
    1200 * _YD_TO_M: 0.61,
    1600 * _YD_TO_M: 0.53,
    2000 * _YD_TO_M: 0.48,
}


def crossing_target_ratio(range_m: float, follow_up: bool = False) -> float:
    """Multiplier for a target crossing the line of fire vs. standing still
    or closing/receding directly. Source: Appendix 17 p.121. Interpolated
    linearly between the source's own range bands; clamped at the ends.

    A crossing target is never as easy to hit as a stationary one even with
    unlimited ranging shots -- the follow-up-shot ratio bottoms out around
    0.48-0.53 at 1600-2000 yards rather than approaching 1.0.
    """
    table = _CROSSING_RATIO_FOLLOWUP if follow_up else _CROSSING_RATIO_FIRST_SHOT
    ranges = sorted(table)
    r = min(max(range_m, ranges[0]), ranges[-1])
    lo = max(x for x in ranges if x <= r)
    hi = min(x for x in ranges if x >= r)
    if lo == hi:
        return table[lo]
    frac = (r - lo) / (hi - lo)
    return table[lo] + frac * (table[hi] - table[lo])


def hit_probability(
    muzzle_velocity_fps: float,
    k_factor: float,
    range_m: float,
    quality: CrewQuality,
    crossing: bool = False,
    follow_up: bool = False,
) -> float:
    """Fully resolved hit probability (%) for one shot: base flight-time
    curve, crew-quality cap, and target-crossing modifier if applicable.

    Does not include wind/drift or trunnion cant (Appendix 7/8) -- both are
    first-shot-only effects too small to matter at this game's 40-yard hex
    scale (largest wind/drift offset found was 0.64m at ~1000 yards),
    deliberately omitted rather than modelled.
    """
    ft = flight_time(muzzle_velocity_fps, k_factor, range_m)
    pct = min(base_hit_probability(ft), crew_quality_hit_cap(quality) * 100)
    if crossing:
        pct *= crossing_target_ratio(range_m, follow_up)
    return pct


# ----------------------------------------------------------------------------
# Unification: one 1d6+1d8+1d12 roll resolves Miss / Hit-Turret / Hit-Hull.
#
# The game's fire combat already rolls this exact combination for every other
# attack (design note E.7) and Appendix C already publishes its full 576-
# outcome probability table -- reusing it here means no new dice, and reuses
# a distribution the game already characterizes precisely. Design spec §11.
# ----------------------------------------------------------------------------


def _dice_sum_cdf_at_least() -> dict[int, float]:
    """P(1d6+1d8+1d12 >= s) for every possible sum s (3-26), computed once
    from the full 576-outcome enumeration (not approximated)."""
    from itertools import product

    counts: dict[int, int] = {}
    for a, b, c in product(range(1, 7), range(1, 9), range(1, 13)):
        s = a + b + c
        counts[s] = counts.get(s, 0) + 1
    total = sum(counts.values())
    running = 0.0
    result: dict[int, float] = {}
    for s in sorted(counts, reverse=True):
        running += counts[s] / total
        result[s] = running
    return result


_DICE_CDF_GE = _dice_sum_cdf_at_least()
_DICE_MIN, _DICE_MAX = min(_DICE_CDF_GE), max(_DICE_CDF_GE)


def roll_threshold_for_probability(target_pct: float) -> int | None:
    """The smallest 1d6+1d8+1d12 sum R such that P(roll >= R) does not
    exceed target_pct/100 -- i.e. "roll >= R" happens with probability as
    close to (and not exceeding) target_pct as this dice combination allows.

    Returns the minimum possible roll (3) if target_pct is so high that even
    the worst roll clears it (effectively "always"), or None if target_pct
    is below what even the best possible roll (26, ~0.17%) can represent --
    i.e. genuinely un-hittable at this dice combination's resolution, which
    should read as an automatic miss rather than a very-high-number-needed
    roll. There are only 24 distinct achievable thresholds (3-26), so a
    requested probability is rounded to the nearest one the dice can express,
    same rounding tradeoff as any discrete-dice probability model.
    """
    target = target_pct / 100.0
    if target >= _DICE_CDF_GE[_DICE_MIN]:
        return _DICE_MIN
    if target < _DICE_CDF_GE[_DICE_MAX]:
        return None
    for s in sorted(_DICE_CDF_GE):
        if _DICE_CDF_GE[s] <= target:
            return s
    return None  # pragma: no cover -- unreachable given the bounds checks above


def hull_turret_split(range_m: float) -> tuple[float, float]:
    """(turret_fraction, hull_fraction) of hits landing on turret vs. hull,
    GIVEN that the shot hits at all. Sums to 1.0.

    Rough first pass (design spec §10/§13): extends the Ch.11 Panther-mantlet
    finding that hits bunch on hull at short range (tight dispersion near a
    center-mass aim point) and spread toward the turret as range grows
    (wider dispersion). Two-band model, not a continuous curve -- the
    source data behind it is one gun/scenario, not enough to justify a
    finer curve without more data.
    """
    if range_m <= 150.0:  # roughly the tactical-scale "short range" (~4 hexes)
        return (1 / 6, 5 / 6)
    return (2 / 6, 4 / 6)


@dataclass(frozen=True)
class VehicleFireThresholds:
    """The two numbers printed for a shot: roll the 1d6+1d8+1d12 sum against
    them to resolve Miss / Hit-Turret / Hit-Hull in one roll.

    Attributes:
        miss_threshold: Roll < this = miss. None if even the best possible
            roll can't hit (automatic miss -- e.g. far beyond effective range).
        hull_threshold: Roll >= this = hull. Between miss_threshold and this
            (exclusive) = turret. None if no roll can reach the hull band
            specifically (every hit that can occur lands on the turret).
    """

    miss_threshold: int | None
    hull_threshold: int | None


def vehicle_fire_thresholds(
    muzzle_velocity_fps: float,
    k_factor: float,
    range_m: float,
    quality: CrewQuality,
    crossing: bool = False,
    follow_up: bool = False,
) -> VehicleFireThresholds:
    """Fully resolved Miss/Turret/Hull thresholds for one shot, ready to
    compare against a single 1d6+1d8+1d12 roll.
    """
    hit_pct = hit_probability(muzzle_velocity_fps, k_factor, range_m, quality, crossing, follow_up)
    _, hull_frac = hull_turret_split(range_m)
    miss_t = roll_threshold_for_probability(hit_pct)
    hull_t = roll_threshold_for_probability(hit_pct * hull_frac)
    return VehicleFireThresholds(miss_threshold=miss_t, hull_threshold=hull_t)


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


def compound_angle(vertical_deg: float, lateral_deg: float) -> float:
    """Single effective impact angle from vertical slope and lateral (traverse) angle.

    Source: Bird & Livingston Ch.12, p.45.

    Args:
        vertical_deg: Plate's slope from vertical, degrees. 0 = vertical plate.
        lateral_deg: Angle off the attacker's line of fire, degrees. 0 = dead-on.

    Returns:
        Compound impact angle, degrees, for use in the slope-multiplier formulas.
    """
    v = np.radians(vertical_deg)
    l = np.radians(lateral_deg)
    return float(np.degrees(np.arccos(np.cos(v) * np.cos(l))))


def heat_multiplier(angle_deg: NDArray | float) -> NDArray | float:
    """HEAT (shaped-charge) slope multiplier: a clean secant law, no T/D or
    armor-quality dependence.

    Source: Bird & Livingston Ch.2, p.16. "HEAT is the only WW II ammunition
    where slope effects appear to follow the T/Cosine equation" -- validated
    against the chapter's own angle-only reference curve (e.g. 3.9x at
    75deg, matching 1/cos(75deg)=3.86).

    This is also the fix for Rule 17.2.6's current error: HEAT is immune to
    RICOCHET at extreme angle (a shaped-charge jet doesn't bounce the way a
    kinetic round does), but it is NOT immune to this slope-effect loss --
    those are two different claims the current rule conflates.

    No cast/face-hardened/high-hardness/flaw correction is applied here --
    the source describes HEAT jet penetration as having "much weaker
    sensitivity" to armor quality than kinetic nose-shatter/plugging
    failure modes, and models it as a function of raw thickness and angle
    only. Does not account for spaced-armor/schurzen standoff disruption,
    which affects HEAT differently than kinetic rounds -- a separate,
    not-yet-designed interaction (design spec §7/§12).

    Args:
        angle_deg: Compound impact angle, degrees.

    Returns:
        Multiplier to convert raw thickness at this angle into
        0-degree-equivalent resistance against HEAT.
    """
    return 1.0 / np.cos(np.radians(angle_deg))


def heat_effective_resistance(thickness_mm: float, vertical_deg: float, lateral_deg: float = 0.0) -> float:
    """0-degree-equivalent resistance against HEAT, from raw thickness and angle.

    Deliberately takes only thickness and angle -- no projectile diameter,
    no cast/hardness/flaw corrections -- see heat_multiplier() for why.
    """
    angle = compound_angle(vertical_deg, lateral_deg)
    return float(thickness_mm * heat_multiplier(angle))


def heat_reference_table(angle_bands_deg: tuple[float, ...] = (0, 15, 30, 45, 60, 75)) -> list[tuple[float, float]]:
    """The small universal HEAT reference table meant for the player aid card.

    One table for the whole game -- unlike AV-vs-Capped/AV-vs-Tungsten,
    HEAT needs no per-vehicle column, just this angle->multiplier lookup
    applied to a vehicle's already-printed raw thickness.
    """
    return [(a, float(heat_multiplier(a))) for a in angle_bands_deg]


def _capped_kinetic_fg(angle_deg: NDArray) -> tuple[NDArray, NDArray]:
    """F, G coefficients for APCBC/APC (capped kinetic) nose shape.

    Source: Bird & Livingston Ch.2, p.20-21. Piecewise by compound angle.
    """
    a = np.asarray(angle_deg, dtype=float)
    f = np.zeros_like(a)
    g = np.zeros_like(a)

    m1 = a <= 55
    f[m1] = np.exp(0.0000408 * a[m1] ** 2.5)
    g[m1] = 0.0101 * np.exp(0.1313 * a[m1] ** 0.8)

    m2 = (a > 55) & (a <= 60)
    f[m2] = -3.434 + 0.10856 * a[m2]
    g[m2] = 0.2174 + 0.00046 * a[m2]

    m3 = (a > 60) & (a <= 70)
    f[m3] = 0.00000518 * a[m3] ** 3.25
    g[m3] = 0.00002123 * a[m3] ** 2.295

    m4 = a > 70
    f[m4] = 0.0678 * 1.0634**a[m4]
    g[m4] = 0.1017 * 1.0178**a[m4]

    return f, g


def _apbc_fg(angle_deg: NDArray) -> tuple[NDArray, NDArray]:
    """F, G coefficients for APBC (blunt-nose / Soviet-style) nose shape.

    Source: Bird & Livingston Ch.2, p.20-21. Piecewise by compound angle.

    Confidence note: cross-validated well at low-mid angle against the
    chapter's own rough graph-reading description; one specific spot check
    (55deg, T/D=0.9) disagreed by nearly 2x against that same rough reading
    (equation: 1.95, graph-reading: ~3.6). The equation is internally
    continuous across its own piecewise boundaries (checked at 55 and 60
    degrees, both agree within ~2%), so it is used here as the more
    trustworthy of the two, but the 45-60deg band deserves a direct
    page spot-check before being treated as final for any specific vehicle.
    """
    a = np.asarray(angle_deg, dtype=float)
    f = np.zeros_like(a)
    g = np.zeros_like(a)

    m1 = a <= 55
    f[m1] = np.exp(0.019925 * 1.06758**a[m1])
    g[m1] = 0.007012 * 1.08289**a[m1]

    m2 = (a > 55) & (a <= 60)
    f[m2] = np.exp(0.002542 * 1.1089**a[m2])
    g[m2] = 0.0004763 * 1.1373**a[m2]

    m3 = a > 60
    f[m3] = np.exp(0.03723 * 1.06033**a[m3])
    g[m3] = -3.3667 + 0.07411 * a[m3]

    return f, g


def _ap_uncapped_fg(angle_deg: NDArray) -> tuple[NDArray, NDArray]:
    """F, G coefficients for uncapped AP (solid shot, no ballistic/AP cap).

    Source: Bird & Livingston Ch.2, p.20-21 (PDF48-49). Distinct from
    "capped" (APCBC/APC): uncapped rounds lack the cap that protects the
    nose against cracking/deflection, giving them different (generally
    lower at moderate angle) slope multipliers.

    Cross-validated against Appendix 9 (p.103-105), which tabulates the
    book's own computed "0 degree armor" figures for real 17pdr/6pdr AP
    firing tests against Tiger E armor -- 4 independent points, all inside
    the <=40deg band used here, matched to within 2% (82mm/57mm@20deg:
    89.5mm vs. table's 90mm; 102mm/57mm@10deg: 102.8mm vs. 103mm;
    102mm/76.2mm@25deg: 119.8mm vs. 119mm; 100mm/57mm@21deg: 113.5mm vs.
    114mm). The 40-55deg and 55-65deg bands are transcribed verbatim from
    the source but have no worked example in this project's range to check
    against -- treat them as sourced-but-unconfirmed. There is also a real
    discontinuity in G (not just F) at the 40deg band boundary already
    present in the source's own two separate formulas (e.g. at T/D=1.4 the
    multiplier jumps from ~1.82 to ~1.66 crossing 40deg) -- a genuine
    characteristic of the source material, not a transcription error.
    Beyond 65deg the source gives no AP data at all; this function
    extrapolates the 55-65deg formula rather than raising, matching the
    extrapolate-past-the-last-band pattern used by the other nose-shape
    families below.
    """
    a = np.asarray(angle_deg, dtype=float)
    f = np.zeros_like(a)
    g = np.zeros_like(a)

    m1 = a <= 40
    f[m1] = 0.95 * np.exp(0.0000539 * a[m1] ** 2.5)
    g[m1] = 0.04433 * np.exp(0.04867 * a[m1])

    m2 = (a > 40) & (a <= 55)
    f[m2] = 0.04754 * a[m2] ** 0.953
    g[m2] = 0.02047164 * a[m2] ** 0.46471

    m3 = a > 55
    f[m3] = 0.0001675 * a[m3] ** 2.3655
    g[m3] = 0.02047164 * a[m3] ** 0.46471

    return f, g


def slope_multiplier(angle_deg: NDArray | float, td_ratio: NDArray | float, family: AmmoFamily) -> NDArray:
    """0-degree-equivalent slope multiplier for a given ammo nose shape.

    Source: Bird & Livingston Ch.2 (capped/APBC/uncapped AP) and Appendix 16
    (tungsten). Uncapped AP cross-validated against Appendix 9.

    Tungsten families (hvap90, hvap76, apds) have no T/D dependence -- only
    three curves are sourced (90mm HVAP, 76mm HVAP, and APDS, the last
    stated as calibre-independent). Any other tungsten round (German/Soviet
    APCR on other calibres) must borrow the closest analog; this is a
    modelling limitation of the source material, not of this function.

    Args:
        angle_deg: Compound impact angle, degrees.
        td_ratio: Target thickness / projectile diameter. Ignored for
            tungsten families.
        family: Which nose-shape curve family to use.

    Returns:
        Multiplier to convert real thickness at this angle into
        0-degree-equivalent resistance.
    """
    a = np.asarray(angle_deg, dtype=float)
    result: NDArray
    if family == "capped":
        f, g = _capped_kinetic_fg(a)
        result = f * np.asarray(td_ratio, dtype=float) ** g
    elif family == "apbc":
        f, g = _apbc_fg(a)
        result = f * np.asarray(td_ratio, dtype=float) ** g
    elif family == "ap_uncapped":
        f, g = _ap_uncapped_fg(a)
        result = f * np.asarray(td_ratio, dtype=float) ** g
    elif family == "hvap90":
        result = np.where(a <= 30, 1.0 * np.exp((a**1.75) * 0.000662), 0.9043 * np.exp((a**2.20) * 0.0001987))
    elif family == "hvap76":
        result = np.where(a <= 25, 1.0 * np.exp((a**2.20) * 0.0001727), 0.7277 * np.exp((a**1.50) * 0.003787))
    elif family == "apds":
        result = 1.0 * np.exp((a**2.60) * 0.00003011)
    else:
        raise ValueError(f"Unknown ammo family: {family!r}")
    return result


def effective_0deg_resistance(
    thickness_mm: NDArray | float,
    diameter_mm: float,
    angle_deg: NDArray | float,
    family: AmmoFamily = "capped",
) -> NDArray:
    """Real plate at an angle -> 0-degree-equivalent resistance, slope only.

    Does not apply cast/face-hardened/high-hardness/flaw corrections --
    chain with cast_deficiency_multiplier() and high_hardness_multiplier()
    as appropriate. See §3.2/§7 of the design spec for why these are
    separate steps.
    """
    t = np.asarray(thickness_mm, dtype=float)
    td = t / diameter_mm
    return t * slope_multiplier(angle_deg, td, family)


def layered_plate_effective_thickness(first_hit_mm: float, underlying_mm: float) -> float:
    """Single-plate-equivalent thickness for two homogeneous plates bolted or
    welded together in contact (not spaced apart -- see the Ch.9 spaced-armor
    equations for that separate case).

    Source: Bird & Livingston Ch.9 p.38. Regression fit to three real test
    points (Sherman 38mm+38mm applique, Navy 3in-over-1in and 1in-over-3in
    deck plate). Validated against all three of the chapter's own worked
    examples this session: Sherman 38mm+38mm -> 57.7mm (book states 58mm),
    T-34 15mm-scrap-over-45mm -> 49.5mm (book states ~50mm, floor-limited),
    KV-1 30mm-over-75mm -> 92.0mm (book states 92mm) -- all within rounding.

    Preferred over the chapter's own alternative "Okun equation" (also
    given, p.39) because the book's own three-way comparison table shows
    this formula matching the real test data more closely than either the
    Okun equation or the "Naval rule of thumb" simplification.

    Args:
        first_hit_mm: Thickness of the plate the projectile reaches first, mm.
        underlying_mm: Thickness of the plate behind it, mm.

    Returns:
        Single-plate-equivalent thickness, mm -- feed this into
        effective_0deg_resistance() etc. as if it were one plate's raw
        thickness. Clamped between the source's own stated floor (0.3x the
        thinner plate, plus the thicker plate) and ceiling (96% of the
        combined total thickness).
    """
    t1, t2 = first_hit_mm, underlying_mm
    plate_ratio = t1 / t2
    max_thickness = max(t1, t2)
    multiplier = 0.3129 * plate_ratio**0.02527 * max_thickness**0.2439
    raw = multiplier * (t1 + t2)
    floor = 0.3 * min(t1, t2) + max(t1, t2)
    ceiling = 0.96 * (t1 + t2)
    return max(floor, min(raw, ceiling))


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
    one equation-based worked example (dice=66, hit=85% -> 0.7m) -- see
    test_formulas.py::TestShotDisplacement. (The book also gives
    dice=22/50 @ ~95% examples, but those are computed via its separate
    discrete lookup table, not this equation, so they don't apply here.)

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
    """Return the first zone (in list order) whose bounding box contains
    (x, y), or None if no zone does.

    If zones overlap, list order is the tie-break: earlier zones in the
    list take precedence. Callers authoring zone geometry should keep
    zones non-overlapping where possible rather than relying on this.
    """
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


def cast_deficiency_multiplier(thickness_mm: float, diameter_mm: float) -> float:
    """Cast armor's resistance deficiency relative to rolled homogeneous armor.

    Source: Bird & Livingston Ch.5, p.26.

    Args:
        thickness_mm: Real (cast) plate thickness, mm.
        diameter_mm: Attacking projectile diameter, mm.

    Returns:
        Multiplier (typically < 1.0) to apply to a cast plate's slope-adjusted
        resistance. Only apply to cast armor -- do not apply to rolled plate.
    """
    t, d = thickness_mm, diameter_mm
    return 0.8063 + t * 0.001238 - 0.0002628 * d + (t / d) * 0.02706


def high_hardness_multiplier(thickness_mm: float, diameter_mm: float, bhn: float) -> float:
    """High-hardness armor's resistance relative to ~240 BHN standard test plate.

    Source: Bird & Livingston Ch.4, p.24. Loses resistance when the plate is
    overmatched by the projectile diameter (T/D << 1); gains resistance when
    it isn't (T/D >= ~1) -- this is a real crossover, not a bug, and was
    validated against the source's own T-34-vs-75mm-APCBC worked example
    (122mm slope-adjusted x 0.766 = 93.7mm, source states 0.76 -> 93mm).

    Args:
        thickness_mm: Real plate thickness, mm.
        diameter_mm: Attacking projectile diameter, mm.
        bhn: Plate's actual Brinell Hardness Number.

    Returns:
        Multiplier to apply to the plate's slope-adjusted (and, if cast,
        cast-corrected) resistance.
    """
    t, d = thickness_mm, diameter_mm
    return 0.01 * 977.07 * d**0.06111 * (t / d) ** 0.2821 * bhn**-0.4363


# Ch.4 p.24 (opening paragraph, before the multiplier equation itself):
# "Armor hardnesses below 375 Brinell Hardness Number (BHN) are normally
# referred to as machineable quality and are expected to have reasonable
# impact resistance, allowing them to stand up to repeated hits by large
# projectiles without cracking or spalling. When hardness equals or exceeds
# about 375 BHN, armor becomes brittle and loses resistance..." -- i.e. the
# whole high-hardness apparatus above is the book's own explicit answer to
# a brittleness phenomenon that, by its own definition, doesn't occur below
# 375 BHN. This was discovered as the root cause of a real discrepancy: Tiger
# E's own measured hardness (310-340 BHN, Appendix 9) had been evaluated
# through this formula and gave a 9-21% resistance bonus at the T/D values
# Appendix 9's own guns (57mm/76.2mm) create, well above the source's own
# qualitative estimate for Tiger ("1% to 3% additional penetration
# required") -- while the formula itself independently matches the source's
# own BHN=450/460 worked examples and precomputed table exactly. The gap is
# explained by this: 310-340 BHN is below the formula's own stated domain,
# so applying it there is extrapolation into a regime the book itself says
# behaves differently (ordinary "reasonable impact resistance", not the
# brittle-fracture-driven curve this equation encodes).
_HIGH_HARDNESS_MIN_BHN = 375.0


def high_hardness_applies(bhn: float) -> bool:
    """Whether high_hardness_multiplier() is being evaluated within its
    sourced domain (see _HIGH_HARDNESS_MIN_BHN's comment) for this plate's
    hardness.

    ArmorPlate.av_vs() uses this as a gate: below 375 BHN, no correction is
    applied at all (multiplier effectively 1.0) rather than extrapolating a
    brittle-fracture curve onto armor the source's own text says isn't in
    that regime. This affects two previously-computed roster figures that
    both turn out to have used a BHN below this threshold: Tiger E's
    side/rear armor (bhn_override=320) and T-34/85's redesigned turret
    (300 BHN per the Soviet hardness table's 81mm+ bracket) -- both lose
    their previously-applied high-hardness bonus once this guard is in
    place. See design spec for the full writeup of this finding, including
    what does and doesn't survive it.
    """
    return bhn >= _HIGH_HARDNESS_MIN_BHN


FlawSeverity = Literal["small", "medium", "large"]

# Source: Bird & Livingston Ch.6, p.28-29. The chapter's own graphs give only
# two anchor points per (severity, angle) curve: the multiplier at T/D=0.1,
# and the T/D at which the curve converges to 1.00 (full resistance, flaw
# no longer matters once the round isn't badly overmatching the plate).
# Linear interpolation between those two points was cross-validated against
# two of the chapter's own worked Panther-glacis examples (medium flaws,
# ~55deg): predicted 0.827 vs. stated 0.825 at T/D=0.559 (152mm APBC), and
# predicted 0.945 vs. stated 0.95 at T/D=1.115 (17pdr APCBC) -- both within
# ~1%, which is why linear interpolation (rather than a fitted curve) is
# used here instead of trying to over-fit two sparse data points.
#
# "large" severity's convergence point is only precisely sourced at 0deg
# ("converges fastest", ~1.05-1.1) and 60/75deg ("still <1.0 even at
# T/D=1.5" -- the 1.8 used below for those two cells is an unsourced
# placeholder, not a real figure). The 30deg convergence (1.3) is this
# module's own interpolation guess between those two, and it can make
# "large" cross over and read as LESS severe than "medium" at some T/D
# values near 30deg -- a real, known gap in the sparse source data, not
# hidden: see test_large_more_severe_than_small_at_source_anchor_point.
_FLAW_ANCHORS: dict[FlawSeverity, dict[float, tuple[float, float]]] = {
    # severity -> angle_deg -> (multiplier at T/D=0.1, T/D at which mult reaches 1.00)
    "small": {0: (0.88, 1.35), 30: (0.86, 1.35), 60: (0.855, 1.35), 75: (0.845, 1.35)},
    "medium": {0: (0.775, 1.375), 30: (0.75, 1.375), 60: (0.73, 1.375), 75: (0.705, 1.375)},
    "large": {0: (0.90, 1.075), 30: (0.75, 1.3), 60: (0.70, 1.8), 75: (0.60, 1.8)},
}
_FLAW_ANGLES = sorted(_FLAW_ANCHORS["small"])


def flaw_multiplier(thickness_mm: float, diameter_mm: float, angle_deg: float, severity: FlawSeverity) -> float:
    """Resistance multiplier for armor with documented quality flaws (cracks,
    material defects -- distinct from cast deficiency or high-hardness).

    Source: Bird & Livingston Ch.6. See module-level `_FLAW_ANCHORS` comment
    for the cross-validation against real Panther-glacis worked examples.
    Only meaningful where a specific flaw problem is actually documented for
    the plate in question (e.g. Panther glacis, pre-Oct-1943 Sherman glacis)
    -- do not apply to plate with no known flaw history.

    Args:
        thickness_mm: Real plate thickness, mm.
        diameter_mm: Attacking projectile diameter, mm.
        angle_deg: Compound impact angle, degrees. Interpolated between the
            source's own 0/30/60/75 degree data points.
        severity: "small", "medium", or "large" flaw severity.

    Returns:
        Multiplier (<=1.0) to apply to the plate's slope-adjusted resistance.
    """
    td = thickness_mm / diameter_mm
    angle_deg = min(max(angle_deg, _FLAW_ANGLES[0]), _FLAW_ANGLES[-1])
    lo = max(a for a in _FLAW_ANGLES if a <= angle_deg)
    hi = min(a for a in _FLAW_ANGLES if a >= angle_deg)
    frac = 0.0 if hi == lo else (angle_deg - lo) / (hi - lo)

    def _mult_at(a: float) -> float:
        min_mult, td_conv = _FLAW_ANCHORS[severity][a]
        if td <= 0.1:
            return min_mult
        if td >= td_conv:
            return 1.0
        return min_mult + (td - 0.1) / (td_conv - 0.1) * (1.0 - min_mult)

    return _mult_at(lo) + frac * (_mult_at(hi) - _mult_at(lo))


# ----------------------------------------------------------------------------
# Shatter gap (Ch.7, p.29-33): a round with enough kinetic energy to badly
# over-penetrate a plate can shatter its own nose against the armor before
# completing penetration -- a real, counter-intuitive failure mode where a
# shot that "should" penetrate by a comfortable margin instead fails.
# ----------------------------------------------------------------------------

_SHATTER_GAP_LOWER_RATIO = 1.06
_SHATTER_GAP_UPPER_RATIO = 1.22

# Ch.7 p.30: "shatter gap failure would be expected to occur with Russian,
# British, Italian and American steel projectiles" -- i.e. every steel
# kinetic nose shape (capped, uncapped AP, and Soviet-style APBC), not just
# APCBC. Tungsten/APDS are excluded: Appendix 9 p.104 notes APDS failures in
# this same test program did NOT follow this ratio threshold ("may be due
# to excessive angle between nose and flight path... possibility also
# exists that APDS shatter fails... which have not been determined") -- a
# real but different, unsourced failure mode. HEAT has no kinetic nose at
# all and is out of scope by construction (no AmmoFamily value represents
# it in this module).
_SHATTER_ELIGIBLE_FAMILIES: frozenset[str] = frozenset({"capped", "apbc", "ap_uncapped"})


def shatter_gap_window(av_mm: float) -> tuple[float, float]:
    """The PEN range (mm) in which a shot against this AV shatter-fails
    despite nominally over-penetrating.

    Source: Bird & Livingston Ch.7 p.33 (the chapter's final recommended
    thresholds, superseding an earlier, looser p.31 estimate): "Normal
    penetration up to penetration/resistance ratio of 1.05; shatter gap
    failure from 1.06 to 1.22; shatter penetration [succeeds despite
    shattering] when the ratio exceeds 1.22."

    Validated against two of the chapter's own worked examples: Tiger E
    driver plate (100mm@10deg, AV=103mm per the source's own figure) ->
    window (109.2, 125.7), source states "109mm to 126mm"; Panther mantlet
    (100mm cast @10deg, AV=98mm) -> upper bound 119.6, source states
    "120mm". Also matches a real Appendix 9 firing-test row directly: 17pdr
    APCBC at 82mm/50deg Tiger side armor (AV=82mm), 87mm penetration
    (ratio 1.061, just inside this window) -> actual test result "No
    Pen.", consistent with a shatter-gap failure.
    """
    return av_mm * _SHATTER_GAP_LOWER_RATIO, av_mm * _SHATTER_GAP_UPPER_RATIO


def shatter_gap_failure(pen_mm: float, av_mm: float, family: AmmoFamily) -> bool:
    """Whether this shot fails to penetrate due to shatter gap, despite
    pen_mm >= av_mm (an "over-penetration" a naive PEN-vs-AV comparison
    alone would call a success).

    Only checks the penetration/resistance ratio and ammo family (see
    _SHATTER_ELIGIBLE_FAMILIES above) -- it does NOT independently check
    the source's other two stated conditions, T/D ratio >= 0.8 and impact
    velocity >= 2000fps. T/D is handled at the table instead, as a
    caliber-vs-AV comparison using numbers already on both counters (see
    design spec) rather than a formula here. The velocity condition is
    treated as usually implied whenever PEN is this far above AV -- a shot
    only gets deep into over-penetration territory at the higher-velocity,
    closer-range end of a gun's curve -- which is a simplifying assumption
    for this game's roster, not an independently confirmed fact for every
    gun/range combination.
    """
    if family not in _SHATTER_ELIGIBLE_FAMILIES:
        return False
    lower, upper = shatter_gap_window(av_mm)
    return lower <= pen_mm <= upper


def heat_pen_vs_schurzen(pen_mm: float) -> float:
    """Attacking HEAT round's effective PEN after passing through Schürzen
    (standoff skirt armor) before reaching the real armor.

    NOT sourced from Bird & Livingston or John D. Salt's compilation --
    both were searched and neither covers HEAT-vs-spaced-armor interaction
    at all (confirmed this session; the project's other formulas are all
    cited to one of those two). This is general, well-established
    shaped-charge engineering knowledge instead: a HEAT round's jet needs a
    specific standoff distance from the target to fully form before it
    reaches peak penetration, and most WW2-era HEAT munitions were fuzed
    (often via a nose standoff probe/spike) to detonate at close to their
    own optimal distance already. Schürzen forces the jet to begin forming
    tens of centimetres earlier than the round's own fuze intended, so by
    the time it reaches the real armor the jet has traveled well past its
    optimal coherence distance and has begun to disperse -- reducing
    penetration substantially, though the effect is highly dependent on
    the specific round's own standoff design and is not a fixed physical
    constant the way the DeMarre/slope-multiplier formulas are.

    The 0.5 factor used here matches a long-standing wargame-design
    convention (e.g. Advanced Squad Leader's own Side Skirts vehicle note)
    rather than a specific measured figure -- flagged as medium confidence,
    a design convention grounded in real (if variable) physics, not a
    citation-backed number the way the rest of this module's formulas are.

    Does not apply to kinetic (capped/apbc/ap_uncapped/tungsten) rounds --
    Ch.9's own sourced finding is that thin spaced plates ahead of the main
    armor give no defensive benefit against kinetic penetrators (if
    anything, a slight resistance *penalty* vs. solid armor of the same
    combined thickness) -- a completely different mechanism from HEAT's
    jet-formation dependency. Schürzen is HEAT-only in this system.
    """
    return pen_mm * 0.5


def shatter_gap_reference_table(
    av_bands_mm: tuple[float, ...] = tuple(float(x) for x in range(30, 201, 10)),
) -> list[tuple[float, float, float]]:
    """The small universal Shatter Gap reference table for the advanced-rule
    player aid: AV -> (lower, upper) PEN thresholds.

    One table for the whole game, not a per-vehicle column -- consistent
    with the HEAT reference table's reasoning (design spec) and doubly so
    here since this is an optional/advanced module most games won't use.
    Round a target's AV to the nearest listed band: the source's own
    recommendation is already an average-case approximation ("these
    recommendations are based on average values, variations will occur"),
    so resolving finer than a 10mm band isn't meaningful.
    """
    return [(av, *shatter_gap_window(av)) for av in av_bands_mm]


# ----------------------------------------------------------------------------
# Face-hardened armor (Ch.3, p.21-23): a thin (2.5-5mm) surface layer hardened
# to 450-650 BHN over an otherwise homogeneous (220-300 BHN) core. Defeats
# early-war UNCAPPED AP by shattering the projectile nose before it digs in --
# a real bonus over homogeneous plate of the same thickness. Once capped
# ammunition (APC/APCBC) became standard, the advantage reversed: the cap
# protects the nose from shattering, and face-hardened plate performs WORSE
# than homogeneous plate of the same thickness against it. Slope-multiplier
# SHAPE is similar to homogeneous for capped rounds either way (Ch.3's own
# 12-case comparison, average error 3.7%) -- only the base 0-degree multiplier
# differs, which is what this function provides.
# ----------------------------------------------------------------------------

# capped (APC/APCBC): triangulated from the chapter's own worked example
# (PzKpfw IVH driver plate, 85mm@10deg, vs. 75mm APCBC -- "if homogeneous,
# 85mm@10deg would limit Sherman 75mm penetration to 150m; face-hardened
# version penetrated at 940m instead"). Cross-checked against this project's
# own fitted Sherman 75mm M61 APC gun curve: PEN@150m = 86.65mm, matching
# the homogeneous effective-0deg figure (86.35mm) to <0.4% -- confirming the
# gun curve is self-consistent with this worked example before using it to
# derive the face-hardened figure. PEN@940m = 68.18mm; dividing by the raw
# 85mm thickness gives a 0.80 multiplier for face-hardened vs. capped rounds.
# ap_uncapped: directly stated, 0deg impact, no slope-formula involvement --
# "2pdr AP could penetrate 86mm of homogeneous armor at 0 yards/0 degree
# impact, but limited to 66mm of face-hardened penetration at same range/
# angle" -- i.e. a 66mm face-hardened plate resists like 86mm homogeneous,
# multiplier = 86/66 = 1.303. One data point, an early-war low-velocity gun.
# apds: directly stated -- "For 17 pdr APDS, face-hardened armor appears to
# be more vulnerable than homogeneous armor by factors of 1.155 to 1.229" --
# i.e. face-hardened resistance is 1/1.155 to 1/1.229 of homogeneous;
# midpoint of the stated range used here (1/1.192 = 0.839).
# hvap76/hvap90: no sourced figure for U.S.-calibre tungsten specifically --
# borrows the APDS figure as the nearest analog (same "no direct data,
# borrow the closest sourced curve" pattern used elsewhere in this module),
# flagged rather than left unhandled.
# apbc (Soviet-style): no sourced figure at all for this ammo type against
# face-hardened plate -- returns 1.0 (no correction), a real gap, not a
# claim of parity.
_FACE_HARDENED_MULTIPLIER: dict[str, float] = {
    "capped": 0.80,
    "ap_uncapped": 1.303,
    "apds": 0.839,
    "hvap76": 0.839,
    "hvap90": 0.839,
    "apbc": 1.0,
}


def face_hardened_multiplier(family: AmmoFamily) -> float:
    """Face-hardened plate's resistance relative to homogeneous plate of the
    same thickness, against a given ammo family. See module comment above
    for how each figure was sourced or triangulated.

    Apply only to plates with documented face-hardening (e.g. Panzer III/IV
    hull front/side per 1942 German policy) -- not a general-purpose armor
    property. Does not apply to HEAT: face-hardening's mechanism is
    specifically about shattering a kinetic round's nose before it digs in,
    which has no equivalent for a shaped-charge jet.
    """
    return _FACE_HARDENED_MULTIPLIER[family]


@dataclass(frozen=True)
class ArmorPlate:
    """One arc's worth of real armor geometry, ready to run through the pipeline.

    Attributes:
        thickness_mm: Real (as-mounted) plate thickness, mm.
        vertical_deg: Slope from vertical, degrees.
        lateral_deg: Additional traverse-relative angle, degrees (0 if none).
        cast: Whether this plate is cast (vs. rolled homogeneous).
        bhn: Brinell Hardness Number, if known/deviates from baseline
            (~230 BHN). None means "assume baseline, no high-hardness
            correction" -- this is an assumption, not a verified fact, for
            any plate where bhn is None. A non-None value below 375 BHN
            also gets no correction (see high_hardness_applies) -- the
            source's own text scopes this correction to genuinely brittle
            (>=375 BHN) armor specifically, not any hardness deviation.
        flaw_severity: "small"/"medium"/"large" if this plate has a
            documented quality-flaw problem (e.g. Panther glacis), else
            None. None means "no flaw correction applied" -- for most
            plates that's simply correct (no documented flaw history), but
            for a plate with a known, unmodelled flaw problem it is an
            explicit gap, not a claim the plate is flaw-free.
        face_hardened: Whether this plate has a documented face-hardened
            surface layer (e.g. Panzer III/IV hull front/side per 1942
            German policy). False means "no correction applied" -- for
            most plates that's simply correct (no documented face-hardening
            history). For a plate that is a layered composite of a
            face-hardened base plus a non-face-hardened bolt-on addition
            (e.g. Panzer III's 50mm base + 20mm applique), use
            face_hardened_fraction instead of this boolean.
        face_hardened_fraction: For a layered composite plate where only
            part of the effective thickness is genuinely face-hardened, the
            fraction (0.0-1.0) attributed to the face-hardened layer. When
            set (not None), this overrides `face_hardened` and blends
            face_hardened_multiplier() with 1.0 (no correction) by this
            fraction, rather than applying the full multiplier to the
            whole (already layered-combined) thickness. This is this
            project's own construction, not sourced from either project
            source directly -- neither describes how to treat a partially
            face-hardened composite plate. None (the default) means use
            `face_hardened` as an all-or-nothing flag instead.
    """

    thickness_mm: float
    vertical_deg: float
    lateral_deg: float = 0.0
    cast: bool = False
    bhn: float | None = None
    flaw_severity: FlawSeverity | None = None
    face_hardened: bool = False
    face_hardened_fraction: float | None = None

    def av_vs(self, diameter_mm: float, family: AmmoFamily = "capped") -> float:
        """Fully-corrected AV against a given attacker calibre and ammo family."""
        angle = compound_angle(self.vertical_deg, self.lateral_deg)
        av = effective_0deg_resistance(self.thickness_mm, diameter_mm, angle, family)
        if self.cast:
            av *= cast_deficiency_multiplier(self.thickness_mm, diameter_mm)
        if self.bhn is not None and high_hardness_applies(self.bhn):
            av *= high_hardness_multiplier(self.thickness_mm, diameter_mm, self.bhn)
        if self.flaw_severity is not None:
            av *= flaw_multiplier(self.thickness_mm, diameter_mm, angle, self.flaw_severity)
        if self.face_hardened_fraction is not None:
            blended = 1.0 * (1 - self.face_hardened_fraction) + face_hardened_multiplier(family) * self.face_hardened_fraction
            av *= blended
        elif self.face_hardened:
            av *= face_hardened_multiplier(family)
        return float(av)


# ----------------------------------------------------------------------------
# Rounded mantlet / turret-front area-weighting (Ch.11 p.44-45): a curved cast
# turret front doesn't present one fixed impact angle -- different hits land
# at different points on the curve and see a different effective slope. Tiger
# and Sherman M4A1 got vehicle-specific treatments from real source tables
# (Ch.10's mantlet edge-effect data, Ch.8's M34A1 mount hit-distribution
# table respectively); Panther got a Panther-specific 5-band distribution
# (also Ch.11, but explicitly tied to "hits at 200m range strike the Panther
# mantlet" -- not reusable as-is). This is the GENERAL-PURPOSE distribution
# the same chapter gives for any other rounded mantlet: "based on analysis of
# impact angles on a rounded mantlet when the hits are evenly distributed,
# which might occur at medium to long range or against hull down vehicles."
# ----------------------------------------------------------------------------

# (angle_deg, weight out of 100) -- derived directly from the source's own
# "decimal dice score" ranges (e.g. 70deg = dice roll 2-4 = 3 values = weight
# 3). Weights sum to exactly 100, matching the source's own 1-100 dice scale.
_ROUNDED_MANTLET_DICE_BANDS: list[tuple[float, int]] = [
    (75, 1), (70, 3), (65, 4), (60, 5), (55, 5), (50, 6), (45, 6), (40, 7),
    (35, 7), (30, 8), (25, 8), (20, 8), (15, 9), (10, 9), (5, 9), (0, 5),
]


def rounded_mantlet_angle_distribution() -> list[tuple[float, float]]:
    """The general rounded-mantlet impact-angle distribution (Ch.11 p.44-45),
    as (angle_deg, weight) pairs summing to 1.0.

    Use for any vehicle with a curved/domed cast turret front or mantlet
    that lacks its own vehicle-specific distribution or edge-effect table.
    Panther's turret front uses a Panther-specific 5-band distribution
    instead (also sourced, but tied to a specific 200m/76mm APCBC analysis)
    -- see design spec §13/§18 for which vehicles use which.
    """
    return [(a, w / 100.0) for a, w in _ROUNDED_MANTLET_DICE_BANDS]


def area_weighted_av(
    plate: ArmorPlate,
    diameter_mm: float,
    angle_distribution: list[tuple[float, float]],
    family: AmmoFamily = "capped",
) -> float:
    """AV for a plate whose effective impact angle varies across its surface
    (a rounded/curved mantlet or turret front), area-weighted by hit
    probability at each angle rather than assumed to be one flat plate at a
    single fixed angle.

    `plate.vertical_deg` is ignored -- the angle comes entirely from
    `angle_distribution` (see rounded_mantlet_angle_distribution()).
    `plate.lateral_deg`, thickness, cast, bhn, flaw_severity, and
    face_hardened are all preserved and applied at each sampled angle via
    ArmorPlate.av_vs() itself, so every other correction chains through
    automatically and consistently -- this does not duplicate any of that
    logic, only adds the angle-weighting on top of it.

    Args:
        plate: Template plate (vertical_deg is overridden per angle sample).
        diameter_mm: Attacking projectile diameter, mm.
        angle_distribution: (angle_deg, weight) pairs. Weights are
            normalized internally, so they need not already sum to 1.0.
        family: Ammo nose-shape family.

    Returns:
        Weighted-average AV, mm.
    """
    total_weight = sum(w for _, w in angle_distribution)
    total = 0.0
    for angle, weight in angle_distribution:
        sample = replace(plate, vertical_deg=angle)
        total += sample.av_vs(diameter_mm, family) * (weight / total_weight)
    return total


@dataclass(frozen=True)
class GunCurveFit:
    """A calibrated gun+ammo penetration-by-range curve.

    Attributes:
        p_ref: 0-degree-equivalent penetration at v_ref, mm.
        v_ref: Reference velocity the fit is anchored to, fps.
        exponent: Fitted DeMarre-style velocity exponent.
        muzzle_velocity_fps: Muzzle velocity, fps.
        k_factor: Ballistic K-factor.
        confidence: "fitted" (>=3 calibration points, least-squares -- the
            only tier where the fit can be checked against held-out
            residuals), "interpolated" (exactly 2 points -- an exact fit,
            since 2 points fully determine a 2-parameter power law, but
            with no spare data to check the fit against), or "rough" (a
            single point, generic DeMarre exponent 1.4283 assumed).
    """

    p_ref: float
    v_ref: float
    exponent: float
    muzzle_velocity_fps: float
    k_factor: float
    confidence: Literal["fitted", "interpolated", "rough"]

    def pen_0deg(self, range_m: NDArray | float) -> NDArray | float:
        """0-degree-equivalent penetration at range, mm."""
        v = velocity_at_range(self.muzzle_velocity_fps, self.k_factor, range_m)
        return self.p_ref * (v / self.v_ref) ** self.exponent


def fit_gun_curve(
    muzzle_velocity_fps: float,
    k_factor: float,
    calibration_ranges_m: list[float],
    calibration_pens_mm: list[float],
    calibration_angle_deg: float,
    projectile_diameter_mm: float,
    family: AmmoFamily = "capped",
) -> GunCurveFit:
    """Fit a gun+ammo penetration-by-range curve to attested calibration data.

    With 3+ calibration points, fits the velocity exponent by least squares
    (validated to <1.2% error against 5-point calibrations for the 75mm
    KwK40/PzGr39 and 88mm KwK36/PzGr39 guns) -- "fitted" confidence. With
    exactly 2 points, solves for the same 2 parameters (p_ref, exponent)
    exactly rather than assuming the generic exponent -- "interpolated"
    confidence: strictly better than assuming a generic exponent, but with
    no third point to check the fit's residual against. With a single
    point, falls back to a fixed anchor and the generic DeMarre exponent
    (1.4283) -- "rough" confidence, since this measured ~7% error at range
    extremes in testing versus the least-squares approach.

    Args:
        muzzle_velocity_fps: Muzzle velocity, fps.
        k_factor: Ballistic K-factor for this projectile.
        calibration_ranges_m: Ranges (metres) of attested penetration figures.
        calibration_pens_mm: Attested penetration (mm) at each calibration range.
        calibration_angle_deg: Impact angle the calibration data was measured at
            (often 30 degrees in period sources -- not necessarily 0).
        projectile_diameter_mm: Projectile diameter, mm (for slope conversion
            of the calibration data if it wasn't measured at 0 degrees).
        family: Ammo nose-shape family, for converting calibration data to
            0-degree-equivalent if calibration_angle_deg != 0.

    Returns:
        A GunCurveFit ready to evaluate at any range.
    """
    ranges = np.array(calibration_ranges_m, dtype=float)
    pens = np.array(calibration_pens_mm, dtype=float)
    v = velocity_at_range(muzzle_velocity_fps, k_factor, ranges)
    eff0 = effective_0deg_resistance(pens, projectile_diameter_mm, calibration_angle_deg, family)

    confidence: Literal["fitted", "interpolated", "rough"]
    if len(ranges) >= 3:
        v_ref = v[len(v) // 2]
        x = np.log(v / v_ref)
        y = np.log(eff0)
        exponent, log_p_ref = np.polyfit(x, y, 1)
        confidence = "fitted"
    elif len(ranges) == 2:
        v_ref = v[0]
        x = np.log(v / v_ref)
        y = np.log(eff0)
        exponent, log_p_ref = np.polyfit(x, y, 1)  # exact fit through both points
        confidence = "interpolated"
    else:
        v_ref = v[0]
        exponent = 1.4283
        log_p_ref = np.log(eff0[0])
        confidence = "rough"

    return GunCurveFit(
        p_ref=float(np.exp(log_p_ref)),
        v_ref=float(v_ref),
        exponent=float(exponent),
        muzzle_velocity_fps=muzzle_velocity_fps,
        k_factor=k_factor,
        confidence=confidence,
    )
