# execute_code Pattern for Batch Claim Creation

Session 1 proved that creating claim files via a single `execute_code` script is faster and cleaner than serial `write_file` calls. Use this pattern when a batch has 3+ notes (typically 8-15 claim files).

## Template

```python
from hermes_tools import write_file
from datetime import date

today = str(date.today())
claims_dir = "/Users/littleseneca/Projects/Personal/Truth/notes/claims"

write_file(f"{claims_dir}/claim-slug-goes-here.md", f"""---
tags:
  - type/claim
  - topic/primary-topic
  - topic/secondary-topic
  - evidence/evidence-type
  - scholar/scholar-slug
  - source/book-slug
  - truth-project
claim_id: "scholar-book-chapter.number"
statement: "One-sentence claim statement"
confidence: "high"
confidence_rationale: "One sentence rationale"
claim_type: "textual"
source_note: "[[Chapter Note Title]]"
created: {today}
updated: {today}
status: active
---

# claim_id: Statement

**Source:** [[Chapter Note Title]] — Scholar, *Book* (Year), Chapter

## The Claim
...full content...

## Evidence
...structured evidence...

## Confidence
**Rating:** rating
**Rationale:** rationale

## Stakes
...what's at stake...

## Disagreement
**Who disagrees:** ...
**Alternative reading:** ...

## Edges
**Depends on:** ...
**Supports:** ...
**Contradicts:** ...
**Challenged by:** ...
**Primary sources:** ...

## Assessment
Graham's evaluation.
""")

print("Claim slug done")
```

## Key Details

- Use `f"""..."""` (triple-quoted f-string) for the file content — it handles embedded quotes and newlines naturally
- Use `{today}` for the date — consistent across all files in the batch
- Print a simple marker after each write so the script output shows progress
- One `execute_code` call per scholar (4-5 claims) keeps each script readable
- The `write_file` from `hermes_tools` handles directory creation automatically

## Session 1 Example

Session 1 processed 12 claims (4 Smith, 4 Römer, 4 Day) using three `execute_code` scripts:

1. Smith: 3 files created (claim 2 already existed as example), ~150 lines of Python
2. Römer: 4 files created, ~120 lines of Python
3. Day: 4 files created, ~140 lines of Python

Each script completed in under 0.5 seconds. The alternative — 11 sequential `write_file` tool calls — would have taken 11+ turns with context accumulation between each.
