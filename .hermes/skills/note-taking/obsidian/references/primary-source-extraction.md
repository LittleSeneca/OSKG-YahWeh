# Primary Source Extraction from Internet Archive

Pipeline for extracting ancient Near Eastern primary source texts from Internet Archive scanned books into formatted Obsidian source notes. Used by the Truth Project to build the `sources/primary-sources/` collection.

---

## Phase 1: Find the Book

### Search IA advancedsearch API

```bash
curl -s "https://archive.org/advancedsearch.php?q=title%3A%22Exact+Title%22+AND+creator%3AAuthor&fl[]=identifier&fl[]=title&fl[]=year&fl[]=creator&output=json&rows=10" | python3 -m json.tool
```

Key parameters:
- `q=` — Lucene query. Use `title%3A` and `creator%3A` for exact matching. `AND` for multiple terms.
- `fl[]=` — which fields to return. Always include `identifier,title,year`.
- `output=json` — required for machine parsing.
- `rows=` — max results (default 10).

### Example: find Cowley 1923

```bash
curl -s "https://archive.org/advancedsearch.php?q=title%3A%22Aramaic+Papyri+of+the+Fifth+Century%22+AND+creator%3ACowley&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=5"
```

### Check file availability (metadata)

```bash
curl -s "https://archive.org/metadata/[IDENTIFIER]" | python3 -c "
import sys,json; d=json.load(sys.stdin)
for f in d.get('files',[]):
    print(f.get('name','?'), f.get('format','?'), f.get('size','?'))
"
```

Look for:
- `_djvu.txt` — OCR text, best for extraction. Public domain books: freely downloadable. In-copyright books: requires auth (401).
- `.epub` — EPUB format. Same access rules as djvu.txt.
- `.pdf` — PDF. Plain PDFs may work; "LCP Encrypted PDF" requires borrowing.
- `_hocr_searchtext.txt.gz` — alternative OCR text (gzipped).

### Accessibility check

- **Public domain (pre-1928):** Almost always fully accessible — `_djvu.txt`, PDF, EPUB all downloadable without auth. Cowley 1923, Sayce 1906, older editions.
- **In-copyright (post-1928):** Varies. May require IA lending/borrowing. May return 401 on direct download. Check with a curl HEAD request. Gibson 2004, Parker 1997, Coogan 1978 are all restricted.
- **Anna's Archive:** Requires login to see actual results. Unauthenticated searches show "0+" result counts (all hidden). Not useful for programmatic access but good for manual verification that a book exists.

---

## Phase 2: Download and Extract

### Download OCR text (public domain books)

```bash
curl -sL --max-time 60 "https://archive.org/download/[IDENTIFIER]/[IDENTIFIER]_djvu.txt" -o /tmp/book.txt
```

Check result:
```bash
wc -l /tmp/book.txt   # Should be thousands of lines for a real book
wc -c /tmp/book.txt   # Should be hundreds of KB
head -50 /tmp/book.txt  # Verify legible text
```

If the file is 172 bytes (the 401 HTML page), the book is restricted.

### OCR quality expectations

OCR from scanned books has:
- Extra spaces between words (e.g., "temple    of   Ya'u")
- Occasional misread characters (e.g., "Khnub" vs "Khnum", "Ya'u" vs "Yahu")
- Broken line breaks mid-sentence
- Page headers/footers mixed into text

These do NOT prevent extraction. Grep patterns work fine with extra spaces. Read chunks with `read_file` to capture context around matches.

### Search for key passages

```bash
# Broad searches work with OCR noise
grep -ni "temple\|destroy\|sacrifice" /tmp/book.txt | head -30

# Specific terms
grep -ni "Anat\|Anath\|Bethel\|oath\|swear" /tmp/book.txt | head -20

# Find section boundaries (page headers often contain line numbers)
grep -n "ARAMAIC PAPYRI No\|PAPYRI No\." /tmp/book.txt
```

### Read around matches

Once you have line numbers from grep, use `read_file` with `offset` and `limit` to capture the full passage:

```python
# Line 8420 grabbed a match — read 120 lines around it
read_file(path="/tmp/book.txt", offset=8400, limit=120)
```

---

## Phase 3: Compile Source Note

### Format

Follow the established pattern from `key-inscriptions.md`:

```markdown
# Primary Source: [NAME]

**Location:** ...
**Date:** ...
**Discovery:** ...
**Medium:** ...
**Script:** ...
**Standard reference:** ...

---

## Overview

(2-3 paragraph context)

---

## Key Texts

### 1. [Document Name]

**Date:** ...
**Full English Translation (Citation):**

> (Indented blockquote with the actual translation)

---

## Key Features

(numbered list of key terms/observations)

---

## Significance for the Truth Project

(numbered list of why this matters for the Yahweh/monotheism question)

---

## Bibliography

- Standard scholarly edition with IA link
- Accessible translation with IA link
- Wikipedia link
- Museum location
```

### Citations

Always include:
- The Internet Archive link where the text was extracted from
- The standard scholarly edition (KAI, TAD, KTU, etc.)
- The page/line reference within the source book

---

## Complete Example: Elephantine Papyri from Cowley 1923

```bash
# 1. Search
curl -s "https://archive.org/advancedsearch.php?q=title%3A%22Aramaic+Papyri+of+the+Fifth+Century%22+AND+creator%3ACowley&fl[]=identifier&output=json&rows=5"

# 2. Download (public domain, no auth needed)
curl -sL --max-time 60 "https://archive.org/download/aramaicpapyrioff00ahikuoft/aramaicpapyrioff00ahikuoft_djvu.txt" -o /tmp/cowley.txt
# Result: 24,586 lines, 869KB

# 3. Search for key texts
grep -ni "Passover\|unleavened\|feast" /tmp/cowley.txt | head -20     # → line 5374: Papyrus 21
grep -ni "destroy.*temple\|Waidrang\|Yedoniah" /tmp/cowley.txt        # → line 8421: Papyrus 30
grep -ni "Anat\|Anathbethel\|swear.*oath" /tmp/cowley.txt             # → lines 1216-1220

# 4. Read the full passages
read_file(path="/tmp/cowley.txt", offset=5490, limit=90)    # Passover Letter translation
read_file(path="/tmp/cowley.txt", offset=8400, limit=120)   # Temple Petition translation
read_file(path="/tmp/cowley.txt", offset=1210, limit=50)    # Anat-Bethel commentary

# 5. Compile into elephantine-papyri.md
```

---

## Handling Restricted Books

When `_djvu.txt` returns 401 (in-copyright), try:

1. **Check if a public domain edition exists.** Older editions (pre-1928) of the same texts may be available. E.g., Cowley 1923 instead of TAD 1986.
2. **Browser reader may work.** Navigate to the IA details page with the browser — some restricted books allow page-by-page viewing even without direct download.
3. **Synthesize from scholarly consensus.** If the text is well-established (like the Baal Cycle), write the source note from scholarly consensus, citing KTU numbers and linking to the IA editions for reference. Be explicit about what was extracted vs. synthesized.
4. **Anna's Archive** may have the book for download (requires login).
