from pydoc import visiblename
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def bfs(graph, R, C,vis, r, c):
    q = [(r,c)]
    while q:
        q2 = []
        for r, c in q:
            for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    tup = nr, nc
                    if not vis[nr][nc] and graph[nr][nc] != '#':
                        vis[nr][nc] = 1
                        q2.append(tup)
        q = q2
    return vis


def solve(graph, R, C):
    visited = [[0 for _ in range(C)] for _ in range(R)]
    stars = 0
    for row in range(R):
        for col in range(C):
            if not visited[row][col] and graph[row][col] != '#':
                stars += 1
                visited = bfs(graph,R,C,visited, row, col)
    return stars

case = 1
while True:
    
    try:
        R, C = list(map(int,input().split()))
        graph = []
        for i in range(R):
            line = []
            s = input()
            for el in s:
                line.append(el)
            graph.append(line)
            
        stars = solve(graph,R,C)
        print(f'Case {case}: {stars}')
        case += 1
    except:
        break

    
    