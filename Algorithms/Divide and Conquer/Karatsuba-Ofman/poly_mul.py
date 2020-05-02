# -*- coding: utf-8 -*-
import numpy as np


def zero_pad(a, n):
    return np.pad(a, n, "constant", constant_values=0)


def poly_mul(X, Y):
    """
    Polynomial Multiplication using variation of Karatsuba-Ofman Algorithm
    """
    if len(X) != len(Y):
        raise Exception("Invalid Input")

    n = len(X)

    if n == 1:
        return X * Y
    elif n == 0:
        return 0

    a = X[: n // 2]
    b = X[n // 2 :]
    c = Y[: n // 2]
    d = Y[n // 2 :]

    Vac = poly_mul(a, c)
    Vbd = poly_mul(b, d)
    tmp = poly_mul(a + b, c + d)

    #     n = len(X)+len(X)%2

    tmp = tmp - Vac - Vbd

    Vac = zero_pad(Vac, (0, n))
    tmp = zero_pad(tmp, (0, n // 2))

    maxlen = max(len(Vac), len(tmp), len(Vbd))

    return (
        zero_pad(Vac, (maxlen - len(Vac), 0))
        + zero_pad(tmp, (maxlen - len(tmp), 0))
        + zero_pad(Vbd, (maxlen - len(Vbd), 0))
    )


if __name__ == "__main__":
    X = np.array([1, 2])
    Y = np.array([1, 3])

    assert np.array_equal(poly_mul(X, Y), np.array([1, 5, 6]))
