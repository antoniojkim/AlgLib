# [Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)

## Problem

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Your solution should run in O(log n) time and O(1) space.

### Examples

```
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Input: nums = [3,3,7,7,10,11,11]
Output: 10
```

## Solution

We can use a divide and conque approach to solve this much quicker than linear time

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Divide%20and%20Conquer/Single%20Element%20in%20a%20Sorted%20Array/single_element_sorted_array.py#L5)

```python
def single_non_duplicate(nums: List[int]) -> int:
    l = 0
    r = len(nums)-1

    while(l < r):
        m = (l + r + 1) // 2
        if m+1 < len(nums) and nums[m] == nums[m+1]:
            if m % 2 == 0:
                l = m+2
            else:
                r = m-1
        elif m > 0 and nums[m] == nums[m-1]:
            if m % 2 == 0:
                r = m-2
            else:
                l = m+1

        else:
            l = m
            break

    return nums[l]
```

### Runtime

Runtime: `O(log(n))`
Space: `O(1)`
