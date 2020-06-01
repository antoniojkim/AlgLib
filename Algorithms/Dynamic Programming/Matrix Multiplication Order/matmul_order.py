# -*- coding: utf-8 -*-
from typing import List

from numpy import inf, zeros


def matmul_order(dims: List[int]):
    n = len(dims) - 1

    S = zeros((n, n))
    B = zeros((n, n), dtype=int)

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                B[i][j] = i
            elif i + 1 == j:
                S[i][j] = dims[i] * dims[i + 1] * dims[i + 2]
                B[i][j] = i
            else:
                min_i_j = inf
                for k in range(i, j - 1):
                    new_min = (
                        S[i][k] + S[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                    )
                    if new_min < min_i_j:
                        min_i_j = new_min
                        B[i][j] = k

                S[i][j] = min_i_j

    def backtrace(i, j):
        objects = []
        if i + 1 < j:
            objects.append(B[i][j])
            objects.extend(backtrace(B[i][j] + 1, j))
            objects.extend(backtrace(i, B[i][j]))

        return objects

    return backtrace(0, n - 1), S[0][n - 1]
