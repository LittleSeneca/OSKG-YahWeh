# Programmatic Canvas Generation

Generate Obsidian Canvas JSON files via `execute_code` + Python when the canvas has more than ~5 nodes or requires geometric layout (radial, grid, tree).

## When to use this

- Radial/concentric ring layouts (cascade maps, dependency trees)
- Multi-level graphs with 20+ nodes
- Any layout where hand-computing positions is error-prone
- Bulk node generation from structured source data

## Core pattern

```python
import json, math

nodes = []
edges = []

def add_node(id, text, x, y, width, height, color):
    nodes.append({
        "id": id, "type": "text", "text": text,
        "x": round(x), "y": round(y),
        "width": width, "height": height, "color": color
    })

def add_edge(id, from_node, to_node, from_side, to_side, label=""):
    edges.append({
        "id": id, "fromNode": from_node, "toNode": to_node,
        "fromSide": from_side, "toSide": to_side, "label": label
    })

# Build nodes and edges here...

canvas = {"nodes": nodes, "edges": edges}
with open(output_path, "w") as f:
    json.dump(canvas, f, indent="\t")  # tab indent matches Obsidian native
```

## Radial/concentric ring layout

```python
# Place N nodes equally around a circle of given radius
radius = 350
for i in range(num_nodes):
    angle = math.radians(i * (360 / num_nodes) - 90)  # -90 starts from top
    x = radius * math.cos(angle) - width / 2   # subtract half-width: x,y is top-left
    y = radius * math.sin(angle) - height / 2
    add_node(f"n{i}", text, x, y, width, height, color)
```

## Key pitfalls

1. **x,y is top-left corner, not center.** Always subtract `width/2` and `height/2` after computing the desired center position.

2. **Center the root node properly.** For a root at origin with dimensions w×h:
   ```python
   x = -w / 2
   y = -h / 2
   ```

3. **Use `json.dump` with tab indent.** Obsidian's native `.canvas` format uses `\t` indentation. `json.dump(canvas, f, indent="\t")` produces clean, readable output.

4. **Wikilinks are relative from vault root.** `[[notes/synthesis/phase2-cascade-trees]]` resolves to the vault root, regardless of where the `.canvas` file lives.

5. **Validate after writing.** Re-read the file with `json.load()` and verify node counts, positions, and edge connectivity before reporting success.

## Edge routing for radial layouts

For edges in a radial layout, determine the `fromSide` and `toSide` based on relative positions:

```python
if from_node_is_right_of_to_node:
    from_side, to_side = "left", "right"
else:
    from_side, to_side = "right", "left"
```

For parent-to-child edges in a cascade (parent at inner ring, child at outer ring), `fromSide="right"`, `toSide="left"` is a safe default that Obsidian renders cleanly.

## Color conventions

| Color | Use |
|-------|-----|
| `"1"` (red) | Root/center/hinge node |
| `"2"` (orange) | Fault lines, threat zones, overlays |
| `"3"` (yellow) | Level 1 direct dependents |
| `"4"` (green) | Level 2 dependents / settled convergences |
| `"5"` (cyan) | Deepest chain / reference nodes |
| `"6"` (purple) | Conflicted level / critical children |

## Multi-level cascade example

For a 5-level cascade (Hinge #3, 65 dependents):
- L0: 1 node at origin, color `"1"`
- L1: 8 nodes at r=350, color `"3"`, angles 0°/45°/90°/...
- L2: 7 nodes at r=650, color `"4"`, angles distributed
- L3: 5 nodes at r=950, color `"6"`, critical children with red-border indicators
- L4: 3 nodes at r=1250, color `"5"`, deepest chain
- Overlay: threat zone node at color `"2"`, positioned near the center

Total: 25 nodes, ~40 edges. Generated in a single `execute_code` call.
