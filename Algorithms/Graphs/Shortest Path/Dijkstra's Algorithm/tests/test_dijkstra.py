# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import create_graph
from dijkstra import dijkstra


def test_dijkstra_1():
    paths = dijkstra(
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
    )
    expected = {
        "B": ("A", "B"),
        "C": ("A", "B", "C"),
        "D": ("A", "D"),
        "E": ("A", "D", "E"),
        "F": ("A", "D", "E", "F"),
        "G": ("A", "D", "E", "F", "G"),
        "H": ("A", "B", "C", "H"),
    }

    for v in expected:
        assert set(paths[v]) == set(expected[v])
