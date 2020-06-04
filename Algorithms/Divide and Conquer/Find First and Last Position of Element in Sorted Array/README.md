# [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Problem

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of `O(log n)`.

If the target is not found in the array, return `[-1, -1]`.

### Examples

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

## Solution

The idea is to use binary search to find the leftmost occurence of the target and the rightmost occurence of the target.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Divide%20and%20Conquer/Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array/find_first_and_last_position_of_element_in_sorted_array.pyL#5)

```python
def find_first_and_last_position_of_element_in_sorted_array(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]

    start = 0
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r + 1) // 2
        if nums[m] == target:
            start = m

        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1

    if nums[start] != target:
        return [-1, -1]

    end = start
    l = start
    r = len(nums) - 1
    while l <= r:
        m = (l + r + 1) // 2
        if nums[m] == target:
            end = m

        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1

    return [start, end]

```

### Runtime

`O(log n)`
