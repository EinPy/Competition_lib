import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,s):
    let = list(s)
    #print(let)
    d = {}
    used = {}
    rev = {}
    #lexographic size is determined in order from first to last
    #always set a to the first character in the string, unless it is a
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    out = []
    cnt = 0
    for l in let:
        if l not in d:
            if len(d) == 25:
                for cha in alph:
                    if cha not in used:
                        d[l] = cha
            else:
                for j in alph:
                    if  j != l and j not in used:
                        go = True
                        if l in rev:
                            p = rev[l]
                            if p == j:
                                go = False
                            while p in rev:
                                p = rev[p]
                                if p == j:
                                    go = False
                        if go:
                            d[l] = j
                            rev[j] = l
                            used[j] = True
                            cnt += 1
                            break
                #print(d, rev)
    
    out = []
    #print(d)
    for l in let:
        out.append(d[l])
        #print(out)
    print(''.join(out))

    


t = ni()
for case in range(t):
    n = ni()
    s = INP()
    solve(n,s)