# -*- coding: utf-8 -*-
import os
import sys
from typing import List
from typing import Tuple

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from graphs import Graph


def kruskal(G: Graph) -> List[Tuple[str, str]]:
    """
    G is a weighted undirected graph
    """
    parent = {v: v for v in G.get_vertices()}
    rank = {v: 0 for v in G.get_vertices()}

    def find(x):
        nonlocal parent

        if parent[x] == x:
            return x

        return find(parent[x])

    def union(uroot, vroot):
        nonlocal parent, rank

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
