import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code




def solve(n,m,p,graph,c,s,e):
#    print(graph)
    newG = [[] for _ in range(c*n)]
    for node in range(n):
        newN = []
        for el in range(len(graph[node])):
            to,cost,dist = graph[node][el]
            newN.append((to*c,cost,dist))
        for dup in range(c):
            if dup != c-1:
#                print(node)
                withEnd = newN + [(node*c + dup + 1, p[node],-1)]
#                print(node*c+dup)
                newG[node*c+dup] = withEnd
            else:
                newG[node*c+dup] = newN

#    print(newG)
    print(djikstra(s*c,e*c,newG,c, n))

            

INF = 10**9
#djikstra ashortest path in weighted graph. 
from heapq import heappush, heappop
# S: Start node
# G: [[(to_node, weight)]], for instance [[(1,3), (0,3), ...], [...], ...]
#return shortes dists to all
#return shortest path
def djikstra(S, F, G, c, n):
    dists = {}
#    print(dists)
    heap = []
    #tot cost, node, curTank
    heappush(heap, (0,S,0))
    dists[(0,S)] = 0
    
    while heap:
        cost, node, tank = heappop(heap)
        if node == F: return cost
        for vertex, price, dist in G[node]:
            alt = cost + price
            fuel = tank - dist
            if fuel >= 0 and fuel <= c:
                if (fuel, vertex) not in dists:
                    dists[(fuel, vertex)] = alt
                    heappush(heap, (alt, vertex,fuel))
                elif alt < dists[(fuel, vertex)]:
                    dists[(fuel, vertex)] = alt
                    heappush(heap, (alt, vertex,fuel))
                
    if (0,F) not in dists: return "impossible"
    return dists[(0,F)]



def run():
    n, m = list(map(int,input().split()))
    p = list(map(int,input().split()))
    graph = [[] for _ in range(n)]
    for edge in range(m):
        u, v, d = list(map(int,input().split()))
        graph[u].append((v,0, d))
        graph[v].append((u,0, d))
        
        
    q = int(input())
    for query in range(q):
        c, s, e = list(map(int,input().split()))
        solve(n,m,p,graph,c,s,e)


run()