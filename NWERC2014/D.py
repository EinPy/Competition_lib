import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [_ for _ in INP().split()]

db = True

def solve(adj, n, dir):
    #compute in_degree of each node
    #print(adj)
    in_deg = [0] * len(adj)
    for i in range(1,len(adj)):
        #check left and right path
        a, b = adj[i]
        in_deg[a] += 1
        in_deg[b] += 1
        
    if db: print(in_deg)
        
    q = deque([1]) #starting node
    balls = [0] * len(adj)
    balls[1] = n
    
    while q:
        u = q.popleft()
        if u != 0:
            
            b = balls[u]
            left, right = 0,0
            
            if db: print("at", u, "balls: ", b, "dir", dir[u])
            
            if b % 2 == 0:
                #equal to left and right
                left = b // 2
                right = b // 2
            else:
                #flip switch and uneven distribution
                if dir[u] == "L":
                    left = b // 2 + 1
                    right = b // 2 
                    dir[u] = "R"
                else:
                    left = b // 2
                    right = b // 2 + 1
                    dir[u] = "L"
            

            left_n = adj[u][0]
            right_n = adj[u][1]
            
            balls[left_n] += left
            balls[right_n] += right
            
            in_deg[left_n] -= 1
            if in_deg[left_n] == 0:
                q.append(left_n)
            
            in_deg[right_n] -= 1
            if in_deg[right_n] == 0:
                q.append(right_n)
    
    #print(dir)
    print("".join(dir[1:]))


n, m = nl()
n = int(n)
m = int(m) #nodes from 0 to m inclusive
adj = [[] for _ in range(m+1)]
dir = [-1] * (m+1)
#starting at 1
for s in range(1, m+1):
    d, a, b = nl()
    a = int(a)
    b = int(b)
    
    dir[s] = d
    
    adj[s].append(a) #left first
    adj[s].append(b) #right second
    
solve(adj, n, dir)