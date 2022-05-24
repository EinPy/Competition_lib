import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, k , s):
    #for every substring the last of that substring and the first of the substring that begins at theat one
    #has to be the same. Since all substrings must, in fact, be equal
    cnt = Counter(s)
    if cnt['?'] == n:
        return "YES"
    s = list(s)
    #print(s)

    zs, os =0,0
    for i in range(k):
        c = -1
        for j in range(i, n, k):
            if s[j] != '?':
                if c != -1 and s[j] != c:
                    return "NO"
                if c == -1:
                    c = s[j]

        if c != -1:
            if c == '1': os += 1
            if c == '0': zs += 1
    #print(zs, os)
    
    if max(zs, os) <= k / 2:
        return "YES"
    return "NO"

t = ni()
for case in range(t):
    n,k = nl()
    s = INP()
    print(solve(n, k , s))