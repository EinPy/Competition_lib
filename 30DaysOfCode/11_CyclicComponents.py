#Realize that a sufficient test for seeing if a 
#component of a graph is cyclic is that all nodes has
#two non duplicate edges
def bfs(graph, node, visited):
    q = [node]
    if not len(graph[node]) == 2:
        return False
    visited[node] = True
    cycle = True
    while q:
        q2 = []
        for u in q:
            for n in graph[u]:
                if not visited[n]:
                    if len(graph[n]) != 2:
                        cycle = False
                    visited[n] = True
                    q2.append(n)
        q = q2
 #   print(cycl)
    return cycle


v, e=  list(map(int,input().split()))
visited = [False for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
for edge in range(e):
    a, b = list(map(int,input().split()))
#    print(a,b)
    graph[a].append(b)
    graph[b].append(a)

cycles = 0
for node in range(1,len(graph)):
    if not visited[node]:
        if bfs(graph, node, visited):
            cycles += 1
print(cycles)