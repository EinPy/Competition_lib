import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [float(_) for _ in INP().split()]


import math


dist = nl()
num = nl()
lambd = 640 * 10 **(-9)
ans = []
for i in range(len(num)):
    ans.append(math.sqrt(dist[i]*10**(-2) * num[i] * lambd))
    

print(ans)

tot = sum(ans)
mid = tot / len(num)
print(mid)
print("mmm:", mid * 10**3)
