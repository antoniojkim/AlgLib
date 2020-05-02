# -*- coding: utf-8 -*-
import os
import sys
from typing import List

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../Topological Sort"))

from graphs import Graph, reverse_graph
from topsort import topsort


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
