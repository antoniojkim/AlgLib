# Bellman-Ford Algorithm

Single source shortest path with negatives edges (but no negative cycles).

## Negative Weight Cycle

How can we define shortest paths, if there are negative weight cycles in the graph?
* Option 1: Standard definition: across any paths, from `s` to `t`, the one with the least cost (allows cycles)
    * Problem: Some paths will not exist (e.g. there is no shortest `s ⇝ y` path) because always make any path to `y` shortest with another turn around the cycle.
* Option 2: Don't allow paths to contain cycles.
    * Problem: Well-defined but very difficult to compute (NP-Complete)

Solution: Assume there are no negative weight cycles.

The cool part about the Bellman-Ford Algorithm is that it has "built-in" negative weight cycle detection.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Shortest%20Path/Bellman-Ford%20Algorithm/bellmanford.py#L15)

Here is an implementation of the algorithm:

```python
def bellman_ford(G: Graph, s: str) -> Dict[str, List[str]]:
    n = len(list(G.get_vertices()))
    A = [{v: np.inf for v in G.get_vertices()} for _ in range(n)]

    A[0][s] = 0

    paths = {v: [] for v in G.get_vertices()}
    paths[s] = [s]

    def iteration(i):
        converged = True
        for v in G.get_vertices():
            A[i][v] = A[i - 1][v]
            alt = np.inf
            alt_path = None
            for u in G.get_in_edges(v):
                if A[i - 1][u] + G.get_weight(u, v) < alt:
                    alt = A[i - 1][u] + G.get_weight(u, v)
                    alt_path = paths[u] + [v]

            if alt < A[i - 1][v]:
                A[i][v] = alt
                paths[v] = alt_path
                converged = False

        return converged

    for i in range(1, n - 1):
        converged = iteration(i)
        if converged:
            return paths

    # Detect negative cycle
    converged = iteration(n - 1)
    if not converged:
        return None

    return paths
```

### Runtime

* `∑_(v∈V)(in−deg⁡(v)) = m`

Total: `O(mn)`
