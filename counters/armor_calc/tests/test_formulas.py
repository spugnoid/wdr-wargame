"""Regression tests: the consolidated module must reproduce the hand-validated
worked examples from the design session, not just "look reasonable"."""

import numpy as np
import pytest

from armor_calc.formulas import (
    ArmorPlate,
    area_weighted_av,
    base_hit_probability,
    cast_deficiency_multiplier,
    compound_angle,
    crew_quality_from_morale,
    crew_quality_hit_cap,
    crossing_target_ratio,
    effective_0deg_resistance,
    face_hardened_multiplier,
    fit_gun_curve,
    flaw_multiplier,
    flight_time,
    heat_effective_resistance,
    heat_multiplier,
    heat_pen_vs_schurzen,
    heat_reference_table,
    hit_probability,
    high_hardness_applies,
    high_hardness_multiplier,
    hull_turret_split,
    layered_plate_effective_thickness,
    roll_threshold_for_probability,
    rounded_mantlet_angle_distribution,
    shot_displacement_m,
    shatter_gap_failure,
    shatter_gap_reference_table,
    shatter_gap_window,
    slope_multiplier,
    vehicle_fire_thresholds,
)

YD_TO_M = 0.9144


class TestGunCurveFits:
    def test_75mm_kwk40_pzgr39_matches_attested_data(self):
        """5-point fit vs. Encyclopedia of German Tanks data, validated to <1.2% error."""
        fit = fit_gun_curve(
            muzzle_velocity_fps=2460,
            k_factor=2361,
            calibration_ranges_m=[100, 500, 1000, 1500, 2000],
            calibration_pens_mm=[106, 96, 85, 74, 64],
            calibration_angle_deg=30,
            projectile_diameter_mm=75,
        )
        assert fit.confidence == "fitted"
        assert fit.exponent == pytest.approx(1.72, abs=0.02)
        # 0-degree-equivalent penetration at the calibration ranges, back-solved
        expected_0deg = effective_0deg_resistance(
            np.array([106.0, 96.0, 85.0, 74.0, 64.0]), 75, 30.0
        )
        for r, exp in zip([100, 500, 1000, 1500, 2000], expected_0deg):
            assert fit.pen_0deg(r) == pytest.approx(float(exp), rel=0.012)

    def test_88mm_kwk36_pzgr39_matches_attested_data(self):
        fit = fit_gun_curve(
            muzzle_velocity_fps=2580,
            k_factor=1778,
            calibration_ranges_m=[100, 500, 1000, 1500, 2000],
            calibration_pens_mm=[120, 110, 100, 91, 84],
            calibration_angle_deg=30,
            projectile_diameter_mm=88,
        )
        assert fit.confidence == "fitted"
        expected_0deg = effective_0deg_resistance(
            np.array([120.0, 110.0, 100.0, 91.0, 84.0]), 88, 30.0
        )
        for r, exp in zip([100, 500, 1000, 1500, 2000], expected_0deg):
            assert fit.pen_0deg(r) == pytest.approx(float(exp), rel=0.01)

    def test_rough_fit_falls_back_to_generic_demarre_exponent(self):
        fit = fit_gun_curve(
            muzzle_velocity_fps=1850,
            k_factor=2300,
            calibration_ranges_m=[0],
            calibration_pens_mm=[79],
            calibration_angle_deg=0,
            projectile_diameter_mm=75,
        )
        assert fit.confidence == "rough"
        assert fit.exponent == pytest.approx(1.4283)

    def test_two_point_fit_is_interpolated_not_rough(self):
        """2 points fully determine the 2-parameter power law exactly --
        strictly better than assuming the generic exponent, but flagged as
        its own tier since there's no third point to check the fit against."""
        fit = fit_gun_curve(
            muzzle_velocity_fps=2739,
            k_factor=5061,
            calibration_ranges_m=[500, 1000],
            calibration_pens_mm=[57, 44],
            calibration_angle_deg=30,
            projectile_diameter_mm=50,
        )
        assert fit.confidence == "interpolated"
        assert fit.exponent != pytest.approx(1.4283)  # actually solved for, not assumed
        # the fit must reproduce both calibration points exactly (2 eqns, 2 unknowns)
        expected_0deg = effective_0deg_resistance(np.array([57.0, 44.0]), 50, 30.0)
        for r, exp in zip([500, 1000], expected_0deg):
            assert fit.pen_0deg(r) == pytest.approx(float(exp), rel=0.005)


class TestSlopeMultipliers:
    def test_zero_angle_is_no_multiplier(self):
        assert slope_multiplier(0.0, 1.0, "capped") == pytest.approx(1.0, abs=0.01)

    def test_capped_kinetic_matches_tm9_1907_table_at_60deg(self):
        """Ch.2 p.18-19 source table: 60deg, T/D=0.56 (57mm proj) -> multiplier 2.78.
        The fitted piecewise formula is a smooth fit across the whole table, not
        pinned to any single entry -- a few percent residual here is expected,
        not a bug (measured ~3.8% at this specific point)."""
        mult = slope_multiplier(60.0, 0.56, "capped")
        assert float(mult) == pytest.approx(2.78, rel=0.05)

    def test_tungsten_has_no_td_dependence(self):
        """Tungsten families ignore td_ratio -- same result regardless of T/D."""
        m1 = slope_multiplier(45.0, 0.3, "hvap90")
        m2 = slope_multiplier(45.0, 2.0, "hvap90")
        assert float(m1) == pytest.approx(float(m2))

    def test_tungsten_loses_relative_effectiveness_faster_than_capped_at_steep_angle(self):
        """Session finding: parity at 0deg, tungsten needs ~44% more multiplier by 60deg."""
        capped_60 = float(slope_multiplier(60.0, 1.13, "capped"))
        tungsten_60 = float(slope_multiplier(60.0, 1.13, "hvap90"))
        assert tungsten_60 / capped_60 == pytest.approx(1.44, rel=0.05)

    def test_apbc_flatter_than_capped_at_moderate_angle(self):
        """Blunt-nose APBC should be flatter (lower multiplier) than capped at 30-55deg."""
        capped = float(slope_multiplier(45.0, 1.13, "capped"))
        apbc = float(slope_multiplier(45.0, 1.13, "apbc"))
        assert apbc < capped

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError):
            slope_multiplier(30.0, 1.0, "made-up-family")  # type: ignore[arg-type]


class TestUncappedAP:
    """Appendix 9 (p.103-105): the book's own computed "0 degree armor"
    figures for real 17pdr/6pdr AP (uncapped, no ballistic cap) firing tests
    against Tiger E armor -- 4 independent points, all matched to <2%."""

    def test_matches_appendix9_82mm_6pdr_20deg(self):
        av = float(effective_0deg_resistance(82.0, 57.0, 20.0, "ap_uncapped"))
        assert av == pytest.approx(90.0, rel=0.02)

    def test_matches_appendix9_102mm_6pdr_10deg(self):
        av = float(effective_0deg_resistance(102.0, 57.0, 10.0, "ap_uncapped"))
        assert av == pytest.approx(103.0, rel=0.02)

    def test_matches_appendix9_102mm_17pdr_25deg(self):
        av = float(effective_0deg_resistance(102.0, 76.2, 25.0, "ap_uncapped"))
        assert av == pytest.approx(119.0, rel=0.02)

    def test_matches_appendix9_100mm_6pdr_21deg(self):
        """This is the firing-test row where the real outcome ("Not through")
        diverged from what raw penetration-vs-armor numbers alone would
        predict (114mm armor vs. 118mm quoted penetration) -- the book
        attributes this to Tiger's actual armor hardness (315-324 BHN)
        exceeding the 275 BHN test-plate baseline the gun's penetration
        figure was measured against. That real-world variance is a fact
        about the physical test, not something this formula (which only
        computes the slope-adjusted 0deg-equivalent armor figure, not the
        outcome) is expected to reproduce."""
        av = float(effective_0deg_resistance(100.0, 57.0, 21.0, "ap_uncapped"))
        assert av == pytest.approx(114.0, rel=0.02)


class TestCompoundAngle:
    def test_no_lateral_angle_is_identity(self):
        assert compound_angle(45.0, 0.0) == pytest.approx(45.0)

    def test_matches_worked_example_45mm_60deg_slope_40deg_lateral(self):
        """Ch.12 worked example: 45mm@60deg vertical, 40deg lateral -> 67.5deg compound."""
        assert compound_angle(60.0, 40.0) == pytest.approx(67.5, abs=0.5)


class TestCastAndHardnessCorrections:
    def test_cast_deficiency_reduces_resistance(self):
        assert cast_deficiency_multiplier(52.0, 75.0) < 1.0

    def test_t34_hull_front_matches_source_worked_example(self):
        """Bird & Livingston Ch.4's own worked example: 122mm slope-adjusted
        x 0.76 high-hardness multiplier -> 93mm. This is the exact case that
        resolved the 'T-34 anomaly' this session."""
        slope_only = effective_0deg_resistance(45.0, 75.0, 60.0)
        assert float(slope_only) == pytest.approx(122.3, abs=0.2)

        hh_mult = high_hardness_multiplier(45.0, 75.0, bhn=450)
        assert hh_mult == pytest.approx(0.766, abs=0.01)

        corrected = float(slope_only) * hh_mult
        assert corrected == pytest.approx(93.0, abs=1.5)

    def test_high_hardness_gives_bonus_when_not_overmatched(self):
        """T/D > 1 (not overmatched) should give a bonus, not a penalty."""
        mult = high_hardness_multiplier(90.0, 75.0, bhn=300)
        assert mult > 1.0

    def test_high_hardness_applies_only_at_or_above_375bhn(self):
        """Ch.4 p.24: 'Armor hardnesses below 375 BHN are normally referred
        to as machineable quality and are expected to have reasonable
        impact resistance... When hardness equals or exceeds about 375
        BHN, armor becomes brittle...' -- this correction's own sourced
        domain is >=375 BHN specifically, not any hardness deviation."""
        assert not high_hardness_applies(374.9)
        assert high_hardness_applies(375.0)
        assert high_hardness_applies(450.0)

    def test_armor_plate_skips_correction_below_375bhn(self):
        """Tiger E's real measured hardness (310-340 BHN, Appendix 9) is
        below the correction's sourced domain -- ArmorPlate.av_vs() must
        not apply a high-hardness bonus for it, even though bhn is set."""
        plate_below = ArmorPlate(thickness_mm=80.0, vertical_deg=0.0, cast=False, bhn=320.0)
        plate_uncorrected = ArmorPlate(thickness_mm=80.0, vertical_deg=0.0, cast=False, bhn=None)
        assert plate_below.av_vs(diameter_mm=75.0) == pytest.approx(plate_uncorrected.av_vs(diameter_mm=75.0))

    def test_armor_plate_still_applies_correction_at_or_above_375bhn(self):
        """The T-34 hull worked example (bhn=450) must still get its
        validated correction -- the gate must not suppress genuinely
        in-domain cases."""
        plate = ArmorPlate(thickness_mm=45.0, vertical_deg=60.0, cast=False, bhn=450.0)
        assert plate.av_vs(diameter_mm=75.0) == pytest.approx(93.7, abs=1.0)


class TestHitProbability:
    # Appendix 17 p.120-121: first-shot Head-On hit%, 3 guns x 5 ranges (yards).
    CALIBRATION = [
        # (mv_fps, k, range_yd, hit_pct)
        (1850, 2300, 400, 97), (1850, 2300, 800, 50), (1850, 2300, 1200, 18),
        (1850, 2300, 1600, 8), (1850, 2300, 2000, 4),
        (2900, 1686, 400, 100), (2900, 1686, 800, 73), (2900, 1686, 1200, 34),
        (2900, 1686, 1600, 17), (2900, 1686, 2000, 9),
        (2600, 2722, 400, 100), (2600, 2722, 800, 66), (2600, 2722, 1200, 29),
        (2600, 2722, 1600, 13), (2600, 2722, 2000, 7),
    ]

    def test_matches_calibration_within_expected_error(self):
        """Mean abs error 5.7pp, max 12.4pp across the 15-point fit -- checked
        with generous per-point tolerance, tight aggregate tolerance."""
        errors = []
        for mv, k, range_yd, hit_pct in self.CALIBRATION:
            ft = flight_time(mv, k, range_yd * YD_TO_M)
            pred = base_hit_probability(ft)
            errors.append(abs(pred - hit_pct))
            assert pred == pytest.approx(hit_pct, abs=15)  # generous per-point
        assert sum(errors) / len(errors) < 7.0  # tight on the aggregate

    def test_monotonically_decreasing_with_flight_time(self):
        times = [0.3, 0.8, 1.5, 2.5, 4.0]
        values = [base_hit_probability(t) for t in times]
        assert values == sorted(values, reverse=True)

    def test_crew_quality_caps_ordered(self):
        assert (
            crew_quality_hit_cap("elite")
            > crew_quality_hit_cap("veteran")
            > crew_quality_hit_cap("regular")
            > crew_quality_hit_cap("green")
            > crew_quality_hit_cap("militia")
        )

    def test_crew_quality_from_morale_bands(self):
        assert crew_quality_from_morale(7) == "elite"
        assert crew_quality_from_morale(6) == "veteran"
        assert crew_quality_from_morale(5) == "regular"
        assert crew_quality_from_morale(4) == "green"
        assert crew_quality_from_morale(3) == "green"
        assert crew_quality_from_morale(2) == "militia"

    def test_low_quality_crew_caps_close_range_hit_chance(self):
        """At very short range the raw curve predicts near-100% -- a militia
        crew should be capped well below that."""
        ft = flight_time(2900, 1686, 100.0)  # 17pdr at 100m, raw curve ~100%
        assert base_hit_probability(ft) > 95
        capped = hit_probability(2900, 1686, 100.0, quality="militia")
        assert capped == pytest.approx(50.0, abs=0.1)

    def test_crossing_target_is_harder_to_hit_than_stationary(self):
        r = 800 * YD_TO_M
        assert crossing_target_ratio(r) < 1.0
        assert crossing_target_ratio(r, follow_up=True) > crossing_target_ratio(r, follow_up=False)

    def test_crossing_ratio_never_fully_recovers_even_on_follow_up(self):
        """Session finding (Appendix 17 p.121): a direct crosser is never as
        easy to hit as a stationary target, even with unlimited ranging shots."""
        r = 2000 * YD_TO_M
        assert crossing_target_ratio(r, follow_up=True) < 0.6

    def test_no_wind_drift_or_trunnion_cant_modelled(self):
        """Deliberate omission (Appendix 7/8): both are small, first-shot-only
        effects at this game's scale -- confirm hit_probability's signature
        has no such parameters (would raise TypeError if someone tried)."""
        with pytest.raises(TypeError):
            hit_probability(2900, 1686, 500.0, quality="veteran", wind_mph=10)  # type: ignore[call-arg]


class TestDiceThresholdUnification:
    def test_roll_threshold_matches_known_dice_cdf(self):
        """1d6+1d8+1d12 (576 outcomes): sum>=15 happens exactly 50% of the
        time (the distribution's own median), sum>=3 is 100% (guaranteed)."""
        assert roll_threshold_for_probability(50.0) == 15
        assert roll_threshold_for_probability(100.0) == 3

    def test_below_dice_resolution_is_automatic_miss(self):
        """Below the rarest single outcome (sum=26, ~0.17%), no roll can
        represent the probability -- must read as an automatic miss, not
        an impossibly-high threshold."""
        assert roll_threshold_for_probability(0.01) is None

    def test_hull_turret_split_favors_hull_at_short_range(self):
        turret_frac, hull_frac = hull_turret_split(100.0)
        assert hull_frac > turret_frac
        assert turret_frac + hull_frac == pytest.approx(1.0)

    def test_hull_turret_split_shifts_toward_turret_at_long_range(self):
        turret_short, _ = hull_turret_split(100.0)
        turret_long, _ = hull_turret_split(1000.0)
        assert turret_long > turret_short

    def test_thresholds_partition_correctly(self):
        """The three bands (miss / turret / hull) must be internally
        consistent: hull_threshold, if it exists, is strictly higher than
        miss_threshold (hull requires clearing a higher bar than a bare hit)."""
        t = vehicle_fire_thresholds(2460, 2361, 500.0, quality="regular")
        assert t.miss_threshold is not None and t.hull_threshold is not None
        assert t.hull_threshold > t.miss_threshold

    def test_probability_of_each_band_matches_the_component_probabilities(self):
        """Reconstructing P(Turret) and P(Hull) from the two thresholds via
        the real dice CDF must reproduce hit_pct * turret_frac / hull_frac --
        this is the actual mathematical claim the unification depends on."""
        from armor_calc.formulas import _DICE_CDF_GE

        mv, k, range_m, quality = 2460, 2361, 500.0, "regular"
        hit_pct = hit_probability(mv, k, range_m, quality)
        turret_frac, hull_frac = hull_turret_split(range_m)
        t = vehicle_fire_thresholds(mv, k, range_m, quality)

        p_hit = _DICE_CDF_GE[t.miss_threshold]
        p_hull = _DICE_CDF_GE[t.hull_threshold]
        p_turret = p_hit - p_hull

        assert p_hit * 100 == pytest.approx(hit_pct, abs=3)  # dice-rounding tolerance
        assert p_turret == pytest.approx((hit_pct / 100) * turret_frac, abs=0.03)
        assert p_hull == pytest.approx((hit_pct / 100) * hull_frac, abs=0.03)

    def test_negligible_hit_chance_at_extreme_range_is_automatic_miss(self):
        """Panther's flat-shooting 75L70 still eventually runs out of
        practical hit chance at long enough range."""
        t = vehicle_fire_thresholds(3068, 2448, 3500.0, quality="militia")
        assert t.miss_threshold is None


class TestHeat:
    def test_zero_angle_is_no_multiplier(self):
        assert heat_multiplier(0.0) == pytest.approx(1.0)

    def test_matches_ch2_reference_curve_at_75deg(self):
        """Ch.2 p.16 angle-only reference curve: ~3.9x at 75deg, matching
        the stated 1/cos(75deg)=3.86 identity check."""
        assert float(heat_multiplier(75.0)) == pytest.approx(3.86, abs=0.05)

    def test_has_no_td_dependence_by_construction(self):
        """HEAT ignores diameter entirely -- effective_resistance only takes
        thickness and angle, unlike the kinetic families."""
        r1 = heat_effective_resistance(thickness_mm=50.0, vertical_deg=45.0)
        r2 = heat_effective_resistance(thickness_mm=50.0, vertical_deg=45.0)
        assert r1 == r2  # no diameter parameter exists to vary

    def test_gentler_than_capped_at_steep_angle(self):
        """Correction of an earlier (wrong) assumption from this session: HEAT's
        secant law is actually GENTLER than the capped-kinetic curve at steep
        angle for typical T/D, not steeper. Capped rounds carry a compounding
        penalty beyond pure geometry -- increasing ricochet/deflection failure
        as angle grows -- that HEAT's jet doesn't experience (HEAT is immune to
        ricochet, per 17.2.6's intended fix). At 70deg, T/D=1.13: HEAT 2.92x
        vs. capped 5.37x."""
        heat = float(heat_multiplier(70.0))
        capped = float(slope_multiplier(70.0, 1.13, "capped"))
        assert heat < capped

    def test_reference_table_is_monotonically_increasing(self):
        table = heat_reference_table()
        values = [v for _, v in table]
        assert values == sorted(values)
        assert values[0] == pytest.approx(1.0)

    def test_schurzen_halves_heat_pen(self):
        """Design convention (ASL's own Side Skirts note), not a sourced
        figure -- see heat_pen_vs_schurzen()'s docstring for why this is
        flagged medium confidence rather than cited to Bird & Livingston."""
        assert heat_pen_vs_schurzen(120.0) == pytest.approx(60.0)


class TestFlawMultiplier:
    def test_matches_panther_glacis_worked_example_152mm_apbc(self):
        """Ch.6 p.29: 152mm APBC vs 85mm@55deg Panther glacis, medium flaws
        -> 17.5% reduction (0.825x). T/D = 85/152 = 0.559."""
        mult = flaw_multiplier(thickness_mm=85.0, diameter_mm=152.0, angle_deg=55.0, severity="medium")
        assert mult == pytest.approx(0.825, abs=0.01)

    def test_matches_panther_glacis_worked_example_17pdr_apcbc(self):
        """Ch.6 p.29: 17pdr APCBC vs 85mm@55deg Panther glacis, medium flaws
        -> 5% reduction (0.95x). T/D = 85/76.2 = 1.115."""
        mult = flaw_multiplier(thickness_mm=85.0, diameter_mm=76.2, angle_deg=55.0, severity="medium")
        assert mult == pytest.approx(0.95, abs=0.01)

    def test_converges_to_one_when_not_overmatched(self):
        assert flaw_multiplier(150.0, 75.0, 45.0, "medium") == pytest.approx(1.0)

    def test_large_more_severe_than_small_at_source_anchor_point(self):
        """At T/D=0.1 (the source's own directly-read anchor, not an interpolated
        point) small/medium/large are cleanly ordered at 60deg. Deliberately not
        asserting this ordering holds at every T/D: "large" severity's
        convergence point is only precisely sourced at 0deg (fastest) and
        60/75deg (still <1.0 at T/D=1.5) -- the 30deg convergence used in this
        module is an unsourced interpolation guess and can cross over "medium"
        at some T/D values as a result. That's a known gap, not silently hidden."""
        small = flaw_multiplier(7.5, 75.0, 60.0, "small")
        medium = flaw_multiplier(7.5, 75.0, 60.0, "medium")
        large = flaw_multiplier(7.5, 75.0, 60.0, "large")
        assert small > medium > large


class TestShatterGap:
    """Ch.7 p.29-33: over-penetration can shatter a round's nose before it
    completes penetration -- validated against the chapter's own two worked
    examples plus a real Appendix 9 firing-test row."""

    def test_matches_tiger_driver_plate_worked_example(self):
        """Tiger E driver plate, AV=103mm -> source states window is
        109mm to 126mm."""
        lower, upper = shatter_gap_window(103.0)
        assert lower == pytest.approx(109.0, abs=1.0)
        assert upper == pytest.approx(126.0, abs=1.0)

    def test_matches_panther_mantlet_worked_example(self):
        """Panther mantlet, AV=98mm -> source states upper bound 120mm."""
        _, upper = shatter_gap_window(98.0)
        assert upper == pytest.approx(120.0, abs=1.0)

    def test_matches_real_appendix9_firing_test_row(self):
        """17pdr APCBC vs Tiger 82mm/50deg side armor (AV=82mm): 3035fps
        shot penetrated 87mm (ratio 1.061, just inside the window) --
        actual test result was 'No Pen.', consistent with shatter-gap
        failure despite PEN > AV."""
        assert shatter_gap_failure(pen_mm=87.0, av_mm=82.0, family="capped")

    def test_below_window_is_not_shatter_failure(self):
        """Ratio 1.00 (PEN == AV): well below the 1.06 threshold, this is
        an ordinary marginal penetration case, not shatter gap."""
        assert not shatter_gap_failure(pen_mm=82.0, av_mm=82.0, family="capped")

    def test_above_window_is_shatter_penetration_not_failure(self):
        """Ratio 1.30 (beyond 1.22): 'shatter penetration' -- the round
        still gets through despite shattering."""
        assert not shatter_gap_failure(pen_mm=106.6, av_mm=82.0, family="capped")

    def test_tungsten_never_shatter_fails(self):
        """APDS/tungsten failures follow a different, unsourced mechanism
        (Appendix 9 p.104) -- this function must not apply the kinetic
        steel-round threshold to them."""
        assert not shatter_gap_failure(pen_mm=87.0, av_mm=82.0, family="apds")
        assert not shatter_gap_failure(pen_mm=87.0, av_mm=82.0, family="hvap76")

    def test_apbc_is_eligible(self):
        """Ch.7 p.30 explicitly includes Russian steel projectiles."""
        assert shatter_gap_failure(pen_mm=87.0, av_mm=82.0, family="apbc")

    def test_reference_table_covers_practical_av_range(self):
        table = shatter_gap_reference_table()
        avs = [row[0] for row in table]
        assert min(avs) <= 40 and max(avs) >= 190
        # every window's upper bound must exceed its lower bound
        assert all(upper > lower for _, lower, upper in table)


class TestFaceHardenedArmor:
    """Ch.3 p.21-23: face-hardened armor gives an early-war bonus against
    uncapped AP, but a real penalty against capped rounds once capped
    ammunition became standard -- validated against the chapter's own two
    worked examples."""

    def test_capped_penalty_matches_pzivh_worked_example(self):
        """PzKpfw IVH driver plate (85mm@10deg) vs 75mm APCBC: 'if
        homogeneous, would limit penetration to 150m; face-hardened
        version penetrated at 940m instead.' Triangulated via this
        project's own fitted Sherman 75mm M61 APC gun curve (see
        formulas.py module comment for the full derivation) to a 0.80
        multiplier."""
        assert face_hardened_multiplier("capped") == pytest.approx(0.80, abs=0.01)

    def test_uncapped_bonus_matches_2pdr_worked_example(self):
        """'2pdr AP could penetrate 86mm of homogeneous armor at 0 yards/0
        degree impact, but limited to 66mm of face-hardened penetration at
        same range/angle' -- multiplier = 86/66."""
        assert face_hardened_multiplier("ap_uncapped") == pytest.approx(86.0 / 66.0, rel=0.01)

    def test_apds_penalty_matches_17pdr_worked_example(self):
        """'For 17 pdr APDS, face-hardened armor appears to be more
        vulnerable than homogeneous armor by factors of 1.155 to 1.229' --
        resistance multiplier is the reciprocal, ~0.84."""
        mult = face_hardened_multiplier("apds")
        assert 1 / 1.229 <= mult <= 1 / 1.155

    def test_capped_and_uncapped_go_opposite_directions(self):
        """The historically-real reversal: face-hardening helps against
        uncapped AP and hurts against capped rounds."""
        assert face_hardened_multiplier("ap_uncapped") > 1.0
        assert face_hardened_multiplier("capped") < 1.0

    def test_armor_plate_applies_face_hardened_penalty_for_capped(self):
        plate_fh = ArmorPlate(thickness_mm=85.0, vertical_deg=10.0, face_hardened=True)
        plate_plain = ArmorPlate(thickness_mm=85.0, vertical_deg=10.0, face_hardened=False)
        assert plate_fh.av_vs(diameter_mm=75.0, family="capped") < plate_plain.av_vs(diameter_mm=75.0, family="capped")

    def test_armor_plate_applies_face_hardened_bonus_for_uncapped(self):
        plate_fh = ArmorPlate(thickness_mm=85.0, vertical_deg=0.0, face_hardened=True)
        plate_plain = ArmorPlate(thickness_mm=85.0, vertical_deg=0.0, face_hardened=False)
        assert plate_fh.av_vs(diameter_mm=57.0, family="ap_uncapped") > plate_plain.av_vs(
            diameter_mm=57.0, family="ap_uncapped"
        )


class TestLayeredPlateInContact:
    """Ch.9 p.38: two homogeneous plates bolted/welded together resist less
    than the sum of their thicknesses -- validated against all three of the
    chapter's own worked examples."""

    def test_matches_sherman_applique_worked_example(self):
        """Sherman 38mm applique + 38mm side hull -> 58mm effective."""
        eff = layered_plate_effective_thickness(38.0, 38.0)
        assert eff == pytest.approx(58.0, abs=0.5)

    def test_matches_t34_scrap_armor_worked_example_floor_limited(self):
        """T-34 15mm scrap armor over 45mm base -> ~50mm, floor-limited
        (the source's own text notes the raw formula gives 46mm, below the
        0.3x15+45=49.5mm floor, so the floor value is used instead)."""
        eff = layered_plate_effective_thickness(15.0, 45.0)
        assert eff == pytest.approx(49.5, abs=0.5)

    def test_matches_kv1_added_plate_worked_example(self):
        """KV-1 75mm driver plate + 30mm added plate -> 92mm effective."""
        eff = layered_plate_effective_thickness(30.0, 75.0)
        assert eff == pytest.approx(92.0, abs=0.5)

    def test_less_than_naive_sum(self):
        """The whole point of this correction: layered plates never resist
        as well as one solid plate of the same total thickness."""
        eff = layered_plate_effective_thickness(20.0, 50.0)
        assert eff < 70.0


class TestShotDisplacement:
    """Appendix 15 p.117-118: dice score + hit% -> displacement in metres
    along one axis.

    The source presents TWO distinct methods for this conversion: a
    discrete percentile lookup table (not transcribed in this codebase --
    see the design spec's scope decision) and this closed-form equation,
    introduced in the text as "an alternative to table use." The book
    validates the equation against exactly one worked example computed
    via the equation itself (dice=66, hit=85% -> 0.7m, tested below).
    Other displacement figures appearing in the book's prose (e.g. a
    Tiger-vs-IS-2 example using dice=22/50 at an approximate 95% hit
    rate) come from the discrete table's own threshold-crossing lookup,
    not from this equation -- the two methods are different approximating
    models of the same phenomenon and are not expected to agree to tight
    tolerance, so they are not valid tests of this function.
    """

    def test_matches_worked_example_85pct_dice66(self):
        """'Assume hit score against 2m x 2m target is 85 vertical, and
        corresponding dice score for vertical shot placement is 66... The
        ratio of the dice and hit scores equals 0.948/1.38, or 0.7m.'"""
        displacement = shot_displacement_m(dice_score=66.0, hit_pct=85.0)
        assert displacement == pytest.approx(0.7, abs=0.05)

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


class TestPartialFaceHardening:
    """Session finding: Panzer III Ausf M's hull front is a 20mm bolted
    applique over a 50mm face-hardened base plate -- a composite where
    only part of the effective thickness is genuinely face-hardened.
    ArmorPlate.face_hardened_fraction blends the correction proportionally
    rather than applying it (or not) to the whole layered thickness."""

    def test_fraction_blends_between_no_correction_and_full_correction(self):
        layered = layered_plate_effective_thickness(20.0, 50.0)
        no_fh = ArmorPlate(thickness_mm=layered, vertical_deg=21.0, face_hardened=False)
        full_fh = ArmorPlate(thickness_mm=layered, vertical_deg=21.0, face_hardened=True)
        partial_fh = ArmorPlate(thickness_mm=layered, vertical_deg=21.0, face_hardened_fraction=50.0 / 70.0)

        av_none = no_fh.av_vs(75.0, family="capped")
        av_full = full_fh.av_vs(75.0, family="capped")
        av_partial = partial_fh.av_vs(75.0, family="capped")

        # capped rounds get a penalty from face-hardening, so full < none;
        # the partial blend must land strictly between the two extremes.
        assert av_full < av_partial < av_none

    def test_fraction_of_zero_matches_no_correction(self):
        plate_frac0 = ArmorPlate(thickness_mm=56.0, vertical_deg=21.0, face_hardened_fraction=0.0)
        plate_none = ArmorPlate(thickness_mm=56.0, vertical_deg=21.0, face_hardened=False)
        assert plate_frac0.av_vs(75.0) == pytest.approx(plate_none.av_vs(75.0))

    def test_fraction_of_one_matches_full_correction(self):
        plate_frac1 = ArmorPlate(thickness_mm=56.0, vertical_deg=21.0, face_hardened_fraction=1.0)
        plate_full = ArmorPlate(thickness_mm=56.0, vertical_deg=21.0, face_hardened=True)
        assert plate_frac1.av_vs(75.0) == pytest.approx(plate_full.av_vs(75.0))

    def test_fraction_takes_precedence_over_boolean_flag(self):
        """If both are set, face_hardened_fraction wins -- documented
        behavior, not an ambiguous conflict."""
        plate = ArmorPlate(thickness_mm=56.0, vertical_deg=21.0, face_hardened=True, face_hardened_fraction=0.0)
        plate_none = ArmorPlate(thickness_mm=56.0, vertical_deg=21.0, face_hardened=False)
        assert plate.av_vs(75.0) == pytest.approx(plate_none.av_vs(75.0))


class TestRoundedMantlet:
    """Ch.11 p.44-45: the general rounded-mantlet impact-angle distribution
    ("based on analysis of impact angles on a rounded mantlet when the hits
    are evenly distributed, which might occur at medium to long range or
    against hull down vehicles... converted to a 1-100 decimal dice system"),
    distinct from Panther's own Panther-specific 5-band distribution."""

    def test_distribution_weights_sum_to_one(self):
        dist = rounded_mantlet_angle_distribution()
        assert sum(w for _, w in dist) == pytest.approx(1.0)

    def test_distribution_matches_source_dice_bands(self):
        """Spot-check a few bands directly against the source's own dice
        ranges: 70deg=2-4 (3 values), 0deg=96-00 (5 values)."""
        dist = dict(rounded_mantlet_angle_distribution())
        assert dist[70.0] == pytest.approx(0.03)
        assert dist[0.0] == pytest.approx(0.05)

    def test_area_weighted_av_within_bounds(self):
        """The weighted average must fall strictly between the flattest
        (0deg) and steepest (75deg) single-angle AV -- a basic sanity
        check that the weighting isn't producing an out-of-range result."""
        plate = ArmorPlate(thickness_mm=90.0, vertical_deg=0.0, cast=True)
        dist = rounded_mantlet_angle_distribution()
        weighted = area_weighted_av(plate, 75.0, dist)
        av_0deg = ArmorPlate(thickness_mm=90.0, vertical_deg=0.0, cast=True).av_vs(75.0)
        av_75deg = ArmorPlate(thickness_mm=90.0, vertical_deg=75.0, cast=True).av_vs(75.0)
        assert av_0deg < weighted < av_75deg

    def test_area_weighted_av_ignores_plates_own_vertical_deg(self):
        """vertical_deg on the input plate must be irrelevant -- only the
        distribution's own angles matter."""
        dist = rounded_mantlet_angle_distribution()
        plate_a = ArmorPlate(thickness_mm=90.0, vertical_deg=10.0, cast=True)
        plate_b = ArmorPlate(thickness_mm=90.0, vertical_deg=60.0, cast=True)
        assert area_weighted_av(plate_a, 75.0, dist) == pytest.approx(area_weighted_av(plate_b, 75.0, dist))

    def test_area_weighted_av_chains_other_corrections(self):
        """cast/bhn/flaw/face_hardened must still apply at each sampled
        angle -- a cast plate's weighted AV must be lower than the same
        plate treated as rolled."""
        dist = rounded_mantlet_angle_distribution()
        cast_plate = ArmorPlate(thickness_mm=90.0, vertical_deg=0.0, cast=True)
        rolled_plate = ArmorPlate(thickness_mm=90.0, vertical_deg=0.0, cast=False)
        assert area_weighted_av(cast_plate, 75.0, dist) < area_weighted_av(rolled_plate, 75.0, dist)


class TestArmorPlate:
    def test_t34_hull_front_end_to_end(self):
        plate = ArmorPlate(thickness_mm=45.0, vertical_deg=60.0, cast=False, bhn=450)
        assert plate.av_vs(diameter_mm=75.0) == pytest.approx(93.7, abs=1.0)

    def test_tungsten_family_via_av_vs(self):
        """ArmorPlate.av_vs() already threads the family parameter through --
        wiring AV-vs-Tungsten into the pipeline needed no new formula, just
        plumbing. Confirms tungsten needs MORE multiplier than capped at
        steep angle here (the correctly-validated earlier finding, unlike
        the HEAT mixup)."""
        plate = ArmorPlate(thickness_mm=45.0, vertical_deg=60.0, cast=False)
        capped_av = plate.av_vs(diameter_mm=75.0, family="capped")
        tungsten_av = plate.av_vs(diameter_mm=75.0, family="hvap76")
        assert tungsten_av > capped_av

    def test_cast_and_hardness_both_apply_to_cast_plates(self):
        """Both corrections must chain for a cast+hardened plate -- catches the
        session's own mistake of applying only one of the two."""
        plate = ArmorPlate(thickness_mm=52.0, vertical_deg=20.0, cast=True, bhn=480)
        av = plate.av_vs(diameter_mm=75.0)
        slope_only = float(effective_0deg_resistance(52.0, 75.0, 20.0))
        assert av < slope_only  # both corrections should reduce it here
        cast_only = slope_only * cast_deficiency_multiplier(52.0, 75.0)
        assert av < cast_only  # hardness correction must additionally apply on top
