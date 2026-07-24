#!/usr/bin/env python3
"""Phase 4: Genuine Unknowns and Convergence Points analysis.

Parses all claim files, builds the edge graph, and identifies:
- Part A: Genuine unknowns (bidirectional MEDIUM+ contradiction pairs)
- Part B: Convergence points (5+ HIGH+ supports, zero MEDIUM+ contradicts)
"""

import re
import os
import json
from pathlib import Path
from collections import defaultdict

CLAIMS_DIR = Path("/Users/littleseneca/Projects/Personal/Truth/notes/claims")

# Confidence hierarchy: numeric values for comparison
CONFIDENCE_MAP = {
    "very-low": 0,
    "low": 1,
    "low-medium": 2,
    "medium": 3,
    "medium-high": 4,
    "high": 5,
    "very-high": 6,
}

def parse_frontmatter(text):
    """Parse YAML frontmatter from markdown text."""
    match = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not match:
        return {}
    fm = match.group(1)
    data = {}
    # Simple key-value parser (avoids yaml dependency)
    current_key = None
    for line in fm.split('\n'):
        # Check for key: value
        kv = re.match(r'^(\w[\w_]*):\s*(.*)', line)
        if kv:
            current_key = kv.group(1)
            val = kv.group(2).strip()
            # Remove quotes
            val = val.strip('"').strip("'")
            data[current_key] = val
        elif current_key and line.strip().startswith('- '):
            # List continuation - not critical for our purposes
            pass
    return data


def extract_tags(text):
    """Extract tags from markdown body or frontmatter - specifically evidence/ and scholar/ tags."""
    tags = []
    for line in text.split('\n'):
        # Frontmatter tags: "  - evidence/biblical-text"
        m = re.match(r'\s*-\s+(evidence/\S+|scholar/\S+)', line)
        if m:
            tags.append(m.group(1))
    return tags


def parse_edges(text):
    """Extract edges from the Edges section."""
    edges = {
        "depends_on": [],
        "supports": [],
        "contradicts": [],
        "challenged_by": [],
    }

    # Find the Edges section
    edges_start = text.find("## Edges")
    if edges_start == -1:
        return edges

    edges_text = text[edges_start:]

    current_section = None
    for line in edges_text.split('\n'):
        line = line.strip()
        # Detect section headers
        if line.startswith("**Depends on:**"):
            current_section = "depends_on"
            continue
        elif line.startswith("**Supports:**"):
            current_section = "supports"
            continue
        elif line.startswith("**Contradicts:**"):
            current_section = "contradicts"
            continue
        elif line.startswith("**Challenged by:**"):
            current_section = "challenged_by"
            continue
        elif line.startswith("**Primary sources:**"):
            current_section = None
            continue
        elif line.startswith("**") and line.endswith(":**"):
            current_section = None
            continue

        if current_section and line:
            # Extract wikilinks: [[claim-name]] or [[claim-name]] (id)
            # Also handle plain text wikilinks without brackets
            wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', line)
            for wl in wikilinks:
                wl = wl.strip()
                # Skip non-claim wikilinks (source references, primary sources)
                if not wl.startswith('claim-') and not wl.startswith('../'):
                    # Could be a reference like 'kuntillet-ajrud-inscriptions' - skip
                    if any(wl.startswith(p) for p in ['kuntillet', 'khirbet', 'ugaritic', 'deut-', 'soleb', 'arad']):
                        continue
                if wl.startswith('claim-'):
                    edges[current_section].append(wl)
                # Also check for claim_id pattern in parentheses
                cid_match = re.search(r'\(([a-z]+-[a-z]+-[\d.]+)\)', line)
                if cid_match:
                    cid = cid_match.group(1)
                    if cid not in edges[current_section]:
                        edges[current_section].append(cid)

    return edges


def main():
    # Phase 1: Parse all claims
    claims = {}
    slug_to_id = {}
    id_to_slug = {}

    print(f"Parsing claims from {CLAIMS_DIR}...")
    for fpath in CLAIMS_DIR.glob("claim-*.md"):
        slug = fpath.stem  # claim-asherah-was-yahwistic-symbol
        text = fpath.read_text()

        fm = parse_frontmatter(text)
        claim_id = fm.get("claim_id", "")
        confidence = fm.get("confidence", "medium")
        statement = fm.get("statement", "")
        claim_type = fm.get("claim_type", "unknown")
        status = fm.get("status", "active")

        # Only count active claims
        if status != "active":
            continue

        tags = extract_tags(text)
        edges = parse_edges(text)

        claims[claim_id] = {
            "slug": slug,
            "claim_id": claim_id,
            "confidence": confidence,
            "confidence_val": CONFIDENCE_MAP.get(confidence, 3),
            "statement": statement,
            "claim_type": claim_type,
            "tags": tags,
            "edges": edges,
        }
        slug_to_id[slug] = claim_id
        id_to_slug[claim_id] = slug

    print(f"Parsed {len(claims)} active claims")

    # Build slug-to-id mapping for ALL files (including inactive ones for edge resolution)
    for fpath in CLAIMS_DIR.glob("claim-*.md"):
        slug = fpath.stem
        if slug not in slug_to_id:
            text = fpath.read_text()
            fm = parse_frontmatter(text)
            claim_id = fm.get("claim_id", "")
            if claim_id:
                slug_to_id[slug] = claim_id

    # Phase 2: Resolve edges
    # Convert slug references in edges to claim_ids
    for cid, claim in claims.items():
        for edge_type in ["depends_on", "supports", "contradicts", "challenged_by"]:
            resolved = []
            for ref in claim["edges"][edge_type]:
                # Try claim_id format first
                if ref in claims:
                    resolved.append(ref)
                elif ref in slug_to_id:
                    resolved.append(slug_to_id[ref])
                # else: edge points to a claim we didn't parse (might be inactive or missing)
            claim["edges"][edge_type] = list(set(resolved))  # deduplicate

    # Phase 3: Build reverse edge index
    # "contradicted_by" = reverse of "contradicts"
    # "supported_by" = reverse of "supports"
    # "challenged_by" is already a forward edge (who challenges this claim)
    reversed_contradicts = defaultdict(set)
    reversed_supports = defaultdict(set)
    reversed_challenges = defaultdict(set)

    for cid, claim in claims.items():
        for target in claim["edges"]["contradicts"]:
            reversed_contradicts[target].add(cid)
        for target in claim["edges"]["supports"]:
            reversed_supports[target].add(cid)
        for target in claim["edges"]["challenged_by"]:
            reversed_challenges[target].add(cid)

    # Phase 4: Find Genuine Unknowns (Part A)
    # Bidirectional contradicts where BOTH claims have confidence >= MEDIUM
    genuine_unknowns = []
    seen_pairs = set()

    for cid_a, claim_a in claims.items():
        if claim_a["confidence_val"] < 3:  # MEDIUM = 3
            continue
        for cid_b in claim_a["edges"]["contradicts"]:
            if cid_b not in claims:
                continue
            claim_b = claims[cid_b]
            if claim_b["confidence_val"] < 3:
                continue
            # Check bidirectional
            if cid_a in claim_b["edges"]["contradicts"]:
                pair_key = tuple(sorted([cid_a, cid_b]))
                if pair_key not in seen_pairs:
                    seen_pairs.add(pair_key)
                    # Determine which claim is the "pro" and "con" side
                    # Count support edges to see which side has more
                    supports_a = len(reversed_supports.get(cid_a, set()))
                    supports_b = len(reversed_supports.get(cid_b, set()))
                    
                    # Identify evidence types
                    evidence_a = [t for t in claim_a["tags"] if t.startswith("evidence/")]
                    evidence_b = [t for t in claim_b["tags"] if t.startswith("evidence/")]
                    scholar_a = [t.replace("scholar/", "") for t in claim_a["tags"] if t.startswith("scholar/")]
                    scholar_b = [t.replace("scholar/", "") for t in claim_b["tags"] if t.startswith("scholar/")]

                    # Are they interpreting the SAME evidence or DIFFERENT evidence?
                    ev_a_set = set(evidence_a)
                    ev_b_set = set(evidence_b)
                    same_evidence = bool(ev_a_set & ev_b_set)
                    different_evidence = bool(ev_a_set - ev_b_set) or bool(ev_b_set - ev_a_set)

                    genuine_unknowns.append({
                        "claim_a": cid_a,
                        "statement_a": claim_a["statement"],
                        "scholar_a": scholar_a,
                        "confidence_a": claim_a["confidence"],
                        "evidence_a": evidence_a,
                        "supports_a": supports_a,
                        "claim_b": cid_b,
                        "statement_b": claim_b["statement"],
                        "scholar_b": scholar_b,
                        "confidence_b": claim_b["confidence"],
                        "evidence_b": evidence_b,
                        "supports_b": supports_b,
                        "same_evidence": same_evidence,
                        "different_evidence": different_evidence,
                    })

    # Sort by how balanced the support is (closer ratio = more genuine unknown)
    # Actually sort by minimum of the two confidences (both must be high)
    genuine_unknowns.sort(key=lambda x: (
        min(CONFIDENCE_MAP.get(x["confidence_a"], 0), CONFIDENCE_MAP.get(x["confidence_b"], 0)),
        abs(x["supports_a"] - x["supports_b"])  # Lower difference = more balanced
    ), reverse=True)

    # Phase 5: Convergence Points (Part B)
    # For the top 25 hinge claims, check for 5+ HIGH+ supports and zero MEDIUM+ contradicts
    # The top 25 hinge claim_ids from Phase 1 inventory
    top_25_ids = [
        "sommer-bog-intro.1",
        "sommer-bog-1.1", 
        "day-ygc-1.1",
        "kaufmann-ri-1.2",
        "stav-god-pro-1.2",
        "kaufmann-ri-2.1",  # Torah is pre-prophetic
        "heiser-ur-14.1",  # Divine council pervasive
        "smith-ehg-3.1",  # Asherah was Yahwistic symbol
        "smith-ehg-1.1",  # Ugaritic texts best background
        "albertz-hir-4.2",  # Deuteronomic theology mediating synthesis
        "albertz-hir-2.1",  # Monarchy decisive challenge
        "albertz-hir-1.2",  # Patriarchal religion substratum
        "albertz-hir-1.3",  # Internal religious pluralism
        "smith-ehg-1.2",  # Israelite culture was Canaanite
        "kaufmann-ri-1.1",  # God's absolute supremacy
        "tigay-nog-1.1",  # Epigraphic onomasticon
        "lewis-ocg-4.1",  # El was original god
        "kaufmann-ri-1.3",  # Metadivine realm
        "smith-obm-2.1",  # Center-periphery scheme
        "day-ygc-1.3",  # Divine council 70 sons of El
        "heiser-ur-16.1",  # Babel nations assigned 
        "smith-obm-2.2",  # Four-tier pantheon
        "albertz-hir-6.1",  # Exile differential impact
        "romer-inv-6-7.1",  # Biblical pure Yahwism Dtr propaganda
        "smith-ehg-2.2",  # Yahweh absorbed Baal
    ]

    convergence_points = []
    for hinge_id in top_25_ids:
        if hinge_id not in claims:
            # Try to find by slug
            found = False
            for cid, claim in claims.items():
                if hinge_id in cid:
                    hinge_id = cid
                    found = True
                    break
            if not found:
                print(f"  WARNING: Hinge claim {hinge_id} not found in parsed claims")
                continue

        claim = claims[hinge_id]
        
        # Count HIGH+ supports
        supporters = reversed_supports.get(hinge_id, set())
        high_supporters = set()
        for sid in supporters:
            if sid in claims and claims[sid]["confidence_val"] >= 5:  # HIGH
                high_supporters.add(sid)
        
        # Count MEDIUM+ contradicts
        contra_at_medium_plus = set()
        # Who contradicts this claim?
        for con_id in reversed_contradicts.get(hinge_id, set()):
            if con_id in claims and claims[con_id]["confidence_val"] >= 3:
                contra_at_medium_plus.add(con_id)
        
        # Also check challenged_by
        # "Challenged by" from the claim itself, and from the reverse
        for ch_id in claim["edges"]["challenged_by"]:
            if ch_id in claims and claims[ch_id]["confidence_val"] >= 3:
                contra_at_medium_plus.add(ch_id)
        for ch_id in reversed_challenges.get(hinge_id, set()):
            if ch_id in claims and claims[ch_id]["confidence_val"] >= 3:
                contra_at_medium_plus.add(ch_id)

        # Determine scholar names from supporters
        scholar_set = set()
        for sid in high_supporters:
            s_tags = claims[sid]["tags"]
            for t in s_tags:
                if t.startswith("scholar/"):
                    scholar_set.add(t.replace("scholar/", ""))

        # Evidence types for the claim
        evidence_types = [t.replace("evidence/", "") for t in claim["tags"] if t.startswith("evidence/")]

        is_convergence = len(high_supporters) >= 5 and len(contra_at_medium_plus) == 0

        convergence_points.append({
            "claim_id": hinge_id,
            "statement": claim["statement"],
            "confidence": claim["confidence"],
            "high_supporters": len(high_supporters),
            "scholars": sorted(scholar_set),
            "evidence_types": evidence_types,
            "contradictions_medium_plus": len(contra_at_medium_plus),
            "is_convergence": is_convergence,
        })

    # Print results
    print("\n" + "="*80)
    print("PART A: GENUINE UNKNOWNS (Bidirectional MEDIUM+ Contradiction Pairs)")
    print("="*80)
    print(f"\nFound {len(genuine_unknowns)} bidirectional contradiction pairs at MEDIUM+ confidence\n")

    for i, gu in enumerate(genuine_unknowns):
        print(f"--- Genuine Unknown #{i+1} ---")
        print(f"Question: Is {gu['statement_a'][:100]}... OR {gu['statement_b'][:100]}...?")
        print(f"  Side A: {', '.join(gu['scholar_a'])} (confidence: {gu['confidence_a']}, supports: {gu['supports_a']})")
        print(f"    Evidence: {', '.join(gu['evidence_a']) or 'none tagged'}")
        print(f"    Statement: {gu['statement_a'][:200]}")
        print(f"  Side B: {', '.join(gu['scholar_b'])} (confidence: {gu['confidence_b']}, supports: {gu['supports_b']})")
        print(f"    Evidence: {', '.join(gu['evidence_b']) or 'none tagged'}")
        print(f"    Statement: {gu['statement_b'][:200]}")
        print(f"  Same evidence: {gu['same_evidence']}, Different evidence: {gu['different_evidence']}")
        print()

    print("\n" + "="*80)
    print("PART B: CONVERGENCE POINTS (5+ HIGH+ supports, zero MEDIUM+ contradictions)")
    print("="*80)

    conv = [cp for cp in convergence_points if cp["is_convergence"]]
    non_conv = [cp for cp in convergence_points if not cp["is_convergence"]]

    print(f"\nCONVERGENCE POINTS ({len(conv)}):")
    for cp in conv:
        print(f"  ✓ {cp['claim_id']}: {cp['statement'][:120]}")
        print(f"    Scholars: {', '.join(cp['scholars'])}")
        print(f"    HIGH+ supports: {cp['high_supporters']}, MEDIUM+ contradicts: {cp['contradictions_medium_plus']}")
        print(f"    Evidence: {', '.join(cp['evidence_types']) or 'none tagged'}")

    print(f"\nNON-CONVERGENCE (failing threshold) ({len(non_conv)}):")
    for cp in non_conv:
        reason = []
        if cp["high_supporters"] < 5:
            reason.append(f"only {cp['high_supporters']} HIGH+ supports")
        if cp["contradictions_medium_plus"] > 0:
            reason.append(f"{cp['contradictions_medium_plus']} MEDIUM+ contradictions")
        print(f"  ✗ {cp['claim_id']}: {'; '.join(reason)}")
        print(f"    Scholars: {', '.join(cp['scholars'])}")
        print(f"    Statement: {cp['statement'][:120]}")

    # Output the summary as JSON for easier use
    output = {
        "genuine_unknowns": genuine_unknowns,
        "convergence_points": convergence_points,
    }
    return output


if __name__ == "__main__":
    main()
