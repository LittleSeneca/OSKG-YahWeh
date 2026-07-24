# Project Rename: Batch Update Across Project + Obsidian Vault

When renaming a project that lives both in its own directory AND has mirrored notes in the Obsidian vault, follow this sequence:

## 1. Rename GitHub remote first

```bash
cd <project-dir>
gh repo rename <new-name> --repo <owner>/<old-name> --yes
```

## 2. Rename local directory and update remote

```bash
cd <parent-dir>
mv <old-name> <new-name>
cd <new-name>
git remote set-url origin https://github.com/<owner>/<new-name>.git
```

## 3. Batch-replace tags across project (all .md files)

```bash
cd <project-dir>
find . -name '*.md' -exec sed -i '' 's/<old-tag>/<new-tag>/g' {} +
```

## 4. Batch-replace path references (all .md files)

```bash
find . -name '*.md' -exec sed -i '' 's|~/Projects/<old-path>|~/Projects/<new-path>|g' {} +
```

## 5. Batch-replace GitHub URLs

```bash
find . -name '*.md' -exec sed -i '' 's|<owner>/<old-name>|<owner>/<new-name>|g' {} +
```

## 6. Apply the same replacements to the Obsidian vault

```bash
cd ~/Projects/Personal/obsidian
find . -name '*.md' -exec sed -i '' 's/<old-tag>/<new-tag>/g' {} +
find . -name '*.md' -exec sed -i '' 's|~/Projects/<old-path>|~/Projects/<new-path>|g' {} +
find . -name '*.md' -exec sed -i '' 's|<owner>/<old-name>|<owner>/<new-name>|g' {} +
```

## 7. Rename the Obsidian project note

```bash
cd ~/Projects/Personal/obsidian/Hermes/Projects/<Domain>/
mv <old-name>.md <new-name>.md
```

## 8. Rewrite Home.md and the Obsidian project note

Update titles, descriptions, aliases, and status sections.

## 9. Update the domain index (Personal Index, etc.)

Update the entry linking to the project note.

## 10. Verify

```bash
# Zero remaining old tags
grep -rl '<old-tag>' <project-dir> --include='*.md' | wc -l
grep -rl '<old-tag>' ~/Projects/Personal/obsidian --include='*.md' | wc -l

# Zero remaining old paths
grep -rl '<old-path-segment>' ~/Projects/Personal/obsidian --include='*.md' | wc -l

# Zero remaining old GitHub URLs
grep -rl '<owner>/<old-name>' ~/Projects/Personal/obsidian --include='*.md' | wc -l
```

## Pitfalls

- **Session note filenames should NOT be renamed.** Session filenames like `2026-07-22 — truth-project-launch.md` contain the old project name but are historical artifacts. Renaming them breaks wikilinks across the entire vault. The tags inside them are updated; the filenames stay.
- **Wikilinks in project notes to session files will still reference old filenames.** This is correct — the session files exist at those names. Leave them.
- **Run the find/sed commands from the project root and obsidian root separately.** Do not try to run from a parent directory — the path patterns differ between the project and the vault.
