# -*- coding: utf-8 -*-
import sys

import numpy as np

from graphs import create_graph

sys.path.append("../../")


def bellman_ford(G, s):
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


def test_bellman_ford(result, expected):
    if expected is None:
        if result is not None:
            raise Exception("Expected negative cycle, not found")

    else:
        for v in expected:
            if set(expected[v]) != set(result[v]):
                raise Exception(f"{v}:  {expected[v]} != {result[v]}")


if __name__ == "__main__":
    test_bellman_ford(
        bellman_ford(
            create_graph(
                ["s", "a", "b", "c", "x", "w", "z", "t"],
                [
                    ("s", "a", -1),
                    ("s", "w", 2),
                    ("s", "x", 1),
                    ("a", "b", 1),
                    ("b", "c", 0),
                    ("c", "t", 2),
                    ("w", "z", 3),
                    ("z", "t", -6),
                    ("x", "t", 1),
                ],
                track_in=True,
            ),
            "s",
        ),
        {
            "a": ["s", "a"],
            "b": ["s", "a", "b"],
            "c": ["s", "a", "b", "c"],
            "x": ["s", "x"],
            "w": ["s", "w"],
            "z": ["s", "w", "z"],
            "t": ["s", "w", "z", "t"],
        },
    )
    test_bellman_ford(
        bellman_ford(
            create_graph(
                ["s", "a", "b", "c", "x", "w", "z", "t"],
                [
                    ("s", "a", -1),
                    ("s", "w", 2),
                    ("s", "x", 1),
                    ("a", "b", 1),
                    ("b", "c", 0),
                    ("c", "t", 2),
                    ("w", "z", 3),
                    ("z", "t", -6),
                    ("x", "t", 1),
                    ("w", "a", -3),
                    ("b", "w", -1),
                ],
                track_in=True,
            ),
            "s",
        ),
        None,
    )

    print("All Bellman Ford Tests Passed!")
