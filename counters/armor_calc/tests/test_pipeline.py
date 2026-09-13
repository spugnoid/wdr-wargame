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


class TestUS57mmAgainstFaceHardenedPlate:
    """New 2026-09-11 (design note E.129, counters/toe/us_57mm_at_1943.md):
    the US 57mm Gun M1 fired only the uncapped AP Shot M70 in 1943 (the
    capped M86/M85 shell didn't reach troops until late summer 1944) --
    ammo_family=ap_uncapped, not capped. face_hardened_multiplier is a real
    penalty for capped rounds but a real BONUS for uncapped AP (face-
    hardening was originally designed to shatter uncapped shot; a cap
    defeats that mechanism), so this gun's AV against a face-hardened German
    plate is genuinely higher than the roster's own av_vs_capped_mm column
    would suggest -- reading that column directly for this gun would
    understate German protection, the same class of mistake note (e) in
    Rule 18.12 already caught and fixed for the T-70's 45mm APBC gun."""

    def test_panzer_iv_hull_front_av_is_much_higher_against_this_guns_uncapped_shot(self):
        hardness_table = load_hardness_table()
        vehicles = load_vehicles()
        plate = next(
            v for v in vehicles if v.vehicle == "Panzer IV Ausf H" and v.profile == "Hull" and v.arc == "Front"
        )
        av_capped = plate.resolve_av(57.0, hardness_table, family="capped")
        av_ap_uncapped = plate.resolve_av(57.0, hardness_table, family="ap_uncapped")
        assert av_ap_uncapped > av_capped + 30  # a real, large gap, not a rounding difference


class TestStuGIIILayeredHullFront:
    """New 2026-09-12 (design note E.138, counters/toe/stug3_panzer_tracts_1943.md):
    Panzer Tracts No.8 (Jentz & Doyle), the authoritative primary source for
    this exact vehicle, states plainly (p.8-26) that the Ausf.G's frontal
    armor is "50 mm base plate with 30 mm face-hardened plates bolted on" --
    a layered composite, not the single homogeneous 80mm plate this project
    had modelled by default absent a source. Same layered_plate_effective_
    thickness() methodology already used for Panzer III's own hull front
    (TestPartialFaceHardening), but with the face-hardened layer on the
    OPPOSITE side (the thinner bolted-on applique, not the thicker base) --
    face_hardened_fraction=30/80, not 50/70."""

    def test_hull_front_is_layered_not_single_plate(self):
        hardness_table = load_hardness_table()
        vehicles = load_vehicles()
        plate = next(
            v for v in vehicles if v.vehicle == "StuG III Ausf G" and v.profile == "Hull" and v.arc == "Front"
        )
        av_layered = plate.resolve_av(75.0, hardness_table)
        # the old single-80mm-plate model gave ~87.1mm -- the layered
        # composite is a real, substantial reduction, not a rounding change.
        assert av_layered < 70.0
        assert av_layered == pytest.approx(64.0, abs=0.5)


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
        """Panzer III, StuG III, SU-85, and Cromwell all came back genuinely
        unsourced or disputed for top armor -- confirms none of them got a
        guessed-at row rather than an honest gap. T-34/85 is excluded from
        this list since design note E.157 sourced its Hull Top (Scheibert,
        Russian T-34 Battle Tank, p.47) -- see the dedicated T-34/85 tests
        below."""
        vehicles = load_vehicles()
        for name in ["Panzer III Ausf M", "StuG III Ausf G", "SU-85", "Cromwell Mk IV"]:
            tops = [v for v in vehicles if v.vehicle == name and v.arc == "Top"]
            assert tops == [], f"{name} should have no Top rows (unsourced)"

    def test_t34_1943_turret_top_intentionally_absent(self):
        """The two candidate turret-roof figures found (20mm vs. 56mm) were
        too far apart to pick between -- Hull Top is sourced, Turret Top is
        deliberately not."""
        vehicles = load_vehicles()
        rows = [v for v in vehicles if v.vehicle == "T-34 Model 1943" and v.arc == "Top"]
        assert [r.profile for r in rows] == ["Hull"]

    def test_t34_85_hull_top_sourced_turret_top_intentionally_absent(self):
        """Design note E.157: Scheibert's Russian T-34 Battle Tank (Schiffer,
        1992, p.47 Technical Data table) sources T-34/85's Hull Top at
        18-22mm (20mm used as the representative midpoint) -- the same
        table's only turret-armor line is a vague aggregate range that
        doesn't distinguish the disputed 20mm-vs-56mm turret roof figures,
        so Turret Top stays deliberately absent, mirroring T-34 Model 1943."""
        vehicles = load_vehicles()
        rows = [v for v in vehicles if v.vehicle == "T-34/85 (late 1943)" and v.arc == "Top"]
        assert [r.profile for r in rows] == ["Hull"]
        assert rows[0].thickness_mm == 20


class TestShermanFireflyLoading:
    """Session finding: Sherman Firefly (the British 17-pdr-on-Sherman
    conversion) was named as a known gap in this roster from the very
    first armor_calc build-out (README "Known gaps", Section 17's own
    intro text, design note E.118). It is a real 1944 vehicle -- entered
    British service ~Jan 1944, combat debut Normandy June 1944 -- and is
    deliberately dated era="1944", the roster's first departure from the
    1943 baseline (not forced into 1943 for consistency's own sake). See
    counters/toe/sherman_firefly_1944.md for full sourcing."""

    def test_loads_with_expected_profile_count_and_era(self):
        vehicles = load_vehicles()
        rows = [v for v in vehicles if v.vehicle == "Sherman Firefly VC"]
        assert len(rows) == 6
        assert all(v.nation == "British" and v.era == "1944" for v in rows)

    def test_hull_front_uses_small_hatch_glacis_not_large_hatch(self):
        """The Firefly's M4A4 hull was never upgraded to the later
        large-hatch glacis this project's existing M4A3(76mm) row uses
        (64mm@47deg) -- it's the earlier, steeper small-hatch plate."""
        vehicles = load_vehicles()
        plate = next(v for v in vehicles if v.vehicle == "Sherman Firefly VC" and v.profile == "Hull" and v.arc == "Front")
        assert plate.thickness_mm == 51
        assert plate.vertical_deg == 56

    def test_turret_front_mantlet_is_13mm_tougher_than_m4a1_baseline(self):
        """The one well-cited, specific number this research pass found:
        Fletcher's Osprey monograph credits the Firefly's mantlet with
        '+13mm of protection' over the standard Sherman mantlet -- modelled
        here as the existing M4A1 turret-front override (89mm) plus that
        sourced delta, a documented stand-in rather than a fresh
        hit-distribution re-weighting (which would need source data this
        project doesn't have access to)."""
        hardness_table = load_hardness_table()
        vehicles = load_vehicles()
        firefly_mantlet = next(
            v for v in vehicles if v.vehicle == "Sherman Firefly VC" and v.profile == "Turret" and v.arc == "Front"
        )
        m4a1_mantlet = next(
            v for v in vehicles if v.vehicle == "Sherman M4A1 (75mm)" and v.profile == "Turret" and v.arc == "Front"
        )
        assert m4a1_mantlet.av_override_mm is not None
        assert firefly_mantlet.av_override_mm == pytest.approx(m4a1_mantlet.av_override_mm + 13, abs=0.01)
        av_firefly = firefly_mantlet.resolve_av(76.2, hardness_table, family="capped")
        av_m4a1 = m4a1_mantlet.resolve_av(76.2, hardness_table, family="capped")
        assert av_firefly == pytest.approx(av_m4a1 + 13, abs=0.01)

    def test_turret_rear_is_the_radio_bustle_box_not_the_base_wall(self):
        """The radio relocated out of the hull into a new armoured bustle
        box bolted to the turret rear (51mm sides / 62mm rear, Sherman
        Minutia) -- a genuine, sourced improvement over the base M4
        turret's 51mm rear wall, not a guess. Side wasn't touched (still
        51mm, matching the base turret casting the Firefly reused)."""
        vehicles = load_vehicles()
        side = next(v for v in vehicles if v.vehicle == "Sherman Firefly VC" and v.profile == "Turret" and v.arc == "Side")
        rear = next(v for v in vehicles if v.vehicle == "Sherman Firefly VC" and v.profile == "Turret" and v.arc == "Rear")
        assert side.thickness_mm == 51
        assert rear.thickness_mm == 62
        assert rear.thickness_mm > side.thickness_mm


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
