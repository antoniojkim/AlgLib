# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from find_first_and_last_position_of_element_in_sorted_array import (
    find_first_and_last_position_of_element_in_sorted_array,
)


def test_find_first_and_last_position_of_element_in_sorted_array_1():
    assert find_first_and_last_position_of_element_in_sorted_array(
        [5, 7, 7, 8, 8, 10], 8
    ) == [3, 4]


def test_find_first_and_last_position_of_element_in_sorted_array_2():
    assert find_first_and_last_position_of_element_in_sorted_array(
        [5, 7, 7, 8, 8, 10], 6
    ) == [-1, -1]
