import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def st(s, c):
    
    alph =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    def solve(s, c):
        #Can always be split into separate parts. 
        if len(s) == 1:
            if s[0] != c: return 1
            else: return 0
        mid = len(s) // 2
        #cost to make the left side c+1 good
        cntl = solve(s[:mid], alph[alph.index(c)+1])
        #cost to make the right side c good 
        cntl += len(s) / 2 - s[mid:].count(c)
        #cost to make the right side c+ 1 good
        cntr = solve(s[mid:], alph[alph.index(c) + 1])
        #cost to make the left siide c good
        cntr += len(s) / 2 - s[:mid].count(c)
        return min(cntl, cntr)

    return int(solve(s, c))


t = ni()
for case in range(t):
    n = ni()
    s = INP()
    print(st(s, 'a'))