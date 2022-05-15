import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def ok(s, k):
    tmp0 = tmp1 = 0
    max1 = i = j = 0
    s = list(map(int, s))
    n = len(s)
    #print(s)
    while i < n:
        print(j, i)
        if s[i] == 0:
            tmp0 += 1
        else:
            tmp1 += 1

        max1 = max(tmp1, max1)

        if tmp0 > k:
            if s[j] == 0:
                tmp0 -= 1
            else:
                tmp1 -= 1
            j += 1
        i += 1
    return max1




def solve(s):
    z,o= s.count('0'), s.count('1')
    n = len(s)
    if  z== n:
        print(0)
        return
    if o == n:
        print(0)
        return
    
    s = list(s)

    l, r = 0, z + 1
    #print(s)
    #print(l, r)
    ans = -1
    while l <= r:
        mid = (l+r) // 2
        #print("checking: ", mid)
        if o - ok(s,mid) <= mid:
            #print("worked!")
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    print(ans)
    

t = ni()
for _ in range(t):
    s = INP()
    solve(s)