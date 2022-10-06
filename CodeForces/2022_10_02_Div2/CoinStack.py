import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


from heapq import heappush, heappop
c = ni()
a = nl()
sa = sum(a)
ma = max(a)

heap = []
heappush(heap,(-1 * a[0], 1))

for i in range(1,c):
    heappush(heap, (-1 * a[i], i+1))
    
    
if sa - ma >= ma and  sa % 2 == 0:
    l , r = 0, c -1
    outL = []
    outR = []

    while True:


        v, il = heappop(heap)
        v2, ir = heappop(heap)

        #print(v, il, v2, ir)
        if v == v2 and v == 0:
            possible = True
            break
        elif v != v2 and v == 0 or v2 == 0:
            possible = False
            print("no")
            break
        else:
            v += 1
            v2 += 1
            
            outL.append(il)
            outR.append(ir)
            
            heappush(heap,(v, il))
            heappush(heap,(v2, ir))
    if possible:
        print("yes")
        for i in range(len(outL)):
            print(outL[i], outR[i])
else:
    print("no")