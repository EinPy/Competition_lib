import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
if n == 1:
    print(0)
else:
    n -= 1
    n = n
    s = list(map(int,list(bin(n))[2:]))
    #print(s)
    arr = []
    for i in range(len(s)):
        if s[i] == 0:
            arr.append(i+1)
            
    pFail = 0

    for num in arr:
        pFail += 1/2**num

    ans = (1-pFail) * len(s)
    el = 0
    for num in arr:
        el += num / (2**num)
        
    print((ans+el)/(1-pFail))

            
    #print(arr)