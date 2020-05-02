# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import create_graph

from BFS import BFS


def test_BFS_1():
    G = create_graph(["A", "B", "C"], [("A", "B"), ("B", "C")])
    assert BFS(G, "A", "C")
    assert not BFS(G, "C", "A")
