"""Regression tests for pipeline.py's orchestration logic -- distinct from
test_formulas.py, which validates the underlying physics formulas
themselves against worked examples."""

import csv

import pytest

from armor_calc.pipeline import load_hardness_table, load_hit_zones, load_vehicles


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
