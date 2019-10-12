
import sys
sys.path.append("../")
sys.path.append("../Topological Sort")

from string import ascii_lowercase
import numpy as np

from graphs import create_graph
from topsort import topsort

def verify_alien_language(sorted_words, alphabet):
    alphabet = {l: i for i, l in enumerate(alphabet)}
    
    for w1, w2 in zip(sorted_words, sorted_words[1:]):
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                if alphabet[l1] > alphabet[l2]:
                    return False
                
                break
                
        else:
            if len(w1) > len(w2):
                return False
                
    return True


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
        
    edges = []
    for w1, w2 in zip(sorted_words, sorted_words[1:]):
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                edges.append((l1, l2))
                break
        
    G = create_graph(list(vertices), list(edges))
    
    return topsort(G)
    

def assert_test(actual, expected):
    if actual != expected:
        raise Exception(f"{actual} != {expected}")
        
        
def verify_test(words):
    alphabet = derive_alien_language(words)
    if not verify_alien_language(words, alphabet):
        print(words)
        print(alphabet)
        raise Exception(f"Alphabet is incorrect")
        
    
    
    
if __name__ == "__main__":
    
    assert_test(derive_alien_language([
        "baa", "abcd", "abca", "cab", "cad"
    ]), ['b', 'd', 'a', 'c'])
    
    assert_test(derive_alien_language([
        "caa", "aaa", "aab"
    ]), ['c', 'a', 'b'])
    
    assert_test(derive_alien_language([
        "wrt", "wrf", "er", "ett", "rftt"
    ]), ["w", "e", "r", "t", "f"])
    
    verify_test(["baa", "abcd", "abca", "cab", "cad"])
    verify_test(["caa", "aaa", "aab"])
    verify_test(["wrt", "wrf", "er", "ett", "rftt"])
