#https://www.spoj.com/problems/HAYBALE/

import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n,k = nl()
arr = [0 for _ in range(n+2)]
for q in range(k):
    l, r = nl()
    arr[l] += 1
    arr[r+1] -= 1

pref = [0] * (n+1)
tot = 0
for i in range(n+1):
    tot += arr[i]
    pref[i] = tot

pref = pref[1:]
#print(pref)
pref.sort()
if len(pref) == 1:
    print(pref[0])
else: print(pref[(n-1)//2])