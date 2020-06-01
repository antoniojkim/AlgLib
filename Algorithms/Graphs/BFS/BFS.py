# -*- coding: utf-8 -*-
import os
import sys
from collections import deque

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from graphs import Graph


def BFS(G: Graph, u: str, v: str) -> bool:
    """
    Check if there exists a path from u to v
    """
    assert u in G and v in G

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
