#To start code
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#code



def att(row, col, a):
    sum = 0
    sum += a[row][col]

    r = row + 1
    c = col + 1

    maxR, maxC = len(a), len(a[0])

    while r < maxR and c < maxC:
        sum += a[r][c]
        r+= 1
        c += 1

    r = row - 1
    c = col -1 
    while r >= 0 and c >= 0:
        sum += a[r][c]
        r -= 1
        c -= 1

    r = row + 1
    c = col -1 
    while r < maxR and c >= 0:
        sum += a[r][c]
        r += 1
        c -= 1

    r = row - 1
    c = col + 1 
    while r >= 0 and c < maxC:
        sum += a[r][c]
        r -= 1
        c += 1
    
    return sum


def solve(row, col, a):
    best = 0
    #print(2, 2, a)
    #print(att(2,2,a))

    for r in range(row):
        for c in range(col):
            #print(r,c)
            best = max(best, att(r,c,a))
    return best




t = ni()
for case in range(t):
    r, c = nl()
    a = []
    for i in range(r):
        a.append(nl())
    print(solve(r, c, a))