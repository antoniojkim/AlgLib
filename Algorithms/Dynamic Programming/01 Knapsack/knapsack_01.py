# -*- coding: utf-8 -*-
from typing import List

import numpy as np


def knapsack_01(items, values: List[float], weights: List[float], capacity: int):
    n = len(items)
    A = np.zeros((n, capacity))
    B = [
        [0 for i in range(capacity)] for j in range(n)
    ]  # Used to book keep for backtracing

    # Base Cases
    for c in range(capacity):
        if weights[0] <= c:
            A[0][c] = values[0]

    for i in range(1, n):
        for c in range(1, capacity):
            # Solving subproblem (with bookkeeping):
            #     A[i][c] = max(A[i-1][c],
            #                   A[i-1][c-weights[i]]+values[i])
            if A[i - 1][c] >= A[i - 1][c - weights[i]] + values[i]:
                A[i][c] = A[i - 1][c]
                B[i][c] = (i - 1, c)
            else:
                A[i][c] = A[i - 1][c - weights[i]] + values[i]
                B[i][c] = (i - 1, c - weights[i])

    # backtracing
    objects = []
    i, c = n - 1, capacity - 1
    while i >= 0 and c >= 0:
        i, c = B[i][c]
        objects.append(items[i])
        if B[i][c] == 0:
            break

    return objects, A[n - 1][capacity - 1]
