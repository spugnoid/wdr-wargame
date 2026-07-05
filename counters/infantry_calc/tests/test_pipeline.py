import csv

import pytest

from infantry_calc.pipeline import load_units, load_weapons


class TestLoadWeapons:
    """Weapon reference data: name, class, rates of fire, max range.
    Source: infantry-counter-design spreadsheet's UNIT CALC and UNIT
    ROSTER sheets' weapon-loadout columns, deduplicated to one row per
    distinct weapon."""

    def test_loads_all_seven_pilot_weapons(self):
        weapons = load_weapons()
        names = {w.name for w in weapons}
        assert names == {
            "MG42 LMG (bipod)",
            "MG42 HMG (tripod)",
            "Kar98k",
            "Mosin-Nagant",
            "MP40",
            "PPSh-41",
            "DP-28",
        }

    def test_mg42_lmg_matches_the_worked_example(self):
        weapons = {w.name: w for w in load_weapons()}
        mg42_lmg = weapons["MG42 LMG (bipod)"]
        assert mg42_lmg.weapon_class == "lmg"
        assert mg42_lmg.cyclic_rpm == 1200
        assert mg42_lmg.practical_rpm == 300
        assert mg42_lmg.max_range_yds == 1000

    def test_kar98k_is_a_rifle(self):
        weapons = {w.name: w for w in load_weapons()}
        kar98k = weapons["Kar98k"]
        assert kar98k.weapon_class == "rifle"
        assert kar98k.practical_rpm == 15
        assert kar98k.max_range_yds == 600


class TestLoadUnits:
    """The pilot roster: 6 units (German Grenadier/Panzergrenadier/MG42
    team, Soviet Guards Rifle/Rifle/DP-28 team), each with a Front and
    Rear face -- 12 rows total. Source: infantry-counter-design
    spreadsheet's UNIT ROSTER sheet."""

    def test_loads_all_twelve_rows(self):
        units = load_units()
        assert len(units) == 12

    def test_gren_43_front_face_matches_the_anchor_unit(self):
        units = {u.unit_id: u for u in load_units()}
        gren_f = units["GER_GREN_1943.3_F"]
        assert gren_f.nation == "Germany"
        assert gren_f.unit_type == "Grenadier Squad"
        assert gren_f.face == "F"
        assert gren_f.quality == "regular"
        assert gren_f.manpower_full == 9
        assert gren_f.manpower_reduced == 4
        assert gren_f.m_number == 2
        assert gren_f.f_number == 2
        assert gren_f.g_number == 3
        assert gren_f.verify_status == "ANCHOR"
        assert len(gren_f.loadout) == 2
        assert gren_f.loadout[0].weapon_name == "MG42 LMG (bipod)"
        assert gren_f.loadout[0].count == 1
        assert gren_f.loadout[0].practical_rpm_override is None
        assert gren_f.loadout[1].weapon_name == "Kar98k"
        assert gren_f.loadout[1].count == 8

    def test_weapon_team_rear_face_has_a_practical_rpm_override(self):
        """GER_MG42_1943.3_R: 2-man reduced crew, same MG42 HMG but a
        slower practical rate of fire (250 vs. the front face's 350) --
        the one case in the pilot roster where a unit's own loadout
        entry overrides the weapon's default practical RPM."""
        units = {u.unit_id: u for u in load_units()}
        mg42_r = units["GER_MG42_1943.3_R"]
        assert len(mg42_r.loadout) == 1
        assert mg42_r.loadout[0].weapon_name == "MG42 HMG (tripod)"
        assert mg42_r.loadout[0].practical_rpm_override == 250

    def test_rifsq_front_face_has_three_weapon_slots(self):
        """SOV_RIFSQ_1943.3_F: DP-28 + Mosin-Nagant + PPSh-41 -- the
        widest loadout in the pilot roster, confirms all three slots
        parse, not just the first two."""
        units = {u.unit_id: u for u in load_units()}
        rifsq_f = units["SOV_RIFSQ_1943.3_F"]
        assert [slot.weapon_name for slot in rifsq_f.loadout] == [
            "DP-28",
            "Mosin-Nagant",
            "PPSh-41",
        ]

    def test_a_units_source_citation_is_preserved(self):
        units = {u.unit_id: u for u in load_units()}
        assert units["GER_GREN_1943.3_F"].source == "Nafziger OOB, TM-E 30-451"
        assert units["SOV_GDSRIF_1943.3_F"].source == "STAVKA TO&E 1943"
