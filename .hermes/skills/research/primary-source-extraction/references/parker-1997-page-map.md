# Parker 1997: EPUB-to-Book Page Mapping

*Ugaritic Narrative Poetry*, ed. Simon B. Parker (Scholars Press, 1997). The Baal Cycle translation is by Mark S. Smith.

The EPUB (34MB, from LibGen) is image-based — every page is a PNG. The file naming is `index-N_1.png` where N is the EPUB image number. The EPUB image number does NOT match the book page number.

## Offset formula

**EPUB image # ≈ book page # + 16**

This offset was verified across multiple pages. It may drift by 1-2 pages at the extremes.

## Book structure

| Book pages | EPUB images | Content |
|------------|-------------|---------|
| 1-9 | 1-25 | Front matter: title pages, map, introduction |
| 10-48 | 26-64 | Kirta (Legend of Keret) |
| 49-80 | 65-96 | Aqhat (Tale of Aqhat) |
| 81-87 | 97-103 | Baal Cycle introduction (commentary by Smith) |
| 88-164 | 104-180 | Baal Cycle translation (KTU 1.1-1.6) |
| 165+ | 181+ | Bibliography, indexes, shorter texts |

## All 12 extracted passages

| # | Passage | KTU | Parker book page | EPUB image |
|---|---------|-----|-----------------|------------|
| 1 | El names Yamm as his son | 1.1.iv | 89 | ~105 |
| 2 | Baal defeats Yamm (Chaoskampf) | 1.2.iv | 104-105 | ~120-121 |
| 3 | Anat threatens El | 1.3.v | 115 | ~131 |
| 4 | Cloudrider in the divine council | 1.4.iii | 124 | ~140 |
| 5 | Warning about Mot | 1.4.viii | 139 | ~155 |
| 6 | Mot's challenge to Baal | 1.5.i | 141 | ~157 |
| 7 | Baal is dead; El mourns | 1.5.vi | 149 | ~165 |
| 8 | Anat confronts Mot | 1.6.ii | 155 | ~171 |
| 9 | Baal returns to life | 1.6.iii | 158 | ~174 |
| 10 | Baal and Mot battle | 1.6.vi | 162 | ~178 |
| 11 | Shapash intervenes — resolution | 1.6.vi | 163 | ~179 |
| 12 | Scribe's colophon (Ilimalku) | — | 164 | ~180 |

## Layout

Each translation page has two columns:
- **Left column:** Ugaritic transliteration (Latin alphabet with diacritics)
- **Right column:** English translation with footnotes

Section headings (e.g., "El's Messengers Go and Speak with Anat") appear in bold in the right column.

## EPUB extraction command

```python
import zipfile
z = zipfile.ZipFile("Ugaritic Narrative Poetry{...} libgen.li.epub")
# Extract all PNGs
for name in z.namelist():
    if name.endswith('.png'):
        z.extract(name, path='/tmp/parker_extracted/')
```
