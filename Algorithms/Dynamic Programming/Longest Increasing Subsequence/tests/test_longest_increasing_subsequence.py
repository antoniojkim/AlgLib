# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from longest_increasing_subsequence import longest_increasing_subsequence


def test_longest_increasing_subsequence_1():
    assert (
        longest_increasing_subsequence(
            [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        )
        == 6
    )
