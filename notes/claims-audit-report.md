---
tags:
  - analysis/meta
  - oskg-yahweh
created: 2026-07-24
updated: 2026-07-24
status: complete
---

# Claims Audit Report — July 24, 2026

## Summary

| Metric | Count |
|--------|-------|
| Total claim files audited | 723 |
| Broken frontmatter | 0 |
| Missing required fields | 0 |
| Missing type/claim tag | 0 |
| Missing topic tags | 0 |
| Missing evidence tags | 0 |
| Missing scholar tags | 0 |
| Missing source tags | 0 |
| Non-canonical topic tags | 0 |
| **Broken edge wikilinks** | **40** |
| **Missing primary source links** | **269** |
| **Non-standard confidence ratings** | **3** |
| Forward-reference wikilinks (should be comments) | ~5 |

## 1. Broken Edge Wikilinks (40)

### 1a. Unfilled Template Placeholders (19)

These 19 files contain `[[source-<slug>]]` — the literal template text was never replaced during extraction. All are from Keel/Uehlinger and a few other iconographic/archaeological claims.

Files:
- claim-amun-cryptography-theological-divine-hiddenness-seals.md
- claim-amun-gaza-temple-hidden-god-theology-precursor-aniconism.md
- claim-anthropomorphic-goddess-disappears-iron-i-glyptic-art.md
- claim-ben-anat-warrior-class-restricted-goddess-survival-military.md
- claim-deuteronomistic-suppression-parallels-christian-anti-judaism.md
- claim-erotic-couple-imagery-mb-iib-specific-not-eternal-canaanite.md
- claim-external-evidence-rejects-mosaic-monotheism-extreme-minimalism.md
- claim-falcon-headed-figure-canaanite-egyptian-royal-god-syncretism.md
- claim-fertility-depersonalized-numinous-power-goddess-attributes-detached.md
- claim-fringed-garment-ruler-deified-city-state-king-mediator.md
- claim-iron-age-i-genuine-transitional-period-iconographic.md
- claim-iron-i-iconography-two-themes-aggression-fertility-judges-correlation.md
- claim-megiddo-female-figurines-outnumber-male-sixteen-six.md
- claim-no-distinctive-yahweh-iconography-absorbed-imagery.md
- claim-pictures-better-than-words-constellations-not-propositions.md
- claim-seth-baal-reshef-combat-to-command-standing-motif.md
- claim-tel-kitan-female-stele-massebah-not-necessarily-male.md
- claim-ugaritic-bible-corpora-structurally-flawed-israelite-religion.md
- claim-yahweh-open-ego-absorptive-identity-thomas-mann.md

**Fix:** Replace `[[source-<slug>]]` with HTML comment placeholder.

### 1b. Wrong Primary Source Slugs (6)

- `[[source-kuntillet-ajrud]]` → should be `[[kuntillet-ajrud-inscriptions]]` (3 occurrences)
- `[[source-khirbet-el-qom]]` → should be `[[khirbet-el-qom-inscription]]` (3 occurrences)

Files: claim-kuntillet-ajrud-symbol-not-goddess.md, claim-kuntillet-ajrud-proves-consort.md, claim-kuntillet-ajrud-cult-object-symbolized-goddess.md

### 1c. Non-Existent Claim Wikilinks (15)

| Broken Wikilink | Source File | Resolution |
|----------------|-------------|------------|
| [[claim-divine-council-monotheism-late-development]] | claim-divine-council-seventy-sons-of-el.md | Forward ref → HTML comment |
| [[claim-heiser-subordinate-created-beings]] | claim-divine-council-seventy-sons-of-el.md | Forward ref → HTML comment |
| [[claim-josiah-reform-centralized-not-original]] | claim-divine-image-prohibition-late-exilic.md | → [[claim-josiah-reform-invented-exclusive-yahwism]] |
| [[claim-golden-calves-represented-baal]] | claim-jeroboam-golden-calves-yahwistic-el-bull.md | → [[claim-golden-calves-yhwh-worship-not-pagan-idolatry]] |
| [[claim-pedestal-theory-calves]] | claim-jeroboam-golden-calves-yahwistic-el-bull.md | → [[claim-jeroboam-bethel-cult-conservative-archaizing-bull-pedestal]] |
| [[claim-inscriptions-unambiguously-pair-yhwh-asherah]] | claim-kuntillet-ajrud-symbol-not-goddess.md | → [[claim-dever-archaeology-proves-asherah-real-goddess-yhwh-consort]] |
| [[claim-ugaritic-divine-names-with-suffixes]] | claim-kuntillet-ajrud-symbol-not-goddess.md | Forward ref → HTML comment |
| [[claim-3000-figurines-prove-goddess-worship]] | claim-kuntillet-ajrud-symbol-not-goddess.md | → [[claim-judean-pillar-figurines-asherah-goddess-worship-domestic]] |
| [[claim-divine-statue-in-jerusalem-temple]] | claim-seals-coins-depict-yhwh-anthropomorphic.md | → [[claim-no-anthropomorphic-yahweh-statue-jerusalem-temple]] |
| [[claim-yahweh-el-identification-foundational]] | claim-yahweh-el-originally-distinct-deities.md | Forward ref → HTML comment |
| [[claim-cross-el-yahweh-identity]] | claim-yahweh-el-originally-distinct-deities.md | Forward ref (Cross) → HTML comment |
| [[claim-yahweh-midianite-origin]] | claim-yahweh-originated-south-midian-edom.md | → [[claim-yahweh-southern-mountain-storm-god-midianite-origin]] |
| [[claim-fleming-yahweh-indigenous-origins]] | claim-yahweh-originated-south-midian-edom.md | → [[claim-yahweh-not-taken-from-outsiders-divine-name-israel-diverse-origins]] |
| [[claim-cross-el-yahweh-identity]] | claim-yahweh-originated-south-midian-edom.md | Forward ref (Cross) → HTML comment |
| [[claim-yhwh-asherah-divine-couple-evidence]] | claim-yhwh-represented-by-standing-stones-massebot.md | → [[claim-arad-temple-massebot-yhwh-asherah-divine-couple]] |

## 2. Missing Primary Source Links (269)

Claims that mention a primary source in their text but don't wikilink to it in the Primary Sources section:

| Primary Source | Claims Missing Link |
|----------------|-------------------|
| kuntillet-ajrud-inscriptions | 65 |
| ugaritic-baal-cycle | 57 |
| deut-32-8-9-qumran-variant | 34 |
| lachish-ostraca | 27 |
| khirbet-el-qom-inscription | 25 |
| soleb-shasu-inscription | 22 |
| mesha-stele | 12 |
| elephantine-papyri | 11 |
| ketef-hinnom | 6 |
| merneptah-stele | 6 |
| tel-dan-stele | 4 |

## 3. Non-Standard Confidence Ratings (3)

| File | Current | Should Be |
|------|---------|-----------|
| claim-moses-creative-genius-monotheistic-revolution.md | very-low | low |
| claim-torah-contradictions-prove-antiquity-faithful-transmission.md | medium-low | low-medium |
| claim-torah-sealed-canonized-before-prophecy.md | very-low | low |

## 4. Tag Consistency

All 723 files have complete, canonical tags. No normalization needed. The extraction pipeline produced consistent output.

**Tag distribution highlights:**
- Most-used topic: monotheism (200), historiography (155), yahweh-origin (124)
- Most-used evidence: biblical-text (503), comparative-ane (130), archaeological (129)
- Every scholar tag has a matching source tag

## 5. Cross-Scholar Edge Gaps (identified, not yet audited in detail)

Areas needing cross-scholar edge review:
- Smith + Römer both claim Yahweh originated in south → should cross-reference
- Dever + Smith disagree on Asherah (goddess vs. symbol) → contradiction edges exist but could be denser
- Heiser + Smith disagree on Deut 32:8-9 → needs cross-scholar edges
- Kaufmann + consensus disagree on early monotheism → edges should be explicit
