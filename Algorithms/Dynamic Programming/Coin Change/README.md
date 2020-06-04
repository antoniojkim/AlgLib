# [Coin Change](https://leetcode.com/problems/coin-change/)

## Problem

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

### Examples

```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
```

## Solution

We choose a top down dynamic programming approach. Let `S` be the optimal solution. Notice that the optimal solution is the optimal solution for `amount - c` plus one more coin with value `c`. However, since we don't know which coin this might be, we try out every single coin and take the one that produces the least number of coins.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/Coin%20Change/coin_change.py#L8)

```python
def coin_change(self, coins: List[int], amount: int) -> int:
    if amount < 1:
        return 0

    counts = zeros(amount)

    def recurse(amount):
        nonlocal counts
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if counts[amount-1] != 0:
            return counts[amount-1]

        min_count = inf
        for c in coins:
            count = recurse(amount - c)
            if count >= 0 and count < min_count:
                min_count = count + 1

        counts[amount-1] = -1 if isinf(min_count) else int(min_count)
        return counts[amount-1]

    return recurse(amount)
```

### Runtime

`O(amount * number of coins)`
