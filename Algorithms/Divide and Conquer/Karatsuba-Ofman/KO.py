# -*- coding: utf-8 -*-
import numpy as np


def int_to_list(i):
    return np.array([int(d) for d in str(i)])


def KO(X, Y):
    """
    Karatsuba-Ofman algorithm for integer multiplication
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

    Vac = KO(a, c)
    Vbd = KO(b, d)
    tmp = KO(a + b, c + d)

    return Vac * 10 ** n + (tmp - Vac - Vbd) * 10 ** (n // 2) + Vbd


if __name__ == "__main__":
    for i in range(10):
        X = np.random.randint(10, 100)
        Y = np.random.randint(10, 100)
        XY = X * Y
        X = int_to_list(X)
        Y = int_to_list(Y)

        assert KO(X, Y) == XY

    print("All KO Tests passed!")
