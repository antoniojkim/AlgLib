# Linear Independent Set

## Problem

Input: An undirected line graph `G(V, E)` and (non-negative) weights on nodes, where `n = |V|`

Output: The max-weight independent set in `G`.

i.e. a subset `S∗ ⊆ V`  such that `∀ u,v ∈ S∗` `u` and `v` are not connected.

### Example

```
{A:1} -- {B:5} -- {C:6} -- {D:3}
```

`{A, C} = 7, {A, D} = 4, {B, D} = 8`

Optimal solution would be `{B, D}`

## Algorithm

### Naive Algorithm

Search all `2^n` subsets of `V` and keep track of the max weight independent subset.

Runtime: `Θ(2^n)`

### Better Solution

We use dynamic programming to try and construct a better algorithm.

Let `S∗` be the optimal solution.

Tautology: Only two possibilities
* Case 1:  If `v_n ∉ S∗`, then `S∗` is `opt_(n−1)`
* Case 2:  If `v_n ∈ S∗`, then `S∗ − {v_n}` is `opt_(n−2)`

Using this observation we can construct the subproblems used in final algorithm.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/Linear%20Independent%20Set/linear_independent_set.py#L7)

Here is an implementation of the algorithm:

```python
def lis(V: List[int]):
    A = zeros(len(V) + 1, dtype=int)
    S = [[] for _ in range(len(A))]
    A[0] = 0
    A[1] = V[0][1]
    S[1].append(V[0][0])

    for i in range(2, len(A)):
        if A[i - 1] <= A[i - 2] + V[i - 1][1]:
            A[i] = A[i - 2] + V[i - 1][1]
            S[i] = S[i - 2] + [V[i - 1][0]]
        else:
            A[i] = A[i - 1]
            S[i] = S[i - 1]

    return A[-1], S[-1]
```

### Runtime

Total: `O(n)`

Far better than the naive solution!
