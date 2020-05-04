# Maximum of the Minimum Sum of Segments

## Problem

Given an array of integers `A`, split the array into `k` contiguous segments such that the minimum of the sums of the segments is maximized.

## Example

Consider the following input `A = [6, 3, 2, 8, 7, 5]`, and `k = 3`.

One possible split of `3` contiguous segments is: `[{6}, {3, 2}, {8, 7, 5}]`. The sums of the segments are `6, 5, 20` respectively. The minimum of these sums is `5`.

The split that maximizes the minimum of the sums of the segments is `[{6, 3}, {2, 8}, {7, 5}]`. The sums of the segments are `9, 10, 12` respectively. The minimum of these sums is `9`.

## Solution

This is a difficult problem for a number of reasons. It is difficult to come up with the correct approach to this problem. A common mistake is to try and approach this as a dynamic programming problem. However, the correct approach is a binary search variation.

The idea is to perform binary search on the minimum value itself. The smallest this value could possibly be is the minimum of `A` and the highest this value could possibly be is the sum of `A`. From here, for each "guess", we see how many contiguous segments the array can be split into where the sum of each segment is at least the "guess". If the number of segments is less than `k`, then the guess was too high and we guess lower (binary search style). If the number of segments is more than `k`, then the guess was too low and we guess higher (binary search style). We repeat this until we converge on a value.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Divide%20and%20Conquer/Maximum%20of%20Minimum%20Sum%20of%20Segments/max_min_sum_segments.py#L5)

Here is an implementation of the above described solution:

```python
def max_min_sum_segments(A: List[int], k: int) -> int:
    def split(min_sum):
        count = 0
        segment_sum = 0
        for a in A:
            segment_sum += a
            if segment_sum >= min_sum:
                count += 1
                segment_sum = 0

        return count

    l = min(A)
    h = sum(A)

    while l < h:
        min_sum = (l + h + 1) // 2
        if split(min_sum) < k:
            h = min_sum - 1
        else:
            l = min_sum

    return l
```
