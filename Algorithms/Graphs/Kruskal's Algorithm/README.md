# Kruskal's Algorithm for Minimum Spanning Trees

## Definitions

### Tree

An undirected graph that is **acyclic** and **connected**.

Properties of Trees:

* Breaking a tree lemma: Removing any edge from a tree `T` disconnects `T`.
* Breaking a cycle lemma: Let `G` be a connected undirected graph and let `C` be a cycle in `G`. Then, removing any edge from `C` cannot disconnect `G`.
* Cycle Creation Lemma: Adding any edge `(u, v)`  to a tree `T` creates a cycle.
* Every tree of n vertices contains exactly n−1 edges.
* Every `n−1` set of edges among `n` nodes that are acyclic is a tree (also connected)
* Every `n−1` set of edges connecting `n` nodes is a tree, i.e. they are acyclic

### Minimum Spanning Tree

Input: An undirected connected graph `G` with arbitrary edge weights `w_e`.

Output: A tree `T∗` of `E` such that `w(T∗) ≤` weight of any other tree `T` in the graph.

## Algorithm

We need to sort the edges in ascending order of their weight. Then, we keep adding edges in that order until a tree is formed. Any edge that causes a cycle to be formed is skipped.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Kruskal's%20Algorithm/kruskal.py#L13)

Here is an efficient implementation using Union-find. Union-find is an efficient way of checking if a cycle is formed by adding an edge.

```python
def kruskal(G: Graph) -> List[Tuple[str, str]]:
    parent = {v: v for v in G.get_vertices()}
    rank = {v: 0 for v in G.get_vertices()}

    def find(x):
        if parent[x] == x:
            return x

        return find(parent[x])

    def union(uroot, vroot):
        if rank[uroot] < rank[vroot]:
            parent[uroot] = vroot
        elif rank[uroot] > rank[vroot]:
            parent[vroot] = uroot
        else:
            parent[vroot] = uroot
            rank[uroot] += 1

    E = sorted(list(G.get_edges()), key=lambda x: G.get_weight(x[0], x[1]))
    T = []
    for u, v in E:
        uroot = find(u)
        vroot = find(v)
        if uroot != vroot:  # T union (u, v) does not create a cycle
            T.append((u, v))
            union(uroot, vroot)

    return T
```
