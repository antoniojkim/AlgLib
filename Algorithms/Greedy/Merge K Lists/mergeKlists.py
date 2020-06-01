# -*- coding: utf-8 -*-
from heapq import heappush, heappop
from typing import List


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
