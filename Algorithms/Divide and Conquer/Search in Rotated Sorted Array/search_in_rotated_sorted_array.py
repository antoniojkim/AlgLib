# -*- coding: utf-8 -*-
from typing import List


def search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        if target > nums[m]:
            if target > nums[r] >= nums[m]:
                r = m - 1
            else:
                l = m + 1
        elif target < nums[l] <= nums[m]:
            l = m + 1
        else:
            r = m - 1

    return -1
