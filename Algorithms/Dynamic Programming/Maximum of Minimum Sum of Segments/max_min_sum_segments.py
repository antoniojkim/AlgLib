
import numpy as np
import itertools

def naive_max_min_sum_segments(A, k):
    max_sum = -np.inf

    for ts in list(itertools.combinations(range(1, len(A)), k-1)):
        ts = sorted([0]+list(ts)+[len(A)])
        chunk_sum = min(sum(A[ts[i-1]:ts[i]]) for i in range(1, len(ts)))
        if (chunk_sum > max_sum):
            max_sum = chunk_sum
        
    return max_sum


def max_min_sum_segments(A, k):
    '''
    Split an array of integers A into k segments
    such that the minimum of the sums of the
    segments is maximized. Return the maximum
    value.

    Parameters
    ----------
    A: list[int]
    k: int

    Returns
    -------
    int
    '''

    def split(min_sum):
        count = 0
        segment_sum = 0
        for a in A:
            segment_sum += a
            if segment_sum >= min_sum:
                count += 1
                segment_sum = 0

        return count

    l = min(A)
    h = sum(A)

    while l < h:
        min_sum = (l + h + 1) // 2
        if split(min_sum) < k:
            h = min_sum - 1
        else:
            l = min_sum

    return l



if __name__ == "__main__":
    
    assert(naive_max_min_sum_segments([6, 3, 2, 8, 7, 5], 3) == 9)
    assert(max_min_sum_segments([6, 3, 2, 8, 7, 5], 3) == 9)

    assert(naive_max_min_sum_segments([5, 7, 4, 2, 8, 1, 6], 3) == 7)
    assert(max_min_sum_segments([5, 7, 4, 2, 8, 1, 6], 3) == 7)
    
    assert(naive_max_min_sum_segments([6, 5, 3, 8, 9, 10, 4, 7, 10], 4) == 14)
    assert(max_min_sum_segments([6, 5, 3, 8, 9, 10, 4, 7, 10], 4) == 14)

    for i in range(100):
        A = np.random.randint(0, 100, size=15)
        k = np.random.randint(2, 10)
        assert(max_min_sum_segments(A, k) == naive_max_min_sum_segments(A, k))

