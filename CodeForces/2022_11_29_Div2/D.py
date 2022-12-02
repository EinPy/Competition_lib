import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math
t = ni()
for _ in range(t):
    n = ni()
    # in the case of two, 3, 1

    if n == 2:
        print("3 1")
    else:
        for i in range(2,3*10**5):
            sq = i ** 2
            #print(sq)
            if (i+1) + (n-1) <= sq and (i+1)*(n-1) + 1 > sq:
                out = [i+1, 1]
                add = [1 for _ in range(n-2)]
                toAdd = sq
                sq -= (i+1)
                sq -= 1
                sq -= sum(add)
                #print(add)
                for j in range(len(add)):
                    if sq >= i:
                        add[j] += i
                        sq -= i
                    else:
                        add[j] += sq
                        sq = 0
                #print(add)
                out += add
                print(*out)
                break