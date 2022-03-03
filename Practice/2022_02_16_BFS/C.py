import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def bfs(graph,hL,N):
    q = hL
    scores = [(0,False) for _ in range(N)]
    for id in hL:
        scores[id] = (0,True)
    while q:
        p = q.pop(0)
        for n in graph[p]:
            if not scores[n][0] and not scores[n][1]:
                scores[n] = (scores[p][0] + 1, False)
                q.append(n)
    return scores.index(max(scores)), scores
            
    
def solve(graph, hL, N):
    best, scores = bfs(graph,hL,N)
    for i in range(N):
        if scores[i][0] == 0 and scores[i][1] == False:
            return i
    return best

N, H, L = list(map(int,input().split()))
horrLst = list(map(int,input().split()))
graph = [[] for _ in range(N)]
for i in range(L):
    a, b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a) 

print(solve(graph,horrLst,N))
    