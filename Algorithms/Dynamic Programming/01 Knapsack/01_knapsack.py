# -*- coding: utf-8 -*-
import numpy as np


def knapsack(items, values, weights, capacity: int):
    """
    0/1 Integer Weight Knapsack

    n items:  o_1, o_2, ..., o_n
    Input:
        Values of items:  v_1, v_2, ..., v_n
        Weights: w_1, w_2, ..., w_n
        Knapsack capacity (Integer)
    Output:
        Subset S of {o_1, o_2, ..., o_n} with maximum total value
        such that the sum of the weights <= capacity
    """
    n = len(items)
    A = np.zeros((n, capacity))  # where A[i][c] is the max value that
    # can be packed into a knapsack with capacity c
    # using objects {o_1, .., o_i}
    B = [
        [0 for i in range(capacity)] for j in range(n)
    ]  # Used to book keep for backtracing

    # Base Cases
    for c in range(capacity):
        if weights[0] <= c:
            A[0][c] = values[0]

    for i in range(1, n):
        for c in range(1, capacity):
            #             A[i][c] = max(A[i-1][c],
            #                           A[i-1][c-weights[i]]+values[i])
            if A[i - 1][c] >= A[i - 1][c - weights[i]] + values[i]:
                A[i][c] = A[i - 1][c]
                B[i][c] = (i - 1, c)
            else:
                A[i][c] = A[i - 1][c - weights[i]] + values[i]
                B[i][c] = (i - 1, c - weights[i])

    # backtracing
    objects = []
    i_, c_ = n - 1, capacity - 1
    while i_ >= 0 and c_ >= 0:
        i_, c_ = B[i_][c_]
        objects.append(items[i_])
        if B[i_][c_] == 0:
            break

    return objects, A[n - 1][capacity - 1]


def assert_equals(sol, opt):
    sol[0].sort()
    opt[0].sort()

    if any(x != y for x, y in zip(sol[0], opt[0])) or sol[1] != opt[1]:
        print(sol, "!=", opt)
        exit(1)


if __name__ == "__main__":
    assert_equals(
        knapsack(
            items=["A", "B", "C", "D"],
            values=[2.2, 4, 2, 3],
            weights=[2, 3, 3, 5],
            capacity=9,
        ),
        (["A", "B", "C"], 8.2),
    )
    print("All 0/1 Knapsack Tests passed!")
