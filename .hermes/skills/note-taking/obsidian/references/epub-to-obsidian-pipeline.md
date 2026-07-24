# EPUB/PDF to Obsidian Study Vault Pipeline

Full pipeline for converting textbooks and reference documents into structured, tagged, cross-referenced Obsidian study vaults.

## EPUB Extraction

### Extract chapter text from EPUB
```python
import zipfile
from html.parser import HTMLParser

class ChapterExtractor(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # CRITICAL: do NOT skip <header> — Wiley/Sybex EPUBs use it to wrap section headings
        if tag in ('script', 'style', 'nav'):  # 'header' intentionally excluded
            self.skip_content = True
        if tag in ('h1','h2','h3','h4','h5','h6'):
            self._flush()
            self.output.append(f'\n{"#" * int(tag[1])} ')
        # ... etc

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'nav'):
            self.skip_content = False
        if tag in ('h1','h2','h3','h4','h5','h6'):
            self._flush()
            self.output.append('\n')
```

**Pitfall:** `<header>` in academic EPUBs wraps content headings, unlike web HTML where it's navigation. Putting `'header'` in the skip list silently drops all heading text.

### Verify extraction quality
After extraction, grep for known heading text to confirm it survived:
```bash
grep "Types of AI" extracted/ch01.txt
```

## PDF Extraction

Use PyMuPDF (fitz) — installed in the Hermes venv:
```bash
~/.hermes/venv/bin/python3 -c "
import fitz
doc = fitz.open('document.pdf')
text = ''
for p in doc: text += p.get_text()
doc.close()
print(f'{len(text):,} chars')
"
```

**Pitfall:** Default `python3` (3.11) does not have `fitz`. Always use `~/.hermes/venv/bin/python3` (3.14) which has PyMuPDF pre-installed. Do NOT use `pip install pymupdf` on the default Python.

### Quick PDF text check
```python
import fitz
doc = fitz.open('doc.pdf')
# Check first 5 pages for extractability
for i in range(min(5, len(doc))):
    chars = len(doc[i].get_text())
    avg = chars // max(1, len(doc))
has_text = 'TEXT' if avg > 100 else ('SCANNED' if avg < 20 else 'LOW_TEXT')
```

## LLM Restructuring into Markdown

### Chapter note template
```yaml
---
tags:
  - domain/xxx
  - type/chapter
created: YYYY-MM-DD
domain: "I: Description"
subdomain: "I.A: Description"
related:
  - "[[Part Index]]"
  - "[[Adjacent Chapter]]"
  - "[[Exam Questions]]"
---
```

### Content structure
1. Performance Indicators (from BOK)
2. Structured content with markdown tables
3. Callout boxes: `> **Note:**`, `> **Exam note:**`, `> **Key insight:**`
4. Exam Essentials (bullet summary)
5. Key Terms with `[[wikilinks]]`

### Parallel processing
Use `delegate_task` with 3 subagents per batch, each processing one chapter:
- Provide the raw extracted text path
- Provide a reference template (processed Chapter 1)
- Provide the exact output path with absolute vault path
- Each subagent needs: `["terminal", "file"]` toolsets

## Exam Question Extraction

### From chapter review sections
Questions appear at end of chapters under `## Review Questions`. Pattern:
- Question line ends with `?` or `:`
- 4 option lines follow, each starting with `- **A.**`
- Answer and explanation follow

Parse with regex:
```python
q_pattern = r'### Q(\d+)\.(\d+): (.+?)\n\n((?:- \*\*[A-D]\.\*\* .+?\n)+)(?:\n> \*\*Answer: ([A-D])\*\* — (.+?))?'
```

### From external PDF question banks
PDFs with format: `Question N [Difficulty]\n...text...\nA) ...\nB) ...\nCorrect Answer: X\nExplanation: ...`

Parse by splitting on `Question \d+ \[(Easy|Medium|Hard)\]` markers.

**Pitfall:** External PDF question banks may use different chapter numbering than the Sybex guide. Always map to exam domains by question number ranges rather than chapter labels.

### Clean option text of answer markers
Strip `✅` emoji from option text during extraction to avoid spoiling answers:
```python
text = re.sub(r'\s*✅\s*', '', text)
```

## Canvas Mind Map Generation

Generate `.canvas` JSON programmatically:
```python
canvas = {"nodes": [...], "edges": [...]}
with open('Canvas/Master Mind Map.canvas', 'w') as f:
    json.dump(canvas, f, indent=2)
```

### Node color conventions for study maps
| Color | Canvas ID | Use |
|-------|-----------|-----|
| Red | `"1"` | Root node |
| Orange | `"2"` | Domains/Parts |
| Yellow | `"3"` | Chapters |
| Green | `"4"` | Concepts, legislation |
| Cyan | `"5"` | Exam resources |
| Purple | `"6"` | Standards, frameworks |

For each node pointing to a vault file, use absolute path in `file` field for click-through.

### Cross-reference structure
Link related documents:
- Legislation ↔ chapters (e.g., EU AI Act ↔ Ch 6)
- Frameworks ↔ frameworks (e.g., NIST RMF ↔ NIST ARIA)
- Standards ↔ legislation (e.g., ISO 42001 ↔ EU AI Act)

## Vault Organization

```
Study Vault/
├── Study Index.md           ← master index with tag reference
├── Body of Knowledge.md     ← exam blueprint
├── Part I - Domain/
│   ├── Part I Index.md
│   └── Ch N - Topic.md
├── Part II - Domain/
│   └── ...
├── Legislation/
│   ├── EU AI Act — Key Provisions.md
│   └── GDPR — AI Provisions.md
├── Standards/
│   ├── NIST AI RMF.md
│   ├── ISO 42001.md
│   └── ...
├── Exam Questions/
│   ├── Chapter Review Qs.md
│   └── External Practice Qs.md
└── Canvas/
    └── Master Mind Map.canvas
```

### Tag hierarchy for study vaults
```
domain/I, domain/II, domain/III, domain/IV  ← exam domains
chapter                                       ← chapter notes
reference                                     ← legislation, standards
legal, privacy                                ← legal documents
standards, nist, iso, oecd                   ← framework docs
exam, questions                               ← question banks
index, master                                 ← navigation notes
bok                                           ← body of knowledge
```
