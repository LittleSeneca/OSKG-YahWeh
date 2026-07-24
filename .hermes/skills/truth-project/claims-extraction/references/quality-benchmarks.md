# Quality Benchmarks for Claim Extraction

Concrete examples of "good" output from session 1 (2026-07-23). Use these to calibrate quality at the midpoint gate.

## Claim File Quality

**Good (smith-ehg-3.1, 5,766 bytes):**
- 5 topic tags, 2 evidence tags — specific, not generic
- Evidence section has 5 bullet points with biblical citations and scholar names
- Edge descriptions name scholars AND arguments: "Römer argues the asherah represented a real goddess transferred from El to Yahweh" not "contradicts the goddess reading"
- Cross-scholar edges to Römer and Day claims
- Assessment preserved verbatim from original chapter note

**Good (romer-inv-9.1, 4,754 bytes):**
- 4 topic tags, 2 evidence tags
- Evidence section has 3 bullet points with specific Ugaritic/Mesopotamian/Arabian attestations
- Edges to Smith and Day claims with specific descriptions
- Primary sources section lists actual text references (KTU² 1.4, KTU² 1.15)

**Good (day-ygc-2.2, 5,268 bytes):**
- Detailed reply to Bernhardt's critique preserved (3 objections with Day's counters)
- Edges to both Smith and Römer claims
- Primary sources list specific text references + ANEP plate numbers

## Warning Signs of Compression

If you see these at the midpoint gate, STOP:

- Evidence section is one paragraph instead of bullet points/tables
- Edge descriptions are "supports the Asherah thesis" instead of named scholar + specific argument
- Tags are generic (only `topic/asherah` and `topic/monotheism`) instead of specific (adding `topic/deuteronomist`, `topic/josiah-reform`, `topic/folk-religion`)
- Assessment is truncated — the original chapter note had 3-5 sentences and the claim file has one
- File size drops below 3KB for a claim that originally had substantial evidence

## Expected Output Per Batch

Session 1 (3 notes, 12 claims):
- 3 updated chapter notes (84, 65, 96 lines each — down from 147, 79, ~120)
- 11-12 claim files (5-6KB each)
- 30-40 cross-scholar edges
- Progress file updated with session log entry
- Git commit
