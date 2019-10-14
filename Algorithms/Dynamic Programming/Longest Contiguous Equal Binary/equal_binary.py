
import numpy as np


def naive_equal_binary(arr):
    max_len = 0

    for i in range(len(arr)+1):
        for j in range(i):
            if (i-j)%2 == 0:
                sum_01 = sum(arr[j:i])
                if sum_01 == (i-j)//2 and (i-j) > max_len:
                    max_len = (i-j)
        
    return max_len


def equal_binary(arr):
    '''
    Given a binary array(array only containing 0 and 1),
    find the maximum length of a contiguous subarray
    where the number of 0’s is equal to the number of 1’s.
    '''
    n = len(arr)
    
    max_len = 0
    running_total = 0
    for i in range(n):
        running_total += arr[i]
        current_total = running_total
            
        for j in range(i+1):
            if (i-j+1)%2 == 0 and current_total == (i-j+1)//2 and (i-j+1) > max_len:
                max_len = (i-j+1)
            
            current_total -= arr[j]

    return max_len
    
if __name__ == "__main__":
    
    assert(naive_equal_binary([0, 1]) == 2)
    assert(naive_equal_binary([0,1,0,0,0,1,1]) == 6)
    
    assert(equal_binary([0, 1]) == 2)
    assert(equal_binary([0,1,0,0,0,1,1]) == 6)
    
    for i in range(100):
        arr = np.random.randint(2, size=i)
        assert(naive_equal_binary(arr) == equal_binary(arr))
