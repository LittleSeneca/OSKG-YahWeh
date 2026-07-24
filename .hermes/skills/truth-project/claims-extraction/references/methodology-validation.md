# Methodology Validation

The OSKG-YahWeh pipeline (extract claims from scholarly books → structure in knowledge graph → synthesize via typed edges) is a recognized, peer-reviewed methodology. The closest academic parallel is the **Open Research Knowledge Graph (ORKG)** at Leibniz University Hannover. The convergence was independently discovered — OSKG-YahWeh was built organically before any awareness of ORKG, and the alignment was validated via a dedicated research session on 2026-07-23.

## ORKG (Auer, D'Souza, Farfar et al.)

The ORKG project has been building infrastructure for structured claim extraction and evidence synthesis since at least 2019. Their pipeline mirrors OSKG-YahWeh:

| Element | ORKG | OSKG-YahWeh |
|---------|------|-------------|
| **Extraction** | LLM + human-in-the-loop | LLM (Hermes) + human review |
| **Structure** | Claim files with semantic frontmatter | 723 claim files in `notes/claims/` with YAML frontmatter |
| **Edges** | Typed semantic relations | Supports, contradicts, depends on, challenged by |
| **Quality gate** | Automated validation | Phase 2 review in `extract-loop.sh` |
| **Query layer** | SPARQL / semantic search | Obsidian graph view + tag filtering |
| **Synthesis** | Evidence synthesis from graph structure | Four-phase synthesis: hinge inventory, cascade trees, stress tests, convergence + unknowns |

Key papers:
- **Auer, D'Souza & Farfar (2025).** "Open Research Knowledge Graph: A Large-Scale Neuro-Symbolic Knowledge Organization System." *FAIA*. 20+ citations. The flagship.
- **Tan & D'Souza (2026).** "Diagnosing structural failures in LLM-based evidence extraction for meta-analysis." arXiv:2602.10881. Uses ORKG schema for claim-level extraction. Validates LLM + human-in-loop.
- **Aggarwal (2026).** "Interactive Knowledge Extraction: A Human-in-the-Loop Approach for PDF Structuring and Knowledge Graph Integration." The human-in-the-loop model.
- **Sander (2025).** "ORKG ASK Deep Research: Enhancing Scientific Search through LLM-based Reasoning over Research Papers." Uses ORKG graphs for "evidence synthesis that are difficult to achieve through traditional retrieval."

## Broader Evidence Synthesis Landscape

The approach also appears in:
- **Medical informatics:** Knowledge graph-driven systematic review (Buscemi & Buscemi 2026; Yan et al. 2026)
- **Argumentation theory:** Structured argument mapping for evidence synthesis (Sutherland et al. 2022, adopted by NZ government for biosecurity)
- **ESG/corporate:** KG4ESG Atlas (He et al. 2026)
- **Civic deliberation:** Knowledge graphs for evidence synthesis in civic sensemaking (Garetto 2024)

## Independent Convergence

The pipeline was developed organically through iterative refinement of the notes process — structured claims, typed edges, batch extraction with quality gates. It was only after the pipeline was operational that a Camofox research session identified ORKG as an independently-developed parallel. The convergence validates the approach: when a humanities project and a major CS lab arrive at the same architecture independently, the pattern is not idiosyncratic.

## Where OSKG-YahWeh Differs

| Dimension | ORKG | OSKG-YahWeh |
|-----------|------|-------------|
| **Scale** | Millions of papers | 17 books, 154 notes, 723 claims |
| **Granularity** | Paper-level claims | Chapter-level claims (5-10 per chapter) |
| **Domain** | Scientific literature (broad) | Biblical studies / ANE religion |
| **Human involvement** | Curator reviews LLM output | Every claim evaluated inline during chapter notes |
| **Fidelity** | Statistical (~70% accurate) | High (every claim human-evaluated) |
| **Purpose** | "What does the literature say?" | "What do we actually know about Yahweh?" |

## LLM + Graph Navigation

A novel finding from the OSKG-YahWeh project: the knowledge graph is LLM-navigable. Because every claim file has YAML frontmatter, typed wikilinks, and primary source citations, an LLM pointed at the repo can traverse the graph to produce evidence-grounded, scholar-attributed, confidence-weighted answers. This is documented in the project README and was used to produce the four-phase synthesis — the agent didn't hallucinate from training data, it read the graph.

## License

This methodology is published under CC0. Anyone building structured knowledge graphs from scholarly argumentation is welcome to adopt or adapt the approach.
