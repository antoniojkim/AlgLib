# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from search_in_rotated_sorted_array import search_in_rotated_sorted_array


def test_search_in_rotated_sorted_array_1():
    assert search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_search_in_rotated_sorted_array_2():
    assert search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3) == -1
