# -*- coding: utf-8 -*-

import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from karatsuba_ofman import karatsuba_ofman


def int_to_list(i):
    return np.array([int(d) for d in str(i)])


def test_karatsuba_ofman():
    for i in range(100):
        X = np.random.randint(10, 100)
        Y = np.random.randint(10, 100)
        XY = X * Y
        X = int_to_list(X)
        Y = int_to_list(Y)

        assert karatsuba_ofman(X, Y) == XY
