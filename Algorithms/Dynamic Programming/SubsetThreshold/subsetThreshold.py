# -*- coding: utf-8 -*-
from numpy import bool, zeros


def subsetThreshold(a, m):
    n = len(a)
    C = zeros((n + 1, n + 1, n * m), dtype=bool)

    for i in range(1, n + 1):
        if a[i - 1] < n * m:
            C[i][1][a[i - 1]] = 1
            for j in range(1, i + 1):
                for l in range(1, n * m):
                    if i > 1 and C[i - 1][j][l]:
                        C[i][j][l] = 1

                    if C[i - 1][j - 1][l - a[i - 1]]:
                        C[i][j][l] = 1

    S = set()
    i = n
    j = n // 2
    asum = sum(a)
    for l in range(n * m // 4 + 1, n * m):
        if C[i][j][l] == 1 and asum - l > n * m // 4:
            while i >= 0 and j >= 0 and l > 0:
                if C[i - 1][j][l] == 0:
                    S.add(a[i - 1])
                    l -= a[i - 1]
                    j -= 1

                i -= 1

            return True, S, set(a) - S

    return False, set(), set()
