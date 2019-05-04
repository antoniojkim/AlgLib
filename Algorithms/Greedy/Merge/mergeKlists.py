
import numpy as np
from heapq import heappush, heappop

def mergeKLists(lists):
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


def assert_equals(result, expected):
    if len(result) != len(expected):
        raise Exception(f"len(result) = {len(result)} != {len(expected)} = len(expected)")
        
    if any(r != e for r, e in zip(result, expected)):
        raise Exception(f"{results} != {expected}")
    


if __name__ == "__main__":
    for i in range(1000):
        lists = [sorted(np.random.randint(100, size=np.random.randint(5, 20))) for i in range(np.random.randint(2, 10))]
        expected = sorted(sum(lists, []))
        result = mergeKLists(lists)
        assert_equals(result, expected)
        
    print("All Merge K Lists Tests passed!")