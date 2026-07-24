# Extracting Full Text from Monograph PDFs and EPUBs

For the Truth Project and similar research, full-text extraction enables
grep, chunked reading, and citation-level note-taking.

## Requirements

- PyMuPDF (`fitz`) for PDFs — installed in Hermes venv
- `ebooklib` + `html2text` for EPUBs — install as needed:
  ```bash
  ~/.hermes/venv/bin/pip install ebooklib html2text
  ```

## Extraction Script Pattern

The core extraction logic lives at `/tmp/extract_monographs.py` from the
2026-07-22 session. Key design decisions:

- PDFs: iterate pages with `fitz`, extract with `get_text("text")`
- EPUBs: use `ebooklib.read_epub()`, filter for `ITEM_DOCUMENT` (type 9),
  convert HTML to text with `html2text`
- Output: plain `.txt` with page markers for PDFs, clean text for EPUBs
- Mapping: use a dictionary mapping readable names to download filenames
  so the output files have consistent, sortable names

## Storage

- Extract to `sources/books/_fulltext/` — gitignored, local only
- Copyrighted material must NEVER be committed to a public repo
- The reading list and chapter notes are the public-facing artifacts

## Google Books Extraction (gbscraper)

When a book is only available via Google Books preview (no PDF/EPUB in
Downloads), use the `gbscraper` CLI:

```bash
# Install (macOS/Linux)
brew install shloop/tap/google-book-scraper

# Scrape a Google Books URL
gbscraper -f pdf -o ./output_dir "https://books.google.com/books?id=BOOK_ID"

# The binary is named gbscraper (not google-book-scraper)
```

**Pitfall:** The `-f pdf` flag MUST come BEFORE the URL argument. If the URL
is parsed as a format value, the tool errors with "invalid value for
'--format.'" Always: `gbscraper -f pdf -o <dir> <url>`.

**Limitations:** Google Books previews are partial. The scraper gets whatever
pages are publicly accessible — not the full book unless it's fully open
access. For Zevit's 821-page *Religions of Ancient Israel*, this means a
partial text. Note this in the _fulltext filename (e.g., `Zevit_Religions_of_Ancient_Israel_2001_PARTIAL.txt`).

## File Naming Convention

Use consistent, sortable names:
```
AuthorLast_Title_Shorthand_Year.txt
```

Examples:
- `Smith_Early_History_of_God_2002.txt`
- `Cross_Canaanite_Myth_and_Hebrew_Epic_1973.txt`
- `Albertz_History_of_Israelite_Religion_Vol1_1994.txt`

```bash
# Search across all books at once
grep -r "Asherah" sources/books/_fulltext/

# Read a specific chunk
read_file offset=N limit=M sources/books/_fulltext/Smith_Early_History_of_God_2002.txt

# Find chapter boundaries
grep -n "^CHAPTER\|^Introduction\|^Foreword" sources/books/_fulltext/*.txt
```
