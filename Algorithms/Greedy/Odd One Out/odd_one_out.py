# -*- coding: utf-8 -*-
from typing import List


def odd_one_out(A: List[int]) -> int:
    """
    Given a list of integers where every single
    element repeats an even number of times except
    for one element who repeats an odd number of times.
    The following algorithm finds the element that
    repeats an odd number of times.
    """
    n = 0
    for a in A:
        n ^= a

    return n
