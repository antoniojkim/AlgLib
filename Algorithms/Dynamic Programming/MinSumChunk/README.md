# Minimum Sum Chunk

## Problem

Given a sequence of `n` integers `a_1,...,a_n` and an integer `t`, we want to divide the sequence into `t` chunks so as to minimize the sum of the squares of the chunk sums. In
other words, we want to find `1 < i_1 < i_2 < ... < i_(t−1) < n` to minimize `(a_1+...+a_(i_1−1))^2 + (a_(i_1)+...+a_(i_2−1))^2 + ... + (a_(i_(t−1))+...+a_n)^2`.

### Example

Given

```
[1, 2, 3],   t = 2
```

Then we have two cases:
* `[{1, 2}, {3}] -> (1+2)^2 + (3)^2 = 18`
* `[{1}, {2, 3}] -> (1)^2 + (2+3)^2 = 26`

The solution is clearly `[{1, 2}, {3}]` since it has the smallest sum of the squares of the sums of the subarrays.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/MinSumChunk/minSumChunk.py#L7)

Here is an implementation using dynamic programming:

```python
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
```

### Runtime

Total: `O(nt^2)`
