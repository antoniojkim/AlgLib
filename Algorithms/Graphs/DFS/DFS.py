
import sys
sys.path.append("../")

from graphs import create_graph

def DFS(G, u, v):
    '''
    Check if there exists a path from u to v
    '''
    assert(u in G and v in G)

    if (u == v):
        return True

    
    for n in G[u]:
        if (DFS(G, n, v)):
            return True

    return False

if __name__ == "__main__":
    G = create_graph(["A", "B", "C"], [("A", "B"), ("B", "C")])
    assert(DFS(G, "A", "C") == True)
    assert(DFS(G, "C", "A") == False)
    print("All DFS Tests Passed!")
    
