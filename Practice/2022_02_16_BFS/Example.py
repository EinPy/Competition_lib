import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#Bfs to find distannce to all nodes in graph
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

test = input()
print(test)