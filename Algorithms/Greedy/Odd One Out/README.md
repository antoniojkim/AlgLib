# Odd One Out

## Problem

Given a list of integers where every single element repeats an even number of times except for one element who repeats an odd number of times. Find the element that repeats an odd number of times.

## Solution

The solution can be done quite cleverly by exploiting the properties of XOR. For any integer `x`, `x ^ x = 0`. The XOR operator is associative and communative, so it does not matter the order in which the numbers are XORed together. For example, `x ^ y ^ x = y`.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Greedy/Odd%20One%20Out/odd_one_out.py#L5)

Keeping the above in mind, here is a clever simple solution to the problem:

```python
def odd_one_out(A: List[int]) -> int:
    n = 0
    for a in A:
        n ^= a

    return n
```

## Runtime

Total: `O(n)`.
