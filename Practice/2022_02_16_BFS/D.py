import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

def printarr(arr):
    for row in arr:
        print(row)
    print('\n')

def bfs(graph, R, C, start):
    q = start
    dists = [[-1 for _ in range(C)] for _ in range(R)]
    for r, c in q:
        dists[r][c] = 0
    while q:
        q2 = []
        for r, c in q:
            for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    tup = nr, nc
                    if dists[nr][nc] == -1 and graph[nr][nc] != '#':
                        dists[nr][nc] = dists[r][c] + 1
                        q2.append(tup)
        q = q2
#    printarr(dists)
    return dists


def solve(graph, R, C):
    fires = []
    person = (0,0)
    for r in range(R):
        for c, val in enumerate(graph[r]):
            if val == '*':
                fires.append((r,c))
            elif val == '@':
                person = [(r,c)]
    fDists = bfs(graph,R,C, fires)
    pDists = bfs(graph,R,C, person)
    for r in range(R):
        for c, val in enumerate(graph[r]):
            if (val == '.'  or val == '@') and (r == 0 or r == R-1):
                if pDists[r][c] < fDists[r][c] and pDists[r][c] != -1:
                    return pDists[r][c] + 1
            elif (val == '.'  or val == '@') and (c == 0 or c == C-1):
                if pDists[r][c] < fDists[r][c] and pDists[r][c] != -1:
                    return pDists[r][c] + 1
    return "impossible".upper()

T = int(input())
for i in range(T):
    C, R = list(map(int,input().split()))
    graph= []
    for line in range(R):
        l = input()
        arr = []
        for c in l:
            arr.append(c)
        graph.append(arr)
        
    print(solve(graph,R,C))
            
    