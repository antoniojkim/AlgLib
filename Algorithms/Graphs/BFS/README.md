# Breadth-First Search Traversal (BFS)

## Definition

* Starts from `s` and traverses the graph in waves

See [wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search) article for more details.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/BFS/BFS.py#L12)

Here is a simple implementation of BFS that checks to see if a path exists between two vertices:

```python
def BFS(G: Graph, u: str, v: str) -> bool:
    V = {k: False for k in G.get_vertices()}  # visited
    Q = deque([u])
    while len(Q) > 0:
        n = Q.popleft()
        V[n] = True
        if n == v:
            return True
        else:
            for k in G[n]:
                if not V[k]:
                    Q.append(k)

    return False
```
