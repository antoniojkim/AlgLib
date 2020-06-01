# -*- coding: utf-8 -*-

import itertools
import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from subsetThreshold import subsetThreshold


def subsetThreshold_naive(a, m):
    n = len(a)
    asum = sum(a)
    for S in itertools.combinations(a, n // 2):
        l = sum(S)
        if l > n * m // 4 and asum - l > n * m // 4:
            return True, set(S), set(a) - set(S)

    return False, [], []


def test_subset_threshold():

    while True:
        n = np.random.randint(2, 5) * 2
        a = np.random.randint(100, 200, size=n)
        m = np.random.randint(50, 200)
        m = max(m * n, max(a) + 1)

        s1 = subsetThreshold_naive(a, m)
        s2 = subsetThreshold(a, m)

        assert s1[0] == s2[0]

        if s1[0]:
            assert sum(s1[1]) > n * m // 4
            assert sum(s1[2]) > n * m // 4
            assert sum(s2[1]) > n * m // 4
            assert sum(s2[2]) > n * m // 4
            break
