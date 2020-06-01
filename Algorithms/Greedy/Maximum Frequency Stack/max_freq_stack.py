# -*- coding: utf-8 -*-
from heapq import heappush, heappop


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
