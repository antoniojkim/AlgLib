# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import create_graph
from DFS import DFS


def test_DFS_1():
    G = create_graph(["A", "B", "C"], [("A", "B"), ("B", "C")])
    assert DFS(G, "A", "C")
    assert not DFS(G, "C", "A")
