# Matrix Multiplication Order

## Problem

Given the dimensions of `n` rectangular matrices, where the column dimension of `A_i` is equal to the row dimension of `A_(i+1)`, find the minimum cost parenthesization for multiplying `n` matrices with the given dimensions where given `A`, `B`, cost `(A×B) = pqr`

```
            q                        r
  +-------------------+         +---------+
  |                   |         |         |
p |                   |         |         |
  |                   |         |         |
  +-------------------+       q |         |
                                |         |
        A                       |         |
                                |         |
                                |         |
                                +---------+

                                    B
```

### Example

```
        5                 20                      10
    +-------+     +------------------+       +---------+
    |       |   5 |                  |       |         |
    |       |     |                  |       |         |
    |       |     +------------------+    20 |         |
    |       |                                |         |
100 |       |           A_2                  |         |
    |       |                                |         |
    |       |                                +---------+
    |       |
    |       |                                    A_3
    |       |
    +-------+

        A_1
```

For the above matrices, one possible parenthesization is `((A_1 * A_2) * A_3)`. Then, the total cost is `(100×5×20) + (100×20×10) = 30000`.

Another possible parenthesization is `(A_1 * (A_2 * A_3))`. Then, the total cost is `(5×20×10) + (100×5×10) = 6000`.

In total, there are  `Ω(4^n/n^(3∕2))` different parenthesizations. Thus, a brute force solution is definitely not great.

Instead we use dynamic programming to create a better solution.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/Matrix%20Multiplication%20Order/matmul_order.py#L7)

Here is an implementation using dynamic programming:

```python
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
```

### Runtime

Total: `O(n^3)`
