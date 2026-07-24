---
name: obsidian-book-notes
description: "Create detailed, critical Obsidian notes from books — chapter by chapter, claim by claim, with full evaluation format. Works for any domain."
version: 1.0.0
platforms: [linux, macos]
metadata:
  hermes:
    tags: [note-taking, obsidian, research, reading, truth-project]
---

# Obsidian Book Notes

Turn any book into a structured set of Obsidian notes — one per chapter (or major section), with every major claim evaluated for evidence, confidence, stakes, and disagreement. Designed for critical engagement, not passive summary.

---

## Core Principles

1. **You are a critic, not a stenographer.** Report what the author says, then EVALUATE it. Where is the evidence weakest? What assumptions are unexamined? Who disagrees?
2. **Chapter-by-chapter granularity.** One note per chapter unless chapters are very short and form a single argument. Never compress an entire book into a single note.
3. **Every major claim gets the full format.** Claim. Evidence. Confidence. Stakes. Disagreement. Alternative reading. Assessment.
4. **Tag aggressively.** Every note gets domain tags, topic tags, scholar tags, and project tags in its frontmatter.
5. **Cross-reference relentlessly.** Link to other book notes, to the broader project index, to primary sources, and to any scholarly directory or meta-analysis the project contains.

---

## The Note Format

Every chapter note follows this structure:

### Frontmatter

**Standalone chapter note:**
```yaml
---
tags: [source/book-notes, domain-tag, topic-tags, scholars/author-name, project-tag]
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: high|medium|low
source:
  title: "Book Title"
  author: "Author Name"
  year: YYYY
  publisher: "Publisher"
  local_file: "path/to/extracted/text.txt"
related:
  - "[[Other Note]]"
  - "[[Another Note]]"
---
```

**Combined-note (when adjacent chapters are combined):** add three fields:
```yaml
note_type: combined
combined_sections: "§§X-Y"   # or "Chs N-M" — the sections covered
justification: "§X (89 lines) and §Y (108 lines) too short for standalone; form single chronological argument about [...]"
```
The `justification` field MUST be specific — state the line counts AND the argumentative reason for combining. "Efficiency" or "these chapters are short" without the argumentative connection is NOT sufficient justification.

### Chapter header and overview
```markdown
# Author — Chapter Title

Brief 1-2 sentence summary of the chapter's contribution.
```

**Combined notes:** use the contributed-sections format:
```markdown
# Author — §§X-Y: Descriptive Title

Brief summary covering the argument shared across the combined sections.

## §X: Section Title
[claims for this section using ### Claim N:]

## §Y: Section Title
[claims for this section using ### Claim N:]
```

### Per-claim format (repeat for each major claim)

**Heading level convention:**
- Standalone chapter notes: use `## Claim N:` (h2)
- Combined notes: use `### Claim N:` (h3), nested under the `## §X:` section header

```markdown
### Claim N: [One sentence — what is the author asserting?]

**Author's claim:** Full statement of the claim with direct quotes from the text.

**Evidence presented:** What specific data does the author marshal? Bullet points. Be specific — cite passages, inscriptions, statistics, studies.

**Confidence:** HIGH / MEDIUM / LOW with one-sentence justification. What makes this strong or weak?

**What's at stake:** If true, what changes? If false, what depends on it? Why does this matter?

**Who disagrees:** Named scholars or schools with specific counter-arguments. Link to their entries if a scholarly directory exists.

**Alternative reading:** If the evidence can be reasonably interpreted differently, what's the other reading?

**My assessment:** Brief — does this hold up? What would I need to verify? What's the weakest link?
```

### Chapter-level cross-cutting assessment
```markdown
## Chapter N Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| Claim 1 summary | HIGH/MEDIUM/LOW | What would falsify it |
| Claim 2 summary | HIGH/MEDIUM/LOW | What would falsify it |

**Strongest section:** What part of the chapter is most persuasive?

**Weakest section:** What part is least persuasive?
```

---

## The Workflow

### Step 1: Extract the text
If the book is not already extracted:
- Find the PDF/EPUB in Downloads or elsewhere
- Extract with PyMuPDF (`fitz`) for PDFs, `ebooklib` + `html2text` for EPUBs
- Place in `sources/books/_fulltext/` (gitignored — never commit copyrighted full text)
- Naming convention: `Author_Title_Year.txt`

### Step 2: Map the structure
- Read the table of contents
- Identify chapter boundaries. Start with the TOC near the front of the file — it gives the authoritative chapter list with page numbers. Then locate body-text positions using one of these patterns depending on the extraction format:
  - **Explicit chapter headers:** `grep -n "^Chapter\|^CHAPTER\|^C H A P T E R"`
  - **Part/subsection structures (§1.1, §2.3):** `grep -n "^[0-9]\.[0-9]"` in the body text
  - **Bare number + title (common in PDF extractions):** chapters may appear as a bare digit on its own line followed by the title on the next line (e.g., "2\nYhwʒ of Shasu-Land"), with no "Chapter" prefix. These often appear near PAGE markers. Use the TOC page numbers to estimate the PDF offset (book page + N ≈ PDF page), then search near the corresponding PAGE marker for `^[0-9]+$` lines. The TOC's section titles double as the expected chapter title near that number.
  - **PITFALL — OCR-garbled chapter headers:** PDF extraction can garble "CHAPTER" beyond recognition (e.g., ". CH^APTER II", "ciiArrKR v", "CHAPTER VIIJ"). A `grep -n '^CHAPTER '` will miss these. When the TOC says a chapter exists but `grep '^CHAPTER'` doesn't find it, try broader patterns: `grep -n 'CHAPTER\\|CH^APTER\\|C H A P T E R'` for garbled headers, or search for the chapter's first section heading (from the TOC) as a landmark — e.g., if Ch II begins with "THE FUNDAMENTAL IDEA", grep for that. Also scan around the expected page-offset: if the TOC says Ch II starts at book page 21, look near the body-text line range that maps to that page number.
- Decide note granularity (see above)
- **Chapter splitting for large extractions (20K+ lines):** when the full text is huge, split each chapter into a separate temp file before reading. Use `execute_code` with Python to run `sed` boundaries against the source file, writing each chapter to `/tmp/book_ChN.txt`. This avoids re-reading the entire source for every chapter and makes chunked reading via `execute_code` + `open()` much faster. Confirm boundaries with a test read of the first/last 5 lines of each temp file.
- **PITFALL — `read_file` fails with special characters:** the `read_file` tool cannot resolve filenames containing em dashes or other Unicode punctuation common in Truth project paths. Do NOT use `read_file` to read these files. Instead use (a) `terminal` with `sed -n 'START,ENDp'` for targeted reads, or (b) `execute_code` with Python `open().read()` for full-chapter ingestion. The chapter-splitting pattern above (writing to `/tmp/book_ChN.txt`) avoids the filename issue entirely.
- **Optional companion step — primary sources:** If the book references specific ancient texts, inscriptions, or primary documents repeatedly (e.g., Kuntillet Ajrud, Ugaritic tablets, stele inscriptions), consider collecting those primary sources alongside the book notes. Place them in `sources/primary-sources/` and cross-reference from the book notes. The primary source collection should precede or parallel the reading — you want the texts at hand when the author discusses them.
- PITFALL: popular books with 40+ short chapters should get one note per Part, not one per chapter. Academic monographs with 7-12 substantial chapters should get one per chapter.
- **Part/subsection structure (common in German academic monographs):** books organized into a small number of Parts (typically 2-4) each containing numbered subsections (e.g., §2.1, §2.2, §3.1-3.9) should get one note per top-level subsection. The Part is the organizing container; the subsections are the real "chapters." If adjacent subsections are short and form a single argument, they can be combined, but the default is one per subsection. Do NOT combine entire Parts into single notes — a Part with 9 subsections is half the book.
- **Thematic books:** books organized by topic rather than chronology (e.g., body-part anatomy, geographical regions, genres of literature) should get one note per Part/Section. The grouping principle should match the author's own organizational logic.
- **Multi-session work:** long books (15+ subsections, dense monographs) will span multiple sessions. This is normal. Finish the session at a natural boundary (e.g., end of a Part), provide a clear handoff summary listing completed and remaining notes, and resume in the next session. Do not rush or compress to finish in one sitting.

### Step 3: Read and write — one chapter at a time (MANDATORY PRE-CHECK)

**CRITICAL — PRE-WRITING CHECK (before writing ANY note):**
- [ ] Ask: "Is this note covering ONE chapter or MULTIPLE chapters?"
- [ ] If MULTIPLE: "What is the justification for combining?" The ONLY acceptable justifications: (a) chapters are very short and form a single indivisible argument, or (b) the book is a popular work with 40+ very short chapters organized into Parts. "I'm tired" is not a justification. "This is efficient" is not a justification.
- [ ] The DEFAULT is one note per chapter. COMBINING requires explicit, defensible justification.
- [ ] If you catch yourself thinking "I can cover chapters X-Y in one note" — STOP. That's the compression instinct. Write them separately.

**After reading — MANDATORY COVERAGE CHECK (before writing the note):**
- [ ] Calculate approximate coverage: (total lines in chapter) vs. (cumulative lines you've read across all chunks). If you've read fewer than 85% of the chapter's lines, you have gaps. Find and fill them now.
- [ ] Check for large unread gaps: the chapter starts at line A and ends at line B. Your read chunks covered [A1-B1], [A2-B2], etc. Is there any gap larger than 100 lines between chunks? If so, read it.
- [ ] If the dedup system blocks re-reading because you already read a range earlier in the session, read different lines — the gap you actually missed, not the range you already consumed.
- [ ] **PITFALL — the "I've read enough" illusion:** reading 6 chunks of 200 lines from a 2100-line chapter means you've only read ~57%. You CANNOT write a thorough note on 57% coverage. Longer chapters need 10+ chunks. Count your chunks against the chapter length before assuming you're done.
- [ ] Only proceed to writing once you've verified ≥85% coverage. If you can't, flag the note as partial and note the unread ranges.
- Write the note using the full format above — every claim gets Claim, Evidence, Confidence, Stakes, Disagreement, Alternative, Assessment
- Commit after each substantial note or batch of notes
- **PITFALL — Git with em dashes in filenames:** `git add notes/theology/Author — Chapter Title.md` fails unless the filename is quoted: `git add 'notes/theology/Author — Chapter Title.md'`. The em dash is valid in filenames but confuses shell word-splitting. Always quote filenames containing em dashes or other Unicode punctuation.

### Step 3.5: Periodic retrospective review (MANDATORY)
After every 3-4 chapters (or every major section), pause and review:
- [ ] Compare note sizes: are later chapters getting thinner? If Chapter 1 is 12KB and Chapter 5 is 2KB, you're compressing — go back.
- [ ] Count claims per chapter: are you identifying FEWER claims in later chapters? If you found 5 claims in Ch 1 and only 1 in Ch 4, you're skimming.
- [ ] Check the quality of "what's at stake": are later stakes generic ("this matters for understanding") while early stakes were specific?
- [ ] Verify cross-references: are later chapters still linking to the scholarly directory and other notes?
- [ ] Ask: "If I stopped now and only had these notes, would a reader know what this chapter argues AND whether to believe it?"
- If any check fails: STOP. Go back. Re-read the thin chapters. Fill in what's missing. Do not continue until quality is consistent.

### Step 3.6: Continue reading and writing
- Resume the read → write cycle
- Repeat the retrospective review after the next 3-4 chapters

### Step 3.7: Acceleration via delegate_task (for books with 7+ chapters)

When the book has enough chapters to justify parallelization, use `delegate_task` to dispatch chapters to subagents in batches of 3. This cuts a 10-chapter book from hours to ~30 minutes.

**Preparation:**
- Complete Steps 1-2 first (extract, map structure, split into /tmp files).
- Write the Introduction note yourself to establish the format, tone, and cross-reference baseline that subagents will follow.

**Dispatching:**
- Batch chapters in groups of 3 (max concurrent subagents). Give each subagent:
  - The path to the temp chapter file (e.g., `/tmp/smith_Ch1.txt`).
  - The exact output path in the notes directory.
  - Context with the format requirements, a pointer to the Introduction note as format reference, and a list of scholars to cross-reference.
  - The instruction "Read ENTIRE chapter first" and "Do NOT combine with other chapters."
- Continue working on a chapter yourself while subagents run — do not wait idle.

**PITFALL — subagent quality varies (and can be BETTER):** subagent-written notes are often larger (more claims, more detail). This is because subagents start fresh without session-length fatigue — they can produce RICHER notes than the main agent writing sequentially. In one case, subagent notes for later chapters were 33-34KB (7-8 claims) vs. the main agent's 17-22KB (4-5 claims). During the final retrospective, always compare sibling versions and keep the richer one. Do NOT assume your own version is better just because you wrote it. After all subagents finish, spot-check each note: (1) does the frontmatter match format? (2) are there at least 5 claims? (3) is there a chapter-level assessment table? If a note is suspiciously short, rewrite it yourself or re-dispatch.

**PITFALL — subagent git commit messages:** subagents commit their output with whatever message they generate, which may reference unrelated books or tasks. The files are correctly tracked but the git log will be messy. After the session, verify all files are in git with `git ls-files`.

**PITFALL — cross-session duplicates from prior delegations:** Previous sessions may have already committed notes for the same book under a DIFFERENT naming convention (e.g., "Part I-VII" vs. "Ch I-X"). Before dispatching delegates or writing notes, run `git log --oneline -5` and `ls NOTES_DIR/PREFIX*` to check what already exists. If notes are already committed with different names, decide BEFORE writing: (a) keep existing names and add only missing chapters, (b) rename existing notes to match new convention, or (c) accept naming inconsistency. Do NOT write duplicates and then try to sort it out in the retrospective — that path led to accidentally deleting a self-written note during cleanup.

### Step 4: Quality check
Before considering a chapter done, verify:
- [ ] Every major claim has confidence rating with justification
- [ ] Direct quotes from the text are included
- [ ] Cross-references to other notes exist
- [ ] "What's at stake" is specific — not generic
- [ ] Alternative readings are plausible, not strawmen
- [ ] Assessment is honest about uncertainty

### Step 4.5: Final retrospective (MANDATORY — before declaring the book done)
After completing all chapters, run the full retrospective:
- [ ] Run `scripts/retrospective_metrics.py NOTES_DIR PREFIX` to get automated size/claim/cross-ref counts and a taper check. This catches compression rot that eye inspection might miss.
- [ ] Read back through EVERY note. Are later chapters as detailed as early ones?
- [ ] Compare note sizes across the whole book. If there's a visible taper (early notes 8-15KB, late notes 2-4KB), the taper is real — go back and fill.
- [ ] Count total claims per chapter. Consistent? If not, re-read the thin chapters.
- [ ] Verify that EVERY chapter has at least one cross-reference to another note in the project.
- [ ] Ask: "Could someone who hasn't read this book understand its argument AND evaluate it from my notes alone?" If not, what's missing?
- [ ] Fix deficiencies BEFORE committing that the book is complete.

### Step 5: Cross-cutting
After completing all chapters:
- Add a book-level summary note or section if appropriate
- Update the project index to link to the new notes
- Note where this book's claims interact with other books in the project

---

## Confidence Rating Guide

| Rating | When to Use |
|--------|------------|
| **VERY HIGH** | Publicly verifiable fact (text exists, artifact found, date confirmed) |
| **HIGH** | Strong scholarly consensus, multiple lines of converging evidence |
| **MEDIUM-HIGH** | Good evidence but some reasonable counter-arguments exist |
| **MEDIUM** | Evidence supports the claim but significant alternatives are possible |
| **LOW-MEDIUM** | Claim is plausible but evidence is thin |
| **LOW** | Speculative — the author is reaching |
| **DEBATABLE** | The claim depends entirely on which scholar you ask |

---

## Common Pitfalls

1. **Stenographer mode:** Reporting what the author says without evaluating it. Every claim needs an assessment. If you can't assess it, say so honestly.
2. **Compression rot:** Later chapters get less detail than earlier ones. Check your note sizes — if Chapter 1 got 12KB and Chapter 8 got 2KB, you got lazy. Go back.
3. **Confidence flattening:** Treating all claims with similar weight. Strong claims deserve HIGH; speculative claims deserve LOW. Be willing to say "this is probably wrong."
4. **Missing stakes:** Generic "what's at stake" statements. Every claim should specify what CHANGES for the reader's understanding if it's true or false.
5. **Strawman alternatives:** Offering alternative readings that no serious scholar holds. The alternative should be credible.
6. **No cross-references:** Notes existing in a vacuum. Link to other book notes, to the scholarly directory, to primary sources, to the project index.
7. **Single-note books:** Compressing an entire monograph into one note. Never acceptable for a book being taken seriously. Minimum viable is one note per major section or chapter.
8. **Multi-chapter combining without justification:** The DEFAULT is one note per chapter. If you find yourself thinking "I can cover chapter
s X through Y in one note" — STOP. That's the compression instinct. Combined notes require EXPLICIT justification. "This is faster" is not justification. "The chapters are short and form one argument" CAN be justification — but you must state it explicitly.
9. **Session-length laziness:** As sessions get long, the temptation to compress increases. This is the structural hangup. Counter it by: (a) taking a breath before each chapter, (b) explicitly asking "would I have written the first chapter at this level of detail?", and (c) if the answer is no, re-reading the chapter and writing the note properly. If you catch yourself thinking "I can cover multiple chapters in one note" — STOP. The default is one per chapter. Combining is the exception that requires justification.
10. **Repeated compression across sessions:** When the same book gets compressed across multiple attempts, the skill's safeguards aren't sufficient. Recognize the pattern: if a book needs a REDO, do it in a FRESH session. Don't fix compression in the same session that caused it — the session-length laziness applies to fixes too. **The LAST chapter is the most vulnerable** — session fatigue peaks, the finish line is visible, and the temptation to sprint is strongest. The final chapter of an academic monograph is often the book's argumentative climax (e.g., Smith Ch 10 on Second Isaiah, Römer's conclusion). Writing it at half the detail level of Ch 1 is a structural failure. If you catch yourself thinking "this chapter is more focused, fewer claims is fine" — verify that against the TEXT, not your fatigue. A genuinely focused chapter will still have rich evidence and stakes for its fewer claims; a compressed chapter will have thin evidence and generic stakes.

10. **The "go back and fill" cliff at session end:** The final retrospective may detect compression rot (later notes 2-3x smaller than early ones) right as the session ends, when there is no practical way to re-read and expand thin notes. Do NOT pretend the book is complete. Instead: (a) in the retrospective, explicitly list which notes are thin, (b) note their current sizes vs. the benchmark, (c) record the line number ranges for the under-covered sections from the source text, and (d) flag them for expansion in a follow-up session. A book with known thin notes is an honest work-in-progress; a book silently declared complete with half-sized notes is a quality failure. The handoff should say: "These N notes are solid. These M notes need expansion. Here is where to resume reading." For the general pattern for coordinating work across many independent sessions (progress files, batch sizing, durable state), see the `multi-session-batch-processing` skill.

11. **Sibling subagent file conflicts (delegate_task mode):** When using delegate_task to parallelize chapters, sibling subagents may write to the same output paths as the main agent, producing DUPLICATE files with slightly different names (e.g., `Ch7 — El, Yahweh, and the Original God of IsraEL and the Exodus.md` vs. `Ch7 — El Yahweh and the Original God of Israel.md`). The `write_file` tool warns about sibling modifications, but the warning is easy to miss in a long session. During the final retrospective: (a) run `ls -la NOTES_DIR/PREFIX*` to detect duplicates, (b) compare sizes and claim counts — sibling versions are often LARGER and RICHER because subagents don't suffer session-length fatigue, (c) keep the richer version and delete the compressed one, (d) verify the survivor has correct frontmatter and cross-references. Do NOT assume the main agent's version is better. In practice, subagent notes for Ch7-9 of Smith's Origins were 33-34KB (7-8 claims) vs. the main agent's 17-22KB (4-5 claims) — the subagents won. **Lesson: delegate_task is not just a speed optimization; it is a QUALITY safeguard against session-length compression.** Subagents starting fresh don't have the fatigue that causes the main agent to thin out in later chapters.

12. **Mid-chapter skipping (distinct from compression rot):** You read 5-6 chunks of 200 lines from a 2000+ line chapter and assumed coverage was complete. You read ~60% of the text and missed large sections — especially the middle third, which is neither the exciting opening nor the memorable conclusion. The resulting note will have CLAIMS but will miss entire sub-arguments, key evidence, and transitional reasoning. The note may even look thorough (good claim count, proper format) while being substantively incomplete. This failure is INVISIBLE to the retrospective's size/claim-count checks — the only fix is the MANDATORY COVERAGE CHECK in Step 3. Run it EVERY TIME before writing. If you haven't read at least 85% of the chapter's lines, you cannot write a thorough note. Period. Count your chunks against the chapter length before assuming you're done.

13. **Combined-note format drift:** When combining multiple short subsections, the combined note MUST have: (a) the `note_type: combined`, `combined_sections`, and `justification` frontmatter fields; (b) one `## §X:` header per combined section; (c) `### Claim N:` (h3) for claims within each section; (d) ONE cross-cutting assessment table at the end covering all claims from all combined sections — NOT one per section. The assessment table's "Strongest/Weakest section" fields should reference specific subsections by their § number. Without these conventions, combined notes become visually inconsistent with standalone chapter notes, confusing readers navigating the note collection.

14. **Self-deletion during duplicate cleanup:** When deduplicating notes with similar names (e.g., "Ch I — Starting Point" vs. "Introduction — Starting Point"), it's easy to delete your OWN note instead of the subagent's. The names are similar enough that a quick `rm` based on partial filename matching can hit the wrong file. Before deleting ANY duplicate: (a) verify the exact filename with `ls`, (b) check file sizes — if two files are within 1KB of each other, they may be equivalent, but if they differ by 5KB+ one is richer, (c) open both and compare claim count and first-claim content before choosing which to delete. Never batch-delete duplicates from a list without verifying each file individually.

---

## Example: The Right Level of Detail

**BAD (too compressed):**
```markdown
# Smith — Chapter 3: Yahweh and Asherah

Smith argues Asherah was a cult symbol, not a goddess. The evidence
is from Kuntillet Ajrud. Most scholars disagree. Confidence: MEDIUM.
```

**GOOD (proper detail):**
```markdown
## Claim 1: The asherah was a cult symbol, not the goddess herself

**Smith's claim:** "I am not opposed in theory to the possibility that
Asherah was an Israelite goddess during the monarchy. My chief
objection... is that it has not been demonstrated."

**Evidence presented:** The grammatical ambiguity of 'šrth; the biblical
texts treat the asherah as a wooden pole; the iconographic evidence
is ambiguous.

**Confidence:** LOW. Smith is in the minority even within his own camp.
Dever, Day, Olyan, and Zevit all read the evidence differently.

**What's at stake:** Whether Yahweh had a consort. This is the single
most explosive question in the field. Smith's caution is methodologically
admirable but increasingly looks like motivated skepticism.

**Who disagrees:** Dever (Did God Have a Wife?, Ch V-VI), Römer
(The Invention of God, Ch 9), Day, Olyan, Zevit, Hadley.

**Alternative reading:** The inscriptions clearly pair Yahweh with Asherah.
The possessive suffix on 'šrth is most naturally read as a goddess name.

**My assessment:** After reading Dever's archaeological evidence
(3000+ figurines) and Römer's epigraphic analysis, Smith's position
looks increasingly untenable. I'm convinced: Yahweh had a consort.
```

---

## When to Use This Skill

- User asks to "take notes on this book" or "read this chapter"
- User is building a research project and needs structured critical notes
- User has extracted a book's text and wants to process it chapter by chapter
- ANY domain — theology, history, philosophy, science, politics, etc. The format works for any argumentative or evidence-based book.
- When creating session handoff prompts for the user to process a book in a new session, see `references/session-handoff-prompt.md` for the required template.

## Resources

- `references/examples.md` — worked examples: bad vs. good note quality, compression rot detection, granularity decision-making (40+ short chapters vs. 12 dense chapters)
- `references/large-monograph-strategy.md` — efficient reading strategy for very large monograph extractions (30K+ lines): chunked reading, structure mapping, skipping bibliography blocks, post-hoc patch-based claim insertion
- `scripts/retrospective_metrics.py` — automated quality metrics for the final retrospective: counts claims, sizes, cross-refs per note, detects compression taper

- `references/note-size-benchmarks.md` — concrete size benchmarks from the Truth project: what "thorough" (23-47KB), "solid" (14-20KB), and "compressed" (6-10KB) look like. Use these to calibrate depth during the periodic retrospective.

- `references/chapter-type-calibration.md` — expected note sizes by chapter type (interpretive vs. descriptive vs. characterization). Use this during retrospective review to distinguish legitimate variance from session-fatigue compression.
- `references/claims-extraction-pattern.md` — advanced extension for large research projects (50+ chapter notes): extracting inline claims to standalone Obsidian nodes with typed edges (depends_on, supports, contradicts, challenged_by). Used by the Truth project to build an Argument Dependency Map from ~500 scholarly claims.

## When NOT to Use

- Fiction, poetry, or narrative works where "claims and evidence" format doesn't apply (adapt the format instead)
- Reference works meant for lookup rather than reading (create index notes instead)
- Books the user just wants a quick summary of (use a lighter format)
