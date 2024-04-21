import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


from heapq import heapify, heappop, heappush

n = ni()
tasks = []
for _ in range(n):
    a, b = nl()
    tasks.append((b, a))
tasks.sort()

#keep a heap of longest task to now, half it

cur = []
heapify(cur)

curtime = 0
totwork = 0
drinks = 0
for nowtime, worktime in tasks:
    curtime = nowtime
    totwork += worktime
    heappush(cur, - 1 * worktime)
    #print("adding ", worktime, "curtime ", curtime, "totwork", totwork)
    #print(cur)
    while totwork > curtime:
        rem = heappop(cur)
        actual = -1 * rem
        totwork -= actual
        totwork += actual // 2
        heappush(cur, -1 * (actual // 2))
        drinks += 1
        
print(drinks)
        
