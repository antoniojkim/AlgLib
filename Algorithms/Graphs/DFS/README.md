# Depth-First Search Traversal (DFS)

## Definition

* From `s` tries to go "as far as" it can "as fast as" it can
* Backtracking when stuck

See [wikipedia](https://en.wikipedia.org/wiki/Depth-first_search) article for more details.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/DFS/DFS.py#L11)

Here is a simple implementation of DFS that checks to see if a path exists between two vertices:

```python
def DFS(G: Graph, u: str, v: str) -> bool:
    if u == v:
        return True

    for n in G[u]:  # Traverse out-edges of `u`
        if DFS(G, n, v):
            return True

    return False
```
