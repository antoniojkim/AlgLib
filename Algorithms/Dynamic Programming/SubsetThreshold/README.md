# Subset Threshold

## Problem

Suppose we have a set `X` of `n` pairs of numbers `(a_i, b_i)`, such that for each `i` the sum of `a_i + b_i = m`. You can assume all `a_i` and `b_i` are non-negative integers. Our goal is to find out if it is possible to divide `X` into two disjoint subsets of size `n/2`, `S` and `R = X − S`, such that the average of the a values in both S and R are strictly greater than `m/2` (or equivalently the sum of the `a` values is greater than `mn/4`).

### Example

Consider the following example with `n = 4` pairs of numbers where `m = 200`.

|    | a   | b   |
|----|-----|-----|
| p1 | 110 | 90  |
| p2 | 84  | 116 |
| p3 | 120 | 80  |
| p4 | 94  | 106 |

For this example, it is possible to divide the set into two disjoint subsets that meet the conditions. If we set `S = {p_1, p_4}` and `R = {p_2, p_2}`, then the
`a` values in `S` is `204 > 200`. Similarly the `a` values in `R` is `204 > 200`.


## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/SubsetThreshold/subsetThreshold.py#L5)

Here is an implementation using dynamic programming:

```python
def subsetThreshold(a, m):
    n = len(a)
    C = zeros((n + 1, n + 1, n * m), dtype=bool)

    for i in range(1, n + 1):
        if a[i - 1] < n * m:
            C[i][1][a[i - 1]] = 1
            for j in range(1, i + 1):
                for l in range(1, n * m):
                    if i > 1 and C[i - 1][j][l]:
                        C[i][j][l] = 1

                    if C[i - 1][j - 1][l - a[i - 1]]:
                        C[i][j][l] = 1

    S = set()
    i = n
    j = n // 2
    asum = sum(a)
    for l in range(n * m // 4 + 1, n * m):
        if C[i][j][l] == 1 and asum - l > n * m // 4:
            while i >= 0 and j >= 0 and l > 0:
                if C[i - 1][j][l] == 0:
                    S.add(a[i - 1])
                    l -= a[i - 1]
                    j -= 1

                i -= 1

            return True, S, set(a) - S

    return False, set(), set()
```

### Runtime

Total: `O(m(n-1)n^2)`
