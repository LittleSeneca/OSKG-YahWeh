---
name: primary-source-extraction
description: "Extract translated texts from academic PDFs/EPUBs (Internet Archive, LibGen) using vision models and OCR, and from Wikipedia for shorter inscriptions — compile into Truth Project primary source notes with cross-links and bibliographies."
version: 1.0.0
author: agent-created
platforms: [macos]
metadata:
  hermes:
    tags: [research, extraction, vision, ocr, truth-project]
    related: [obsidian, scholarly-research]
---

# Primary Source Extraction

Extract translated ancient texts from scanned academic books for the Truth Project primary source archive. Covers the full pipeline: finding books, checking extractability, vision-based reading, and compiling source notes.

## Trigger

When the user mentions extracting texts from academic books, downloading from LibGen/IA, or adding to `sources/primary-sources/` in the Truth Project.

## Workflow

### 0. Wikipedia Extraction (fastest — for short inscriptions)

For ANE inscriptions under ~10 lines (Ekron, Siloam, Gezer, Kurkh Monolith, Black Obelisk), Wikipedia has complete translations. Use this before any other method:

**Via browser_console (quick):**
```javascript
document.querySelector('#bodyContent')?.innerText?.substring(N, M)
```

**Via Wikipedia API (batch):**
```bash
curl -s "https://en.wikipedia.org/w/api.php?action=query&titles=PAGE_NAME&prop=extracts&exlimit=1&explaintext=1&format=json&redirects=1"
```

**Via execute_code (batch multiple):** Use `terminal()` to curl the API, parse JSON, extract the translation section by searching for "Translation" in the extract text.

Wikipedia pages that have complete translations ready to extract:
- Ekron inscription, Siloam inscription, Gezer calendar
- Kurkh Monoliths, Black Obelisk of Shalmaneser III
- Lachish letters, Mesha Stele, Tel Dan stele, Ketef Hinnom scrolls

### 1. Finding Books

**Internet Archive (open access):**
```bash
curl -s "https://archive.org/advancedsearch.php?q=title%3A%22Book+Title%22+AND+creator%3AAuthor&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=10"
```
Open access books can be downloaded directly. Restricted books show "Borrow Unavailable."

**Internet Archive (restricted):** Try the `/details/` page in the browser. Some books allow borrowing; others are print-disabled only.

**Anna's Archive:** `annas-archive.cc` — requires login to see results. Not useful for unauthenticated search.

**LibGen:** User handles downloads. Check `~/Downloads/` for new `.pdf`/`.epub`/`.crdownload` files.

### 2. Check Extractability

**EPUBs (zipfile):**
```python
import zipfile
z = zipfile.ZipFile(epub_path)
# Check for HTML files with text
html_files = [n for n in z.namelist() if n.endswith(('.xhtml','.html'))]
# If only PNG/JPEG: image-based, needs vision
# If HTML with substantial text: extractable
```

**PDFs (PyMuPDF — use Hermes venv):**
```bash
~/.hermes/venv/bin/python3 -c "
import fitz
doc = fitz.open('book.pdf')
for i in range(min(5, len(doc))):
    t = doc[i].get_text()
    if t.strip():
        print(f'p.{i+1}: HAS TEXT ({len(t)} chars)')
    else:
        print(f'p.{i+1}: NO TEXT — image-based')
"
```
PyMuPDF is installed in `~/.hermes/venv/bin/python3` (NOT the default `python3`).

### 3. Extract Text

**For extractable PDFs:**
```bash
~/.hermes/venv/bin/python3 -c "
import fitz
doc = fitz.open('book.pdf')
t = doc[PAGE_NUM].get_text()
print(t)
"
```

**For EPUBs with HTML text:**
```python
import zipfile, re
z = zipfile.ZipFile(epub_path)
for name in z.namelist():
    if name.endswith('.html') and 'notice' not in name.lower():
        text = z.read(name).decode('utf-8', errors='ignore')
        clean = re.sub(r'<[^>]+>', ' ', text)
        clean = re.sub(r'\s+', ' ', clean).strip()
        if len(clean) > 200:
            print(clean)
```

### 4. Vision-Based Extraction (for image-based books)

When PDFs/EPUBs are image-only (no embedded text), use DeepSeek vision:

**Extract page images from PDF (PyMuPDF):**
```bash
~/.hermes/venv/bin/python3 -c "
import fitz
doc = fitz.open('book.pdf')
for i in range(START, END):
    pix = doc[i].get_pixmap(dpi=200)
    pix.save(f'/tmp/pages/page_{i+1:03d}.png')
"
```

**Extract page images from EPUB (zipfile):**
```python
import zipfile
z = zipfile.ZipFile(epub_path)
for name in z.namelist():
    if name.endswith('.png') or name.endswith('.jpg'):
        z.extract(name, path='/tmp/extracted/')
```

**Map the book structure FIRST.** Do not extract blindly. Extract sample pages at regular intervals (every 10-20 pages) and use vision_analyze to identify:
- Title page, table of contents, introduction
- Where each chapter/text begins
- Page numbering offset (EPUB image numbers often don't match book page numbers)

**Target specific passages.** Once you know the structure, feed only the pages containing the desired text to vision_analyze. Prompt format:

> "Read the English translation column. What heading, book page number, and section is this? Read all visible translated text."

**Key principle:** Vision extraction is for ~20-40 targeted pages, not whole books. Use text extraction for the bulk; vision for image-based pages with diacritical marks or mixed scripts.

### 5. Compile Source Notes

Output goes to `~/Projects/Personal/Truth/sources/primary-sources/<source-name>.md`.

Format follows the established pattern (see `key-inscriptions.md`):
- Location, Date, Discovery, Medium, Script, Present location, Standard reference
- Overview (2-3 paragraphs)
- Actual translated texts with section headings
- Key features
- Significance for the Truth Project
- Bibliography with Internet Archive links

When two translations exist (e.g., Cowley 1923 vs. TAD 1986), include a comparison table showing transliteration differences.

### 6. Update the Audit

After extraction, patch `missing-sources-audit.md` with acquisition links and status changes.

## Pitfalls

1. **EPUB page numbering is offset.** Image files like `index-100_1.png` don't match book page 100. Always verify by checking a few pages with vision_analyze first. The offset for Parker 1997 was EPUB # ≈ book page # + 16.

2. **qlmanage only extracts one page.** Use PyMuPDF for multi-page PDF image extraction, not macOS qlmanage.

3. **Anna's Archive requires login.** Books that show "0+" results may be available but hidden behind the login wall.

4. **IA restricted books may be borrowable.** Check the `/details/` page in the browser — some restricted books allow 1-hour borrowing.

5. **Diacritical marks survive in PyMuPDF text extraction.** Gibson 1978's transliteration pages preserved ṯ, š, ḫ, ġ, ṭ, ṣ in extracted text — no vision needed for those pages.

6. **Cowley EPUB OCR is rough.** The IA-generated EPUB has OCR text but with excessive whitespace and some garbled characters. Search with short substring patterns, not whole phrases.

7. **Gibson 1978 has extractable transliteration.** Even though `pdftotext` returns nothing, PyMuPDF (`fitz`) extracts clean text with preserved diacritical marks (ṯ, š, ḫ, ġ, ṭ, ṣ). Always test fitz before assuming a PDF needs vision extraction.

8. **Smith 1994 Vol 1 (Brill) has embedded translation in commentary.** The 535-page volume doesn't have standalone translation pages. The English translations of KTU 1.1-1.2 are scattered through the introduction and commentary sections, not in a bilingual column format. Use Gibson or Parker for quick translation extraction; use Smith for the definitive scholarly commentary.

9. **Porten 1996 has information Cowley and TAD lack.** The critical finding about the animal sacrifice ban at the rebuilt Elephantine temple came from Porten's commentary (p. 84 n. 15), not from the translation text itself. Always check Porten's notes and commentary in addition to the translations — he consolidates scholarship Cowley didn't have access to in 1923.

10. **Smith & Pitard 2009 IS Vol 2.** The file `Mark S. Smith, Wayne T. Pitard - The Ugaritic Baal Cycle (2009, Brill).pdf` (904 pages, 3MB) is Volume 2 covering KTU 1.3-1.4. Despite being only 3MB (vs. Vol 1's 59MB), it has full extractable text. The title page confirms: "The Ugaritic Baal Cycle, Volume II, Introduction with Text, Translation and Commentary of KTU/CAT 1.3-1.4." Use this for the Baal's Palace and divine council sections.

11. **Check Downloads first.** Before searching Internet Archive or Anna's Archive, always check `~/Downloads/` for local PDFs and EPUBs the user may have already downloaded from LibGen. Use `ls -lt ~/Downloads/ | head -20` to see recently added files.

12. **Wikipedia is the fastest path for short inscriptions.** For ANE inscriptions under ~10 lines (Ekron, Siloam, Gezer, Kurkh, Black Obelisk), Wikipedia has complete translations. Use `browser_console` with `document.querySelector('#bodyContent')?.innerText` or the Wikipedia API (`action=query&prop=extracts&explaintext=1`) to grab them in seconds. Don't use vision extraction for sources Wikipedia already covers.

## Source Note Cross-Linking

Every primary source note must have a `## Related Notes` section with Obsidian wikilinks. Each link should explain WHY the connection matters, not just list related notes:

```markdown
## Related Notes

- [[ugaritic-baal-cycle]] — Anat, the warrior goddess paired with YHWH at Elephantine as Anat-Yahu
- [[key-inscriptions]] — Kuntillet Ajrud: "YHWH and his Asherah" inscriptions from the same period
- [[ketef-hinnom]] — YHWH without consort (contrast with Elephantine polytheism)
```

Also update the top-level `sources/Sources Index.md` to list all source notes in a table with dates, types, and key content summaries.

## Backlinking Claims and Chapter Notes

After creating source notes, add wikilinks FROM the claims and chapter notes BACK to the sources. This is a separate session task:

1. Search `notes/theology/` AND `notes/claims/` for references to each source using the search terms listed below.
2. For each matching note, add a wikilink to the FIRST substantive mention only.
3. Use piped links where the text already names the source: `[[mesha-stele|the Mesha Stele]]`.
4. Be surgical — don't rewrite notes, just add wikilinks.
5. Skip vague references. "Ugaritic texts" or "Elephantine community" is good. "as we saw previously" is not.

**Search terms per source:**

| Source | Search terms |
|--------|-------------|
| Ugaritic Baal Cycle | `Ugarit`, `Ugaritic`, `Baal Cycle`, `KTU`, `Ras Shamra`, `Baal and`, `Canaanite pantheon`, `El and Baal`, `Rider of the Clouds` |
| Elephantine Papyri | `Elephantine`, `Yeb`, `Anat-Yahu`, `Anat-Bethel`, `Passover Letter`, `temple.*Elephantine`, `Jedaniah`, `Yedoniah` |
| Key Inscriptions | `Kuntillet Ajrud`, `Khirbet el-Qom`, `Deut 32:8`, `4QDeut`, `Soleb`, `Merneptah`, `Shasu`, `sons of God.*Deut`, `Elyon.*nations` |
| Lachish Ostraca | `Lachish`, `Lachish letters`, `Hoshaiah`, `Azekah`, `fire signals` |
| Mesha Stele | `Mesha`, `Moabite Stone`, `Chemosh`, `vessels of YHWH`, `Moabite` |
| Tel Dan Stele | `Tel Dan`, `House of David`, `bytdwd`, `Hazael.*stele`, `Biran.*Naveh` |
| Ketef Hinnom | `Ketef Hinnom`, `silver amulet`, `Priestly Blessing.*amulet`, `Barkay.*silver`, `oldest biblical` |

**Prompt for the backlink session is saved at** `~/Projects/Personal/Truth/.hermes/backlink-sources-prompt.md`.

## Reference Files

- `references/parker-1997-page-map.md` — Complete EPUB-to-book-page mapping for Parker 1997 (SBL). KTU 1.1-1.6, all 12 key passages with exact Parker page numbers.
- `references/gibson-1978-page-map.md` — Gibson 1978 facing transliteration pages. Baal Cycle runs PDF pages 67-85. Left pages = Ugaritic transliteration, right pages = English translation.
- `references/elephantine-editions-guide.md` — Cowley 1923 vs. TAD 1986 vs. Porten 1996: which edition to use for which purpose, transliteration differences, and the critical Porten-only finding about the animal sacrifice ban.
