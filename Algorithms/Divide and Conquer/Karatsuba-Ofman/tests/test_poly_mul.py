# -*- coding: utf-8 -*-

import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from poly_mul import poly_mul


def test_poly_mul():
    X = np.array([1, 2])
    Y = np.array([1, 3])

    assert np.array_equal(poly_mul(X, Y), np.array([1, 5, 6]))
