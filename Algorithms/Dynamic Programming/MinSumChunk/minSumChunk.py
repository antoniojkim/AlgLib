
import numpy as np
import itertools

def minSumChunk_naive(a, t):
    min_sum = np.inf
    for ts in list(itertools.combinations(range(1, len(a)), t-1)):
        ts = sorted([0]+list(ts)+[len(a)])
        chunk_sum = sum(sum(a[ts[i-1]:ts[i]])**2 for i in range(1, len(ts)))
        if (chunk_sum < min_sum):
            min_sum = chunk_sum
        
    return min_sum

def minSumChunk_dp(a, t):
    n = len(a)
    A = np.zeros((n, n), dtype=np.int)
    T = np.zeros((n, t), dtype=np.int)
    
    for i in range(n):
        A[i][i] = a[i]**2
        for j in range(i+1, n):
            A[i][j] = (np.sqrt(A[i][j-1])+a[j])**2
    
    for i in range(n):
        T[i][0] = A[0][i]
        
        for j in range(1, min(i+1, t)):       
            T[i][j] = min(T[k][j-1]+A[k+1][i] for k in range(j-1, i))
                
    return T[n-1][t-1]


def test(a, t):
    s1 = minSumChunk_dp(a, t)
    s2 = minSumChunk_naive(a, t)
    if (s1 != s2):
        raise Exception(f"{s1} {s2} {a} {t}")


if __name__ == "__main__":
    for _ in range(1000):
        r = np.random.randint(6, 15)
        a = np.random.randint(100, size=r)
        t = np.random.randint(1, r)
        test(a, t)
            
    print("All Tests Passed!")