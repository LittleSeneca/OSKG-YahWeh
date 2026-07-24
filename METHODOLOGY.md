---
tags:
  - type/meta
  - methodology
  - oskg-yahweh
  - oskg
  - knowledge-graph
  - pipeline
created: 2026-08-01
updated: 2026-07-24
related:
  - "[[notes/claims-architecture]]"
  - "[[notes/synthesis/phase1-hinge-inventory]]"
  - "[[notes/synthesis/phase2-cascade-trees]]"
  - "[[notes/synthesis/phase3-counter-position-stress-tests]]"
  - "[[notes/synthesis/phase4-unknowns-and-convergence]]"
  - "[[notes/synthesis/capstone-what-does-this-mean]]"
---

# METHODOLOGY

## What This Is

OSKG-YahWeh is an **Open Source Knowledge Graph** (OSKG) — a structured, queryable graph of scholarly claims about the origins of Yahweh and the emergence of biblical monotheism, built from 17 books, 149 chapter notes, and 723 extracted claims with typed edges. Every claim, edge, and synthesis artifact is open and reproducible.

The graph does not summarize books. It decomposes them into first-class claim nodes and connects them through typed relationships. The synthesis that emerges — what is settled, what is contested, what is load-bearing — is generated from graph structure, not from reading summaries or relying on scholarly reputation.

## What an OSKG Is

An Open Source Knowledge Graph applies three principles:

1. **Structured extraction.** Source documents are not summarized. They are decomposed into discrete, individually addressable claim nodes with explicit metadata (scholar, confidence, evidence type, topic).
2. **Typed edges.** Claims are connected through semantic relationships — supports, contradicts, depends on, challenged by — creating a traversable argument graph, not a flat collection of notes.
3. **Open and reproducible.** Every claim is traceable to its source. Every edge is documented. The synthesis methodology is explicit. Anyone with the same sources can reproduce, audit, or extend the graph.

The canonical academic implementation is the **Open Research Knowledge Graph (ORKG)** at Leibniz University Hannover, which has built the same pipeline architecture for scientific literature since ~2019. OSKG-YahWeh applies the same principles to a humanities domain — biblical studies and ancient Near Eastern religion — where the approach is largely untested.

## The Pipeline

The project moves through five phases:

```
17 books → 149 chapter notes → 723 claims → typed-edge graph → 4-phase synthesis → capstone
```

### Phase 0: Source Ingestion

Scholarly monographs are read chapter by chapter. Each chapter produces a structured note with the author's arguments, evidence, and scholarly interactions. Notes include explicit frontmatter (scholar, work, chapter, topics) and inline cross-references to other scholars and primary sources. This is the extraction substrate.

### Phase 1: Claims Extraction

Each chapter note is decomposed into 5-10 discrete claims. Each claim becomes a standalone file in `notes/claims/` with:

- **YAML frontmatter**: claim ID, scholar, source work, confidence rating (very-high to low), evidence type (biblical-text, archaeological, inscriptional, comparative-ANE, iconographic, onomastic), topic tags
- **Claim statement**: one atomic, falsifiable assertion
- **Edges section**: explicit wikilinks to other claims the claim supports, contradicts, depends on, or is challenged by

Claims are first-class nodes. They are not summaries of what a scholar said. They are testable assertions extracted from scholarly argumentation, tagged with metadata that makes the graph queryable.

### Phase 2: Graph Construction

Edges are created in two passes:

1. **Intra-scholar edges (Phase 1):** Claims from the same scholar are connected during extraction — what depends on what, what supports what, within a single scholar's argument.
2. **Cross-scholar edges (Phase 3):** Claims are connected across scholars — who contradicts whom, who cites whom, where do independent scholars converge on the same finding. This produces the contradiction pairs, support clusters, and convergence patterns that drive synthesis.

Edge types:
- **Supports** — Claim A provides evidence or reasoning for Claim B
- **Contradicts** — Claim A asserts the opposite of Claim B (same topic, incompatible conclusions)
- **Depends on** — Claim B logically requires Claim A to be true
- **Challenged by** — Claim A faces substantive criticism from a scholar who does not directly assert the opposite

### Phase 3: Structural Analysis (Synthesis Phases 1-4)

The completed graph is analyzed through four passes:

**Phase 1 — Hinge Inventory** ([[notes/synthesis/phase1-hinge-inventory]]): Identifies load-bearing claims by counting how many other claims depend on them. The top 25 hinges are ranked by dependency count. Hinge #3 (Yahweh and El were originally distinct deities) has the widest reach at 65 total dependents.

**Phase 2 — Cascade Trees** ([[notes/synthesis/phase2-cascade-trees]]): Traces full collapse radii for the top 5 hinges using breadth-first search to 4 levels deep. Maps what claims become unsupported if a hinge is falsified. Identifies critical children — claims deep in the dependency chain that also face active scholarly contradiction.

**Phase 3 — Counter-Position Stress Tests** ([[notes/synthesis/phase3-counter-position-stress-tests]]): Tests the graph against four major counter-positions. Not "are these positions correct?" but "if they were, what would survive?" Produces survival rates (Heiser 72%, Schmid 41%, Tigay 85%, Kaufmann 58%) and identifies the chronological assumption as the graph's single point of failure.

**Phase 4 — Unknowns and Convergence** ([[notes/synthesis/phase4-unknowns-and-convergence]]): Identifies settled convergences (5+ HIGH+ confidence supports with zero MEDIUM+ contradictions) and genuine unknowns (bidirectional HIGH+ contradictions where both sides are confident). Produces the evidence-density map that drives the capstone.

### Phase 4: Capstone Synthesis

The capstone ([[notes/synthesis/capstone-what-does-this-mean]]) synthesizes the structural analysis into a document that reports what the graph shows: what is settled, what is genuinely contested, what the graph's architecture reveals about evidence density, and where the fragilities lie. The capstone does not summarize books or scholars. It reports graph structure.

## How This Aligns with OSKG Principles

The pipeline converges with the ORKG approach. Both implement the same architecture: structured claim extraction → typed edges → graph querying → synthesis from structure. The convergence across a humanities domain (biblical studies) and a scientific domain (biomedicine, CS) validates the pattern as a general solution to scholarly synthesis.

| OSKG Principle | ORKG Implementation | OSKG-YahWeh Implementation |
|---------------|-------------------|--------------------------|
| **Structured extraction** | LLM + human-in-the-loop extraction from scientific papers | LLM (Hermes) + human review from chapter notes |
| **Claim nodes** | Semantic frontmatter on structured claim objects | Standalone claim files with YAML frontmatter in `notes/claims/` |
| **Typed edges** | Semantic relations between claims | Supports, contradicts, depends on, challenged by |
| **Quality gate** | Automated validation | Phase 2 review in extraction loop |
| **Edge creation** | Cross-paper inference + curator review | Intra-scholar (Phase 1) + cross-scholar (Phase 3) |
| **Query layer** | SPARQL / semantic search | Obsidian graph view + tag filtering + wikilink traversal |
| **Synthesis** | Evidence synthesis from graph structure | Convergence scoring, fault line detection, cascade trees, stress tests |
| **Openness** | Open-access knowledge graph | Open-source GitHub repo, all claims and edges documented |

The convergence is methodologically significant: a humanities knowledge graph and a scientific knowledge graph implementing the same architecture (structured claim extraction → typed edges → graph querying → synthesis from structure) demonstrates the pattern is not domain-specific. It is a general solution to the problem of synthesizing large bodies of scholarly argumentation.

## Where This Differs from the Standard OSKG Approach

| Dimension             | ORKG Standard                                       | OSKG-YahWeh                                                           |
| --------------------- | --------------------------------------------------- | --------------------------------------------------------------------- |
| **Scale**             | Millions of papers, tens of millions of claims      | 17 books, 723 claims                                                  |
| **Granularity**       | Paper-level or finding-level claims                 | Chapter-level claims (5-10 per chapter)                               |
| **Domain**            | Scientific literature (biomedical, CS, engineering) | Humanities: biblical studies, ANE religion                            |
| **Fidelity**          | Statistical (~70% extraction accuracy at scale)     | High (every claim traced to a specific passage in a specific chapter) |
| **Human involvement** | Curator reviews LLM output on samples               | Author evaluates every claim inline during extraction                 |
| **Edge density**      | Sparse (cross-paper connections scale poorly)       | Dense (small corpus enables comprehensive cross-referencing)          |
| **Synthesis depth**   | Broad coverage across many topics                   | Deep analysis of one question: "What do we actually know?"            |
| **Query mechanism**   | Formal semantic queries (SPARQL)                    | Filesystem graph traversal (wikilinks + Obsidian graph view)          |

### The Humanities-Specific Challenge

The standard OSKG approach was designed for scientific literature, where claims are empirical, falsifiable, and relatively self-contained. Humanities scholarship presents different challenges:

- **Claims are interpretive.** "El was Israel's original god" is not falsifiable the way "Protein X binds to Receptor Y" is. Evidence is textual, archaeological, and comparative — different evidence types that do not all point the same direction.
- **Argumentation is sequential.** A scholar's claims in Chapter 7 depend on claims established in Chapter 2. The dependency structure is narrative, not just logical.
- **Disagreement is nuanced.** Scholars rarely say "Smith is wrong." They say "Smith's reading of the Kuntillet Ajrud grammar is possible but the archaeological evidence favors an alternative." Capturing this in typed edges requires judgment.
- **The corpus is small.** 17 foundational books, not millions of papers. This enables high-fidelity extraction (every claim traced to a specific passage) but limits statistical approaches.

OSKG-YahWeh addresses these by trading scale for depth. Every claim is extracted at chapter granularity. Every edge is human-evaluated. The synthesis does not produce statistical meta-analysis — it produces a structural map of where evidence converges, where it genuinely conflicts, and where the graph's architecture reveals fragility.

### Query Layer Differences

The standard OSKG uses formal semantic queries (SPARQL) over RDF triples. OSKG-YahWeh uses the Obsidian vault as its graph database — wikilinks are edges, files are nodes, tag filtering is the query language, and graph view is the visualization layer. This is a pragmatic choice: Obsidian provides a filesystem-native graph that is immediately usable without building a separate query infrastructure. The tradeoff is that formal queries ("show me all HIGH-confidence claims with archaeological evidence that support the Asherah-as-goddess position") require tag navigation rather than a query language. For a corpus of 723 claims, this is sufficient. For larger corpora, a formal semantic layer would be necessary.

## Key References (ORKG Literature)

The ORKG literature provides the academic scaffolding for this methodology:

1. **Auer, D'Souza & Farfar (2025).** "Open Research Knowledge Graph: A Large-Scale Neuro-Symbolic Knowledge Organization System." *Frontiers in AI and Knowledge Organization*. The flagship paper describing structured claim extraction → typed edges → semantic synthesis.

2. **Tan & D'Souza (2026).** "Diagnosing structural failures in LLM-based evidence extraction for meta-analysis." arXiv:2602.10881. Uses ORKG schema for claim-level extraction. Validates the LLM + human-in-loop approach.

3. **Aggarwal (2026).** "Interactive Knowledge Extraction: A Human-in-the-Loop Approach for PDF Structuring and Knowledge Graph Integration." Leibniz University Hannover. The human-in-the-loop extraction model.

4. **Sander (2025).** "ORKG ASK Deep Research: Enhancing Scientific Search through LLM-based Reasoning over Research Papers." Uses ORKG graphs for "evidence synthesis that are difficult to achieve through traditional retrieval."

## Convergence with ORKG

The ORKG literature provides the academic scaffolding for this methodology. The architecture — structured claim extraction, typed edges, graph querying, synthesis from structure — is the same. ORKG validates the approach at scale (millions of papers); OSKG-YahWeh validates the approach at depth (high-fidelity extraction from a small corpus in a humanities domain). The two implementations are complementary: ORKG demonstrates the pattern works for broad coverage; OSKG-YahWeh demonstrates the pattern works for contested, interpretive domains where claims are nuanced and evidence types are diverse.

## Why This Matters

The standard mode of scholarly synthesis is narrative: a human reads many books and writes a summary that identifies patterns. This works but has limits. The synthesizer's own judgments — which scholars to trust, which arguments feel compelling, which patterns seem important — are invisible. The reader cannot audit the synthesis. The synthesizer cannot query the evidence base.

An OSKG makes synthesis auditable. Every claim is individually addressable. Every edge is explicit. The synthesis does not say "scholars agree that El was Israel's original god" — it says "16 claims at HIGH+ confidence support this; zero claims at MEDIUM+ confidence contradict it." The confidence is structural, not rhetorical.

The approach is particularly valuable for contested domains where scholars with different confessional commitments, methodological assumptions, and evidence preferences reach different conclusions. The graph does not resolve these disagreements. But it makes them visible — as bidirectional contradiction edges, as fault lines, as claims that are simultaneously heavily supported and heavily contradicted (Kaufmann's position in this graph). The graph reveals the shape of the disagreement, not just the winner.

## Related Project Documents

- [[notes/claims-architecture]] — Claim file format, tag taxonomy, and edge type specification
- [[notes/synthesis/phase1-hinge-inventory]] — Top 25 load-bearing claims
- [[notes/synthesis/phase2-cascade-trees]] — Full cascade trees for top 5 hinges
- [[notes/synthesis/phase3-counter-position-stress-tests]] — Counter-position stress testing
- [[notes/synthesis/phase4-unknowns-and-convergence]] — Settled convergences and genuine unknowns
- [[notes/synthesis/capstone-what-does-this-mean]] — Culminating synthesis
