import csv

import pytest

from infantry_calc.pipeline import load_units, load_weapons, write_infantry_roster_csv


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


class TestWriteInfantryRosterCsv:
    """Cross-checked against the infantry-counter-design spreadsheet's
    own UNIT ROSTER sheet -- every expected value below was read directly
    from that sheet's own computed cells, not re-derived from the
    formulas under test (that would make this a tautology, not a
    validation)."""

    def _rows_by_unit_id(self, tmp_path):
        out_path = tmp_path / "infantry_roster_output.csv"
        write_infantry_roster_csv(load_weapons(), load_units(), out_path)
        with open(out_path, newline="") as f:
            return {r["unit_id"]: r for r in csv.DictReader(f)}

    def test_writes_one_row_per_unit(self, tmp_path):
        rows = self._rows_by_unit_id(tmp_path)
        assert len(rows) == 12

    def test_gren_43_front_face_matches_the_worked_example(self, tmp_path):
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["GER_GREN_1943.3_F"]
        assert row["fire_line_1"] == "─● 7 ⬡4 -1"
        assert row["fire_line_2"] == "╌ 3 ⬡5 -1"
        assert row["defence"] == "8"
        assert row["morale"] == "5"
        assert row["m_number"] == "2"
        assert row["f_number"] == "2"
        assert row["g_number"] == "3"

    def test_gren_43_rear_face_defence_is_front_minus_two(self, tmp_path):
        """4x Kar98k alone computes to rFP 1 -- below MIN_RFP (2), so this
        fire line reads 'omit', not a printed '1 ⬡15 -1' notation (matches
        the source spreadsheet's own UNIT ROSTER cell BX5)."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["GER_GREN_1943.3_R"]
        assert row["defence"] == "6"
        assert row["fire_line_1"] == "omit (rFP too low)"

    def test_mg42_team_rear_face_uses_the_practical_rpm_override(self, tmp_path):
        """This unit's loadout entry overrides practical RPM to 250
        (vs. the weapon's own default of 350) -- confirms the override
        actually flows into the rFP calculation, not just get parsed."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["GER_MG42_1943.3_R"]
        assert row["fire_line_1"] == "═● 8 ⬡6 -1"
        assert row["defence"] == "3"

    def test_soviet_rifle_squad_rear_face_below_min_rfp_is_omitted(self, tmp_path):
        """SOV_RIFSQ_1943.3_R's lone weapon (4x Mosin-Nagant) computes to
        rFP 0 -- below MIN_RFP, so the fire line reads 'omit', not a
        bogus '0 ⬡- -1' notation."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["SOV_RIFSQ_1943.3_R"]
        assert row["fire_line_1"] == "omit (rFP too low)"

    def test_rifle_squad_front_face_has_three_fire_lines(self, tmp_path):
        """The Mosin-Nagant slot (weapon2, 6x, rFP 1) is below MIN_RFP and
        reads 'omit', not a printed notation -- matches the source
        spreadsheet's own UNIT ROSTER cell BY12. Only the DP-28 and
        PPSh-41 slots clear the threshold."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["SOV_RIFSQ_1943.3_F"]
        assert row["fire_line_1"] == "─● 7 ⬡3 -1"
        assert row["fire_line_2"] == "omit (rFP too low)"
        assert row["fire_line_3"] == "≡ 3 ⬡2 -1"
