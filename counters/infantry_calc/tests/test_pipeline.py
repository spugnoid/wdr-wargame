import csv

import pytest

from infantry_calc.pipeline import load_units, load_weapons, write_infantry_roster_csv


class TestLoadWeapons:
    """Weapon reference data: name, class, rates of fire, max range.
    The original 7 are from the infantry-counter-design spreadsheet's
    UNIT CALC and UNIT ROSTER sheets. The 9 added 2026-09-11 (M1 Garand
    through Arisaka Type 38/99) support the US/UK/Japan rows added the
    same day from counters/toe/*_1943.md; their practical RPM and max
    range figures are sourced to real-world small-arms references (see
    counters/infantry_calc/README.md's sourcing notes for each), not
    transcribed from the original design spreadsheet."""

    def test_loads_all_sixteen_weapons(self):
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
            "M1 Garand",
            "M1903 Springfield",
            "M1918A2 BAR",
            "M1919A4",
            "Bren",
            "Lee-Enfield",
            "Sten",
            "Type 96/99 LMG",
            "Arisaka Type 38/99",
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
    """The roster as of 2026-09-11: the original 6 German/Soviet units
    (each Front/Rear, 12 rows) plus 4 new units added the same day from
    counters/toe/*_1943.md (US Rifle Squad, UK Rifle Section, Japan Rifle
    Squad, US Light Machine Gun Squad -- each Front/Rear, 8 more rows),
    plus a Soviet Rifle Squad (Pattern B) added shortly after (Front/Rear,
    2 more rows), 22 rows total. The German Grenadier Squad, German
    Panzergrenadier Squad, and Soviet Guards Rifle Squad rows were also
    corrected against newly-sourced TOE research -- see their own `notes`
    column and design notes E.110/E.116."""

    def test_loads_all_twenty_four_rows(self):
        units = load_units()
        assert len(units) == 24

    def test_gren_43_front_face_matches_the_anchor_unit(self):
        """Corrected 2026-09-11: manpower_full 9->10 and a third weapon
        slot (MP40 x1, the squad leader's personal weapon -- present in
        every source checked but absent from the original transcription)
        added, per counters/toe/germany_1943.md. f_number corrected 2->1
        per design note E.109 (F# standardized against Rule 6.6.2's
        table). The MG42 LMG slot itself
        (count=1, practical_rpm=300) is untouched -- it remains the
        system's calibration anchor."""
        units = {u.unit_id: u for u in load_units()}
        gren_f = units["GER_GREN_1943.3_F"]
        assert gren_f.nation == "Germany"
        assert gren_f.unit_type == "Grenadier Squad"
        assert gren_f.face == "F"
        assert gren_f.quality == "regular"
        assert gren_f.manpower_full == 10
        assert gren_f.manpower_reduced == 5
        assert gren_f.m_number == 2
        assert gren_f.f_number == 1
        assert gren_f.g_number == 3
        assert gren_f.verify_status == "ANCHOR"
        assert len(gren_f.loadout) == 3
        assert gren_f.loadout[0].weapon_name == "MG42 LMG (bipod)"
        assert gren_f.loadout[0].count == 1
        assert gren_f.loadout[0].practical_rpm_override is None
        assert gren_f.loadout[1].weapon_name == "Kar98k"
        assert gren_f.loadout[1].count == 7
        assert gren_f.loadout[2].weapon_name == "MP40"
        assert gren_f.loadout[2].count == 1

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
        assert units["GER_GREN_1943.3_F"].source == (
            "Nafziger OOB, TM-E 30-451, MIS Special Series No.9; counters/toe/germany_1943.md"
        )
        assert units["SOV_GDSRIF_1943.3_F"].source == (
            "Red Army shtat 04/551 (Dec 1942, as amended 1943); counters/toe/soviet_union_1943.md"
        )

    def test_invalid_face_value_raises_value_error(self, tmp_path):
        """Confirm that face must be exactly 'F' or 'R', not any other value."""
        csv_path = tmp_path / "units_bad_face.csv"
        # Minimal valid CSV structure with an invalid face value
        csv_path.write_text(
            "unit_id,nation,unit_type,year_bracket,face,quality,"
            "manpower_full,manpower_reduced,weapon1_name,weapon1_count,"
            "weapon1_practical_rpm_override,weapon2_name,weapon2_count,"
            "weapon2_practical_rpm_override,weapon3_name,weapon3_count,"
            "weapon3_practical_rpm_override,m_number,f_number,g_number,"
            "source,verify_status,notes\n"
            "TEST_UNIT_1,TestNation,TestType,1943.3,f,regular,"
            "10,5,Kar98k,4,,,,,,,,2,2,3,TestSource,TEST,\n"
        )
        with pytest.raises(ValueError) as exc_info:
            load_units(path=csv_path)
        assert "face must be 'F' or 'R'" in str(exc_info.value)
        assert "TEST_UNIT_1" in str(exc_info.value)


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
        assert len(rows) == 24

    def test_gren_43_front_face_matches_the_worked_example(self, tmp_path):
        """The MG42 LMG line is untouched by the 2026-09-11 correction --
        still the calibration anchor, still rFP 7. The Kar98k line stays
        at the same rFP (3) despite the count dropping 8->7 (log
        compression rounds both to the same integer). The corrected
        MP40 line (the previously-missing squad leader's weapon) computes
        to a real value but is too low-volume (1 SMG) to clear MIN_RFP --
        it reads 'omit', so the printed counter's visible fire lines are
        unchanged even though the underlying data now correctly models
        the weapon."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["GER_GREN_1943.3_F"]
        assert row["fire_line_1"] == "─● 7 ⬡4 -1"
        assert row["fire_line_2"] == "╌ 3 ⬡5 -1"
        assert row["fire_line_3"] == "omit (rFP too low)"
        assert row["defence"] == "8"
        assert row["morale"] == "5"
        assert row["m_number"] == "2"
        assert row["f_number"] == "1"
        assert row["g_number"] == "3"

    def test_gren_43_rear_face_now_clears_min_rfp(self, tmp_path):
        """Corrected 2026-09-11: the rear face's rifleman count rose from
        4 to 5 (manpower_reduced 4->5, matching the corrected 10-man front
        face's established pattern of losing exactly the crew-served
        weapons on the reduced face, same as every other squad in this
        roster). 5x Kar98k clears MIN_RFP (2) where 4x didn't -- this is a
        real, visible change to the printed counter, not just a metadata
        correction: the reduced-strength Grenadier squad now has an actual
        fire line instead of 'omit'."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["GER_GREN_1943.3_R"]
        assert row["defence"] == "6"
        assert row["fire_line_1"] == "╌ 2 ⬡5 -1"

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

    def test_rear_face_reuses_front_face_interval(self, tmp_path):
        """Rule 3.2.6: the ⬡h interval is identical on both counter faces
        -- weapon physics do not change with crew size. DP-28 team's
        reduced crew has a lower rFP (5 vs 7), which naively recomputes
        to ⬡5; the printed rear face must keep the front face's ⬡3 so a
        crew casualty lowers the whole curve instead of flattening it
        (at ⬡5 the reduced team equalled the full team at range 10)."""
        rows = self._rows_by_unit_id(tmp_path)
        assert rows["SOV_DP28_1943.3_F"]["fire_line_1"] == "─● 7 ⬡3 -1"
        assert rows["SOV_DP28_1943.3_R"]["fire_line_1"] == "─● 5 ⬡3 -1"

    def test_dp28_team_f_number_is_two_not_three(self, tmp_path):
        """Corrected 2026-09-11 per design note E.109: a bipod-mounted LMG
        team's F# (Rule 6.6.2) is 2, matching the same rule's LMG team
        row -- 3 is reserved for a tripod HMG team."""
        rows = self._rows_by_unit_id(tmp_path)
        assert rows["SOV_DP28_1943.3_F"]["f_number"] == "2"

    def test_guards_rifle_squad_now_matches_the_standard_rifle_squad(self, tmp_path):
        """Corrected 2026-09-11 per counters/toe/soviet_union_1943.md:
        no distinct Guards squad organization was found in the sourced
        Red Army shtat documents, so the Guards Rifle Squad's loadout now
        matches the standard Rifle Squad exactly -- only the quality tier
        (veteran vs. regular) distinguishes them, which is enough on its
        own to produce different computed values (higher rFP here than
        SOV_RIFSQ_1943.3_F's ─● 7 ⬡3 -1, and a Mosin-Nagant line that
        clears MIN_RFP for veteran quality where it didn't for regular)."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["SOV_GDSRIF_1943.3_F"]
        assert row["fire_line_1"] == "─● 8 ⬡3 -1"
        assert row["fire_line_2"] == "╌ 3 ⬡4 -1"
        assert row["fire_line_3"] == "≡ 4 ⬡1 -1"

    def test_us_rifle_squad_garand_outperforms_bolt_action_rifle_lines(self, tmp_path):
        """New 2026-09-11, from counters/toe/united_states_1943.md. The
        M1 Garand's semi-automatic practical rate of fire (45 rpm) is
        roughly 3x a bolt-action rifle's (Kar98k/Lee-Enfield/Mosin, all
        12-15 rpm) -- a real, historically-attested US infantry firepower
        advantage that should show up as a materially higher rifle-line
        rFP here (8) than the German Grenadier Squad's Kar98k line (3) at
        an even larger headcount (10 vs 7)."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["US_RIFSQ_1943.3_F"]
        assert row["fire_line_1"] == "─● 5 ⬡3 -1"
        assert row["fire_line_2"] == "╌ 8 ⬡2 -1"
        assert row["fire_line_3"] == "omit (rFP too low)"
        assert row["f_number"] == "1"

    def test_uk_rifle_section_loads_and_computes(self, tmp_path):
        """New 2026-09-11, from counters/toe/united_kingdom_1943.md."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["UK_RIFSEC_1943.3_F"]
        assert row["fire_line_1"] == "─● 4 ⬡4 -1"
        assert row["fire_line_2"] == "╌ 3 ⬡5 -1"
        assert row["fire_line_3"] == "omit (rFP too low)"

    def test_japan_rifle_squad_loads_and_computes(self, tmp_path):
        """New 2026-09-11, from counters/toe/japan_1943.md."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["JPN_RIFSQ_1943.3_F"]
        assert row["fire_line_1"] == "─● 4 ⬡6 -1"
        assert row["fire_line_2"] == "╌ 3 ⬡4 -1"

    def test_towed_at_gun_teams_have_no_fire_lines_but_do_have_defence_and_morale(self, tmp_path):
        """New 2026-09-11 (design notes E.123/E.127): the PaK 40 and 6pdr
        towed anti-tank guns get a printed weapon-team stat block (Rule
        17.1a.1) with no fire-line weapon slots -- their actual attack is
        resolved via armor_calc's PEN/Gunnery Table and Rule 18.8.4's flat
        HE formula, not this pipeline's RPM-based small-arms model. Both
        guns share the same 6-man crew and Regular quality (independently
        converging crew-size sourcing, an explicitly-hedged quality
        inference for both -- see each gun's own counters/toe/*.md file),
        so both rows should compute identical Defence/Morale/M#/F#."""
        rows = self._rows_by_unit_id(tmp_path)
        for unit_id in ("GER_PAK40_1943.3_F", "UK_6PDR_1943.3_F"):
            row = rows[unit_id]
            assert row["fire_line_1"] == ""
            assert row["fire_line_2"] == ""
            assert row["fire_line_3"] == ""
            assert row["defence"] == "6"
            assert row["morale"] == "5"
            assert row["m_number"] == "0"
            assert row["f_number"] == "2"

    def test_us_1919_team_rfp_well_below_mg42_hmg_team(self, tmp_path):
        """New 2026-09-11. The M1919A4's practical rate of fire (150 rpm,
        sourced) is well under half the MG42's (350 rpm) -- a real,
        historically-attested gap (the MG42's belt-fed rate of fire was
        legendary precisely because contemporary Allied MMGs were much
        slower) that produces a correspondingly large rFP gap (6 vs 9)
        between otherwise-parallel tripod HMG team counters. Flagged here
        deliberately -- this is a real game-balance difference between
        the US and German MMG teams, not a copy-paste oversight, and is
        worth a human sanity check before either counter is finalized."""
        rows = self._rows_by_unit_id(tmp_path)
        assert rows["US_MG_1919_1943.3_F"]["fire_line_1"] == "═● 6 ⬡6 -1"
        assert rows["GER_MG42_1943.3_F"]["fire_line_1"] == "═● 9 ⬡6 -1"

    def test_panzergrenadier_squad_now_shows_two_lmg(self, tmp_path):
        """Corrected 2026-09-11 per counters/toe/germany_1943.md (KStN
        1114): the squad carries 2x LMG, not 1 -- a real, visible change
        from the previous 1x MG42 + 6x MP40 loadout, which had no KStN
        citation behind it. The single MP40 (veteran quality) now clears
        MIN_RFP where the Grenadier Squad's own single MP40 (regular
        quality) doesn't -- a quality-tier difference surviving the
        correction, not a new inconsistency."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["GER_PZGR_1943.3_F"]
        assert row["fire_line_1"] == "─● 11 ⬡2 -1"
        assert row["fire_line_3"] == "≡ 2 ⬡3 -1"

    def test_soviet_pattern_b_squad_loads_and_computes(self, tmp_path):
        """New 2026-09-11 per counters/toe/soviet_union_1943.md: the
        second of two equally-common 1943 Soviet squad patterns (2x
        DP-28 instead of Pattern A's 1x) -- a real, higher rFP than
        Pattern A's own DP-28 line (SOV_RIFSQ_1943.3_F's ─● 7 ⬡3 -1)."""
        rows = self._rows_by_unit_id(tmp_path)
        row = rows["SOV_RIFSQ_B_1943.3_F"]
        assert row["fire_line_1"] == "─● 9 ⬡3 -1"
        assert row["fire_line_3"] == "≡ 3 ⬡2 -1"
