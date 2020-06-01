# -*- coding: utf-8 -*-

import itertools
import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from max_min_sum_segments import max_min_sum_segments


def naive_max_min_sum_segments(A, k):
    max_sum = -np.inf

    for ts in itertools.combinations(range(1, len(A)), k - 1):
        ts = sorted([0] + list(ts) + [len(A)])
        min_sum = min(sum(A[ts[i - 1] : ts[i]]) for i in range(1, len(ts)))
        if min_sum > max_sum:
            max_sum = min_sum

    return max_sum


def test_max_min_sum_segments_1():
    assert naive_max_min_sum_segments([6, 3, 2, 8, 7, 5], 3) == 9
    assert max_min_sum_segments([6, 3, 2, 8, 7, 5], 3) == 9


def test_max_min_sum_segments_2():
    assert naive_max_min_sum_segments([5, 7, 4, 2, 8, 1, 6], 3) == 7
    assert max_min_sum_segments([5, 7, 4, 2, 8, 1, 6], 3) == 7


def test_max_min_sum_segments_3():
    assert naive_max_min_sum_segments([6, 5, 3, 8, 9, 10, 4, 7, 10], 4) == 14
    assert max_min_sum_segments([6, 5, 3, 8, 9, 10, 4, 7, 10], 4) == 14


def test_max_min_sum_segments_4():
    for i in range(10):
        A = np.random.randint(0, 100, size=15)
        k = np.random.randint(2, 10)
        assert max_min_sum_segments(A, k) == naive_max_min_sum_segments(A, k)
