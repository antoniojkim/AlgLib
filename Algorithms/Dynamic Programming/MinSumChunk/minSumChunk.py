# -*- coding: utf-8 -*-
from typing import List

from numpy import int, zeros


def minSumChunk(a: List[int], t: int):
    n = len(a)
    A = zeros((n, n), dtype=int)
    T = zeros((n, t), dtype=int)

    for i in range(n):
        A[i][i] = a[i]
        for j in range(i + 1, n):
            A[i][j] = A[i][j - 1] + a[j]

    for i in range(n):
        T[i][0] = A[0][i] ** 2

        for j in range(1, min(i + 1, t)):
            T[i][j] = min(T[k][j - 1] + A[k + 1][i] ** 2 for k in range(j - 1, i))

    return T[n - 1][t - 1]
