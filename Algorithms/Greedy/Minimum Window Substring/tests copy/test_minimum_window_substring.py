# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from minimum_window_substring import minimum_window_substring


def test_minimum_window_substring_1():
    assert minimum_window_substring("ADOBECODEBANC", "ABC") == "BANC"


def test_minimum_window_substring_2():
    assert minimum_window_substring("bba", "ab") == "ba"
