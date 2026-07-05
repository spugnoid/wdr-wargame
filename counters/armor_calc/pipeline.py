"""CSV-driven orchestration: reads gun/vehicle data, runs the formulas, writes results.

Source data (editable like a spreadsheet, no Python required to update):
  data/guns.csv             -- one row per gun+ammo-nature
  data/gun_calibration.csv  -- one row per attested penetration data point
  data/vehicles.csv         -- one row per vehicle arc-profile plate
  data/hardness_table.csv   -- BHN by nation/armor-type/era/thickness bracket
  data/hit_zones.csv        -- one row per vehicle hit-location zone (profile/arc/classification)

Run: PYTHONPATH=counters python3 -m armor_calc.pipeline (from the repo root)
Output: counters/armor_calc/roster_output.csv
"""

from __future__ import annotations

import csv
import pathlib
from dataclasses import dataclass

import numpy as np

from .formulas import (
    ALL_CREW_QUALITIES,
    AmmoFamily,
    ArmorPlate,
    FlawSeverity,
    GunCurveFit,
    HitZone,
    area_weighted_av,
    base_hit_probability,
    classify_hit_location,
    crew_quality_hit_cap,
    crossing_target_ratio,
    fit_gun_curve,
    flight_time,
    heat_effective_resistance,
    hit_location_thresholds,
    hit_probability,
    rounded_mantlet_angle_distribution,
    vehicle_fire_thresholds,
)

# Representative tungsten family for the roster's single D_ref=75mm attacker
# convention. Only 90mm HVAP, 76mm HVAP, and APDS (calibre-independent) are
# sourced (Appendix 16) -- 76mm HVAP is the closest analog to a 75mm-class
# gun, same "borrow the nearest sourced curve" approach already used for
# individual guns (design spec §7). A gun-specific roster would pick its own
# nearest analog instead of this one global default.
DEFAULT_TUNGSTEN_FAMILY: AmmoFamily = "hvap76"

# Fixed seed for Hit Location Table Monte Carlo classification.
# The printed table must be reproducible run-to-run (design principle: "one
# stable printed table, roll once, read the result" -- see superpowers plan
# 2026-07-04-hit-location-and-crew-position.md). Without a fixed seed, the
# CSV's own thresholds would drift on regeneration, undermining this principle.
_HIT_LOCATION_RNG_SEED = 20260704

DATA_DIR = pathlib.Path(__file__).parent / "data"


@dataclass(frozen=True)
class HardnessRow:
    nation: str
    armor_type: str
    era: str
    thickness_min_mm: float
    thickness_max_mm: float
    bhn: float


def load_hardness_table(path: pathlib.Path = DATA_DIR / "hardness_table.csv") -> list[HardnessRow]:
    """Load the BHN-by-thickness-bracket table.

    Nations with no rows here (e.g. German, American, British as of this
    writing -- see design spec §7) simply produce no match, which
    lookup_bhn() treats as "no high-hardness correction" rather than an
    error. That is a real evidentiary gap, not a claim those nations'
    armor is definitely at baseline hardness -- see the spec for why.
    """
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append(
                HardnessRow(
                    nation=r["nation"],
                    armor_type=r["armor_type"],
                    era=r["era"],
                    thickness_min_mm=float(r["thickness_min_mm"]),
                    thickness_max_mm=float(r["thickness_max_mm"]),
                    bhn=float(r["bhn"]),
                )
            )
    return rows


def lookup_bhn(
    nation: str, armor_type: str, era: str, thickness_mm: float, table: list[HardnessRow]
) -> float | None:
    """Find the BHN for a plate, or None if this nation/type has no sourced data."""
    for row in table:
        if row.nation != nation or row.armor_type != armor_type:
            continue
        if row.era != "any" and row.era != era:
            continue
        if row.thickness_min_mm <= thickness_mm <= row.thickness_max_mm:
            return row.bhn
    return None


@dataclass(frozen=True)
class VehiclePlateRow:
    vehicle: str
    profile: str  # "Hull" or "Turret"
    arc: str  # "Front", "Side", "Rear"
    thickness_mm: float | None
    vertical_deg: float | None
    lateral_deg: float
    cast: bool
    nation: str
    era: str
    bhn_override: float | None
    av_override_mm: float | None
    flaw_severity: FlawSeverity | None
    heat_thickness_mm: float | None
    heat_vertical_deg: float | None
    schurzen: bool
    face_hardened: bool
    face_hardened_fraction: float | None
    rounded_mantlet: bool
    notes: str

    def _resolved_bhn(self, hardness_table: list[HardnessRow]) -> float | None:
        if self.bhn_override is not None:
            return self.bhn_override
        assert self.thickness_mm is not None
        armor_type = "cast" if self.cast else "rolled"
        return lookup_bhn(self.nation, armor_type, self.era, self.thickness_mm, hardness_table)

    def resolve_av(
        self, diameter_mm: float, hardness_table: list[HardnessRow], family: AmmoFamily = "capped"
    ) -> float:
        """AV for this plate against a given attacker ammo family, fully corrected, mm.

        Defaults to "capped" -- this is what `write_roster_csv` uses for the
        printed `av_vs_capped_mm` column, and what every caller used
        implicitly before this parameter existed. Pass `family="apbc"` or
        `family="ap_uncapped"` explicitly for a matchup or validation script
        that needs the correct AV against one of those attacker families
        specifically -- do NOT reuse `av_vs_capped_mm` (or this method's own
        default) for them.

        This distinction is not academic: `face_hardened_multiplier()` is
        family-dependent (a real penalty for capped rounds, a real bonus for
        uncapped AP, no correction at all for APBC), so a face-hardened
        plate's AV genuinely differs by attacker family -- e.g. Panzer IV
        Ausf H's Hull Front is 64.9mm vs. Capped but 83.2mm vs. APBC.
        Reusing the Capped-family figure for an APBC attacker (as an early
        pass at the 18.12 historical-matchup re-run did, against T-70's
        45mm gun) silently produces a wrong answer -- caught and corrected
        this session, see design spec §18/19.

        `av_override_mm`, where set (Tiger/Sherman M4A1/Panther mantlets),
        does NOT vary by family -- those figures were precomputed by hand
        for a Capped-family attacker only, and none of those three plates
        are face-hardened, so this is not currently a live bug, but it IS a
        known limitation: if a future override-based plate is ever also
        face-hardened, its override figure will be wrong for
        APBC/uncapped-AP attackers and nothing here will catch it.

        If `rounded_mantlet` is set, vertical_deg is ignored in favor of the
        general rounded-mantlet angle distribution (Ch.11) -- see
        area_weighted_av()'s docstring and design spec §18 for which
        vehicles use this vs. a single fixed angle.
        """
        if self.av_override_mm is not None:
            return self.av_override_mm
        assert self.thickness_mm is not None and self.vertical_deg is not None
        plate = ArmorPlate(
            thickness_mm=self.thickness_mm,
            vertical_deg=self.vertical_deg,
            lateral_deg=self.lateral_deg,
            cast=self.cast,
            bhn=self._resolved_bhn(hardness_table),
            flaw_severity=self.flaw_severity,
            face_hardened=self.face_hardened,
            face_hardened_fraction=self.face_hardened_fraction,
        )
        if self.rounded_mantlet:
            return area_weighted_av(plate, diameter_mm, rounded_mantlet_angle_distribution(), family=family)
        return plate.av_vs(diameter_mm, family=family)

    def resolve_av_tungsten(
        self, diameter_mm: float, hardness_table: list[HardnessRow], family: AmmoFamily = DEFAULT_TUNGSTEN_FAMILY
    ) -> float:
        """AV-vs-Tungsten for this plate, mm.

        Reuses the cast/high-hardness/flaw multipliers exactly as computed
        for capped rounds -- none of the three sourced tungsten curves came
        with their own cast/hardness/flaw corrections, so this applies the
        best available (capped-derived) correction rather than none. That is
        a real, flagged assumption: Ch.2's own discussion notes tungsten
        cores can behave differently against very hard plate (sometimes
        worse, via core shatter, not just better) -- not modelled here.

        Falls back to heat_thickness_mm/heat_vertical_deg for plates whose
        AV-vs-Capped was pre-resolved from a distribution/edge-effect table
        (Tiger/Sherman/Panther mantlets) -- same single-plate approximation
        used for AV-vs-HEAT, for the same reason (no tungsten-specific
        edge-effect data exists for those mantlets either).
        """
        if self.av_override_mm is not None:
            t = self.heat_thickness_mm
            v = self.heat_vertical_deg
        else:
            t = self.thickness_mm
            v = self.vertical_deg
        assert t is not None and v is not None
        plate = ArmorPlate(
            thickness_mm=t,
            vertical_deg=v,
            lateral_deg=self.lateral_deg,
            cast=self.cast,
            bhn=self._resolved_bhn(hardness_table) if self.thickness_mm is not None else None,
            flaw_severity=self.flaw_severity,
            face_hardened=self.face_hardened,
            face_hardened_fraction=self.face_hardened_fraction,
        )
        if self.rounded_mantlet and self.av_override_mm is None:
            return area_weighted_av(plate, diameter_mm, rounded_mantlet_angle_distribution(), family=family)
        return plate.av_vs(diameter_mm, family=family)

    def resolve_av_heat(self) -> float:
        """AV-vs-HEAT for this plate, mm.

        Uses heat_thickness_mm/heat_vertical_deg if set (needed for plates
        like Tiger/Panther/Sherman mantlets whose AV-vs-Capped was
        pre-resolved from a distribution/edge-effect table rather than a
        single thickness+angle -- see vehicles.csv notes for each). Those
        cases use a single-plate approximation of the mantlet's real
        thickness, not the same spaced/curved-geometry treatment the
        capped-round figure got -- a known simplification, not a claim the
        two are equally rigorous.
        """
        t = self.heat_thickness_mm if self.heat_thickness_mm is not None else self.thickness_mm
        v = self.heat_vertical_deg if self.heat_vertical_deg is not None else self.vertical_deg
        assert t is not None and v is not None
        return heat_effective_resistance(t, v, self.lateral_deg)


@dataclass(frozen=True)
class HitZoneRow:
    vehicle: str
    profile: str  # "Hull" or "Turret"
    arc: str  # "Front" only, this phase
    zone: HitZone


def load_hit_zones(path: pathlib.Path = DATA_DIR / "hit_zones.csv") -> list[HitZoneRow]:
    """Load per-vehicle hit-location zone geometry.

    See that CSV's own notes column for provenance -- neither project
    source provides interior vehicle layout diagrams, so this data is
    general historical knowledge, not project-source-cited.
    """
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append(
                HitZoneRow(
                    vehicle=r["vehicle"],
                    profile=r["profile"],
                    arc=r["arc"],
                    zone=HitZone(
                        name=r["zone_name"],
                        classification=r["classification"],  # type: ignore[arg-type]
                        x_min=float(r["x_min_m"]),
                        x_max=float(r["x_max_m"]),
                        y_min=float(r["y_min_m"]),
                        y_max=float(r["y_max_m"]),
                    ),
                )
            )
    return rows


def _parse_optional_float(value: str) -> float | None:
    return float(value) if value.strip() else None


def load_vehicles(path: pathlib.Path = DATA_DIR / "vehicles.csv") -> list[VehiclePlateRow]:
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append(
                VehiclePlateRow(
                    vehicle=r["vehicle"],
                    profile=r["profile"],
                    arc=r["arc"],
                    thickness_mm=_parse_optional_float(r["thickness_mm"]),
                    vertical_deg=_parse_optional_float(r["vertical_deg"]),
                    lateral_deg=float(r["lateral_deg"] or 0.0),
                    cast=r["cast"].strip().lower() == "true",
                    nation=r["nation"],
                    era=r["era"],
                    bhn_override=_parse_optional_float(r["bhn_override"]),
                    av_override_mm=_parse_optional_float(r["av_override_mm"]),
                    flaw_severity=(r.get("flaw_severity", "").strip() or None),  # type: ignore[arg-type]
                    heat_thickness_mm=_parse_optional_float(r.get("heat_thickness_mm", "")),
                    heat_vertical_deg=_parse_optional_float(r.get("heat_vertical_deg", "")),
                    schurzen=r.get("schurzen", "").strip().lower() == "true",
                    face_hardened=r.get("face_hardened", "").strip().lower() == "true",
                    face_hardened_fraction=_parse_optional_float(r.get("face_hardened_fraction", "")),
                    rounded_mantlet=r.get("rounded_mantlet", "").strip().lower() == "true",
                    notes=r["notes"],
                )
            )
    return rows


def load_gun_curves(
    guns_path: pathlib.Path = DATA_DIR / "guns.csv",
    calibration_path: pathlib.Path = DATA_DIR / "gun_calibration.csv",
) -> dict[str, GunCurveFit]:
    """Fit every gun+ammo pair in guns.csv against its calibration data."""
    calib_by_gun: dict[str, list[tuple[float, float, float]]] = {}
    with open(calibration_path, newline="") as f:
        for r in csv.DictReader(f):
            calib_by_gun.setdefault(r["gun_id"], []).append(
                (float(r["range_m"]), float(r["pen_mm"]), float(r["angle_deg"]))
            )

    curves: dict[str, GunCurveFit] = {}
    with open(guns_path, newline="") as f:
        for r in csv.DictReader(f):
            gun_id = r["gun_id"]
            points = calib_by_gun[gun_id]
            ranges = [p[0] for p in points]
            pens = [p[1] for p in points]
            angle = points[0][2]  # assumes one calibration angle per gun, true for all guns so far
            curves[gun_id] = fit_gun_curve(
                muzzle_velocity_fps=float(r["muzzle_velocity_fps"]),
                k_factor=float(r["k_factor"]),
                calibration_ranges_m=ranges,
                calibration_pens_mm=pens,
                calibration_angle_deg=angle,
                projectile_diameter_mm=float(r["projectile_diameter_mm"]),
                family=r["ammo_family"],
            )
    return curves


def write_roster_csv(
    vehicles: list[VehiclePlateRow],
    hardness_table: list[HardnessRow],
    diameter_mm: float,
    out_path: pathlib.Path,
    tungsten_family: AmmoFamily = DEFAULT_TUNGSTEN_FAMILY,
) -> None:
    """Compute AV-vs-Capped, AV-vs-Tungsten, and AV-vs-HEAT for every plate.

    The `schurzen` column is a pass-through flag, not a computed value.
    Schürzen halves the *attacker's* HEAT PEN against a protected arc
    (formulas.heat_pen_vs_schurzen) rather than boosting this plate's own
    av_vs_heat_mm, so it is not folded into that column here -- it is
    printed as its own flag for the rule text to reference directly. See
    design spec §16.

    The `face_hardened` column, by contrast, IS already folded into
    av_vs_capped_mm/av_vs_tungsten_mm (via ArmorPlate.av_vs's own chain) --
    it is printed alongside them purely so a designer can see which plates
    received the correction, not because a separate rule-text reference
    needs it the way schurzen does.
    """
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "vehicle",
                "profile",
                "arc",
                "av_vs_capped_mm",
                "av_vs_tungsten_mm",
                "av_vs_heat_mm",
                "d_ref_mm",
                "schurzen",
                "face_hardened",
                "rounded_mantlet",
                "notes",
            ]
        )
        for v in vehicles:
            av = v.resolve_av(diameter_mm, hardness_table)
            av_tungsten = v.resolve_av_tungsten(diameter_mm, hardness_table, tungsten_family)
            av_heat = v.resolve_av_heat()
            writer.writerow(
                [
                    v.vehicle,
                    v.profile,
                    v.arc,
                    round(av, 1),
                    round(av_tungsten, 1),
                    round(av_heat, 1),
                    diameter_mm,
                    v.schurzen,
                    v.face_hardened_fraction if v.face_hardened_fraction is not None else v.face_hardened,
                    v.rounded_mantlet,
                    v.notes,
                ]
            )


def write_heat_reference_csv(out_path: pathlib.Path) -> None:
    """The small universal player-aid-card table: angle -> HEAT multiplier.

    One table for the whole game, applied to a vehicle's raw thickness --
    see heat_multiplier()'s docstring for why HEAT doesn't need a per-vehicle
    AV column the way capped/tungsten rounds do.
    """
    from .formulas import heat_reference_table

    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["angle_deg", "heat_multiplier"])
        for angle, mult in heat_reference_table():
            writer.writerow([angle, round(mult, 3)])


def write_shatter_gap_reference_csv(out_path: pathlib.Path) -> None:
    """The small universal advanced-rule player-aid table: AV -> the PEN
    window (mm) in which a shot shatter-fails despite over-penetrating.

    Optional/advanced module (design spec) -- not part of the core 18.2
    resolution table, kept as its own small reference rather than adding
    two more numbers to every vehicle counter.
    """
    from .formulas import shatter_gap_reference_table

    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["av_mm", "shatter_window_lower_mm", "shatter_window_upper_mm"])
        for av, lower, upper in shatter_gap_reference_table():
            writer.writerow([av, round(lower, 1), round(upper, 1)])


def write_gun_curves_csv(curves: dict[str, GunCurveFit], out_path: pathlib.Path) -> None:
    """Write range-band PEN values for every gun, matching the counter ready-reckoner format."""
    bands = [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2500]
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["gun_id", "confidence", *[f"pen_{b}m" for b in bands]])
        for gun_id, fit in curves.items():
            values = [round(float(fit.pen_0deg(max(b, 1))), 1) for b in bands]
            writer.writerow([gun_id, fit.confidence, *values])


def write_hit_probability_csv(curves: dict[str, GunCurveFit], out_path: pathlib.Path) -> None:
    """Base (uncapped) first-shot hit% by range band, per gun.

    Uncapped -- a specific unit applies its own crew-quality cap
    (crew_quality_from_morale + crew_quality_hit_cap) on top of this,
    same "gun-specific ready-reckoner, universal modifier applied at the
    table" split used for AV-vs-Capped/Tungsten vs. the HEAT reference.
    """
    bands = [100, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2500]
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["gun_id", *[f"hit_pct_{b}m" for b in bands]])
        for gun_id, fit in curves.items():
            values = [round(base_hit_probability(flight_time(fit.muzzle_velocity_fps, fit.k_factor, b)), 1) for b in bands]
            writer.writerow([gun_id, *values])


def write_gunnery_reference_csv(out_path: pathlib.Path) -> None:
    """The small universal reference tables for the player aid card:
    crew-quality hit caps, and the target-crossing ratio by range."""
    bands_yd = [400, 800, 1200, 1600, 2000]
    yd_to_m = 0.9144
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["crew_quality", "max_hit_pct"])
        for q in ALL_CREW_QUALITIES:
            writer.writerow([q, round(crew_quality_hit_cap(q) * 100, 0)])
        writer.writerow([])
        writer.writerow(["range_yd", "crossing_ratio_first_shot", "crossing_ratio_follow_up"])
        for ryd in bands_yd:
            rm = ryd * yd_to_m
            writer.writerow([ryd, round(crossing_target_ratio(rm), 2), round(crossing_target_ratio(rm, follow_up=True), 2)])


def write_vehicle_fire_thresholds_csv(curves: dict[str, GunCurveFit], out_path: pathlib.Path) -> None:
    """The actual unified table (design spec §11): per gun, per range band,
    per crew quality, the two 1d6+1d8+1d12 thresholds that resolve
    Miss/Turret/Hull in one roll. "None" means that band is unreachable at
    this range (e.g. miss_threshold=None -> automatic miss; hull_threshold
    None but miss_threshold set -> every possible hit lands on the turret).
    """
    bands = [100, 250, 500, 750, 1000, 1500, 2000, 2500]
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["gun_id", "crew_quality", "range_m", "miss_below", "hull_at_or_above"])
        for gun_id, fit in curves.items():
            for quality in ALL_CREW_QUALITIES:
                for rm in bands:
                    t = vehicle_fire_thresholds(fit.muzzle_velocity_fps, fit.k_factor, rm, quality)
                    writer.writerow([gun_id, quality, rm, t.miss_threshold, t.hull_threshold])


def write_hit_location_reference_csv(
    hit_zones: list[HitZoneRow],
    curves: dict[str, GunCurveFit],
    out_path: pathlib.Path,
    representative_gun_id: str = "pziv_75l48_apcbc",
) -> None:
    """The Hit Location Table: per vehicle, per profile (Hull/Turret), per
    range band, per crew quality, the two thresholds that resolve
    Neither/Gun/Mobility in one roll when a Casualty result occurs
    (Rule 18.6a).

    Uses a single representative attacking gun (default: the roster's
    75mm KwK40) to compute the hit% that drives scatter width, rather
    than a separate table per attacking gun -- the same simplification
    already used for the AV-vs-Capped columns (diameter_mm=75.0
    representative attacker). A real per-gun table is a reasonable future
    expansion, not built in this pilot -- see design spec open items.
    """
    bands = [100, 250, 500, 750, 1000, 1500, 2000, 2500]
    fit = curves[representative_gun_id]

    zones_by_vehicle_profile: dict[tuple[str, str], list[HitZone]] = {}
    for row in hit_zones:
        zones_by_vehicle_profile.setdefault((row.vehicle, row.profile), []).append(row.zone)

    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["vehicle", "profile", "crew_quality", "range_m", "mobility_pct", "gun_pct", "neither_pct",
             "neither_below", "mobility_at_or_above"]
        )
        for (vehicle, profile), zones in zones_by_vehicle_profile.items():
            for quality in ALL_CREW_QUALITIES:
                for range_m in bands:
                    hit_pct = hit_probability(fit.muzzle_velocity_fps, fit.k_factor, range_m, quality)
                    split = classify_hit_location(
                        zones, hit_pct, rng=np.random.default_rng(_HIT_LOCATION_RNG_SEED)
                    )
                    thresholds = hit_location_thresholds(split)
                    writer.writerow(
                        [
                            vehicle, profile, quality, range_m,
                            round(split["mobility"], 1), round(split["gun"], 1), round(split["neither"], 1),
                            thresholds.neither_threshold, thresholds.gun_threshold,
                        ]
                    )


def main(diameter_mm: float = 75.0) -> None:
    hardness_table = load_hardness_table()
    vehicles = load_vehicles()
    curves = load_gun_curves()

    write_roster_csv(vehicles, hardness_table, diameter_mm, DATA_DIR.parent / "roster_output.csv")
    write_gun_curves_csv(curves, DATA_DIR.parent / "gun_curves_output.csv")
    write_heat_reference_csv(DATA_DIR.parent / "heat_reference_output.csv")
    write_shatter_gap_reference_csv(DATA_DIR.parent / "shatter_gap_reference_output.csv")
    write_hit_probability_csv(curves, DATA_DIR.parent / "hit_probability_output.csv")
    write_gunnery_reference_csv(DATA_DIR.parent / "gunnery_reference_output.csv")
    write_vehicle_fire_thresholds_csv(curves, DATA_DIR.parent / "vehicle_fire_thresholds_output.csv")
    hit_zones = load_hit_zones()
    write_hit_location_reference_csv(hit_zones, curves, DATA_DIR.parent / "hit_location_output.csv")
    print(f"Wrote all armor_calc outputs to {DATA_DIR.parent}")


if __name__ == "__main__":
    main()
