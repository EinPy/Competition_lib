import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


# Tested on: https://open.kattis.com/problems/froshweek
class FenwickTree: # zero indexed calls!
    # Give array or size!
    def __init__(self, blob):
        if type(blob) == int:
            self.sz = blob
            self.data = [0]*(blob+1)
        elif type(blob) == list:
            A = blob
            self.sz = len(A)
            self.data = [0]*(self.sz + 1)
            for i, a in enumerate(A):
                self.inc(i, a)
    # A[i] = v
    def assign(self, i, v):
        currV = self.query(i, i)
        self.inc(i, v - currV)
    # A[i] += delta
    # this method is ~3x faster than doing A[i] += delta
    def inc(self, i, delta):
        i += 1 # (to 1 indexing)
        while i <= self.sz:
            self.data[i] += delta
            i += i&-i # lowest oneBit
    # sum(A[:i+1])
    def sum(self, i):
        i += 1 # (to 1 indexing)
        S = 0
        while i > 0:
            S += self.data[i]
            i -= i&-i
        return S
    # return sum(A[lo:hi+1])
    def query(self, lo, hi):
        return self.sum(hi) - self.sum(lo-1)


def c(i,n): #clockwise
    return (i + 1) % n
def cc(i,n): #counterclockwise
    if i == 0:
        return n-1
    return i - 1

#insight, rotating all objects clockwise means walking in the 
#counterclockwise direction
#if i rotate the thing clockwise the counterclockwise object will fall in my hand

db = False
def solve(order, n):
    balls = [1 for _ in range(n)]
    T = FenwickTree(balls)
    cur = 0
    ops = 0
    ccstep = 0
    cstep = 0
    for p in order:
        if db: print("at index", cur, "rem", p)
        ccstep = 0
        cstep = 0
        if p == cur:
            if db: print("same idx")
            ops += 1
            T.assign(cur, 0)
            cur = c(cur, n)
        else:
            if p < cur:
                ccstep = T.query(p, cur)
                cstep += T.query(cur, n-1) + T.query(0, p)
            elif p > cur:
                cstep = T.query(cur, p)
                ccstep = T.query(0, cur) + T.query(p, n-1)
            if T.query(cur, cur) == 0:
                cstep -= 1
            if T.query(cur, cur) == 1:
                cstep -= 1
                ccstep -= 1
            ops += min(cstep, ccstep) + 1
            T.assign(p,0)
            cur = c(p, n)
            
    print(ops)       
    F = False 
    for i in range(n):
        if T.query(i,i) != 0:
            F = True
    if F: print("ERR")
    
    return 0


for i in range(10):
    n = ni()
    order = [0 for _ in range(n)] #pos i is the position of the ball starting clockwise form the jugglers hand
    for i in range(n):
        pos = ni() - 1
        order[pos] = i


    if db: print(order)
    solve(order, n)
            


def test():
    T = FenwickTree([1, 1, 1, 0, 1])
    n = 5
    ccstep = 0
    cstep = 0
    p = 0
    cur = 4
    ops = 0
    if p == cur:
        if db: print("same idx")
        ops += 1
        T.assign(cur, 0)
        cur = c(cur, n)
    else:
        if p < cur:
            ccstep = T.query(p, cur)
            cstep += T.query(cur, n-1) + T.query(0, p)
        elif p > cur:
            cstep = T.query(cur, p)
            ccstep = T.query(0, cur) + T.query(p, n-1)
        if T.query(cur, cur) == 0:
            cstep -= 1
        if T.query(cur, cur) == 1:
            cstep -= 1
            ccstep -= 1
        ops += min(cstep, ccstep) + 1
        T.assign(p,0)
        cur = c(p, n)
    print(ops)
    
#test()