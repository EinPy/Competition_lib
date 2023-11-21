import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



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


arr = [[10, 1], []]

def pWin(a, b):
    return a / (a + b)
        
def add(left, right):
    newArr = []
    
    #for every player in left node
    #fight every player in right node
    #leftmostplayer will be dale
    #print("match", left, right)
    for a, p1, id1 in left:
        for b, p2, id2 in right:
            newArr.append((a,pWin(a, b) * p1 * p2, id1))
            newArr.append((b,pWin(b, a) * p1 * p2, id2))
    #print("result,", newArr)
    return newArr
    
    
n = ni()

ratings = []
dale = ni()
for _ in range(n-1):
    ratings.append([(ni(), 1, 0)])
    
ratings.sort(reverse=True)
cur = 2
while cur < n:
    cur *= 2
    
if cur != n:
    to_add = cur - n
    ratings = [[(dale, 1, 1)]] + [[(0,1,0)] * to_add] + ratings
    print(cur)
    print(len(ratings))
else:
    ratings = [[(dale, 1, 1)]] +  ratings
#ratings = [[(dale, 1, 1)]] + ratings
print(ratings)
#print(ratings)
T = SegmentTree(ratings, add)
#print("query")
#print(T.query(0,n-1))
out = T.query(0, n-1)
tot = 0
for pow, prob, id in out:
    #print(pow, prob, id)
    if id == 1:
        #print("adding", prob)
        tot += prob
print(tot)



