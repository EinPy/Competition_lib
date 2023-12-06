import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def find_segment_overlap(a, b, c, d):
    # Check if the segments overlap
    if a <= d and c <= b:
        # Calculate the overlap
        overlap_min = max(a, c)
        overlap_max = min(b, d)
        return True, overlap_min, overlap_max
    else:
        # Segments do not overlap
        return False, None, None

def ok(k, segs):
    #start at 0, jump no more than k steps
    #keep track of leftmost value and rightmost value
    mi, ma = 0,0
    for lb, rb in segs:
        overlap, left, right = find_segment_overlap(mi-k, ma+k, lb, rb)
        if not overlap:
            return False
        else:
            mi = left
            ma = right
    return True
            

def solve(n,a):
    l, r = 0, 10** 9 + 5
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if ok(mid, a):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)
            


t = ni()
for case in range(t):
    n = ni()
    a = []
    for _ in range(n):
        a.append(nl())
    solve(n,a)