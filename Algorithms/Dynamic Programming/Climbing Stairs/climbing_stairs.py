# -*- coding: utf-8 -*-


def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2

    last1 = 1
    last2 = 2
    for i in range(2, n):
        last = last1 + last2
        last1 = last2
        last2 = last

    return last2
