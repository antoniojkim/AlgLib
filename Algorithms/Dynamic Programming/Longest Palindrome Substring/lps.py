# -*- coding: utf-8 -*-
from numpy import zeros


def longest_palindrome_substring(s):
    n = len(s)
    A = zeros((n, n))

    for i in range(n):
        A[i][0] = True
        if i < n - 1:
            A[i][1] = s[i] == s[i + 1]

    longest = 0
    for j in range(2, n):
        l = j // 2
        for i in range(l, n - l):
            if A[i][j - 2] and s[i - l] == s[i + l]:
                A[i][j] = True
                longest = max(longest, j)

    return longest + 1
