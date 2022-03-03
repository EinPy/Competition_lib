import sys
from turtle import circle
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


from heapq import heappush, heappop


INF = 10**9
def solve (S, G, F, fuelLim, fPrice):
    dists = [[INF for _ in range(fuelLim)] for _ in range(len(G))]
    heap = []
    for node in range(N):
        price = fPrice[node]
        for dummy in range(fuelLim):
            pass
 
    #(totCost, node, inTank)
    heappush(heap, (0,S, 0))
    dists[S] = 0
    
    while heap:
        d, u, t = heappop(heap)
        if u == F: return d
        for v, c in G[u]:
            alt = d + c
            fuel = t - c
            if t >= 0 and alt < dists[v]:
                dists[v] = alt
                heappush(heap, (alt, v, fuel))
    return dists[F]
        
        

N, M = list(map(int,input().split()))
fPrice = list(map(int,input().split()))
graph = [[] for _ in range(N)]
quer = []

for i in range(M):
    u, v, w = list(map(int,input().split()))
    graph[u].append((v,w))
q = int(input())
for i in range(q):
    cCap, S, E = list(map(int,input().split()))
    quer.append((cCap,S,E))
    
for query in quer:
    print(solve(query[1], graph, query[2], query[1], fPrice))