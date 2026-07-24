# DAG Dependency Traversal for Claim Knowledge Graphs

When building cascade trees or dependency maps from a wikilink-based knowledge graph (claims depending on claims), the graph is a **DAG** (directed acyclic graph), not a tree. Many nodes have multiple parents. This creates a traversal-order trap.

## The Pitfall: DFS Buries Multi-Parent Nodes

If you traverse the graph depth-first (DFS), the first time you encounter a node determines its depth forever. When a claim depends on BOTH the hinge directly (level 1) AND a child of the hinge via a longer path (level 3), DFS may hit it via the longer path first — placing it at depth 3 when it should be at depth 1.

**Symptom**: dependency counts don't match the source data. Phase 1 says 10 dependents, your tree shows 3. The missing 7 are buried deeper in the tree, invisible as direct children.

**Root cause**: `visited` set prevents re-processing, so the first (deep) encounter wins.

## The Fix: BFS Discovers Shallowest Depth First

Breadth-first traversal processes all level-1 nodes before any level-2 nodes, guaranteeing each node is discovered at its shallowest possible depth.

```python
from collections import defaultdict, deque

depth_of = {root_slug: 0}
parent_of = {}  # slug -> shallowest parent slug
queue = deque([root_slug])

while queue:
    current = queue.popleft()
    current_depth = depth_of[current]
    if current_depth >= max_depth:
        continue
    for child_slug in dep_index.get(current, []):
        if child_slug not in depth_of:
            depth_of[child_slug] = current_depth + 1
            parent_of[child_slug] = current
            queue.append(child_slug)

# Then build tree: a child belongs to a parent only if
# parent_of[child] == parent AND depth_of[child] == depth_of[parent] + 1
```

## Verification

After BFS, spot-check: the number of nodes at level 1 in the tree MUST match the number of claims that have the hinge in their `Depends on` section. If they differ, your traversal is wrong.

## When to Use BFS vs DFS

| Goal | Use |
|------|-----|
| Cascade tree (what collapses if X breaks?) | **BFS** — shallowest = most direct impact |
| Deep-dive lineage (trace ALL paths from X to Y) | DFS + path tracking |
| Find all reachable nodes | Either, but BFS gives depth levels |
| Longest dependency chain | DFS with max-depth tracking |
