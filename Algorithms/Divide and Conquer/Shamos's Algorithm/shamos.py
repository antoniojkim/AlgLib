# -*- coding: utf-8 -*-
from typing import List
from typing import Tuple

from numpy import inf, sqrt


def euclidean_dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def shamos(P: List[Tuple[int, int]]) -> Tuple[Tuple[int, int], float]:
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
