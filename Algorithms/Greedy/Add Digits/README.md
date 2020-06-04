# [Add Digits](https://leetcode.com/problems/add-digits/)

## Problem

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Create an `O(1)` algorithm to solve this problem.

### Examples

```
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
```

## Solution



## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Greedy/Add%20Digits/add_digits.py#L4)

```python
def add_digits(num: int) -> int:
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9
```

### Runtime

`O(1)`
