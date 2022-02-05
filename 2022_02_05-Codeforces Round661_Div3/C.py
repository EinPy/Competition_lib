import sys
import statistics as stat

def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("D:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("D:\\Temp\\input.txt", mode = 'r')
#setupInputOutputSublime()
from math import sqrt

itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def solve(w):
    w.sort()
    s = stat.median(w) * 2
    p1, p2 = 0, len(w) - 1
    teams = 0
    while p1 < p2:
        tot = w[p1] + w[p2]
        if tot == s:
            teams += 1
            p1 += 1
            p2 -= 1
        else:
            if tot > s:
                p2 -= 1
            else:
                p1 += 1
    return teams


def solve2(w):
    hashT = {}
    tot = 0
    for i in range(len(w)):
        for j in range(i+1, len(w)):
            tot = w[i] + w[j]
            if tot not in hashT:
                hashT[tot] = [1, [i, j]]
            else:
                if i not in hashT[tot][1] and j not in hashT[tot][1]: 
                    hashT[tot][0] += 1
                    hashT[tot][1].append(i)
                    hashT[tot][1].append(j)
    curMax = 0
    for key in hashT.keys():
        curMax = max(curMax, hashT[key][0])
    return curMax



T = int(input())
for i in range(T):
    n = int(input())
    w = list(map(int,input().split()))
    print(solve2(w))
