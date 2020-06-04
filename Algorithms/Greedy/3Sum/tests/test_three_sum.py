# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from three_sum import three_sum


def test_three_sum_1():
    assert three_sum([-1, 0, 1, 2, -1, -4]) == {(-1, 0, 1), (-1, -1, 2)}
