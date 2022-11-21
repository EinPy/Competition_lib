from re import L
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

#solution to https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/C
# Input
# The first line contains two integers n and m (1≤n,m≤100000), the size of the array and the number of operations. 
# The next line contains n numbers ai, the initial state of the array (0≤ai≤109). The following lines contain the description of the operations. The description of each operation is as follows:

# 1 i v: set the element with index i to v (0≤i<n, 0≤v≤109).
# 2 l r: calculate the minimum and number of elements equal to minimum of elements with indices from l to r−1 (0≤l<r≤n).
# Output
# For each operation of the second type print two integers: the minimum on a segment, and the number of elements equal to minimum.



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


def comb(l, r):
    #print(l, r)
    cl, vl = l
    cr, vr = r
    if vl == vr:
        #print("result", )
        return [cl + cr, vl]
    if vl < vr:
        return [cl, vl]
    else:
        return [cr, vr]
    

n, m = nl()
a = [[1, i] for i in nl()]
#print(a)
tree = SegmentTree(a, comb)
for _ in range(m):
    t, l, r = nl()
    if t == 1:
        tree.assign(l, [1,r])
    else:
        #print(t, l, r)
        cnt, num = tree.query(l, r-1)
        print(num, cnt)
