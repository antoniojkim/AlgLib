# Shamos's Algorithm

Given a set of points (at least two) on a cartesian plane, find the two points have the smallest Euclidean distance:

```
dist(p, q) = √((p.x−q.x)^2+(p.y−q.y)^2)
```

## Algorithm

### Naive Algorithm

The naive solution here would be to compute the euclidean distance between all pairs of points and choose the ones with the minimum distance. However, this has a runtime of `O(n^2)`. We can improve upon this using a divide and conquer algorithm.

### Shamos's Algorithm

Shamos's algorithm revolves around the idea of separating the cartesian plane into two parts and solving the closest pair problem in those two subplanes and then checking if there could exist any closer pairs between the two of them.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Divide%20and%20Conquer/Shamos's%20Algorithm/shamos.py#L11)

Here is an implementation:

```python
def shamos(P: List[Tuple[int, int]]) -> Tuple[Tuple[int, int], float]:\
    def findMinSpanningPair(Px, Py, delta):
        m = Px[len(Px) // 2]  # median point
        S = [p for p in Py if abs(m[0] - p[0]) <= delta]

        minPair = None
        minDist = inf

        for i in range(len(S)):
            for j in range(i + 1, len(S)):
                if S[j][1] < S[i][1] + delta:
                    dist = euclidean_dist(S[j], S[i])
                    if dist < minDist:
                        minDist = dist
                        minPair = (S[j], S[i])

        return minPair, minDist

    def shamos_closest_pair(Px, Py):
        if len(Px) == 2:
            return Px, euclidean_dist(Px[0], Px[1])
        if len(Px) == 3:
            return min(
                (
                    ((Px[0], Px[1]), euclidean_dist(Px[0], Px[1])),
                    ((Px[1], Px[2]), euclidean_dist(Px[1], Px[2])),
                    ((Px[0], Px[2]), euclidean_dist(Px[0], Px[2])),
                ),
                key=lambda x: x[1],
            )

        m = Px[len(Px) // 2]  # median point
        Pyl = [p for p in Py if p[0] <= m[0]]
        Pyr = [p for p in Py if p[0] > m[0]]

        pairL, distL = shamos_closest_pair(Px[: len(Px) // 2], Pyl)
        pairR, distR = shamos_closest_pair(Px[len(Px) // 2 :], Pyr)

        delta = min(distL, distR)

        pairS, distS = findMinSpanningPair(Px, Py, delta)

        return min(((pairL, distL), (pairR, distR), (pairS, distS)), key=lambda x: x[1])

    Px = sorted(P, key=lambda p: p[0])
    Py = sorted(P, key=lambda p: p[1])
    return shamos_closest_pair(Px, Py)
```

### Runtime

Total: `O(nlog⁡n)`
