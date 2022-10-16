import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




def s(a,b,c,d):
    div = a * b
    # for a multiple of div, find 
    biggest = c * d
    for i in range(100000):
        targ = i * div
        if targ > biggest:
            break
        if targ < (a * b):
            continue
        else:
            for x in range(a+1, c+1):
                if targ // x == targ / x and targ // x > b and targ // x <= d:
                    print(x, targ//x)
                    return
        #create this number within boundries
    print(-1 ,-1)
    return
        
t = ni()
for case in range(t):
    a, b, c, d = nl()
    s(a,b,c,d)
