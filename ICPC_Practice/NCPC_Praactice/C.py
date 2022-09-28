import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


import math

t = ni()
cubes = []
cyls = []
for _ in range(t):
    a, b = INP().split()
    if a == "cube":
        cubes.append(int(b))
    else:
        cyls.append(int(b))
    
out = [("dummy", 1e5)]
cubes.sort(reverse=True)
cyls.sort(reverse=True)

imp = [[-1 for _  in range(len(cubes)+2)] for _ in range(len(cyls)+2)]

def rec(iCy,iCu, out):
    print("call", iCy, iCu, out, imp)
    if imp[iCy][iCu] == 0:
        return False
    if out == []:
        outA = [(cubes[iCu], 0)]
        outB = [(cyls[iCy], 1)]
        rec(iCy, iCu -1, outA)
        rec(iCy -1, iCu, outB)
    if iCy == -1 and iCu == -1:    
        out.reverse()
        for i in out:
            if i[1] == 0:
                print("cube", i[0])
            else:
                print("cylinder", i[0])
        return True
    else:
        one = False
        print(out)
        print(out[-1])
        if out[-1][1] == 0: #cube
            if iCy != -1 and 2 * cyls[iCy] <=  out[-1][0]:
                rec(iCy -1, iCu, out + [(cyls[iCy], 1)])
                one = True
            if iCu != -1 and cubes[iCu] <=  out[-1][0]:
                rec(iCy, iCu-1, out + [(cubes[iCu], 0)])
                one = True
        else:#cyl
            if iCy != -1 and cyls[iCy] <=  out[-1][0]:
                rec(iCy -1, iCu, out + [(cyls[iCy], 1)])
                one = True
            if iCu != -1 and math.sqrt(2) * cubes[iCu] <=  2 * out[-1][0]:
                rec(iCy, iCu-1, out + [(cubes[iCu], 0)])
                one = True
        if one == False:
            imp[iCy][iCu] = 0
            return False
            
if rec(len(cyls)-1, len(cubes)-1, []) == False:
    print("impossible")
    