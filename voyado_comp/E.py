import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
l = nl()
seen = {}
for i in range(len(l)):
    l[i] += 1
    if l[i] not in seen:
        seen[l[i]] = 1
    else:
        seen[l[i]] += 1
        
#print(seen)
total = 0
for k in seen.keys():
    whole = seen[k] // k
    if seen[k] % k != 0:
        whole += 1
    total += max(whole * k, k)
    
print(total)