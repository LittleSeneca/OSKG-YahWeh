---
name: obsidian-tag-audit
description: "Audit and retrofit Obsidian notes with consistent, relational tagging — ensuring graph-view connectivity across a large project."
version: 1.0.0
platforms: [linux, macos]
metadata:
  hermes:
    tags: [note-taking, obsidian, metadata, tag-audit]
---

# Obsidian Tag Audit

Audit a collection of Obsidian notes for tag gaps and retrofit them with consistent, relational tags. Designed to make Obsidian's graph view show meaningful connections between notes, scholars, themes, and source types.

---

## The Tag Taxonomy

Every note should carry tags from at minimum FOUR categories, plus any project-specific tags.

### Category 1: Type (always include exactly one)
- `source/book-notes` — chapter notes from a scholarly monograph
- `source/primary-source` — original inscription, text, or artifact
- `source/secondary-source` — scholarly directory or reference entry
- `analysis/meta` — meta-analysis, synthesis, or comparative note
- `analysis/methodology` — notes about method or research approach
- `index/reading-list` — reading queues, bibliographies

### Category 2: Topic (at least two — what is this note ABOUT?)
**Deities and divine beings:**
- `faith/yahweh` — Yahweh specifically
- `faith/el` — El, Elyon, the high god
- `faith/baal` — Baal, Hadad, storm gods
- `faith/asherah` — Asherah, the goddess, cult objects
- `faith/divine-council` — the council of gods, sons of God, *elohim*
- `faith/monotheism` — the emergence, definition, or nature of monotheism
- `faith/polytheism` — polytheistic practice or vestiges

**Historical periods and events:**
- `history/israel-judah` — the two kingdoms
- `history/jerusalem` — the city, temple, Davidic dynasty
- `history/exile` — Babylonian exile as catalyst
- `history/merneptah` — Merneptah Stele and early Israel
- `history/kenite-hypothesis` — Moses, Midian, southern origins
- `history/josiah` — Deuteronomistic reform
- `history/aniconism` — image prohibition, statues, standing stones

**Methods and evidence:**
- `archaeology` — material culture, figurines, stratigraphy
- `philology` — language, etymology, textual criticism
- `historiography` — how history is written, Tendenz, bias

**Theology and philosophy:**
- `theology/divine-embodiment` — God's body, corporeality
- `theology/kabbalah` — Jewish mysticism, sefirot
- `christology` — Jesus, incarnation, Trinity
- `eschatology` — end times, new creation, final judgment
- `gender` — women's religion, masculinity of God, feminist scholarship

**Geography:**
- `ane-religion` — broader ANE comparative context
- `ugarit` — Ugaritic texts specifically

### Category 3: Scholar (the author of the book or the scholar discussed)
- `scholars/mark-smith`, `scholars/thomas-romer`, `scholars/william-dever`
- `scholars/benjamin-sommer`, `scholars/jeffrey-tigay`, `scholars/frank-moore-cross`
- `scholars/michael-heiser`, `scholars/francesca-stavrakopoulou`
- Use the full firstname-lastname format. If a note discusses MULTIPLE scholars, tag all of them.

### Category 4: Project (what larger project this note serves)
- `oskg-yahweh` — the Yahweh/monotheism research project
- Use additional project tags if the note serves multiple projects.

### Cross-Cutting Tags (add when relevant)
These don't fit into the four categories but create valuable graph connections:
- `primary-sources` — note engages directly with inscriptions or ancient texts
- `comparative-religion` — note makes cross-cultural comparisons
- `methodology` — note addresses research method explicitly
- `canon-formation` — note discusses how the Bible was compiled/edited

---

## Minimum Requirements (Mandatory)

Every note in the project MUST have:
- [ ] The Type tag (`source/book-notes`, etc.)
- [ ] At least TWO topic tags relevant to the chapter's content
- [ ] The Scholar tag for the author (or all scholars discussed)
- [ ] The Project tag (`oskg-yahweh`)
- [ ] At least one cross-reference in `related:` frontmatter to another note

**That's 5+ tags minimum per note.** If a note has fewer, it's a gap.

---

## The Audit Process

### Step 1: Build the canonical tag list
Read the existing tags across all notes. Identify what's being used. Normalize variants (e.g., `faith/yahweh` vs. `Yahweh` vs. `yahweh` → all become `faith/yahweh`). Document the canonical list.

### Step 2: Choose the approach — manual vs. hybrid

**For small vaults (< 30 notes):** Use the manual close-reading approach below. Read every note, understand its content, and tag accordingly.

**For large vaults (30+ notes):** Use the **hybrid approach**. The manual close-reading step is essential for the first 10-20 notes to understand content patterns, but the normalization leg (replacing non-canonical tags like `theology/yahweh` → `faith/yahweh`) is mechanical at scale. Once you've built the canonical map in Step 1, switch to automated batch normalization using Python scripts (see `references/batch-normalization-pattern.md` for the reusable script template). The pattern:
1. Scan all frontmatter tags across the vault
2. Build a normalization map: `{non-canonical-tag: canonical-tag}` for every variant found
3. Run a script that reads each file, normalizes inline and bullet-list tag formats, deduplicates, and writes back
4. Re-scan immediately to verify no concatenation bugs or stray characters were introduced
5. Return to manual close-reading for notes that are still below the 5-tag minimum after normalization

### Onboarding New Scholars (fresh notes dropped into an established vault)

When the user adds notes for new scholars to a vault that already has a canonical tag taxonomy, the notes were likely created with non-canonical tags (e.g., `theology/monotheism` instead of `faith/monotheism`, `scholars/kaufmann` instead of `scholars/yehezkel-kaufmann`). The audit must handle two distinct phases:

**Phase A: Discovery and normalization (mechanical).**
1. Scan ALL notes for the new scholars in one pass using `execute_code` with a Python script. Collect every tag with counts.
2. Identify every tag that doesn't match the canonical taxonomy. Group them by scholar — different scholars will have different non-canonical patterns.
3. Build a normalization map: `{non-canonical-tag: canonical-tag}` for every variant. One non-canonical tag maps to exactly one canonical tag. Watch for cases where MULTIPLE non-canonical tags map to the SAME canonical tag (e.g., both `theology/polytheism` and `theology/paganism` → `faith/polytheism`). These will produce duplicates after normalization.
4. Run normalization across ALL of the new scholar's notes at once. Use `execute_code` with `f.write_text(modified)` — this is faster and less error-prone than individual patch() calls for mechanical substitutions. The script should iterate over every file, replace every non-canonical string, and write back only if changes were made.
5. Re-scan immediately. Check for: remaining non-canonical tags, duplicate tags (same tag appears twice in the bullet list), and concatenation artifacts. Deduplication must happen in a separate pass since the normalization script can't anticipate which non-canonical pairs map to the same canonical tag.

**Phase B: Content-based additions (close-reading).**
1. For each note, read enough content to understand what the chapter covers. The introduction paragraph, the claim headings, "What's at stake" blocks, and "Who disagrees" sections are the highest-signal areas.
2. Identify: topic tags the content demands but aren't present, period tags for the historical era covered, evidence-type tags for the method used, and scholar tags for any scholar discussed extensively.
3. Add missing tags with `patch()`. Use the closing `---` of the frontmatter as anchor context.
4. The user may provide per-scholar tagging guidance (e.g., "Keel/Uehlinger notes will be heavy on archaeology, iconography; Kaufmann on historiography, faith/monotheism"). Use this as a starting point but confirm against actual chapter content — a chapter may cover different ground than the book as a whole.

**Key difference from standard audit:** In a standard audit, notes already have mostly-correct tags and you're filling gaps. In new-scholar onboarding, the notes start with systematically wrong tags and you must normalize EVERY note before you can assess what's missing. The normalization pass is the rate-limiting step.

### Step 3: Audit notes in batches (8-10 per batch)
For each note in the batch:
1. Read the note's content (especially its "what's at stake" and "who disagrees" sections — these often reveal topics that should be tagged)
2. List its current tags
3. Compare current tags against what the content covers
4. Identify gaps: missing Type? fewer than 2 Topics? no Scholar tag? no Project tag?
5. Patch the frontmatter to add missing tags. Use `patch` with `old_string` matching the closing `---` of the frontmatter and `new_string` appending the new tags.
6. Do NOT remove existing tags unless they're duplicates of newly added ones or clearly wrong.

### Step 4: Commit after each batch
```
git add -A && git commit -m "Tag audit: notes X through Y — added [N] missing tags"
```

### Step 5: Gap report
After auditing all notes, produce a report:
- Total notes audited
- Notes that were missing Type tags
- Notes with <2 Topic tags
- Notes missing Scholar tags
- Notes missing cross-references
- Notes that now exceed minimums (improvement)

### Step 6: Verify graph connectivity
After the audit is complete, verify that Obsidian's graph view shows meaningful connections. The goal: click on `faith/asherah` and see ALL notes across ALL books that discuss Asherah. Click on `scholars/mark-smith` and see ALL notes discussing his work. Click on `archaeology` + `faith/yahweh` and see the intersection.

---

## The Tag Application Logic

When deciding which tags to add to a note, ask:
1. **What chapter is this?** → The chapter's subject determines the primary topic tags.
2. **Who wrote it?** → Always tag the author.
3. **What evidence does it use?** → If archaeology, tag `archaeology`. If texts, tag `philology`. If both, tag both.
4. **What's at stake?** → If the stakes involve faith deconstruction, tag `faith/monotheism` or `faith/yahweh`. If the stakes are methodological, tag `methodology`.
5. **Who disagrees?** → If the note discusses named scholars who disagree, tag them as well.
6. **What period?** → If the chapter covers exile-era developments, tag `history/exile`. If monarchic, tag `history/israel-judah`.

---

## Common Tagging Gaps (what the audit will find)

1. **Notes with only `oskg-yahweh` and `source/book-notes`** — missing topic tags entirely.
2. **Notes that discuss Asherah but don't tag `faith/asherah`** — the content is there but the tag isn't.
3. **Notes that cite Dever's archaeology but don't tag `archaeology`** — missing evidence-type tags.
4. **Notes missing the scholar tag** — especially common when a note discusses multiple scholars.
5. **Notes with no cross-references** — isolated from the graph.

---

## Pitfalls

### Pitfall 1: Concatenation bugs during batch normalization

When normalizing tags with a Python script that modifies YAML frontmatter, inline-format and bullet-list format are easily confused by regex. A script that replaces `project/truth` with `oskg-yahweh` in inline format (`tags: [..., project/truth, ...]`) works correctly. But if the same replacement runs against bullet-list format where the closing `]` doesn't exist, the result is `oskg-yahwehcreated:` — the tag gets concatenated with the next YAML field.

**Fix:** Always handle inline (`tags: [a, b, c]`) and bullet-list (`tags:\n  - a\n  - b`) formats separately. Test normalization scripts on 2-3 notes first before running against the full vault. Always run a follow-up scan after batch normalization to detect concatenation artifacts.

### Pitfall 2: Malformed frontmatter is silently skipped

Notes with frontmatter that's missing a closing `---` will be invisible to regex-based tag extraction (`re.match(r'^---\s*\n(.*?)\n---', ...)`). They won't appear in audit results and will pass through undetected. The symptoms are subtle: a note shows up in the file count but not in tag analysis.

**Fix:** After building the file list, compare the count of files found by glob against the count of files with successfully extracted frontmatter. Any discrepancy means a broken frontmatter. Pattern to detect: `len(glob_files) != len(parsed_notes)`. When found, read the suspect file directly to check for the missing `---`.

### Pitfall 3: Normalization can introduce duplicates silently

When a note already has `faith/yahweh` and the normalization map also converts `yahweh-origins` → `faith/yahweh`, the script must deduplicate. Without dedup logic, the tag appears twice, inflating graph edge counts and breaking queries that expect unique tags.

**Fix:** Always maintain a `seen` set during tag construction in normalization scripts and skip any tag already added. This applies to both inline and bullet-list format handlers.

### Pitfall 4: Subagent-generated notes arrive with non-canonical tags

When subagents create chapter notes, they don't know the canonical taxonomy. They use bare or malformed tags: `theology` (no namespace), `yahweh-origins` (wrong prefix), `scholars/keel` (missing first name), `iron-age-i`, `goddess`, `figurines` (content words, not taxonomy entries). Every subagent note needs full normalization — it's not a gap-filling exercise, it's a rebuild.

**Detection:** Scan newly added notes. If any tag lacks a `/` prefix (bare) or uses `theology/` instead of `faith/` or `history/`, the note was subagent-generated and needs the full two-phase treatment (Phase A normalization + Phase B content additions) from the "Onboarding New Scholars" section above.

**Fix:** Treat the entire batch of subagent notes as a normalization problem first. Build the map, run replace, re-scan. Only then do close-reading for missing topic tags. The normalization pass IS the audit for these notes — there's nothing to "audit" when every tag is wrong.

## When to Use This Skill

- After completing a batch of book notes and wanting them integrated into the existing graph
- When building a large project and noticing tag inconsistency
- Before a synthesis phase — consistent tags enable meaningful searches and graph exploration
- As a periodic maintenance task on a growing note collection

## When NOT to Use

- On a brand new project with only 1-2 notes (no tagging baseline yet)
- When the note content itself needs editing (fix content before fixing tags)
