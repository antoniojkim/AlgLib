# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from max_points_on_line import max_points_on_line


def test_max_points_on_line_1():
    assert max_points_on_line([[1, 1], [2, 2], [3, 3]]) == 3


def test_max_points_on_line_2():
    assert max_points_on_line([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
