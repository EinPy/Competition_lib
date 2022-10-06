import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



a = INP()
b = INP()

a1 = a.count("S")
b1 = b.count("S")
ans = a1 * b1
out =[]

out.append("S(" * ans)
    
out.append("0")
out.append(")"*ans)
print(''.join(out))
