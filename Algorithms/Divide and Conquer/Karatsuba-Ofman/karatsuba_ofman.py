# -*- coding: utf-8 -*-
from typing import List


def karatsuba_ofman(X: List[int], Y: List[int]) -> int:
    if len(X) != len(Y):
        raise Exception("Invalid Input")

    n = len(X)

    if n == 0:
        return 0
    elif n == 1:
        return X[0] * Y[0]

    a = X[: n // 2]
    b = X[n // 2 :]
    c = Y[: n // 2]
    d = Y[n // 2 :]

    Vac = karatsuba_ofman(a, c)
    Vbd = karatsuba_ofman(b, d)
    Vab_cd = karatsuba_ofman(a + b, c + d)

    factor = 10 ** (n // 2)
    return (Vac * factor + (Vab_cd - Vac - Vbd)) * factor + Vbd
