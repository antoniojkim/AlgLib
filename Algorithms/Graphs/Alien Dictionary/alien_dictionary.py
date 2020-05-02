# -*- coding: utf-8 -*-
import os
import sys
from typing import List

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))
sys.path.append(os.path.join(file_dir, "../Topological Sort"))

from graphs import create_graph
from topsort import topsort


def derive_alien_language(sorted_words: List[str]) -> List[str]:
    """
    Given a list of words, derive the order
    of the alphabet that would classify the
    list of words as "lexicographically"
    sorted.
    """

    vertices = set()
    for word in sorted_words:
        vertices |= set(list(word))

    edges = []
    for w1, w2 in zip(sorted_words, sorted_words[1:]):
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                edges.append((l1, l2))
                break

    G = create_graph(list(vertices), list(edges))

    return topsort(G)
