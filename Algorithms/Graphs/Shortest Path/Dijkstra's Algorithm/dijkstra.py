# -*- coding: utf-8 -*-
import os
import sys
from typing import Dict
from typing import List

from numpy import inf

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import Graph
import heapq


def dijkstra(G: Graph, s: str) -> Dict[str, List[str]]:
    L = {s}
    R = set([v for v in G.get_vertices() if v != s])
    SD = {v: None for v in G.get_vertices()}  # Shortest Distances
    parent = {v: v for v in G.get_vertices()}
    paths = {v: [] for v in G.get_vertices()}
    paths[s] = [s]
    dSoFar = []
    dSoFarDict = {}
    i = 0

    # Initialization
    dSoFarDict[s] = [0, i, s]
    heapq.heappush(dSoFar, [0, i, s])
    i += 1
    for v in G.get_vertices():
        if v != s:
            dSoFarDict[v] = [inf, i, v]
            heapq.heappush(dSoFar, [inf, i, v])
            i += 1

    for _ in range(len(SD) - 1):
        # Extract min
        while dSoFar[0][2] is None:
            heapq.heappop(dSoFar)

        min_d = heapq.heappop(dSoFar)
        vprime = min_d[2]

        R.discard(vprime)
        L.add(vprime)
        SD[vprime] = min_d[0]

        # Decrement Key
        for z in G[vprime]:
            if z in R:
                newDistToZ = SD[vprime] + G.get_weight(vprime, z)
                if newDistToZ < dSoFarDict[z][0]:
                    # decrease key
                    dSoFarDict[z][2] = None
                    entry = [newDistToZ, i, z]
                    i += 1
                    dSoFarDict[z] = entry
                    heapq.heappush(dSoFar, entry)

                    # set parent
                    parent[z] = vprime

                    # record path
                    paths[z] = paths[vprime] + [z]

    return paths
