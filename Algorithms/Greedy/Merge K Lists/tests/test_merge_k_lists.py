# -*- coding: utf-8 -*-
import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from mergeKlists import mergeKLists


def test_merge_k_lists():
    for i in range(100):
        lists = [
            sorted(np.random.randint(100, size=np.random.randint(5, 20)))
            for i in range(np.random.randint(2, 10))
        ]
        expected = sorted(sum(lists, []))
        merged = mergeKLists(lists)

        assert merged == expected
