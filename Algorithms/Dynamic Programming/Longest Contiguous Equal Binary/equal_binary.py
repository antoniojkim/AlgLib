# -*- coding: utf-8 -*-
from typing import List


def equal_binary(arr: List[int]):
    n = len(arr)

    max_len = 0
    running_total = 0
    for i in range(n):
        running_total += arr[i]
        current_total = running_total

        for j in range(i + 1):
            if (
                (i - j + 1) % 2 == 0
                and current_total == (i - j + 1) // 2
                and (i - j + 1) > max_len
            ):
                max_len = i - j + 1

            current_total -= arr[j]

    return max_len
