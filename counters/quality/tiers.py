"""Shared quality-tier vocabulary used across every domain in this game
(vehicle crews, infantry units, and any future domain that needs a common
notion of unit experience/training level).

This module intentionally holds only the tier labels and their ordering --
not any formula. Each domain defines its own function mapping a Quality to
its own domain-specific effect (e.g. armor_calc's crew_quality_hit_cap()
caps a hit probability; infantry_calc's quality_multipliers() scales
weapon RPM, Defence, and Morale). Unifying the *labels* means "Veteran"
means the same rank everywhere; unifying the *math* would incorrectly
force two different mechanics to share one formula.
"""

from __future__ import annotations

from typing import Literal

Quality = Literal["elite", "veteran", "regular", "green", "militia"]

ALL_QUALITIES: tuple[Quality, ...] = ("elite", "veteran", "regular", "green", "militia")
