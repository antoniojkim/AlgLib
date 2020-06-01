# Alien Dictionary

## Problem Description

Suppose you are given a list of words (consisting of only the letters a-z). What is the alphabet that would classify the list of words as "lexicographically" sorted?

## Solution

The solution here is to create a directed acyclic graph (DAG) where the vertices are the letters of the alphabet. From here, we traverse the list of sorted words that we are given and find the letter where adjacent words deviate. We then add a directed edge between these two letters.

Using this graph, performing a [topological sort](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Topological%20Sort/) would give us the alphabet that would classify the list of words as "lexicographically" sorted.

### [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Graphs/Alien%20Dictionary/alien_dictionary.py#L11)

Here is a simple implementation of the above solution:

```python
def derive_alien_language(sorted_words: List[str]) -> List[str]:
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
```
