import sys
from collections import *
sys.setrecursionlimit(1*10**5 + 30000)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,arr):
    #finding root
    root = None
    arr = [-1] + arr
    
    outDeg = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        if arr[i] == i:
            root = i
        
    newG = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        to = arr[i]
        if to != i:
            newG[i].append(to)
            newG[to].append(i)
        else:
            newG[to].append(i)
        
    #print(root)
    #print(newG)
    
    
    used = [False for _ in range(n+1)]
    paths = []

    def dfs(v, p = []):
        used[v] = True
        p.append(v)
        
        branches = 0
        
        for u in range(len(newG[v])):
            if not used[newG[v][u]]:
                if branches == 0:
                    #print("going to ->", newG[v][u], "with path", p)
                    dfs(newG[v][u],p)
                    branches += 1
                else:
                    #print("going to: ", newG[v][u])
                    new = []
                    dfs(newG[v][u], new)
                    branches += 1
            
        if branches == 0:
            paths.append(p)
            dfs.leafs += 1
            #print("leaf: ", v,"curPath", p)
    
            #print("allpaths", paths)
    
    dfs.leafs = 0
      
    dfs(root)  
    print(dfs.leafs)
    for path in paths:
        print(len(path))
        for i in path:
            print(i, end = ' ')
        print()
    print()
    


t = ni()
for case in range(t):
    n = ni()
    arr = nl()
    solve(n,arr)