# [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

## Problem

You are climbing a stair case. It takes `n` steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given `n` will be a positive integer.

### Examples

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Solution

The key idea to see here is that to reach the `n`th step, you can get to it by taken a step of 1 from the `n-1`th step or by taking a step of 2 from the `n-2`th step.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/Climbing%20Stairs/climbing_stairs.py#L4)

```python
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
```

## Runtime

`O(n)`
