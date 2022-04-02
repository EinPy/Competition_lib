import code
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code

def solve(n,bs):
    if n == 0:
        return 0

    if n <= 3:
        if bs[0] == 1:
            return 1
        else:
            return 0

    bs = bs +[0,0]
    n += 2
    g = [[] for _ in range(n)]

    
#    print(bs)
    for node in range(2):
#        print(node)
        if bs[node] == 1:
#            print("true")
            if node + 2 < n and bs[node+2] == 1:
#                print("happned")
                g[node].append((node+2,2))
            elif node + 2 < n:
                g[node].append((node+2,1))
            if node + 3 < n and bs[node+3] == 1:
                g[node].append((node+3,2))
            elif node + 3 < n:
                g[node].append((node+3,1))
        else:
            if node + 2 < n and bs[node+2] == 1:
                [node].append((node+2,1))
            elif node + 2 < n:
                g[node].append((node+2,0))
            if node + 3 < n and bs[node+3] == 1:
                g[node].append((node+3,1))
            elif node + 3 < n:
                g[node].append((node+3,0))
        if node == 0:
            cost = 0
            cost += bs[0] + bs[1]
            g[node].append((node+1,cost))

    for node in range(2,n):
        if node + 2 < n and bs[node+2] == 1:
            g[node].append((node+2,1))
        elif node + 2 < n:
            g[node].append((node+2,0))
        if node + 3 < n and bs[node+3] == 1:
            g[node].append((node+3,1))
        elif node + 3 < n:
            g[node].append((node+3,0))

    print(g)
    return djikstra(0,g)[-1]


#djikstra ashortest path in weighted graph. 
from heapq import heappush, heappop
# S: Start node
# G: [[(to_node, weight)]], for instance [[(1,3), (0,3), ...], [...], ...]
#return shortes dists to all
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
    


T = int(input())
for c in range(T):
    n = int(input())
    bs = list(map(int,input().split()))
    print(solve(n,bs))
