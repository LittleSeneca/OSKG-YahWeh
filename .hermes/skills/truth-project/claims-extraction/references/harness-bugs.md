# Harness Bugs — `extract-loop.sh`

Bugs found and fixed in the three-phase batch harness. Each entry: symptom, root cause, fix.

## Bug 1: `-q` flag ordering (fatal)

**Symptom:** `hermes chat: error: argument -q/--query: expected one argument`

**Root cause:** `hermes chat -q -s claims-extraction "$prompt"` — the `-s` flag sits between `-q` and its required argument. argparse interprets `-s` as the query value.

**Fix:** `hermes chat -q "$prompt" -s claims-extraction`. Query text must immediately follow `-q`.

## Bug 2: Quality gate false positive — prompt template (non-fatal, wrong gate)

**Symptom:** Quality gate reports "FAIL" when all notes show PASS in the review output.

**Root cause:** The Phase 2 prompt template contains `TITLE: FAIL — specific issues found` as a format example. The naive `grep -q "FAIL"` scans the entire log file (which includes the echoed prompt) and matches the template text.

**Fix v1:** Scope grep to content between `=== QUALITY REVIEW ===` and `=== END QUALITY REVIEW ===` markers using awk. This fixed the case where the template `TITLE: FAIL` line was OUTSIDE the quality review block.

## Bug 3: Quality gate false positive — hermes prompt echo (non-fatal, wrong gate)

**Symptom:** Same as Bug 2, but occurring even after awk marker scoping.

**Root cause:** Hermes echoes the full prompt into its log output, including the `=== QUALITY REVIEW ===` block from the prompt template (which contains `TITLE: FAIL — specific issues found`). The awk filter matches this echoed block before reaching the actual output block.

**Fix v2:** Add `$0 !~ /^TITLE: FAIL/` to the awk condition. The template placeholder line starts with the literal word `TITLE:` while real failure lines start with actual note names (e.g., `Smith Origins — Ch5: FAIL — ...`).

```bash
log_failures=$(awk '/=== QUALITY REVIEW ===/{found=1; next} /=== END QUALITY REVIEW ===/{found=0} found && /FAIL/ && $0 !~ /^TITLE: FAIL/' "$TMPDIR/hermes-extract-phase2-review.log")
```

## Bug 4: `local` outside function (fatal)

**Symptom:** `extract-loop.sh: line 211: local: can only be used in a function`

**Root cause:** Bash `local` keyword only works inside function bodies. The quality gate check runs in the script's main body.

**Fix:** Remove `local` declaration. Use plain assignment in the top-level scope.

## Bug 5: Missing file paths in prompts (recoverable, wasted turns)

**Symptom:** Hermes session reads wrong filename on first attempt (e.g., `Smith - Chapter 0 - Foreword.md` with hyphens instead of em dashes), then searches to find correct file.

**Root cause:** The `$note_list` variable passed only note titles to the prompt. The hermes session had to reconstruct file paths from titles, and got the dashes wrong (em dashes `—` vs hyphens `-`).

**Fix:** Include full relative paths in the note list: `title → notes/theology/filename.md` instead of just `title`.
