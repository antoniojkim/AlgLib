import sys
sys.path.append("../")

from graphs import create_graph

import numpy as np

def kruskal(G):
    '''
    G is a weight undirected graph
    '''    
    parent = {v:v for v in G.get_vertices()}
    rank = {v:0 for v in G.get_vertices()}
    
    def find(x):
        nonlocal parent
        
        if (parent[x] == x):
            return x
        
        return find(parent[x])
    
    def union(u, v):
        uroot = find(u)
        vroot = find(v)
        
        if (rank[uroot] < rank[vroot]):
            parent[uroot] = yroot
        
        elif(rank[uroot] > rank[vroot]):
            parent[vroot] = uroot
            
        else:
            parent[vroot] = uroot
            rank[uroot] += 1
    
    E = sorted(list(G.get_edges()), key=lambda x: G.get_weight(x[0], x[1]))
    T = []
    for u, v in E:
        if find(u) != find(v):  # T union (u, v) does not create a cycle
            T.append((u, v))
            union(u, v)
        
    return T #list(G.get_edges())


def test_kruskal(G, expected):
    mst = kruskal(G)

    mst_cost = 0
    visited = {v:False for v in G.get_vertices()}
    for u, v in mst:
        visited[u] = True
        visited[v] = True
        mst_cost += G.get_weight(u, v)
    if any(v == False for v in visited):
        raise Exception(f"Tkrus is not spanning:  {mst}")
        
    visited = {v:False for v in visited}
    expt_cost = 0
    for u, v in expected:
        visited[u] = True
        visited[v] = True
        expt_cost += G.get_weight(u, v)
    if any(v == False for v in visited):
        raise Exception(f"Expected is not spanning:  {mst}")
        
    if (mst_cost != expt_cost):
        raise Exception(f"{mst_cost} != {expt_cost}")


if __name__ == "__main__":
    test_kruskal(create_graph(
        ["A", "B", "C", "D", "E", "F", "G", "H"],
        [("A", "B", 4),
         ("A", "C", 6),
         ("A", "D", 1),
         ("B", "C", 8),
         ("C", "D", 5),
         ("C", "F", 2.5),
         ("C", "H", 7),
         ("D", "E", 2),
         ("E", "F", 3),
         ("F", "G", 7.5),
         ("G", "H", 9)],
        directed=False
    ), [
        ("A", "B"),
        ("A", "D"),
        ("D", "E"),
        ("E", "F"),
        ("C", "F"),
        ("C", "H"),
        ("F", "G")
    ])
    
    print("All Kruskal's Algorithm Tests Passed!")
