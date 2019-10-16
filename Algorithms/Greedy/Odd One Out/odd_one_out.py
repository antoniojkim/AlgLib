
import numpy as np
from random import shuffle


def odd_one_out(A):
    '''
    Given a list of integers where every single
    element repeats an even number of times except
    for one element who repeats an odd number of times.
    The following algorithm finds the element that
    repeats an odd number of times.
    '''
    n = 0
    for a in A:
        n ^= a
        
    return n




if __name__ == "__main__":
    for i in range(100):
        A = []
        n = np.random.randint(3, 10)
        for j in range(n):
            a = np.random.randint(0, 100)
            A.extend((a for _ in range(
                np.random.randint(1, 5) * 2
            )))
            
        odd = np.random.randint(0, 100)
        while odd in A:
            odd = np.random.randint(0, 100)
            
        A.extend((odd for _ in range(
            np.random.randint(0, 5) * 2 + 1
        )))
        
        shuffle(A)
        
        assert(odd_one_out(A) == odd)