
import sys
sys.path.append("../")

from graphs import create_graph

def topsort(G):
    '''
    Topologically sort the graph
    '''
    i = 0    
    visited = {v:False for v in G.get_vertices()}
    ft = {v:None for v in G.get_vertices()}
    
    def DFS(u):
        nonlocal i
        nonlocal visited
        
        visited[u] = True
        
        for v in G[u]:
            if (visited[v] == False):
                DFS(v)
                
        ft[u] = i
        i += 1
    
    for u in visited:
        if (visited[u] == False):
            DFS(u)
    
    return sorted(ft, key=ft.get, reverse=True)


if __name__ == "__main__":
    dag = create_graph(
        ["A", "B", "C", "D", "E", "F", "G", "H"], 
        [("A", "B"), 
         ("A", "C"), 
         ("H", "A"),
         ("H", "D"),
         ("D", "F"),
         ("E", "H"),
         ("E", "G"),
         ("G", "D")]
    )
    
    print(topsort(dag))


