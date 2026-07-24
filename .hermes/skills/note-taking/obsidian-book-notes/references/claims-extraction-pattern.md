# Claims Extraction: From Inline Claims to Argument Dependency Map

When a research project accumulates 50+ chapter notes across multiple scholars using the `obsidian-book-notes` claim format, the inline claims become buried. You cannot query "show me every claim about Asherah" or trace "what claims depend on the Soleb inscription?" This reference documents the extraction pattern designed for the Truth project (~500 claims across 13+ scholars).

## When to Use This Pattern

- You have 50+ chapter notes with claims formatted per `obsidian-book-notes`
- You have cross-cutting research questions that span multiple scholars
- You need to build an argument dependency map: who supports whom, what contradicts what
- Obsidian's graph view at the note level is too coarse (one note = 10 claims on different topics)

## Architecture Summary

### Claims as First-Class Nodes

Each claim becomes its own file in a flat `notes/claims/` directory. The filename is a human-readable slug: `claim-kuntillet-ajrud-symbol-not-goddess.md`. Obsidian's graph view uses filenames as node labels, so slugs must be descriptive.

### Claim ID System

`<scholar-initials>-<book-abbreviation>-<chapter>.<claim-number>`

Examples:
- `smith-ehg-3.2` — Mark S. Smith, Early History of God, Ch 3, Claim 2
- `romer-inv-9.1` — Thomas Römer, Invention of God, Ch 9, Claim 1
- `dever-dghw-5.4` — William Dever, Did God Have a Wife?, Ch 5, Claim 4

Stable, human-readable, conversation-friendly ("check smith-ehg-3.2").

### Tag Taxonomy

Every claim file carries:
- `type/claim` — non-negotiable; enables graph view filtering
- `topic/*` — primary subject matter (asherah, monotheism, divine-council, etc.)
- `evidence/*` — evidence type (inscriptional, archaeological, grammatical, etc.)
- `scholar/*` — who made the claim
- `source/*` — which book it comes from

### Edge Types

Five relationship types expressed as wikilinks with prose descriptors in an **Edges** section:

| Edge | Meaning |
|-------|---------|
| Depends on | Claim A requires Claim B to be true |
| Supports | Claim A provides evidence that strengthens Claim B |
| Contradicts | Claim A and Claim B cannot both be true |
| Challenged by | Claim A is weakened by evidence in Claim B |
| Primary sources | Links to inscription/text/artifact nodes |

Edges are manual — they require semantic understanding of how claims relate. This is the most labor-intensive phase but also where the value lives.

### Chapter Notes After Extraction

Replace each full claim block with a compact summary:

```markdown
## Claim 2: The Kuntillet Ajrud inscriptions refer to the asherah symbol, not the goddess
→ [[claim-kuntillet-ajrud-symbol-not-goddess]] | **smith-ehg-3.2** | Confidence: MEDIUM
  The grammatical argument is strong but Ugaritic counter-examples exist.
  Contradicted by: [[claim-kuntillet-ajrud-proves-consort]] (Römer)
```

This keeps chapter notes readable as standalone documents. The chapter-level assessment tables stay intact.

### Primary Sources as Nodes

Inscriptions, texts, and artifacts (Kuntillet Ajrud, Soleb Shasu, Deut 32:8-9 + 4QDeut) get their own files with `type/primary-source` tags. Claims link to them bidirectionally.

## Extraction Feasibility

**Automation coverage:** ~70-80%. The claim headers (`## Claim N:`) and bold-labeled sections are consistent enough for structured parsing. A script can extract text, generate frontmatter, and suggest tags.

**Manual work:** Edges (fully manual), tag refinement, slug assignment, quality checks.

**Scope estimate for the Truth project:** 400-500 claims across ~150 chapter notes. 75-160 hours total at 2-3 sessions/week = 3-6 months. Phased rollout recommended: extract all claims first, add edges incrementally.

## Reference Implementation

The Truth project's design document lives at `~/Projects/Personal/Truth/notes/claims-architecture.md`. It includes:
- Full audit of six chapter notes (claim counts, structure, metadata gaps)
- Complete tag taxonomy with ~30 topic tags
- Worked example: `claim-kuntillet-ajrud-symbol-not-goddess.md`
- Post-extraction chapter note example: `example-smith-ch3-post-extraction.md`
