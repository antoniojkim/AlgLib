# -*- coding: utf-8 -*-
from typing import List

from numpy import zeros


def linear_independent_set(V: List[int]):
    A = zeros(len(V) + 1, dtype=int)
    S = [[] for _ in range(len(A))]
    A[0] = 0
    A[1] = V[0][1]
    S[1].append(V[0][0])

    for i in range(2, len(A)):
        if A[i - 1] <= A[i - 2] + V[i - 1][1]:
            A[i] = A[i - 2] + V[i - 1][1]
            S[i] = S[i - 2] + [V[i - 1][0]]
        else:
            A[i] = A[i - 1]
            S[i] = S[i - 1]

    return A[-1], S[-1]
