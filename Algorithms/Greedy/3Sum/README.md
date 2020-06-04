# [3Sum](https://leetcode.com/problems/3sum/)

## Problem

Given an array nums of `n` integers, are there elements `a`, `b`, `c` in nums such that `a + b + c = 0`? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

### Examples

Given array nums = `[-1, 0, 1, 2, -1, -4]`,

A solution set is:
```
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

## Solution

The naive solution would be to search all possible combinations and form a list from there. However, this has runtime `O(n^3)`. We can do better.

The trick here is to search in combinations of two and check to see if the third number exists in the list.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Greedy/3Sum/three_sum.py#L7)

```python
def three_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    nums = Counter(nums)

    zero_sums = set()
    for a, b in combinations_with_replacement(nums, 2):
        c = -a-b

        if c in nums:
            add = True
            if a == b == c:
                add = nums[a] > 2
            elif a == b:
                add = nums[a] > 1
            elif a == c:
                add = nums[a] > 1
            elif b == c:
                add = nums[b] > 1

            if add:
                zero_sums.add(tuple(sorted((a, b, c))))

    return zero_sums
```

### Runtime

`O(n^2)`
