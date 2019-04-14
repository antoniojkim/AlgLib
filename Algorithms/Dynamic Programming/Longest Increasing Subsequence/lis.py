
import numpy as np

def lis(a):
    M = np.zeros(len(a), dtype=int)
    for k in range(len(M)):
        M[k] = 1
        for j in range(k-1):
            if a[j] < a[k]:
                M[k] = max(M[k], M[j]+1)
                
    return max(M)


def test_lis(result, expected):
    if (result != expected):
        raise Exception(f"{result} != {expected}")

if __name__ == "__main__":
    test_lis(lis(
        [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    ),
    6)
    print("All Longest Increasing Subsequence Tests Passed!")
