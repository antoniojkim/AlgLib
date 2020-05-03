# -*- coding: utf-8 -*-
import os
import sys
from typing import Dict
from typing import List

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import Graph


def bellman_ford(G: Graph, s: str) -> Dict[str, List[str]]:
    n = len(list(G.get_vertices()))
    A = [{v: np.inf for v in G.get_vertices()} for _ in range(n)]

    A[0][s] = 0

    paths = {v: [] for v in G.get_vertices()}
    paths[s] = [s]

    def iteration(i):
        converged = True
        for v in G.get_vertices():
            A[i][v] = A[i - 1][v]
            alt = np.inf
            alt_path = None
            for u in G.get_in_edges(v):
                if A[i - 1][u] + G.get_weight(u, v) < alt:
                    alt = A[i - 1][u] + G.get_weight(u, v)
                    alt_path = paths[u] + [v]

            if alt < A[i - 1][v]:
                A[i][v] = alt
                paths[v] = alt_path
                converged = False

        return converged

    for i in range(1, n - 1):
        converged = iteration(i)
        if converged:
            return paths

    # Detect negative cycle
    converged = iteration(n - 1)
    if not converged:
        return None

    return paths
