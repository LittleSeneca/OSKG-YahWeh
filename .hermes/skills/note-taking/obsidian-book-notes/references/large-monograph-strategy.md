# Efficient Reading Strategy for Very Large Monograph Extractions

When a book's full text is 30K+ lines (1MB+) and chapters span 3K-5K lines each, reading every line linearly before writing is impractical. This reference captures a proven strategy used for Albertz's two-volume "History of Israelite Religion" (31K lines, three massive chapters).

## The Strategy

### 1. Map the structure aggressively
```bash
# Find TOC entries
grep -n "^Contents\|^[0-9]\.[0-9]" fulltext.txt | head -50

# Find chapter/section headers in body text
grep -n "^[0-9]\.\s\|^§[0-9]\|^[4-6]\.\s" fulltext.txt

# Confirm chapter boundaries
grep -n "^4\.\s\|^5\.\s\|^6\.\s" fulltext.txt
```

### 2. Read in 200-250 line chunks
For chapters of 3K-5K lines: read 5-8 chunks to cover the chapter. Each chunk takes one `read_file` call.

**Preferred method for large extractions with Unicode filenames:** use `execute_code` + `terminal` with `sed -n 'START,ENDp'` to read targeted line ranges. This avoids two pitfalls: (a) `read_file` cannot resolve filenames containing em dashes or Unicode punctuation common in Truth project paths, and (b) it keeps the agent's context window clear of garbled PDF-extraction artifacts. The pattern:

```python
from hermes_tools import terminal
r = terminal("sed -n '2000,2300p' /tmp/book_ChN.txt")
print(r['output'])
```

When the text has already been split into `/tmp` chapter files (see Step 2 above), `sed` against those temp files is always safe — `/tmp` paths are pure ASCII. For full-chapter ingestion in one pass, `execute_code` with `open().read()` also works, but the chunked `sed` approach is preferred for 3000+ line chapters to manage context-window pressure.

### 3. Identify claims mentally as you read
Don't wait to finish reading — note the argument structure as you go. When you've read ~70-80% of the chapter, you can usually identify the 5-12 major claims.

### 4. Skip bibliography sections
German academic monographs often have massive bibliography sections (50-100 lines of citations) at the start of each subsection. Skip these — they're reference material, not argument.

### 5. Draft the note in one burst after reading
Once you have the chapter's argument structure, write the entire note in a single `write_file` call. This is faster than incremental writes and produces more coherent notes.

### 6. Use `patch` for post-hoc fixes
During the retrospective, use `patch` (not full rewrites) to:
- Add missing claims discovered during review
- Update cross-reference frontmatter
- Renumber claims when inserting new ones

### 7. Track sizes for taper detection
```bash
wc -c notes/theology/Author\ Vol*\ Chapter*.md
```
This gives you immediate visibility into whether later chapters are getting thinner.

### 8. Extract subsection structure within a chapter range\nWhen a chapter is 1,200+ lines and you need to find which subsections to read, use `awk` with a line-range filter to extract only the subsection headers within that chapter:\n```bash\nawk 'NR>=CHAPTER_START && NR<=CHAPTER_END && /^####/ {print NR\":\"$0}' fulltext.txt\n```\nThis gives you a table of contents for the chapter alone, letting you jump to the most important subsections without reading everything linearly. Combine with targeted `read_file` calls at specific line offsets for those subsections. This is especially valuable for iconography chapters (which are mostly figure descriptions) and cosmic warfare surveys (which are mostly plot summary of texts you already know from other books).\n\n## Pitfalls Specific to Large Monographs

- **Bibliography sections look like content.** Don't let the dense citation blocks (lines of "Author, Title, Year, Publisher" format) fool you into thinking you've read substantive argument. Skip them.
- **Chapter introductions summarize the whole chapter.** Read them carefully — they tell you what claims to look for in the subsections.
- **The retrospective is MORE important for large books.** Taper is harder to detect when chapters are huge because even a "thin" chapter at 19KB looks substantial compared to a 2KB note. Compare proportional sizes, not absolute sizes.
- **ASCII-art diagrams in extracted text are noise.** PDF extraction often garbles diagrams into scattered ASCII fragments. Skip these sections — they don't contain readable argument.
