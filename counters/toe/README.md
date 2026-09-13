# Nation TOE Reference Docs

Tables of Organization and Equipment (TOE) for each nation represented in
*With Deepest Regret...* — the real-world historical organizational
structure and weapon complement at the rifle squad, platoon, and company
level, cited to real sources.

## Purpose

Before this existed, counter design for any nation beyond Germany and the
Soviet Union (both 1943 only, per `counters/infantry_calc/`) had no
organizational reference to work from — deciding what a US, British, or
Japanese rifle squad's counter should look like meant guessing rather than
reading it off a real source. These docs are that missing reference: not
game stats, not yet counter data, just "what a rifle squad, platoon, and
company actually looked like" for each nation, so the counter design and
`infantry_calc` pipeline work that follows can proceed from real
organizational facts instead of assumption.

## Scope

- **Nations:** Germany, Soviet Union, United States, United Kingdom, Japan
  — every nation already referenced somewhere in the rules text (rosters,
  weapon citations, the Section 15.6 national morale table) but never
  assembled into one organizational reference.
- **Year:** 1943 for all five, as a first pass — matching how the game
  already frames itself ("representative 1943") and how the
  `infantry_calc` pilot was scoped. Later year bands (Section 15.6 already
  references Germany 1941-42/1944-45, USSR 1941/1943+) are an explicit
  follow-up, not part of this pass.
- **Echelon:** Rifle squad through company — organic squad/platoon weapons
  plus company-level heavy-weapons assets (HMG, medium mortar, AT weapon
  teams), matching what the counter roster already partially represents
  as separate unit types.
- **What this is not:** Not game stats (M#/F#/G#, Defence, Morale) and not
  structured data ready for a pipeline yet — that's deliberately a later
  step (see design note on this in `docs/source/appendix_e__design_notes.rst`
  once filed), sequenced behind these docs so game-balance decisions are
  made from real organizational facts, not guessed alongside them.

## Files

The five original nation TOE files (`germany_1943.md`, `soviet_union_1943.md`,
`united_states_1943.md`, `united_kingdom_1943.md`, `japan_1943.md`) follow one
shared structure (Sources, Rifle Squad, Other Squad-Level Units, Platoon
Organization, Company Organization, Confidence Notes, Open Questions) so
they're directly comparable side by side.

Since then, this directory has grown into the general home for every
single-book, single-topic research pass in this project (vehicle armor,
weapons, snipers, fortifications, airborne, elite units, etc.) — each one
still follows the same broad shape (Sources / Findings / Confidence Notes /
Open Questions), adapted to whatever the topic actually needs. Every file
here is cross-referenced from a design note in
`docs/source/appendix_e__design_notes.rst` (search that file for the
research filename to find its E.### note) and from the rule text it
informed, if any.

The source books themselves live in `reference/` (gitignored, not part of
the repo) — see `reference/CATALOG.md` for the full library index: verified
title/author for every file (filenames are not always trustworthy — see
that catalog's own notes on mislabeled files), which folder it's organized
into, and which research file/design note (if any) has used it.

## Relationship to existing counter data

`counters/infantry_calc/data/units.csv` already encodes some of this for
Germany and the USSR (e.g. the Grenadier and Panzergrenadier squads, cited
to Nafziger and TM-E 30-451). These docs don't replace that — they're the
same kind of sourcing, made explicit and extended to the three nations
that don't have it yet, and written up in a form a human can read and
sanity-check before anything is fed back into a data pipeline.
