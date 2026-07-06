from viz import data


def test_vehicle_names_includes_known_vehicles():
    names = data.vehicle_names()
    assert "Tiger I Ausf E" in names
    assert "Panther Ausf G" in names
    assert len(names) == len(set(names))  # no duplicates


def test_vehicle_armor_for_returns_hull_and_turret_front_only():
    result = data.vehicle_armor_for(["Tiger I Ausf E"])
    assert list(result.columns) == ["vehicle", "profile", "av_mm"]
    assert set(result["profile"]) == {"Hull", "Turret"}
    assert len(result) == 2  # exactly one Hull row, one Turret row


def test_vehicle_armor_for_known_value():
    # Spot-check against a value already verified elsewhere in this
    # project (Section 19.7's vehicle counter table).
    result = data.vehicle_armor_for(["Tiger I Ausf E"])
    hull_row = result[result["profile"] == "Hull"].iloc[0]
    assert hull_row["av_mm"] == 102.0


def test_vehicle_armor_for_respects_av_column_choice():
    capped = data.vehicle_armor_for(["Tiger I Ausf E"], av_column="av_vs_capped_mm")
    tungsten = data.vehicle_armor_for(["Tiger I Ausf E"], av_column="av_vs_tungsten_mm")
    # Different columns should (at least for this vehicle) give different
    # numbers -- confirms the av_column argument actually changes the result.
    assert not capped["av_mm"].equals(tungsten["av_mm"])


def test_gun_ids_includes_known_guns():
    ids = data.gun_ids()
    assert "tiger_88_apcbc" in ids
    assert "pziv_75l48_apcbc" in ids


def test_gun_curve_long_covers_all_range_bands_for_each_gun():
    result = data.gun_curve_long(["tiger_88_apcbc", "pziv_75l48_apcbc"])
    assert list(result.columns) == ["gun_id", "range_m", "pen_mm"]
    assert len(result) == 2 * len(data.PEN_RANGE_COLUMNS)
    assert set(result["range_m"]) == set(data.PEN_RANGE_COLUMNS.values())


def test_gun_curve_long_only_includes_requested_guns():
    result = data.gun_curve_long(["tiger_88_apcbc"])
    assert set(result["gun_id"]) == {"tiger_88_apcbc"}


def test_infantry_unit_ids_includes_known_units():
    ids = data.infantry_unit_ids()
    assert "GER_GREN_1943.3_F" in ids
    assert "SOV_RIFSQ_1943.3_F" in ids


def test_infantry_stats_for_covers_all_numeric_columns_for_each_unit():
    result = data.infantry_stats_for(["GER_GREN_1943.3_F", "SOV_RIFSQ_1943.3_F"])
    assert list(result.columns) == ["unit_id", "stat", "value"]
    assert len(result) == 2 * len(data.INFANTRY_NUMERIC_COLUMNS)
    assert set(result["stat"]) == set(data.INFANTRY_NUMERIC_COLUMNS)


def test_infantry_fire_lines_for_returns_expected_columns():
    result = data.infantry_fire_lines_for(["GER_GREN_1943.3_F"])
    assert list(result.columns) == [
        "unit_id",
        "fire_line_1",
        "fire_line_2",
        "fire_line_3",
    ]
    assert len(result) == 1
