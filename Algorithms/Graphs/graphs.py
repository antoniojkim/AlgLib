# -*- coding: utf-8 -*-
from abc import abstractmethod

import numpy as np


class Graph:
    def __init__(self, V, E, directed=True):
        self.directed = directed

    @abstractmethod
    def add_vertex(self, v):
        pass

    def __lshift__(self, v):
        self.add_vertex(v)
        return self

    @abstractmethod
    def remove_vertex(self, v):
        pass

    def __rshift__(self, v):
        self.remove_vertex(v)
        return self

    @abstractmethod
    def add_edge(self, e):
        pass

    def __iadd__(self, e):
        self.add_edge(e)
        return self

    @abstractmethod
    def remove_edge(self, e):
        pass

    def __isub__(self, e):
        self.remove_edge(e)
        return self

    def contains_vertex(self, v):
        return False

    def contains_edge(self, e):
        return False

    def __contains__(self, g):
        if isinstance(g, tuple):
            return self.contains_edge(g)
        else:
            return self.contains_vertex(g)

    @abstractmethod
    def get_edges(self, v):
        pass

    def __getitem__(self, v):
        return self.get_edges(v)

    @abstractmethod
    def get_vertices(self):
        pass

    @abstractmethod
    def get_weight(self, u, v):
        pass


class AdjacencyMatrix(Graph):
    def __init__(self, V, E, directed=True):
        super().__init__(V, E, directed)
        self.V = V
        self.E = np.zeros((len(V), len(V)), dtype=np.bool)
        for e in E:
            self.add_edge(e)

    def add_vertex(self, v):
        if v not in self.V:
            self.V.append(v)
            self.E.resize((len(self.V), len(self.V)))

    def remove_vertex(self, v):
        if v in self.V:
            self.V.remove(v)

    def add_edge(self, e):
        u = self.V.index(e[0])
        v = self.V.index(e[1])

        self.E[u][v] = True
        if not self.directed:
            self.E[v][u] = True

    def remove_edge(self, e):
        u = self.V.index(e[0])
        v = self.V.index(e[1])

        self.E[u][v] = False
        if not self.directed:
            self.E[v][u] = False

    def contains_vertex(self, v):
        return v in self.V

    def contains_edge(self, e):
        u = self.V.index(e[0])
        v = self.V.index(e[1])
        return self.E[u][v]

    def get_edges(self, v):
        u = self.V.index(v)
        return (self.V[i] for i, e in enumerate(self.E[u]) if e)

    def get_vertices(self):
        return self.V


class AdjacencyList(Graph):
    def __init__(self, V, E, directed=True, **kwargs):
        super().__init__(V, E, directed)
        self.V = {v: {} for v in V}
        self.in_edges = {v: {} for v in V}
        for e in E:
            self.add_edge(e)

    def add_vertex(self, v):
        if v not in self.V:
            self.V[v] = {}

    def remove_vertex(self, v):
        self.V.pop(v, None)

    def add_edge(self, e):
        u, v, w = e[0], e[1], 0
        if len(e) >= 3:
            w = e[2]

        if u in self.V and v in self.V:
            self.V[u][v] = w
            if not self.directed:
                self.V[v][u] = w
            else:
                self.in_edges[v][u] = w

    def remove_edge(self, e):
        if e[0] in self.V and e[1] in self.V and e[1] in self.V[e[0]]:
            self.V[e[0]] = [edge for edge in self.V[e[0]] if edge != e[1]]
            if not self.directed:
                self.V[e[1]] = [edge for edge in self.V[e[1]] if edge != e[0]]
            else:
                self.in_edges[e[1]] = [
                    edge for edge in self.in_edges[e[1]] if edge != e[0]
                ]

    def contains_vertex(self, v):
        return v in self.V

    def contains_edge(self, e):
        return e[0] in self.V and e[1] in self.V[e[1]]

    def get_edges(self, v=None):
        if v is None:
            if self.directed:
                return ((u, k) for u in self.V for k in self.V[u])
            elif self.track_in:
                return ((k, u) for u in self.in_edges for k in self.in_edges[u])
            else:
                return set(tuple(sorted([u, k])) for u in self.V for k in self.V[u])

        assert v in self.V
        return (k for k in self.V[v])

    def get_in_edges(self, v):
        assert v in self.in_edges
        return iter(self.in_edges[v])

    def get_vertices(self):
        return self.V.keys()

    def get_weight(self, u, v):
        return self.V[u][v]

    def __str__(self):
        return str(self.V)


def create_graph(*args, **kwargs):
    return AdjacencyList(*args, **kwargs)


def reverse_graph(G):
    Grev = create_graph(G.get_vertices(), [], G.directed)

    for u in G.get_vertices():
        for v in G[u]:
            Grev.add_edge((v, u))

    return Grev
