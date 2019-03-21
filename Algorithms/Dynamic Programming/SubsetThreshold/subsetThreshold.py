
import numpy as np
import itertools

from collections import Counter

def subsetThreshold_naive(a, n, m):
    asum = sum(a)
    for S in itertools.combinations(a, n//2):
        l = sum(S)
        if (l > n*m//4 and asum-l > n*m//4):
            return True, list(S), list((Counter(a)-Counter(S)).elements())
        
    return False, [], []

def subsetThreshold_dp(a, n, m):
    C = np.zeros((n+1, n+1, n*m), dtype=np.bool)

    for i in range(1, n+1):
        if (a[i-1] < n*m):
            C[i][1][a[i-1]] = 1                
            for j in range(1, i+1):
                for l in range(1, n*m):
                    if (i > 1 and C[i-1][j][l]):
                        C[i][j][l] = 1

                    if (C[i-1][j-1][l-a[i-1]]):
                        C[i][j][l] = 1

    S_exists = False
    S = []
    i = n
    j = n//2
    asum = sum(a)
    for l in range(n*m//4+1, n*m):
        if (C[i][j][l] == 1 and asum-l > n*m//4):
            S_exists = True
            while (i >= 0 and j >= 0 and l > 0):
                if (C[i-1][j][l] == 0):
                    S.append(a[i-1])
                    l -= a[i-1]
                    j -= 1
                
                i -= 1
                
            break
        
    return S_exists, S, list((Counter(a)-Counter(S)).elements())
    
    
def test(a, n, m):
    s1 = subsetThreshold_naive(a, n, m)
    s2 = subsetThreshold_dp(a, n, m)
    if(s1[0] != s2[0]):
        print(a, n, m)
        print(s1, s2)
        raise Exception(f"{s1[0]} != {s2[0]}")
    if (s1[0] == True):
        if(sum(s1[1]) <= n*m//4 or sum(s1[2]) <= n*m//4):
            print(a, n, m)
            print(s1, sum(s1[1]), sum(s1[2]), n*m//4)
            print(s2, sum(s2[1]), sum(s2[2]), n*m//4)
            raise Exception(f"s1 doesn't meet criteria")
        if(sum(s2[1]) <= n*m//4 or sum(s2[2]) <= n*m//4):
            print(a, n, m)
            print(s1, sum(s1[1]), sum(s1[2]), n*m//4)
            print(s2, sum(s2[1]), sum(s2[2]), n*m//4)
            raise Exception(f"s2 doesn't meet criteria")
        
        return 1
    
    return 0

    
if __name__ == "__main__":
    count = 0
    for _ in range(1000):
        n = np.random.randint(1, 5)*2
        a = np.random.randint(100, 200, size=n)
        m = np.random.randint(50, 200)
        m = max(m*n,
                max(a)+1)
        count += test(a, n, m)
        
    print(f"All Tests Passed!  Tested {count} cases where solutions were found")
    