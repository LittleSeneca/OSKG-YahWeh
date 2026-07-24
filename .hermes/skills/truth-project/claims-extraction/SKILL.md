---
name: claims-extraction
description: "Extract structured claims from Truth Project chapter notes into first-class Obsidian claim files — multi-session batch workflow with progress tracking."
version: 1.0.0
category: truth-project
metadata:
  hermes:
    tags: [truth-project, obsidian, extraction, knowledge-graph]
---

# Claims Extraction — Truth Project

Extract scholarly claims from chapter notes in the Truth Project (`~/Projects/Personal/Truth`) into individual Obsidian claim files. This is a multi-session batch workflow: every session processes 3-5 chapter notes, updates the progress file, and commits. The next session picks up where the last one left off.

## Trigger

User says "let's extract claims" or "claims extraction session" or similar. Load this skill, read the progress file, and start processing the next unclaimed batch.

## Prerequisites

Before the FIRST extraction session, ensure these exist:
- `notes/claims-architecture.md` — the design document (reference for format decisions)
- `notes/claims-progress.md` — the progress tracker (this file IS the state)
- `notes/claims/` — directory for claim files (should exist, create if not)

## Project Structure

```
~/Projects/Personal/Truth/
├── notes/
│   ├── claims-architecture.md      # Design document (reference)
│   ├── claims-progress.md          # Progress tracker (this is STATE)
│   ├── theology/                   # Chapter notes (INPUT — read only, but frontmatter gets updated)
│   ├── claims/                     # Claim files (OUTPUT — created here)
│   └── example-smith-ch3-post-extraction.md  # Format reference
├── sources/
│   ├── primary-sources/
│   │   └── key-inscriptions.md     # To be split into individual source notes later
│   └── books/_fulltext/            # Full-text source books (for reference)
```

## Session Workflow

### Step 1: Session Start (load state)

**Always do these first, in order:**

1. Read `notes/claims-progress.md` — identify the next unclaimed batch
2. Identify 3-5 unchecked chapter notes. Batch selection is strategic, not random. See "Batch Selection Strategy" below.
3. Read `notes/claims-architecture.md` sections on tag taxonomy and claim ID format (or rely on this skill)

### Step 2: Process Each Note (15-30 min per note)

**When creating claim files in batch:** use `execute_code` with `from hermes_tools import write_file`. Writing 10+ claim files via serial `write_file` calls burns turns and context. A single `execute_code` script can create all claim files for a 3-note batch (8-15 files) in one turn. Write each file's full content as a Python string, call `write_file(path, content)` for each, and print progress markers. See `references/execute-code-pattern.md` for the Session 1 example.

**When processing 5 notes (the upper end): use the midpoint quality gate.** After note 3, pause and verify:
- Is the third claim file as thorough as the first? Check: evidence section has bullet points/tables not just a paragraph, edge descriptions name scholars and arguments not just claim slugs
- If quality is holding, continue to notes 4-5
- If there's thinning (shorter evidence, generic edges), stop at 3, update progress, and flag the skill for tuning. Do not push through degraded quality.

**For each chapter note in the batch:**

**2a. Read the chapter note** — use `read_file` on the full note.

**2b. Find all claims** — look for `## Claim N:` headers. Each one is a claim to extract. Also scan for implicit claims (Dever-style category headings, Kaufmann-style multi-paragraph arguments without `## Claim N:` format).

**2c. For each claim, create a claim file in `notes/claims/`:**

**2c-i. Determine the slug** — a short, descriptive, unique handle. Rules:
- Lowercase, hyphens between words
- Must be distinctive enough that no two claims get the same slug
- Capture the core assertion: `kuntillet-ajrud-symbol-not-goddess` not `smith-claim-2`
- If unsure, read the claim's stakes section — it often reveals what makes the claim distinctive
- Use `search_files` to check the slug doesn't collide with an existing claim file
- **Use `yhwh` (not `yahweh`) for the divine name in slugs.** The claim_id format standardizes on `yhwh` (e.g., `romer-inv-1.2`), and mixing `yhwh`/`yahweh` spellings produces broken wikilinks when other files reference the claim using the wrong variant. Session 8 had 7 broken links from `claim-yahweh-originated-southern-deserts-edom-seir` when the file was actually `claim-yhwh-originated-southern-deserts-edom-seir`.

**2c-ii. Generate the claim ID** — format: `<scholar-initials>-<book-abbrev>-<chapter>.<claim-number>`

| Scholar | Abbreviation |
|---------|-------------|
| Mark S. Smith, Early History of God | `smith-ehg` |
| Mark S. Smith, Origins of Biblical Monotheism | `smith-obm` |
| Thomas Römer, The Invention of God | `romer-inv` |
| William Dever, Did God Have a Wife? | `dever-dghw` |
| Theodore Lewis, Origin and Character of God | `lewis-ocg` |
| Yehezkel Kaufmann, Religion of Israel | `kaufmann-ri` |
| Jeffrey Tigay, You Shall Have No Other Gods | `tigay-nog` |
| John Day, Yahweh and the Gods of Canaan | `day-ygc` |
| Frank Moore Cross, Canaanite Myth and Hebrew Epic | `cross-cmhe` |
| Daniel Fleming, Yahweh Before Israel | `fleming-ybi` |
| Othmar Keel/Christoph Uehlinger, Gods Goddesses Images | `keel-ggi` |
| Konrad Schmid, Historical Theology of the Hebrew Bible | `schmid-ht` |
| Michael Heiser, The Unseen Realm | `heiser-ur` |
| Benjamin Sommer, The Bodies of God | `sommer-bog` |
| Francesca Stavrakopoulou, God: An Anatomy | `stav-god` |
| Rainer Albertz, History of Israelite Religion | `albertz-hir` |

**2c-iii. Write the claim file** — use this template:

```yaml
---
tags:
  - type/claim
  - topic/<primary-topic>       # REQUIRED: at least one, typically 2-4
  - topic/<secondary-topic>
  - evidence/<evidence-type>    # REQUIRED: at least one
  - scholar/<scholar-slug>      # REQUIRED
  - source/<book-slug>          # REQUIRED
  - truth-project
claim_id: "<id>"               # REQUIRED
statement: "<one sentence>"     # REQUIRED
confidence: "<rating>"          # REQUIRED
confidence_rationale: "<one sentence>"
claim_type: "<textual|archaeological|philological|theological>"
source_note: "[[<chapter note>]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active
---

# <claim_id>: <statement>

**Source:** [[<chapter note>]] — <Scholar>, *<Book>* (<Year>), <Chapter>

## The Claim

<Full claim statement with direct quotes from the chapter note.>

## Evidence

<Structured evidence — bullet points, tables, narrative. Copy the evidence section from the chapter note verbatim.>

## Confidence

**Rating:** <rating>

**Rationale:** <One sentence from the chapter note's confidence section.>

## Stakes

<What's at stake — copied from the chapter note.>

## Disagreement

**Who disagrees:** <Named scholars from the chapter note. If they have claim files already, wikilink them: [[claim-<slug>]]>

**Alternative reading:** <The counter-position.>

## Edges

<!-- Populate during extraction when connections are obvious. Leave placeholders for cross-scholar connections to be filled later. -->

**Depends on:**
<!-- Claims this one requires to be true -->

**Supports:**
<!-- Claims this one provides evidence for -->

**Contradicts:**
<!-- Claims that cannot be true if this one is -->

**Challenged by:**
<!-- Evidence or arguments that weaken this claim -->

**Primary sources:**
<!-- Inscriptions, texts, artifacts — use [[<filename-slug>]] wikilinks matching the exact filename in sources/primary-sources/. Do NOT prefix with source- unless the file actually has that prefix. Example: [[soleb-shasu-inscription]] not [[source-soleb-shasu-inscription]]. The Amara West list is covered by the Soleb note — do not create separate broken wikilinks for it. -->

## Assessment

<Graham's evaluation from the chapter note.>
```

**2d. Tag assignment — use this taxonomy:**

**Topic tags (pick 1-4 that BEST describe what the claim is ABOUT):**
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
- `topic/kuntillet-ajrud`
- `topic/soleb-shasu`
- `topic/deut-32-8-9`
- `topic/merneptah-stele`
- `topic/second-isaiah`
- `topic/wisdom-literature`
- `topic/ugaritic-parallels`
- `topic/syncretism`
- `topic/archaeology-method`
- `topic/historiography`
- `topic/persian-period`
- `topic/exodus`
- `topic/patriarchs`
- `topic/covenant`
- `topic/prophecy`

**Evidence tags (pick 1-3 that describe the TYPE of evidence):**
- `evidence/inscriptional`
- `evidence/archaeological`
- `evidence/biblical-text`
- `evidence/grammatical`
- `evidence/onomastic`
- `evidence/iconographic`
- `evidence/comparative-ane`
- `evidence/ugaritic`
- `evidence/historiographical`
- `evidence/philological`

**Scholar tags (exactly one):**
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

**Source tags (exactly one):**
- `source/smith-early-history-of-god`
- `source/smith-origins-biblical-monotheism`
- `source/romer-invention-of-god`
- `source/dever-did-god-have-a-wife`
- `source/lewis-origin-character-of-god`
- `source/kaufmann-religion-of-israel`
- `source/tigay-no-other-gods`
- `source/day-yahweh-gods-of-canaan`
- `source/cross-canaanite-myth-hebrew-epic`
- `source/fleming-yahweh-before-israel`
- `source/keel-gods-goddesses-images`
- `source/schmid-historical-theology`
- `source/heiser-unseen-realm`
- `source/sommer-bodies-of-god`
- `source/stavrakopoulou-god-anatomy`
- `source/albertz-history-israelite-religion`

**2e. Add edges** — when processing notes within the same session, you may recognize connections between claims. Add them immediately:
- If you just extracted Claim A from Smith and Claim B from Römer that directly contradict each other, add the edge now
- If Claim C from Dever obviously supports Claim D from Day, add it now
- Leave `<!-- placeholder -->` for connections you suspect exist but can't verify without reading other notes

**Wikilink format: use file slugs, NEVER claim IDs.** Every `[[wikilink]]` in an Edges section must use the exact filename slug you wrote to `notes/claims/`. The claim ID (e.g., `kaufmann-ri-8.4`) is metadata — it is NOT a filename. Files are named with descriptive slugs (`claim-golden-calves-yhwh-worship-not-pagan-idolatry.md`), so wikilinks must be `[[claim-golden-calves-yhwh-worship-not-pagan-idolatry]]`. Writing `[[claim-kaufmann-ri-8.4]]` creates a broken link because no file has that name. Cross-scholar edges (to Smith/Römer/Day) naturally use correct slugs because you look up the existing file. Internal edges within the same batch are where this bug bites: you know the claim ID because you just assigned it, but you must look up the slug you also just assigned. After creating all claims in a batch, verify every `[[claim-...]]` wikilink you wrote resolves to a real file before declaring the batch complete.

**Edge wikilink rule: only reference extracted claims.** When writing edges (in new claim files or when updating existing Session N claims with edges from Session N+1), wikilinks MUST point to claims that already exist in `notes/claims/`. Forward references to claims not yet extracted break Obsidian's graph. For anticipated edges to future claims, use HTML comments:
```
<!-- Will edge to Day Ch4 (Yahweh appropriates Baal imagery) when extracted -->
```
Verify each wikilink with `search_files` before writing it. Non-existent wikilinks create broken graph edges and misleading dependency chains.

### Step 3: Update the Chapter Note

After extracting all claims from a note:

1. **Replace each `## Claim N:` block** with the compact summary format:
```markdown
## Claim N: <title>
→ [[claim-<slug>]] | **<claim_id>** | Confidence: <rating>
  <one-sentence summary of the claim's significance>
  <key edges if obvious: Contradicted by: [[claim-x]], Supports: [[claim-y]]>
```

2. **Add to the chapter note's YAML frontmatter:**
```yaml
claims_status: "extracted"
claims_extracted_date: YYYY-MM-DD
claims_count: <N>
claims_files:
  - "[[claim-<slug1>]]"
  - "[[claim-<slug2>]]"
```

3. **Keep the cross-cutting assessment table intact** — it now references claim IDs alongside the summaries.

4. **Do NOT delete the original claim content** — it stays in git history. The replacement is the active version.

### Step 4: Update Progress

After processing all notes in the batch:

1. **Update `notes/claims-progress.md`:**
   - Check off each processed note (`[ ]` → `[x]`)
   - Update the Status Summary numbers
   - Append a session log entry:
   ```markdown
   ### YYYY-MM-DD — Session N
   - Notes processed: N (<list which ones>)
   - Claims extracted: N
   - Edges added: N (plus N placeholders)
   - Commits: N
   - Notes remaining: N
   ```

2. **Git commit** in the Truth project:
   ```bash
   cd ~/Projects/Personal/Truth
   git add notes/claims/ notes/theology/ notes/claims-progress.md
   git commit -m "claims: extracted N claims from M notes (<scholar list>)"
   ```

### Step 5: Session Handoff

Before ending the session, report:
- What was processed (notes and claim counts)
- What the next batch should be (first 3-5 unchecked notes in the progress file)
- Any claims that need special attention (implicit claims, claims that seem to contradict but need verification)
- Any patterns noticed (e.g., "Smith and Römer overlap heavily on Kuntillet Ajrud — batch them together next session")
- Updated notes-remaining count

## Batch Selection Strategy

Don't pick notes randomly or just in alphabetical order. The goal is **edge compounding**: every session's edges should connect to claims already extracted in prior sessions, so the graph grows denser with each batch rather than starting fresh each time.

**Principles:**

1. **Thread-first, not scholar-first.** Pick notes that share a topic across scholars (Asherah, Baal, El, monotheism, divine council) rather than finishing one scholar before starting another. Three notes on Asherah from Smith, Römer, and Day produced 38+ cross-scholar edges. Three notes from the same scholar would have produced maybe 8 internal edges.

2. **Dependency direction.** After extracting claims that make assertions (e.g., "Asherah was a goddess consort"), the next batch should pick up the foundation claims those assertions DEPEND on (e.g., "Yahweh absorbed El's identity", "Ugaritic Athirat = OT Asherah"). This builds the argument tree from leaves toward roots.

3. **Mix sizes.** Pair dense notes (Kaufmann, Lewis — 6-10 claims each) with lighter ones (Tigay, Cross — 2-4 claims). A batch of three Kaufmann chapters (30 claims) will degrade; a batch of one Kaufmann + two Day chapters (~14 claims) is balanced.

4. **Review edges from prior sessions.** Before picking a batch, skim the edges in 2-3 claims from the last session. What threads are they pointing at? What claims do they say they depend on? Pick notes that supply those dependencies.

5. **Every session's handoff suggests the next batch.** The session log entry includes a "next batch suggestion." The next session starts there unless Graham overrides.

## Handling Edge Cases

### Combined/Overlapping Notes

Some scholars have notes that cover multiple chapters AND individual chapter notes (especially Römer: "Romer — Chapters 2-3 — Geographic Origin and Moses" vs. "Romer — Chapter 2 — Geographic Origin" and "Romer — Chapter 3 — Moses and the Midianites").

**When processing a combined note:** extract claims normally. The claim_id uses the combined note's chapter designation (e.g., `romer-inv-2-3.1`).

**When processing individual notes that overlap with a combined note:** check if the combined note has ALREADY been processed. If yes, the individual notes may already have their claims extracted — check the progress file and the note's frontmatter. If the combined note has NOT been processed, process the individual notes and skip the combined note (or mark it as `[~] partially covered`).

**Decision rule:** prefer individual chapter notes over combined notes. Process individual notes first. When you encounter a combined note that covers already-processed chapters, check if there are claims in the combined note that aren't in the individual notes — there may be cross-cutting synthesis claims that only appear in the combined version.

### Implicit Claims

When a note uses category headings (Dever Ch V) or narrative argument (Kaufmann) rather than `## Claim N:` format:

1. Identify argumentative shifts as claim boundaries
2. Write the claim statement yourself — make it a single sentence assertion
3. Add `claim_format: "implicit"` to the claim file's frontmatter
4. In the chapter note, add an HTML comment: `<!-- Implicit claim extracted to [[claim-<slug>]] -->`
5. For the chapter note replacement, add a `### Implicit Claim:` heading (h3) with the compact summary format

### Meta-notes and Index Notes

Do NOT extract claims from:
- `Theology Index.md`
- `scholarly-directory-yahweh-origins.md`
- `meta-analysis-scholars.md`
- `yahweh-monotheism-polytheism-debate.md`

These are project infrastructure, not chapter notes. They stay as-is.

### Notes Without Claims

Some notes (forewords, prefaces, book summaries) may contain zero or one claim. That's fine — process what's there. The progress file checkbox still gets checked.

## Quality Checklist

Before marking ANY note as `claims_status: "extracted"`, verify:

- [ ] Every `## Claim N:` block in the original has a corresponding claim file
- [ ] Every claim file has a unique, descriptive slug
- [ ] Every claim file has ALL required frontmatter fields (claim_id, statement, confidence, tags)
- [ ] Every claim file has at least one topic tag and one evidence tag
- [ ] Every claim file has the correct scholar and source tags
- [ ] **Every claim file has an `## Evidence` section header with structured content (bullets or tables, not just a paragraph). grep for `^## Evidence` — missing header = embedded-evidence defect (Pitfall 18).**
- [ ] The chapter note's claims_status, claims_count, and claims_files frontmatter match reality
- [ ] Each replaced claim block in the chapter note has the correct wikilink and claim_id
- [ ] The cross-cutting assessment table is preserved
- [ ] No original content was deleted — only transformed (git shows the diff)
- [ ] **All wikilinks in chapter notes' compact summaries and claims_files resolve to real files**

See `references/quality-benchmarks.md` for concrete examples of what "good" looks like from session 1. Use these to calibrate at the midpoint gate.

## Confidence Rating Standardization

The existing notes use inconsistent ratings. Standardize to this scale during extraction:

| Original | Standardized |
|----------|-------------|
| VERY HIGH | very-high |
| HIGH | high |
| MEDIUM-HIGH | medium-high |
| MEDIUM | medium |
| LOW-MEDIUM | low-medium |
| LOW | low |
| DEBATABLE | debatable |

The confidence_rationale field captures the one-sentence justification.

## Pitfalls

1. **Skipping the progress file read.** Always read `notes/claims-progress.md` at session start. Don't guess what's been done.
2. **Processing too many notes per session.** The context window degrades. 3-5 notes is the sweet spot. If you feel pressure to do more, stop and pick up next session.
3. **Losing the assessment.** The "My assessment" section is Graham's own voice — the most valuable part. Never truncate or paraphrase it.
4. **Generic slugs.** "claim-smith-asherah.md" is too vague. Make it specific: "claim-asherah-was-yahwistic-symbol.md"
5. **Inconsistent divine-name spelling in slugs.** Use `yhwh` (not `yahweh`) consistently. The claim_id format uses `yhwh`, and mixing spellings produces broken wikilinks.
6. **Forgetting frontmatter fields.** claim_id, statement, and confidence are REQUIRED on every claim file.
7. **Not committing between sessions.** If a session crashes, uncommitted work is lost. Commit after each batch.
8. **Handling duplicate combined+individual notes incorrectly.** When in doubt, prefer individual chapter notes and mark the combined note for later review.
9. **Session log landing inside HTML comment.** The progress file wraps the session log template inside an HTML comment. Close the comment (`-->`) before appending.
10. **Pre-existing example claim files.** When progress says unchecked but a claim file already exists, verify it's complete before skipping.
11. **Writing prompts for fresh sessions.** Must be self-contained: project path, current state, specific batch, rationale, skill name, and handoff instructions. A fresh agent has zero context.
12. **`patch` for chapter note claim blocks has failure modes.** Works for simple replacements but can fail on self-referential headings. Fall back to `write_file`.
13. **Edge wikilink verification.** Verify every wikilink targets a real file with `search_files` before writing. Broken edges corrupt the graph.
14. **Internal edges use claim IDs instead of slugs.** The most frequent bug: `[[claim-kaufmann-ri-8.4]]` instead of `[[claim-golden-calves-yhwh-worship-not-pagan-idolatry]]`. Happens on internal edges within the same scholar's batch. grep for `[[claim-<scholar-prefix>-` after writing to catch these.
15. **Harness quality gate false positives.** The Phase 2 prompt template contains `FAIL` as a format example. The harness must scope grep to content between `=== QUALITY REVIEW ===` markers.
16. **`hermes chat -q` flag ordering.** `-q` consumes the NEXT argument. Correct: `hermes chat -q "prompt" -s skill`. Wrong: `hermes chat -q -s skill "prompt"`.
17. **Harness prompts missing full file paths.** Passing only titles forces the session to guess filenames. Always include `title → notes/theology/filename.md`.
18. **Evidence section merged into The Claim.** The most common structural defect: evidence content is substantial (bullets, tables, data) but lives inside `## The Claim` instead of under its own `## Evidence` header. The claim file has sections The Claim → Confidence → Stakes → Disagreement → Edges, skipping Evidence entirely. This happens when the extractor doesn't split the chapter note's combined claim+evidence block. **Fix:** insert `## Evidence\n\n` between The Claim's statement paragraph and the evidence paragraphs. The content is already there — it's a heading placement issue, not missing content. In batch 24, 2 of 19 files (4.2 and 4.9) had this defect. Phase 2 quality review must catch this: grep for `^## Evidence` in every claim file created.
19. **`patch` corrupting frontmatter with matching `created:` lines.** When `old_string` in a frontmatter patch includes `---` (the closing frontmatter marker) and `created:` (which appears in multiple note files), the patch tool can match the wrong occurrence, silently removing tags and escaping quotes. Symptoms: missing YAML tags (faith/polytheism, truth-project dropped), escaped quotes (`\\\"title\\\"`), misplaced frontmatter. **Fix:** when adding claims_status block to frontmatter, use `write_file` with the complete rewritten file rather than `patch`. If you do use `patch`, include enough unique context lines (at least 5 lines of surrounding YAML) to guarantee a single match. Always read the patched file immediately after to verify nothing was corrupted.
20. **Primary source wikilinks using wrong slugs.** The `sources/primary-sources/` directory contains files with specific names — wikilinks must match the exact filename. The Soleb note is `soleb-shasu-inscription.md`, not `source-soleb-shasu-list.md` or `source-soleb-shasu-inscription.md`. Amara West content is covered by the Soleb note — do not create a separate broken `[[source-amara-west-shasu-list]]` wikilink. Before writing any primary source wikilink, verify with `ls sources/primary-sources/*.md` that the slug matches. Broken primary source wikilinks = automatic FAIL in quality review.

21. **Template placeholder `[[source-<slug>]]` surviving extraction.** The claim template includes `<!-- Inscriptions, texts, artifacts — use [[<filename-slug>]] wikilinks -->` as a placeholder. During batch extraction, this was sometimes replaced with the literal text `[[source-<slug>]]` (the INSTRUCTION text, not an actual wikilink). 19 Keel/Uehlinger claims shipped with this literal placeholder (July 2024 audit). **Fix:** Phase 2 quality review must grep ALL claim files created in the batch for the literal string `source-<slug>`. Any hit means the Primary Sources section was never filled in and the placeholder was corrupted. Replace with the HTML comment: `<!-- Inscriptions, texts, artifacts — add wikilinks when primary source identification is complete -->`.

22. **Broken wikilink scanners catching HTML comments.** Regex `\[\[([^\]]+)\]\]` matches wikilinks inside `<!-- ... -->` comments. Forward references intentionally commented out (e.g., `<!-- [[claim-cross-el-yahweh-identity]] — forward reference to Cross claim, not yet extracted -->`) will be flagged as broken edges, producing false positives. **Fix:** strip HTML comments from the content before scanning for wikilinks: `no_comments = re.sub(r'<!--.*?-->', text, flags=re.DOTALL)`. Then run the wikilink regex on the stripped text. This applies to both Phase 2 quality review and any post-extraction audit scripts.

## References

- `references/methodology-validation.md` — ORKG and academic validation of the claim-extraction-to-knowledge-graph methodology
- `references/harness-debugging.md` — all known harness bugs and their fixes
- `references/execute-code-pattern.md` — batch file creation via execute_code
- `references/quality-benchmarks.md` — what "good" looks like from Session 1
- `references/primary-source-link-batch-fixer.md` — reusable Python script for retrofitting primary source wikilinks across claim files
- Project pipeline overview: `notes/pipeline-overview.md` in the Truth repo

## Batch Mode / Unattended Operation

The harness script (`extract-loop.sh`) runs this skill non-interactively via `hermes chat -q`. It invokes three distinct phases per batch, each as a fresh session. No conversation context carries between phases — `claims-progress.md` is the only shared state.

**Correct invocation:** `hermes chat -q "<prompt>" -s claims-extraction`. The `-q` flag consumes the next argument as the query — `-s` must not sit between `-q` and the prompt text. See Pitfall 13.

**Quality gate caveat:** The Phase 2 review prompt includes the word "FAIL" in its format template (`TITLE: FAIL — specific issues found`). The harness must scope its grep to lines between the `=== QUALITY REVIEW ===` markers, not the full log file. See Pitfall 14.

**File paths in prompts:** Always include the full relative path (e.g., `notes/theology/Smith Chapter 1 — Deities.md`) alongside note titles. Titles alone force the session to guess filenames, which fails on em dashes and special characters. See Pitfall 15.

### Phase 1: Extraction (`extract`)

Invoked as: `hermes chat -q "<prompt>" -s claims-extraction`

The prompt is constructed by the harness and contains:
- The project path (`~/Projects/Personal/Truth`)
- The specific 3 notes to process (exact filenames)
- The batch number and any context about why these notes were chosen
- Instructions to NOT update claims-progress.md or git commit (Phase 3 does that)

**Phase 1 responsibilities:**
1. Read `notes/claims-progress.md` to confirm state
2. List existing claims in `notes/claims/` (for edge targeting)
3. For each of the 3 notes: read it, extract all `## Claim N:` blocks into claim files, update the chapter note with compact summaries and frontmatter
4. Add edges between the new claims and to any existing claims in `notes/claims/`
5. Print a structured summary to stdout (the harness parses this):

```
=== BATCH SUMMARY ===
Notes processed: 3
Smith Chapter 2 — Yahweh and Baal: 5 claims created (smith-ehg-2.1 through 2.5)
Romer — Chapter 8 — Statue of Yhwh: 4 claims created (romer-inv-8.1 through 8.4)
Day — Chapter 1 — Yahweh and El: 4 claims created (day-ygc-1.1 through 1.4)
Total claims created: 13
Edges added: ~25 (internal + cross-scholar)
=== END SUMMARY ===
```

**Do NOT in Phase 1:** update claims-progress.md, run git commit, or ask clarifying questions (there's no user to answer them). If something is genuinely ambiguous, note it in the summary under `=== ISSUES ===`.

### Phase 2: Quality Review (`review`)

Invoked as: `hermes chat -q "quality review for batch <N>: <note list>" -s claims-extraction`

**Phase 2 responsibilities:**
1. Check every claim file just created: required frontmatter present, tags complete, at least one topic tag and one evidence tag.
2. **Verify `## Evidence` section header exists.** grep every claim file for `^## Evidence`. This catches the embedded-evidence defect (Pitfall 18) where evidence content lives under `## The Claim` instead. Also confirm evidence has structured content (bullets or tables, not just a paragraph).
3. Check every chapter note updated: claims_status frontmatter present with correct count, compact summaries correct, claims_files wikilinks resolve to real files (verify with search_files or `ls`).
4. Check for content degradation: are later claims in each note as thorough as the first? Compare line counts, evidence section size, and edge count across claims within a note.
5. Verify ALL wikilinks in both claim files and chapter notes resolve to real files. This includes BOTH inter-claim wikilinks AND primary source wikilinks (in `## Edges → **Primary sources:**` sections). Broken wikilinks = automatic FAIL regardless of content quality. Verify primary source wikilinks with `ls sources/primary-sources/<slug>.md` — NOT with the claims directory. **When scanning for broken wikilinks, strip HTML comments (`<!-- ... -->`) from the content first.** Raw regex `\[\[([^\]]+)\]\]` will match wikilinks inside HTML comments — forward references intentionally commented out should not be flagged as broken. See Pitfall 22.
6. **Grep for literal `source-<slug>` in all claim files.** The template placeholder `[[source-<slug>]]` has survived extraction in 19 Keel/Uehlinger claims (July 2024 audit). This is the literal text `<slug>`, not a variable — it was never replaced with an actual filename. grep for `source-<slug>` — any hits are unfilled template placeholders. See Pitfall 21.
7. Verify edge descriptions name scholars and arguments, not just claim slugs.
7. Print a per-note pass/fail report:

```
=== QUALITY REVIEW ===
Smith Chapter 2: PASS — 5 claims, all frontmatter valid, 8 edges
Romer Chapter 8: PASS — 4 claims, all frontmatter valid, 6 edges
Day Chapter 1: FAIL — day-ygc-1.3 missing confidence_rationale, edges section has only placeholders
=== END REVIEW ===
```

Exit with non-zero if any note fails. The harness stops the loop on failure.

### Phase 3: Finalize (`finalize`)

Invoked as: `hermes chat -q "finalize batch <N>: <note list>" -s claims-extraction`

**Phase 3 responsibilities:**
1. Cross-scholar edge pass: re-read the new claims and add edges between scholars within the batch (contradictions, supports, dependencies). Each session processed its own scholar's notes in isolation — Phase 3 sees all three together.
2. Update `notes/claims-progress.md`: check off the three notes, update status summary, append session log entry
3. Git commit with message: `claims: extracted <N> claims from <scholar list> (session <N>)`
4. Print next-batch suggestion:

```
=== FINALIZE COMPLETE ===
Batch 2 committed: 13 claims from Smith Ch2, Römer Ch8, Day Ch1
Notes remaining: 143
Next batch: Smith Ch4 (Yahweh and the Sun) + Römer Ch10 (Fall of Samaria) + Day Ch3 (Yahweh vs Baal)
=== END FINALIZE ===
```

### Harness Script Location

`~/Projects/Personal/Truth/extract-loop.sh`

Run it with: `bash extract-loop.sh [--batch N] [--dry-run] [--stop-after N]`

The harness parses `=== BATCH SUMMARY ===`, `=== QUALITY REVIEW ===`, and `=== FINALIZE COMPLETE ===` markers from stdout to track progress and detect failures.

Known bugs and fixes documented in `references/harness-bugs.md` — if the harness breaks, check there first.

When debugging harness failures, see `references/harness-debugging.md` for known bugs and their fixes (flag ordering, quality gate false positives, missing file paths, `local` scope in bash).
