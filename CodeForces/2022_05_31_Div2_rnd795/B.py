import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    cnt = {}
    #print(a)
    for i in range(n):
        if a[i] not in cnt:
            cnt[a[i]] = [i]
        else:
            cnt[a[i]].append(i)
    out = []
    #print(cnt)
    for k in cnt.keys():
        if len(cnt[k]) <= 1:
            return -1
        else:
            rot = [cnt[k][-1]] + cnt[k][:len(cnt[k])-1]
            for i in range(len(rot)):
                rot[i] += 1
            out += rot
            
    return ' '.join(map(str,out))
    



t = ni()
for case in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))