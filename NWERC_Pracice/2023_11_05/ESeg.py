import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def add(a,b):
    return a + b

# Tested on: https://open.kattis.com/problems/supercomputer
class SegmentTree:
    def __init__(self, arr, func=min):
        self.sz = len(arr)
        assert self.sz > 0
        self.func = func
        sz4 = self.sz*4
        self.L, self.R = [None]*sz4, [None]*sz4
        self.value = [None]*sz4
        def setup(i, lo, hi):
            self.L[i], self.R[i] = lo, hi
            if lo == hi:
                self.value[i] = arr[lo]
                return
            mid = (lo + hi)//2
            setup(2*i, lo, mid)
            setup(2*i + 1, mid+1, hi)
            self._fix(i)
        setup(1, 0, self.sz-1)
    def _fix(self, i):
        self.value[i] = self.func(self.value[2*i], self.value[2*i+1])

    def _combine(self, a, b):
        if a is None: return b
        if b is None: return a
        return self.func(a, b)

    def query(self, lo, hi):
        assert 0 <= lo <= hi < self.sz
        return self.__query(1, lo, hi)

    def __query(self, i, lo, hi):
        l, r = self.L[i], self.R[i]
        if r < lo or hi < l:
            return None
        if lo <= l <= r <= hi:
            return self.value[i]
        return self._combine(
            self.__query(i*2, lo, hi),
            self.__query(i*2 + 1, lo, hi)
            )

    def assign(self, pos, value):
        assert 0 <= pos < self.sz
        return self.__assign(1, pos, value)

    def __assign(self, i, pos, value):
        l, r = self.L[i], self.R[i]
        if pos < l or r < pos: return
        if pos == l == r:
            self.value[i] = value
            return
        self.__assign(i*2, pos, value)
        self.__assign(i*2 + 1, pos, value)
        self._fix(i)

    def inc(self, pos, delta):
        assert 0 <= pos < self.sz
        self.__inc(1, pos, delta)

    def __inc(self, i, pos, delta):
        l, r = self.L[i], self.R[i]
        if pos < l or r < pos: return
        if pos == l == r:
            self.value[i] += delta
            return
        self.__inc(i*2, pos, delta)
        self.__inc(i*2 + 1, pos, delta)
        self._fix(i)

    # for indexing - nice to have but not required
    def __setitem__(self, i, v):
        self.assign(i, v)
    def __fixslice__(self, k):
        return slice(k.start or 0, self.sz if k.stop == None else k.stop)
    def __getitem__(self, k):
        if type(k) == slice:
            k = self.__fixslice__(k)
            return self.query(k.start, k.stop - 1)
        elif type(k) == int:
            return self.query(k, k)


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
    T = SegmentTree(balls, add)
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
        #print("after removal")
        #printTree(T)
        #print(T.query(0,0),T.query(1,1),T.query(2,2))
            
    
            
    #print(T[:], T[:1], T[:2], T[:3])
    
    print(ops)
    
    return 0

def printTree(T):
    #print(T.sz)
    for i in range(T.sz):
        print(T.query(i, i), end = " ")
    print()
    

for i in range(28):
    t = ni()
    k = [0 for _ in range(t)]
    for i in range(t):
        k[i] = ni() - 1

    solve(k,t)


# Test = [1, 1, 1, 1, 1]
# TT = SegmentTree(Test, add)
# printTree(TT)
# print(TT.query(0,4))
# #print(TT.query(0,-1))
# TT.inc(0, -1)
# printTree(TT)
