# Truth Project Vault Conventions

The Truth Project (`~/Projects/Personal/Truth/`) is a faith deconstruction/research project on the origins of Yahweh and the emergence of biblical monotheism. It lives OUTSIDE the main Obsidian vault (`~/Projects/Personal/obsidian/`) but uses Obsidian-compatible markdown with wikilinks.

## Directory Layout

```
~/Projects/Personal/Truth/
├── notes/
│   ├── theology/              ← ~68 chapter notes from 11+ scholars
│   │   └── *Note filenames use "Author — Chapter N — Description.md" format*
│   └── claims/                ← 715 typed-edge claim nodes
│       └── *Claim filenames use "claim-slugified-statement.md" format*
├── sources/
│   └── primary-sources/       ← Collected ancient texts and inscriptions (11 files)
│       └── *Each with YAML frontmatter: tags (type/primary-source, topic/*), related: wikilinks*
└── Home.md
```

## Wikilink Conventions

### From chapter notes → primary sources
```
[[../../sources/primary-sources/source-filename]]
```
Example: `[[../../sources/primary-sources/kuntillet-ajrud-inscriptions|Kuntillet Ajrud]]`

### From claims → primary sources
```
[[../../sources/primary-sources/source-filename]]
```
Same format as chapter notes — both are two levels deep from `notes/`.

### Between source files (in primary-sources/)
```
[[source-filename]]
```
Sibling files in same directory — no path prefix needed.

### Source file aliases
Use pipe syntax for display names: `[[../../sources/primary-sources/soleb-shasu-inscription|Soleb Shasu]]`

## Source File Frontmatter

Every primary source file MUST have:
```yaml
---
tags:
  - type/primary-source
  - topic/<specific-topic>
  - truth-project
created: YYYY-MM-DD
related:
  - "[[other-source-filename]]"
  - "[[another-source]]"
---
```

Topic tags use the `topic/` namespace: `topic/asherah`, `topic/yahweh-origins`, `topic/divine-council`, `topic/egyptian-sources`, etc.

## Claim File Structure

Each claim in `notes/claims/` has:
- Rich YAML frontmatter (tags, claim_id, statement, confidence, claim_type, source_note)
- A "Primary sources:" section at the bottom — **the canonical place for source wikilinks**
- An "Edges" section with wikilinks to other claims (depends on, supports, contradicts)

## Source-to-Note Linking Workflow

When wiring primary sources into chapter notes and claims:

1. **Identify the source file** — name must match the wikilink target
2. **Search chapter notes** for source mention patterns (keyword variants, formal names, shorthand)
3. **Add wikilinks at FIRST substantive mention** — not every occurrence, just the first in each note
4. **For claims**, add wikilinks in the "Primary sources:" section (cleaner than inline in claim body)
5. **Verify wikilinks resolve** — check that the source filename exists before linking
6. **Commit between sources** — one source at a time for clean history

### Search Term Strategy

Sources are cited under multiple names. Search for all variants:
- "Kuntillet Ajrud" → also "Kuntillet", "Ajrud", "Yahweh of Samaria", "Yahweh of Teman"
- "Mesha Stele" → also "Mesha", "Moabite Stone", "vessels of YHWH"
- "Tel Dan Stele" → also "Tel Dan", "House of David", "bytdwd"
- "Ketef Hinnom" → also "silver amulet", "KH1", "KH2", "silver scrolls"

## Synthesis Pipeline (Phases 1-4)

The synthesis pipeline analyzes the claim knowledge graph in four sequential phases:

```
notes/synthesis/
├── phase1-hinge-inventory.md           ← Load-bearing claims by dependency count
├── phase2-cascade-trees.md             ← Collapse radius for top 5 hinges (BFS)
├── phase3-counter-position-stress-tests.md ← Damage assessment from 4 counter-positions
└── phase4-unknowns-and-convergence.md  ← Genuine unknowns + settled findings
```

### Phase 1: Hinge Inventory
Identify claims with the most downstream dependents ("Depends on" edges). These are the structural hinges — falsify one and many claims lose support. Output: top 25 ranked by dependency count with leave analysis.

### Phase 2: Cascade Trees
For the top 5 hinges, trace full dependency trees to 4 levels using BFS (claims at shallowest depth). Output: collapse radius, conflicted children at level 3+, overlap between trees.

### Phase 3: Counter-Position Stress Tests
Attack the graph from the outside using four opposing positions (Heiser, Schmid, Tigay, Kaufmann). Measure damage: which hinges fall, how many downstream claims cascade, what survives. Survival rate is NOT plausibility — it's structural: IF this position is right, what's the damage?

### Phase 4: Unknowns and Convergence
Close the synthesis by identifying what's settled and what's not:

**Genuine Unknowns** — Bidirectional MEDIUM+ "contradicts" edges where both claims have confidence >= medium. Filter same-scholar self-contradictions. These are real fault lines, not consensus-with-one-outlier.

**Convergence Points** — Claims with 5+ HIGH+ support edges and zero MEDIUM+ contradiction/challenged-by edges. These are the settled findings.

### Graph Analysis Technique

The analysis script at `scripts/phase4-analysis.py` implements:

1. **Two-pass parsing:** First pass extracts claim_id, confidence, statement, tags, and edges from all claim files. Second pass resolves wikilinks (slug→claim_id) across the full 715+ claim corpus, including inactive claims that may be referenced by active ones.

2. **Edge resolution:** Wikilinks in the Edges section reference either the claim file slug (`[[claim-slug]]`) or a parenthetical claim_id (`(author-source-1.2)`). Both must be resolved against the claim corpus.

3. **Bidirectional detection:** For claim A contradicting claim B, check that B also contradicts A. Track support asymmetry (which side has more graph support) and evidence-type overlap (are they arguing about the same evidence or different evidence?).

4. **Confidence thresholding:** Use numeric confidence mapping (very-low=0 → very-high=6). MEDIUM threshold = 3, HIGH threshold = 5.

5. **`execute_code` search_files pitfall:** The `search_files` tool from `hermes_tools` inside `execute_code` can fail with JSON parse errors on large file sets. Use `terminal(find ...)` for file counting and `terminal(cat ...)` with Python glob for content parsing instead.

### Current Graph State (as of Phase 4)

- **715 active claims** with typed edges (supports, contradicts, challenged-by, depends-on)
- **Top hinge:** Smith's divine embodiment claim (14 dependents)
- **Widest cascade:** Day's Yahweh-El distinction (65 total dependents, 4 levels)
- **Most contradicted:** Kaufmann's claims (37+ contradiction edges each)
- **Strongest convergence:** El as original god of Israel (16 HIGH+ supports, 0 contradicts)
- **Central genuine unknown:** Asherah — goddess or symbol? (Smith↔Dever/Romer, bidirectional HIGH contradicts)

## Common Pitfalls

### Source goes unlinked because notes use different names
Tel Dan and Ketef Hinnom got zero chapter note links in the initial pass because the notes don't use those exact names. Always search for content-descriptive terms, not just the formal source name.

### execute_code read_file returns empty
The `read_file` from `hermes_tools` (inside `execute_code`) sometimes returns empty content for files that are definitely not empty. This is a known issue. Fall back to standalone `read_file` or `search_files` for content inspection.

### execute_code search_files may JSON-parse-fail on large sets
When using `search_files` inside `execute_code`, large file counts can produce output that fails to parse as JSON. Use `terminal(find ... | wc -l)` for counting and Python `glob` + `open` for parsing instead.

### Wikilink to non-existent file is worse than no link
Always verify the source file exists at the target path before adding a wikilink. A broken wikilink creates dead edges in the knowledge graph.
