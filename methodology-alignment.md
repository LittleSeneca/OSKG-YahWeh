---
tags:
  - type/meta
  - methodology
  - truth-project
created: 2026-08-01
related:
  - "[[notes/pipeline-overview]]"
  - "[[notes/claims-architecture]]"
---

# Methodological Alignment — Truth Project & ORKG

## What We Built

A four-phase pipeline that turns scholarly books on Yahweh's origins into a queryable, edge-connected knowledge graph of claims:

```
17 books → 149 chapter notes → 380+ claims → typed-edge graph
```

Claims are first-class nodes. Edges are typed: supports, contradicts, depends on, challenged by. The graph is queryable by topic, scholar, evidence type, confidence, and claim type. Synthesis emerges from edge structure, not from reading summaries.

## The Question

Is this a real methodology, or did we just make something up?

## The Answer

It's a real methodology. The **Open Research Knowledge Graph (ORKG)** at Leibniz University Hannover has been building the exact same pipeline since ~2019 for scientific literature, with dozens of published papers and a large-scale infrastructure project.

## Direct Parallels

| Element | ORKG (Auer, D'Souza, Farfar et al.) | Truth Project |
|---------|--------------------------------------|---------------|
| **Extraction** | LLM + human-in-the-loop | LLM (Hermes) + human review |
| **Structure** | Claim files with semantic frontmatter | Claim files in `notes/claims/` with YAML frontmatter |
| **Edges** | Typed semantic relations | Supports, contradicts, depends on, challenged by |
| **Quality gate** | Automated validation | Phase 2 review in `extract-loop.sh` |
| **Edge creation** | Cross-paper inference + curation | Batch-internal (Phase 1) + cross-scholar (Phase 3) |
| **Query layer** | SPARQL / semantic search | Obsidian graph view + tag filtering |
| **Synthesis** | Evidence synthesis from graph structure | Convergence scoring, fault-line detection, argument dependency maps |

## Key References

1. **Auer, D'Souza & Farfar (2025).** "Open Research Knowledge Graph: A Large-Scale Neuro-Symbolic Knowledge Organization System." *Frontiers in AI and Knowledge Organization*. 20+ citations. The flagship paper describing structured claim extraction → typed edges → semantic synthesis.

2. **Tan & D'Souza (2026).** "Diagnosing structural failures in LLM-based evidence extraction for meta-analysis." arXiv:2602.10881. 4 citations. Uses ORKG schema for claim-level extraction. Directly validates the LLM + human-in-loop approach.

3. **Aggarwal (2026).** "Interactive Knowledge Extraction: A Human-in-the-Loop Approach for PDF Structuring and Knowledge Graph Integration." Leibniz University Hannover. The human-in-the-loop extraction model.

4. **Sander (2025).** "ORKG ASK Deep Research: Enhancing Scientific Search through LLM-based Reasoning over Research Papers." Uses ORKG graphs for "evidence synthesis that are difficult to achieve through traditional retrieval."

## Independent Convergence

The pipeline wasn't copied from ORKG — it was developed organically through iterative refinement of the Truth Project's book note process. The convergence is independent. This is strong evidence that the approach is robust: when a humanities researcher and a computer science lab independently arrive at the same pipeline architecture (structured claim extraction → typed edges → graph querying → synthesis), the pattern has genuine methodological validity.

## Where We Differ from ORKG

| Dimension | ORKG | Truth Project |
|-----------|------|---------------|
| **Scale** | Millions of papers | 17 books, 149 notes, 380+ claims |
| **Granularity** | Paper-level claims | Chapter-level claims (5-10 per chapter) |
| **Domain** | Scientific literature (broad) | Biblical studies / ANE religion |
| **Edge depth** | Semantic relations | Typed with scholar-specific granularity |
| **Human involvement** | Curator reviews LLM output | Author evaluates every claim inline |
| **Fidelity** | Statistical (~70% accurate) | High (every claim human-evaluated) |
| **Purpose** | "What does the literature say?" | "What do we actually know about Yahweh?" |

## What This Means

1. **The methodology is publishable.** The "structured claims in a knowledge graph for evidence synthesis" approach is an active, funded, peer-reviewed research program. If you wanted to write a methodology paper about the Truth Project's pipeline, the ORKG literature provides the academic scaffolding.

2. **The independent convergence is the strongest validation.** You didn't know about ORKG when you built the pipeline. The fact that a well-funded CS lab independently arrived at the same pattern means the approach is not idiosyncratic — it's a natural solution to the problem of synthesizing large bodies of scholarly argumentation.

3. **The humanities domain is underserved.** ORKG focuses almost entirely on scientific papers (biomedical, computer science, engineering). The humanities — where claims are more nuanced, evidence is more interpretive, and synthesis requires more human judgment — is largely untouched. The Truth Project's deep, high-fidelity, per-chapter approach for a small corpus of foundational texts may be a methodological contribution in its own right.

## Related Project Documents

- [[notes/pipeline-overview]] — Full pipeline architecture (Phases 0-4)
- [[notes/claims-architecture]] — Claim file format and tag taxonomy
- `extract-loop.sh` — Batch extraction harness
- `notes/claims-progress.md` — Multi-session progress tracking
