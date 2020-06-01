# -*- coding: utf-8 -*-
import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../../"))

from BinaryTree import BinaryTree
from bt_to_dll import binary_tree_to_doubly_linked_list


def test_bt_to_dll_1():
    vals = np.random.randint(0, 20, size=10)
    root = None
    for val in vals:
        if root is None:
            root = BinaryTree(val)
        else:
            root.insert(val)

    start, end = binary_tree_to_doubly_linked_list(root)

    array_list = []
    current = start
    while current != end:
        array_list.append(current.val)
        current = current.right

    array_list.append(current.val)

    vals = sorted(vals)

    assert len(array_list) == len(vals)
    for r, e in zip(array_list, vals):
        assert r == e
