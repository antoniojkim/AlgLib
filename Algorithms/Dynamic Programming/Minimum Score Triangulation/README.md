# [Minimum Score Triangulation of a Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/)

## Problem

Given `N`, consider a convex `N`-sided polygon with vertices labelled `A[0], A[i], ..., A[N-1]` in clockwise order.

Suppose you triangulate the polygon into `N-2` triangles.  For each triangle, the value of that triangle is the product of the labels of the vertices, and the total score of the triangulation is the sum of these values over all `N-2` triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

### Examples

```
Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.

Input: [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
```

## Solution

We can construct a dynamic programming solution for this problem. Notice that anytime we are computing the score of a particular triangulation, it is the minimum of the current best triangulation and the new traingulation plus the minimum scores for the two sub triangulations.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Dynamic%20Programming/Minimum%20Score%20Triangulation/min_score_triangulation.py#L8)

```python
def min_score_triangulation(A: List[int]) -> int:
    S = zeros((len(A), len(A)))  # Min score solution matrix
    for i in range(2, len(A)):
        for j in range(len(A) - i):
            S[j, j + i] = inf
            for k in range(j + 1, j + i):
                S[j, j + i] = min(
                    S[j, j + i], A[j] * A[k] * A[j + i] + S[j, k] + S[k, j + i]
                )

    return S[0, -1]
```

### Runtime

`O(n^3)`
