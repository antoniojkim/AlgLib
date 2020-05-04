# -*- coding: utf-8 -*-

import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from quick_select import quickselect


def test_quickselect():
    for i in range(100):
        N = np.random.randint(-100, 100, size=35)
        n = np.random.randint(35)
        kth = quickselect(N, n)
        assert kth == sorted(N)[n]
