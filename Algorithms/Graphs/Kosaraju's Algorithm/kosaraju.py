
import sys
sys.path.append("../")
sys.path.append("../Topological Sort")

from graphs import create_graph, reverse_graph
from topsort import topsort



def kosaraju(G):
    Grev = reverse_graph(G)
    f = topsort(Grev)
    
    visited = {v:False for v in f}
    scc = []
    
    def DFS(u):
        nonlocal visited
        nonlocal scc
        
        visited[u] = True
        scc[-1].append(u)
        
        for v in G[u]:
            if (visited[v] == False):
                DFS(v)
    
    for v in f:
        if (visited[v] == False):
            scc.append([])
            DFS(v)
        
    return scc

def test_kosaraju(result, expected):
    for scc in result:   scc.sort()
    for scc in expected: scc.sort()
        
    result.sort(key=lambda x: x[0])
    expected.sort(key=lambda x: x[0])
    
    if (any(set(r) != set(s) for r, s in zip(result, expected))):
        raise Exception(f"{result} != {expected}")
    
    
if __name__ == "__main__":
    G = create_graph(
        ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
        [("L", "I"),
         ("I", "J"),
         ("J", "K"),
         ("K", "L"),
         ("J", "A"),
        
         ("A", "D"),
         ("D", "H"), 
         ("H", "A"),
         ("D", "E"),
         ("H", "B"),
        
         ("E", "F"),
         ("F", "G"),
         ("G", "E"),
        
         ("B", "C"),
         ("C", "B")]
    )
    test_kosaraju(
        kosaraju(G),
        [["A", "D", "H"],
         ["B", "C"],
         ["E", "F", "G"],
         ["I", "J", "K", "L"]]
    )
    
    print("All Kosaraju's Algorithm Tests Passed!")
