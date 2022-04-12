import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code



#standard template
def solve(n,m,p,graph,c,s,e):
#    print(graph)
    print(djikstra(s,e,graph,c, n, p))


INF = 10**9
#djikstra ashortest path in weighted graph. 
from heapq import heappush, heappop
# G: [[(to_node, weight)]], for instance [[(1,3), (0,3), ...], [...], ...]
#input is start, finish, graph, fuelTankSize, amount of node, price list
def djikstra(S, F, G, c, n, p):
    dists = [[INF for _ in range(n)] for _ in range(c+1)]
#    print(dists)
    heap = []
    #tot cost, node, curTank
    heappush(heap, (0,S,0))
    dists[0][S] = 0
    
    while heap:
        cost, node, tank = heappop(heap)
        if node == F: return cost
        for vertex, dist in G[node]:
            fuel = tank - dist
            if fuel >= 0 and fuel <= c:
                if cost < dists[fuel][vertex]:
                    dists[fuel][vertex] = cost
                    heappush(heap,(cost, vertex, fuel))

        if tank < c:
            fuel = tank + 1
            cost += p[node]
            if cost < dists[fuel][node]:
                dists[fuel][node] = cost
                heappush(heap,(cost, node, fuel))

    if dists[0][F] == INF: return "impossible"
    return dists[0][F]






def run():
    n, m = list(map(int,input().split()))
    p = list(map(int,input().split()))
    graph = [[] for _ in range(n)]
    for edge in range(m):
        u, v, d = list(map(int,input().split()))
        graph[u].append((v, d))
        graph[v].append((u, d))
        
        
    q = int(input())
    for query in range(q):
        c, s, e = list(map(int,input().split()))
        solve(n,m,p,graph,c,s,e)


run()