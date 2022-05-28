import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def least_rotation(S):
    """Booth's algorithm."""
    S += S  # Concatenate string to it self to avoid modular arithmetic
    f = [-1] * len(S)  # Failure function
    k = 0  # Least rotation of string found so far
    for j in range(1, len(S)):
        sj = S[j]
        i = f[j - k - 1]
        while i != -1 and sj != S[k + i + 1]:
            if sj < S[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != S[k + i + 1]:  # if sj != S[k+i+1], then i == -1
            if sj < S[k]:  # k+i+1 = k
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k


def solve(a):
    n = len(a)
    #if starts with 0, must end with 1
    necks = []
    
    curRight = 0
    look = True
    while look:
        i = n
        while i >= curRight:
            if least_rotation(a[curRight:i]) == 0:
                necks.append(a[curRight:i])
                #print(a[curRight:i])
                curRight = i
                break
            i -= 1
        if curRight == n:
            break
    for ne in necks: print(f"({ne})", end = "")
    print()
                
    
#print(least_rotation("0101"))


t = ni()
for case in range(t):
    a = INP()
    solve(a)