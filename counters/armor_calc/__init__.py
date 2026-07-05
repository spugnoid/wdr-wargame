"""Design-time armor/penetration calculation pipeline for With Deepest Regret...

Nothing in this package runs at the table. It computes the AV/PEN numbers
that get printed on counters, from sourced WWII ballistics formulas, so the
formulas only need to be right once instead of re-derived by hand per vehicle.

See docs/superpowers/specs/2026-07-04-armored-combat-penetration-physics-design.md
for the design this package implements.
"""
