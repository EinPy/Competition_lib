
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



air, r = nl()
g = [[] for _ in range(air+1)]
l = [-1 for _ in range(air+1)]
possible = True

add = 0
vis = [False for _ in range(air+1)]

for _ in range(r):
    a, b, c = nl()
    
    if c == 2:
        if l[a] == 0 or l[b] == 0:
            possible = False
            break
        l[a] = 1
        l[b] = 1
        if not vis[a]:
            add += 1
        if not vis[b]:
            add += 1
        vis[a] = True
        vis[b] = True
    elif c == 0:
        if l[a] == 1 or l[b] == 1:
            possible = False
            break
        l[a] = 0
        l[b] = 0
        vis[a] = True
        vis[b] = True
    else:
        g[a].append(b)
        g[b].append(a)
        

#Bfs to find distannce to all nodes in graph 
def bfs(S, t):
    global possible
    q = [S]
    toAdd = 0
    #print("visa:", S, t)
    while q:
        q2 = []
        t = not t
        for u in q:
            ##print("visa:", u, t)
            for n in g[u]:
                if t:
                    if l[n] == 0:
                        possible = False
                        return 0
                else:
                    if l[n] == 1:
                        possible = False
                        return 0
                if not vis[n]:
                    
                    vis[n] = True
                    q2.append(n)
                    if t:
                        l[n] = 1
                        toAdd += 1
                    else:
                        l[n] = 0
                    
        q = q2
    return toAdd


#Bfs to find distannce to all nodes in graph 
def bfsdub(S, t):
    q = [S]
    toAdd = 0
    seen = {S: True}
    if t:
        toAdd += 1
    #print("vis:", S, t)
    col = [-1 for _ in range(air+1)]
    col[S] = t
    while q:
        q2 = []
        t = not t
        for u in q:
            for n in g[u]:
                if t:
                    if l[n] == 0 or col[n] == 0:
                        return 1e9, {}
                else:
                    if l[n] == 1 or col[n] == 1:
                        return 1e9, {}
                if n not in seen:
                    #print("vis:", n, t)
                    seen[n] = True
                    q2.append(n)
                    if t:
                        col[n] = 1
                        toAdd += 1
                    else:
                        col[n] = 0
                    
        q = q2
    return toAdd, seen

#print(g)

for i in range(1,air+1):
    if l[i] != -1:
        t = l[i]
        if t == 0:
            t = False
        else:
            t = True
        #print("newC")
        add += bfs(i, t)

motherDict = {}
for i in range(1,air+1):
    if not vis[i] and  i not in motherDict:
        #print(i)
        #print(motherDict)
        a1, d = bfsdub(i,True)
        a2, d2 = bfsdub(i,False)
        if a1 == 1e9 and a2 == 1e9:
            possible = False
        if a1 <= a2:
            add += a1
            motherDict.update(d)
            #print(a1)
        else:
            add += a2
            motherDict.update(d2)
            #print(a2)
        #print("it")
        #print(motherDict)
if possible:
    print(add)
else:
    print("impossible")