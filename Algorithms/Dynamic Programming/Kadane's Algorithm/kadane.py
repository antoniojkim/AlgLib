# -*- coding: utf-8 -*-
from typing import List

from numpy import zeros


def kadane(A: List[int]):
    B = zeros(len(A))
    B[0] = A[0]
    msub = B[0]
    for j in range(1, len(B)):
        B[j] = max(A[j], B[j - 1] + A[j])
        msub = max(msub, B[j])

    return msub
