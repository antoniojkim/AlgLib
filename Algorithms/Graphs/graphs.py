import numpy as np

class Graph:

    def __init__(self, V, E, directed=True):
        self.directed = directed

    def add_vertex(self, v):
        pass

    def __lshift__(self, v):
        self.add_vertex(v)

    def remove_vertex(self, v):
        pass

    def __rshift__(self, v):
        self.remove_vertex(v)

    def add_edge(self, e):
        pass

    def __iadd__(self, e):
        self.add_edge(e)

    def remove_edge(self, e):
        pass

    def __isub__(self, e):
        self.remove_edge(e)

    def contains_vertex(self, v):
        return False

    def contains_edge(self, e):
        return False

    def __contains__(self, g):
        if isinstance(g, tuple):
            return self.contains_edge(g)
        else:
            return self.contains_vertex(g)

    def get_edges(self, v):
        pass

    def __getitem__(self, v):
        return self.get_edges(v)


class AdjacencyMatrix(Graph):

    def __init__(self, V, E, directed=True):
        super().__init__(V, E, directed)
        self.V = V
        self.E = np.zeros((len(V), len(V)), dtype=np.bool)
        for e in E:
            self.add_edge(e)

    def add_vertex(self, v):
        if (v not in self.V):
            self.V.append(v)
            self.E.resize((len(self.V), len(self.V)))

    def remove_vertex(self, v):
        if (v in self.V):
            self.V.remove(v)

    def add_edge(self, e):
        u = self.V.index(e[0])
        v = self.V.index(e[1])

        self.E[u][v] = True
        if (not self.directed):
            self.E[v][u] = True

    def remove_edge(self, e):
        u = self.V.index(e[0])
        v = self.V.index(e[1])

        self.E[u][v] = False
        if (not self.directed):
            self.E[v][u] = False

    def contains_vertex(self, v):
        return v in self.V

    def contains_edge(self, e):
        u = self.V.index(e[0])
        v = self.V.index(e[1])
        return self.E[u][v] == True

    def get_edges(self, v):
        u = self.V.index(v)
        return (self.V[i] for i, e in enumerate(self.E[u]) if e)
    


class AdjacencyList(Graph):

    def __init__(self, V, E, directed=True):
        super().__init__(V, E, directed)
        self.V = {v:{} for v in V}
        for e in E:
            self.add_edge(e)

    def add_vertex(self, v):
        if (v not in self.V):
            self.V[v] = {}

    def remove_vertex(self, v):
        self.V.pop(v, None)

    def add_edge(self, e):
        if (e[0] in self.V and e[1] in self.V):
            self.V[e[0]][e[1]] = True
            if (not self.directed):
                self.V[e[1]][e[0]] = True

    def remove_edge(self, e):
        if (e[0] in self.V and e[1] in self.V):
            self.V[e[0]].pop(e[1], None)
            if (not self.directed):
                self.V[e[1]].pop(e[0], None)

    def contains_vertex(self, v):
        return v in self.V

    def contains_edge(self, e):
        return e[0] in self.V and e[1] in self.V[e[1]]

    def get_edges(self, v):
        assert(v in self.V)
        return (k for k in self.V[v])
    


def create_graph(V, E, directed=True):
    return AdjacencyList(V, E)
