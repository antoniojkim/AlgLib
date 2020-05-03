# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import create_graph
from kruskal import kruskal


def kruskal_test(G, expected):
    mst = kruskal(G)

    assert len(mst) == len(G.get_vertices()) - 1

    mst_cost = 0
    unvisited = set(G.get_vertices())
    for u, v in mst:
        unvisited.discard(u)
        unvisited.discard(v)
        mst_cost += G.get_weight(u, v)

    assert len(unvisited) == 0, f"Tkrus is not spanning:  {mst}"

    unvisited = set(G.get_vertices())
    expt_cost = 0
    for u, v in expected:
        unvisited.discard(u)
        unvisited.discard(v)
        expt_cost += G.get_weight(u, v)

    assert len(unvisited) == 0, f"Expected is not spanning:  {expected}"

    assert mst_cost == expt_cost


def test_kruskal_1():
    kruskal_test(
        create_graph(
            ["A", "B", "C", "D", "E", "F", "G", "H"],
            [
                ("A", "B", 4),
                ("A", "C", 6),
                ("A", "D", 1),
                ("B", "C", 8),
                ("C", "D", 5),
                ("C", "F", 2.5),
                ("C", "H", 7),
                ("D", "E", 2),
                ("E", "F", 3),
                ("F", "G", 7.5),
                ("G", "H", 9),
            ],
            directed=False,
        ),
        [
            ("A", "B"),
            ("A", "D"),
            ("D", "E"),
            ("E", "F"),
            ("C", "F"),
            ("C", "H"),
            ("F", "G"),
        ],
    )
