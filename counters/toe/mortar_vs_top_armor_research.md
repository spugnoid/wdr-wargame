# Research Memo: Can WWII Mortar/Light Artillery HE Penetrate Tank Top Armor?

**Purpose:** Historical research to inform whether "With Deepest Regret..." should allow mortars/light
artillery HE rounds to roll on the Section 18 penetration tables against closed AFVs via contact-fuze
top hits, or whether the current flat rule ("Mortars never roll on Section 18 penetration tables against
closed AFVs — suppression only") is the historically defensible position.

Scope note: this is about *ordinary contact-fuzed HE* mortar bombs and light/divisional artillery HE
shells landing on the top deck/turret roof. It explicitly excludes shaped-charge/HEAT top-attack munitions
(e.g., modern sensor-fuzed submunitions), which are a different, well-documented mechanism from a later era.

---

## Q1: Did WWII mortars/light artillery HE have real documented capability to penetrate top/deck armor via contact fuze?

**Finding:** Weak/marginal capability at best, and only against the thinnest top surfaces on the lightest
vehicles or non-armor "weak spots" (engine louvres, radiator grilles, vision blocks, hatch seams) — not
against a solid rolled/cast roof plate of typical thickness. No source found asserts confident, repeatable
penetration of a proper turret roof or hull deck plate by mortar or light-gun HE.

- Forum synthesis (Axis History Forum, "Mortars vs Tanks" thread) states plainly: "the mortar is poorly
  suited for attacks on tanks" and that top armor hits are valuable mainly for *mobility kills via engine
  deck damage* rather than crew-compartment penetration: "An 81mm mortar round might not be able to get
  into the crew compartment but hitting [the] engine['s] thin top armor can make a mobility kill."
  (https://forum.axishistory.com/viewtopic.php?t=222799) — **Confidence: medium**. This is an informed
  enthusiast/wargamer discussion thread, not a primary source, but it aligns with the ordnance data below
  and with doctrine sources.
- The same thread notes German 81mm mortar bombs carried roughly 0.5 kg of TNT-equivalent filler, "about
  equal to a 75mm HE tank shell" — i.e., meaningful blast/frag power against unarmored things, but the
  thread explicitly qualifies this as effective mainly "against the lighter or earlier tanks" and via
  vulnerable unarmored features (radiator grilles, engine intakes) rather than through armor plate proper.
  **Confidence: low-medium** (secondary, uncited explosive-weight figure, plausible but not independently verified here).

**Bottom line for Q1:** No real evidence of mortars/light HE defeating actual armor plate on a tank
top/deck. What evidence exists points to secondary routes (engine grilles/louvres, open hatches, vision
blocks) rather than penetration of the armor itself.

---

## Q2: Is there a known formula/rule of thumb relating HE shell caliber or explosive weight to penetration of armor plate?

**Finding:** Yes — a well-documented naval/ordnance engineering rule of thumb exists, and it can be
extrapolated (with real caveats) to mortars and field guns.

- NavWeaps' Nathan Okun ordnance-technical resource ("Miscellaneous Naval-Armor-Related Formulae",
  https://www.navweaps.com/index_nathan/Miscarmr.php) gives empirically-derived caliber-fraction limits for
  fragment/blast perforation of quality WWII armor plate (US STS / "Class B" homogeneous steel):
  - AP projectile fragments: **~0.08 × caliber**
  - Common/SAP projectile fragments: **~0.095 × caliber**
  - Large-cavity HE/HC-type projectile fragments (thin-walled, big bursting charge): **just over 0.11 × caliber**
    — this is the "sideways fragment, at ~5 calibers standoff" limit, i.e. a near-miss/graze case, not
    a direct contact detonation.
  - For an **instantaneous-fuzed HE projectile detonating in direct contact with the plate** (which is the
    relevant case for a mortar bomb's PD fuze hitting a tank deck), the source states penetration/hole-making
    capability increases sharply — on the order of "142%" greater than the standoff/fragment-only case — to
    the point it can blow a caliber-wide (or larger) hole through plate at or below that increased thickness
    limit, i.e. very roughly on the order of **0.15–0.16 × caliber** for a plate it can hole outright, though
    the source frames this qualitatively (hole size scaling with shell length/diameter) rather than as a
    single hard multiplier.
  - **Confidence: medium-high** for the general engineering principle (this is a widely cited naval ordnance
    reference used by naval historians); **low** for applying naval heavy-shell-vs-ship-armor data directly to
    mortar bombs vs. tank plate — different plate quality (face-hardened ship armor vs. rolled/cast tank
    steel), different burster ratios, different impact geometry (near-vertical drop vs. naval near-horizontal
    flat trajectory), and no source found that validates the formula specifically against WWII tank deck steel.

**Applying the rule of thumb (illustrative, not authoritative) — contact-burst case, ~0.15–0.16× caliber:**

| Weapon | Caliber | Rough contact-burst hole-through capability |
|---|---|---|
| 50mm light mortar | 50mm | ~7.5–8mm |
| 60mm light mortar | 60mm | ~9–10mm |
| 81/82mm medium mortar | 81mm | ~12–13mm |
| 120mm heavy mortar | 120mm | ~18–19mm |
| 75mm infantry/tank gun HE | 75mm | ~11–12mm |
| 105mm light howitzer HE | 105mm | ~16–17mm |

Even taken at face value, these numbers sit at or below the low end of tank top armor (see Q3) for
everything except the 120mm heavy mortar and 105mm+ howitzers against the very thinnest (10–13mm) roofs —
and that's before accounting for the plate-quality/geometry caveats above, which all cut against the mortar.

- **Confidence: low** on the specific extrapolated numbers in the table (my calculation applying a
  naval-armor formula outside its validated domain) — presented as an order-of-magnitude sanity check, not
  a design-ready formula. Flagging this explicitly so it isn't mistaken for sourced fact.

---

## Q3: What thickness is WWII medium/heavy tank top/deck armor typically?

**Finding:** Roughly 8–26mm across nations and vehicle classes, generally on the thinner end for hull/engine
deck and slightly thicker for turret roofs on later/heavier designs. This is thin in absolute terms, but see
Q2 — it's still generally above or at the ragged edge of what contact-fuzed mortar/light-gun HE could
plausibly defeat, especially once plate-quality caveats are applied.

Approximate figures gathered from general secondary sources (Britannica, Sherman Tank Site, Wikipedia
aggregation — **confidence: medium**, these are commonly repeated figures rather than primary armor
specification documents, but they agree with each other):

- **Panzer IV**: turret roof ~10mm; hull roof ~10mm (thinner early, similar through most production).
- **Panther**: turret roof ~16mm; hull deck ~16–17mm.
- **Tiger I**: turret roof ~25mm; hull deck ~25mm (notably thicker than most).
- **T-34 (1941–43)**: hull top ~15–20mm (one source used in discussion below cites 20mm specifically for
  hull top).
- **M4 Sherman**: hull roof as thin as ~13mm (0.5in) in places, turret roof somewhat thicker (~25mm/1in
  region reported for turret top on many variants — figures vary by source and production change).

**Bottom line for Q3:** "Thin" top armor in WWII tanks is generally in the **10–25mm** band, not the 25mm+
band of hull/turret front armor, so it's not absurd on its face that HE effects might matter — but per Q2,
even a 120mm heavy mortar's contact-burst capability is only borderline against the low end of this range,
and medium (81/82mm) mortars and typical 75mm-class HE are well below it against anything but the very
thinnest decks (10–13mm, i.e., early/light tanks' engine decks, not turret roofs).

---

## Q4: Documented real combat incidents of a tank being knocked out or seriously damaged by a mortar/light artillery round landing on top?

**Finding: No confirmed, specific, named incident found.** This is the weakest-evidenced of the five
questions, and the search consistently surfaced statistical loss-cause studies (aggregate data, not
individual documented incidents) or well-known incidents that turned out to have other causes.

- **Michael Wittmann's Tiger (Villers-Bocage, Aug 1944)** was checked as a plausible famous "top hit"
  candidate — but sourced accounts (Wikipedia; Warfare History Network) attribute his death to either a
  British Firefly 17-pounder side/rear hit igniting ammunition, or possibly a rocket-firing Typhoon strike
  on the engine deck — not a mortar or field-artillery HE round. **Confidence: medium** this rules out
  Wittmann as an example; the exact cause is still debated among historians, but "mortar bomb" is not one
  of the competing theories.
- Statistical loss-cause surveys consistently show artillery/mortar/HE as a *minor* overall cause of tank
  loss, and none of the sources found break this down further into "penetrated the roof" vs. "damaged
  track/wheels/engine grille from a near top hit" vs. "crew bailed from concussion" — which is itself
  telling: if top-armor penetration by HE were a recognized, named phenomenon, the loss-cause literature
  would likely have a category for it, and it doesn't. See Q5 sources for the actual numbers.
- The Axis History Forum discussion (non-primary, informed enthusiast synthesis) frames mortar "kills" on
  tanks as mobility kills via engine-deck/grille damage, not turret-roof/hull-deck armor penetration
  proper — consistent with there being no clean "mortar penetrated the roof" anecdote in the record.
  **Confidence: low** as a source, but consistent with the absence of a real citable incident elsewhere.

**Bottom line for Q4:** Absence of evidence isn't proof of absence, but given how much WWII armor-loss
literature exists (ORO-T-117, British 21st Army Group ORS reports, German loss returns, etc.) and how
thoroughly this exact question has apparently already been chewed over in wargame-design forums without
anyone producing a clean citable incident, the fair reading is that **top-armor-penetration kills by
mortar/light-artillery HE are, at best, vanishingly rare and not clearly attested in the record** — as
opposed to, say, tank losses to mines or Panzerfausts, which have abundant specific documented incidents.

---

## Q5: How did WWII doctrine actually treat mortars as an anti-tank tool?

**Finding:** Consistently and explicitly as a suppression/harassment/button-up tool, not a killing
mechanism, across the sources found — this is the best-supported of the five questions.

- U.S. Marine Corps doctrine reference material and general infantry-tactics literature (via search
  synthesis of MCWP 3-15.2 *Tactical Employment of Mortars* content, and separately the Axis History Forum
  discussion) describes mortar fire's contribution to the "antiarmor battle" as: forcing tank crews to
  **button up** (severely degrading vision), **separating** dismounted infantry from supporting tanks so the
  tanks become vulnerable to dedicated AT weapons/infantry, and generally **harassing/obscuring** rather
  than destroying the tank directly. A buttoned-up, unsupported tank is explicitly framed as "a relatively
  helpless piece of equipment" for *other* arms (bazookas, AT guns, satchel charges, close-assault infantry)
  to then finish off. **Confidence: medium** — this is standard, uncontroversial doctrine language repeated
  across multiple eras/sources and matches known combined-arms AT doctrine generally (mortars suppress,
  something else with real AP capability kills).
- Quantitative confirmation that HE/mortar fire was a minor tank-killing category in practice:
  - **ORO-T-117** ("Survey of Allied Tank Casualties in World War II," Coox & Naisawald, 1951 — a primary
    U.S. Army Operations Research Office study, archived at
    https://archive.org/details/oro-t-117): for Western Europe 1944, ~50.9% of US tank losses (1051/2065)
    were attributed to gunfire (AP shot), i.e. the dominant kill mechanism was direct-fire AP guns, not HE.
    **Confidence: high** for the top-line gunfire figure (primary Army ORO study); I could not fully extract
    the granular mortar-specific sub-breakdown from this particular document within this research pass — see
    caveat below.
  - A widely-repeated secondary figure (sourced to Richard C. Anderson Jr.'s work on U.S. tank
    design/doctrine, surfaced via forum discussion) states: of 883 First U.S. Army light/medium tank losses
    investigated, only **12 (1.36%)** were attributed to mortar fire specifically (no distinction between
    50mm/81mm/120mm mortars). **Confidence: medium** — I have this via a secondary citation chain
    (forum → Anderson) rather than having directly read Anderson's primary text, but the figure is
    consistent with the broader pattern below.
  - **The Dupuy Institute's "Artillery Effectiveness vs. Armor" series**
    (https://dupuyinstitute.org/2018/10/15/artillery-effectiveness-vs-armor-part-1/ and linked Kursk/Ardennes/
    summary parts) — a serious quantitative historical-analysis outfit — found **artillery fire (mortars +
    guns combined) caused an average of ~12.8% of tank/AFV losses** across seven WWII engagements studied
    (range 5.9%–14.8%), versus AP gunfire dominating the rest. Their summary piece explicitly notes the data
    sample is still limited (only 7 engagements, small heavy-tank sub-sample) and does **not** break down how
    many of those artillery-caused losses were actual armor penetrations vs. mobility kills, crew casualties
    from open hatches, or "combat ineffective" (bailed out/suppressed) results. **Confidence: medium-high**
    on the ~12.8% aggregate figure as reported by a credible quantitative historical-analysis group; **no
    data available** on the penetration-vs-other-mechanism breakdown, which is exactly the question this
    memo needs — so it doesn't resolve Q1 by itself, but it bounds how big a phenomenon this could possibly be.
  - **British 21st Army Group / No. 2 Operational Research Section** studied armored-unit casualties in NW
    Europe (24 Mar–5 May 1945): of casualties (crew casualties, not necessarily tank losses) **41% AP shot,
    33% "H.C." (hollow-charge/HEAT weapons — Panzerfaust etc.), 21% AT mines, 3% H.E. shells, 2% unknown.**
    HE shells (which would include mortar and field-artillery HE) are the smallest identified category at
    **3%**. **Confidence: medium** — figure surfaced via secondary aggregation citing the ORS study; could
    not independently verify against the primary ORS report text in this pass, but it's a specific, plausible
    number consistent with everything else found.

**Bottom line for Q5:** Every source found — doctrine descriptions, primary-adjacent ORO/ORS casualty
studies, and quantitative historical-analysis (Dupuy Institute) — agrees that mortar/light-artillery HE was
understood and used as a suppression/button-up/harassment tool, and that HE fire (mortar + field guns
combined) was a small minority cause of actual tank losses (roughly 3%–13% depending on study and what's
counted), utterly dwarfed by AP gunfire. Nothing found treats penetration as the intended or expected
mechanism.

---

## Bottom line

The historical record does **not** support giving mortars/light HE artillery a real, meaningful
top-armor-penetration capability against closed AFVs. Every line of evidence points the same direction:

- The one hard engineering rule of thumb available (NavWeaps/Okun caliber-fraction formula, extrapolated
  with real caution outside its validated naval-armor domain) puts contact-burst HE hole-making capability
  at roughly 0.15–0.16× caliber — which only clears WWII top-armor thicknesses (Q3: ~10–25mm) for the
  heaviest mortars (120mm+) and only against the thinnest decks, and even then the extrapolation itself
  carries real uncertainty (different plate quality/geometry than the naval case it's drawn from).
- No specific, citable combat incident of a mortar or light-artillery HE round penetrating a tank's top
  armor and killing/disabling it was found, despite this being exactly the kind of question wargame-design
  communities have already gone looking for and apparently come up empty on too.
- Every quantitative casualty study found (ORO-T-117, British 21st Army Group ORS, Dupuy Institute's
  cross-engagement analysis) shows HE/mortar fire as a small minority cause of actual tank losses (roughly
  3–13%), and contemporary doctrine explicitly describes mortars' anti-tank role as suppression/button-up/
  infantry-separation, not killing power.

Where mortar/HE fire against tanks *does* have real documented teeth is exactly what the current WDR rule
already models: forcing buttoned-up crews (vision/situational-awareness penalty), suppressing/scattering
accompanying infantry, and — per the informed forum synthesis, with lower confidence — occasional mobility
kills via unarmored engine-deck grilles/louvres or track/roadwheel damage rather than through solid armor
plate. If the designer wants to add *anything* for top hits, the historically defensible version would be
narrow and probably should not be a straight "roll on Section 18" penetration mechanic: at most, a
special/rare mechanism gated to heavy mortars (120mm+) or larger-caliber HE against specifically the
thinnest hull/engine-deck locations (not turret roofs generally), likely modeled as a mobility-kill /
component-damage check rather than a full penetration-and-crew-casualty result — and even that should be
treated as a low-probability, "historically marginal" event rather than a routine capability, given how
consistently the sourced data shows this was not how tanks actually died in WWII.

**Overall confidence in this bottom-line judgment: medium-high.** It rests on convergent evidence from
several independent lines (doctrine literature, two different national casualty studies, one quantitative
cross-engagement historical analysis, and an engineering rule-of-thumb sanity check) all pointing the same
way, even though no single source was a slam-dunk primary-source answer to the exact question asked, and
several individual figures were sourced through secondary/forum citation chains that could benefit from
direct primary-source verification (ORO-T-117 full text, British ORS reports, Anderson's book) if the
designer wants to firm this up further before finalizing the rule.

---

## Sources referenced

- Axis History Forum, "Mortars vs Tanks" thread — https://forum.axishistory.com/viewtopic.php?t=222799 (enthusiast/wargamer discussion synthesizing mortar-vs-tank ordnance and doctrine points; not primary, used for orientation and cross-checked against other sources)
- NavWeaps / Nathan Okun, "Miscellaneous Naval-Armor-Related Formulae" — https://www.navweaps.com/index_nathan/Miscarmr.php (naval ordnance engineering reference; caliber-fraction penetration rule of thumb, extrapolated here to mortars/field guns with caveats)
- ORO-T-117, "Survey of Allied Tank Casualties in World War II" (Coox & Naisawald, 1951) — https://archive.org/details/oro-t-117 (primary U.S. Army Operations Research Office study)
- The Dupuy Institute, "Artillery Effectiveness vs. Armor" series (Parts 1–5) — https://dupuyinstitute.org/2018/10/15/artillery-effectiveness-vs-armor-part-1/ and linked parts (quantitative historical-analysis organization; cross-engagement casualty-cause data)
- Tank Archives, "Tank Crew Losses" — https://www.tankarchives.com/2016/03/tank-crew-losses.html (Soviet crew-casualty-by-position data; did not break down by weapon cause)
- General secondary/reference sources on tank armor thicknesses (Britannica, The Sherman Tank Site, Wikipedia aggregation) used for Q3 approximate figures
- Secondary citation (via forum) to Richard C. Anderson Jr.'s work on U.S. tank design/doctrine, for the "883 losses / 12 mortar-caused / 1.36%" First U.S. Army figure
- Secondary citation (via forum aggregation) to a British 21st Army Group / No. 2 Operational Research Section study of armored-unit casualties, NW Europe, 24 Mar–5 May 1945, for the AP/HC/mine/HE casualty-cause breakdown
- Wikipedia and general encyclopedic sources used only as orientation/starting points, not relied on for final claims, per research instructions
