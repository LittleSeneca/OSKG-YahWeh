# Elephantine Editions Guide

Which edition to use for what purpose when extracting Elephantine papyri.

## Cowley 1923

*Aramaic Papyri of the Fifth Century B.C.* Oxford: Clarendon Press.

- **Best for:** Quick access to 87 papyri with English translations
- **Availability:** Internet Archive open access + EPUB with OCR text
- **Local files:** `~/Downloads/aramaicpapyrioff00ahikuoft.epub` (IA EPUB), `~/Downloads/Aramaic papyri discovered at Assuan.pdf` (Sayce & Cowley 1906 — earlier edition)
- **Transliteration style:** "Ya'u" (for YHWH), "Bigvai" (for Bagohi), "Waidrang" (for Vidranga), "Nephayan" (for Naphaina)
- **Quirk:** Dated 1923. The IA EPUB has OCR text embedded but with excessive whitespace and some garbled characters. Short substring search patterns work; whole-phrase search doesn't.
- **Contains:** Temple Petition (Papyrus 30, pp. 108-122), Passover Letter (Papyrus 21, pp. 60-65), general introduction with Anat-Bethel analysis

## TAD 1986 (Vol 1)

Porten, B. & Yardeni, A. *Textbook of Aramaic Documents from Ancient Egypt*, Vol. 1: Letters. Winona Lake: Eisenbrauns.

- **Best for:** Scholarly-standard translations with improved readings
- **Availability:** Internet Archive open access + local PDF (26MB)
- **Local file:** `~/Downloads/Porten B., Yardeni A. (eds.) - Textbook of Aramaic Documents from Ancient Egypt... volume I_ Letter - libgen.li.pdf`
- **Transliteration style:** "YHW" (for YHWH), "Bagohi" (not Bigvai), "Vidranga" (not Waidrang), "Naphaina" (not Nephayan)
- **Quirk:** 150 pages. Has both Hebrew/Aramaic script AND English translation on facing pages. The Hebrew script pages are garbled in text extraction; the English pages are clean.
- **Layout:** Aramaic/Hebrew text → English translation → textual notes. Letters numbered by archive (A4.1, A4.2, etc.).

## Porten 1996

Porten, B. *The Elephantine Papyri in English: Three Millennia of Cross-Cultural Continuity and Change.* Leiden: Brill.

- **Best for:** Commentary that synthesizes scholarship Cowley didn't have access to
- **Availability:** Internet Archive open access + local PDF (26MB)
- **Local file:** `~/Downloads/Bezalel Porten - The Elephantine Papyri in English... (1996, BRILL) - libgen.li.pdf`
- **326 pages.** Almost all pages have extractable text (PyMuPDF). Only page 1 is image-based.
- **Contains:** All key letters with introductions, footnotes, and cross-references. The Jedaniah Archive section (pp. 71-85) covers the Passover Letter, Temple Petition, and the response from Bagohi and Delaiah.
- **Critical unique finding (Porten p. 84 n. 15):** The rebuilt Elephantine temple was forbidden from animal sacrifice — only incense and meal-offering were permitted. This detail is absent from Cowley 1923 and only implied in TAD. Porten explicitly confirms it.

## Kraeling 1953

Kraeling, E.G. *The Brooklyn Museum Aramaic Papyri.* Yale.

- **Best for:** The Anani family archive (private legal documents)
- **Availability:** Internet Archive open access
- **Not in local downloads.** The file in Downloads is a journal review, not the book.

## Cowley vs. TAD transliteration comparison

| Element | Cowley 1923 | TAD 1986 |
|---------|------------|----------|
| God's name | "Ya'u" | "YHW" |
| Persian governor | "Waidrang" | "Vidranga" |
| His son | "Nephayan" | "Naphaina" |
| Governor of Judah | "Bigvai" | "Bagohi" |
| Jewish leader | "Yedoniah" | "Jedaniah" |
| "May God seek your welfare" | Opens with plural "gods" | Same formula |

## Which to cite in source notes

- **Cite both** when the translations differ meaningfully
- **Prefer TAD** for transliteration accuracy (it reflects 60+ years of improved readings)
- **Prefer Porten** for commentary and historical synthesis
- **Cowley is the historical baseline** — the edition Smith, Day, Dever, and Cross all used
