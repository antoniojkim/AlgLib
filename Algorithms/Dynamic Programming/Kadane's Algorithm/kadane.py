import numpy as np

def kadane(A):
    B = np.zeros(len(A))
    B[0] = A[0]
    msub = B[0]
    for j in range(1, len(B)):
        B[j] = max(A[j], B[j-1]+A[j])
        msub = max(msub, B[j])
        
    return msub


def test_kadane(result, expected):
    if (result != expected):
        raise Exception(f"{result} != {expected}")
    
    
if __name__ == "__main__":
    test_kadane(kadane(
        [1, -2, 3, -4, 5, 6, 7, -8, 9, -10]
    ), 19)
    print("All Kadane's Algorithm Tests Passed!")
