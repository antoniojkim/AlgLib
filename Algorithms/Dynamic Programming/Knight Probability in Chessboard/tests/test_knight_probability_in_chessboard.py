# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from knight_probability_in_chessboard import knight_probability_in_chessboard


def test_knight_probability_in_chessboard_1():
    assert knight_probability_in_chessboard(3, 2, 0, 0) == 0.0625
