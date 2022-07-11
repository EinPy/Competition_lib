import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve():
    s = list(INP())
    org = s[:]
    p = ni()
    s.sort()
    #print(s)
    value = 0
    for l in s:
        value += ord(l) - ord('a') + 1
    
    if value <= p:
        return ''.join(org)
    if p == 0:
        return ''
    
    rem = {}
    while value > p:
        value -= ord(s[-1]) - ord('a') + 1
        if s[-1] not in rem:
            rem[s[-1]] = 1
        else:
            rem[s[-1]] += 1
        s.pop()
        
    out = []
    for l in org:
        if l not in rem:
            out.append(l)
        else:
            if rem[l] == 0:
                out.append(l)
            else:
                rem[l] -= 1
    #print(org)
    return ''.join(out)
    
        


t = ni()
for case in range(t):
    print(solve())
    
    