# Harness Troubleshooting — extract-loop.sh

Common failure modes of the batch extraction harness and their fixes.

## 1. `hermes chat: error: argument -q/--query: expected one argument`

**Symptom:** Harness dies immediately on Phase 1 with argparse error.

**Cause:** `-q` takes its argument immediately — nothing can sit between `-q` and the query text.

**Wrong:** `hermes chat -q -s claims-extraction "$prompt"`
**Right:** `hermes chat -q "$prompt" -s claims-extraction`

## 2. Quality gate false positive: "TITLE: FAIL — specific issues found"

**Symptom:** Phase 2 quality review shows all notes PASS but the harness still dies with `QUALITY GATE FAILED`.

**Cause:** Hermes echoes the prompt into the log. The Phase 2 prompt includes a format template:

```
=== QUALITY REVIEW ===
TITLE: PASS — N claims...
TITLE: FAIL — specific issues found    <-- this line
=== END QUALITY REVIEW ===
```

A naive `grep FAIL` on the log matches the template placeholder, not actual failures.

**Fix (two layers):**

1. Scope the grep to content between `=== QUALITY REVIEW ===` and `=== END QUALITY REVIEW ===` using awk:
```bash
awk '/=== QUALITY REVIEW ===/{found=1; next} /=== END QUALITY REVIEW ===/{found=0} found && /FAIL/' logfile
```

2. But hermes echoes the prompt which ALSO contains these markers. So exclude the template placeholder line (starts with literal "TITLE:"):
```bash
awk '/=== QUALITY REVIEW ===/{found=1; next} /=== END QUALITY REVIEW ===/{found=0} found && /FAIL/ && $0 !~ /^TITLE: FAIL/' logfile
```

Real failures start with note names (`Smith Origins — Ch5: FAIL — ...`), not the literal word `TITLE:`.

## 3. `local: can only be used in a function`

**Symptom:** Harness dies on quality gate check with bash syntax error.

**Cause:** `local` is only valid inside bash functions. The quality gate check runs in the script's main body.

**Fix:** Remove `local` keyword. In the main body, variables are already scoped to the script.

## 4. Hermes session guesses wrong filename

**Symptom:** Phase 1 or 2 shows `read_file` failing with "File not found" for filenames with hyphens instead of em dashes.

**Cause:** The harness only passes note titles (not file paths) in the prompt. Hermes sessions must construct paths themselves and may use wrong characters.

**Fix:** Include full relative paths in the note list fed to hermes:
```
1. Smith Chapter 0 — Foreword and Preface → notes/theology/Smith Chapter 0 — Foreword and Preface.md
```

## 5. `$TMPDIR` may contain double slashes

**Symptom:** Log file paths show `//` (e.g., `/var/folders/.../T//hermes-extract-phase1-extract.log`).

**Cause:** `TMPDIR` on macOS may already end with `/`. Concatenating with `/` prefix produces `//`.

**Fix:** Use `"${TMPDIR%/}/filename"` to strip trailing slash before concatenating. Not yet implemented in the script.

## 6. `patch` tool corrupts bash heredocs — use `sed -i` instead

**Symptom:** After using the Hermes `patch` tool to edit `extract-loop.sh`, `bash -n` reports "unexpected EOF while looking for matching `''" and the script won't parse. The error points to a line far from the edit site (e.g., an awk command with balanced single quotes).

**Cause:** The `patch` tool can introduce invisible encoding changes that break heredoc parsing. Bash heredocs (`<<PROMPT` ... `PROMPT`) are sensitive to multi-byte character boundaries and the tool can silently corrupt the delimiter recognition. The error appears on an unrelated line because bash scans forward looking for the closing delimiter and fails at EOF.

**Fix:** Never use the Hermes `patch` tool on bash scripts containing heredocs. Use `sed -i` instead:

```bash
# Insert text after line 155:
sed -i '' '155a\
new line of text here\
' extract-loop.sh

# Replace a substring:
sed -i '' 's/old text/new text/' extract-loop.sh
```

Always run `bash -n extract-loop.sh` after any sed edit to verify the script still parses.
