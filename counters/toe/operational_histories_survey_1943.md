# Operational Histories Closeout Survey (Non-1943 Campaign Titles)

Design note: E.165. A low-expectation, completionist sweep through the last
five unread Osprey Campaign-series operational histories in the library.
None of these five books is set in 1943 (four are 1944, one is 1941), so
this pass was scoped from the outset as a check against Table of
Contents / "Opposing Forces" or "Order of Battle" appendices (organizational
data ages more slowly than narrative) plus a skim for any citable
1943-adjacent detail — not a full narrative read of any book. Consistent
with that scope, no `units.csv` row, unit type, or rule mechanic is
proposed by this pass.

## 1. Operation Cobra 1944: Breakout from Normandy (Zaloga, Osprey Campaign 88)

`reference/operational-histories/epdf.pub_osprey-campaign-088-operation-cobra-1944-breakout-from-normandy.pdf`,
97pp. Confirmed image-only: `pdftotext -layout` over the entire file returns
no extractable text (matches the existing `reference/CATALOG.md` flag).
No Order of Battle appendix is accessible without OCR, which is out of
scope for this pass's budget. **Clean negative, closed out** — nothing
further to check here without a re-scan of the source file.

## 2. Caen 1944: Montgomery's Break-out Attempt (Ford, Osprey Campaign 143 — filed as "Campaign 105")

`reference/operational-histories/epdf.pub_osprey-campaign-105-1944-d-day-3-sword-and-beach-british-airborne-landings.pdf`,
96pp. Re-verified per this project's standing practice (`pdfinfo` title
field reads "Caen 1944 : Montgomery's Break-out Attempt"; page 3 confirms
"Campaign • 143"; the book's own bibliography lists Ken Ford's *D-Day 1944
(3): Sword Beach & the British Airborne Landings* (Campaign 105, 2002) as a
separate title): the existing `reference/CATALOG.md` mislabeling note is
**confirmed correct as written**, no correction needed.

Real text layer. Its "Order of Battle" appendix (pp.92-93) gives a full
British/Canadian and German division-brigade-regiment order of battle for
the Caen fighting, June-July 1944, with named commanders down to brigade
(Allied) and regiment (German) level. This is formation-level OOB, not the
squad/platoon tactical composition data this project's TOE files track, so
it does not corroborate or extend any existing British or German 1943 TOE
file. One incidental, dated organizational fact from the narrative: 21st
Panzer Division is stated to have been "re-formed in Normandy in July
1943" after its destruction in the North African collapse, with green/
foreign-national replacements and obsolete equipment — a real, dated 1943
event for a division this project's `waffen_ss_michulec_1943.md` currently
mentions only in passing, but not itself combat or roster data. **No
usable roster/TOE finding; one minor dated-fact footnote only.**

## 3. D-Day 1944 (4): Gold & Juno Beaches (Ford, Osprey Campaign 112)

`reference/operational-histories/epdf.pub_osprey-campaign-112-d-day-1944-4-gold-amp-juno-beaches.pdf`,
96pp. Confirmed image-only via `pdftotext -layout` (matches the existing
catalog flag). **Clean negative, closed out**, same as Cobra above.

## 4. Operation Barbarossa 1941 (1): Army Group South (Kirchubel, Osprey Campaign 129)

`reference/operational-histories/epdf.pub_osprey-campaign-129-operation-barbarossa-1941-1-army-group-south.pdf`,
95pp, real text layer. Has a full "Opposing Armies" section and two
detailed "Order of Battle" appendices (pp.26-27 Axis, p.30 Soviet) —
extensive, named-commander order of battle down to division level for
German Army Group South (plus Rumanian, Italian, Hungarian, and Slovak
contingents) and the Soviet Southwest/Southern Fronts as of June 1941.
This is genuine, citable organizational data, but at army/corps/division
granularity — not the squad/platoon/company tactical composition this
project's German and Soviet 1943 TOE files track — so it doesn't overlap
with or extend them. A full-text search for "1943" turns up exactly one
hit, an incidental postwar-damage remark unrelated to the campaign; the
book's narrative ends with 1941's Kharkov-to-Rostov fighting and never
reaches 1943. **Clean negative for this project's purposes**: real OOB
exists, but at the wrong granularity and the wrong year.

## 5. Wake Island 1941: A Battle to Make the Gods Weep (Moran, Osprey Campaign 144)

`reference/operational-histories/epdf.pub_wake-island-1941-a-battle-to-make-the-gods-weep-osprey-campaign-144.pdf`,
97pp, real text layer. Has an explicit "Opposing Forces... Orders of
Battle" section (pp.18-25) with real organizational data: the US 1st
Defense Battalion's coastal-artillery/AA battery-by-battery breakdown
(named officers, gun counts, personnel), and — more interesting for this
project's existing Japan thread — a full platoon-level table of organization
for the Japanese 2nd Maizuru Special Naval Landing Force (SNLF): four
50-man rifle platoons, one 55-man heavy machine gun platoon, a heavy-weapons
unit with regimental-gun and battalion-howitzer platoons, plus engineer,
medical, supply, and transport sub-units, totaling 1,069 personnel.

This is a genuine near-miss rather than a hit: this project's
`counters/toe/japan_1943.md` documents Imperial Japanese **Army** squad/
platoon organization (from TM-E 30-480), while the SNLF is an Imperial
Japanese **Navy** landing force with its own separate organizational
lineage — a different service, and dated December 1941, not 1943. It is
not applied to `japan_1943.md` here, but is flagged as a real, sourced lead
for a future SNLF-specific research pass if this project ever wants Navy
landing-force (vs. Army) organization on the Japan side.

One precisely dated, named 1943 anecdote also surfaced in the narrative
(not the OOB section): in October 1943, island commander Rear Admiral
Shigematsu Sakaibara ordered the machine-gunning of the 98 American
civilian contractors still held as forced labor on Wake — a war crime for
which he was tried and hanged in 1947. This is real and dated, but it is
an occupation-era war crime, not combat or organizational data, so it is
recorded here only as a possible future flavor-text anecdote, not applied
to any roster or rule.

## Net effect

A clean five-for-five completionist closeout with modest but real
findings, none rising to "add this" for the coordinator: two confirmed
image-only negatives (Cobra, Gold & Juno); one confirmed-correct
mislabeling entry plus a minor dated 21st Panzer footnote (Caen 1944); one
extensive but wrong-granularity/wrong-year Order of Battle (Barbarossa
Army Group South); and one genuine near-miss (Wake Island's Japanese Navy
SNLF platoon organization — right country, wrong service and wrong year)
plus a single dated-but-non-combat 1943 anecdote. No `units.csv` row, no
new unit type, and no rule mechanic is proposed. All five books' library
research is now closed out — no future session needs to revisit them
absent new questions.
