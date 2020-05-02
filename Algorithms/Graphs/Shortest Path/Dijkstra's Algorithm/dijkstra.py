# -*- coding: utf-8 -*-
import sys

sys.path.append("../../")

import numpy as np

from graphs import create_graph
import heapq


def dijkstra(G, s):
    L = set([s])
    R = set([v for v in G.get_vertices() if v != s])
    SD = {v: None for v in G.get_vertices()}
    parent = {v: v for v in G.get_vertices()}
    paths = {v: [] for v in G.get_vertices()}
    paths[s] = [s]
    dSoFar = []
    dSoFarDict = {}

    i = 0
    entry = [0, i, s]
    i += 1
    dSoFarDict[s] = entry
    heapq.heappush(dSoFar, entry)
    for v in G.get_vertices():
        if v != s:
            entry = [np.inf, i, v]
            i += 1
            dSoFarDict[v] = entry
            heapq.heappush(dSoFar, entry)

    for _ in range(len(SD) - 1):
        while dSoFar[0][2] is None:
            heapq.heappop(dSoFar)

        min_d = heapq.heappop(dSoFar)
        vprime = min_d[2]

        R.discard(vprime)
        L.add(vprime)
        SD[vprime] = min_d[0]

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


def test_dijkstra(result, expected):
    for v in expected:
        if set(result[v]) != set(expected[v]):
            raise Exception(f"{v}:  {result[v]} != {expected[v]}")


if __name__ == "__main__":
    test_dijkstra(
        dijkstra(
            create_graph(
                ["A", "B", "C", "D", "E", "F", "G", "H"],
                [
                    ("A", "B", 4),
                    ("A", "C", 8),
                    ("A", "D", 1),
                    ("B", "C", 3),
                    ("C", "D", 9),
                    ("C", "F", 5),
                    ("C", "H", 4),
                    ("D", "E", 2),
                    ("E", "F", 3),
                    ("F", "G", 2),
                    ("G", "H", 3),
                ],
                directed=False,
            ),
            "A",
        ),
        {
            "B": ("A", "B"),
            "C": ("A", "B", "C"),
            "D": ("A", "D"),
            "E": ("A", "D", "E"),
            "F": ("A", "D", "E", "F"),
            "G": ("A", "D", "E", "F", "G"),
            "H": ("A", "B", "C", "H"),
        },
    )

    print("All Dijsktra's Algorithm Tests Passed!")
