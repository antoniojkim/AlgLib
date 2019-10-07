
import numpy as np

def quickselect(N, k):
    '''
    Find the kth smallest element in N

    Parameters
    ----------
    N: list[int]
    k: int
    '''
    def swap(i, j):
        nonlocal N
        N[i], N[j] = N[j], N[i]

    def partition(left, right, pivot_index):
        pivot = N[pivot_index]
        swap(pivot_index, right)
        store_index = left
        for i in range(left, right):
            if N[i] < pivot:
                swap(store_index, i)
                store_index += 1

        swap(right, store_index)
        return store_index

    def select(left, right, k):
        while True:
            if left == right:
                return N[left]

            pivot_index = left + np.random.randint(right - left + 1)

            pivot_index = partition(left, right, pivot_index)

            if k == pivot_index:
                return N[k]
            elif k < pivot_index:
                right = pivot_index - 1
            else:
                left = pivot_index + 1

    return select(0, len(N)-1, k)


if __name__ == "__main__":
    for i in range(100):
        N = np.random.randint(-100, 100, size=35)
        n = np.random.randint(35)
        kth = quickselect(N, n)
        assert(kth == sorted(N)[n])

