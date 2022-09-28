#https://codeforces.com/problemset/problem/441/C
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



x, y, cgr = nl()
g = [[False for _ in range(y)] for _ in range(x)]
#fill it via dfs, fill two at a time until there are only one left
#for l in g: print(l)
def dfs(xx, yy, cgr):
    g[xx][yy] = True
    q = [(xx,yy)]
    ordX =[]
    ordY = []
    cnt = 0
    while q:
        #print(q)
        a, b = q.pop()
        #for _ in g: print(_)
        ordX.append(a)
        ordY.append(b)
        cnt += 1
        if cgr > 1 and cnt > 1:
            cgr -= 1
            return ordX, ordY
        #print(ordX, ordY)
        for nx, ny in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if nx >= 0 and nx < x and ny >= 0 and ny < y:
                #print(nx, ny)
                if not g[nx][ny]:
                    q.append((nx,ny))
                    g[nx][ny] = True
    return ordX, ordY

for i in range(x):
    for j in range(y):
        if not g[i][j]:
            a, b = dfs(i, j, cgr)
            cgr -= 1
            print(len(a), end = " ")
            for p in range(len(a)):
                print(a[p]+1, b[p]+1, end = " ")
            print()