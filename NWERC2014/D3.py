import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math
from collections import deque

def solve(adj, direction ,balls):
    in_deg = [0] * len(adj)
    
    for i in range(1, len(adj)):
        a, b = adj[i]
        in_deg[a] += 1
        in_deg[b] += 1
        
    q = deque([1])
    b = [0] * len(adj)
    b[1] = balls
    
    while q:
        u = q.popleft()
        if u != 0:
            left, right = 0,0
            cnt = b[u]
            if cnt % 2 == 0:
                left = cnt // 2
                right = cnt // 2
            else:
                if direction[u] == "L":
                    left = math.ceil(cnt / 2)
                    right = math.floor(cnt / 2)
                else:
                    left = math.floor(cnt / 2)
                    right = math.ceil(cnt / 2)
                    
            l_node = adj[u][0]
            r_node = adj[u][1]
            
            b[l_node] += left
            b[r_node] += right

            in_deg[l_node] -= 1
            if in_deg[l_node] == 0:
                q.append(l_node)
            
            in_deg[r_node] -= 1
            if in_deg[r_node] == 0:
                q.append(r_node)
                
    #print(direction)
    out = []
    for i in range(1, len(adj)):
        if b[i] % 2 == 0:
            out.append(direction[i])
        else:
            if direction[i] == "L":
                out.append("R")
            if direction[i] == "R":
                out.append("L")
    print("".join(out))
    


n, m = nl()
adj = [[0,0] for _ in range(m+1)]
direction = ["0"] * (m+1)

for s in range(1, m+1):
    C, L, R = INP().split()
    L = int(L)
    R = int(R)
    
    direction[s] = C
    adj[s][0] = L
    adj[s][1] = R
    
solve(adj, direction, n)