# Graphs

## Definition

A graph `G(V, E)` is a pair of sets:

* `V`: set of nodes/vertices
* `E`: set `(u, v)` of edges such that `u ∈ V, v ∈ V`

It is a natural way of representing connected data.

## Terminology

Directed graphs vs Undirected graphs

* **Directed**: Edges have direction (e.g. Twitter)
* **Undirected**: Edges have no direction (e.g. FB)

Simple vs Multigraphs

* **Simple**:
    * Can have at most one edge between `u` and `v` if `G` is undirected.
    * At most two edges between `u` anbd `v` if `G` is directed.
* Multigraphs: Parallel edges are allowed

Cyclic vs Acyclic

* **Cyclic**: Has a cycle
* **Acyclic**: No cycles

Connected vs Unconnected

* **Connected**: `G` is one piece
* **Unconnected**: `G` has more than one piece

## Conventions

* `|V| = n`
* `|E| = m`

## Properties

* If `G` is undirected and simple, then the maximum number of edges it can have is `m ≤ (n choose 2)`
* If `G` is directed and simple, then the maximum number of edges it can have is `m ≤ 2*(n choose 2)`
* If `G` is undirected and connected, then the minimum number of edges it can have is `m ≥ n−1`

## More Definitions

Degree of `v`

* `out-degree(v)` is the number of outgoing edges from `v`, i.e. `(v, w) ∈ E`
* `in-degree(v)` is the number of incoming edges to `v`, i.e. `(w, v) ∈ E`

For undirected graphs, we just say `deg⁡(v)`


### Graph Implementations

* [Adjacency List Graph](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/graphs.py#L120)
* [Adjacency Matrix Graph](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/graphs.py#L71)

Adjacency list implementations are more typically used as most practical graphs are very sparse.
