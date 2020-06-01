# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from lps import longest_palindrome_substring


def test_longest_palindrome_substring_1():
    assert longest_palindrome_substring("AABACCAAA") == 4


def test_longest_palindrome_substring_2():
    assert longest_palindrome_substring("MADAM") == 5


def test_longest_palindrome_substring_3():
    assert longest_palindrome_substring("RACECAR") == 7


def test_longest_palindrome_substring_4():
    assert longest_palindrome_substring("saippuakivikauppias") == 19


def test_longest_palindrome_substring_5():
    assert longest_palindrome_substring("sgafgsaippuakivikauppiasafshdg") == 19
