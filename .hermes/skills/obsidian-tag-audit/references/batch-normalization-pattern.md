# Batch Normalization Script Pattern

Reusable Python pattern for normalizing tags across a large Obsidian vault. Designed to be run inside Hermes's `execute_code` sandbox. Handles both inline (`tags: [a, b, c]`) and bullet-list (`tags:\n  - a\n  - b`) YAML frontmatter formats.

## Pattern

```python
from pathlib import Path
import re

base = Path("/path/to/vault/notes")

# Define the normalization map: {old_noncanonical: new_canonical}
# Use None as the value to REMOVE a tag entirely (e.g., bare 'theology')
normalize = {
    'theology/yahweh': 'faith/yahweh',
    'theology/divine-council': 'faith/divine-council',
    'uggritic-studies': 'ugarit',
    'truth/book-notes': 'source/book-notes',
    'project/truth': 'oskg-yahweh',
    'scholars/albertz': 'scholars/rainer-albertz',
    # etc.
}

fixed = 0
for f in sorted(base.rglob("*.md")):
    content = f.read_text()
    original = content

    # Handle inline format: tags: [tag1, tag2, ...]
    def replace_inline(m):
        tag_str = m.group(1)
        tags = [t.strip().strip('"\'') for t in tag_str.split(',') if t.strip()]
        new_tags = []
        modified = False
        seen = set()
        for t in tags:
            if t in normalize:
                new_t = normalize[t]
                if new_t and new_t not in seen:
                    new_tags.append(new_t)
                    seen.add(new_t)
                    modified = True
                # if new_t is None: tag is dropped (modified=True but no append)
                elif new_t is None:
                    modified = True
            else:
                if t not in seen:
                    new_tags.append(t)
                    seen.add(t)
        if modified:
            return 'tags: [' + ', '.join(new_tags) + ']'
        return m.group(0)

    content = re.sub(r'^tags:\s*\[(.*?)\]', replace_inline, content, flags=re.MULTILINE)

    # Handle bullet-list format: tags:\n  - tag1\n  - tag2\n
    def replace_bullet(m):
        inner = m.group(1)
        tags = re.findall(r'-\s+(.+)', inner)
        new_tags = []
        modified = False
        seen = set()
        for t in tags:
            t = t.strip()
            if t in normalize:
                new_t = normalize[t]
                if new_t and new_t not in seen:
                    new_tags.append(new_t)
                    seen.add(new_t)
                    modified = True
                elif new_t is None:
                    modified = True
            else:
                if t not in seen:
                    new_tags.append(t)
                    seen.add(t)
        if modified:
            return 'tags:\n' + '\n'.join('  - ' + t for t in new_tags)
        return m.group(0)

    content = re.sub(r'^tags:\s*\n((?:\s+-\s+.+\n)+)', replace_bullet, content, flags=re.MULTILINE)

    if content != original:
        f.write_text(content)
        fixed += 1

print(f"Normalized {fixed} files")
```

## Post-normalization verification

Always run a follow-up scan to catch concatenation bugs:

```python
for f in sorted(base.rglob("*.md")):
    content = f.read_text()
    # Concatenation artifact: oskg-yahwehcreated:
    if 'oskg-yahwehcreated' in content:
        print(f"BROKEN: {f.name} — oskg-yahweh concatenated with next field")
        content = content.replace('oskg-yahwehcreated:', 'oskg-yahweh\ncreated:')
        # For bullet format, also handle inline variant
        content = content.replace('- oskg-yahwehcreated:', '- oskg-yahweh\ncreated:')
        f.write_text(content)
```

## Manual addition of missing tags

After normalization, scan for notes still below the minimum:

```python
for f in sorted(base.rglob("*.md")):
    content = f.read_text()
    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        print(f"MISSING FRONTMATTER: {f.name}")
        continue
    # ... extract tags, check count < 5, report
```
