# Maximum Subarray Problem

In the maximum subarray problem, we are given as input an array $A[1],\dots,A[n]$ of $n$ integers. Our goal is to find the maximum value of any subarray of $A$. I.e., the valid solution is the value

$$
\max_{i,j:1\le i\le j\le n}\sum_{l=i}^{j}A[l]
$$

Let $B$ be a solution array such that $B[j]$ is the maximum subarray that ends at $A[j-1]$, i.e.
$$
B[j] = \max_{i,j:1\le i\le j}\sum_{l=i}^{j}A[l]
$$

The key observation is that there are only two possibilities to consider for $B[j]$: either it includes the maximum subarray that ends at $A[j−1]$ (along with $A[j]$), or it does not (in which case $B[j] = A[j]$).

## Runtime

Overall, the algorithm makes one pass through the solution array of length $n$. So, the runtime is $O(n)$
