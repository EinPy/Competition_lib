import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


import math
def check(pop, box, targ):
    use = 0
    for p in pop:
        use += math.ceil(p / targ)
        if use > box:
            return False
    return True

def bns(pop, box):
    l, r = 0, max(pop)
    best = 0
    while l <= r:
        mid = (l + r) // 2
        if check(pop, box, mid):
            best =  mid
            r = mid -1
        else:
            l = mid +1
    return best

while True:
    N,B = nl()
    if N == B == -1:
        break
    q  =[]
    for row in range(N):
        q.append(ni())
        
    print(bns(q, B))
    
    clear = INP()