import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

def bfs(Graph, S):
    q = [S]
    dists = {S:0}
    while q:
        q2 = []
        for u in q:
            for n in Graph[u]:
                if n not in dists:
                    dists[v] = dists[u] + 1
                    q2.append(v)
        q = q2
    return dists

def bfsGrid(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    q = [(r,c)]
    dists = {(r,c):0}
    while q:
        q2 = []
        for r, c in q:
            for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
                if 0 <= nr <= R and 0 <= nc < C:
                    tup = nr, nc
                    if tup not in dists: #add other conditions here
                        dits[tup] = dists[r,c] + 1
                        q2.append(tup)
        q = q2
    return dists

#test = input()
#print(test)

# Use a heap in the algorithm so that you always pick the 
# smallest distance in a type of list

from heapq import heappush, heappop

# S: Start node
# G: [[(to_node, weight)]], for instance [[(1,3), (0,3), ...], [...], ...]


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


def djikstra(S, F, G):
    dists = [INF] * len(G)
    parent = [None] * len(G)
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
                parent[v] = u
                heappush(heap, (alt, v))
                
    if dists[F] == INF: return None
    path = []
    curr = F
    while curr != None:
        path.append(curr)
        curr = parent[curr]
                
    return path[::-1]