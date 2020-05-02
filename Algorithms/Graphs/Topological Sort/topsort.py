# -*- coding: utf-8 -*-
import os
import sys
from typing import List

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from graphs import Graph


def topsort(G: Graph) -> List[str]:
    """
    Topologically sort the graph
    """
    i = 0
    visited = {v: False for v in G.get_vertices()}
    ft = {v: None for v in G.get_vertices()}

    def DFS(u):
        nonlocal i, visited, ft

        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFS(v)

        ft[u] = i
        i += 1

    for u in visited:
        if not visited[u]:
            DFS(u)

    return sorted(ft, key=ft.get, reverse=True)
