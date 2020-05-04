# -*- coding: utf-8 -*-
from typing import List


def max_min_sum_segments(A: List[int], k: int) -> int:
    def split(min_sum):
        count = 0
        segment_sum = 0
        for a in A:
            segment_sum += a
            if segment_sum >= min_sum:
                count += 1
                segment_sum = 0

        return count

    l = min(A)
    h = sum(A)

    while l < h:
        min_sum = (l + h + 1) // 2
        if split(min_sum) < k:
            h = min_sum - 1
        else:
            l = min_sum

    return l
