# -*- coding: utf-8 -*-

import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from dll_to_bt import DoublyLinkedList, doubly_linked_list_to_binary_tree


def binary_tree_generator(bt):
    if bt.prev is not None:
        yield from binary_tree_generator(bt.prev)

    yield bt.val

    if bt.next is not None:
        yield from binary_tree_generator(bt.next)


def test_dll_to_bt_1():
    vals = sorted(np.random.randint(0, 20, size=10))
    ll = None
    for val in vals:
        if ll is None:
            ll = DoublyLinkedList(val)
        else:
            ll.emplace_back(val)

    assert len(list(ll)) == len(vals)

    root = doubly_linked_list_to_binary_tree(ll)

    assert len(list(binary_tree_generator(root))) == len(vals)

    for val, l, t in zip(vals, ll, binary_tree_generator(root)):
        assert val == l
        assert val == t
