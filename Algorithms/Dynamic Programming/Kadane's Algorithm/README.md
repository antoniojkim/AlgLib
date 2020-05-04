# Kadane's Algorithm (Maximum Subarray Problem)

## Problem

In the maximum subarray problem, we are given as input an array `A[1],...,A[n]` of `n` integers. Our goal is to find the maximum value of any subarray of `A`. i.e., the valid solution is the value

```
max_{i,j ; 1≤i≤j≤n} ∑_(l=i..j) A[l]
```

## Algorithm

Let `B` be a solution array such that `B[j]` is the maximum subarray that ends at `A[j-1]`, i.e.

```
B[j] = max_{i,j ; 1≤i≤j} ∑_(l=i..j) A[l]
```

The key observation for Kadane's algorithm is that there are only two possibilities to consider for `B[j]`:
* it includes the maximum subarray that ends at `A[j−1]` (along with `A[j]`)
* it does not include the maximum subarray (in which case `B[j] = A[j]`).

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/Kadane's%20Algorithm/kadane.py#L7)

Here is a simple implementation:

```python
def kadane(A: List[int]):
    B = zeros(len(A))
    B[0] = A[0]
    msub = B[0]
    for j in range(1, len(B)):
        B[j] = max(A[j], B[j - 1] + A[j])
        msub = max(msub, B[j])

    return msub
```

## Runtime

Overall, the algorithm makes one pass through the solution array of length `n`. So, the runtime is `O(n)`
