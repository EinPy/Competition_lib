import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code


#djikstra ashortest path in weighted graph. 
from heapq import heappush, heappop
# S: Start node
# G: [[(to_node, weight)]], for instance [[(1,3), (0,3), ...], [...], ...]
#return shortes dists to all


def solve(n,m,p,graph,c,s,e):
    newG = [[] for _ in range(c*n)]
    for node in range(n):
        newN = []
        for el in range(len(node)):
            to,dist = graph[node][el]
            newN.append((to*c,dist))
        for dup in range(c):
            if dup != c-1:
                withEnd = newN + [(node*c + dup + 1, 200,1, )]
                newG[node*c+dup].append()
            
    


INF = 10**9
def djikstra (S, G):
    dists = [INF] * len(G)
    heap = []
    heappush(heap, (0,S))
    dists[S] = 0
    
    while heap:
        d, u = heappop(heap)
        for v, c in G[u]:
            alt = d + c
            if alt < dists[v]:
                dists[v] = alt
                heappush(heap, (alt, v))
                
    return dists


#return shortest path
def djikstra(S, F, G):
    dists = [INF] * len(G)
    heap = []
    heappush(heap, (0,S))
    dists[S] = 0
    
    while heap:
        d, u = heappop(heap)
        if u == F: return d
        if d > dists[u]: continue
        for v, c in G[u]:
            alt = d + c
            if alt < dists[v]:
                dists[v] = alt
                heappush(heap, (alt, v))
                
    if dists[F] == INF: return "impossible"
    return dists[F]

n, m = list(map(int,input().split()))
p = list(map(int,input().split()))
graph = [[] for _ in range(n)]
for edge in range(m):
    u, v, d = list(map(int,input().split()))
    graph[u].append(v,d,0)
    graph[v].append(u,d,0)
    
    
q = int(input())
for query in range(q):
    c, s, e = list(map(int,input().split()))
    solve(n,m,p,graph,c,s,e)
