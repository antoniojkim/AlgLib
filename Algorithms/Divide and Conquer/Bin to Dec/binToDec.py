# -*- coding: utf-8 -*-
import numpy as np


def binToDec(b):
    n = len(b)
    if n == 1:
        return b[0]

    L = binToDec(b[: n // 2])
    R = binToDec(b[n // 2 :])

    return L * 2 ** (n - n // 2) + R


def test_binToDec(b):
    expected = int("".join(map(str, b)), 2)
    result = binToDec(b)
    if result != expected:
        raise Exception(f"{result} != {expected}")


#     else:
#         print(f"{result} == {expected}")

if __name__ == "__main__":
    for i in range(10000):
        test_binToDec(list(np.random.randint(2, size=np.random.randint(10, 50))))

    print("All Divide and Conquer Binary to Decimal Tests Passed!")
