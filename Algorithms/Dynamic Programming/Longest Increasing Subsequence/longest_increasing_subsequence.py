# -*- coding: utf-8 -*-
from typing import List

from numpy import zeros


def longest_increasing_subsequence(a: List[int]):
    M = zeros(len(a), dtype=int)
    for k in range(len(M)):
        M[k] = 1
        for j in range(k - 1):
            if a[j] < a[k]:
                M[k] = max(M[k], M[j] + 1)

    return max(M)
