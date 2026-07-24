---
name: obsidian
description: "Read, search, create, and edit notes in the Obsidian vault. Enforces maximal vault writing, good tagging, and branching-tree documentation style for knowledge graph utility."
version: 2.0.0
author: vault-import
platforms: [linux, macos, windows]
env_vars:
  OBSIDIAN_VAULT_PATH: "~/Projects/Personal/obsidian"
metadata:
  hermes:
    tags: [note-taking, obsidian, vault, knowledge-management]
---

# Obsidian Vault

Use this skill for filesystem-first Obsidian vault work: reading notes, listing notes, searching note files, creating notes, appending content, and adding wikilinks.

## Vault path

The vault is at `~/Projects/Personal/obsidian`. Always use this resolved absolute path. File tools do not expand shell variables, so expand `~` to `/Users/littleseneca` when constructing paths.

## Tagging Conventions

Every note must have meaningful YAML frontmatter tags. Use a hierarchical/namespace tag structure:

| Tag | When |
|-----|------|
| `hermes/skill` | Skill definition notes |
| `hermes/memory` | Persistent memory entries mirrored to vault |
| `hermes/session` | Session summaries |
| `avatarfleet/*` | AvatarFleet-specific notes |
| `security/*` | Security/grc content |
| `infra/*` | Cloud infrastructure notes |
| `writing/*` | Writing/generative content |
| `projects/*` | Project-specific notes |

Each note should have 2-5 tags minimum: one domain tag, one type tag, and optionally context tags.

## Frontmatter Template

```yaml
---
tags:
  - domain/tag
  - context/tag
created: YYYY-MM-DD
related:
  - "[[Related Note]]"
  - "[[Another Note]]"
---
```

## Branching Tree Documentation Style

Organize notes in a branching tree structure for knowledge graph utility. Each note occupies one level in a hierarchy and is linked vertically (parent/child) and horizontally (sibling/related).

### Structure Rules

1. **Each note has one parent** — linked via `related` or inline `[[Parent Note]]`
2. **Related notes link laterally** — always add `[[Note Name]]` wikilinks to connected content
3. **Index notes** — every folder has an `Index.md` that lists all child notes with brief descriptions
4. **Depth-first** — drill into specifics, don't flatten everything at the top level
5. **Backlinks** — when creating a note, check what existing notes should link to it and add backlinks

### Example Tree

```
Vault Root/
├── Skills Index.md
├── Memory Index.md
├── Projects/
│   ├── Projects Index.md        (links to sub-indexes)
│   ├── AvatarFleet/
│   │   ├── AvatarFleet Index.md
│   │   ├── AS-#### — description.md
│   │   └── af30-ecr/
│   │       ├── af30-ecr-migration.md
│   │       └── ...
│   ├── Brooks Security/
│   │   ├── Brooks Security Index.md
│   │   └── ...
│   └── Personal/
│       ├── Personal Index.md
│       └── ...
├── Skills/
│   └── ...
└── references/
    └── ...
```

Projects are organized by domain: AvatarFleet (DriverHub/Jira work), Brooks Security (website, blog, client work), and Personal. Each domain has its own index. The top-level Projects Index links to the three sub-indexes.

## Write Maximally to the Vault

When you encounter information that should persist — configuration details, project context, decision records, meeting outcomes, skill imports — write it to the vault immediately. The vault is the durable knowledge store. Prefer creating a new documented note over relying only on ephemeral chat context.

### Artifacts to Mirror

- **Skills** — when importing or creating from vault sources, also maintain the vault copy
- **Key decisions** — record ADR-style notes in `Projects/*/Decisions/`
- **Session outcomes** — if a session produced important context, write it to the vault
- **Technical context** — architecture, configuration, runbooks

## Read a note

Use `read_file` with the resolved absolute path to the note. Prefer this over `cat` because it provides line numbers and pagination.

## List notes

Use `search_files` with `target: "files"` and the resolved vault path. Prefer this over `find` or `ls`.

- To list all markdown notes, use `pattern: "*.md"` under the vault path.
- To list a subfolder, search under that subfolder's absolute path.

## Search

Use `search_files` for both filename and content searches. Prefer this over `grep`, `find`, or `ls`.

- For filenames, use `search_files` with `target: "files"` and a filename `pattern`.
- For note contents, use `search_files` with `target: "content"`, the content regex as `pattern`, and `file_glob: "*.md"` when you want to restrict matches to markdown notes.

## Create a note

Use `write_file` with the resolved absolute path and the full markdown content. Prefer this over shell heredocs or `echo` because it avoids shell quoting issues and returns structured results.

## Append to a note

Prefer a native file-tool workflow when it is not awkward:

- Read the target note with `read_file`.
- Use `patch` for an anchored append when there is stable context, such as adding a section after an existing heading or appending before a known trailing block.
- Use `write_file` when rewriting the whole note is clearer than constructing a fragile patch.

For an anchored append with `patch`, replace the anchor with the anchor plus the new content.

For a simple append with no stable context, `terminal` is acceptable if it is the clearest safe option.

## Targeted edits

Use `patch` for focused note changes when the current content gives you stable context. Prefer this over shell text rewriting.

## Wikilinks

Obsidian links notes with `[[Note Name]]` syntax. When creating notes, use these to link related content.

## Canvas Mind Maps

Obsidian Canvas files (`.canvas`) are JSON documents with `nodes` and `edges`. Build them programmatically when creating study vaults or knowledge maps.

```json
{
  "nodes": [
    {
      "id": "unique-id",
      "type": "text",
      "text": "## Node Title\nMarkdown content",
      "x": 0, "y": 0,
      "width": 320, "height": 200,
      "color": "2",
      "file": "/absolute/path/to/note.md"
    }
  ],
  "edges": [
    {
      "id": "unique-id",
      "fromNode": "source-id",
      "toNode": "target-id",
      "fromSide": "right",
      "toSide": "left",
      "label": "relationship label"
    }
  ]
}
```

**Color scheme conventions:**
| Color | Use |
|-------|-----|
| `"1"` (red) | Root/center node |
| `"2"` (orange) | Major branches/sections |
| `"3"` (yellow) | Chapter/content nodes |
| `"4"` (green) | Concept/key-takeaway nodes |
| `"5"` (cyan) | Reference/exam nodes |
| `"6"` (purple) | Cross-reference/auxiliary nodes |

Set `file` on nodes pointing to `.md` files for click-through navigation in Obsidian.

For programmatic Canvas generation from structured synthesis data (tiered layouts, spacing calculation, edge design, Python validation), see `references/canvas-generation-workflow.md`.

### Programmatic Canvas Generation

For canvases with more than a handful of nodes (especially radial/concentric layouts), generate the JSON programmatically via `execute_code` + Python rather than hand-coding positions. Use `math.cos`/`math.sin` to place nodes on concentric rings:

```python
angle = math.radians(i * (360 / num_nodes) - 90)  # start from top
x = radius * math.cos(angle) - width / 2
y = radius * math.sin(angle) - height / 2
```

Write with `json.dump(canvas, f, indent="\t")` — Obsidian's native format uses tabs.

For the full pattern including edge routing, multi-level cascade layouts, and wikilink conventions, see `references/canvas-programmatic-generation.md`.

## Study Material Conversion Pipeline

For converting EPUBs/PDFs into structured Obsidian study vaults (textbook → tagged notes → exam questions → Canvas mind map), see `references/epub-to-obsidian-pipeline.md`. This covers:

For creating a research project vault (GitHub repo + Obsidian-compatible structure for systematic investigation), see `references/research-vault-structure.md`. This covers directory layout, source processing, research note format, and questions index patterns.

The pipeline reference covers:

- EPUB XHTML extraction with proper `<header>` handling
- LLM restructuring into tagged, wikilinked markdown
- Parallel chapter processing via `delegate_task`
- Exam question extraction from chapter text and external PDFs
- Programmatic Canvas mind map generation

## Common Pitfalls

### Pitfall 1: Skipping session recording (MOST COMMON)

**Agents routinely forget to record sessions in the vault even though the rules say to.** The skill describes *how* to do it, but there's no hard stop — so the agent finishes the code work and moves on without writing the vault notes.

**Fix:** Load the companion skill `obsidian-session-record` at the **start** of every session, not at the end. It has a non-negotiable checklist that must be completed before the session concludes. The `hermes/session` memory entry also flags this as a hard rule.

If you find yourself finishing code work and the vault is empty, you skipped the skill. Stop, load it, and record the session before responding to the user.

### Pitfall 2: Forgetting hierarchical backlinking

Every note must link to its **immediate parent index** via `related:` frontmatter — NOT directly to Memory Index (unless that IS the parent). Without this, the graph becomes a flat star instead of a traversable tree. The hierarchy is:

| Note type | Parent index |\n|---|---|\n| Session note | `[[../Sessions Index]]` |\n| Artifact note | `[[../Artifacts Index]]` |\n| Project note (in domain subdir) | `[[<Domain> Index]]` (sibling index) |\n| Domain project index | `[[../Projects Index]]` |\n| Skill note | `[[../<category> Index]]` |\n| Documentation note | `[[Documentation Index]]` |\n\nOnly domain project indexes (AvatarFleet Index, Brooks Security Index, Personal Index) link to `[[../Projects Index]]`. Individual project notes in those directories link to their sibling domain index.

### Pitfall 7: Canvas node overlap from cramped layout

The most common Canvas failure: nodes too small for their text (cut-off content) and rows too close together (cards stacked on top of each other). The symptom is illegible cards and edges routed through card bodies. Full fix with sizing formulas, validation script, and OSKG-tested dimensions is in `references/canvas-generation-workflow.md` under "Node overlap from insufficient spacing."

Quick rules:
- Estimate height: ~20px per line of markdown text + 80px padding
- Vertical rows: ensure `row_N.bottom + 40px ≤ row_{N+1}.top`
- Horizontal same-row: center gap ≥ node width + 80px
- Always run a bounding-box overlap check before declaring done

### Pitfall 8: EPUB `header` wraps content headings

When extracting EPUB chapters with an HTML parser, do NOT put `'header'` in the skip list (alongside `script`, `style`, `nav`). Many EPUBs — especially Wiley/Sybex textbooks — use `<header>` as a semantic wrapper around section headings: `<header><h2>The Types of AI</h2></header>`. Treating `header` as skippable silently drops all heading text. See `references/epub-to-obsidian-pipeline.md` for the full extraction pattern.

### Pitfall 4: PDF extraction requires venv Python

PyMuPDF (`fitz`) is installed in the Hermes venv at `~/.hermes/venv/bin/python3` (Python 3.14), NOT on the default `python3` (3.11). Always prefix PDF extraction commands with the venv path:
```bash
~/.hermes/venv/bin/python3 -c "import fitz; ..."
```
Do NOT `pip install pymupdf` on the default Python — it will install to the wrong version.

### Pitfall 6: Canvas node x,y is top-left corner, not center

When positioning a Canvas node to sit at the center of a ring or the origin, remember that `x` and `y` are the **top-left corner** of the node, not its visual center. For a centered root node:

```python
# WRONG — node's top-left is at origin, center is off by (w/2, h/2)
{"id": "root", "x": 0, "y": 0, "width": 360, "height": 260}

# RIGHT — node's visual center is at origin
{"id": "root", "x": -180, "y": -130, "width": 360, "height": 260}
```

Same applies to ring positioning: subtract `width/2` from x and `height/2` from y after computing the center-point position.

### Pitfall 5: EPUB extraction requires ebooklib + html2text

EPUB extraction uses `ebooklib` and `html2text`, both installed in the Hermes venv:
```bash
~/.hermes/venv/bin/pip install ebooklib html2text
```
Then iterate `book.get_items()`, filter `item.get_type() == 9` for XHTML documents, and convert to plaintext with `html2text.HTML2Text()`.

## Truth Project Vault Conventions

The OSKG-YahWeh project (`~/Projects/Personal/OSKG-YahWeh/`) has its own directory structure and wikilink conventions distinct from the main Obsidian vault. See `references/truth-project-vault-conventions.md` for the full reference: directory layout, wikilink formats between notes/theology/ → sources/primary-sources/, source file frontmatter conventions, claim file structure, and the source-to-note linking workflow.

## OSKG-YahWeh Synthesis Writing

When writing capstone or synthesis documents from the OSKG-YahWeh claims knowledge graph, load the `evidence-synthesis-writing` skill. It encodes the conventions established in the 2026-07-24 capstone rewrite: evidence-forward voice (no first-person, no theological conclusions), dense claim wikilinks (100+ for a full capstone), super tag-rich frontmatter (15+ tags), and the 8-part analytical structure. The key rule: report what the graph reports — do not adjudicate what the evidence means for belief.

## Project Rename: Vault + GitHub + Directory

When renaming a project that lives in its own directory AND has mirrored notes in the Obsidian vault, see `references/project-rename-workflow.md` for the full 10-step sequence: GitHub rename, directory rename, batch sed across all .md files in both project and vault, Home.md rewrite, index updates, and verification.

## Truth Project Graph Analysis

When building cascade trees, dependency maps, or collapse-radius analyses from the claim knowledge graph, the graph is a DAG (many claims have multiple parents). See `references/dag-dependency-traversal.md` for the critical BFS-vs-DFS pitfall: DFS buries multi-parent nodes at their deepest encountered level, producing incorrect dependency counts. Always use BFS for cascade trees.

## Reading Monographs into Obsidian

For the workflow that converts scholarly monographs into structured, wikilinked Obsidian notes — chunking strategy, note structure, frontmatter conventions, and link density — see `references/book-to-notes-workflow.md`.

## Primary Source Extraction from Internet Archive

For extracting ancient primary source texts from Internet Archive scanned books into formatted Obsidian source notes — IA advancedsearch API, OCR text download, grep extraction, and compilation — see `references/primary-source-extraction.md`. This is the pipeline the Truth Project uses to build `sources/primary-sources/`.
