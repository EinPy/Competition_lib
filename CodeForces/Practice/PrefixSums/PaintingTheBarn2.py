#Solution to http://www.usaco.org/index.php?page=viewproblem2&cpid=923

import sys
from collections import *
sys.setrecursionlimit(10**5)
#sys.stdin = open("paintbarn.in")
#sys.stdout = open("paintbarn.out", "w")
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


### WORK IN PROGRESS ###

n, k = nl()
barn = [[0 for _ in range(11)] for _ in range(11)]
big = 0
for q in range(n):
    l = nl()
    for i in range(4):
        l[i] += 1
    x1, y1, x2, y2 = l
    #apparently it's non inclusive?
    #it's 0 indexed you fucking idiot
    barn[x1][y1] += 1
    barn[x2][y1] -= 1
    barn[x1][y2] -= 1
    barn[x2][y2] += 1

#for l in barn: print(l)
#print()


for r in range(1,11):
    for c in range(1, 11):
        barn[r][c] = barn[r-1][c] + barn[r][c-1] - barn[r-1][c-1] + barn[r][c]

tot = 0
for r in barn: print(r)
for r in range(1, 11):
    tot += barn[r].count(k)
print(tot)

