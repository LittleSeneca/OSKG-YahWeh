#!/usr/bin/env python3
"""Run quality metrics on a set of book notes for the final retrospective.

Usage: python3 scripts/retrospective_metrics.py NOTES_DIR PREFIX

Example: python3 scripts/retrospective_metrics.py \
  /Users/littleseneca/Projects/Personal/Truth/notes/theology/ \
  "Smith Origins"

Reports: file count, total KB, total claims, claim range, cross-ref counts,
and verifies that every note has an Overall Assessment table and What's at Stake sections.
"""

import os
import sys

def metrics(notes_dir, prefix):
    files = {}
    for f in os.listdir(notes_dir):
        if f.startswith(prefix) and f.endswith(".md"):
            path = os.path.join(notes_dir, f)
            size = os.path.getsize(path)
            with open(path) as fh:
                content = fh.read()
                claim_count = content.count("## Claim ")
                cross_refs = content.count("[[")
                has_assessment = (
                    "Overall Assessment" in content
                    or "Cross-Cutting Assessment" in content
                    or "Chapter" in content and "Overall Assessment" in content
                )
                has_stakes = "**What's at stake:**" in content
                files[f] = {
                    "bytes": size,
                    "claims": claim_count,
                    "cross_refs": cross_refs,
                    "assessment": has_assessment,
                    "stakes_check": has_stakes,
                }

    if not files:
        print(f"No files found matching prefix '{prefix}' in {notes_dir}")
        return

    print(f"{'Chapter':<55} {'KB':>5} {'Claims':>7} {'XRefs':>6} {'Assess':>8} {'Stakes':>7}")
    print("-" * 95)
    total = 0
    for f in sorted(files.keys()):
        d = files[f]
        total += d["claims"]
        short = f.replace(f"{prefix} — ", "").replace(".md", "")
        if len(short) > 52:
            short = short[:49] + "..."
        print(f"{short:<55} {d['bytes']//1024:>5} {d['claims']:>7} {d['cross_refs']:>6} {str(d['assessment']):>8} {str(d['stakes_check']):>7}")

    print("-" * 95)
    total_kb = sum(d["bytes"] for d in files.values()) // 1024
    print(f"{'TOTAL':<55} {total_kb:>5} {total:>7}")
    print(f"\nNotes written: {len(files)}")
    print(f"Total claims: {total}")
    print(f"Average claims/note: {total/len(files):.1f}")
    print(f"All have assessments: {all(d['assessment'] for d in files.values())}")
    print(f"All have stakes sections: {all(d['stakes_check'] for d in files.values())}")

    # Taper check
    sizes = [(f, d["bytes"]) for f, d in files.items()]
    if len(sizes) >= 2:
        sizes.sort()
        first_size = sizes[0][1]
        last_size = sizes[-1][1]
        if last_size < first_size * 0.5:
            print(f"\n⚠️  TAPER WARNING: last note ({last_size//1024}KB) is less than half of first ({first_size//1024}KB)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: retrospective_metrics.py NOTES_DIR PREFIX")
        sys.exit(1)
    metrics(sys.argv[1], sys.argv[2])
