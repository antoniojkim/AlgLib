# Binary to Decimal

Given an array of binary numbers (0 or 1), convert that into a decimal number

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Divide%20and%20Conquer/Bin%20to%20Dec/binToDec.py#L4)

We use divide and conquer to solve the problem which avoids the use of strings and string to decimal conversions:

```python
def binToDec(b: List[int]):
    n = len(b)
    if n == 1:
        return b[0]

    L = binToDec(b[: n // 2])
    R = binToDec(b[n // 2 :])

    return L * 2 ** (n - n // 2) + R
```

### Runtime

According to the [master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)#Generic_form), since

```
a = 2, b = 2   ->   log(a)/log(b) = 1
```

and the "recombine" step is `O(1)`, we have that the total runtime is `O(n)`.
