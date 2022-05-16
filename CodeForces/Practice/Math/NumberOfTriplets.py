import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




def solve(t, p):
    #sorted by x coordinate
    a2 = [[0 for _ in range(2002)] for _ in range(2002)]
    
    for i in range(t):
        x1, y1 = p[i][0], p[i][1]
        a2[x1 + 1000][y1+1000] = 1
        
    seg = 0
    for p1 in range(t-1):
        for p2 in range(p1+1, t):
            x1, y1 = p[p1]
            x2, y2 = p[p2]
            if (x1 + x2) % 2 == 0 and (y1 + y2) % 2 == 0:
                x = (x1 + x2) //2
                y = (y1 + y2) // 2
                if a2[x+1000][y+1000]:
                    #print(x1, y1, x2, y2, x, y)
                    seg += 1
                    
    print(seg)
            
    



t = ni()
p = []
for case in range(t):
    x, y = nl()
    p.append((x,y))
solve(t, p)