import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





row, col  = nl()
g=[]  
water = [] 
start =(0,0)
end = (0,0)
for line in range (row):
    r = list(INP())
    g.append(r)
    for idx, c in enumerate(r):
        if c == '*':
            water.append((line,idx))
        if c == 'S':
            start = (line, idx, 0)
        if c == 'D':
            end = (line, idx)
            
    
# for l in g:
#     print(l)
# print(water) 
# print(start)
# print(end)

#first fill the water squares one layer, then fill the possible movement squares one layer
 
q = [start]
vis=[[0 for _ in range(col)] for _ in range(row)]
vis[start[0]][start[1]] = 1

while True:
    
    #one water iteration
    w2=[]
    #print(water)
    for r, c in water:
        for nr, nc in [(r, c +1), (r, c - 1), (r + 1, c), (r - 1, c)]:
            if nr >=0 and nr < row and nc>=0 and nc < col:
                if g[nr][nc] != 'X' and g[nr][nc] != '*' and g[nr][nc] != 'D':
                    g[nr][nc] = '*'
                    w2.append((nr, nc))
    water = w2
    
    q2 = []
    if not q:
        print('KAKTUS')
        exit()
    
    for r, c, d in q:
        for nr, nc in [(r, c +1), (r, c - 1), (r + 1, c), (r - 1, c)]:
            if nr >=0 and nr < row and nc>=0 and nc < col:
                if g[nr][nc] != 'X' and g[nr][nc] != '*' and not vis[nr][nc]:
                    if (nr, nc) == end:
                       print(d+1)
                       exit()
                    q2.append((nr, nc, d+ 1))
                    vis[nr][nc] = 1
                    
    q = q2
    # for l in g:
    #     print(l)
    
    
    
                    
    
                    
    
                     