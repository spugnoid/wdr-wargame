"""Regression tests for pipeline.py's orchestration logic -- distinct from
test_formulas.py, which validates the underlying physics formulas
themselves against worked examples."""

import pytest

from armor_calc.pipeline import load_hardness_table, load_vehicles


class TestResolveAvFamilyParameter:
    """Session finding (design spec S18/19, 18.12 historical-matchup
    re-run): VehiclePlateRow.resolve_av() used to be hardcoded to the
    "capped" ammo family, silently producing a wrong AV for any other
    attacker family against a face-hardened plate (face_hardened_multiplier
    is family-dependent -- a penalty for capped, a bonus for uncapped AP, no
    correction at all for APBC). Caught when a Soviet APBC gun (T-70's
    45mm) was checked against Panzer IV's face-hardened Hull Front and
    produced Automatic Penetration using the Capped-family figure, which
    should have been a Bounce."""

    def test_panzer_iv_hull_front_av_differs_by_family(self):
        hardness_table = load_hardness_table()
        vehicles = load_vehicles()
        plate = next(
            v for v in vehicles if v.vehicle == "Panzer IV Ausf H" and v.profile == "Hull" and v.arc == "Front"
        )
        assert plate.face_hardened

        av_capped = plate.resolve_av(75.0, hardness_table, family="capped")
        av_apbc = plate.resolve_av(75.0, hardness_table, family="apbc")

        # Face-hardening penalizes capped rounds but doesn't apply to APBC at
        # all -- the APBC figure must therefore be meaningfully higher.
        assert av_capped == pytest.approx(64.9, abs=0.5)
        assert av_apbc == pytest.approx(83.2, abs=0.5)
        assert av_apbc > av_capped

    def test_resolve_av_defaults_to_capped_for_backward_compatibility(self):
        """write_roster_csv and every pre-existing caller relied on the old
        implicit "capped" behavior -- the new family parameter's default
        must reproduce it exactly, not just approximately."""
        hardness_table = load_hardness_table()
        vehicles = load_vehicles()
        plate = next(
            v for v in vehicles if v.vehicle == "Panzer IV Ausf H" and v.profile == "Hull" and v.arc == "Front"
        )
        assert plate.resolve_av(75.0, hardness_table) == plate.resolve_av(75.0, hardness_table, family="capped")

    def test_rounded_mantlet_plate_also_honors_family(self):
        """area_weighted_av() must also thread the family through -- checked
        on a rounded-mantlet vehicle (T-34/85's turret) rather than a flat
        plate, since that path constructs its own ArmorPlate samples
        internally rather than calling av_vs() once."""
        hardness_table = load_hardness_table()
        vehicles = load_vehicles()
        plate = next(
            v for v in vehicles if v.vehicle == "T-34/85 (late 1943)" and v.profile == "Turret" and v.arc == "Front"
        )
        assert plate.rounded_mantlet

        av_capped = plate.resolve_av(75.0, hardness_table, family="capped")
        av_tungsten = plate.resolve_av(75.0, hardness_table, family="hvap76")
        # Different family -> different slope curve -> different result;
        # this would silently pass even if family were ignored unless the
        # two families produce different numbers, so assert they do.
        assert av_capped != pytest.approx(av_tungsten)
