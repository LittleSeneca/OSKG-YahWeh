---
tags:
  - type/architecture
  - oskg-yahweh
  - methodology
created: 2026-07-23
updated: 2026-07-23
status: implemented
related:
  - "[[Theology Index]]"
  - "[[meta-analysis-scholars]]"
  - "[[scholarly-directory-yahweh-origins]]"
  - "[[claims-progress]]"
implementation:
  skill: "~/.hermes/skills/oskg-yahweh/claims-extraction/SKILL.md"
  progress_file: "notes/claims-progress.md"
  example_claim: "notes/claims/claim-kuntillet-ajrud-symbol-not-goddess.md"
  example_note: "notes/example-smith-ch3-post-extraction.md"
---

# Claims Architecture: Argument Dependency Map

## The Problem

The Truth project has ~150+ chapter notes across 13+ scholars, each containing 4-10 explicitly formatted claims with evidence, confidence ratings, stakes analysis, and scholarly disagreement. These claims are currently buried inside chapter notes. There is no way to:

- Query "show me every claim about Asherah"
- Trace "what claims depend on the Soleb inscription?"
- Ask "what claims does Schmid's late dating threaten?"
- See a network of how claims support, contradict, and depend on each other

The Obsidian graph view connects **notes** — but one note can contain 10 claims about different topics. The edges are too coarse. We need claims to be first-class citizens.

### The Vision

Open Obsidian's graph view, filter to `type:claim` + `topic:asherah`, and see a **network of every claim about Asherah** — who made it, what evidence it uses, what claims it depends on, and what claims challenge it.

---

## Audit Results (July 2026)

### Claims per Note

Sampled six notes across six scholars:

| Note | Scholar | Explicit Claims |
|------|---------|-----------------|
| Smith Ch 3 — Yahweh and Asherah | Mark S. Smith | 4 + assessment table |
| Römer Ch 9 — Yhwh and His Asherah | Thomas Römer | 4 + assessment table |
| Dever Ch V — Archaeological Evidence | William Dever | 8 categories (implicit claims with confidence ratings) |
| Tigay Ch I — Onomastic Evidence | Jeffrey Tigay | 2 major + sub-analysis |
| Lewis Ch 6 — Origin of Yahweh | Theodore Lewis | 6 + assessment table |
| Kaufmann Ch I — The Basic Problem | Yehezkel Kaufmann | 10 + assessment table |

**Average: 5-6 explicit claims per chapter note.** Projected total: **350-450 claims** across the project.

### Claim Structure

Every claim follows a consistent pattern in the markdown:

```
## Claim N: <one-sentence summary>

**Author's claim:** Paragraph describing the claim with direct quotes.

**Evidence presented:** Bullet points, tables, narrative evidence.

**Confidence:** HIGH / MEDIUM / LOW / VERY HIGH / MEDIUM-HIGH / LOW-MEDIUM — with one-sentence justification.

**What's at stake:** Why this matters for faith or scholarship.

**Who disagrees:** Named scholars or schools with specific counter-arguments.

**Alternative reading:** The counter-position, presented fairly.

**My assessment:** Graham's own evaluation — often the most valuable section.
```

Some claims add variant sections (e.g., `**Additional negative evidence:**`, `**The Baal Names Problem**`).

### Metadata Currently on Each Claim

| Metadata | Location | Structured? |
|----------|----------|-------------|
| Claim number | H2 header | Yes (`## Claim N:`) |
| Claim title | H2 header | Yes |
| Source scholar | Note title + frontmatter | Yes (note-level, not claim-level) |
| Source book/chapter | Note title | Yes |
| Confidence | Bold text paragraph | Semi (prose, not YAML) |
| Evidence type | Implicit in evidence section | No |
| Stakes | Bold text paragraph | No |
| Disagreement | Bold text paragraph | Semi (scholar names, sometimes wikilinks) |
| Alternative | Bold text paragraph | No |
| Assessment | Bold text paragraph | No |

### Cross-References — What Exists Now

**Note-level (YAML `related:`):**
- Wikilinks to other chapter notes (e.g., `[[Romer — Chapter 9 — Yhwh and His Asherah]]`)
- Wikilinks to meta-notes (e.g., `[[scholarly-directory-yahweh-origins]]`)

**Claim-level (inline in body):**
- Scholar names mentioned in "Who disagrees" (sometimes wikilinked, usually not)
- Primary sources mentioned by name (e.g., "Kuntillet Ajrud," "Khirbet el-Qom," "Deut 32:8-9")
- No wikilinks to **specific claims** from other notes — only to other chapter notes

**Primary source note:** `sources/primary-sources/key-inscriptions.md` exists as a single file covering 5 inscriptions (Kuntillet Ajrud, Khirbet el-Qom, Deut 32:8-9 + 4QDeut, Soleb Shasu, Merneptah Stele). Scholar-specific notes don't always wikilink to it.

### What Would Be Lost If Claims Were Extracted

1. **Narrative flow** — claims build on each other within a chapter; the sequence of argument matters
2. **Cross-cutting assessment tables** — the chapter-level tables that compare claims side-by-side
3. **Cumulative evaluation** — e.g., Römer's "My assessment after three books: Smith says symbol; Römer says goddess; Dever says goddess with 3,000+ figurines..."
4. **The reader's ability to read one chapter as a coherent document** — if every claim is extracted, the chapter note becomes a skeleton

---

## Architecture Design

### Folder Structure

```
notes/
├── claims/                          # All claim files — flat, no subfolders
│   ├── claim-kuntillet-ajrud-symbol-not-goddess.md
│   ├── claim-asherah-was-goddess-consort.md
│   ├── claim-biblical-names-89-percent-yahwistic.md
│   └── ...                          # 350-450 files
├── sources/                         # Primary source nodes
│   ├── source-kuntillet-ajrud.md    # Extracted from key-inscriptions.md
│   ├── source-khirbet-el-qom.md
│   ├── source-deut-32-8-9.md
│   ├── source-soleb-shasu.md
│   └── source-merneptah-stele.md
├── theology/                        # Existing chapter notes — updated to link to claims
│   ├── Smith Chapter 3 — Yahweh and Asherah.md
│   └── ...
├── Theology Index.md
├── scholarly-directory-yahweh-origins.md
├── meta-analysis-scholars.md
└── claims-architecture.md           # This document
```

**Why flat?** In Obsidian, folders are secondary to tags. A flat `claims/` folder with consistent tagging lets the graph view and search handle discovery. Subfolders create structural debt (what folder does a claim about Asherah AND monotheism AND Kuntillet Ajrud go in?).

### File Naming Convention

`claim-<descriptive-slug>.md`

The slug is a short, human-readable key that identifies the claim at a glance. This is important because Obsidian's graph view displays filenames. Examples:

- `claim-kuntillet-ajrud-symbol-not-goddess.md`
- `claim-yahweh-had-consort-asherah.md`
- `claim-3000-figurines-prove-goddess-worship.md`
- `claim-biblical-names-overwhelmingly-yahwistic.md`
- `claim-deut-32-8-9-elyon-divided-nations.md`
- `claim-shasu-texts-earliest-yahweh.md`
- `claim-bible-genuinely-ignorant-of-paganism.md`

**Not GUIDs.** GUIDs make the filesystem unreadable and defeat the purpose of Obsidian's graph view (which shows filenames as node labels). The slug must be unique but human-readable.

**Collision risk:** Low. With ~400 claims, descriptive slugs in this domain are naturally distinct. If two claims would get the same slug, they're probably the same claim and should be examined.

### Claim File Format

#### Frontmatter

```yaml
---
tags:
  - type/claim
  - topic/<primary-topic>
  - topic/<secondary-topic>
  - evidence/<evidence-type>
  - scholar/<scholar-slug>
  - source/<book-slug>
  - oskg-yahweh
claim_id: "<scholar>-<book-abbrev>-<ch>.<num>"
statement: "<one sentence — the claim's assertion>"
confidence: "<rating>"
confidence_rationale: "<one sentence on why this rating>"
claim_type: "<textual|archaeological|philological|theological>"
source_note: "[[<chapter note>]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

```

#### Tag Taxonomy

**Required:**
- `type/claim` — on every claim file (non-negotiable; enables graph view filtering)

**Topic tags** (at least one, typically 2-4):
- `topic/yahweh-origin`
- `topic/asherah`
- `topic/monotheism`
- `topic/polytheism`
- `topic/divine-council`
- `topic/aniconism`
- `topic/el`
- `topic/baal`
- `topic/deuteronomist`
- `topic/josiah-reform`
- `topic/exile`
- `topic/onomastics`
- `topic/folk-religion`
- `topic/midianite-hypothesis`
- `topic/kenite-hypothesis`
- ... (extensible; new topics added as needed)

**Evidence tags:**
- `evidence/inscriptional`
- `evidence/archaeological`
- `evidence/biblical-text`
- `evidence/grammatical`
- `evidence/onomastic`
- `evidence/iconographic`
- `evidence/comparative-ane`
- `evidence/ugaritic`

**Source tags:**
- `scholar/mark-smith`
- `scholar/thomas-romer`
- `scholar/william-dever`
- `scholar/jeffrey-tigay`
- `scholar/theodore-lewis`
- `scholar/yehezkel-kaufmann`
- `scholar/konrad-schmid`
- `scholar/john-day`
- `scholar/frank-moore-cross`
- `scholar/michael-heiser`
- `scholar/francesca-stavrakopoulou`
- `scholar/benjamin-sommer`
- `scholar/daniel-fleming`
- `scholar/othmar-keel`
- `scholar/rainer-albertz`
- ... (one per scholar)

- `source/smith-early-history-of-god`
- `source/smith-origins-biblical-monotheism`
- `source/romer-invention-of-god`
- `source/dever-did-god-have-a-wife`
- `source/tigay-no-other-gods`
- `source/lewis-origin-character-of-god`
- `source/kaufmann-religion-of-israel`
- ... (one per book)

#### Claim ID Format

`<scholar-initials>-<book-abbreviation>-<chapter>.<claim-number>`

| Claim ID | Decodes to |
|----------|-----------|
| `smith-ehg-3.2` | Mark S. Smith, *Early History of God*, Ch 3, Claim 2 |
| `romer-inv-9.1` | Thomas Römer, *Invention of God*, Ch 9, Claim 1 |
| `dever-dghw-5.4` | William Dever, *Did God Have a Wife?*, Ch 5, Claim 4 |
| `tigay-nog-1.1` | Jeffrey Tigay, *No Other Gods*, Ch 1, Claim 1 |
| `lewis-ocg-6.4` | Theodore Lewis, *Origin and Character of God*, Ch 6, Claim 4 |
| `kaufmann-ri-1.3` | Yehezkel Kaufmann, *Religion of Israel*, Ch 1, Claim 3 |
| `smith-obm-7.2` | Mark S. Smith, *Origins of Biblical Monotheism*, Ch 7, Claim 2 |

**Why claim IDs?** They provide a stable, human-readable reference that works in conversation ("check smith-ehg-3.2"), in Dataview queries, and in edge descriptions. They also handle the case where Smith has claims in two different books about the same topic — `smith-ehg-3.2` and `smith-obm-7.4` are unambiguously different claims.

#### Body Format

```markdown
# <claim_id>: <statement>

**Source:** [[<chapter note>]] — <Scholar>, *<Book>* (<Year>), <Chapter>

## The Claim

<Full statement of the claim with direct quotes.>

## Evidence

<Structured evidence — bullet points, tables, narrative. Copied from the chapter note's evidence section.>

## Confidence

**Rating:** <HIGH|MEDIUM|LOW|etc.>

**Rationale:** <One sentence on why.>

## Stakes

<Why this claim matters. What changes if true? What depends on it?>

## Disagreement

**Who disagrees:** <Named scholars with brief summaries.>

**Alternative reading:** <The counter-position.>

## Edges

**Depends on:**
- [[claim-<slug>]] — <how this claim relies on it>

**Supports:**
- [[claim-<slug>]] — <how this claim reinforces it>

**Contradicts:**
- [[claim-<slug>]] — <how these claims conflict>

**Challenged by:**
- [[claim-<slug>]] — <what evidence or argument threatens it>

**Primary sources:**
- [[source-kuntillet-ajrud]]
- [[source-deut-32-8-9]]

## Assessment

<Graham's own evaluation, copied from the chapter note.>
```

The **Edges** section is the critical addition. This is what turns isolated claim files into a dependency network. Each edge is a wikilink (creating a graph edge in Obsidian) with a human-readable description of the relationship. There are five edge types:

| Edge Type | Meaning | Example |
|-----------|---------|---------|
| **Depends on** | Claim A requires Claim B to be true; if B falls, A falls | Smith's symbol reading of Kuntillet Ajrud depends on the claim that divine names don't take pronominal suffixes in Hebrew |
| **Supports** | Claim A provides evidence or reasoning that strengthens Claim B | Dever's 3,000+ figurines support the claim that Asherah was actively worshipped |
| **Contradicts** | Claim A and Claim B cannot both be true | Smith: "Kuntillet Ajrud = symbol" contradicts Römer: "Kuntillet Ajrud = goddess consort" |
| **Challenged by** | Claim A is weakened by evidence or argument in Claim B | Tigay's onomastic evidence is challenged by the Ugarit parallel (few Asherah names despite widespread cult) |
| **Primary sources** | The claim relies on specific inscriptions, texts, or artifacts | Claims about Kuntillet Ajrud link to the primary source note for the inscriptions |

**Relationship to existing chapter notes:**

Each claim in a chapter note gets replaced with a compact summary block that links to the claim file:

```markdown
## Claim 2: The Kuntillet Ajrud inscriptions refer to the asherah symbol, not the goddess
→ [[claim-kuntillet-ajrud-symbol-not-goddess]] | **smith-ehg-3.2** | Confidence: MEDIUM
  The grammatical argument (pronominal suffix on divine name) is strong but not decisive.
  Contradicted by: [[claim-kuntillet-ajrud-proves-consort]] (Römer), [[claim-asherah-was-goddess]] (Dever)
```

This keeps the chapter note readable as a standalone document while making every claim one click away. The chapter-level cross-cutting assessment table stays intact.

### Handling Smith's Two Books

Mark S. Smith wrote *The Early History of God* (1990, rev. 2002) and *The Origins of Biblical Monotheism* (2001). Some claims appear in both. The claim ID system distinguishes them:

- `smith-ehg-3.2` — Early History of God, Chapter 3, Claim 2
- `smith-obm-7.4` — Origins of Biblical Monotheism, Chapter 7, Claim 4

If Smith's position evolved between books, these are **different claims** with a `refined_in` or `superseded_by` edge connecting them. If his position is identical, the later claim file can reference the earlier one:

```markdown
## Edges

**Refines:** [[claim-kuntillet-ajrud-symbol-not-goddess]] (smith-ehg-3.2) — Smith's 2001 treatment adds the McCarter hypostasis theory not present in 1990.
```

### Primary Source Nodes

The existing `sources/primary-sources/key-inscriptions.md` gets split into individual files:

```
notes/sources/
├── source-kuntillet-ajrud.md
├── source-khirbet-el-qom.md
├── source-deut-32-8-9.md
├── source-soleb-shasu.md
├── source-merneptah-stele.md
└── Sources Index.md
```

Each source note gets:

```yaml
---
tags:
  - type/primary-source
  - oskg-yahweh
source_id: "<slug>"
source_type: "<inscription|biblical-text|stele|papyrus>"
date: "<approximate date>"
location: "<discovery location>"
---
```

Claims link to these in their Edges section, and primary source notes link back to all claims that use them. This creates a bidirectional network: claims → sources → claims.

### Scholar and Book Nodes

The meta-notes (`scholarly-directory-yahweh-origins.md`, `meta-analysis-scholars.md`) already serve as scholar nodes. Each claim links to its source chapter note, which links to these meta-notes. No new scholar nodes are needed.

---

## Extraction Process: Multi-Session Batch Workflow

The original plan (one script, one pass, then manual edges) assumed this could be done in a single context window. It can't. 150+ chapter notes yielding 400-500 claims won't survive one Hermes session, much less one context window. The research is clear: we need a **skill-driven, multi-session batch workflow with file-based progress tracking**.

This section replaces the original "Extraction Process" section entirely, incorporating patterns from Karpathy's LLM Wiki Stack, agent memory checkpoint/resume patterns, and batched LLM query strategies.

### Research Foundations

Three patterns from the research directly inform this design:

**1. Karpathy's LLM Wiki Pattern (April 2026):** Three-layer architecture — raw sources (immutable), wiki (LLM-maintained), schema (CLAUDE.md loaded at every session). The ingest workflow touches 5-15 files per source. Progress is tracked via `log.md` (append-only activity log) and `index.md` (master catalog). The human stays involved — "ingest one source at a time and stay involved. Read the summaries, check updates, guide emphasis."

**2. Agent Memory Patterns (UnderstandingData, 2026):** Three memory tiers — Session (ephemeral), File-Based (survives sessions via TASKS.md, progress.txt, ERRORS.md), Event-Sourced (full history). "Externalize agent state to durable storage." Git is the durability layer. The RALPH Loop pattern: spawn fresh agent, load state from files, execute task, persist state back.

**3. Batched LLM Queries (Kavale, 2025):** ID-based tracking, batching strategy with configurable size, validation loop (check for dropped/missed items, retry), incremental processing with deduplication against previously processed results.

Translated to our problem: we don't need a script that processes everything at once. We need a **skill** (the schema), a **progress file** (the state), and a **batch-per-session** rhythm (the workflow). Every session is self-contained: load the skill, read the progress file, process 3-5 notes, update progress, commit.

### The Claims Extraction Skill

Create a skill at `~/.hermes/skills/oskg-yahweh/claims-extraction/SKILL.md` that gets loaded at the start of every extraction session. This is the equivalent of Karpathy's CLAUDE.md — the operational schema that teaches the agent what to do, what conventions to follow, and how to track progress.

**What the skill contains:**

1. **The claim file format** — frontmatter schema, body template, tag taxonomy (from this architecture document)
2. **The extraction workflow** — step-by-step instructions for processing a batch of chapter notes
3. **The progress tracking protocol** — how to read and update the progress file
4. **Quality check rules** — what to verify before marking a note as done
5. **Edge-adding guidelines** — when and how to add claim-to-claim edges

### The Progress File

Create `notes/claims-progress.md` at the Truth project root. This is the single source of truth for what's been done and what remains:

```markdown
---
tags:
  - type/progress
  - oskg-yahweh
created: 2026-07-23
updated: 2026-07-23
---

# Claims Extraction Progress

## Status Summary

- **Total chapter notes:** 152
- **Notes with claims extracted:** 0
- **Total claims extracted:** 0
- **Notes with edges added:** 0
- **Last session:** (none)

## By Scholar

### Smith, Early History of God (10 notes)
- [ ] Smith Chapter 0 — Foreword and Preface
- [ ] Smith Chapter 0 — Introduction
- [ ] Smith Chapter 1 — Deities in the Period of the Judges
- [ ] Smith Chapter 2 — Yahweh and Baal
- [ ] Smith Chapter 3 — Yahweh and Asherah
- [ ] Smith Chapter 4 — Yahweh and the Sun
- [ ] Smith Chapters 5-7 — Cult, Monotheism, Portraits

### Smith, Origins of Biblical Monotheism (11 notes)
- [ ] Smith Origins — Introduction
- [ ] Smith Origins — Ch1 — Anthropomorphic Deities and Divine Monsters
- [ ] Smith Origins — Ch2 — The Divine Council
...

### Römer, The Invention of God (14 notes)
...

## Session Log

<!-- Append-only. Each session adds one entry. Format:
### YYYY-MM-DD — Session N
- Notes processed: 4 (Smith Ch 3, Römer Ch 9, Dever Ch V, Tigay Ch I)
- Claims extracted: 18
- Edges added: 12
- Commits: 3
- Notes remaining: 148
-->
```

This file serves three functions:
- **At session start:** the agent reads it to know exactly what to work on next
- **During session:** the agent checks off items as they complete
- **Between sessions:** Graham can see progress at a glance, and the file is git-committed for durability

### Chapter Note Status Tracking

Each chapter note's YAML frontmatter gets a `claims_status` field:

```yaml
claims_status: "extracted"  # Values: pending | extracted | reviewed | edges_added
claims_extracted_date: 2026-07-23
claims_count: 4
claims_files:
  - "[[claim-asherah-was-yahwistic-symbol]]"
  - "[[claim-kuntillet-ajrud-symbol-not-goddess]]"
  - "[[claim-biblical-evidence-insufficient-for-goddess]]"
  - "[[claim-female-imagery-absorbed-into-yahweh]]"
```

This is queryable with Dataview:
```dataview
TABLE claims_status, claims_count, claims_extracted_date
FROM "notes/theology"
WHERE claims_status = "extracted"
SORT claims_extracted_date DESC
```

And in the Obsidian graph, notes with `claims_status: "pending"` can be visually distinguished from those with `claims_status: "extracted"` using graph view group colors.

### Session Workflow

Every extraction session follows this pattern:

**1. Session start (3-5 minutes):**
- Load the `claims-extraction` skill
- Read `notes/claims-progress.md` to determine the next batch
- Identify 3-5 unprocessed chapter notes (from different scholars for variety)

**2. Batch processing (per note, 15-30 minutes):**
- Read the chapter note
- For each `## Claim N:` block:
  - Extract the claim text and all structured sections
  - Assign a descriptive slug
  - Generate the claim ID
  - Determine topic tags, evidence tags, scholar/source tags
  - Write the claim file to `notes/claims/`
  - Add basic edges if related claims from this session are obvious
- Add placeholders in the Edges section for cross-scholar connections

**3. Update chapter note (5 minutes):**
- Replace each claim block with the compact summary + link format
- Add `claims_status: "extracted"` to frontmatter
- Add `claims_count` and `claims_files` to frontmatter
- The cross-cutting assessment table stays — it now references claim IDs

**4. Session close (5 minutes):**
- Update `notes/claims-progress.md`:
  - Check off processed notes
  - Update the status summary numbers
  - Append a session log entry
- Git commit in the Truth project: `claims: extracted N claims from M notes (2026-07-23 session)`
- The next session picks up where this one left off

### Batch Size and Session Cadence

**Batch size: 3-5 notes per session.** Each note has 4-10 claims, so that's 15-40 claims per session. This is small enough to fit in a single context window with room for the skill, the notes, and the generated claim files, but large enough to build momentum.

**Session cadence:** 2-3 sessions per week, each 45-90 minutes. At 150 notes and 4 notes per session, that's ~38 sessions, or about 3-4 months at 3 sessions/week. This is sustainable. The alternative (trying to batch 20+ notes in one marathon session) would degrade quality through context rot and session-length laziness.

**Why this works where a single session wouldn't:**
- Each session starts fresh — no context rot from accumulated conversation
- The skill provides consistent instructions (no drift across sessions)
- The progress file ensures continuity (no "what did I do last time?")
- Git commits create a durable trail (recoverable from any state)
- The human stays involved (quality control at every session boundary)

### What Can Be Automated (Per Note, Not Batch)

Within a single session, processing one chapter note can be partially automated:

1. **Parse claim blocks** — the `## Claim N:` headers and `**Bold Label:**` sections are machine-readable. A Python helper script (loaded via `execute_code`) can split a chapter note into claim segments, extract the labeled sections, and generate the claim file skeleton with frontmatter populated from the note's YAML.
2. **Suggest tags** — keyword analysis on the claim text (e.g., "Kuntillet Ajrud" → `topic/kuntillet-ajrud`, "asherah" → `topic/asherah`, "grammar" → `evidence/grammatical`).
3. **Generate the claim file** — fill in the body template with extracted sections, leaving the Edges section as a placeholder.

But the value-add work — slug assignment, tag refinement, edge identification — requires the agent's semantic understanding of the claim and its relationship to the broader field.

### What Must Be Manual (Per Claim)

1. **Slug assignment** — the descriptive filename must be unique, short, and readable. This requires understanding what makes the claim distinctive.
2. **Tag refinement** — automated tags are suggestions. A claim about "asherah" might be primarily about "aniconism" or "josiah-reform." The agent must read the claim's stakes section to understand what it's REALLY about.
3. **Edge identification** — determining that claim A depends on claim B, or contradicts claim C, requires reading both claims and understanding the argument structure. This is the highest-value work and cannot be automated.
4. **Quality verification** — the extracted text must be complete. Did the parser catch all the evidence? Did it handle the table in the evidence section? Is the confidence rating correctly parsed?

### Handling Claims That Span Multiple Paragraphs

Some chapter notes (especially Dever and Kaufmann) have implicit claims that aren't formatted with `## Claim N:` headers. The agent must:

1. **Identify implicit claims** by reading for argumentative shifts — a new thesis, a new piece of evidence, a counter-argument addressed
2. **Write the claim statement** from scratch, derived from the prose
3. **Add `claim_format: "implicit"`** to the claim file's frontmatter
4. **Add a comment** in the chapter note: `<!-- Implicit claim extracted to [[claim-<slug>]] during processing -->`

### Progress Tracking Between Sessions

The definitive question at session start: "What notes still need claims extracted?"

Answering this question requires only reading the progress file. No need to scan 150 notes or run Dataview queries. The progress file's checklist is authoritative.

When a note is processed, two things happen atomically:
1. The note's frontmatter gets `claims_status: "extracted"`
2. The progress file's checkbox gets checked

These should always agree. A lint operation (added to the skill as a `/lint` command) can scan for discrepancies: notes with `claims_status: "extracted"` but unchecked in the progress file, or vice versa.

### How Many Claims and Sessions?

Revised estimate based on the actual file listing and batch workflow:

| Scholar | Notes | Est. Claims | Sessions (at 4 notes/session) |
|---------|-------|------------|-------------------------------|
| Smith (both books) | 21 | 95 | 5 |
| Römer | 14 | 55 | 4 |
| Kaufmann | 15 | 60 | 4 |
| Lewis | 12 | 50 | 3 |
| Albertz | 15 | 45 | 4 |
| Keel/Uehlinger | 12 | 40 | 3 |
| Dever | 9 | 35 | 2 |
| Day | 8 | 35 | 2 |
| Fleming | 8 | 35 | 2 |
| Sommer | 10 | 25 | 3 |
| Heiser | 8 | 25 | 2 |
| Schmid | 8 | 20 | 2 |
| Stavrakopoulou | 6 | 20 | 2 |
| Cross | 3 | 15 | 1 |
| Tigay | 3 | 10 | 1 |
| **TOTAL** | **~152** | **~565** | **~40** |

**Realistic:** 400-500 claims extracted across 35-40 sessions. At 2-3 sessions per week, that's **3-4 months** for Phase 1 (extraction + basic edges). Add another 2-3 months for Phase 2 (full edge network across all scholars). Total: **5-7 months to a complete Argument Dependency Map.**

This is a research infrastructure project — the kind of thing that, done manually by a human without LLM assistance, would take 2-3 years. An LLM-assisted batch workflow compresses that to half a year of part-time work. The value is in the resulting graph, which compounds: every new book you read can have its claims extracted in a single session and immediately connected to the existing network.

---

## Example

See the companion files:
- **Example claim file:** [[claim-kuntillet-ajrud-symbol-not-goddess]] (smith-ehg-3.2)
- **Modified chapter note:** [[Smith Chapter 3 — Yahweh and Asherah]] (showing post-extraction format)

---

## Open Questions

1. **Should the obsidian-book-notes skill be updated** to generate claim files automatically during initial note creation, rather than extracting after the fact? This would prevent the backlog problem for future books.

2. **Canvas mind map.** Once claims are extracted, should we generate an Obsidian Canvas that visualizes the claim network? The Canvas format supports labeled edges and color-coded nodes.

3. **Dataview integration.** Should we add Dataview queries to the Theology Index that dynamically list claims by topic, confidence, or scholar? This would give a living dashboard.

4. **Confidence standardization.** The existing notes use inconsistent confidence ratings (HIGH, MEDIUM-HIGH, LOW-MEDIUM, etc.). Should we standardize to a fixed scale during extraction?

5. **Claim versioning.** If Graham re-reads a chapter and changes his assessment of a claim, does the claim file get edited in place, or does it get a new version with a `superseded_by` edge? The former is simpler; the latter preserves intellectual history.

---

## Design Principles (Summary)

1. **Claims are first-class citizens.** Every claim gets its own file. The graph view becomes a claim network, not a note network.
2. **Tags do the organizing work.** Folder structure is flat. Topic, evidence, scholar, and source tags enable filtering.
3. **Edges are explicit and typed.** Dependencies, contradictions, support, and challenges are named relationships with wikilinks.
4. **Chapter notes remain readable.** Extraction replaces claim blocks with compact summaries + links. The chapter note is still a coherent document.
5. **Primary sources are nodes too.** Inscriptions, texts, and artifacts get their own files linked bidirectionally to claims.
6. **Automation handles the mechanical work. Humans handle the semantics.** Extraction is scriptable. Edges require reading and judgment.
7. **The graph is the deliverable.** The design is successful when you can filter by `type:claim` + `topic:asherah` and see a meaningful network.
