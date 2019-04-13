import sys
sys.path.append("../../")

import numpy as np
from graphs import create_graph


def floyd_warshall(G):
    V = list(G.get_vertices())
    n = len(V)
    A = {u:{v:[np.inf for _ in range(n)] for v in V} for u in V}
    
    for i in V:
        A[i][i][0] = 0
    for i, j in G.get_edges():
        A[i][j][0] = G.get_weight(i, j)
    
    
    
    for k in range(1, n):
        for i in G.get_vertices():
            for j in G.get_vertices():
                A[i][j][k] = min(A[i][j][k-1],
                                 A[i][V[k]][k-1] + A[V[k]][j][k-1])
    
    return {i:{j:A[i][j][-1] for j in V if i != j} for i in V}


def test_floyd_warshall(result, expected):
    for i in expected:
        if i not in result:
            raise Exception(f"{i} not in result")
        for j in expected[i]:
            if j not in result[i]:
                raise Exception(f"{j} not in result[{i}]")
                
            if expected[i][j] != result[i][j]:
                raise Exception(f"({i}, {j}):   {expected[i][j]} != result[{result[i][j]}]")
            


if __name__ == "__main__":
    test_floyd_warshall(
        floyd_warshall(create_graph(
            ["1", "2", "3", "4", "6", "7"],
            [
                ("1", "4", 1),
                ("2", "1", 1),
                ("2", "3", -1),
                ("2", "6", 2),
                ("2", "7", 5),
                ("3", "6", 1),
                ("6", "7", 0),
                ("7", "4", 2)
            ]
        )),
        {'1': {'2': np.inf, '3': np.inf, '4': 1, '6': np.inf, '7': np.inf}, 
         '2': {'1': 1, '3': -1, '4': 2, '6': 0, '7': 0}, 
         '3': {'1': np.inf, '2': np.inf, '4': 3, '6': 1, '7': 1}, 
         '4': {'1': np.inf, '2': np.inf, '3': np.inf, '6': np.inf, '7': np.inf}, 
         '6': {'1': np.inf, '2': np.inf, '3': np.inf, '4': 2, '7': 0}, 
         '7': {'1': np.inf, '2': np.inf, '3': np.inf, '4': 2, '6': np.inf}}
    )
    print("All Floyd-Warshall Tests Passed!")
