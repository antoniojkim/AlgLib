# [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Problem

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You are given a target value to search. If found in the array return its index, otherwise return `-1`.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of `O(log n)`.

### Examples

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## Solution

We use a modified binary search.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Divide%20and%20Conquer/Search%20in%20Rotated%20Sorted%20Array/search_in_rotated_sorted_array.py#L5)

```python
def search_in_rotated_sorted_array(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        if target > nums[m]:
            if target > nums[r] >= nums[m]:
                r = m - 1
            else:
                l = m + 1
        elif target < nums[l] <= nums[m]:
            l = m + 1
        else:
            r = m - 1

    return -1
```

### Runtime

`O(log n)`
