# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from single_element_sorted_array import single_non_duplicate


def test_single_element_sorted_array_1():
    assert single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2


def test_single_element_sorted_array_2():
    assert single_non_duplicate([3, 3, 7, 7, 10, 11, 11]) == 10


def test_single_element_sorted_array_3():
    assert single_non_duplicate([1, 1, 3, 3, 2]) == 2


def test_single_element_sorted_array_4():
    assert single_non_duplicate([1, 1, 2, 3, 3]) == 2


def test_single_element_sorted_array_5():
    assert single_non_duplicate([2, 1, 1, 3, 3]) == 2
