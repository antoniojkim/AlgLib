# -*- coding: utf-8 -*-
from typing import List


def find_first_and_last_position_of_element_in_sorted_array(
    nums: List[int], target: int
) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]

    start = 0
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r + 1) // 2
        if nums[m] == target:
            start = m

        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1

    if nums[start] != target:
        return [-1, -1]

    end = start
    l = start
    r = len(nums) - 1
    while l <= r:
        m = (l + r + 1) // 2
        if nums[m] == target:
            end = m

        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1

    return [start, end]
