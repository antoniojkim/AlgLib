# -*- coding: utf-8 -*-


import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from binToDec import binToDec


def test_binToDec():
    for i in range(1000):
        b = np.random.randint(2, size=np.random.randint(10, 50))
        assert binToDec(b) == int("".join(map(str, b)), 2)
