import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

from heapq import heappush, heappop

new, opt, slot, cap = nl()
#insight: maximize the available slots that have no warm soda
arr = nl()
heap = []
available = 0

for i in range(slot):
    available += arr[i]
    heappush(heap,(arr[i], i))
    
out = []

while new > 0:
    am, ind = heappop(heap)
    diff = cap - am
    add = min(diff, new)
    new -= add
    out.append((ind, add))
    
out.sort()

for i, el in out:
    print(el, end = " ")