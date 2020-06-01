# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import create_graph
from bellmanford import bellman_ford


def compare_bellman_ford(result, expected):
    if expected is None:
        assert result is None, "Expected negative cycle, not found"
    else:
        for v in expected:
            assert set(expected[v]) == set(result[v])


def test_bellman_ford_1():
    compare_bellman_ford(
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


def test_bellman_ford_2():
    compare_bellman_ford(
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
