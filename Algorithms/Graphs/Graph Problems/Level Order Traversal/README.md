# Level Order Traversal

## Problem

Given a binary tree return the level order traversal, i.e. elements in the first level, then second, then third, etc.

### Example

The level order traversal of the following binary tree

```
        10
      /    \
    3       20
  /       /    \
2       15      24
```

is

```python
[[10], [3, 20], [2, 15, 24]]
```


## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Level%20Order%20Traversal/level_order_traversal.py#L12)

Here is an fairly efficient implementation of the algorithm using a modified BFS:

```python
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
```

### Runtime

Total: `O(n)`
