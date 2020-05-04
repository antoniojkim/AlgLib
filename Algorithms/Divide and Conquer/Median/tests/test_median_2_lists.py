# -*- coding: utf-8 -*-

import os
import sys
from typing import List

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from median2list import median2list


def median2list_naive(nums1: List[int], nums2: List[int]) -> float:
    """
    Naive Solution where the two lists are merged and the median
    is easily found from the merged list

    Runtime:   O(m+n)
    """
    i, j, size = 0, 0, len(nums1) + len(nums2)
    merged = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1

        else:
            merged.append(nums2[j])
            j += 1

    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    return (
        (merged[size // 2 - 1] + merged[size // 2]) / 2
        if size % 2 == 0
        else merged[size // 2]
    )


def assert_equals(A, B):
    """
    Asserts that the solution for the better solution
    matches the solution for the naive solution
    """
    assert median2list(A, B) == median2list_naive(A, B)


def test_median_2_lists_1():
    assert_equals([1, 3], [2])


def test_median_2_lists_2():
    assert_equals([1, 2], [3, 4])


def test_median_2_lists_3():
    assert_equals([1, 3], [2, 4])


def test_median_2_lists_4():
    assert_equals([1, 3, 4, 5], [2])


def test_median_2_lists_5():
    for i in range(1000):
        A = np.random.choice(1000, np.random.randint(25, 50))
        r = np.random.randint(1, len(A))
        A, B = A[:r], A[r:]
        A.sort()
        B.sort()
        assert_equals(A, B)

    print("All Median of 2 Lists Tests Passed!")
