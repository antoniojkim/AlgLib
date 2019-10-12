
import numpy as np

import sys
sys.path.append("../")
sys.path.append("../Topological Sort")

from graphs import create_graph
from topsort import topsort

def verify_alien_language(sorted_words, alphabet):
    


def derive_alien_language(sorted_words):
    '''
    Given a list of words, derive the order
    of the alphabet that would classify the
    list of words as "lexicographically"
    sorted.
    '''
    
    vertices = set()
    for word in sorted_words:
        vertices |= set(list(word))
        
    edges = set()
    for w1, w2 in zip(sorted_words, sorted_words[1:]):
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                edges.add((l1, l2))
                break
        
    G = create_graph(list(vertices), list(edges))
    
    return topsort(G)
    

def assert_test(actual, expected):
    if actual != expected:
        raise Exception(f"{actual} != {expected}")
    
    
if __name__ == "__main__":
    
    assert_test(derive_alien_language([
        "baa", "abcd", "abca", "cab", "cad"
    ]), ['b', 'd', 'a', 'c'])
    
    assert_test(derive_alien_language([
        "caa", "aaa", "aab"
    ]), ['c', 'a', 'b'])
