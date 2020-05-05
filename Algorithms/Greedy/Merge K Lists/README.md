# Merge `K` Lists

## Problem

Given `K` sorted lists, merge them into a single sorted list.

## Algorithm

### Naive Solution

Simply concatenate the lists and re-sort them. However, this solution is `O(nK log(nK))`.

### Better Solution

We can exploit the fact that the lists are already sorted to create a better solution.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Greedy/Merge%20K%20Lists/mergeKlists.py#L6)

Here is an implementation using a min-heap to keep track of the smallest value amongst all of the lists:

```python
def mergeKLists(lists: List[List[int]]) -> List[int]:
    merged = []

    heap = []
    for i, l in enumerate(lists):
        if len(l) > 0:
            heappush(heap, (l.pop(0), i))

    while len(heap) > 0:
        val, i = heappop(heap)
        merged.append(val)

        if len(lists[i]) > 0:
            heappush(heap, (lists[i].pop(0), i))

    return merged
```

### Runtime

Total: `O(nK logK)`
