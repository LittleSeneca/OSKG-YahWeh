# Truth Project: Claims Quality Review

After each extraction batch, run a systematic quality review on the batch's output. This catches incomplete extractions, broken wikilinks, and un-updated chapter notes before they compound across sessions.

## When

After every extraction session, before committing. Also on-demand when the user says "quality review."

## What to Check

### Claim Files (every .md in the batch)

1. **Required frontmatter fields:** `claim_id`, `statement`, `confidence`, `claim_type`, `source_note`
2. **Tags:** At least one `topic/` tag AND at least one `evidence/` tag
3. **Evidence section:** `## Evidence` heading exists AND contains structured content (numbered points, bullet lists, tables — NOT just a single paragraph)
4. **Edges section:** `## Edges` heading with wikilinks to other claims. Each edge description MUST name scholars and their arguments, not just claim slugs
5. **Wikilinks:** Every `[[claim-...]]` in the file resolves to an actual `.md` file in `notes/claims/`. Broken wikilink = automatic FAIL regardless of content quality

### Chapter Notes (the source notes for the batch)

1. **claims_status frontmatter:** `claims_status: "extracted"`, `claims_extracted_date`, `claims_count`, `claims_files` (list of wikilinks to extracted claims). All four fields required
2. **Compact summaries:** Original `## Claim N:` blocks replaced with compact one-paragraph summaries ending with `→ [[claim-slug]]` wikilinks
3. **Cross-cutting assessment tables:** The `## Chapter N Overall Assessment` table preserved (do not delete during extraction)
4. **Wikilinks in compact summaries:** Verify each `[[claim-...]]` in the compact summaries resolves to a real file

### Content Degradation

Compare the last claim in each note to the first. Are they equally thorough? Signs of degradation:
- Later claims missing sections (Evidence, Edges, Assessment)
- Later claims substantially shorter without reason (a low-confidence simple claim can be short; a complex historiography claim shouldn't be)
- Later claims lacking edge connections when earlier ones have full edge sets

## Output Format

Always use this exact format:

```
=== QUALITY REVIEW ===
Scholar — Chapter: PASS — N claims, all frontmatter valid, N edges
Scholar — Chapter: FAIL — specific issues found
=== END QUALITY REVIEW ===
```

On FAIL, describe exactly what is broken so the next session can fix it:
- Missing frontmatter fields: list them
- Broken wikilinks: list the slugs
- Missing chapter note updates: specify what's absent
- Missing claims: note which claims from the chapter note weren't extracted
- Content degradation: point to specific claims that are thinner than expected

## Verification Techniques

### Avoid grep with -P flag
macOS grep doesn't support `-P` (Perl regex). Use `grep -oE` for extended regex or read files directly and parse in Python/execute_code.

### Avoid single-quoted paths in terminal with special characters
Filenames with dashes, spaces, or parentheses break when single-quoted in terminal commands. Use double-quotes: `test -f "$path"` not `test -f '$path'`. Or better: use read_file for individual files and execute_code with terminal() for batch operations.

### Batch wikilink verification
The most efficient approach:
1. Use `grep -o '\[\[claim-[^]]*\]\]'` on each claim file to collect all wikilinks
2. Deduplicate the set
3. For each unique slug, `test -f "notes/claims/$slug.md"` 
4. Any MISSING = fail

### Frontmatter verification
Direct `read_file` on claim files is more reliable than grepping for YAML fields. Grep can miss fields due to formatting variance; reading the file lets you visually confirm.

## Common Failure Modes

### Phase 1 incompletion (most common)
The extraction session created claim files but never updated the chapter notes. Symptoms:
- Claim files exist and look correct
- Chapter notes have no `claims_status` frontmatter
- Original `## Claim N:` blocks still present
- Fix: add claims_status to chapter note, replace claim blocks with compact summaries

### Partial extraction
The chapter note has N `## Claim N:` blocks but only M < N claim files were created. Symptoms:
- Missing claim IDs in the expected sequence
- Remaining `## Claim N:` blocks in the chapter note without corresponding claim files
- Fix: extract the remaining claims, then update the chapter note

### Broken wikilinks
Wikilinks point to claim slugs that don't exist. This happens when:
- Slug was typoed during extraction
- Target claim hasn't been extracted yet (from a different batch)
- Slug format changed between extraction and edge-linking
- Fix: correct the slug or note the dependency as planned
