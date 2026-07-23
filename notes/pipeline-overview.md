---
tags:
  - type/meta
  - methodology
  - truth-project
created: 2026-08-01
related:
  - "[[claims-architecture]]"
  - "[[../../notes/theology/Theology Index]]"
---

# Truth Project Pipeline — From Books to Claims to Knowledge Graph

## What This Pipeline Does

Turns scholarly books into a queryable, edge-connected knowledge graph of claims about Yahweh. The question isn't "what did Smith say?" — it's "which claims does our evidence support, which contradict each other, and where does the weight of scholarship actually fall?"

---

## Phase 0: Source Acquisition

**Input:** PDFs/EPUBs from Downloads, Library Genesis, or direct purchase.

**Process:** Searched for in Downloads → extracted to plaintext via PyMuPDF (`fitz`) → placed in `sources/books/_fulltext/` (gitignored, local-only, ~19MB, 17 books).

**Output:** Searchable, citable full text of each monograph. The archive includes every major work in the field: Smith (2 books), Römer, Dever, Sommer, Tigay, Cross, Heiser, Stavrakopoulou, Albertz (2 vols), Day, Fleming, Lewis, Keel/Uehlinger, Kaufmann, Schmid.

**Tooling:** `~/.hermes/venv/bin/python3 -c "import fitz..."` one-liner per file.

---

## Phase 1: Chapter Notes (`obsidian-book-notes` skill)

**Input:** Extracted full text in `sources/books/_fulltext/`.

**Process:** Read chapter → identify discrete, evaluable claims → write Obsidian note with full format: Claim, Evidence, Confidence, Stakes, Disagreement, Alternative Reading, Assessment. Cross-referenced with every other book note. One note per chapter.

**Output:** ~149 chapter notes in `notes/theology/`, ~466KB+. Each note has YAML frontmatter with tags, wikilinks to other notes, and a chapter-level assessment table. The notes are critical, not stenographic — every claim is evaluated, not just reported.

**Quality controls:** Pre-writing check (is this one chapter or many?), periodic retrospective review (are later chapters getting thinner?), final retrospective before declaring the book done.

**Skill:** `obsidian-book-notes` — generalized chapter-by-chapter note-taking with claim evaluation.

---

## Phase 2: Claims Extraction (`claims-extraction` skill + `extract-loop.sh`)

**Input:** Chapter notes in `notes/theology/`.

**Process:** Three-phase batch workflow per loop script:

1. **Phase 1 (Extract):** Read 3-5 chapter notes. For each `## Claim N:` block: create a first-class claim file in `notes/claims/` with full YAML frontmatter (claim_id, statement, confidence, confidence_rationale, claim_type, tags for topic/evidence/scholar/source) and structured body (The Claim, Evidence, Confidence, Stakes, Disagreement, Edges, Assessment). Replace the original `## Claim N:` block in the chapter note with a compact summary + wikilink to the claim file. Add edges between claims within the batch and to existing claims.

2. **Phase 2 (Review):** Validate every claim file: all frontmatter fields present, tags complete, evidence section populated (not just placeholders), edge wikilinks resolve to real files. Check for content degradation within batch. Pass/fail per note. Quality gate halts the harness on failure.

3. **Phase 3 (Finalize):** Cross-scholar edge pass (re-read and connect claims across scholars within batch). Update `claims-progress.md` (check off notes, increment counts, append session log). Git commit. Suggest next batch.

**Output:** 380+ claim files in `notes/claims/`, each a first-class Obsidian node with typed edges (supports, contradicts, depends on, challenged by) to other claims. Chapter notes updated with compact summaries and `claims_status: extracted` frontmatter.

**Status:** 75 of 149 notes processed (50%). 380 claims extracted across 25 sessions (23 batches) as of 2026-08-01.

**Tooling:**
- `extract-loop.sh` — batch harness that spawns `hermes chat -q` sessions per phase, parses structured output markers
- `claims-extraction` skill — defines tag taxonomy, claim ID format, edge types, progress tracking
- `claims-progress.md` — single source of truth across sessions

**Batch selection strategy:** Thread-first, not scholar-first. Pick notes across scholars that share a topic (Asherah, Baal, divine council) for maximum edge compounding. Dependency direction: after extracting assertion claims, batch the foundation claims they depend on.

---

## Phase 3: Knowledge Graph Querying (Obsidian)

**Input:** Claim files with typed edges in `notes/claims/`.

**How it works:** Obsidian's graph view renders every claim file as a node. Wikilinks in the `## Edges` section create typed connections between nodes. Tags in frontmatter create filterable facets.

**What you can query (right now, with 380 claims):**

| Query | How |
|-------|-----|
| "Show all claims about Asherah" | Filter graph to `topic/asherah` → see network of 40+ claims across Smith, Römer, Dever, Day, Keel/Uehlinger |
| "What supports claim X?" | Open claim file, read `### Supports` section |
| "Who disagrees about Y?" | Open claim file, read `### Contradicts` and `### Disagreement` sections |
| "What depends on the Soleb inscription?" | Full-text search `Soleb` across claims/ → list claims with that in Evidence or Depends On |
| "Show the argument tree for southern origins" | Filter to `topic/kenite-hypothesis OR topic/midianite-hypothesis OR topic/soleb-shasu` — shows dependency chains spanning 6+ scholars |

---

## Phase 4: Synthesis (pending — not yet built)

Once claims extraction is complete (149 notes → ~700-800 claims), the knowledge graph becomes the engine for synthesis rather than raw note-reading.

**What synthesis looks like with a claims graph:**

- **Argument dependency map:** Trace every claim's edges. A claim with 15+ incoming "depends on" edges is load-bearing — if it falls, the cascade is measured by the number of downstream claims that lose support.
- **Convergence scoring:** For each subtopic, count how many scholars make the SAME claim with HIGH confidence. "Yahweh was originally a southern deity" scores 6+ scholars at HIGH → VERY HIGH meta-confidence.
- **Fault-line detection:** Identify claim pairs with mutual "contradicts" edges. These are genuine disagreements, not scholars talking past each other. The Kuntillet Ajrud "asherah = symbol vs. goddess" debate is visible as a cluster of contradicting edges.
- **Weighted consensus:** For each question ("Did Yahweh have a consort?"), tally: number of scholars saying YES (HIGH or better), number saying NO (HIGH or better), number saying UNCERTAIN. The weight of evidence emerges from the edge structure, not from counting books.

---

## Current State

| Pipeline Stage | Status | Count |
|---------------|--------|-------|
| Source acquisition | Complete | 17 books, 19MB |
| Chapter notes | Complete for 11 books, 6 remaining | ~149 notes, ~466KB |
| Primary sources | Partial | 5 inscriptions collected, 4+ remaining |
| Claims extraction | In progress | 380 claims from 75 notes (50%) |
| Knowledge graph | Live | Fully queryable in Obsidian |
| Synthesis | Awaiting extraction completion | Not yet started |

**Next steps after extraction completes:**
1. Run the tag audit (`obsidian-tag-audit` skill) across all claim files to ensure consistent topic/evidence/scholar tagging
2. Build the argument dependency map by tracing edge chains through the full graph
3. Produce the weighted consensus synthesis document
4. Add Schmid's late-dating challenge as a structural perturbation test (if his claims are true, what percentage of edges break?)
---

## Pipeline Architecture Diagram

```
Downloads (PDFs)
    │
    ▼
sources/books/_fulltext/ (17 plaintext extracts, gitignored)
    │
    │ obsidian-book-notes skill
    ▼
notes/theology/ (~149 chapter notes, ~466KB)
    │  Each note: ## Claim N → Evidence → Confidence → Stakes → Assessment
    │
    │ claims-extraction skill + extract-loop.sh
    ▼
notes/claims/ (380+ claim files, growing)
    │  Each claim: YAML frontmatter + structured body + typed edges
    │  Edges: supports, contradicts, depends on, challenged by
    │
    │ Obsidian graph view
    ▼
Queryable knowledge graph
    │  Filterable by: topic, scholar, evidence type, confidence, claim type
    │
    ▼
Phase 4: Synthesis (pending)
    Argument dependency map, convergence scoring, fault-line detection,
    weighted consensus, Schmid perturbation test
```
