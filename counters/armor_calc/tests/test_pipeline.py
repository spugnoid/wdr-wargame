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


class TestBritishVehicleLoading:
    """British guns/vehicles (6pdr, 17pdr, Churchill Mk VII, Cromwell Mk IV)
    were the last major nation-coverage gap flagged in the rules text and
    design spec -- see counters/toe/british_vehicles_1943.md and design
    note E.118 for full sourcing. Unlike every other gun in guns.csv, the
    6pdr/17pdr K-factors are not independently sourced (see
    TestBritishGunCurveFits in test_formulas.py for that methodology and
    its own regression coverage); these tests instead cover that the
    vehicle armor data loads correctly and resolves to sane AV figures."""

    def test_churchill_and_cromwell_load_with_expected_profile_count(self):
        vehicles = load_vehicles()
        churchill = [v for v in vehicles if v.vehicle == "Churchill Mk VII"]
        cromwell = [v for v in vehicles if v.vehicle == "Cromwell Mk IV"]
        # 2 profiles (Hull/Turret) x 3 arcs (Front/Side/Rear) each, plus a
        # Hull/Turret Top pair added for the Sidehill Exposure optional
        # module (Rule 18.2c) -- Churchill has sourced Top data, Cromwell
        # does not (counters/toe/vehicle_top_armor_1943.md), so only
        # Churchill's count includes the extra 2 rows.
        assert len(churchill) == 8
        assert len(cromwell) == 6
        assert all(v.nation == "British" and v.era == "1943" for v in churchill + cromwell)

    def test_churchill_hull_front_is_thick_but_unsloped(self):
        """Churchill VII's hull front (152mm, 0deg) was a deliberately
        heavy, flat plate -- Wikipedia's own text calls it 'not sloped,
        reducing its effectiveness.' Confirms the near-vertical plate isn't
        accidentally getting a slope bonus it shouldn't have."""
        hardness_table = load_hardness_table()
        vehicles = load_vehicles()
        plate = next(v for v in vehicles if v.vehicle == "Churchill Mk VII" and v.profile == "Hull" and v.arc == "Front")
        assert plate.thickness_mm == 152
        assert plate.vertical_deg == 0
        av = plate.resolve_av(76.2, hardness_table, family="capped")
        assert av == pytest.approx(153.1, abs=0.5)

    def test_cromwell_turret_front_cast_penalty_applies(self):
        """Cromwell's turret is cast (a single hexagonal casting per
        counters/toe/british_vehicles_1943.md) -- its resolved AV must come
        out below the raw 76.7mm plate thickness, matching this project's
        existing cast-deficiency treatment for every other cast turret."""
        hardness_table = load_hardness_table()
        vehicles = load_vehicles()
        plate = next(v for v in vehicles if v.vehicle == "Cromwell Mk IV" and v.profile == "Turret" and v.arc == "Front")
        assert plate.cast
        assert plate.thickness_mm is not None
        av = plate.resolve_av(76.2, hardness_table, family="capped")
        assert av < plate.thickness_mm
        assert av == pytest.approx(69.8, abs=0.5)


class TestTopArmorLoading:
    """Session finding (a combined-arms playtest surfaced the sidehill/
    broadside-to-slope exposure question, then a follow-up design
    conversation added a proper mortar/artillery treatment): no vehicle in
    this roster had a Top (deck/roof) profile at all before this pass. Real,
    cited top-armor data now exists for 9 of the 14 roster vehicles
    (counters/toe/vehicle_top_armor_1943.md); the rest are an honest gap,
    same convention as hardness_table.csv's missing nations -- a lookup
    miss means "not modeled yet," not zero or an invented value. Top plates
    are modeled flat (vertical_deg=0), representing the worst-case
    near-perpendicular hit these plates are only ever exposed to under the
    Sidehill Exposure optional rule (18.2c) or, historically, plunging
    fire -- not the near-90-degree obliquity a normal horizontal shot would
    see against a flat deck."""

    def test_tiger_hull_top_loads_and_is_much_weaker_than_hull_side(self):
        """The whole point of the Sidehill Exposure module: Tiger's hull
        side was famously tough (matched good Allied test plate per its own
        sourced note), but its deck was ordinary 25mm plate -- comparing
        against the weaker of the two should be a dramatic difference for
        exactly this vehicle."""
        hardness_table = load_hardness_table()
        vehicles = load_vehicles()
        top = next(v for v in vehicles if v.vehicle == "Tiger I Ausf E" and v.profile == "Hull" and v.arc == "Top")
        side = next(v for v in vehicles if v.vehicle == "Tiger I Ausf E" and v.profile == "Hull" and v.arc == "Side")
        assert top.thickness_mm == 25
        assert top.vertical_deg == 0
        av_top = top.resolve_av(75.0, hardness_table, family="capped")
        av_side = side.resolve_av(75.0, hardness_table, family="capped")
        assert av_top == pytest.approx(24.7, abs=0.5)
        assert av_top < av_side / 2

    def test_panzer_iv_turret_top_uses_reinforced_1943_figure(self):
        hardness_table = load_hardness_table()
        vehicles = load_vehicles()
        top = next(v for v in vehicles if v.vehicle == "Panzer IV Ausf H" and v.profile == "Turret" and v.arc == "Top")
        assert top.thickness_mm == 16
        av = top.resolve_av(75.0, hardness_table, family="capped")
        assert av == pytest.approx(15.8, abs=0.3)

    def test_vehicles_without_sourced_top_data_have_no_top_rows(self):
        """Panzer III, StuG III, T-34/85, SU-85, and Cromwell all came back
        genuinely unsourced or disputed for top armor -- confirms none of
        them got a guessed-at row rather than an honest gap."""
        vehicles = load_vehicles()
        for name in ["Panzer III Ausf M", "StuG III Ausf G", "T-34/85 (late 1943)", "SU-85", "Cromwell Mk IV"]:
            tops = [v for v in vehicles if v.vehicle == name and v.arc == "Top"]
            assert tops == [], f"{name} should have no Top rows (unsourced)"

    def test_t34_1943_turret_top_intentionally_absent(self):
        """The two candidate turret-roof figures found (20mm vs. 56mm) were
        too far apart to pick between -- Hull Top is sourced, Turret Top is
        deliberately not."""
        vehicles = load_vehicles()
        rows = [v for v in vehicles if v.vehicle == "T-34 Model 1943" and v.arc == "Top"]
        assert [r.profile for r in rows] == ["Hull"]


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
    def test_writes_exactly_one_row_per_vehicle_profile(self, tmp_path):
        """Post-conditioning, the split is nearly range- and
        crew-quality-independent, so the table is one row per profile
        (player aid card) rather than a 160-row per-band grid."""
        from armor_calc.pipeline import load_gun_curves, load_hit_zones, write_hit_location_reference_csv

        hit_zones = load_hit_zones()
        curves = load_gun_curves()
        out_path = tmp_path / "hit_location_output.csv"
        write_hit_location_reference_csv(hit_zones, curves, out_path)

        with open(out_path, newline="") as f:
            rows = list(csv.DictReader(f))

        vehicles_profiles = [(r["vehicle"], r["profile"]) for r in rows]
        assert sorted(vehicles_profiles) == sorted(set(vehicles_profiles))
        assert ("Tiger I Ausf E", "Hull") in vehicles_profiles
        assert ("Tiger I Ausf E", "Turret") in vehicles_profiles
        assert ("Sherman M4A1 (75mm)", "Hull") in vehicles_profiles
        assert ("Sherman M4A1 (75mm)", "Turret") in vehicles_profiles

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
