---
name: evidence-synthesis-writing
description: "Write evidence-forward synthesis and capstone documents that report what a knowledge graph or structured analysis shows — no first-person testimony, no theological or interpretive conclusions, dense inline references, super tag-rich metadata."
version: 1.0.0
category: writing
tags:
  - writing
  - synthesis
  - evidence
  - methodology
  - capstone
  - knowledge-graph
  - research
---

# Evidence-Forward Synthesis Writing

Use this skill when writing a capstone, synthesis, or culminating document that reports findings from a structured knowledge graph, claims database, or systematic evidence analysis. The document reports what the data shows. It does not offer personal testimony, theological conclusions, or "what this means for me."

## Trigger Conditions

- User asks for a capstone, synthesis, or culminating document from structured claims/graph data
- User asks "what does this mean" or "what have we learned" and the underlying work is a knowledge graph or claims database
- Any document that maps convergences, unknowns, structural architecture, and evidence density from a graph

## Core Principles

### 1. No First-Person Testimony

The document is not about the author's journey, faith, beliefs, or personal response to the evidence. The document reports what the graph reports. If the user wants a personal synthesis, they will ask for it separately — do not conflate the evidence map with the personal response.

**Wrong:** "I remain a person of faith. A different faith than I had before."
**Right:** "The graph records 16 HIGH+ confidence supports for this claim with zero MEDIUM+ contradictions."

**Wrong:** "This changes how I read the Bible."
**Right:** "This convergence is supported by four evidence types: onomastics, biblical text, comparative ANE, and epigraphy."

### 2. Evidence-Forward Framing

The subject of every sentence should be the evidence, the graph, the data, or the claims — not the author.

**Framing vocabulary:**
- "The graph shows" / "The data supports" / "The graph records"
- "Phase 4 identified" / "The analysis produced"
- "The convergence requires" / "The evidence types converge on"
- "X claims at HIGH+ confidence support this; Y claims at MEDIUM+ contradict it"

**Never:**
- "I believe" / "I think" / "I find"
- "This means for my faith" / "This changed how I pray"
- "I am left with" / "I now understand"

### 3. Dense Inline References

Every claim, convergence point, structural finding, and counter-position must be backed by specific inline wikilinks to claim files, note files, or synthesis documents. The reader should be able to click through to the underlying evidence for any assertion.

**Wrong:** "Scholars agree that El was Israel's original god."
**Right:** "El was Israel's original god ([[claim-el-was-original-god-israel-name-and-absence-yahweh]], [[claim-israel-name-contains-el-shechem-deir-alla-confirm-el-priority]], [[claim-name-israel-el-original]]). Sixteen HIGH+ confidence supports, zero MEDIUM+ contradictions."

**Reference targets (in priority order):**
1. Specific claim files: `[[claim-*]]`
2. Chapter notes: `[[Smith Origins — Ch7 — El Yahweh and the Original God of Israel]]`
3. Synthesis documents: `[[phase4-unknowns-and-convergence]]`
4. Primary sources: `[[deut-32-8-9-qumran-variant]]`

A capstone document should have 100+ inline claims references. This is not decorative — it is the evidentiary backbone.

### 4. Super Tag-Rich Frontmatter

The frontmatter must include 15+ tags covering every dimension of the document:

**Required tag categories:**
- `type/synthesis` or `type/capstone` — document type
- Domain tags: the subject matter (e.g., `yahweh-origins`, `monotheism`, `polytheism`, `divine-council`, `el`, `asherah`)
- Method tags: the analytical methods used (e.g., `claims-analysis`, `knowledge-graph`, `convergence-analysis`, `counter-position-analysis`, `structural-analysis`, `evidence-density`)
- Phase tags: where this sits in the project (e.g., `phase5`)
- Source discipline tags: (e.g., `archaeology`, `onomastics`, `text-criticism`, `ugaritic-studies`, `ane-comparative`, `biblical-studies`, `historiography`)
- Project tag: the project namespace (e.g., `oskg-yahweh`)
- Period tags if relevant: (e.g., `exilic-period`, `second-isaiah`)

**Additional frontmatter fields:**
- `scholars:` — list of major scholars cited (not just one or two; the full landscape)
- `scale:` — quantitative metadata (books, notes, claims, phases)
- `related:` — wikilinks to all synthesis documents, methodology documents, and key supporting notes
- `created:` — date

### 5. Report Structural Data Directly

Do not narrate. Report numbers, counts, and confidence levels.

**Wrong:** "The evidence for El's priority is overwhelming."
**Right:** "16 HIGH+ supports. 0 MEDIUM+ contradictions. Evidence types: onomastics, biblical text, comparative ANE, epigraphy."

**Wrong:** "Schmid's position would be devastating if true."
**Right:** "Schmid counter-position: 41% survival rate. ~112 downstream claims at risk. Mechanism: methodological undercutting of the chronological framework."

Every convergence point should include: claim ID, support count, contradiction count, evidence types, key scholars, and confidence level.

### 6. Organize by Analytical Function

The document structure should follow the graph's analytical architecture, not a narrative arc:

1. **Pipeline/context** — what analysis was performed, at what scale
2. **Settled convergences** — what the graph shows as true, with structural data per convergence
3. **Genuine unknowns** — what is contested, with both sides' claims mapped
4. **Structural architecture** — hinges, cascade trees, cross-scholar tensions
5. **Counter-position landscape** — stress test results, survival rates, mechanisms
6. **Evidence density by domain** — where evidence is strongest/thinnest
7. **Graph fragilities** — single points of failure, structural instabilities, impasses
8. **Summary tables** — condensed reference at a glance

### 7. Tables for Comparative Data

Use markdown tables for any data that benefits from side-by-side comparison:

- Fault line maps (scholars, confidences, evidence types, dispute types)
- Convergence candidates that just miss the threshold
- Stress test survival rates with mechanisms
- Evidence density comparisons across domains
- Scholar position maps

### 8. No Theological or Interpretive Conclusions

The synthesis reports graph structure. It does not say what the implications are for religious belief, practice, or authority. The reader supplies that layer. If the user wants theological implications, they will ask for them in a separate document.

**The document answers:** "What does the evidence show?"
**The document does NOT answer:** "What does this mean for my faith?" or "Who is God?"

## Pitfalls

### Pitfall 1: Drifting into Testimony

The most common failure mode. The writer starts neutral and gradually shifts into first-person reflection. Common triggers: sections about "what remains contested" (writer starts adjudicating), the epilogue or conclusion (writer starts reflecting). Guard against this by checking every paragraph for first-person pronouns and theological language before finishing.

### Pitfall 2: Sparse References

A capstone with 5-10 inline references looks like a summary, not an evidence map. The threshold is 100+ for a document of 8-10 parts. If you find yourself writing a paragraph that makes a claim without a wikilink, stop and add one.

### Pitfall 3: Vague Confidence Language

"Scholars agree" / "the consensus holds" / "the evidence is strong" — all of these hide the structural data. Replace with specific numbers: "X HIGH+ supports, Y MEDIUM+ contradicts" or "X scholars at HIGH+ confidence." If you don't have the numbers, you haven't done the analysis.

### Pitfall 4: Missing the Dissenter

Every convergence section must note who dissents and on what basis. The Kaufmann pattern (most cited AND most contradicted) is a structural feature of many graphs. The dissenter is not an afterthought — their presence and isolation are data points.

### Pitfall 5: Conflating Graph Strength with Truth

The graph measures scholarly support and contradiction patterns. It does not measure truth. "16 HIGH+ supports" means 16 scholars are confident — not that their confidence is correct. The synthesis should acknowledge the epistemological gap between "the graph shows convergence" and "the convergence is true."

## Verification Checklist

Before delivering a capstone:

- [ ] Zero first-person pronouns outside of quoted material
- [ ] Zero theological conclusions or faith-implication statements
- [ ] 15+ frontmatter tags
- [ ] Scale metadata in frontmatter (books, claims, notes, phases)
- [ ] Scholar list in frontmatter
- [ ] 100+ inline claim wikilinks
- [ ] Every convergence point backed by specific claim IDs with support/contradiction counts
- [ ] Every fault line maps both sides' claims
- [ ] Structural data reported directly (numbers, not adjectives)
- [ ] Dissenters noted per convergence
- [ ] Tables used for comparative data
- [ ] No vague confidence language without structural backing
