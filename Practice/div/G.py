import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, e = nl()
a = nl()
a.append(n + 1)
a.append(0)
a.sort()

e = []
c = []



for i in range(len(a)-1):
    d = a[i+1] - a[i]
    if d >= 2:
        c.append([a[i]+1, a[i+1]-1])
        
d = c[0][0]
if d >= 2:
    e.append([1, d-1])
for i in range(len(c)-1):
    d = c[i+1][0] - c[i][1]
    if d >= 2:
        e.append([c[i][1]+1, c[i+1][0]-1])
d = n + 1 - c[-1][1]
#print(n+1, c[-1][-1])

if d >= 2:
    e.append([c[-1][1]+1, n])


outE = []
for i in range(len(e)):
    if i == len(e)-2 and len(e) > 1:
        if e[i][0] == e[i][1]:
            outE.append(f"{e[i][0]}")
        else:
            outE.append(f"{e[i][0]}-{e[i][1]}")
        outE.append("and")
    elif i == len(e) -1:
        if e[i][0] == e[i][1]:
            outE.append(f"{e[i][0]}")
        else:
            outE.append(f"{e[i][0]}-{e[i][1]}")
    else:
        if e[i][0] == e[i][1]:
            outE.append(f"{e[i][0]},")
        else:
            outE.append(f"{e[i][0]}-{e[i][1]},")


outC = []
for i in range(len(c)):
    if i == len(c)-2 and len(c) > 1:
        if c[i][0] == c[i][1]:
            outC.append(f"{c[i][0]}")
        else:
            outC.append(f"{c[i][0]}-{c[i][1]}")
        outC.append("and")
    elif i == len(c) -1:
        if c[i][0] == c[i][1]:
            outC.append(f"{c[i][0]}")
        else:
            outC.append(f"{c[i][0]}-{c[i][1]}")
    else:
        if c[i][0] == c[i][1]:
            outC.append(f"{c[i][0]},")
        else:
            outC.append(f"{c[i][0]}-{c[i][1]},")

    
print("Errors:", end = " ")
print(' '.join(outE))
print("Correct:", end = " ")
print(' '.join(outC))