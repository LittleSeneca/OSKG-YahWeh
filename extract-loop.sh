#!/usr/bin/env bash
set -euo pipefail

# extract-loop.sh — batch claims extraction harness for Truth Project
# Spawns hermes chat -q sessions for each phase: extract, review, finalize.
# Runs unattended until all 149 notes are processed or a quality gate fails.

PROJECT_DIR="$HOME/Projects/Personal/Truth"
PROGRESS_FILE="$PROJECT_DIR/notes/claims-progress.md"
SKILL="claims-extraction"
BATCH_SIZE=3
DRY_RUN=false
STOP_AFTER=999
TMPDIR="${TMPDIR:-/tmp}"

usage() {
    cat <<'EOF'
Usage: bash extract-loop.sh [--batch N] [--dry-run] [--stop-after N]

  --batch N       Start at batch N (default: auto-detect from progress file)
  --dry-run       Print what would be done, don't run hermes
  --stop-after N  Stop after N batches (default: run until done)
EOF
    exit 1
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --batch)     START_BATCH="$2"; shift 2 ;;
        --dry-run)   DRY_RUN=true; shift ;;
        --stop-after) STOP_AFTER="$2"; shift 2 ;;
        --help|-h)   usage ;;
        *)           echo "Unknown flag: $1"; usage ;;
    esac
done

# ── helpers ──────────────────────────────────────────────────────────

log()  { echo "[$(date +%H:%M:%S)] $*"; }
die()  { log "ERROR: $*"; exit 1; }

# Parse progress file to find next N unchecked notes.
# Output: first line = count, remaining lines = title (tab) filename
get_next_batch() {
    local count=0
    local batch=""
    while IFS= read -r line; do
        if [[ "$line" =~ ^"- [ ] " ]]; then
            local title="${line#- \[ \] }"
            local filename="$title.md"
            batch+="$title"$'\t'"$filename"$'\n'
            ((count++))
            if [[ $count -ge $BATCH_SIZE ]]; then
                break
            fi
        fi
    done < "$PROGRESS_FILE"

    if [[ $count -eq 0 ]]; then
        return 1
    fi
    echo "$count"
    echo "$batch"
}

# Write a prompt file in the temp directory, return the path.
# Usage: write_prompt phase-name <<'PROMPT'
#   ... prompt content with $VARIABLES expanded ...
# PROMPT
# The heredoc delimiter must be PROMPT (no quotes) so variables expand.
write_prompt() {
    local phase="$1"
    local prompt_file="$TMPDIR/hermes-extract-${phase}.txt"
    cat > "$prompt_file"
    echo "$prompt_file"
}

# Run hermes (or print what would be run in dry-run mode)
run_hermes() {
    local phase="$1"
    local prompt_file="$2"
    local log_file="$TMPDIR/hermes-extract-${phase}.log"

    if $DRY_RUN; then
        log "[DRY RUN] Would run: hermes chat -q \"\$(cat $prompt_file)\" -s $SKILL"
        log "[DRY RUN] Prompt: $(wc -c < "$prompt_file") chars"
        return 0
    fi

    log "Running phase: $phase"
    hermes chat -q "$(cat "$prompt_file")" -s "$SKILL" 2>&1 | tee "$log_file"
    local exit_code=${PIPESTATUS[0]}
    if [[ $exit_code -ne 0 ]]; then
        die "Phase $phase failed with exit code $exit_code"
    fi
    echo "$log_file"
}

# ── main loop ────────────────────────────────────────────────────────

log "Claims extraction harness starting"
log "Project: $PROJECT_DIR"
log "Skill: $SKILL"
log "Batch size: $BATCH_SIZE"
$DRY_RUN && log "DRY RUN — no hermes sessions will be spawned"

cd "$PROJECT_DIR" || die "Cannot cd to $PROJECT_DIR"
command -v hermes >/dev/null 2>&1 || $DRY_RUN || die "hermes CLI not found in PATH"

# Determine starting batch number
BATCH_NUM="${START_BATCH:-}"
if [[ -z "$BATCH_NUM" ]]; then
    BATCH_NUM=$(grep -c "^### 20" "$PROGRESS_FILE" 2>/dev/null || echo 0)
    BATCH_NUM=$((BATCH_NUM + 1))
fi
log "Starting at batch $BATCH_NUM"

BATCHES_DONE=0
while true; do
    # ── fetch next batch ──────────────────────────────────────────
    BATCH_DATA=$(get_next_batch) || {
        log "No unchecked notes remain. Done."
        break
    }

    batch_count=$(echo "$BATCH_DATA" | sed -n '1p')
    notes_data=$(echo "$BATCH_DATA" | tail -n +2)

    if [[ "$batch_count" -lt 1 ]]; then
        log "Batch empty. Done."
        break
    fi

    # Build note list for prompts (title + full path so sessions don't guess filenames)
    note_list=""
    i=1
    while IFS=$'\t' read -r title filename; do
        [[ -z "$title" ]] && continue
        note_list+="  $i. $title → notes/theology/$filename"$'\n'
        ((i++))
    done <<< "$notes_data"

    log "Batch $BATCH_NUM: $batch_count notes"
    echo "$note_list"

    # ── Phase 1: Extraction ───────────────────────────────────────
    extract_prompt_file=$(write_prompt "phase1-extract" <<PROMPT
Claims extraction batch $BATCH_NUM. Truth Project at $PROJECT_DIR.

Read notes/claims-progress.md to verify current state. List all existing claims in notes/claims/ for edge targeting.

Process only these $batch_count notes:
$note_list

For each note: read it from notes/theology/, extract every ## Claim N: block into a claim file in notes/claims/, update the chapter note with compact summaries and claims_status frontmatter, add edges between new claims and to any existing claims.

DO NOT update claims-progress.md. DO NOT git commit. DO NOT ask questions — there is no user.

Print a structured summary using this exact format:

=== BATCH SUMMARY ===
Notes processed: N
(per-note breakdown: title and claim IDs)
Total claims created: N
Edges added: N (internal + cross-scholar)
=== END BATCH SUMMARY ===

If any issues, print them under === ISSUES === before the summary.
PROMPT
)
    run_hermes "phase1-extract" "$extract_prompt_file"

    # ── Phase 2: Quality Review ──────────────────────────────────
    review_prompt_file=$(write_prompt "phase2-review" <<PROMPT
Quality review for claims extraction batch $BATCH_NUM. Truth Project at $PROJECT_DIR.

The following notes were just processed:
$note_list

Check every claim file just created:
- All required frontmatter fields present (claim_id, statement, confidence, tags)
- At least one topic tag and one evidence tag
- Evidence section has structured content (bullet points or tables, not just a paragraph)
- Edges section has wikilinks to other claims (not just placeholders or HTML comments)
- Edge descriptions name scholars and arguments, not just claim slugs

Check every chapter note updated:
- claims_status frontmatter present with correct count
- Compact summaries have correct wikilinks (verify files exist)
- Cross-cutting assessment tables preserved

Check for content degradation: are later claims in each note as thorough as the first?

Print a per-note pass/fail using this exact format:

=== QUALITY REVIEW ===
TITLE: PASS — N claims, all frontmatter valid, N edges
TITLE: FAIL — specific issues found
=== END QUALITY REVIEW ===

If any note fails, describe exactly what is broken so the next session can fix it.
PROMPT
)
    run_hermes "phase2-review" "$review_prompt_file"

    # Check for failures in quality review
    if ! $DRY_RUN; then
        # Only check FAIL between the quality review markers — the prompt
        # template itself contains "FAIL" as a format example, so we must
        # scope the grep to the model's actual output, not the prompt.
        local log_failures
        log_failures=$(awk '/=== QUALITY REVIEW ===/{found=1; next} /=== END QUALITY REVIEW ===/{found=0} found && /FAIL/' "$TMPDIR/hermes-extract-phase2-review.log")
        if [[ -n "$log_failures" ]]; then
            log "QUALITY GATE FAILED — stopping loop"
            echo "$log_failures"
            die "Quality review failed. Review output above and fix before continuing."
        fi
        log "Phase 2: All notes PASS"
    fi

    # ── Phase 3: Finalize ────────────────────────────────────────
    finalize_prompt_file=$(write_prompt "phase3-finalize" <<PROMPT
Finalize claims extraction batch $BATCH_NUM. Truth Project at $PROJECT_DIR.

The following notes were processed:
$note_list

Step 1 - Cross-scholar edge pass:
Re-read the newly created claim files. Add edges between scholars within this batch: contradictions, supports, dependencies. Focus on threads that connect scholars. Also check if any of the new claims should edge to prior-session claims already in notes/claims/ and add those edges.

Step 2 - Update progress:
- Check off each processed note in notes/claims-progress.md ([] becomes [x])
- Update the Status Summary numbers
- Append a session log entry

Step 3 - Git commit:
  cd $PROJECT_DIR
  git add notes/claims/ notes/theology/ notes/claims-progress.md
  git commit -m "claims: extracted N claims from SCHOLARS (session $BATCH_NUM)"

Step 4 - Next batch suggestion:
Read claims-progress.md, find the next 3 unchecked notes, and suggest them. Include the strategic rationale (thread-first selection, edge compounding).

Print using this exact format:

=== FINALIZE COMPLETE ===
Batch $BATCH_NUM committed: N claims from SCHOLARS
Notes remaining: N
Next batch: NOTE1, NOTE2, NOTE3 — RATIONALE
=== END FINALIZE ===
PROMPT
)
    run_hermes "phase3-finalize" "$finalize_prompt_file"

    # ── loop control ─────────────────────────────────────────────
    BATCHES_DONE=$((BATCHES_DONE + 1))
    BATCH_NUM=$((BATCH_NUM + 1))

    if [[ $BATCHES_DONE -ge $STOP_AFTER ]]; then
        log "Stop-after limit reached ($STOP_AFTER batches). Exiting."
        break
    fi

    log "──────────────────────────────────────────────────"
done

log "Harness finished. $BATCHES_DONE batches processed."
