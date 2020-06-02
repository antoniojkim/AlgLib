# [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/)

## Problem

Given `n` points on a 2D plane, find the maximum number of points that lie on the same straight line.

### Examples

```
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
```

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Greedy/Max%20Points%20on%20a%20Line/max_points_on_line.py#L7)

Greedy solution

```python
def maxPoints(points: List[List[int]]) -> int:
    if len(points) <= 2:
        return len(points)

    max_num_points = 1
    for i in range(len(points)):
        duplicates = 0
        counts = {0: 0}
        x1 = points[i][0]
        y1 = points[i][1]
        for j in range(i+1, len(points)):
            x2 = points[j][0]
            y2 = points[j][1]
            m = (y2-y1, x2-x1)
            if m[0] == 0 and m[1] == 0:
                duplicates += 1
                continue
            elif m[0] == 0:
                m = (0, 1)
            elif m[1] == 0:
                m = (1, 0)
            else:
                g = gcd(*m)
                m = (m[0] // g, m[1] // g)
                if m[1] < 0:
                    m = (-m[0], -m[1])

            b = y1*m[1] - m[0]*x1
            counts[(m, b)] = counts.get((m, b), 0) + 1

        max_num_points = max(max_num_points, duplicates + max(counts.values()) + 1)

    return max_num_points
```

### Runtime

`O(n^2)`
