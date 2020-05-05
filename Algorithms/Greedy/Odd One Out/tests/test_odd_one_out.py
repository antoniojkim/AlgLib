# -*- coding: utf-8 -*-

import os
import sys

import numpy as np
from random import shuffle

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from odd_one_out import odd_one_out


def test_odd_one_out():
    for i in range(100):
        A = []
        n = np.random.randint(3, 10)
        for j in range(n):
            a = np.random.randint(0, 100)
            A.extend((a for _ in range(np.random.randint(1, 5) * 2)))

        odd = np.random.randint(0, 100)
        A.extend((odd for i in range(np.random.randint(2, 7) * 2 + 1)))

        shuffle(A)

        assert odd_one_out(A) == odd
