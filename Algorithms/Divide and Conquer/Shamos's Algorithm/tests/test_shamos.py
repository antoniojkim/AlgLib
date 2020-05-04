# -*- coding: utf-8 -*-

import os
import sys

import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from shamos import euclidean_dist, shamos


def naive_closest_pair(P):
    minPair = None
    minDist = np.inf
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            dist = euclidean_dist(P[i], P[j])
            if dist < minDist:
                minDist = dist
                minPair = (P[i], P[j])

    return minPair, minDist


def test_shamos():
    for i in range(100):
        P = np.random.randint(-50, 50, size=(np.random.randint(15, 20), 2)).tolist()
        P = list(map(tuple, P))

        assert shamos(P)[1] == naive_closest_pair(P)[1]
