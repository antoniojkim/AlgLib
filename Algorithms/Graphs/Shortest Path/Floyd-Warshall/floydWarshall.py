# -*- coding: utf-8 -*-
import os
import sys
from typing import Dict

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import Graph


def floyd_warshall(G: Graph) -> Dict[str, Dict[str, float]]:
    V = list(G.get_vertices())
    n = len(V)
    A = {u: {v: [np.inf for _ in range(n)] for v in V} for u in V}

    for i in V:
        A[i][i][0] = 0
    for i, j in G.get_edges():
        A[i][j][0] = G.get_weight(i, j)

    for k in range(1, n):
        for i in G.get_vertices():
            for j in G.get_vertices():
                A[i][j][k] = min(A[i][j][k - 1], A[i][V[k]][k - 1] + A[V[k]][j][k - 1])

    return {i: {j: A[i][j][-1] for j in V if i != j} for i in V}
