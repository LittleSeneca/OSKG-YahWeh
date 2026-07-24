# Primary Source Collection

After reading multiple scholarly monographs, identify the primary sources all authors cite in common — the "canon within the canon."

## Standard Reference Editions

| Collection | Editor | Date | What It Contains |
|-----------|--------|------|------------------|
| ANET | Pritchard | 1969 (3rd ed.) | Classic anthology — all major ANE texts in English. On Internet Archive. |
| COS | Hallo & Younger | 1997-2002 (3 vols.) | Modern replacement for ANET. Better translations. |
| KAI | Donner & Röllig | 1960-64 (5th ed. 2002) | Standard critical edition of NW Semitic inscriptions |
| TAD | Porten & Yardeni | 1986-99 (4 vols.) | Elephantine papyri |
| DJD | Various | 1955-present | Official Qumran publications |

## Core Primary Texts for Yahweh Origins

| Source | Date | Key Content |
|--------|------|-------------|
| Kuntillet Ajrud | c. 800 BCE | "Yhwh of Samaria/Teman and his Asherah" |
| Khirbet el-Qom | c. 700 BCE | "blessed by Yhwh and his Asherah" |
| Deut 32:8-9 + 4QDeut | Poem ~10th c. / MS 1st c. BCE | "sons of God" vs MT "sons of Israel" |
| Soleb Shasu | c. 1370 BCE | Earliest Yhwh attestation — "Shasu of Yhw" |
| Merneptah Stele | c. 1208 BCE | First extra-biblical "Israel" |
| Mesha Stele | c. 840 BCE | First extra-biblical Yhwh after Soleb |
| Tel Dan Stele | c. 840 BCE | "House of David" — only extra-biblical David |
| Elephantine Papyri | 5th c. BCE | Yhwh alongside Anat-Bethel and other deities |

## Collection Method

1. Read the four Tier 1 books (Smith, Römer, Dever, Sommer)
2. Identify which primary sources ALL four cite
3. Search Wikipedia for each inscription's page
4. Extract: reconstructed text, English translation, key epigraphic details, significance
5. Document standard reference editions

## Delegation Pattern

For primary source hunting: delegate to a subagent with browser/terminal tools. The research is parallelizable — each inscription can be researched independently.

```python
delegate_task(tasks=[
  {"goal": "Research and compile primary source texts for Kuntillet Ajrud, Khirbet el-Qom, Deut 32:8-9, Soleb, Merneptah", 
   "toolsets": ["web", "terminal", "browser"]}
])
```

## Storage

Compiled primary sources go in `sources/primary-sources/` in the Truth repo. Individual book fulltext extractions go in `sources/books/_fulltext/` (gitignored).
