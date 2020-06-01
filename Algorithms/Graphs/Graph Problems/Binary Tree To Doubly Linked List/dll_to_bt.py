# -*- coding: utf-8 -*-


class DoublyLinkedList:
    def __init__(self, val):
        self.val = val
        self.prev = self
        self.next = self

    def emplace_back(self, val):
        back = self.prev
        back.next = DoublyLinkedList(val)
        back.next.prev = back
        back.next.next = self
        self.prev = back.next

    def __iter__(self):
        current, end = self, self.prev
        while current != end:
            yield current.val
            current = current.next

        if current is not None:
            yield current.val


def doubly_linked_list_to_binary_tree(ll: DoublyLinkedList):
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
