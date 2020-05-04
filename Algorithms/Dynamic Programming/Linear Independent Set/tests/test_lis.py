# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from lis import lis


def test_lis_1():
    subset = lis([("A", 1), ("B", 5), ("C", 6), ("D", 3)])
    expected = (8, ("B", "D"))

    assert subset[0] == expected[0]
    assert set(subset[1]) == set(expected[1])
