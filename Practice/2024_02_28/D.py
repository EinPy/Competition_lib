import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()

def ok(task, cnt):
    print("drinking", cnt)
    curtime = 0
    totwork = 0
    for nowtime, worktime in task:
        curtime = nowtime
        for div in range(cnt):
            worktime = worktime // 2
        totwork += worktime
        print("adding ", worktime, "curtime ", curtime, "totwork", totwork)
        if curtime < totwork:
            return False
        
    return True
            

tasks = []
for _ in range(n):
    a, b = nl()
    tasks.append((b, a))
tasks.sort()

print(tasks)
#Binary search for lower bound
def lower_bound(tasks):
    l, r, m = 0, 50, 0
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        print(mid)
        if ok(tasks, mid):
            ans = mid
            r = mid-1
        else:
            l = mid + 1
    return ans
    
print(lower_bound(tasks))
    
