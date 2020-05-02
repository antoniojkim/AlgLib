# -*- coding: utf-8 -*-
from typing import List
import numpy as np


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


def median2list(nums1: List[int], nums2: List[int]) -> float:
    size = len(nums1) + len(nums2)
    if len(nums1) > len(nums2):  # we want nums1 to be the smaller list
        nums1, nums2 = nums2, nums1

    min_i = 0
    max_i = len(nums1)
    while min_i <= max_i:
        i = (min_i + max_i) // 2
        j = (size + 1) // 2 - i
        if i < len(nums1) and nums1[i] < nums2[j - 1]:
            min_i = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            max_i = i - 1
        else:

            if i == 0:
                max_left = nums2[j - 1]
            elif j == 0:
                max_left = nums1[i - 1]
            else:
                max_left = max(nums1[i - 1], nums2[j - 1])

            if (size % 2) != 0:
                return max_left

            if i == len(nums1):
                min_right = nums2[j]
            elif j == len(nums2):
                min_right = nums1[i]
            else:
                min_right = min(nums1[i], nums2[j])

            return (max_left + min_right) / 2

    raise Exception(f"Could not find median of {nums1} {nums2}")


def assert_equals(inputs):
    """
    Asserts that the solution for the better solution
    matches the solution for the naive solution
    """
    result = median2list(*inputs)
    expected = median2list_naive(*inputs)
    if result != expected:
        raise Exception(f"median2list{inputs} = {result} != {expected}")


if __name__ == "__main__":
    assert_equals(([1, 3], [2]))
    assert_equals(([1, 2], [3, 4]))
    assert_equals(([1, 3], [2, 4]))
    assert_equals(([1, 3, 4, 5], [2]))
    for i in range(1000):
        A = np.random.choice(1000, np.random.randint(25, 50))
        r = np.random.randint(1, len(A))
        A, B = A[:r], A[r:]
        A.sort()
        B.sort()
        assert_equals((A, B))

    print("All Median of 2 Lists Tests Passed!")
