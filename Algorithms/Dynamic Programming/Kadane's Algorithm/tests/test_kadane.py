# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from kadane import kadane


def test_kadane_1():
    assert kadane([1, -2, 3, -4, 5, 6, 7, -8, 9, -10]) == 19
