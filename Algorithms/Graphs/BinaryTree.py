# -*- coding: utf-8 -*-


class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val < self.val:
            if self.left is not None:
                self.left.insert(val)

            else:
                self.left = BinaryTree(val)

        else:
            if self.right is not None:
                self.right.insert(val)

            else:
                self.right = BinaryTree(val)

    def __iter__(self):
        if self.left is not None:
            yield from iter(self.left)

        yield self.val

        if self.right is not None:
            yield from iter(self.right)

    def __repr__(self):
        return "Binary Tree: [" + " ".join(map(str, iter(self))) + "]"

    @staticmethod
    def print_tree(bt, indent=""):
        if bt.left is not None:
            yield from BinaryTree.print_tree(bt.left, indent + "    ")

        yield indent + str(bt.val)

        if bt.right is not None:
            yield from BinaryTree.print_tree(bt.right, indent + "    ")

    def __str__(self):
        return "\n".join(BinaryTree.print_tree(self, ""))
