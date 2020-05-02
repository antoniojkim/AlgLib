# -*- coding: utf-8 -*-

import numpy as np


def longest_palindrome_substring(s):
    n = len(s)
    A = np.zeros((n, n))

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


def test_longest_palindrome_substring(result, expected):
    if result != expected:
        raise Exception(f"{result} != {expected}")


if __name__ == "__main__":
    tests = [
        ("AABACCAAA", 4),
        ("MADAM", 5),
        ("RACECAR", 7),
        ("saippuakivikauppias", 19),
        ("sgafgsaippuakivikauppiasafshdg", 19),
    ]
    for s, expected in tests:
        test_longest_palindrome_substring(longest_palindrome_substring(s), expected)

    print("All Longest Palindrome Substring tests passed!")
