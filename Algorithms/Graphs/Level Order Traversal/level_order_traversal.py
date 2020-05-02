# -*- coding: utf-8 -*-


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val < self.val:
            if self.left is not None:
                self.left.insert(val)

            else:
                self.left = Node(val)

        else:
            if self.right is not None:
                self.right.insert(val)

            else:
                self.right = Node(val)


def print_bt(root, indent=""):
    if root is None:
        return

    print_bt(root.left, indent + "    ")
    print(indent, root.val)
    print_bt(root.right, indent + "    ")


def level_order_traversal(tree):
    if tree is None:
        return tree

    left = []
    if tree.left is not None:
        left = level_order_traversal(tree.left)

    right = []
    if tree.right is not None:
        right = level_order_traversal(tree.right)

    if len(left) > len(right):
        larger = left
        smaller = right

    else:
        larger = right
        smaller = left

    for i in range(len(smaller)):
        larger[i].extend(smaller[i])

    return [[tree.val]] + larger


if __name__ == "__main__":

    tree = None
    for val in (10, 3, 20, 15, 24):
        if tree is None:
            tree = Node(val)
        else:
            tree.insert(val)

    print_bt(tree)

    print(level_order_traversal(tree))
