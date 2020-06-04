# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from coin_change import coin_change


def test_coin_change_1():
    assert coin_change([1, 2, 5], 11) == 3


def test_coin_change_2():
    assert coin_change([2], 3) == -1
