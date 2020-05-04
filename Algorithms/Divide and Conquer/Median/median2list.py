# -*- coding: utf-8 -*-
from typing import List


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
