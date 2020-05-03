# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import create_graph
from ssspdag import sssp_dag


def test_sssp_dag_1():
    sssps = sssp_dag(
        create_graph(
            ["s", "a", "b", "c", "d", "e", "f", "t"],
            [
                ("s", "a", 9),
                ("s", "b", 4),
                ("a", "c", 1),
                ("a", "d", -3),
                ("b", "c", 2),
                ("b", "d", 3),
                ("b", "e", 2),
                ("c", "e", 2),
                ("c", "f", -4),
                ("d", "e", 1),
                ("d", "f", 2),
                ("e", "t", 5),
                ("f", "t", 3),
            ],
            track_in=True,
        ),
        "s",
    )
    expected = {
        "a": ("s", "a"),
        "b": ("s", "b"),
        "c": ("s", "b", "c"),
        "d": ("s", "a", "d"),
        "e": ("s", "b", "e"),
        "f": ("s", "b", "c", "f"),
        "t": ("s", "b", "c", "f", "t"),
    }

    for k in expected:
        assert set(sssps[k]) == set(expected[k])
