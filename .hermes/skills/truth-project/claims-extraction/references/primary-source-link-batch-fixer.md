# Primary Source Link Batch Fixer

Reusable Python pattern for auditing and retrofitting primary source wikilinks across a large collection of claim files. Used in the July 2024 claims audit to add 269 missing links across 197 files.

## When to use

- After a large extraction batch where Primary Sources sections were left with descriptive text but no wikilinks
- When you discover claims mentioning inscriptions/texts/artifacts that should link to `sources/primary-sources/`
- As a periodic maintenance pass on the claims graph

## Pattern

```python
import os, re

CLAIMS_DIR = "/Users/littleseneca/Projects/Personal/Truth/notes/claims"
PRIMARY_SOURCES_DIR = "/Users/littleseneca/Projects/Personal/Truth/sources/primary-sources"

# Keyword → canonical source slug mapping
# Order matters: more specific patterns first to avoid premature matches
KEYWORD_SOURCE_MAP = [
    ('kuntillet ajrud', 'kuntillet-ajrud-inscriptions'),
    ('baal cycle', 'ugaritic-baal-cycle'),
    ('ktu', 'ugaritic-baal-cycle'),  # Broad match — handles KTU², KTU1, etc.
    ('deuteronomy 32:8', 'deut-32-8-9-qumran-variant'),
    ('deut 32:8', 'deut-32-8-9-qumran-variant'),
    ('khirbet el-qom', 'khirbet-el-qom-inscription'),
    ('soleb', 'soleb-shasu-inscription'),
    ('mesha stele', 'mesha-stele'),
    ('mesha inscription', 'mesha-stele'),
    ('elephantine', 'elephantine-papyri'),
    ('lachish', 'lachish-ostraca'),
    ('merneptah', 'merneptah-stele'),
    ('tel dan', 'tel-dan-stele'),
    ('ketef hinnom', 'ketef-hinnom'),
]

primary_slugs = set(f.replace('.md', '') for f in os.listdir(PRIMARY_SOURCES_DIR) if f.endswith('.md'))

for filename in sorted(os.listdir(CLAIMS_DIR)):
    if not filename.endswith('.md'):
        continue
    
    filepath = os.path.join(CLAIMS_DIR, filename)
    with open(filepath, 'r') as f:
        content = f.read()
    
    content_lower = content.lower()
    
    # Determine which sources are mentioned but not linked
    missing_slugs = set()
    for keyword, slug in KEYWORD_SOURCE_MAP:
        if keyword in content_lower:
            if slug not in content and f'source-{slug}' not in content:
                missing_slugs.add(slug)
    
    if not missing_slugs:
        continue
    
    # Build link text
    new_links = [f'- [[{slug}]]' for slug in sorted(missing_slugs)]
    link_text = '\n' + '\n'.join(new_links)
    
    # Find or create Primary Sources section
    ps_header_match = re.search(r'\*\*Primary sources?:?\*\*', content)
    
    if ps_header_match:
        # Section exists — find insertion point after last bullet
        after_header = content[ps_header_match.end():]
        next_section = re.search(r'\n(\*\*[A-Z]|\#\# |\n---)', after_header)
        insert_pos = ps_header_match.end() + (next_section.start() if next_section else len(after_header))
        
        # Find last bullet position within the section
        section_text = content[ps_header_match.end():insert_pos]
        last_bullet_match = None
        for m in re.finditer(r'^- .+', section_text, re.MULTILINE):
            last_bullet_match = m
        if last_bullet_match:
            bullet_end = ps_header_match.end() + last_bullet_match.end()
            newline_pos = content.find('\n', bullet_end)
            if newline_pos == -1:
                newline_pos = insert_pos
            insert_pos = newline_pos
        
        new_content = content[:insert_pos] + link_text + content[insert_pos:]
    else:
        # No PS section — create one before ## Assessment
        assessment_match = re.search(r'\n## Assessment', content)
        if assessment_match:
            insert_pos = assessment_match.start()
        else:
            insert_pos = len(content)
        
        ps_section = f'\n**Primary sources:**\n{chr(10).join(new_links)}\n'
        new_content = content[:insert_pos] + ps_section + content[insert_pos:]
    
    with open(filepath, 'w') as f:
        f.write(new_content)
```

## Pitfalls

1. **KTU matching needs to be broad.** Ugaritic texts are cited as `KTU² 1.47`, `KTU 1.1`, `KTU1.2`, etc. Match on the bare substring `ktu` — it's distinctive enough. But don't match inside words like `bktu`.

2. **Superscript characters break exact matching.** `KTU²` won't match `ktu ` (with trailing space). Use the substring `ktu` without requiring following whitespace.

3. **`ls | wc -l` inflates file counts.** `ls` outputs in multi-column format when stdout is a terminal. When piped, it switches to one-per-line, but the output can still be unreliable. Use `os.listdir()` in Python or `find ... -type f | wc -l` in shell for accurate counts.

4. **Wikilinks inside HTML comments are false positives.** When scanning for broken wikilinks, strip `<!-- ... -->` blocks first. Forward references intentionally commented out should not be flagged.

5. **Insert after the last bullet, not at end of section.** If the Primary Sources section already has descriptive text entries (e.g., "Egyptian Soleb inscription (Amenophis III, c. 1370 BCE)"), append wikilinks after them rather than replacing them.
