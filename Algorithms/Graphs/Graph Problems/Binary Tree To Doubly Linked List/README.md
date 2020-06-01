# Binary Tree to Doubly Linked List

## Problem

Given a binary tree, *efficiently* convert it into a doubly linked list.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Graph%20Problems/Binary%20Tree%20To%20Doubly%20Linked%20List/bt_to_dll.py#L11)

Here is an implementation that performs the conversion in-place:

```python
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
```

### Runtime

Total: `O(n)` as all nodes must be visited once.

# Doubly Linked List to Binary Tree

## Problem

Given a sorted doubly linked list, *efficiently* convert it into a binary tree.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Graph%20Problems/Binary%20Tree%20To%20Doubly%20Linked%20List/dll_to_bt.py#L26)

Here is an implementation that performs the conversion in-place:

```python
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
```

### Runtime

Total: `O(n)` as all nodes must be visited once.
