# Truth Project: Claims Extraction

Reference implementation of the multi-session batch processing pattern. This is the first use case that motivated the skill's creation.

## Context

The Truth project (`~/Projects/Personal/Truth/`) has ~152 chapter notes across 13+ scholars, each containing 4-10 explicitly formatted scholarly claims. The goal: extract ~400-500 claims into individual Obsidian notes to build an Argument Dependency Map — a network where every claim is a node with typed edges (depends_on, supports, contradicts, challenged_by).

The original approach (write a script, process all notes in one pass) was rejected because:
- 150+ notes with 400-500 claims won't fit in a single context window
- The work requires semantic understanding per claim (tag assignment, slug creation, edge identification)
- Quality would degrade through context rot and session-length laziness

## Project-Specific Components

### Skill

`~/.hermes/skills/truth-project/claims-extraction/SKILL.md` (to be created — see `notes/claims-architecture.md` for the full specification)

Contains:
- Claim file format (frontmatter schema, body template, tag taxonomy)
- Extraction workflow (step-by-step per note)
- Progress tracking protocol
- Quality check rules
- Edge-adding guidelines

### Progress File

`~/Projects/Personal/Truth/notes/claims-progress.md` (to be created)

Checklist of all 152 chapter notes organized by scholar. Status summary at top. Append-only session log.

### Item Status Metadata

Each chapter note's YAML frontmatter gets:

```yaml
claims_status: "extracted"  # pending | extracted | reviewed | edges_added
claims_extracted_date: 2026-07-23
claims_count: 4
claims_files:
  - "[[claim-asherah-was-yahwistic-symbol]]"
  - "[[claim-kuntillet-ajrud-symbol-not-goddess]]"
  - "[[claim-biblical-evidence-insufficient-for-goddess]]"
  - "[[claim-female-imagery-absorbed-into-yahweh]]"
```

## Batch Sizing

- 3-5 chapter notes per session (15-40 claims)
- ~38 sessions for all 152 notes
- 2-3 sessions/week → 3-4 months for Phase 1 (extraction)
- Additional 2-3 months for Phase 2 (full edge network)

## Key Design Decisions (from the architecture document)

- Claims live in `notes/claims/` as flat files with hierarchical tags
- File naming: `claim-<descriptive-slug>.md` (not GUIDs)
- Claim ID format: `smith-ehg-3.2` (scholar-book-chapter.claim)
- Edges in body text with wikilinks, not structured frontmatter
- Chapter notes retain compact summary + link after extraction
- Primary sources extracted into individual files linked bidirectionally

## Session Workflow (Concrete)

Every extraction session:

1. Load skill + read `notes/claims-progress.md`
2. Pick 3-5 unchecked chapter notes (vary scholars for variety)
3. For each note:
   a. Read the full chapter note
   b. For each `## Claim N:` block, extract to claim file
   c. Determine slug, claim ID, topic/evidence/scholar tags
   d. Write claim file to `notes/claims/`
   e. Add basic edges for intra-scholar relationships
4. Update each chapter note: replace claim blocks with summary + link, add `claims_status` frontmatter
5. Update progress file: check off notes, update summary, append session log
6. Git commit

## See Also

- `~/Projects/Personal/Truth/notes/claims-architecture.md` — full architecture specification
- `~/Projects/Personal/Truth/notes/claims/claim-kuntillet-ajrud-symbol-not-goddess.md` — worked example claim file
- `~/Projects/Personal/Truth/notes/example-smith-ch3-post-extraction.md` — example post-extraction chapter note
