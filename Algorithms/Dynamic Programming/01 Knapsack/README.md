# 0/1 Integer Weight Backpack Problem

## Problem

Suppose you are given:

* `n` items `{o_1, o_2, ..., o_n}`
* Values for the above items `{v_1, v_2, ..., v_n}`
* Weights for the above items `{w_1, w_2, ..., w_n}`
* The capacity of the knapsack `W` (integer)

Find the subset `S ⊆ {o_1, o_2, ..., o_n}` with maximum total value such that `∑_(i∈S) w_i ≤ W`.

That is, find the set of items with the greatest value that can fit into the backpack.

### Example

Items:

```
|-----------|---------|---------|---------|
| s_1       | s_2     | s_3     | s_4     |
|-----------|---------|---------|---------|
| v_1 = 2.2 | v_2 = 4 | v_1 = 2 | v_1 = 3 |
| w_1 = 5   | w_2 = 3 | w_1 = 3 | w_1 = 5 |
|-----------|---------|---------|---------|
```

`W = 9`

Optimal Solution:   `S = {o_1, o_2, o_3}` which has a total value of `8.2` and a weight of `8 < 9`.

## Preface

This problem is Intractable and NP-complete. It is uniquely difficult. No fast (polynomial time) algorithm exists for this problem.

The solution will try to use dynamic programming to be feasible to compute for small examples.

## Thought Experiment

Consider optimal solution `S∗`.

Tautology:
    * Case 1: `o_n ∉ S∗`
    * Case 2: `o_n ∈ S∗`

Claim 1: If `S∗` is in case 1, then `S∗` is the optimal solution to the subproblem `{o_1,...,o_(n−1)}`, `W`

Claim 2: If `S∗` is in case 2, then `S∗ − {o_n}` is the optimal solution to the subproblem `{o_1,...,o_(n−1)}`, `W−w_n`

Using this, we can construct the subproblem: `A[n][W]` where `A[i][c]` is the max value that can be packed into a knapsack with capacity `c`, using objects `{o_1,...,o_i}`

We can use this subproblem to create the final algorithms.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/01%20Knapsack/knapsack_01.py#L6)

Here is an implementation utilizing the subproblem found above to compute the final solution:

```python
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
```

### Runtime

Total: `O(nW)`
