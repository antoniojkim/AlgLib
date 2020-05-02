# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import create_graph
from kosaraju import kosaraju


def test_kosaraju_1():
    G = create_graph(
        ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
        [
            ("L", "I"),
            ("I", "J"),
            ("J", "K"),
            ("K", "L"),
            ("J", "A"),
            ("A", "D"),
            ("D", "H"),
            ("H", "A"),
            ("D", "E"),
            ("H", "B"),
            ("E", "F"),
            ("F", "G"),
            ("G", "E"),
            ("B", "C"),
            ("C", "B"),
        ],
    )
    expected = [["A", "D", "H"], ["B", "C"], ["E", "F", "G"], ["I", "J", "K", "L"]]

    result = kosaraju(G)

    for scc in result:
        scc.sort()
    for scc in expected:
        scc.sort()

    result.sort(key=lambda x: x[0])
    expected.sort(key=lambda x: x[0])

    for r, s in zip(result, expected):
        assert set(r) == set(s)
