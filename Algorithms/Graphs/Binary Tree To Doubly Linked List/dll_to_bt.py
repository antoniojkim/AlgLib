# -*- coding: utf-8 -*-

import numpy as np


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self
        self.next = self

    def emplace_back(self, val):
        back = self.prev
        back.next = Node(val)
        back.next.prev = back
        back.next.next = self
        self.prev = back.next


def doubly_linked_list_to_binary_tree(ll):
    if ll.next == ll:
        ll.prev = None
        ll.next = None
        return ll

    start, end = ll, ll.prev
    while start != end:
        start = start.next
        if start != end:
            end = end.prev

    center = start
    start, end = ll, ll.prev

    left_end = center.prev
    left_end.next = start
    start.prev = left_end

    center.prev = doubly_linked_list_to_binary_tree(start)

    if center != end:
        right_start = center.next
        right_start.prev = end
        end.next = right_start

        center.next = doubly_linked_list_to_binary_tree(right_start)

    else:
        center.next = None

    return center


def print_ll(ll):

    start, end = ll, ll.prev

    current = start
    while current != end:
        print(current.val, end=" ")
        current = current.next

    print(end.val)


def print_bt(root, indent=""):
    if root is None:
        return

    print_bt(root.prev, indent + "    ")
    print(indent, root.val)
    print_bt(root.next, indent + "    ")


if __name__ == "__main__":

    vals = sorted(np.random.randint(0, 20, size=10))
    ll = None
    for val in vals:
        if ll is None:
            ll = Node(val)
        else:
            ll.emplace_back(val)

    print(vals)
    print_ll(ll)

    root = doubly_linked_list_to_binary_tree(ll)
    print_bt(root)
