---
name: session-handoff
description: "Craft self-contained prompts for multi-session research workflows — phased synthesis, batch processing, and context-free handoffs."
version: 1.0.0
platforms: [linux, macos]
metadata:
  hermes:
    tags: [workflow, session-management, prompt-engineering]
---

# Session Handoff

Craft self-contained prompts that let a fresh Hermes session pick up where a previous session left off — with zero shared context. Used for multi-phase synthesis, batch processing of large corpora, and any task too large for a single session.

---

## When to Use

- The user asks "make me a prompt for a new session that does X"
- A task needs to be broken into phases (phase 1 → phase 2 → phase 3) because the context window would overflow
- The user wants to delegate batch work (audit all claims, link all sources, extract all notes) across multiple sessions
- You're at the end of a session and the user wants to continue the work in a fresh one

## When NOT to Use

- The task fits in a single session — just do it
- The user is asking YOU to do the work right now — don't deflect to a prompt
- The user explicitly says "just do it in this session"

---

## Prompt Anatomy

Every self-contained session prompt MUST include these elements. Omitting any one forces the next session to guess.

### 1. Project Location
```
Full path to the project (e.g., ~/Projects/Personal/OSKG-YahWeh).
State what the project IS in one sentence.
```

### 2. Current State
```
What exists RIGHT NOW that the next session needs to know:
- Files already created (with paths)
- Phase completions and their outputs
- Counts (how many claims, how many notes, how many sources)
- Any decisions made that affect the next phase
```

### 3. Input Files
```
Exact file paths the next session should READ before starting.
Be specific: "notes/synthesis/phase1-hinge-inventory.md" not "the phase 1 output."
```

### 4. Task Specification
```
What the next session should DO, step by step.
Not "analyze the claims" but "read each claim file, check for X, flag Y, produce Z."
Include the deliverable format and file path for output.
```

### 5. Deliverable Format
```
Where to save the output and what it should look like.
If a table, show the schema. If a document, describe the sections.
```

### 6. Constraints and Pitfalls
```
What NOT to do. Known failure modes from prior sessions.
"If you find yourself compressing chapters, STOP."
"Verify every wikilink resolves before declaring done."
```

### 7. Next Session Hint
```
What the NEXT session after this one should do (so the phase knows its place in the pipeline).
```

---

## Phased Synthesis Pattern

For large analytical tasks (argument dependency maps, systematic comparisons, weighted consensus), break into phases where each phase produces an intermediate artifact consumed by the next:

```
Phase 1: Inventory (what exists?)
  → Output: ranked table of items

Phase 2: Deep analysis (what depends on what?)
  → Input: Phase 1 table
  → Output: detailed maps for top N items

Phase 3: Stress tests (what if X is wrong?)
  → Input: Phase 1 table + Phase 2 maps
  → Output: damage assessments per counter-position

Phase 4: Synthesis (what do we actually know?)
  → Input: Phase 1-3 outputs
  → Output: convergence points + genuine unknowns
```

Each phase prompt references the SPECIFIC file paths of prior phase outputs. No phase prompt says "read what was produced earlier" — it says "read notes/synthesis/phase2-cascade-trees.md."

---

## Batch Processing Pattern

For tasks that process many items (auditing tags, linking sources, extracting claims):

```
Batch size: 15-20 items per session
Each batch: read → check → fix → commit
After each batch: verify nothing degraded
Handoff: "next batch starts at file X, continue through file Y"

The batch prompt MUST include:
- How many items total (so the session knows its place)
- Which item to start from (exact filename or index)
- The checklist for each item
- Commit frequency
```

---

## Common Failure Modes

1. **Prompt says "as discussed" or "as you know."** A fresh session has NO context. Every reference must be explicit.
2. **Prompt says "process the next batch" without saying which batch.** Include the exact filenames.
3. **Prompt references a skill without naming it.** Say "load the claims-extraction skill" not "use the skill."
4. **Prompt omits the project path.** The session can't find the files.
5. **Prompt is too long.** Keep it focused. If you need more than ~500 words, the task is probably too big for one session — phase it.
6. **Prompt does the work instead of asking for it.** Here is the analysis, write it up is wrong. Here is the data, analyze it is right.
7. **Doing the work instead of crafting the prompt.** When the user says give me a prompt for a new session, they want a PROMPT — not a completed task. Do NOT start reading files, extracting claims, or performing the work right now. Just write the prompt. If the user wanted the work done in this session, they would have asked for that.
8. **Monolithic prompt for a moonshot task.** If a task needs 4+ distinct phases with different input/outputs (inventory to analysis to stress tests to synthesis), offer to break it into phased prompts BEFORE the user asks. A monolithic prompt that tries to do everything in one session will fail on context limits or quality degradation. Say this should be pipelined — want me to break it into N phases?

---

## Example: Good vs. Bad

**BAD:**
```
Process the next batch of claims. Fix any issues you find.
```

**GOOD:**
```
Start session in ~/Projects/Personal/OSKG-YahWeh. Phase 1 is complete — 
notes/synthesis/phase1-hinge-inventory.md exists with the top 25 load-bearing 
claims ranked by dependency count. Your task: produce notes/synthesis/phase2-
cascade-trees.md. Read the Phase 1 file. Take the top 5 claims. For each, trace 
the full dependency tree 3 levels deep. Output format: tree diagrams with claim 
IDs, scholar names, and confidence ratings. Do not process claims beyond the 
top 5. Commit when done.
```

---

## README as Project Showcase

When a project produces visual artifacts (canvases, graph screenshots, stress-test diagrams), the README should showcase them. The pattern:

1. **Capture the visual.** Export or screenshot the canvas. Save it as a PNG in the repo root.
2. **Add it to the right section.** Not just dump it at the bottom. Place it near the text that explains what it shows. Graph screenshot near the top for first impression. Stress-test diagram in the methodology section. Lineage map in the sources section.
3. **Write a descriptive caption.** The caption should explain what the viewer is seeing AND why it matters. Not `Figure 1: Knowledge Graph` but `The OSKG knowledge graph: 723 claims with typed edges. Green nodes are claims that survive Schmid's late dating. Red nodes lose their textual foundation.`
4. **Commit the image file with the README update.**

This pattern applies when the user says add this image to the README or the project is being polished for public presentation.
