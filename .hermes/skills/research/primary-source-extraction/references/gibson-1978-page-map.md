# Gibson 1978: Facing Transliteration Pages

*Canaanite Myths and Legends*, J.C.L. Gibson, 2nd ed. (T&T Clark, 1978). 
Local file: `~/Downloads/[Academic Paperback] Canaanite Myths and Legends{John C. Gibson}(1978, A&C Black){113827716} libgen.li.pdf`

189 pages. The Baal Cycle section runs PDF pages 67-85, extracted as 20 pages, 57KB total text.

## Format

Facing-page format:
- **Left pages (odd):** Ugaritic transliteration with line numbers. Diacritical marks preserved in PyMuPDF extraction: ṯ, š, ḫ, ġ, ṭ, ṣ, ḏ, ẓ.
- **Right pages (even):** English translation with footnotes and commentary.

## Baal Cycle section map

| PDF page | Book section | Content |
|----------|-------------|---------|
| 67 | Palace of Baal (3 A) | Banquet scene, Pidray/Tallay daughters |
| 68 | Palace of Baal (3 A,B) | Anat's violence: heads on waist, blood on knees |
| 69-71 | Palace of Baal (3 C,D) | Anat travels to Baal on Zephon |
| 72-73 | Palace of Baal (3 D) | **"Rider on the clouds"** (rkb 'rpt) — facing pages with transliteration |
| 74-75 | Palace of Baal (3 D,E) | Anat's threat to El; English translation: "I shall drag him like a lamb" |
| 76-85 | Palace of Baal continued | Remaining Baal Cycle sections |

## Key Ugaritic phrases extracted

All diacritics preserved:

| Ugaritic | Translation | Gibson page |
|----------|-------------|-------------|
| `frt l rkb 'rpt` | "What foe against the Rider on the Clouds?" | 45-46 |
| `yt'dd.rkb.'rpt` | "The Rider on the Clouds testifies" | 73 |
| `btk phr bn ilm` | "in the assembly of the sons of El" | 73 |
| `lmhšt mdd il ym` | "Did I not destroy Yam the darling of El?" | 45-46 |
| `btn 'qltn` | "the wriggling serpent" | 45-46 |
| `šlyt d šb't rašm` | "the tyrant with seven heads" | 45-46 |

## Extraction approach

PyMuPDF extracts clean text from Gibson even though `pdftotext` returns nothing. Always test with fitz first:

```bash
~/.hermes/venv/bin/python3 -c "
import fitz
doc = fitz.open('gibson.pdf')
print(doc[70].get_text())  # page 71 — English translation
print(doc[71].get_text())  # page 72 — Ugaritic transliteration
"
```
