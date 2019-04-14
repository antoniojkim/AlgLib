import numpy as np

def lis(V):
    A = np.zeros(len(V)+1, dtype=int)
    S = [[] for _ in range(len(A))]
    A[0] = 0
    A[1] = V[0][1]
    S[1].append(V[0][0])
    
    for i in range(2, len(A)):
        if (A[i-1] <= A[i-2]+V[i-1][1]):
            A[i] = A[i-2]+V[i-1][1]
            S[i] = S[i-2]+[V[i-1][0]]
        else:
            A[i] = A[i-1]
            S[i] = S[i-1]
        
    return A[-1], S[-1]


def test_lis(result, expected):
    if (result[0] != expected[0]):
        raise Exception(f"{result[0]} != {expected[0]}")
        
    if (set(result[1]) != set(expected[1])):
        raise Exception(f"{result[1]} != {expected[1]}")

if __name__ == "__main__":
    test_lis(lis(
        [("A", 1),
         ("B", 5),
         ("C", 6),
         ("D", 3)]
    ),
    (8, ("B", "D")))
    
    print("All Linear Independent Set Tests Passed!")


