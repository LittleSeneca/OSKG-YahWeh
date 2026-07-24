---
name: scholarly-book-notes
description: "Take critical, evaluative notes on scholarly monographs — not summaries, not stenography. Every claim gets evidence, confidence, stakes, counter-positions, and assessment."
version: 1.2.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [note-taking, research, reading, scholarship]
---

# Scholarly Book Notes

Take notes that **evaluate, not just report.** The goal is to produce notes a reader can use to assess whether a claim holds up, not just to know what the author said.

## Trigger

- User asks to read/work through a scholarly monograph
- User asks for "book notes" on academic/scholarly work
- Continuing a multi-session reading project (e.g., Truth Project)

## The Critical Format

Every major claim gets these seven elements:

```
## Claim X: [One-sentence summary]

**Author's claim:** One sentence.

**Evidence presented:** Specific data — inscriptions, biblical passages,
archaeological finds, Ugaritic text references. Traceable to source.

**Confidence:** HIGH / MEDIUM / LOW — with one-sentence justification.

**What's at stake for faith:** If true, what changes? Be specific.

**Who disagrees:** Named scholars, linked to directory if available.

**Alternative reading:** How could the same evidence be read differently?

**My assessment:** Does this hold up? What's the weakest link?
```

## Patterns

### Cross-cutting assessment table per chapter

```
| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
```

### Flag the existential threat

Identify the single claim that, if false, would most damage the chapter's argument.

### Flag author's blind spots

Asymmetric method use, treating "shared culture" as "shared religion," making ambitious claims after acknowledging fragmentary evidence.

### Cross-reference to scholarly directory

Link to directory entries and meta-analysis. Don't let notes exist in a vacuum.

## What NOT to Do

- **Be a stenographer.** Evaluate, don't just summarize.
- **Flatten confidence.** Distinguish consensus from speculation.
- **Skip the stakes.** Every claim → "what does this mean for faith?"
- **Be economical.** Depth over brevity. Include specific inscriptions, citations.
- **Compress a multi-Part book into 2 notes.** Books organized in Parts (e.g., Heiser's 8 Parts, 40+ chapters; Cross's 3 Parts of essays) still get ONE NOTE PER PART. The user's rule: "chapter by chapter, subject by subject making notes." For Part-organized books, each Part IS the chapter-equivalent subject unit. The smell test: if book 1 got 8 notes and book 7 got 2, something collapsed.

### Parts-vs-Chapters: Choosing the Right Granularity

| Book Structure | Note Granularity | Example |
|---------------|-----------------|---------|
| Narrative chapters (7-12 chapters) | One note per chapter | Smith, Römer, Dever |
| Short monograph (2 chapters + conclusions + appendices) | One note per section | Tigay: Introduction, Ch I, Ch II+Conclusions = 3 notes |
| Multi-Part popular book (8 Parts, 40+ chapters) | One note per Part | Heiser: 7 notes for 8 Parts |
| Essay collection (3 Parts + multiple chapters each) | One note per major section/essay | Cross: 2 notes for 3 Parts |
| Dense academic (6 chapters + appendix) | One note per chapter | Sommer: Introduction + 6 chapters + Appendix = 8 notes |

## Obsidian Frontmatter

```yaml
---
tags: [source/book-notes, faith/yahweh, scholars/author-name, truth-project]
created: YYYY-MM-DD
confidence: medium
source:
  title: "Book Title"
  author: "Author Name"
  year: YYYY
  publisher: "Publisher"
  local_file: "sources/books/_fulltext/Author_Book_Year.txt"
related:
  - "[[Previous Chapter]]"
  - "[[../../notes/theology/scholarly-directory-yahweh-origins]]"
---
```

### Note Naming Convention

Use consistent filenames:
```
Author — Chapter X — Descriptive Title.md
```

Examples:
- `Smith Chapter 0 — Introduction.md`
- `Romer — Chapter 2 — Geographic Origin.md`
- `Dever — Chapter V — Archaeological Evidence.md`

For multi-chapter consolidated notes (avoid when possible):
```
Author — Chapters X-Y — Combined Title.md
```

Never use the old consolidated format (`Author — Introduction and Chapter 1.md`, `Author — Chapters 2-3 — Geographic Origin and Moses.md`) unless the chapters genuinely form a single argument unit. One note per chapter is the standard; combining chapters is a quality-collapse signal.

## Reading from Extracted Fulltext

Books in `sources/books/_fulltext/` (gitignored). Find chapters with:

```
grep -n "CHAPTER\|chapter title keywords" file.txt
```

Read 100-200 lines at a time. Chapter page headers repeat — first occurrence after TOC is the real start.

## Methodological Assessment

After introduction/preface:

```
| Strength | Weakness |
|----------|----------|
| Acknowledges fragmentary evidence | Builds models from 'barely enough' |
```

## Book Completion Summary

Table: chapters, notes, sizes, verdict in 2-3 sentences, pointer to next book.

## Multi-Book Reading Order and Synthesis

Read evidence-dense first (Smith), then narrative (Römer), then archaeological (Dever), then counter-position (Sommer).

Cross-author comparison tables at end of each book:

```
| Issue | Author A | Author B | My Current Assessment |
|-------|----------|----------|----------------------|
```

Cumulative assessment: update previous assessments after each book.

## The Quality Audit

When user asks "do a retro on quality," audit: source accuracy, evidence specificity, value propositions, utility. Identify deficiencies honestly and propose fixes.

---

## QUALITY ENDURANCE — THE MOST CRITICAL PATTERN

**After finishing the first book with full rigor, there is an almost irresistible tendency to speed up.** The agent combines chapters, skims text, writes summaries instead of evaluations, produces "book reports" instead of critical analyses.

### Warning signs (stop immediately):

- Fewer notes than chapters (Book 1: 8 notes / 7 chapters → Book 2: 5 notes / 12 chapters = COLLAPSED)
- Combining chapters into consolidated notes
- Fewer direct quotes, more paraphrasing
- Thinner evidence sections, missing confidence ratings

### The checkpoint rule:

After Chapter 3 of any book: count notes vs. chapters (or notes vs. Parts for Part-organized books). If ratio worse than 1:1, **stop and retrofit immediately.** Do not continue.

For Part-organized books: count Parts, not chapters. Heiser's 40 chapters in 8 Parts = aim for 7-8 notes. The rule scales: if Part count > notes created, you're compressing. Stop and redo.

### When user catches the collapse:

1. **Acknowledge honestly.** "You're right — I got faster and lazier."
2. **Identify the pattern.** Name what changed.
3. **Propose the retrofit.** Chapter by chapter, same format as book 1.
4. **Execute.** Read each chapter fresh from the fulltext file.

---

## Retrofit Mode

When told to redo notes: read chapter from fulltext → write new note with full format → delete old consolidated note → cross-reference → commit per chapter.

### Retrofit quality standard:

- Evidence-rich: specific inscriptions, biblical passages, archaeological finds
- Directly quoted: multiple blockquotes from the author
- Evaluated: confidence rating with justification for every claim
- Connected: links to scholarly directory, meta-analysis, other books
- Grounded: explicit faith stakes for every major claim

### Speed trap warning:

Retrofitting a 12-chapter book takes a full session. Don't rush. "DO NOT RUSH IT." One book done right is better than three skimmed.

---

## Advanced Analytical Moves

### The "single biggest threat" to an argument

For each chapter or book: identify the ONE claim or scholar that, if correct, would most damage the author's case. Examples:
- For Smith Ch. 1: Schmid's late dating of the Pentateuch → if texts are Persian-period, Smith's Judges-period reconstruction collapses
- For Römer's Kenite hypothesis: if the Jethro narrative is late literary artifice, the bridge from Soleb to Israel vanishes

### Evaluating candidate theories

When an author evaluates multiple proposed explanations (etymologies, origins, interpretations), use a comparison table:

```
| Theory | Meaning | Author's Verdict | My Assessment |
|--------|---------|-----------------|---------------|
| From h-y-h | "I am" | Theological, not historical | Plausible rejection |
| From h-w-y | "He blows" — storm god | PREFERRED | Speculative; 5 theories, none provable |
```

Note when an author honestly flags that their PREFERRED theory has LOW confidence.

### Genre-voice analysis

Every scholarly author has a genre and a voice. Identify it:
- **Smith**: Cautious text critic. "The evidence is barely sufficient." Operates within a hair's breadth of uncertainty.
- **Romer**: Narrative historian. Accessible, confident, lets the story carry the argument.
- **Dever**: Polemicist. Writing to persuade. "More engaging but requires most careful scrutiny."
- **Sommer**: Theological reframer. Accepts the data, challenges the interpretive framework.
- **Tigay**: Empirical challenger. Short, data-driven, methodologically careful. "The numbers speak for themselves" — but he's honest about what they DON'T prove.
- **Cross**: Philological foundation-layer. Dense, technical, establishing the linguistic and mythological groundwork everyone else builds on. Reads like a dissertation series — heavy on Ugaritic parallels and comparative Semitics.
- **Heiser**: Evangelical reconstructor. Popular level (40+ short chapters in 8 Parts). Accepts critical DATA (divine council, multiple elohim, original "sons of God" reading in Deut 32) but rejects critical INTERPRETATION (this does not equal polytheism). Uses critical tools to defend orthodoxy. Voice: accessible, passionate, sometimes polemical. His framework is the strongest evangelical counter-position — methodologically sophisticated but depends on a single hinge claim (Elyon=Yahweh in Deut 32:8-9).

### Cumulative cross-book synthesis

After each book, update a running cross-author assessment:

```
| Issue | Smith | Römer | Dever | Sommer | My Assessment |
|-------|-------|-------|-------|--------|---------------|
| Yhwh had a consort? | NO (symbol) | YES (goddess) | YES (goddess) | — | HIGH — Smith is probably wrong |
```

This prevents the most-recently-read author from seeming the most persuasive.

### Cross-reference sourcing — finding the canon within the canon

After completing multiple books, identify which primary and secondary sources all the books cite in common. This reveals the "canon within the canon" — the evidence the entire field agrees is central.

**Technique:** Run grep across completed notes to tally commonly cited scholars and works:

```bash
cd notes/theology
grep -ohE '(Zevit|Cross|Tigay|Keel|Uehlinger|...)' Smith*.md Romer*.md Dever*.md Sommer*.md | sort | uniq -c | sort -rn
```

Then:
1. Map which scholars are cited by ALL four authors → the foundational consensus
2. Map which are cited by 3 of 4 → the near-consensus
3. Map which are cited by only 1 → the distinctive influences
4. Identify primary sources (inscriptions, texts) cited by all → the evidentiary core

Use this to:
- Build an acquisition list for missing books
- Verify whether scholars are fairly representing commonly-cited sources
- Identify the specific primary evidence the entire debate turns on

### The "surprising concession" flag

When an author admits something that works AGAINST their own position:
- Smith acknowledging his evidence is "barely enough" for the Judges period
- Römer admitting five competing etymologies with no consensus
- Dever acknowledging the two-religions distinction is heuristic, not absolute

These are the most credible moments in any scholarly work. Highlight them.

## Pitfalls

- **Accepting the author's framing uncritically.** Flag loaded terminology.
- **Missing humility/conclusion tension.** Author says "evidence is fragmentary" then builds detailed models — flag it.
- **Not cross-referencing.** Link to directory, meta-analysis, other books.
- **Quality collapse across long sessions.** Treat each chapter as a fresh task.
- **Last-book collapse — within a single session.** After retrofitting multiple books in one session, the LAST book is the most vulnerable to compression. The agent is tired, the user is eager to finish, and the counter-position book (e.g., Sommer, 8 sections) gets 3 notes — precisely when it needs the most thorough treatment. Rule: the counter-position deserves EQUAL OR GREATER rigor than the consensus books, not less.
- **End-of-session quality collapse.** After 6+ books in a session, the agent's quality control degrades. Books 6-7 get compressed (Heiser: 8 Parts collapsed to 2 notes). The symptom: the agent notices a book has many chapters and mentally rounds down. Rule for books 5+ in a session: perform an explicit quality self-check before every note. Ask: Am I about to compress multiple chapters into one note? Why?
- **"Text already loaded" trap.** Read fresh for each chapter.
- **"Last book was easy" complacency.** Every book demands the same engagement.
- **Deference to the author.** Use cross-author comparisons; don't let the current author seem more persuasive by default.
- **Asymmetric method critique.** Flag when the author applies a standard to opponents they don't apply to themselves. Example: Smith dismisses Tigay's YHWH-name data as not proving monotheism, but uses ABSENCE of Asherah-names as evidence she wasn't worshipped — same method, opposite treatment.
- **Missing the author's distinctive voice.** Every author has tells. A note that doesn't capture voice flattens the scholarly landscape.
- **"Single mega-note" trap for short books.** Short monographs (like Tigay, 261KB) still get chapter-by-chapter treatment. The user's instruction: "you are supposed to go chapter by chapter, subject by subject making notes." A book with 4 sections gets 3-4 notes, not 1. If you catch yourself writing one mega-note, STOP, delete it, and do it properly. Same applies to dense multi-essay collections like Cross — each major section gets its own note.
- **write_file truncation on large content.** When a note exceeds ~5KB, model output may truncate. Workaround: create a minimal stub with write_file (just frontmatter + placeholder), then use `patch` mode=replace to fill in the body. Or write in segments using `patch`. First confirmed with Tigay notes where write_file cut content at 224 bytes.
