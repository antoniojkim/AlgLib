# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from min_score_triangulation import min_score_triangulation


def test_min_score_triangulation_1():
    assert min_score_triangulation([1, 2, 3]) == 6


def test_min_score_triangulation_2():
    assert min_score_triangulation([3, 7, 4, 5]) == 144


def test_min_score_triangulation_3():
    assert min_score_triangulation([1, 3, 1, 4, 1, 5]) == 13
