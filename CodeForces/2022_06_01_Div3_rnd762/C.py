import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(a, s):
    a = list(map(int,list(str(a))))
    s = list(map(int, list(str(s))))
    ans = [0] * len(a)
    sI = 0
    aI = 0
    #print(a, s)
    while sI < len(s):
        if s[sI] > a[aI]:
            ans[aI] = s[sI] - a[aI]
            sI += 1
            aI += 1
        elif s[sI] == a[aI]:
            ans[aI] = 0
            sI += 1
            aI += 1
        elif s[sI] < a[aI]:
            rem = 10 - a[aI]
            #print(sI, aI,s[sI], a[aI], rem)
            if sI ==  len(s)-1:
                return -1
            add =  rem + s[sI+1]
            if add > 9:
                return -1
            ans[aI] = add
            sI += 2
            aI += 1
        print(aI, sI , ans)
    ind = 0
    for i in range(len(ans)):
        if ans[i] != 0:
            ind = i
            break
    out = ans[i:]
    return ''.join(map(str,out))
            


t = ni()
for case in range(t):
    a, s = nl()
    print(solve(a, s))