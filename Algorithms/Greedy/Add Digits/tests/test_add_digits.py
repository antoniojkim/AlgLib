# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from add_digits import add_digits


def test_add_digits_1():
    assert add_digits(38) == 2
