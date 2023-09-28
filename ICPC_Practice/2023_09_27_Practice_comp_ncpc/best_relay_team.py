import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n = ni()
rnsF = []
rnsO = []
for _ in range(n):
    na, a,b = INP().split()
    rnsF.append((float(a),float(b),na))
    rnsO.append((float(b),float(a),na))
    
rnsF.sort()
rnsO.sort()
best = 1e9
rns = []
if n > 4:
    for i in range(5):
        r = []
        t = 0
        t += rnsF[i][0]
        r.append(rnsF[i][2])
        leg = 0
        for j in range(5):
            if leg == 3:
                break 
            if rnsO[j][2] != rnsF[i][2]:
                t += rnsO[j][0]
                leg += 1
                r.append(rnsO[j][2])
        if t < best:
            rns = r
            best = t
else:
    for i in range(4):
        r = []
        t = 0
        t += rnsF[i][0]
        r.append(rnsF[i][2])
        for j in range(4):
            if rnsO[j][2] != rnsF[i][2]:
                t += rnsO[j][0]
                r.append(rnsO[j][2])
        if t < best:
            best = t
            rns = r


print(best)
for l in rns:
    print(l)