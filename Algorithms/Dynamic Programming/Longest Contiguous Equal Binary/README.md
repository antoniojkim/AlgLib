# Longest Contiguous Equal Binary

## Problem

Given a binary array(array only containing 0 and 1), find the maximum length of a contiguous subarray where the number of 0’s is equal to the number of 1’s.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/Longest%20Contiguous%20Equal%20Binary/equal_binary.py#L5)

Here is an implementation using dynamic programming:

```python
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
```
