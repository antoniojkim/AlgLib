# -*- coding: utf-8 -*-

from typing import List

from numpy import inf, zeros


def min_score_triangulation(A: List[int]) -> int:
    S = zeros((len(A), len(A)))  # Min score solution matrix
    for i in range(2, len(A)):
        for j in range(len(A) - i):
            S[j, j + i] = inf
            for k in range(j + 1, j + i):
                S[j, j + i] = min(
                    S[j, j + i], A[j] * A[k] * A[j + i] + S[j, k] + S[k, j + i]
                )

    return S[0, -1]
