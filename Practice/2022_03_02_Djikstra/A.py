import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


from heapq import heappush, heappop


INF = 10**9
def solve (S, G, Q):
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
        
    for q in Q:
        if dists[q] == INF: print("Impossible")
        else: print(dists[q])
            
        
while True:
    try:
        N, M, Q, S  = list(map(int,input().split()))
        graph = [[] for _ in range(N)]
        quer = []
        for i in range(M):
            u, v, w = list(map(int,input().split()))
            graph[u].append((v,w))
        for i in range(Q):
            quer.append(int(input()))
            
        solve(S, graph, quer)
    except:
        break

