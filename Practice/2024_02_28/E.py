import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def ok(secs, ms, proj, val, k):
    scores = []
    for i in range(len(ms)):
        #for a week:
        p_week = 0
        s = secs
        #do projects in week i until you cannot anymore
        for j in range(len(proj[i])):
            p = proj[i][j]
            s -= p
            if s >= 0:
                p_week += val[i][j]
            else:
                break
        if p_week >= ms[i]:
            scores.append(10)
        else: 
            scores.append(10 * (1 - (1 - p_week/ms[i])**2))
    scores.sort(reverse=True)
    avg = sum(scores[:k]) / k
    if avg >= 4.75:
        return True
    else:
        return False
        

#Binary search for lower bound
def lower_bound(ms, proj, val, k):
    l, r, m = 0, 10**18, 0
    ans = -1
    while l<= r:
        mid = (l + r) // 2
        #print(mid)
        if ok(mid, ms, proj, val, k):
            ans = mid
            r = mid-1
        else:
            l = mid + 1
    return ans

n, k = nl()

max_score = []
proj = []
val = []

for row in range(n):
    s, m = nl()
    max_score.append(s)
    projects = nl()
    proj.append(projects)
    scores = nl()
    val.append(scores)
    
print(lower_bound(max_score, proj, val, k))