# Research Vault Structure

A repeatable template for creating an Obsidian-compatible research vault (as a GitHub repo) for systematic investigation of a topic. Used for the Truth Project (faith deconstruction).

## Directory Layout

```
project-name/
├── Home.md                    ← Main Obsidian entry point — project philosophy, approach, current phase
├── README.md                  ← GitHub-facing overview (how to use, structure, license)
├── .gitignore                 ← Obsidian workspace files, OS files
├── sources/
│   ├── Sources Index.md       ← Source quality framework, holdings table, processing status
│   ├── transcripts/
│   │   ├── Transcripts Index.md
│   │   └── source-name.md     ← Cleaned transcript with YAML frontmatter, chapter headings, Key Claim blockquotes
│   ├── books/
│   │   └── Books Index.md     ← Reading queue, recommendations from sources, priority
│   └── papers/
│       └── Papers Index.md    ← Academic papers, topics to find
├── notes/
│   ├── Notes Index.md         ← Analysis conventions (confidence tags, speculation markers)
│   ├── theology/
│   │   └── Theology Index.md  ← Major topics, notes list
│   ├── history/
│   │   └── History Index.md   ← Timeline, archaeological sites, notes list
│   └── questions/
│       └── Questions Index.md ← Open questions as checkboxes, organized by category
└── canvases/
    ├── Canvases Index.md
    └── overview.canvas        ← Visual mind map of project structure
```

## Frontmatter Convention for Source Files

Every source file gets rich YAML frontmatter:

```yaml
---
tags:
  - source/transcript        # source type
  - faith/yahweh             # primary topic
  - faith/monotheism          # secondary topics (use hierarchical namespaces)
  - history/ancient-near-east
source:
  title: "Full Title"
  author/host: "Name"
  guest: "Name"
  url: "https://..."
  date: YYYY-MM-DD
created: YYYY-MM-DD
related:
  - "[[Sources Index]]"
  - "[[Theology Index]]"
status: "to-process"          # to-process | processing | annotated
---
```

## Research Note Structure

For deep-dive synthesis notes, this structure proved effective:

1. **Core question** — what specifically is being investigated
2. **Position framework** — table of major positions with scholars and key claims
3. **Timeline** — chronological development with evidence at each stage
4. **Per-position deep dive** — for each position: what it claims, key scholars (with affiliations), specific arguments, evidence cited, strengths, criticisms
5. **Archaeological/textual evidence** — separate section for physical evidence with both mainstream and critical interpretations
6. **Areas of scholarly agreement** — what everyone agrees on despite the debate
7. **Personal assessment** — where the evidence points, with explicit confidence levels
8. **Open questions** — checkbox list for further research

### Frontmatter for Research Notes

```yaml
---
tags:
  - research/synthesis
  - faith/topic-name
  - scholars/smith
confidence: high|medium|low     # confidence in the synthesis
status: active-research         # active-research | stable | superseded
---
```

### Confidence Levels

- **HIGH**: multiple independent scholarly sources agree; well-established in the field
- **MEDIUM**: general scholarly agreement but significant dissent exists; or based on secondary sources
- **LOW**: speculative, based on limited sources, or needs primary source verification

## Transcript Processing

When cleaning a podcast/video transcript:

1. Strip timestamps
2. Divide into chapters matching the original structure
3. Mark every major scholarly claim with `> **Key claim:**` blockquote
4. Preserve exact quotes on the most important points
5. Link the transcript to all relevant index notes via `related:` frontmatter
6. Extract book/paper recommendations into the appropriate index

## Questions Index Pattern

Organize questions by source and category:

```markdown
## From [[source-name]]

### Category
- [ ] Question as checkbox — actionable, researchable
- [ ] Another question
```

This makes it easy to see what's been answered and what's still open.
