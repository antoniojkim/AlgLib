# -*- coding: utf-8 -*-
from typing import List


def binToDec(b: List[int]) -> int:
    n = len(b)
    if n == 1:
        return b[0]

    L = binToDec(b[: n // 2])
    R = binToDec(b[n // 2 :])

    return L * 2 ** (n - n // 2) + R
