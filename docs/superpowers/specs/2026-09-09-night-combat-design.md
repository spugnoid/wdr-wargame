# Night Combat — New Section 23

**Status: DRAFT, pending designer review of this spec (brainstormed 2026-09-09).**

Finishes the night-scenario framework Rule 14.11.5 stubbed in and explicitly
deferred ("Full night rules are a separate design task"), and adds
illumination as a real mechanic. Approach: the genuinely new mechanical
content (ambient visibility, the finished detection framework, the
drifting/fading illumination model) lives in one new Section 23, reusing
existing machinery by reference wherever possible (Section 16's fire-mission
pipeline for starshells, the existing CON/OBS spot-roll procedure, the
existing careless-movement penalty, the existing dispersion-direction table).
Everything else (fire range cap, movement risk, close-assault bonus, command
radius) becomes one short cross-reference rule inserted into its existing
home section — the same reuse-by-reference idiom Section 20 already uses for
spotting.

14.11.5 is superseded by 23.1; a design note (next available, E.106)
documents the supersession the same way E.104 documents superseding E.102.

## 1. Section 23 structure

- **23.1 Ambient Visibility** — replaces 14.11.5's stub.
- **23.2 Illumination — General** — what a lit hex means for detection.
- **23.3 Illumination Source — Off-Map Starshell**
- **23.4 Illumination Source — Handheld Flare Pistol**
- **23.5 Illumination Source — Vehicle Searchlight**
- **23.6 Drift** — shared lifecycle mechanic for 23.3/23.4.

Placed after Section 22 (the last existing content section) rather than
renumbered in — this book never renumbers, only appends (same convention as
the E.100+ design notes).

## 2. 23.1 Ambient Visibility

- **Visual spot range is capped at 2 hexes.** Firms up 14.11.5's "1-2
  hexes" into one number — matches the example already given in Section
  22's scenario-design guidelines ("Night: visibility 2 hexes"). Beyond 2
  hexes, no visual spot roll (Rule 14.9.5) may be attempted against a
  marker, regardless of OBS bonuses. This is a hard eligibility gate, not
  a CON modifier — it sits in front of the existing procedure, doesn't
  replace any part of it.
- **Sound spotting's trigger condition (14.11.1) is unchanged.** Night
  doesn't waive the "no unit has fired within 5 hexes this turn"
  requirement — a firefight still masks footsteps at night same as in
  daylight. Night changes how much sound spotting *matters* (see below),
  not when it's available.
- **Exactly two CON rows double.** 14.11.5 says "sound-based CON
  penalties" without naming them; there are exactly two candidates in the
  existing table, and both are named explicitly in 14.11.3/14.11.4:
  moving through dense woods/rubble (-1 → -2) and moving carelessly (-2 →
  -4). Every other row — terrain cover, the existing "Night scenario: +3"
  row itself, smoke's +2 — is untouched.
- Everything else in the spot-roll procedure (14.9.6's 4+ threshold, the
  full OBS table, RP costs) is unchanged.

## 3. 23.2 Illumination — General

A hex within a lit radius (23.3-23.5) is treated as daylight for detection
purposes: the 2-hex visibility cap, the "Night scenario: +3" CON row, and
the doubled 23.1 sound penalties all stop applying to a spot roll against a
marker in that hex. Normal terrain CON and LOS still apply as usual —
illumination cancels *night*, not concealment in general.

## 4. 23.3 Off-Map Starshell

Reuses Section 16's existing fire-mission pipeline wholesale rather than
introducing a parallel resource:

- A mortar/artillery fire mission may choose **Illum** as a third mode
  alongside HE and Smoke (extends 16.4.1's mode list), expending 1 AMO from
  the **same count** HE and smoke already share (extends 16.3.2's pooling
  rule — no new ammunition pool).
- Identical sealed-slip targeting, delay, accuracy roll, and dispersion
  procedure as any other mission (16.5-16.6) — nothing new to track before
  it lands.
- On landing, place an **ILLUM marker** (instead of SMOKE) at **step 3**.
  **Radius in hexes = current step** (3/2/1), so no separate radius table
  is needed — the step number *is* the radius.
- Each Recovery Phase, roll 1d6 per ILLUM marker: **1-3 advances one step**
  (3→2→1→removed). Faster than smoke's 1-2/6 (16.10.1) — a real
  illumination round burns out quicker than a smoke bank lingers, and the
  difference is worth keeping rather than copying smoke's number
  unexamined.
- Drifts per 23.6.

## 5. 23.4 Handheld Flare Pistol

- Fired as the owning unit's own action — no sealed slip, no delay, no
  accuracy/dispersion roll. Targets the unit's own hex or an adjacent one,
  owning player's choice.
- Very limited uses: **2 per scenario per equipped leader/unit** (unit
  equipment, not a support-request asset — this is a personal signal
  flare, not an artillery mission).
- Starts at **step 2** (radius 2) — smaller than a starshell.
- **Steps down by exactly 1 every Recovery Phase automatically, no roll.**
  Deterministic, on purpose: this is the opposite trade-off from
  starshell (starshell: bigger, delayed, uncertain duration; handheld:
  smaller, but instant and reliable). Two clean uses per scenario, two
  turns of light each, no ambiguity about how long it lasts.
- Drifts per 23.6.

## 6. 23.5 Vehicle Searchlight

- Reuses the vehicle's existing TRAV arc (17.4.1) rather than introducing
  new facing/cone geometry that doesn't exist anywhere else in the
  rules — the searchlight illuminates radius 2 within whatever arc the
  vehicle's gun currently covers.
- No delay, no fade, no drift to track — on for as long as the vehicle
  keeps it on, off when it doesn't.
- Using it **automatically reveals the vehicle** that turn, mirroring
  14.9.3's "a unit that fires is automatically revealed" pattern exactly —
  a searchlight beam is at least as conspicuous as muzzle flash.

## 7. 23.6 Drift (starshell and handheld flare only)

- **Once per scenario**, roll 1d6 on the existing dispersion-direction
  table (16.6.5's six named compass directions — no new table) to set a
  single scenario-wide wind direction.
- Every ILLUM marker still aloft (starshell or handheld) drifts 1 hex in
  that direction each Recovery Phase, at the same time as its fade check
  (23.4's automatic step-down, or 23.3's 1d6 roll).
- The searchlight (23.5) does not drift — it isn't an airborne object,
  it's a beam tied to the vehicle.

## 8. Cross-reference rules in existing sections

Each of these is one short rule in its home section, pointing back to 23.1
or 23.2 for the actual values — not a duplicated procedure.

- **Movement (Section 7, new sub-rule)**: a Move or Assault Move at night
  that takes a unit beyond the 23.1 visibility cap from where it started,
  and not through a lit hex (23.2), requires a **1d6 + Morale modifier
  check, threshold 3** — the same threshold already used for the
  Suppressed recovery roll (5.2) and the reduced-face close-assault nerve
  check (9.1.3a), so it's not a new number to learn. Fail: the unit stops
  **2 hexes short** of its intended hex instead (full movement allowance
  still spent — it just went to the wrong place). Fixed shortfall, not
  random, to stay unambiguous.

- **Fire Combat (Section 8, new sub-rule)**: a unit may not declare fire
  combat at night against a target beyond the 23.1 visibility cap unless
  the target's hex is lit (23.2). Flat eligibility gate, independent of
  the existing Long Range Cap (8.7) — 8.7 still does its own separate job
  of capping *results* for weak effective rFP once a target is in range;
  this new rule is about whether you can declare the attack at all.

- **Close Assault (Section 9, new sub-rule)**: if the assaulting unit is
  still concealed — its blind marker has not been spotted (Rule 14.9.6) —
  at the moment it declares Close Assault, its Grenade Phase roll (9.3.2)
  gets **+3** — reusing the existing +3 figure (9.4.2's range-0 entry-fire
  bonus, 14.10.2's Spot Action bonus) rather than inventing a new
  constant. No new tracking or time window: reads the hidden-info state
  (spotted or not) that already exists at the instant of declaration.

- **Leaders (Section 12, new sub-rule)**: a leader's command radius (12.2)
  is **+1 hex** at night (sound carries farther in still air), but issuing
  a command beyond the leader's *normal daytime* radius applies the
  existing careless-movement CON penalty (14.9.7/14.11.4: -2, doubled to
  -4 at night per 23.1) to that leader's hex **for spotting purposes
  only** — no CARELESS marker is placed, no movement occurs, no other
  consequence of actual Careless Movement (Rule 7.4) applies. It's a
  borrowed CON value, not a status: reach costs concealment, nothing
  else.

## 9. Explicitly out of scope this pass

- No moon-phase/weather visibility tiers — one flat night baseline plus
  illumination, matching the scope actually approved. A future pass could
  add graduated ambient conditions without touching anything above.
- No vehicle infrared/thermal sighting (the historical late-war German
  Sperber/Vampir system) — deliberately left out as too narrow a
  historical case for this pass; a future scenario-specific special rule
  could add it without touching Section 23's core.
- No blind/double-blind CP role — a separate, larger design explored and
  dropped in the same 2026-09-09 conversation that produced this spec; not
  part of Night Combat.
- Operational-scale [OPS] interaction is not addressed — Section 2.1.2's
  operational scale (250 yd/hex) isn't considered here; this spec is
  written for tactical scale only.

## 10. Sections affected on implementation

New: Section 23 (23.1-23.6). Edited: 7.x (new movement sub-rule), 8.x (new
fire-cap sub-rule), 9.x (new infiltration-bonus sub-rule), 12.x (new
command-radius sub-rule), 14.11.5 (superseded, redirects to 23.1), 16.3.2 /
16.4.1 (extend AMO pooling and mode list to include Illum), Appendix E (new
design note superseding 14.11.5), Appendix F index entries, index.rst
toctree (add section_23).
