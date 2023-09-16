import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


class event:
    def __init__(self, s, f):
        self.s = s
        self.f = f
        
    def __lt__(self, nxt):
        if self.f == nxt.f:
            return self.s < nxt.s
        return self.DOB < nxt.DOB


t, k = nl()
act = []
for case in range(t):
    act.append(nl())
print(act)
    
#sort based on end times?, want to insert everything that ends the earliest
#then find the enxt things that ends the earliest, and put into the stream that ends the latest possible?
act.sort(key= lambda x : x[-1])

cur_ends = [0 for _ in range(k)]
print(act)
