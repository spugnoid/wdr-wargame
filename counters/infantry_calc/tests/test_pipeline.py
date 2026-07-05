import csv

import pytest

from infantry_calc.pipeline import load_weapons


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
