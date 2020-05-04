# Dijkstra's Algorithm

In a general graph, with *non-negative* edge weights

Input: A directed (or undirected) graph `G`, source `s`, non-negative `w(u, v)`

Output: Shortest path from `s` to every other node `v`

## [Implementation]((https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Shortest%20Path/Dijkstra's%20Algorithm/dijkstra.py#L16))

```python
def dijkstra(G: Graph, s: str) -> Dict[str, List[str]]:
    L = {s}
    R = set([v for v in G.get_vertices() if v != s])
    SD = {v: None for v in G.get_vertices()}  # Shortest Distances
    parent = {v: v for v in G.get_vertices()}
    paths = {v: [] for v in G.get_vertices()}
    paths[s] = [s]
    dSoFar = []
    dSoFarDict = {}
    i = 0

    # Initialization
    dSoFarDict[s] = [0, i, s]
    heapq.heappush(dSoFar, [0, i, s])
    i += 1
    for v in G.get_vertices():
        if v != s:
            dSoFarDict[v] = [inf, i, v]
            heapq.heappush(dSoFar, [inf, i, v])
            i += 1

    for _ in range(len(SD) - 1):
        # Extract min
        while dSoFar[0][2] is None:
            heapq.heappop(dSoFar)

        min_d = heapq.heappop(dSoFar)
        vprime = min_d[2]

        R.discard(vprime)
        L.add(vprime)
        SD[vprime] = min_d[0]

        # Decrement Key
        for z in G[vprime]:
            if z in R:
                newDistToZ = SD[vprime] + G.get_weight(vprime, z)
                if newDistToZ < dSoFarDict[z][0]:
                    # decrease key
                    dSoFarDict[z][2] = None
                    entry = [newDistToZ, i, z]
                    i += 1
                    dSoFarDict[z] = entry
                    heapq.heappush(dSoFar, entry)

                    # set parent
                    parent[z] = vprime

                    # record path
                    paths[z] = paths[vprime] + [z]

    return paths
```

### Runtime

* Initialization: `O(n)`
* Extract Min: `O(nlog⁡n)`
* Decrement Key: `∑_(v∈V) deg⁡(v) = m` -> `O(mlog⁡n)`

Total Runtime:   `O(mlog⁡n)`
