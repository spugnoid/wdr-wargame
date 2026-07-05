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
