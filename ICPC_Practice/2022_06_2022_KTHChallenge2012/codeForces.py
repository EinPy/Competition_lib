import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,q,quer,item):
    item.sort()
    prefArray = [0] * n
    tot = 0
    for i in range(n):
        tot += item[i]
        prefArray[i] = tot

    for qu in quer:
        x, y = qu[0], qu[1]
        if x == n:
            print(prefArray[y-1])
        else:
            print(prefArray[n-x-1+y] - prefArray[n-x-1])
        
    


n, q = nl()
item = nl()
quer = []
for _ in range(q):
    x, y = nl()
    quer.append([x,y])
solve(n,q,quer,item)