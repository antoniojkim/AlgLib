# -*- coding: utf-8 -*-
import os
import sys
from typing import Dict
from typing import List

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../../"))
sys.path.append(os.path.join(file_dir, "../../Topological Sort"))

from graphs import Graph
from topsort import topsort


def sssp_dag(G: Graph, s: str) -> Dict[str, List[str]]:
    f = topsort(G)
    SD = {v: (0 if v == s else np.inf) for v in f}  # Shortest Distances
    paths = {v: [] for v in f}

    for v in f:
        curpath = []
        for u in G.get_in_edges(v):
            tmp = SD[u] + G.get_weight(u, v)
            if tmp < SD[v]:
                SD[v] = tmp
                curpath = paths[u]

        paths[v].extend(curpath)
        paths[v].append(v)

    return paths
