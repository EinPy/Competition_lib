
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n = ni()

eve, bob = 0, 0
cnt = 1
eveTurn = True
fail = False
for i in range(n):
    print(eveTurn, eve, bob)
    x, y = [int(j) for j in INP().split('-')]
    if i == 0:
        z = x + y
        for k in range(z):
            cnt += 1
            if cnt % 2 == 0:
                eveTurn = not eveTurn
                cnt = 0
        if eveTurn:
            eve = x
            bob = y
        else:
            bob = x
            eve = y
        cnt += 1
        if cnt % 2 == 0:
            cnt = 0
            eveTurn = not eveTurn
    else:
        if (eveTurn and x == eve and y == bob) or (not eveTurn and x == bob and y == eve):
            pass
        else:
            if eveTurn:
                if x < eve or x > eve + 1:
                    fail = True
                    break
                elif y < bob or y > bob + 1:
                    fail = True
                    break
                eve = x
                bob = y
            else:
                if x < bob or x > bob + 1:
                    fail = True
                    break
                elif y < eve or y > eve + 1:
                    fail = True
                    break
                bob = x
                eve = y
            cnt += 1
            if cnt % 2 == 0:
                cnt = 0
                eveTurn = not eveTurn
if not fail:
    print('ok')
else:
    print(f'error {i}')