# [Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)

## Problem

Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

* `push(x: int)`, which pushes an integer x onto the stack.
* `pop()`, which removes and returns the most frequent element in the stack. If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.

### Example

```python
fs = FreqStack()
for i in [5, 7, 5, 7, 4, 5]:
    fs.push(i)
```

At this point, the stack is `[5, 7, 5, 7, 4, 5]` from bottom to top.

`pop()` -> returns 5, as 5 is the most frequent.
The stack becomes `[5, 7, 5, 7, 4]`.

`pop()` -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes `[5, 7, 5, 4]`.

`pop()` -> returns 5.
The stack becomes `[5, 7, 4]`.

`pop()` -> returns 4.
The stack becomes `[5, 7]`.

## Solution

The main idea is that we need to create a max heap. The problem with a simple max heap is that items cannot efficiently be updated in a heap. However, the key realization is that we do not actually need to update items. We just add items with the updated counts and the heap will take care of order for us.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Greedy/Maximum%20Frequency%20Stack/max_freq_stack.py#L5)

```python
class FreqStack:
    def __init__(self):
        self.counts = {}
        self.heap = []
        self.n = 0

    def push(self, x: int) -> None:
        self.n += 1
        self.counts[x] = self.counts.get(x, 0) + 1
        heappush(self.heap, (-self.counts[x], -self.n, x))

    def pop(self) -> int:
        count, index, val = heappop(self.heap)
        self.counts[val] -= 1
        return val
```

### Runtime

`O(n log(n))`
