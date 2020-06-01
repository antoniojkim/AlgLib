# Kosaraju's Algorithm

Kosaraju's algorithm finds the strongly connected components (SCC) in a graph.

## Definition (Strongly Connected Components)

Given a directed grapoh `G(V, E)`, two vertices `u` and `v` are **strongly connected** if and only if there exists a path going from `u` to `v` and there exists a path going from `v` to `u`.

A SCC of `G` is a set `C ⊆ V` such that

1. `∀(u, v) ∈ C`, `u` and `v` are strongly connected
2. `C` is non-empty and maximal, i.e. `∀ v ∈ V-C`, `v` is not strongly connected to any vertex in `C`

### Two-Tiered Structure

Given a directed graph `G(V, E)`, consider `G_SCC`: the meta-graph of its strongly connected components. We call this the "SCC graph of `G`".

Notice that each directed graph has a second higher-level structure which is a DAG.

## Algorithm

Kosaraju's algorithm is as follows: Given a directed graph `G(V, E)`

1. run DFS on the reversed graph (identical graph where every edge direction is flipped) and keep the "finishing times" `f`.
2. run DFS/BFS in `G`:
    * pick start vertices by decreasing `f` times
    * propagate the ID of each new start vertex during traversal

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Kosaraju's%20Algorithm/kosaraju.py#L14)

Here is an implementation of Kosaraju's algorithm:

```python
def kosaraju(G: Graph) -> List[List[str]]:
    Grev = reverse_graph(G)
    f = topsort(Grev)

    visited = set()
    scc = []

    def DFS(u):
        visited.add(u)
        scc[-1].append(u)

        for v in G[u]:
            if v not in visited:
                DFS(v)

    for v in f:
        if v not in visited:
            scc.append([])
            DFS(v)

    return scc
```
