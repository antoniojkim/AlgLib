# -*- coding: utf-8 -*-

import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from set_intersection import set_intersection


def test_set_intersection():
    for i in range(100):
        array1 = sorted(np.random.randint(0, 20, size=np.random.randint(5, 20)))
        array2 = sorted(np.random.randint(0, 20, size=np.random.randint(5, 20)))

        assert set(set_intersection(array1, array2)) == (set(array1) & set(array2))
