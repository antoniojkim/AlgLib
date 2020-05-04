# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from matmul_order import matmul_order


def test_matmul_order():
    order, cost = matmul_order([100, 5, 20, 10])

    assert order == [0]
    assert cost == 6000
