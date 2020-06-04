# -*- coding: utf-8 -*-
from math import inf, isinf
from typing import List

from numpy import zeros


def coin_change(coins: List[int], amount: int) -> int:
    if amount < 1:
        return 0

    counts = zeros(amount)

    def recurse(amount):
        nonlocal counts
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if counts[amount - 1] != 0:
            return counts[amount - 1]

        min_count = inf
        for c in coins:
            count = recurse(amount - c)
            if count >= 0 and count < min_count:
                min_count = count + 1

        counts[amount - 1] = -1 if isinf(min_count) else int(min_count)
        return counts[amount - 1]

    return recurse(amount)
