# -*- coding: utf-8 -*-
import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../"))

from graphs import create_graph
from floydWarshall import floyd_warshall


def test_floyd_warshall_1():

    paths = floyd_warshall(
        create_graph(
            ["1", "2", "3", "4", "6", "7"],
            [
                ("1", "4", 1),
                ("2", "1", 1),
                ("2", "3", -1),
                ("2", "6", 2),
                ("2", "7", 5),
                ("3", "6", 1),
                ("6", "7", 0),
                ("7", "4", 2),
            ],
        )
    )
    expected = {
        "1": {"2": np.inf, "3": np.inf, "4": 1, "6": np.inf, "7": np.inf},
        "2": {"1": 1, "3": -1, "4": 2, "6": 0, "7": 0},
        "3": {"1": np.inf, "2": np.inf, "4": 3, "6": 1, "7": 1},
        "4": {"1": np.inf, "2": np.inf, "3": np.inf, "6": np.inf, "7": np.inf},
        "6": {"1": np.inf, "2": np.inf, "3": np.inf, "4": 2, "7": 0},
        "7": {"1": np.inf, "2": np.inf, "3": np.inf, "4": 2, "6": np.inf},
    }

    for i in paths:
        assert i in paths, f"{i} not in paths"
        for j in expected[i]:
            assert j in paths[i], f"{j} not in paths[{i}]"
            assert expected[i][j] == paths[i][j]
