import sys
sys.path.append("../../")
sys.path.append("../../Topological Sort")

import numpy as np
from graphs import create_graph
from topsort import topsort

def sssp_dag(G, s):
    f = topsort(G)
    SD = {v:(0 if v == s else np.inf) for v in f}
    paths = {v:[] for v in f}
#     paths[s].append(s)
    
    for v in f:
        curpath = []
        for u in G.get_in_edges(v):
            tmp = SD[u]+G.get_weight(u, v)
            if (tmp < SD[v]):
                SD[v] = tmp
                curpath = paths[u]
                
        paths[v].extend(curpath)
        paths[v].append(v)
    
    return paths
    
    
def test_sssp_dag(result, expected):
    for k in expected:
        if (set(result[k]) != set(expected[k])):
            print(result)
            print(expected)
            raise Exception(f"{k}:  {result[k]} != {expected[k]}")


if __name__ == "__main__":
    test_sssp_dag(sssp_dag(create_graph(
        ["s", "a", "b", "c", "d", "e", "f", "t"],
        [("s", "a", 9),
         ("s", "b", 4),
         ("a", "c", 1),
         ("a", "d", -3),
         ("b", "c", 2),
         ("b", "d", 3),
         ("b", "e", 2),
         ("c", "e", 2),
         ("c", "f", -4),
         ("d", "e", 1),
         ("d", "f", 2),
         ("e", "t", 5),
         ("f", "t", 3)],
        track_in = True
    ), "s"), {
        "a": ("s", "a"),
        "b": ("s", "b"),
        "c": ("s", "b", "c"),
        "d": ("s", "a", "d"),
        "e": ("s", "b", "e"),
        "f": ("s", "b", "c", "f"),
        "t": ("s", "b", "c", "f", "t")
    })
    
    print("All Single Source Shortest Paths for DAG Tests Passed!")