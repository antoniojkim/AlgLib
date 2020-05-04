# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from knapsack_01 import knapsack_01


def test_knapsack_01():
    subset = knapsack_01(
        items=["A", "B", "C", "D"],
        values=[2.2, 4, 2, 3],
        weights=[2, 3, 3, 5],
        capacity=9,
    )
    optimal = (["A", "B", "C"], 8.2)

    assert set(subset[0]) == set(optimal[0])
    assert subset[1] == optimal[1]
