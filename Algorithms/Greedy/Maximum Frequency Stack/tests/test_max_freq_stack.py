# -*- coding: utf-8 -*-

import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from max_freq_stack import FreqStack


def test_max_freq_stack():
    fs = FreqStack()
    for i in [5, 7, 5, 7, 4, 5]:
        fs.push(i)

    assert fs.pop() == 5
    assert fs.pop() == 7
    assert fs.pop() == 5
    assert fs.pop() == 4
