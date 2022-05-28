import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def bfs(look, m, peop):
    q = m
    vis = {m: True}
    while q in look:
        #print(q)
        vis[q] = True
        if peop[look[q]] == 'u':
            return True
        elif peop[look[q]] == '?' and look[q] not in vis:
            q = look[q]
        else:
            break
    return False    
        

def solve(peop,look, married):
    #old approach
    """
    while married:
        m = married[0]
        #print(married)
        if m in look and peop[look[m]] == '?':
            if look[m] in look:
                peop[look[m]] = 'm'
                married.append(look[m])
        married.pop(0)
    """
    #print(look)
    for m in married:
        if m in look and peop[look[m]] == '?':
            if bfs(look, m, peop):
                print(1)
                return
        
    #This condition is not true
    """
    qs = []
    for k in peop.keys():
        if peop[k] == '?':
            qs.append(k)

    while qs:
        q = qs[0]
        if q in look and peop[look[q]] == 'u':
            peop[q] = 'u'
            if q in revlook:
                for looking in revlook[q]:
                    if peop[looking] == '?':
                        qs.append(looking)
        qs.pop(0)
    """
        
    #print(peop)
    check(peop,look)
    

def check(peop,look):
    marrToUnmarr = False
    undecided = False
    for p in peop.keys():
        #print(p)
        if p in look:
            #print(p, look[p])
            if peop[look[p]] == 'u':
                if peop[p] == 'm':
                    marrToUnmarr = True
                if peop[p] == '?':
                    undecided = True
            if peop[look[p]] == '?':
                if peop[p] == '?':
                    undecided = True
                if peop[p] == 'm':
                    undecided = True
                
    
    if marrToUnmarr:
        print(1)         
    elif undecided:
        print("?")
    else:print(0) 

N, L = nl()
married = []
peop = {}
look = {}
revlook ={}
for c in range(N):
    name, s = INP().split()
    if s == 'm':
        married.append(name)
    peop[name] = s
for l in range(L):
    p1, p2 = INP().split("->")
    p1 = p1.replace(" ", "")
    p2 = p2.replace(" ", "")
    look[p1] = p2
#print(peop)
#print(look)
solve(peop,look, married)
    