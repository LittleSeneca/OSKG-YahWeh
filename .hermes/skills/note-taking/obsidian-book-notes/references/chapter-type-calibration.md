# Chapter Type Calibration — Expected Note Sizes

Not all chapters are equally dense. During retrospective review, a taper from 20KB to 12KB CAN be legitimate if the later chapters are structurally different from the early ones. Use this guide to distinguish compression from honest variance.

## Chapter Types and Expected Density

### Type A: Interpretive-Argument Chapters (15-25 KB typical)
These chapters advance the book's central thesis through historical reconstruction, close reading of primary texts, and theoretical argument. Expect 5-8 claims with rich evidence sections, detailed cross-references, and specific "what's at stake."

**Examples:** Lewis Ch4 (El Worship, 23KB/8 claims), Lewis Ch6 (Origin of Yahweh, 19KB/6 claims), Lewis Ch3 (Methodology, 20KB/7 claims).

**Reading strategy:** Read the full chapter in 150-200 line chunks. These chapters are dense throughout — every paragraph may contain an evaluable claim.

### Type B: Descriptive-Survey Chapters (12-17 KB typical)
These chapters survey material culture, iconography, or comparative ancient Near Eastern parallels. They have real claims but fewer of them — much of the text is figure descriptions, catalogue entries, or plot summaries of texts the reader may already know. Expect 4-6 claims.

**Examples:** Lewis Ch5 (El Iconography, 17KB/5 claims), Lewis Ch7 (Yahweh Iconography, 15KB/4 claims).

**Reading strategy:** Use `awk` subsection-structure extraction (see `references/large-monograph-strategy.md`) to identify key argumentative subsections. Skip or skim figure descriptions and catalogue entries. Focus on the methodological sections and the conclusions at the end of each section.

### Type C: Characterization-Application Chapters (10-14 KB typical)
These chapters apply a thematic lens (warrior, king, judge, holy one) to the textual evidence. The argument is cumulative rather than claim-by-claim — the evidence is in the sustained textual survey rather than in discrete, falsifiable assertions. Expect 3-5 claims.

**Examples:** Lewis Ch8 (Warrior & Family God, 11KB/3 claims), Lewis Ch9 (King & Judge, 12KB/4 claims), Lewis Ch10 (Holy One, 10KB/3 claims).

**Reading strategy:** Read the introduction and conclusion carefully — they frame the argument. Skim the middle sections (which are mostly textual survey) for particularly striking or original passages. These chapters are the hardest to compress without losing the argument, because the argument IS the survey. If pressed for time, prioritize one strong claim per subsection.

## Retrospective Calibration

When comparing note sizes across a book, ask:

1. **Are the chapter types consistent?** If all chapters are Type A (interpretive), a taper IS compression. If the book moves from Type A to Type B/C, some taper is expected.
2. **Are the "what's at stake" sections specific?** Generic stakes = compression, regardless of chapter type.
3. **Are direct quotes present?** Absence of textual evidence = compression.
4. **Is the assessment honest about uncertainty?** Generic "this seems right" = compression.

## The Lewis Benchmark (2020)

This session produced the calibration data:

| Chapter | Type | Size | Claims | Assessment |
|---------|------|------|--------|------------|
| Ch1 — Introductory Matters | A | 16KB | 5 | Solid |
| Ch2 — History of Scholarship | A | 20KB | 7 | Dense |
| Ch3 — Methodology | A | 20KB | 7 | Dense |
| Ch4 — El Worship | A | 23KB | 8 | Thorough — longest, best |
| Ch5 — El Iconography | B | 17KB | 5 | Solid for type |
| Ch6 — Origin of Yahweh | A | 19KB | 6 | Solid |
| Ch7 — Yahweh Iconography | B | 15KB | 4 | Solid for type |
| Ch8 — Warrior & Family God | C | 11KB | 3 | Lean — some fatigue, some legitimate |
| Ch9 — King & Judge | C | 12KB | 4 | Lean — some fatigue, some legitimate |
| Ch10 — Holy One | C | 10KB | 3 | Lean — some fatigue, some legitimate |
| Conclusion | — | 7KB | 2 | Appropriate |

**Verdict:** The ~35% taper from Ch1-6 (avg 19KB) to Ch7-10 (avg 12KB) is about 50% fatigue, 50% legitimate chapter-type variance. In a fresh session, Ch8-10 could each support 1-2 more claims with richer evidence sections — but they would never match Ch4's density because the material is structurally different.

**Lesson:** When a book moves from origins/worship chapters to characterization chapters, expect note sizes to decrease. Don't panic at a 35% taper if the later chapters are Type B/C. Do panic if ALL chapters are Type A and the taper is still 35%.
