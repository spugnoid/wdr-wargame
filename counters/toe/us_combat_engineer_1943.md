# United States — 1943 Combat Engineer Organization

## Sources

- Gordon L. Rottman, *US Combat Engineer 1941-1945* (Osprey Warrior 147),
  64pp. Real OCR text layer, extracted in full via `pdftotext -layout`
  (2,463 lines) — not an image scan. Cites primary sources directly,
  including FM 5-5 (11 Oct 1943).
- This is a documentation pass, not a fact-check against an existing roster
  row: this project's infantry roster (`counters/infantry_calc/data/units.csv`)
  currently has **no US combat engineer squad row at all** (checked directly
  — there is also no German/Soviet/UK engineer squad row either; the
  reference to an "existing German Pioniere roster entry" in
  `japan_engineers_1943.md`'s own text appears to be aspirational/comparative
  phrasing from that file's own research context, not a row that actually
  exists in `units.csv` as of this pass — corrected here to avoid
  propagating that assumption further).
- Cross-referenced against `counters/toe/japan_engineers_1943.md` (the
  project's existing Japanese combat-engineer research) for structural
  comparison, since both were read with an eye toward comparable
  organizational questions (squad-level presence, mine detection, bridging
  echelon).

## Findings

### 1. Squad/platoon organization, 1943-specific

The book gives an explicitly dated organization table (pp.38-40): **"Prior
to August 8, 1944 an engineer battalion had a strength of 31 commissioned
officers, three warrant officers, and 649 enlisted men"** (reduced to 605 EM
after that date) — confirming this table is the correct 1943-era TOE, not a
later-war revision retroactively assumed to apply.

- **Battalion**: HHSC (12 officers, 3 WO, 106 EM) + medical detachment +
  three engineer combat companies (5 officers, 162 EM each).
- **Company → platoon**: three platoons per company, each with a 5-man
  platoon HQ (Lt platoon commander, SSgt platoon sergeant, Tech.5 tool-room
  keeper, Tech.5 jeep driver, Pvt/Pfc 2½-ton truck driver) plus three
  13-man engineer squads. A nominal "39-man engineer section" appears on
  paper in some org charts but was, per Rottman, "an unused paper fiction —
  never appears in unit histories" in practice; the real building block was
  the 13-man squad. **Platoon total = 44 men** (explicitly stated, p.~54:
  "The 44-man platoon").
- **13-man squad roster** (p.40, exact): Sgt (foreman) + Cpl (asst.
  foreman) + bridge carpenter (Tech.4/5, ×1) + general carpenter (Tech.4/5,
  ×2) + electrician (Tech.5/Pfc/Pvt, ×1) + light truck driver (Tech.5/
  Pfc/Pvt, ×1) + demolition man (Pfc/Pvt, ×1) + jackhammer operator
  (Pfc/Pvt, ×1) + utility repairman (Pfc/Pvt, ×2) + general rigger
  (Pfc/Pvt, ×2) = 13.
- **Internal inconsistency in the book itself, flagged not resolved**: an
  earlier passage (p.16) states a squad has "six different specialties in
  addition to the leader and assistant leader," but the roster table (p.40)
  lists eight distinct specialty names. Not an extraction error — both
  statements are directly present in the source text.
- **Armament**: squad armed entirely with M1 Garand rifles, plus an organic
  M7 rifle grenade launcher and a bazooka. Platoon HQ carried an M8 grenade
  launcher, two water-cooled M1917A1 .30-cal machine guns (lost in the
  August 1944 reorganization), and the platoon's SCR-625 mine detector.
- **Transport**: each squad had its own organic 2½-ton GMC CCKW-352H dump
  truck (16,850 lb, 6×6, winch-equipped) — a real organic vehicle assignment
  down to squad level, notably more mechanized than either the German or
  Japanese engineer organizations documented elsewhere in this project.

This is the most explicitly primary-sourced (FM 5-5-cited), least-inferred
combat-engineer TOE table found in this project's research to date — a
higher confidence level than the Japanese engineer file, which had to infer
its own section-strength figure from a platoon total.

### 2. Mine detection

**SCR-625** ("detector set, mine, SCR-625," Hazeltine Co.), first fielded
North Africa late 1942 (p.29 sidebar): 6ft telescoping handle, 18in disc
search head, 7.5lb + 7lb amplifier haversack, $491 unit cost, detects to
12in depth via audio tone plus meter. Documented operational flaws: too
heavy for sustained sweeping, not waterproof/fragile, and — critically —
degraded in Italy by iron-rich soil, and defeated by German non-metallic
(wood/glass/ceramic) mines and deliberately buried scrap metal even in the
improved SCR-625-E variant.

**Organizational placement**: the detector itself was **platoon-HQ
equipment** (one per platoon, not one per squad); each squad instead
carried an **M1 mine probe**. Detection and probing were split across two
organizational echelons, not bundled at squad level.

**Comparative note for the Japanese engineer gap**: `japan_engineers_1943.md`
flagged "no IJA mine-detector equipment was found described" as an open
question. This pass does not resolve that gap directly (this book is
US-focused and says nothing about Japanese equipment), but it does establish
that mine detectors of this era were a real, fielded metal-detection
technology with well-documented real-world limitations (defeated by
non-metallic mines and iron-rich soil) — useful context if a future rule
ever wants to model detector effectiveness as fallible rather than binary.

### 3. Demolition equipment

Full illustrated charge inventory (p.30 sidebar): ½lb and 1lb TNT blocks,
2½lb M2 tetrytol block, 2¼lb M3 Composition C2/C3 plastic block, M1
demolition haversack (eight 2½lb linked charges), 10lb M1 shaped charge
(12in armor / 36in concrete penetration), 40lb M3 shaped charge (60in
concrete), 40lb ammonium nitrate cratering charge, field-fabricated pole
charges, and the M1 Bangalore torpedo (5ft, 9lb amatol, linkable to 200ft
for wire/minefield breaching).

This inventory is notably larger and more standardized/catalogued than what
this project has documented for German or Japanese demolition equipment so
far (the Japanese file's bangalore-torpedo figure, by comparison, describes
a single 34ft/225lb assembled unit rather than a modular linkable system).
Worth a future comparative pass if demolition mechanics are ever
differentiated by nation.

### 4. Bridging echelon

Directly parallel to the Japanese finding (pp.17-18, 41-42): bridging
materiel and technical expertise lived **above** the engineer company, in
dedicated bridge companies (light pontoon, treadway, Bailey) at corps/group
level — "the bridge company provided the technical expertise" while the
divisional engineer battalion supplied the manpower to erect. Three named
bridge types: M1938 infantry footbridge (12ft sections, ≤400ft), M1
treadway (40-ton capacity, pontoon-supported, used at 1,000ft spans on the
Rhine), M2 Bailey (British-designed, 40-ton, stackable panels, 10×12ft
sections, 180ft unsupported span limit).

This is a genuine structural parallel to the Japanese IJA finding that
large-scale bridging sat above the basic engineer unit, not within it —
worth noting if the project ever writes a cross-national comparative TOE
note on engineer echelon structure.

### 5. Other notable findings

- **Flamethrowers were authorized organically** (24 per battalion, held in
  HQ company's supply section) but "little used" in the Mediterranean/ETO
  theaters and were formally withdrawn from engineer battalions in March
  1944 — before Normandy — though still issuable from depot stock. This
  contrasts with the assumption (carried in `japan_engineers_1943.md`'s own
  comparative language) that a German Pioniere squad carries an organic
  flamethrower as standard kit; no such German roster row currently exists
  in this project to verify that claim against, so it remains an assumption
  from that file, not an independently confirmed fact.
- **US divisional engineers explicitly did NOT do minefield-laying, wire,
  or fortification work directly for the infantry** — that fell to the
  infantry battalion's own ammunition-and-pioneer platoon and the
  regimental antitank mine platoon. Engineers only delivered materials and
  technical advice for those tasks. A genuinely useful nuance if the
  project ever models a US infantry-organic pioneer element separately from
  the combat-engineer battalion.

## Confidence Notes

- This is the highest-confidence, most directly primary-sourced engineer
  TOE table read in this project's history — an explicit date range, an
  explicit primary-source citation (FM 5-5, 11 Oct 1943), and an exact
  squad roster by specialty and rank, not an inferred or triangulated
  figure.
- No numeric roster changes were applied in this pass. Adding a US Combat
  Engineer squad row to `units.csv` is a real, well-sourced candidate for a
  future session, but it requires new weapon-type entries this project's
  `weapons.csv` does not currently have (bazooka, M7/M8 rifle grenade
  launchers, the water-cooled M1917A1 variant of the .30-cal, and an M1 mine
  probe/SCR-625 mine detector as a non-weapon organic item) — a larger
  weapons-data task than this pass's scope, and not something to force
  through without properly sourcing each weapon's own rate-of-fire/range
  figures the way every other roster row's weapons already are.

## Open Questions

1. A US Combat Engineer squad roster row remains unadded — the data to
   support it is now the best-sourced of any nation's engineer unit in this
   project, but adding it cleanly requires new `weapons.csv` entries for
   the bazooka, rifle grenade launchers, and the mine probe/detector, which
   this pass did not attempt.
2. The book's own internal inconsistency (six vs. eight squad specialties)
   is unresolved — not a project gap, a genuine ambiguity in the source
   itself.
3. Whether this project's assumed "German Pioniere squad has an organic
   flamethrower" claim (referenced in `japan_engineers_1943.md`) is actually
   sourced anywhere, given no German engineer roster row currently exists
   to check it against, is itself now an open question worth a future
   session's attention if a German engineer squad is ever added.
