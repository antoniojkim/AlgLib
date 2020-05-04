# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../../"))

from BinaryTree import BinaryTree


def binary_tree_to_doubly_linked_list(root: BinaryTree):
    if root is None:
        return root, root

    if root.left is None and root.right is None:
        root.left = root
        root.right = root
        return root, root

    ll = None
    rr = None

    if root.left is not None:
        ll, lr = binary_tree_to_doubly_linked_list(root.left)
        lr.right = root
        root.left = lr
    else:
        ll = root

    if root.right is not None:
        rl, rr = binary_tree_to_doubly_linked_list(root.right)
        rl.left = root
        root.right = rl
    else:
        rr = root

    ll.left = rr
    rr.right = ll

    return ll, rr
