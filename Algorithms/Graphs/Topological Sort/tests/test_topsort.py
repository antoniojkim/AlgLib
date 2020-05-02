# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import create_graph
from topsort import topsort


def assert_topsort(dag):
    visited = set()
    for t in topsort(dag):
        for u, v in dag.get_edges():
            if t == v:
                assert u in visited

        visited.add(t)


def test_topsort_1():
    assert_topsort(
        create_graph(
            ["A", "B", "C", "D", "E", "F", "G", "H"],
            [
                ("A", "B"),
                ("A", "C"),
                ("H", "A"),
                ("H", "D"),
                ("D", "F"),
                ("E", "H"),
                ("E", "G"),
                ("G", "D"),
            ],
        )
    )
