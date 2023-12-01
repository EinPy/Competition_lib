import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [_ for _ in INP().split()]


def solve(adj, dir, n):
    in_deg = [0] * len(adj)
    for i in range(1, len(adj)):
        a, b = adj[i]
        in_deg[a] += 1
        in_deg[b] += 1
        
    q = deque([i for i in range(len(adj)) if in_deg[i] == 0 and i !=0])
    balls = [0] * len(adj)
    balls[1] = n
    
    while q:
        u = q.popleft()
        #print("at", u, "balls", balls[u])
        if u != 0:
            b = balls[u]
            left, right = 0,0
            if b == 0:
                left = 0
                right = 0
            else:
                if b % 2 == 0:
                    left = b // 2
                    right = b // 2
                else:
                    if dir[u] == "L":
                        left = b // 2 + 1
                        right = b // 2 
                    else:
                        left = b // 2
                        right = b // 2 + 1
                    
            #flip switches later
            left_node = adj[u][0]
            right_node = adj[u][1]
            
            #send balls
            balls[left_node] += left
            balls[right_node] += right
            
            for vert in adj[u]:
                in_deg[vert] -= 1
                if in_deg[vert] == 0:
                    q.append(vert)
                 
    out = []
    #print(balls)
    for i in range(1, len(dir)):
        if balls[i] % 2 == 0:
            out.append(dir[i])
        else:
            if dir[i] == "L":
                out.append("R")
            else:
                out.append("L")
    print("".join(out))
    




N, M = nl()
N = int(N)
M = int(M)


adj = [[0,0] for _ in range(M+1)]
dir = [0] * (M+1)

for s in range(1,M+1):
    d, left, right = nl()
    dir[s] = d
    adj[s][0] = int(left)
    adj[s][1] = int(right)
    
solve(adj, dir, N)