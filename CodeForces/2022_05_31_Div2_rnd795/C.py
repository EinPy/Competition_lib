import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, k, s):
    f0, f1, l0, l1 = -1, -1, -1, -1
    zerCnt = 0
    oneCnt = 0
    #print(s)
    s = list(map(int,list(s)))
    for i in range(n):
        if s[i] == 1:
            if f1 == -1:
                f1 = i
            l1 = max(l1, i)
            oneCnt += 1
        else:
            if f0 == -1:
                f0 = i
            l0 = max(l0, i)
            zerCnt += 1
        
    #print(l1, l0)
    
    if l1 != -1 and l0 != -1:
        #print("here")
        #print(n - l1, k)
        if s[-1] != 1:
            if n - (l1 +1) <= k:
                #print("truee")
                s[l1], s[l0] = 0, 1
                k -= n - (l1 +1)
                zerCnt -= 1
                oneCnt -= 1
        if s[0] != 1:
            if zerCnt > 0 and oneCnt > 0:
                #print(f1)
                if f1 <= k:
                    s[f1], s[f0] = 0, 1
    tot = 0
    print(s)
    for i in range(n-1):
        num = int(str(s[i]) + str(s[i+1]))
        tot += num
    print(tot)
                
            
            
    
t = ni()
for case in range(t):
    n, k = nl()
    s = INP()
    solve(n, k, s)