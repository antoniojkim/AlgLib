# Longest Increasing Subsequence

## Problem

Given a sequence of non-negative integers `a_1,...,a_n`, design an algorithm that computes the length of the longest subsequence of increasing numbers within the original sequence.

### Example

For

```python
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
```

one of the longest increasing subsequences is `[0, 4, 6, 9, 11, 15]` so the valid solution for this instance
is 6. (Note that there are multiple increasing subsequences of length 6 for this example.)

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/Longest%20Increasing%20Subsequence/lis.py#L7)

Here is an implementation using dynamic programming:

```python
def longest_increasing_subsequence(a: List[int]):
    M = zeros(len(a), dtype=int)
    for k in range(len(M)):
        M[k] = 1
        for j in range(k - 1):
            if a[j] < a[k]:
                M[k] = max(M[k], M[j] + 1)

    return max(M)
```
