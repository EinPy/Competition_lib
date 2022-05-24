import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



class FenwickTree: # zero indexed calls!
    def __init__(self, sz):
        self.data = [0]*(sz+1)

    def inc(self, i, delta):
        i += 1 # (to 1 indexing)
        while i < len(self.data):
            self.data[i] += delta
            i += i&-i # lowest oneBit
    def sum(self, i):
        i += 1 # (to 1 indexing)
        S = 0
        while i > 0:
            S += self.data[i]
            i -= i&-i
        return S
    def query(self, lo, hi):
        return self.sum(hi) - self.sum(lo)


n, q= nl()
a = nl()
f = FenwickTree(n)
for i, v in enumerate(a):
    f.inc(i, v)

for _ in range(q):
    l, r = nl()
    print(f.query(l-1,r-1))
