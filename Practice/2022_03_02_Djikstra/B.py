import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


from heapq import heappush, heappop


INF = 10**9
def solve (S, G, F, fuelLim, fuelP,N):
    dists = [[INF]] * (N)
    heap = []
    print(dists)
    #(totCost, node, inTank)
    for re in range(fuelLim + 1):
        heappush(heap, (fuelP[S] * re ,S, re))
    dists[S] = 0
    print(heap)
    print(dists)
    while heap:
        d, u, t = heappop(heap)
        for refill in range(fuelLim - t + 1):
            fuel = t + refill
            cost = fuelP[u] * refill
            for v, c in G[u]:
                cur = fuel - c
                if cur >= 0:
                    newPrice = d + cost
                    dists[v].append(newPrice)
                    heappush(heap, (newPrice, v, cur))
    print(dists[F])
    print(min(dists[F]))
    print(F)
        
    

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
    print(query[1], graph, query[2], query[0], fPrice,N)
    solve(query[1], graph, query[2], query[0], fPrice,N)