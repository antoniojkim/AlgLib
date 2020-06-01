# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from graphs import Graph


def DFS(G: Graph, u: str, v: str) -> bool:
    """
    Check if there exists a path from u to v
    """
    assert u in G and v in G

    if u == v:
        return True

    for n in G[u]:  # Traverse out-edges of `u`
        if DFS(G, n, v):
            return True

    return False
