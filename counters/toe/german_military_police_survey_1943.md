# German Military Police Survey (1943) — Closeout Check for a Possible MP Unit Type

**Source:** Gordon Williamson, *German Military Police Units 1939-45* (Osprey
Men-at-Arms 213, 1989), `reference/infantry-toe/epdf.pub_german-military-police-units-1939-45-osprey-men-at-arms-213.pdf`,
49pp, image-only scan, read in full via the Read tool's `pages` parameter.

**Task:** this project has no Military Police unit type anywhere in
`units.csv`, and — unlike Airborne, Commando, or Waffen-SS — no existing
rules-text mention of "Military Police" as an unaddressed exemplar or
bracketed elite category (confirmed by a direct grep of `docs/source/*.rst`
for "police" and "Feldgendarmerie" before this pass started: the only hit
was an unrelated aside in E.159 about MP28 submachine guns being "usually
issued to second line or police troops"). There was therefore no prior
signal that this project actually needs an MP unit type; this file records
an honest check of whether the book itself supplies one anyway — a real
1943 combat role a tactical scenario would represent — or confirms that
military police work was exclusively rear-area/traffic-control/security
duty with no place in a tactical-scale combat game.

## What the book actually documents

The book is a genuine, citable organizational reference, not a photo
album — it gives real TOE-style tables, a formation history, and named,
dated anecdotes. Its content splits into two clearly separate categories,
and the book itself draws this distinction explicitly (p.20): units that
were *Military Police in the Provost sense* (Feldgendarmerie, Feldjäger,
Geheime Feldpolizei, and several smaller garrison/rail-security services),
versus units that were merely staffed by *former policemen* but functioned
as ordinary combat divisions (the Waffen-SS "Polizei" divisions).

### Feldgendarmerie des Heeres (Army Military Police) — organization (p.6-7)

A typical **Feldgendarmerie Bataillon** (one per Field Army):

- **Command Group:** 1 officer, 1 warrant officer, 2 NCOs, 3 Other Ranks. Vehicles: 1 field car, 1 small bus.
- **MT Section:** 1 NCO, 3 Other Ranks. Vehicles: 1 motorcycle, 1 field car.
- **Platoons (×3):** 1 officer, 3 NCO drivers, 17 NCOs, 10 Other Ranks. Vehicles: 3 motorcycles, 2 motorcycle combinations, 8 Kübelwagens.
- **Support Group:** one each NCO clerk, MT NCO, armourer NCO, cook NCO, cook OR, armourer OR, clerk OR, cobbler, plus 4 driver ORs. Vehicles: 2× 2-ton trucks, 2× 3-ton trucks.

A typical **Feldgendarmerietrupp** (one per Division; the Armoured/Motorised
Division example given): 1 officer commanding, 2 officer platoon
commanders, 3 NCO + 3 OR motorcycle drivers, 8 NCO + 4 OR + 13 OR drivers,
30 NCOs. Vehicle allocation for an Armoured/Motorised Division: 6 solo
motorcycles, 4 motorcycle combinations (sidecar-mounted MG34/42), 17 light
field cars (Kübelwagen), 2× 2-ton trucks, 2 heavy field cars (4×4
Horch/Steyr), 2× 3-ton trucks.

Personal armament: pistols (Walther P38/Luger P08 for NCOs and men,
Walther PP/PPK favored by officers), MP38/40 carried by most NCOs, Kar98k
seen in photos but "not widely used," and MG34/MG42 issued as a *vehicle or
roadblock-defense weapon*, not a squad infantry weapon.

**Duties** (p.7, quoted list, "by no means complete"): traffic control;
maintaining military order and discipline; collection and escorting of
POWs; collection and redirection of stragglers; prevention of looting;
supervision/control of civilian populace in occupied areas; disarming
civilians; interrogating captured enemy soldiers for documents/maps;
checking travel papers; collecting and preventing distribution of enemy
propaganda; searching for shot-down enemy fliers; street patrols in
occupied areas; prevention of sabotage; control of evacuees during
retreats; counter-espionage liaison with the Geheime Feldpolizei;
apprehending deserters; border control; anti-partisan duties. Every item
on this list is rear-area, security, or discipline work — none of it is a
direct-fire tactical combat function.

### Front-line combat commitment — explicitly a late-war phenomenon, not a 1943 feature

The book states plainly (p.6): **"As the war drew towards its end, many
Feldgendarmerie personnel found themselves thrown into front-line combat,
and the deadly Panzerfaust anti-tank projectile saw frequent use"** — and
again (p.8): **"Towards the end of the war, many Feldgendarmen found
themselves used as front line combat troops in desperate defensive or
counter-attack movements, particularly on the Eastern Front."** Both
statements are unambiguously framed as an end-of-war development. The
book's single detailed combat anecdote for a Feldgendarme — Leutnant Heinz
Heuer's defense of Berlin, where he personally destroyed 13 of 27 spotted
Soviet tanks with Panzerfausts on the night of 21 April 1945 while leading
an ad hoc ~28-man Kampfgruppe (pp.8-9) — is dated April 1945, a year and a
half outside this project's 1943 baseline, and is explicitly the kind of
emergency, front-collapsing combat commitment the "towards the end of the
war" framing describes, not a routine 1943 duty. No dated 1943 Feldgendarmerie
combat anecdote appears anywhere in the book.

### Feldjägerkorps — formed November 1943, but a rear-area discipline/anti-straggler force, not a combat unit

A genuinely 1943-dated organizational event: **"By 1943 Germany's fortunes
were on the turn... Strong measures were called for; and in November 1943
an entirely new force was created — the Feldjägerkorps"** (p.12). Its
personnel standard was notably elite for an administrative service — every
man required a minimum three years' front-line combat service and at
least the Iron Cross 2nd Class — but its stated function was explicitly
**not** combat: "Their function was to preserve order and discipline,
prevent panic retreats, and act as a 'safety net'... Feldjäger operated
approximately 12 miles behind, and parallel to, the front line," collecting
stragglers, assembling scattered remnants into ad hoc units, rounding up
deserters and escaped POWs, checking leave papers, and supporting local
Volkssturm units. Structure: a patrol (*Streife*) of 1 officer + 3
experienced NCOs; ~50 patrols in 3 companies per Feldjägerabteilung; 5
Abteilungen per Feldjäger-Regiment; one Regiment per Feldjägerkommando (I
Königsberg, II Breslau, III Vienna). Feldjäger were "fully entitled to
settle any arguments at gunpoint" — real armed enforcement authority, but
against German stragglers and deserters, not enemy combat units.

### Geheime Feldpolizei (GFP) and other services — all rear-area

GFP (formed 21 July 1939, "Germany's 'plain clothes' military police,
somewhat similar to the British Special Investigation Branch"):
counter-espionage, counter-sabotage, detection of treasonable activity,
counter-propaganda, courts-martial assistance (pp.13-15) — entirely
security/intelligence, not combat. Also documented, all similarly
rear-area: Headquarters Guards (garrison/HQ building security),
Heeresstreifendienst (Army Patrol Service — garrison order/discipline,
"occasional traffic control"), Bahnhofswache (railway-station security,
checking travel papers, hunting deserters), Zugwache (rail-transport
guard), and the Waffen-SS's own smaller Feldgendarmerie
(divisional-strength Trupp of 1 officer + 4 NCOs + 36 men, later a full
Kompanie at divisional strength, "used primarily to maintain order and
discipline within their own unit lines" — p.18).

### "Police combat units" — a distinct, unrelated category, already covered by existing TOE

The book's own text (p.20) draws a sharp line: **"Although not Military
Police in the Provost sense, these men were Police troops and did fight at
the front as combat soldiers, and so were certainly Military Police in the
strict sense of the term"** — describing the two Waffen-SS "Polizei"
divisions raised from former Ordnungspolizei (civilian police) and
Allgemeine-SS reservists, not the actual Feldgendarmerie/Feldjäger. The
**4.SS-Polizei-Panzer-Grenadier-Division** did see genuine, heavy combat:
raised October 1939, fought at Wolchow/Lake Ladoga near Leningrad through
1943 ("rather poorly trained and equipped, its performance was uneven...
it acquitted itself well but suffered heavy losses"), then **"from spring
until summer 1943, the division was used for anti-partisan duties in the
protectorate of Bohemia-Moravia (Czechoslovakia) and in Jugoslavia, where
it took part in the ferocious struggle against Tito's partisan forces,
little quarter being given on either side"** — a real, dated 1943 combat
role. The smaller 35.SS-Polizei-Grenadier-Division never exceeded regimental
strength (raised Feb 1945, too late for this project's baseline). Critically,
**neither division performed Military Police functions in combat** — they
were organized, equipped, and employed as ordinary Waffen-SS
infantry/Panzergrenadier formations that happened to draw their initial
manpower from the civilian police force; their combat record has no
bearing on whether this project needs an "MP unit type," since a rifle
company recruited from ex-policemen is functionally indistinguishable from
any other German infantry/Panzergrenadier company already covered by
`counters/toe/germany_1943.md` and the Waffen-SS thread
(`waffen_ss_michulec_1943.md`).

## Verdict

Reported honestly, per the task's low-expectation completionist framing:
**this book does not support adding a Military Police unit type to this
project.** Every genuine Feldgendarmerie/Feldjäger/GFP duty documented for
the 1943 period is rear-area, administrative, discipline, security, or
counter-intelligence work, with no direct-fire tactical role. The one
real 1943-dated organizational event in this space — the Feldjägerkorps'
formation in November 1943 — falls squarely within this project's baseline
year but is itself a rear-area anti-straggler/discipline force by explicit
design, operating ~12 miles behind the front rather than in it. Front-line
combat commitment for actual Feldgendarmerie is documented, but the book
frames it consistently and explicitly as a phenomenon of the war's final
collapse (1944-45), never as a 1943 feature. Separately, real Waffen-SS
"Polizei" combat divisions existed and did fight in 1943, but they were
ordinary infantry/Panzergrenadier formations by another name, not military
police, and add nothing this project's existing German/Waffen-SS infantry
TOE doesn't already cover.

**No `units.csv` row, unit type, or rule mechanic is proposed by this
file.** If a future coordinator decision wants to represent Feldgendarmerie
on the tabletop anyway (e.g., as a rear-area security/scenario-flavor
element rather than a combat unit — perhaps for a "convoy escort" or
"straggler roundup" scenario type), the Feldgendarmerie Bataillon/Trupp
organizational figures and duty list above are the source material for
that decision; this file only establishes that no *combat*-role
justification exists for one.

## Flavor-text material (not a 1943 anecdote, flagged as out-of-baseline)

Leutnant der Feldgendarmerie Heinz Heuer's defense of Berlin (pp.8-9): the
most highly decorated Feldgendarme of the war, sole Feldgendarmerie
recipient of the Knight's Cross, personally destroyed 13 of 27 Soviet
tanks with Panzerfausts on the night of 21 April 1945 while leading an ad
hoc ~28-man Kampfgruppe against a Soviet command post near Berlin; captured
twice by the Soviets afterward and twice escaped custody. A genuinely
dramatic, named, dated anecdote — but dated April 1945, well outside this
project's 1943 baseline, so recorded here for reference only, not proposed
as period-appropriate flavor text.
