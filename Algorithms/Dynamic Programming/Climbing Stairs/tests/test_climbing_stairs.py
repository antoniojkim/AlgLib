# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from climbing_stairs import climbStairs


def test_climbing_stairs_1():
    assert climbStairs(2) == 2


def test_climbing_stairs_2():
    assert climbStairs(3) == 3


def test_climbing_stairs_3():
    assert climbStairs(5) == 8
