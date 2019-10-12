
import numpy as np
import itertools

def naive_split_array(A, k):
    min_sum = np.inf

    for ts in itertools.combinations(range(1, len(A)), k-1):
        ts = sorted([0]+list(ts)+[len(A)])
        max_sum = max(sum(A[ts[i-1]:ts[i]]) for i in range(1, len(ts)))
        if (max_sum < min_sum):
            min_sum = max_sum
        
    return min_sum


def split_array(nums, m):
    '''
    Given an array which consists of non-negative integers and an integer m,
    split the array into m non-empty continuous subarrays. The following algorithm
    minimizes the largest sum among these m subarrays.
    '''
        
    def split(max_sum):

        count = 0
        num_sum = 0
        for i, n in enumerate(nums):

            if num_sum+n < max_sum:
                num_sum += n
                
            else:
                count += 1
                num_sum = n
                
        return count
    
    l = max(nums)
    h = sum(nums)

    i = 0
    while h-l > 1:
        max_sum = (l + h + 1) // 2

        count = split(max_sum)
        if count < m:
            h = max_sum

        else:
            l = max_sum + 1

        i += 1
        if i > 9995:
            print(l, h)
            if i > 10000:
                raise Exception("Took too long")

    return h - 1


def assert_test(nums, m):
    naive_max_sum = naive_split_array(nums, m)
    max_sum = split_array(nums, m)
    if naive_max_sum != max_sum:
        print(nums)
        print(m)
        print(naive_max_sum, "!=", max_sum, "\n")
        raise Exception("max_sums do not match")


if __name__ == "__main__":
    assert_test([7, 2, 5, 10, 8], 2)
    assert_test([1, 7, 3, 8, 4, 4, 5], 3)

    for i in range(100):
        nums = np.random.randint(0, 100, size=np.random.randint(10, 15))
        m = np.random.randint(3, len(nums)-1)

        assert_test(nums, m)

