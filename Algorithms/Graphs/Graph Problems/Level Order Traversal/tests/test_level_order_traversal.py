# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../../../"))

from BinaryTree import BinaryTree
from level_order_traversal import level_order_traversal


def test_level_order_traversal_1():
    tree = None
    for val in (10, 3, 20, 15, 24, 2):
        if tree is None:
            tree = BinaryTree(val)
        else:
            tree.insert(val)

    expected = [[10], [3, 20], [2, 15, 24]]

    result = level_order_traversal(tree)

    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert len(r) == len(e)
        assert set(r) == set(e)
