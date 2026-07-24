---
name: multi-session-batch-processing
description: "Process many items (files, documents, claims) across multiple sessions with durable progress tracking. Skill as schema, progress file as state, batch-per-session as rhythm."
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [strategy, workflow, batch-processing, progress-tracking, multi-session]
---

# Multi-Session Batch Processing

When a task involves processing 50+ items (files, documents, claims, records) and won't fit in a single context window, use this pattern. The core insight: **do NOT try to process everything in one session or one script.** Instead, use a skill as the schema, a progress file as durable state, and a batch-per-session rhythm.

## Trigger

Any task where:
- There are 50+ items to process (files, notes, records, claims)
- Each item requires meaningful LLM work (reading, reasoning, writing)
- The work won't fit in a single session / context window
- Progress must survive across sessions
- The human wants to stay involved at checkpoints

## The Pattern

Three components, analogous to Karpathy's LLM Wiki architecture:

1. **Skill (the schema)** — loaded at every session start. Contains the processing instructions, format rules, quality checks, and progress protocol. This is what keeps the agent consistent across sessions.

2. **Progress file (the state)** — a single markdown file at the project root that tracks what's been done and what remains. Checklist format, organized by category. Append-only session log. Git-committed for durability.

3. **Batch-per-session rhythm (the workflow)** — every session: load skill → read progress file → process 3-5 items → update progress → commit. Next session picks up where the last left off.

## Research Foundations

**Karpathy's LLM Wiki Pattern (April 2026):** Three-layer architecture — raw sources (immutable), wiki (LLM-maintained), schema (CLAUDE.md loaded every session). Progress tracked via `log.md` and `index.md`. Key quote: "ingest one source at a time and stay involved. Read the summaries, check updates, guide emphasis."

**Agent Memory Patterns (UnderstandingData, 2026):** Three memory tiers — Session (ephemeral), File-Based (TASKS.md, progress.txt, ERRORS.md), Event-Sourced (full history). "Externalize agent state to durable storage." Git as the durability layer. RALPH Loop: spawn fresh agent, load state from files, execute task, persist back.

**Batched LLM Queries (Kavale, 2025):** ID-based tracking, configurable batch size, validation loop (check for dropped items, retry), incremental deduplication against previously processed results.

## Why This Works Where a Single Session Wouldn't

- Each session starts fresh — no context rot from accumulated conversation
- The skill provides consistent instructions — no drift across sessions
- The progress file ensures continuity — no "what did I do last time?"
- Git commits create a durable trail — recoverable from any state
- The human stays involved at session boundaries — quality control is built in

## Workflow Template

### Before First Session: Setup

1. Create the skill at `~/.hermes/skills/<category>/<skill-name>/SKILL.md`
2. Create the progress file at the project root
3. Populate the progress file with ALL items to process, organized by category
4. Git commit the progress file

### Every Session

**Start (3-5 min):**
1. Load the skill
2. Read the progress file to determine the next batch
3. Identify 3-5 unprocessed items (vary categories for variety)

**Process (per item, 10-30 min):**
4. Read the item
5. Do the work (extract, transform, create artifacts)
6. Write output files
7. Mark the item as processed (both in the item's metadata AND in the progress file)

**Close (10 min):**
8. Update the progress file: check off items, update summary, append session log entry
9. **Quality review** — before committing, run the QA checklist from `references/truth-claims-qa.md`: verify frontmatter, Evidence sections, wikilinks, chapter note updates, and content degradation on the batch just processed. This catches incomplete extractions and broken links before they compound.
10. Git commit with descriptive message
11. The next session picks up where this one left off

### Progress File Template

```markdown
---
tags:
  - type/progress
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Project Name> Progress

## Status Summary

- **Total items:** N
- **Processed:** 0
- **Remaining:** N
- **Last session:** (none)

## By Category

### Category A (N items)
- [ ] Item 1
- [ ] Item 2
...

### Category B (N items)
...

## Session Log

<!-- Append-only. Format:
### YYYY-MM-DD — Session N
- Items processed: 4 (Item 1, Item 2, Item 3, Item 4)
- Artifacts created: 18
- Commits: 3
- Items remaining: N
-->
```

### Item Status Tracking

Each processed item gets a status field in its own metadata:

```yaml
<workflow>_status: "processed"  # pending | processed | reviewed
<workflow>_date: YYYY-MM-DD
```

This provides two independent sources of truth: the progress file's checklist AND the item's own metadata. A lint operation can scan for discrepancies.

## Batch Size Guidelines

- **3-5 items per session** is the sweet spot. Small enough to fit in a context window with the skill + items + generated artifacts. Large enough to build momentum.
- **Never batch more than 8 items** in one session — context rot and quality degradation set in.
- **If an item is unusually complex** (many sub-artifacts, dense content), count it as 2 items for batch sizing.

## Progress Integrity Checks

Add a `/lint` command to the skill that:
1. Scans all items for `<workflow>_status` metadata
2. Compares against the progress file's checklist
3. Reports discrepancies: items marked "processed" but unchecked, or vice versa
4. Reports orphans: output files without corresponding progress entries

## Pitfalls

### The "one script to rule them all" reflex

The instinct to write a script that processes everything at once is strong. Resist it. Scripts work for mechanical transformations (find-and-replace, file renaming, format conversion). They don't work for tasks requiring semantic understanding per item. The skill + progress file + batch rhythm is the right pattern for LLM-driven processing.

### Batch size creep

"These are short items, I can do 10." You can't. Session-length laziness sets in around item 6-7. Quality degrades. Stick to 3-5.

### Progress file drift

The progress file and item metadata MUST agree. If you update one without the other, you create ambiguity about what's actually been processed. Always update both atomically.

### Forgetting the session log entry

The session log is what makes multi-session work possible. Without it, the next session has no context about what was done, what was hard, what was left incomplete. Always append a log entry before ending the session.

### Skipping quality review before commit

A batch can have perfect-looking claim files while the chapter notes were never updated, or 3 of 7 claims were silently skipped. Running `references/truth-claims-qa.md` catches these failures before they compound. Incomplete batches discovered two sessions later are far harder to fix. Quality review adds 5 minutes; fixing stale partial extractions costs 30.

### Starting without reading the progress file

The first thing every session does is read the progress file. If you skip this, you'll process items that have already been done or miss items that are partially complete. Load skill → read progress → then act.

## When NOT to Use

- **Fewer than 20 items.** A single session can handle this. Don't add process overhead.
- **Purely mechanical transformations.** Use a script for find-and-replace, format conversion, or file renaming.
- **Items that must be processed as a batch for correctness.** If items 1-50 must be processed together (e.g., because they share state or ordering constraints), this pattern doesn't apply. But verify this assumption: most "must be batched" constraints can be refactored into independent units with shared reference data.
- **Real-time or latency-sensitive work.** This pattern is for durable, multi-session work, not for things that need to complete in minutes.

## References

- `references/truth-claims-extraction.md` — Concrete reference implementation: extracting 400-500 scholarly claims from 152 chapter notes in the Truth project (Yahweh origins research). Shows the full project-specific setup, batch sizing, and session workflow.
- `references/truth-claims-qa.md` — Quality review procedure for claims extraction batches. Systematic checklist for verifying claim files, chapter notes, wikilinks, and content quality. Includes output format, verification techniques, and common failure modes. Run after every extraction session before committing.
