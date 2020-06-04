# -*- coding: utf-8 -*-
from collections import Counter
from itertools import combinations_with_replacement
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    nums = Counter(nums)

    zero_sums = set()
    for a, b in combinations_with_replacement(nums, 2):
        c = -a - b

        if c in nums:
            add = True
            if a == b == c:
                add = nums[a] > 2
            elif a == b:
                add = nums[a] > 1
            elif a == c:
                add = nums[a] > 1
            elif b == c:
                add = nums[b] > 1

            if add:
                zero_sums.add(tuple(sorted((a, b, c))))

    return zero_sums
