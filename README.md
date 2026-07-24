# OSKG-YahWeh

An **O**pen **S**tructured **K**nowledge **G**raph applied to the concept of Yahweh in the anthropological record — a data-driven investigation into the historical origins of the biblical God and its implications for an accurate understanding of Old Testament Judaism.

---

## What This Is

A multi-layered research pipeline that transforms 17 scholarly monographs into a queryable, edge-connected knowledge graph of 723 evaluated claims. Each claim is a first-class node tagged by topic, scholar, evidence type, and confidence. Edges are typed: **supports**, **contradicts**, **depends on**, **challenged by**. The graph can answer questions that reading summaries cannot — "show me every claim about Asherah," "what would break if Deut 32:8-9 is monotheistic," "how many scholars converge on Yahweh's southern origin at high confidence?"

The project applies the same structured evidence synthesis methodology used by the Open Research Knowledge Graph (ORKG) at Leibniz University Hannover — independently converged, validated by published literature, and recognized as a supported methodology for computational meta-analysis. See [[METHODOLOGY]] for the full methodological alignment.

## Why Yahweh?

The central question: **who was Yahweh, actually?** Not the God of later Jewish and Christian theology. The deity as his earliest worshippers knew him. A southern storm god? A local Canaanite iteration? A consort to Asherah? The Most High from the beginning? The evidence is scattered across archaeology, epigraphy, philology, and biblical studies. No single scholar holds the full picture. This project synthesizes them all into a single structured corpus and asks: **what does the weight of evidence actually show?**

The implications extend beyond academic curiosity. If the Bible's own internal evidence reveals a polytheistic past later edited into monotheism, what does that mean for how we read the Old Testament? For how we understand the development of Judaism? For faith traditions built on the premise of a unique, unchanging revelation?

## The Pipeline

```
17 books → 154 chapter notes → 723 claims → typed-edge graph → synthesis
```

| Phase | Artifact | Size | Description |
|-------|----------|------|-------------|
| **0. Acquisition** | `sources/books/_fulltext/` (gitignored) | 19MB | 17 monographs extracted to plaintext |
| **1. Chapter Notes** | `notes/theology/` | 154 notes, ~466KB | Chapter-by-chapter critical analysis of every monograph. Every claim evaluated for evidence, confidence, stakes, and disagreement. |
| **2. Claims Extraction** | `notes/claims/` | 723 claims | Each claim extracted into its own file with YAML frontmatter, typed edges, and primary source links. LLM + human-in-the-loop. |
| **3. Knowledge Graph** | Obsidian graph view | Fully connected | Claims are nodes. Edges connect evidence across scholars. Tags filter by topic, scholar, evidence type, confidence. |
| **4. Synthesis** | `notes/synthesis/` | 5 files, 142KB | Hinge inventory, cascade trees, counter-position stress tests, convergence points, and a personal capstone. |

## Graph Structure

### Canvases (Visual Maps)

Open these in Obsidian's Canvas view:

| Canvas | What It Shows |
|--------|---------------|
| **Methodology Canvas** | The full pipeline architecture and ORKG alignment |
| **asherah-debate** | The goddess-vs-symbol fault line across 6+ scholars |
| **convergence-fault-line-map** | Where scholars agree and where they genuinely disagree |
| **counter-position-survival-map** | Heiser/Schmid/Tigay/Kaufmann — what survives each challenge |
| **deut-32-8-9-cascade-map** | Full dependency tree of the project's central text |
| **evidence-density-by-domain** | Textual vs. archaeological vs. onomastic evidence distribution |
| **scholarly-lineage-confessional-map** | Who studied under whom, who's Jewish/Catholic/Evangelical/Atheist |
| **chronology-source-timeline** | Primary sources mapped to historical periods |
| **kaufmann-paradox** | Kaufmann's revolution thesis vs. the consensus |

### Claims (723 nodes)

Every claim file in `notes/claims/` has:
- **Frontmatter:** claim ID, statement, confidence rating, topic tags, evidence tags, scholar tag, source tag
- **Structured body:** The Claim → Evidence → Confidence → Stakes → Disagreement → Edges → Assessment
- **Typed edges:** Supports, Contradicts, Depends On, Challenged By — each with descriptive rationale
- **Primary source links:** Wikilinks to the 18+ inscription files in `sources/primary-sources/`

Filter the graph by tag to see networks: `topic/asherah` (86 connected claims), `topic/kenite-hypothesis` (24 connected claims), `topic/deut-32-8-9` (12 connected claims with cascades).

## Primary Sources (18+ texts)

`sources/primary-sources/` contains full text, translations, and scholarly significance for every major inscription cited in the project:

Kuntillet Ajrud · Khirbet el-Qom · Deut 32:8-9 + 4QDeut · Soleb Shasu · Merneptah Stele · Mesha Stele · Tel Dan Stele · Lachish Ostraca · Ketef Hinnom Amulets · Elephantine Papyri · Ugaritic Baal Cycle (KTU 1.1–1.6, Keret, Aqhat) · Black Obelisk · Kurkh Monolith · Siloam Inscription · Gezer Calendar · Ekron Inscription

## Scholars Covered (17 monographs from 15 scholars)

| Tier 1 (core consensus + counters) | Tier 2 (extensions + challenges) | Reference Works |
|------------------------------------|----------------------------------|-----------------|
| Smith — *Early History of God* (2002) | Albertz — *History of Israelite Religion* Vol I–II (1994) | Keel & Uehlinger — *Gods, Goddesses, and Images* (1998) |
| Smith — *Origins of Biblical Monotheism* (2001) | Day — *Yahweh and the Gods of Canaan* (2000) | Kaufmann — *The Religion of Israel* (1960) |
| Römer — *The Invention of God* (2015) | Fleming — *Yahweh Before Israel* (2021) | Schmid — *Historical Theology of the Hebrew Bible* (2019) |
| Dever — *Did God Have a Wife?* (2005) | Lewis — *Origin and Character of God* (2020) | |
| Sommer — *The Bodies of God* (2009) | Tigay — *You Shall Have No Other Gods* (1986) | |
| Heiser — *The Unseen Realm* (2015) | Cross — *Canaanite Myth and Hebrew Epic* (1973) | |
| Stavrakopoulou — *God: An Anatomy* (2021) | | |

See `notes/theology/scholarly-directory-yahweh-origins.md` for a 45+ scholar reference directory. See `notes/theology/meta-analysis-scholars.md` for analysis of how scholars' confessional commitments, academic genealogies, and institutional incentives shape their conclusions.

## Key Findings (Synthesis)

The four-phase synthesis in `notes/synthesis/` identifies what the graph reveals:

**Hinge claims** (phase 1-2): The top 5 load-bearing claims control cascades of 28-112 downstream claims each. Schmid's late dating of the Pentateuch is the single most destructive counter-position — if correct, ~41% of the consensus graph loses its textual foundation.

**Convergence points** (phase 4): Scholars agree at HIGH+ confidence on: Yahweh's southern origin, El as Israel's original god, monotheism's emergence in the exile, and the divine council as a biblical reality.

**Genuine unknowns** (phase 4): Scholars genuinely disagree (with HIGH confidence on both sides) about: whether Asherah was a goddess consort or a cult symbol, whether Deut 32:8-9 describes one God or two, and whether early Israel was polytheistic or monolatrous.

**Capstone** (`notes/synthesis/capstone-what-does-this-mean.md`, 49KB): Personal synthesis — what the evidence means for faith, scripture, and the God you're left with.

## How to Use

This repository is an **Obsidian vault**. Clone it, open it in [Obsidian](https://obsidian.md), and you get:

- **Graph view:** Filter by tag to see networks of claims, scholars, and evidence
- **Canvas view:** Open the visual maps in `canvases/`
- **Wikilink navigation:** Every claim, note, and source is interlinked
- **Search:** Full-text search across 154 notes, 723 claims, and 18 primary sources

If browsing on GitHub, start at [[Home]].

## Philosophy

1. **Primary sources first.** Every claim links to the inscription or text it cites.
2. **Confidence, not certainty.** Every claim rated VERY HIGH through LOW with explicit rationale.
3. **Steelman every position.** Consensus, counter-positions, and minimalists all represented in their strongest form.
4. **Typed edges.** "Supports" is not "depends on" is not "contradicts." Precision in disagreement.
5. **Human in the loop.** LLM extraction, human verification. The graph is machine-assisted but human-curated.

## Methodology

The pipeline architecture was developed independently but converges with the **Open Research Knowledge Graph (ORKG)** at Leibniz University Hannover (Auer, D'Souza, Farfar et al., 2019–present). Both systems use: structured claim extraction → typed semantic edges → graph querying → evidence synthesis. The independent convergence validates the approach. OSKG-YahWeh differs from ORKG in scale (17 books deep rather than millions of papers shallow) and domain (humanities/biblical studies rather than scientific literature). See [[METHODOLOGY]] for the full analysis.

---

*"The first principle is that you must not fool yourself — and you are the easiest person to fool." — Richard Feynman*
