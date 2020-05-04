# -*- coding: utf-8 -*-
import os
import sys
from typing import List

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../../"))

from BinaryTree import BinaryTree


def level_order_traversal(tree: BinaryTree) -> List[List[str]]:
    if tree is None:
        return []
    else:
        levels = []
        queue = [tree]

        while queue:
            level = []
            next_queue = []
            for current in queue:
                level.append(current.val)
                if current.left:
                    next_queue.append(current.left)
                if current.right:
                    next_queue.append(current.right)

            levels.append(level)
            queue = next_queue

        return levels
