import string
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)



def solve(changes):
    t = -30
    oc = 0
    ox = 0
    for c in changes:
        if "temperature" in c:
            t += int(c[-1])
        if "oxygen" in c:
            ox += int(c[-1])
        if "ocean" in c:
            oc += int(c[-1])
    if t >= 8 and oc >= 9 and ox >= 14:
        print("liveable", end = "")
    else:
        print("not liveable", end = "")


N = int(input())
changes = []

for i in range(N):
    changes.append(input())
    
solve(changes)
