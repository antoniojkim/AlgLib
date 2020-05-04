# Single Source Shortest Path for DAG

In a DAG with arbitrary weights:

Input: A DAG `G(V, E)`, a source `s` and arbitrary edge weights `w(u, v)`

Output: Short paths (and distances) to every other node `v ∈ V`

## Algorithm

We can get the shortest paths from a single source using dynamic programming.

The idea is that we [topologically order](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Topological%20Sort) `G`.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Shortest%20Path/SSSP%20DAG/ssspdag.py#L17)

Here is an implementation of the algorithm:

```python
def sssp_dag(G: Graph, s: str) -> Dict[str, List[str]]:
    f = topsort(G)
    SD = {v: (0 if v == s else inf) for v in f}  # Shortest Distances
    paths = {v: [] for v in f}

    for v in f:
        curpath = []
        for u in G.get_in_edges(v):
            tmp = SD[u] + G.get_weight(u, v)
            if tmp < SD[v]:
                SD[v] = tmp
                curpath = paths[u]

        paths[v].extend(curpath)
        paths[v].append(v)

    return paths
```

### Runtime

Topological sort: `O(n+m)`

Inner loops: `∑_(v∈V) in-deg(v) = m`

**Overall**: `O(n+m)`
