import numpy as np

def matmul_order(dims):
    '''
    Input:  Dimensions of n rectangular matrices
    Output: Min-cost parenthesizationfor multiplying n matrices 
            with the given dimensions where given A, B, cost(A*B)=pqr
    
    Note:  There are Ω(4^n/n^1.5) different parethesizations
    '''
    n = len(dims)-1
    
    S = np.zeros((n, n))
    B = np.zeros((n, n), dtype=int)

    for i in range(n-1, -1, -1):
        for j in range(i, n):

            if (i == j):
                B[i][j] = i

            elif (i+1 == j):
                S[i][j] = dims[i]*dims[i+1]*dims[i+2]
                
                B[i][j] = i

            else:
                min_i_j = np.inf

                for k in range(i, j-1):
                    new_min = S[i][k] + S[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
                    if (new_min < min_i_j):
                        min_i_j = new_min
                        B[i][j] = k
                        
                S[i][j] = min_i_j
    
    def backtrace(i, j):
        objects = []
        if (i+1 < j):
            objects.append(B[i][j])
            objects.extend(backtrace(B[i][j]+1, j))
            objects.extend(backtrace(i, B[i][j]))

        return objects


    return backtrace(0, n-1), S[0][n-1]
    
    
def assert_equals(sol, opt):
    if any(x != y for x, y in zip(sol[0], opt[0])) or sol[1] != opt[1]:
        print(sol, "!=", opt)
        exit(1)


if __name__ == "__main__":
    assert_equals(matmul_order([100, 5, 20, 10]),
                  ((0,), 6000))
    print("All Matrix Multiplication Order Tests Passed!")
    