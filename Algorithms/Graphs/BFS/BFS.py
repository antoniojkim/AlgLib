
import sys
sys.path.append("../")

from graphs import create_graph
from collections import deque

def BFS(G, u, v):
    '''
    Check if there exists a path from u to v
    '''
    assert(u in G and v in G)

    V = {k:False for k in G.get_vertices()} # visited
    Q = deque([u])
    while len(Q) > 0:
        n = Q.popleft()
        V[n] = True
        if (n == v):
            return True
        else:
            for k in G[n]:
                if (V[k] == False):
                    Q.append(k)

    return False


if __name__ == "__main__":
    G = create_graph(["A", "B", "C"], [("A", "B"), ("B", "C")])
    assert(BFS(G, "A", "C") == True)
    assert(BFS(G, "C", "A") == False)
    print("All BFS Tests Passed!")
    
