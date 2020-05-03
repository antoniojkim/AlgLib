# Topological Sorting of a Directed Acyclic Graph (DAG)

## Definition

Input: A graph that is a DAG

Output: Vertices in sorted order such that each each vertex `v` appears after its dependencies.

### Formal Definition

Given an input DAG `G(V, E)` order the nodes such that if `(u, v) ∈ E`, then `u` appears before `v`

## Implementation

The following is an implementation of the topological sort using DFS:

```python
def topsort(G: Graph) -> List[str]:
    i = 0
    visited = set()
    ft = {v: None for v in G.get_vertices()}  # finishing time

    def DFS(u):
        nonlocal i, visited, ft

        visited.add(u)

        for v in G[u]:
            if v not in visited:
                DFS(v)

        ft[u] = i
        i += 1

    for u in G.get_vertices():
        if u not in visited:
            DFS(u)

    return sorted(ft, key=ft.get, reverse=True)
```
