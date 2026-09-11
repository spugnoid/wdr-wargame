# Germany — 1943 Infantry Table of Organization and Equipment

## Sources

- **Kennedy, Gary. "Organization of the German Infantry Battalion 1938 to 1945."** `bayonetstrength.uk`, 3rd draft, October 2021 (1st draft February 2019). PDF: http://www.bayonetstrength.uk/GermanArmy/GerInfBn/Org%20of%20the%20German%20Inf%20Bn%201938-45.pdf — a detailed secondary compilation built directly from Kriegsstärkenachweisung (KStN, "war strength table") documents, reproducing personnel/weapon tables role-by-role with dates. This is the primary backbone of this research; it explicitly identifies **two** distinct organizational patterns that were both in force at different points during calendar year 1943:
  - **KStN 131c, as redrafted early 1941** (the "1942 'c'" pattern in Kennedy's comparative table) — in force from the beginning of 1941 through late 1943, i.e. covering roughly the first three quarters of 1943. 10-man Rifle Squad, 4 squads per Rifle Platoon, 5-cm mortar per platoon, Anti-tank Rifle Squad at Company HQ.
  - **KStN 131n ("neuer Art" / new type), first drafted October 1943, full version issued December 1943** — in force from roughly Q4 1943 onward. 9-man Rifle Squad, 3 squads per Rifle Platoon, no platoon-level mortar or anti-tank rifle, but a new company-level 8-cm Mortar Group.
  - Kennedy's own source list (reproduced at the end of his document) includes the primary documents cross-checked below: US War Department TM-E 30-451 (1 Sept 1943 and 15 Mar 1945 editions), *The German Squad in Combat* (US MIS Special Series No. 9, 25 Jan 1943), *German Infantry Weapons* (US MIS, 25 May 1943), and *Company Officer's Handbook of the German Army* (US, 31 Mar 1944).
- **US War Department, TM-E 30-451, "Handbook on German Military Forces,"** 1 September 1943 edition, Military Intelligence Division. Full OCR text consulted directly at https://archive.org/stream/Tm-e30-451HandbookOnGermanMilitaryForces-1943/1943HandbookOnGermanMilitaryForces_djvu.txt (paragraphs 38–39, "Rifle company" / "Machine-gun company" / infantry battalion). This is a genuine period primary source (US Army officer-training handbook compiled from captured documents and PW interrogation, dated squarely within 1943) and its rifle-company/platoon description matches the pre-October-1943 ("131c") pattern from Kennedy almost verbatim, providing independent corroboration.
- **US War Department, Military Intelligence Service, Special Series No. 9, "The German Squad in Combat,"** 25 January 1943 — a full translation of a German squad-training manual. Full text consulted at https://archive.org/download/TheGermanSquadInCombat/TheGermanSquadInCombat.pdf. Used as the primary-source basis for individual weapon assignment within the (pre-reorganization) 10-man squad (squad leader's machine pistol, gunner/assistant/ammunition-carrier roles, riflemen).
- **"War Strength Table of Organization [Kriegsstärkenachweisung (Heer)], K.St.N. Nr. 131n, 'German Infantry Rifle Company (new type)'"**, dated 1 May 1944 (with amendments through 1 Aug 1944), as reproduced/transcribed by Military Research Service (2009). PDF: https://www.militaryresearch.org/Kstn%20131n%20Inf%20Co.pdf. **Note:** this specific transcription is the *May 1944* revision of KStN 131n, not the original December 1943 issue — it is used here to corroborate the general "new type" (neuer Art) company architecture and, specifically, to show the follow-on change (2 heavy machine guns replacing the 2 8-cm mortars) that Kennedy's narrative also describes. Dated figures from this table are labeled "May 1944" below and are not asserted as the December 1943 figures.
- **"Grenadierkompanie (mot), K.St.N. 1114 (1 November 1943)"**, transcribed at wwiidaybyday.com: https://www.wwiidaybyday.com/kstn/kstn11141nov43.htm — a primary-source KStN table (in German) for the **motorized Grenadier (Panzergrenadier) company**, consulted for the "Other Squad-Level Units" section. This is a plain-text/HTML transcription of the original German table by a hobbyist reference site; role labels and weapon counts are reproduced faithfully but some personnel subtotals required arithmetic reconstruction from platoon-level totals (see Confidence Notes).
- Askari Miniatures, "Composition of the German Infantry Squad" — https://askari-minis.com/composition-of-the-german-infantry-squad/ — a wargaming-hobby secondary source, itself citing *The German Squad in Combat* (above) and Buchner's *Handbuch der Infanterie 1939–1945*. Used only for cross-checking, not as a primary basis.
- Military History Visualized, "German Squad Tactics & Organization in World War 2" — http://militaryhistoryvisualized.com/german-squad-tactics-world-war-2/ — secondary synthesis (YouTube-linked blog), used for cross-checking the squad-leader-weapon transition (rifle → MP40, c. 1941) narrative.
- The project's own existing data file, `counters/infantry_calc/data/units.csv` (rows `GER_GREN_1943.3_F/R`, `GER_PZGR_1943.3_F/R`, `GER_MG42_1943.3_F/R`) and `counters/infantry_calc/data/weapons.csv`, read for context per the task brief. See Open Questions for a specific point of disagreement identified between that file and the sources above.

## Rifle Squad

As documented above, "1943" spans **two different official Rifle Squad (Gruppe) organizations.** Both are given in full below because a mid-1943 scenario date could plausibly use either, and the project's own existing data (`GER_GREN_1943.3_*`, dated "1943.3" / Q3) falls right at the transition point.

### Early-to-mid 1943 (KStN 131c pattern, in force since February 1941)

**10 men total**, built around a single light machine gun:

- **Squad Leader (1)** — armed with an **MP38/40 machine pistol** (submachine gun) with 6 magazines of 32 rounds each, plus field glasses, wire cutters, compass, and signal whistle. (Before roughly 1940–41 the squad leader carried a Kar98k rifle instead; the MP38/40 became his standard personal weapon from 1940–41 onward and remained so through 1943.)
- **Riflemen (6)** — each armed with a **Karabiner 98k (Kar98k)** bolt-action rifle. One of the six also served as second-in-command of the squad. From 1942 onward, one rifle per squad was fitted with a rifle-grenade launcher (Gewehrgranatgerät) as an added-on capability rather than a separate weapon type.
- **Light machine gunner (1)** — his personal/served weapon was the **MG 34** light machine gun (belt-fed, 50-round drum magazine in this role), plus a pistol as personal sidearm.
- **Assistant gunner (1)** — carried the spare barrel, four 50-round belt drums, and a 300-round ammunition box; armed with a pistol.
- **Ammunition carrier (1)** — carried two further 300-round ammunition boxes; sources disagree on whether he was issued a pistol (per the primary translated manual, *The German Squad in Combat*, Jan 1943) or a rifle (per Kennedy's transcription of the KStN table) — see Confidence Notes.

**Totals per squad:** 10 men; 1× MG34 light machine gun; 1× MP38/40 submachine gun (squad leader only); 6× Kar98k rifle; 2–3× pistol (machine-gun team).

The **MG42** began entering service during 1943 and progressively replaced/supplemented the MG34 in front-line units through the year, but did not fully supersede it — both weapons remained in concurrent Army-wide use throughout 1943 and beyond (per Kennedy's narrative and general secondary literature). A given squad's actual gun on a given date in 1943 could be either model.

### Late 1943 reorganization (KStN 131n "neuer Art"/new type, first drafted October 1943, full version December 1943)

Squad strength was reduced by one man (the ammunition-carrier post was eliminated) and a second submachine gun was added:

**9 men total:**

- **Squad Leader (1)** — retained the **MP40 machine pistol** as his personal weapon.
- **Riflemen (6)**, of whom:
  - **5** armed with the **Kar98k** rifle (one fitted with a rifle-grenade launcher).
  - **1** additionally armed with an **MP40** (a second machine pistol added to the squad under this reorganization — commonly understood as going to the acting deputy squad leader, though this is not explicitly stated in the KStN itself per Kennedy).
- **Light machine gunner (1)** — served the squad's single **light machine gun** (MG34 or MG42 — the KStN does not distinguish), armed with a pistol as sidearm.
- **Assistant gunner (1)** — now armed with a **Kar98k rifle** rather than a pistol (the second LMG-team pistol slot was the one eliminated along with the ammunition-carrier post).

**Totals per squad:** 9 men; 1× light machine gun (MG34 or MG42); 2× MP40 submachine gun (squad leader + one designated rifleman); 6× Kar98k rifle; 1× pistol (gunner only).

Each Rifle Platoon (see below) additionally held **2 spare/reserve light machine guns** at Platoon Headquarters from December 1943 (reduced to 1 from March 1944) — these were "weapons reserve" items issued without a normal ammunition allotment, understood as replacement stock rather than guns available for squads to draw on routinely.

## Other Squad-Level Units

### Panzergrenadier (motorized infantry) Squad

The mechanized/motorized "Grenadier" (Panzergrenadier) rifle squad, per KStN 1114 (1 November 1943, the standard truck-mounted "Grenadierkompanie (mot)" table — see note below on the separate armored/SPW variant), differed meaningfully from the standard Rifle Squad in firepower, reflecting its role riding into the assault on trucks (or, in one company per Panzergrenadier battalion, armored Schützenpanzerwagen half-tracks):

- **Squad leader (Gruppenführer)** — armed with an **MP40** machine pistol.
- **Deputy squad leader (stellvertretender Gruppenführer)** — armed with a **Gewehr 41 (G41)** semi-automatic rifle, a comparatively rare weapon reserved for specific roles like this one.
- **Two light machine gun teams** — the squad fielded **2× light machine gun** (double the standard Rifle Squad's allotment), each with its own gunner and loader/rifleman team, armed with a mix of Kar98k rifles and pistols.
- **One Panzerschreck team** — the squad carried **1× 8.8cm Raketenpanzerbüchse ("Panzerbüchse 54", i.e. the Panzerschreck rocket launcher)**, organic at squad level. (The KStN nomenclature retained the older "Panzerbüchse," anti-tank-rifle, designation for continuity even though the weapon itself was the newer rocket-propelled type.)
- Remaining riflemen armed with Kar98k rifles and pistols.

At the Rifle Platoon level (3 squads), the KStN 1114 table totals show **6 light machine guns and 3 Panzerschreck (Panzerbüchse 54) launchers per platoon** — i.e., confirming 2 LMG and 1 Panzerschreck per squad on average, consistent with the per-squad breakdown above.

The company additionally held a dedicated, company-level **Panzerzerstörertrupp** ("tank-destroyer squad," 2 NCOs + 7 men) equipped with **4 more Panzerschreck launchers**, separate from and in addition to the one per platoon rifle squad — see Company Organization below.

**A separate, armored (gepanzert/"gp") version of this company existed** (KStN 1114c(gp), also dated 1 November 1943) for the one battalion per Panzergrenadier regiment actually mounted in Schützenpanzerwagen (Sd.Kfz. 251) half-tracks rather than trucks. This research did not obtain a full breakdown of that table's squad composition; it is understood in general secondary literature to have used a somewhat smaller dismounted squad (some crew stayed with the vehicle to man its pintle-mounted MG), but this specific figure is **not verified** here — see Open Questions.

## Platoon Organization

### Early-to-mid 1943 (KStN 131c pattern)

The **Rifle Platoon (Zug)** consisted of:

- **Four Rifle Squads**, 10 men each (40 men total), as above.
- **Platoon Headquarters (9 men):**
  - 1× Platoon commander — pistol, plus (from 1940) an MP40.
  - 1× Platoon NCO (deputy) — pistol only.
  - 3× Messenger — rifles.
  - 1× Horse leader (for the platoon's two-cart horse team) — rifle.
  - **Light Mortar Troop (3 men)** — an NCO leader (rifle), a gunner (pistol), and an assistant (pistol), serving **1× 5-cm light mortar (leichter Granatwerfer 36)**.

**Total platoon strength: 49 all ranks** — 12 pistols, 5 machine pistols (MP40), 33 rifles, 4 light machine guns (1 per squad), and 1× 5-cm mortar. This figure and breakdown come directly from Kennedy's reproduction of the February 1941 KStN 131c personnel/weapons table and is corroborated narratively by TM-E 30-451 (1 Sept 1943): "the rifle company consists of a headquarters, an antitank rifle section..., three rifle platoons, and a train. Each platoon is divided into one light mortar squad and four rifle squads; each rifle squad...includes one light machine gun and one machine pistol. Platoon and company commanders also carry machine pistols."

By late 1942, a "gesperrte Stellen" (blocked-post) manpower-saving measure had deleted the Platoon NCO post from the paper establishment in many units (filled only with special authorization), though the KStN entry itself remained.

### Late 1943 reorganization (KStN 131n, December 1943)

The **Rifle Platoon** was reorganized to:

- **Three Rifle Squads**, 9 men each (27 men total), as above.
- **Platoon Headquarters, reduced to 6 men:**
  - 1× Platoon commander — pistol + MP40.
  - 2× Messenger — rifles.
  - 1× Stretcher-bearer — pistol.
  - 1× Horse leader — rifle.
  - 1× Wagon driver — rifle.
  - Plus 2 reserve/spare light machine guns held at Platoon HQ (reduced to 1 from March 1944), issued without a normal ammunition allotment.

The dedicated Light Mortar Troop (and its 5-cm mortar) was **eliminated entirely** at platoon level under this reorganization — a direct consequence of the 5-cm mortar being judged ineffective and the rifle-grenade-launcher attachment being seen as an adequate replacement for close-range HE projection at squad level.

Only the **first** of a company's three Rifle Platoons was still commanded by a commissioned officer (Leutnant); the second and third platoons were led by senior NCOs (Feldwebel/Oberfeldwebel), a change from the earlier pattern.

**Total platoon strength: 33 all ranks** — 5 pistols, 7 machine pistols (MP40), 22 rifles, and 3 active light machine guns (1 per squad) plus 2 reserve LMGs at HQ (reduced to 1 from March 1944). This represents roughly a one-third manpower reduction from the 49-man 1941–43 platoon while nominally preserving per-squad LMG density.

## Company Organization

### Early-to-mid 1943 (KStN 131c pattern)

The **Rifle Company (Schützenkompanie)** consisted of:

- **Three Rifle Platoons**, 49 all ranks each (147 total), as above.
- **Company Headquarters** — the company commander, a senior NCO, an NCO for vehicles/transport, an NCO for equipment, messengers (four on foot, two with bicycles per the 1939–41 amendment), and the Company Train (baggage and combat trains).
- **Anti-tank Rifle Squad**, held at Company HQ (not further subdivided into the rifle platoons) — an NCO leader plus **three two-man teams, each serving one Panzerbüchse 38 or 39 anti-tank rifle** (3 anti-tank rifles total). This unit was confirmed independently by TM-E 30-451 (1 Sept 1943): "the rifle company consists of a headquarters, an antitank rifle section armed with three antitank rifles, three rifle platoons, and a train."
- **No organic heavy machine guns or medium (8-cm) mortars.** These weapons were concentrated instead in the Infantry Battalion's separate **Machine-Gun Company** (Maschinengewehrkompanie), which per TM-E 30-451 consisted of "a headquarters, three machine-gun platoons, one heavy mortar platoon, and a train," with each machine-gun platoon fielding heavy (tripod-mounted) machine guns and the mortar platoon fielding 8-cm mortars — a battalion, not company, asset. (TM-E 30-451's OCR text is ambiguous on the exact 8-cm mortar count in this platoon — see Open Questions — but this is outside the company-level scope of this document in any case.)

**Total company strength:** not given as a single reproduced table figure by the sources consulted, but Kennedy's narrative states the company's authorized strength was reduced "from 190 all ranks to 147" at the December 1943 transition described below, implying the earlier (1942/pre-nA) company establishment was approximately **190 all ranks** including Company HQ, the Anti-tank Rifle Squad, and the Company Train, on top of the 147 men across the three Rifle Platoons.

### Late 1943 reorganization (KStN 131n, December 1943)

The **Rifle Company** was reorganized to:

- **Three Rifle Platoons**, 33 all ranks each (99 total), as above.
- **Company Headquarters**, reduced: the commander, a senior NCO, an NCO for combat vehicles, and a Medical NCO, plus three messengers (one with a bicycle) and, newly, **four radio operators** — the first time radio communication (Feldfunksprecher b sets) was issued down to Rifle Company level.
- **Anti-tank Rifle Squad deleted entirely.**
- **New: an organic 8-cm Mortar Group** — a small headquarters (NCO, messenger, rangetaker, wagon driver with a two-horse wagon) plus two mortar detachments, each an NCO and five mortar crewmen with a horse-drawn cart team, serving **2× 8-cm mortars** total. These weapons were reallocated down from the Battalion Machine-Gun Company's mortar platoon (which received a new 12-cm mortar platoon in exchange).
- **Company Train**, slimmed down (Baggage element deleted, all-horse-drawn), additionally issued a single light machine gun for local defense of the train, operated by a clerk when needed.

**Total company strength: 147 all ranks** (per Kennedy's explicit figure for the December 1943 reorganization). **Company-organic heavy weapons as of December 1943: 2× 8-cm mortars; no heavy machine guns; no anti-tank rifles.**

**Important note on the subsequent May 1944 revision** (outside this document's 1943 scope, but noted to avoid confusion with the corroborating KStN 131n table used above): in May 1944 the company's 2× 8-cm mortars were swapped out for **2× heavy machine guns** (MG34/42 on tripod), organized as a 13-man Heavy Machine Gun Section, with the mortars transferred up to the newly redesignated Battalion "Heavy Company." This is confirmed directly in the militaryresearch.org KStN 131n transcription (dated 1 May 1944), which shows a "Heavy Machine Gun Section" (2× MG34/42, tripod) and no mortar line at all, alongside a total company strength of 142 all ranks. **This 2-HMG-per-company arrangement is a 1944 feature and should not be projected back onto 1943.**

## Confidence Notes

- **Existence of two distinct 1943 organizational patterns (pre- and post-October/December 1943 "neuer Art" reorganization) — well established.** This is the central, load-bearing fact of this document. It is corroborated by (a) Kennedy's detailed secondary compilation, itself built from primary KStN documents and explicitly dated; (b) direct primary-source text from TM-E 30-451's 1 September 1943 edition, which describes the *pre*-reorganization pattern (10-man squad, 4 squads/platoon, AT rifle section) and is dated squarely within the "early-to-mid 1943" window — an independent confirmation that this pattern was still current as of September 1943; and (c) the general secondary literature (Military History Visualized, Askari Miniatures) which agrees on the broad shape of the change even where it does not cite exact dates as precisely as Kennedy.
- **Early-1943 (131c) squad, platoon, and company figures — well established**, with the 10-man squad and 49-man platoon figures confirmed by two independent primary-source-derived accounts (Kennedy's KStN table transcription and TM-E 30-451's narrative). The "190 all ranks" company figure is **lower confidence** — it is only stated indirectly by Kennedy (as the "from" side of a before/after delta) rather than reproduced as its own tabulated total; treat it as an approximation rather than an exact reproduced figure.
- **Late-1943 (131n, December 1943) squad, platoon, and company figures — well established** for personnel counts and weapon types, again from Kennedy's direct reproduction of the KStN table (personnel/weapon grid format matching the pattern used for the earlier 1941 table). The **147 all ranks company total** is stated directly and explicitly by Kennedy as the December 1943 figure, giving it good confidence, though it is not independently cross-checked against a second primary-source transcription (the only other KStN 131n transcription obtained, militaryresearch.org's, is the later May 1944 revision, not December 1943).
- **Squad leader's personal weapon (MP38/40 machine pistol, both before and after the late-1943 reorg) — well established across every source consulted,** including the actual 1943 primary-source translated German training manual (*The German Squad in Combat*).
- **Second machine pistol added to the reduced 9-man squad, and which man carries it — moderate confidence.** Kennedy's table clearly shows 2× MP total in the 9-man squad (vs. 1× in the 10-man squad), but he explicitly notes uncertainty about which specific post received it ("commonly attributed to..."), and this document follows that same hedge.
- **Panzergrenadier squad's 2 LMG + 1 Panzerschreck-per-squad figure — moderate confidence, single primary-source table, one step removed from the original archival document.** The wwiidaybyday.com transcription of KStN 1114 (1 Nov 1943) is a hobbyist transcription of a genuine German-language KStN table (not a narrative secondary account), and the platoon-level totals (6 LMG, 3 Panzerbüchse 54 per 3-squad platoon) are internally consistent with a 2-LMG/1-Panzerschreck-per-squad reading, but this research was not able to reconcile every personnel subtotal in the table to an exact per-squad headcount (see Open Questions) — treat the squad's total manpower figure as unverified even though its distinctive weapons loadout is reasonably solid.
- **MG34 vs. MG42 usage in 1943 — well established as concurrent/overlapping,** not as a hard cutover date. Sources agree the MG42 began reaching front-line units during 1943 (with more consistent secondary-source dating to "late 1943") but that the MG34 remained in substantial parallel use throughout 1943 and well beyond. No source gives a specific date by which the MG42 became the sole or even majority weapon at squad level in 1943.
- **Discrepancy flagged against the project's own existing data:** `counters/infantry_calc/data/units.csv` row `GER_GREN_1943.3_F` ("Standard German infantry squad mid-1943") lists weapon complement as 1× MG42 + 8× Kar98k (9 men total, **no submachine gun**). Every source consulted in this research — the primary 1943 US Army translation of the German squad-training manual, TM-E 30-451, and Kennedy's KStN table transcriptions for both the pre- and post-reorganization patterns — agrees that the squad leader carried a machine pistol (MP38/40) as his personal weapon, not a rifle, from 1940–41 onward, and that the 9-man (late-1943) squad had *two* machine pistols, not zero. This is a clear point of disagreement that the project may want to revisit; it is called out here rather than silently reproduced, per the task brief's instruction not to contradict the existing data "without a documented reason" — the documented reason is given above. This document does not attempt to resolve which weapon-count the project's game-stat translation should ultimately use; that is explicitly a separate, later step.

## Open Questions / Gaps for Follow-up

- **Exact date within 1943 that the "neuer Art" reorganization reached front-line units** is not pinned down beyond "first KStN drafts October 1943, full version December 1943" — actual re-equipment of specific divisions in the field likely lagged the paper KStN date by weeks to months and was uneven across the Ostheer, so a scenario set in, say, August or September 1943 should almost certainly use the earlier (10-man squad / 4-squad platoon) pattern, while one set in December 1943 or later should use the new-type pattern; the transition is not a hard switch on a single calendar date.
- **The "190 all ranks" early-1943 company total** is an approximation inferred from a stated before/after delta in the source narrative, not a directly reproduced tabulated figure (see Confidence Notes) — a follow-up pass locating an actual reproduced KStN 131c/February 1941 company-level personnel table (as opposed to just the platoon-level table obtained here) would tighten this.
- **Ammunition-carrier's personal weapon in the 10-man (pre-reorganization) squad** — the primary 1943 US-Army translation of the German manual (*The German Squad in Combat*) states he carried a pistol; Kennedy's KStN-table-derived account gives one of the two "assistant" posts a rifle instead of a pistol. This is a minor discrepancy between two good sources and was not resolved.
- **The armored (gepanzert/SPW-mounted) Panzergrenadier company variant (KStN 1114c(gp), 1 Nov 1943)** was identified by title/existence but its squad-level breakdown was not obtained in this pass — only the standard truck-mounted "Grenadierkompanie (mot)" table (KStN 1114 proper) was read in full. If the project needs a distinct "SPW-mounted Panzergrenadier squad" entry (as opposed to the more general motorized/Panzergrenadier squad given here), this is a specific gap to close.
- **Exact personnel subtotals within the Panzergrenadier squad/platoon** (KStN 1114) could not be fully reconciled man-for-man from the transcribed table — platoon-level personnel totals (1 officer + 7 NCOs + 35 men) do not divide evenly by 3 squads plus a stated Platoon HQ headcount, most likely due to either an OCR/transcription artifact in the hobbyist source or a genuine minor asymmetry (e.g., one squad larger than the other two) not called out in the transcription. The squad's *weapon* loadout (2 LMG, 1 Panzerschreck, MP40 leader, G41 deputy) is considered solid; its exact *headcount* (stated elsewhere in secondary literature as commonly "9-10 men," similar to the standard Rifle Squad) is not independently confirmed here.
- **Battalion Machine-Gun Company's 8-cm mortar count** (TM-E 30-451's OCR text reads as "three mortar squads, each having one 81-mm mortar" = 3 total, whereas Kennedy's account of the same-era organization states "a Mortar Platoon of six 8-cm weapons") is inconsistent between these two sources. This is a **battalion**-level detail outside the scope requested for this document (company and below), so it was not pursued further, but is flagged in case a later battalion-level TO&E document needs it.
- This document did not attempt to verify German infantry organization against Nafziger's published OOB handbooks directly (a lead suggested in the task brief) — no accessible full-text copy was located via web search in this pass; all "neuer Art"/KStN-table claims rest on Kennedy's bayonetstrength.uk compilation (itself citing archival KStN sources) rather than Nafziger. If the project has physical or library access to a Nafziger German-Army handbook, it would be a good independent cross-check, particularly for the Panzergrenadier organization.
