# Karatsuba-Ofman Algorithm for Integer Multiplication

Input: 2 `n`-digit integers `X`, `Y`

Output: `Z = XY`

## Algorithm

### Naive Algorithm

The ["primary-school"](https://en.wikipedia.org/wiki/Multiplication_algorithm#Long_multiplication) algorithm has a runtime of `O(n^2)`.

### Karatsuba-Ofman

The Karatsuba-Ofman improves upon the classic long multiplication algorithm for *integers only*.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Divide%20and%20Conquer/Karatsuba-Ofman/karatsuba_ofman.py#L5)

Here is an implementation:

```python
def karatsuba_ofman(X: List[int], Y: List[int]) -> int:
    n = len(X)

    if n == 1:
        return X[0] * Y[0]
    elif n == 0:
        return 0

    a = X[: n // 2]
    b = X[n // 2 :]
    c = Y[: n // 2]
    d = Y[n // 2 :]

    Vac = karatsuba_ofman(a, c)
    Vbd = karatsuba_ofman(b, d)
    Vab_cd = karatsuba_ofman(a + b, c + d)

    factor = 10 ** (n // 2)
    return (Vac * factor + (Vab_cd - Vac - Vbd)) * factor + Vbd
```

### Runtime

According to the [master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)#Generic_form), the runtime is `O(n^1.59)`.

# Karatsuba-Ofman Algorithm for Polynomial Multiplication

Input: 2 polynomials `X` and `Y` of degree `n`.

Output: `Z = XY`

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Divide%20and%20Conquer/Karatsuba-Ofman/poly_mul.py#L11)

```python
def poly_mul(X: List[int], Y: List[int]):
    n = len(X)

    if n == 0:
        return 0
    elif n == 1:
        return X * Y

    a = X[: n // 2]
    b = X[n // 2 :]
    c = Y[: n // 2]
    d = Y[n // 2 :]

    Vac = poly_mul(a, c)
    Vbd = poly_mul(b, d)
    tmp = poly_mul(a + b, c + d)

    tmp = tmp - Vac - Vbd

    Vac = zero_pad(Vac, (0, n))
    tmp = zero_pad(tmp, (0, n // 2))

    maxlen = max(len(Vac), len(tmp), len(Vbd))

    return (
        zero_pad(Vac, (maxlen - len(Vac), 0))
        + zero_pad(tmp, (maxlen - len(tmp), 0))
        + zero_pad(Vbd, (maxlen - len(Vbd), 0))
    )
```
