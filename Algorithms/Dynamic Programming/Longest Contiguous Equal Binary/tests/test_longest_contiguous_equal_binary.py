# -*- coding: utf-8 -*-

import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from equal_binary import equal_binary


def naive_equal_binary(arr):
    max_len = 0

    for i in range(len(arr) + 1):
        for j in range(i):
            if (i - j) % 2 == 0:
                sum_01 = sum(arr[j:i])
                if sum_01 == (i - j) // 2 and (i - j) > max_len:
                    max_len = i - j

    return max_len


def test_longest_contiguous_equal_binary_1():

    assert naive_equal_binary([0, 1]) == 2
    assert naive_equal_binary([0, 1, 0, 0, 0, 1, 1]) == 6

    assert equal_binary([0, 1]) == 2
    assert equal_binary([0, 1, 0, 0, 0, 1, 1]) == 6


def test_longest_contiguous_equal_binary_2():
    for i in range(100):
        arr = np.random.randint(2, size=i)
        assert naive_equal_binary(arr) == equal_binary(arr)
