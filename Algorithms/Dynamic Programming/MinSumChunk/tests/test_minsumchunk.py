# -*- coding: utf-8 -*-

import itertools
import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from minSumChunk import minSumChunk


def minSumChunk_naive(a, t):
    min_sum = np.inf
    for ts in list(itertools.combinations(range(1, len(a)), t - 1)):
        ts = sorted([0] + list(ts) + [len(a)])
        chunk_sum = sum(sum(a[ts[i - 1] : ts[i]]) ** 2 for i in range(1, len(ts)))
        if chunk_sum < min_sum:
            min_sum = chunk_sum

    return min_sum


def test_minSumCheck():
    for _ in range(1000):
        r = np.random.randint(6, 15)
        a = np.random.randint(-100, 100, size=r)
        t = np.random.randint(1, r)
        assert minSumChunk(a, t) == minSumChunk_naive(a, t)
