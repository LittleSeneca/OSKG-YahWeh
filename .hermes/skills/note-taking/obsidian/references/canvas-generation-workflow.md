# Programmatic Canvas Generation from Structured Data

Build Obsidian Canvas files from synthesis documents, research data, or knowledge graph output.

## When to use this

- Building evidence-density maps, convergence maps, or domain maps from structured research
- Creating multi-tier Canvas layouts from capstone/synthesis data
- Any Canvas with 10+ nodes and explicit tier/band layout

## Workflow

### 1. Load source data

Read the synthesis documents that contain the structured data the Canvas will map. For OSKG-YahWeh, this means the capstone (Part 6 for evidence density) and Phase 4 convergence data.

### 2. Study an existing Canvas for format

Read an existing `.canvas` file from the project to match the exact JSON formatting conventions (tabs vs. spaces, inline vs. pretty-print, node content style). The OSKG-YahWeh canvases use compact single-line JSON with tabs for indentation.

### 3. Plan the node layout

**Tiered layout:** Assign nodes to horizontal bands based on their tier (density, confidence, priority). Space nodes evenly within each band. Use consistent y-coordinates per tier and spread x-coordinates with enough gap to prevent overlap.

Calculate spacing:
```
For N nodes in a band with width W:
  spacing = (total_range) / (N - 1)
  x_positions = [start + i * spacing for i in range(N)]
```

Verify no overlap: nodes at adjacent positions must satisfy `|x1 - x2| > (width1 + width2) / 2`.

**Node sizing:** Increase width/height for higher-tier nodes to signal importance. Typical: Tier 1 at 370px wide, Tier 3 at 350px wide. Heights vary by content length — estimate ~18px per line of text.

### 4. Draft node content

Each node text is markdown. For evidence-density canvases, the convention is:

```
## Domain Name

**X evidence types · Y supports · Z contradicts**
One-line summary of finding.

### Evidence Types
- Type 1: specific data points
- Type 2: specific data points

### Key Scholars
Scholar1 (CONFIDENCE, support_count) · Scholar2 (CONFIDENCE)

### Key Challenges
- Challenge 1
- Challenge 2

⚠️ **Dissent flags** where applicable (Kaufmann, Fleming, etc.)
[[wikilink-to-source]]
```

Keep node text self-contained — the Canvas is browsable without opening linked notes.

### 5. Design edges

Edges should include:
- **Dependency chain:** A → B → C vertical path through tiers
- **Lateral connections:** cross-domain relationships at same tier
- **Diagonal connections:** cross-tier relationships not in the main chain

Every edge needs a descriptive label (not just "relates to"). Use `fromSide`/`toSide` (`top`, `bottom`, `left`, `right`) to control arrow placement and reduce visual clutter.

### 6. Write and validate

Write the full `.canvas` JSON to the project's `canvases/` directory. Before declaring done, run a Python validation script:

```python
import json
with open('path/to/canvas.canvas') as f:
    data = json.load(f)

nodes = data['nodes']
edges = data['edges']
node_ids = {n['id'] for n in nodes}

# Verify counts
print(f'Nodes: {len(nodes)}, Edges: {len(edges)}')

# Verify tier assignment (y-coordinate bands)
for n in nodes:
    tier = 'Tier 1' if n['y'] <= -300 else 'Tier 2' if n['y'] <= 300 else 'Tier 3'
    print(f'{n["id"]}: {tier}, color={n["color"]}, size={n["width"]}x{n["height"]}')

# Verify all edge references are valid
for e in edges:
    assert e['fromNode'] in node_ids, f'BROKEN: {e["fromNode"]}'
    assert e['toNode'] in node_ids, f'BROKEN: {e["toNode"]}'

# Verify required edges exist
required = [('source-a', 'target-b'), ...]
for src, dst in required:
    found = any(e['fromNode'] == src and e['toNode'] == dst for e in edges)
    print(f'{"✓" if found else "✗"} Required: {src} → {dst}')
```

### 7. Record the session

Create a session note and artifact note in the Obsidian vault per `obsidian-session-record` conventions. Link the artifact note to the Canvas file path.

## Pitfalls

### Edge references must match node IDs exactly

A typo in `fromNode` or `toNode` creates a dead edge. The validation script catches this — always run it.

### Node overlap from insufficient spacing (MOST COMMON FAILURE MODE)

Canvas nodes overlap when either horizontal or vertical spacing is too tight. Overlap produces stacked/illegible cards and edges that route through card bodies. **Always run a bounding-box overlap check** before declaring done.

**Horizontal spacing:** For same-row nodes with width W, center-to-center gap must be at least `W + 80` (for edge lanes). With 380px-wide nodes, that means 460px between centers. 4 nodes across one row needs ~1800px total horizontal range.

**Vertical spacing (critical):** Ensure `row_N.y + row_N.height + gap < row_{N+1}.y`. A 40px gap between rows is the minimum for clean edge routing. Never let bounding boxes touch or overlap — Obsidian will stack cards on top of each other.

**Estimating node height from text content:** Count lines in the node's markdown text, multiply by ~20px per line, add 80px padding for headers and margins. A 14-line node needs at minimum 360px height. A 20-line position card with bullet lists needs 480px. When in doubt, round up — text cut off at the bottom is the most common format complaint.

**Practical sizing from OSKG canvases:**
- Evidence/concept nodes (8-14 lines): 380w × 420h
- Position/argument nodes (15-20 lines): 420w × 440h
- Center/root nodes (6-10 lines): 440w × 300h
- Grammar/dispute nodes (12-18 lines): 500w × 380h
- Complication/counter nodes (10-14 lines): 380w × 360h

**Validation script:** After writing the canvas, run a Python overlap check:

```python
import json
with open('path/to/canvas.canvas') as f:
    data = json.load(f)
nodes = data['nodes']
for i, n1 in enumerate(nodes):
    for j, n2 in enumerate(nodes):
        if i >= j: continue
        if (n1['x'] < n2['x'] + n2['width'] and n1['x'] + n1['width'] > n2['x'] and
            n1['y'] < n2['y'] + n2['height'] and n1['y'] + n1['height'] > n2['y']):
            print(f'OVERLAP: {n1[\"id\"]} vs {n2[\"id\"]}')
```

### Inconsistent JSON formatting

Obsidian is picky about Canvas JSON. Match the existing project canvases exactly — if they use tabs, use tabs. If they inline everything, don't pretty-print.

### Wikilinks in Canvas nodes must be absolute from project root

`[[notes/synthesis/capstone-what-does-this-mean]]` works. Relative wikilinks or vault-absolute paths may not resolve.

### Color scheme differs from the vault-level convention

The vault-level color scheme (1=red root, 4=green key-takeaway) is for study vaults. Evidence-density canvases can repurpose colors to mean density tiers: 4=highest, 3=medium, 2=lower. Use whatever makes the visual hierarchy clear.
