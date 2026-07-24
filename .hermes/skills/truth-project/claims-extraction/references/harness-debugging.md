# Harness Script Debugging Notes

Bugs discovered and fixed in `extract-loop.sh`, the batch claims extraction harness
(`~/Projects/Personal/Truth/extract-loop.sh`). These are lessons for maintaining the harness
and for any script that shells out to `hermes chat -q`.

## Bug 1: `-q` flag ordering (fatal)

**Symptom:**
```
hermes chat: error: argument -q/--query: expected one argument
```

**Root cause:** The `-q` flag takes its argument immediately. Putting `-s claims-extraction`
between `-q` and the query text causes argparse to interpret `-s` as the query value.

**Wrong:**
```bash
hermes chat -q -s claims-extraction "$(cat prompt.txt)"
```

**Right:**
```bash
hermes chat -q "$(cat prompt.txt)" -s claims-extraction
```

The `-s` flag is accepted both as a global flag (before `chat`) and as a `chat` subcommand
flag (after `chat`). Either position works as long as `-q` gets its argument immediately.

## Bug 2: Quality gate false positive (fatal)

**Symptom:** Phase 2 review shows all notes PASS, but harness dies with:
```
QUALITY GATE FAILED — stopping loop
TITLE: FAIL — specific issues found
```

**Root cause:** The Phase 2 prompt template itself contains `TITLE: FAIL — specific issues found`
as a format example. The log file (`tee` output) captures both the prompt text AND the model's
output. A naive `grep -q "FAIL"` matches the prompt template, not the actual review output.

**Wrong:**
```bash
if grep -q "FAIL" "$log_file"; then
    die "Quality review failed"
fi
```

**Right:**
```bash
failures=$(awk '/=== QUALITY REVIEW ===/{found=1; next}
                /=== END QUALITY REVIEW ===/{found=0}
                found && /FAIL/' "$log_file")
if [[ -n "$failures" ]]; then
    die "Quality review failed"
fi
```

The `awk` extracts only lines between the `=== QUALITY REVIEW ===` and
`=== END QUALITY REVIEW ===` markers, which is the model's actual output.

## Bug 3: Missing file paths in prompts (recoverable, but wasteful)

**Symptom:** Hermes session tries wrong filenames on first read:
```
read  .../Smith - Chapter 0 - Foreword and Preface.md  [File not found]
```
Then searches, finds correct file, and recovers. Wastes 2-3 turns per note.

**Root cause:** The `note_list` variable only contained note titles:
```
  1. Smith Chapter 0 — Foreword and Preface
```

The hermes session had to construct the filename itself and guessed wrong
(hyphens instead of em dashes). The harness's `get_next_batch` function
already constructs the correct filename from the progress file, but the
main loop discarded it.

**Wrong:**
```bash
note_list+="  $i. $title"$'\n'
```

**Right:**
```bash
note_list+="  $i. $title → notes/theology/$filename"$'\n'
```

Now the prompt includes the exact file path and the session reads it on the first try.

## Bug 4: `local` keyword in bash main body (fatal)

**Symptom:**
```
extract-loop.sh: line 211: local: can only be used in a function
```

**Root cause:** `local` is only valid inside bash functions. The quality gate check
code runs in the script's main body (inside the `while true` loop), not inside a
function. When the quality gate fix introduced `local failures`, it created a new
crash.

**Fix:** Use a plain variable assignment instead of `local`. The variable is inside
a loop body with `set -euo pipefail` so scoping isn't critical — or rename to avoid
collision with any outer variable.

```bash
# Before (broken — local in main body):
local failures
failures=$(awk ...)

# After (works):
log_failures=$(awk ...)
```

**Lesson:** When patching bash scripts, always check whether the code is inside a
function before using `local`. In the harness, the quality gate code is in the
main loop body, not inside `run_hermes()`.

## General Pattern: Testing harness changes

Always run a dry run first to validate flag parsing:
```bash
bash extract-loop.sh --dry-run --stop-after 1
```

Then run a single real batch:
```bash
bash extract-loop.sh --stop-after 1
```

If the quality gate fires, check the log file to distinguish false positives from
real failures:
```bash
grep "FAIL" /tmp/hermes-extract-phase2-review.log
```
