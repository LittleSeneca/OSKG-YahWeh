# Book-to-Structured-Notes Workflow

When converting scholarly monographs into Obsidian-linked research notes, follow this pattern.

## Source Setup

1. Books go in `sources/books/_fulltext/` (gitignored — copyright)
2. Filename convention: `Author_Title_Year.txt`
3. Plaintext extraction uses:
   - **PDFs:** `~/.hermes/venv/bin/python3` with `fitz` (PyMuPDF) — `page.get_text("text")`
   - **EPUBs:** `~/.hermes/venv/bin/python3` with `ebooklib` + `html2text` — iterate `book.get_items()`, filter `item.get_type() == 9` for XHTML documents
4. Batch extraction script at `/tmp/extract_monographs.py` is reusable

## Reading and Note-Taking Pattern

### Chunking

- Read in context-window-appropriate chunks (80-150 lines per chunk from the raw text)
- Natural breaks: chapter boundaries, section boundaries within chapters
- Each chunk becomes one Obsidian note

### Note Structure

Every note gets:

```yaml
---
tags:
  - source/book-notes
  - faith/<topic>
  - scholars/<name>
  - truth-project
created: YYYY-MM-DD
source:
  title: "Full Title"
  author: "Author Name"
  chapter: "Chapter Name"
related:
  - "[[Previous Note]]"
  - "[[Next Note]]"
  - "[[../../notes/theology/<relevant-analysis-note>]]"
status: in-progress
---
```

### Content Organization

For each chunk, produce:

1. **Key claims** — what does this chunk argue? Use blockquotes for Smith's actual words
2. **Methodological observations** — how is the author working? What assumptions are visible?
3. **Connections** — how does this relate to other scholars, other debates, our meta-analysis?
4. **Critical assessment** — does the argument hold up? What's missing? What evidence is strongest/weakest?
5. **"Next" pointer** — what's in the next chunk?

### Link Density

- Wikilink to the reading list, the scholarly directory, and the meta-analysis
- Cross-reference other book notes when the same topic appears across multiple monographs
- Link to specific sub-debate notes when the text addresses them directly

### Commit Convention

```
Book notes: Smith Early History of God — [chunk description]

[Brief description of what this chunk covers and the key payoff]
```

## Critical Evaluation Format (Retro-Ready)

When the user requests a retro or quality check, or when notes have been produced in summary mode (reporting what the author says without critical engagement), retrofit notes to this per-claim structure:

### Claim Evaluation Template

For each major claim in a chapter/section:

```markdown
## Claim N: [One-sentence summary of what the author asserts]

**Smith's claim:** [Direct statement of the assertion]

**Evidence presented:** [Specific data — inscriptions, biblical passages, Ugaritic references, not just summary]

**Confidence:** HIGH / MEDIUM / LOW — with one-sentence justification.
- HIGH: multiple independent sources agree; well-established in the field
- MEDIUM: general agreement but significant dissent; or based on secondary sources
- LOW: speculative, based on limited sources, disputed by majority

**What's at stake for faith:** If true, what does this change for someone deconstructing Christianity? Be specific. Don't say "this matters for theology" — say exactly what doctrine or belief it challenges.

**Who disagrees:** Named scholars with wikilinks to the [[../../notes/theology/scholarly-directory-yahweh-origins|scholarly directory]].

**Alternative reading:** Could the same evidence be reasonably interpreted differently? What's the best counter-argument?

**My assessment:** Evaluation — does this hold up? What's the weakest link? What would I need to verify? Flag tensions in the author's own argument.
```

### Cross-Cutting Assessment Table

At the end of each chapter note, add a summary table:

```markdown
## Cross-Cutting Assessment: Chapter N's Overall Strength

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| [Claim name] | HIGH/MED/LOW | [What would falsify this] |
```

### Signs the Notes Need Retrofitting

- Notes read like a faithful summary rather than a critical dialogue
- No explicit confidence ratings on claims
- No "what's at stake for faith" analysis
- Evidence is summarized in prose rather than bulleted by type
- Author's hedges and qualifications are reported but not interrogated
- Notes don't link to the scholarly directory when specific scholars are mentioned

### Volume Tradeoff

The critical format is more compact per claim (less summary prose, more structured evaluation) but produces more total content because the evaluation dimensions force engagement. Expect notes to grow 20-30% when retrofitted but become substantially more useful.

---

## Volume Estimation

A typical 300-page monograph at this pace produces:
- 1-2 framing notes (preface, introduction, methodology)
- 8-15 chapter notes (depending on chapter density)
- ~50-100KB total across all notes

Figure 15-20 notes per book at this pacing.
