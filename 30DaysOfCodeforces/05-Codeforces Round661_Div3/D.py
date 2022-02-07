import sys

def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("D:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("D:\\Temp\\input.txt", mode = 'r')
#setupInputOutputSublime()
from math import sqrt

itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def kp(elem):
    return int(elem[0])

def solve(s):
    ss = []
    remains = []
    for i, c in enumerate(s):
        remains.append((c,i))
    while len(remains) > 0:
        if max(remains, key=kp) == min(remains, key=kp):
            for i in range(len(remains)):
                ss.append([remains[i]])
            break
        newR = []
        newSub = []
        i = 0
        while i < len(remains):
            if i == 0:
                newSub.append(remains[i])
                i += 1
            else:
                if remains[i-1][0] != remains[i][0]:
                    newSub.append(remains[i])
                    i += 1
                else:
                    newR.append(remains.pop(i))
        remains = newR[:]
        ss.append(newSub)
    return ss


def solve2(s):
    current = []
    remains = []
    substrings = []

    for i, c in enumerate(s):
        current.append((c,i))

    i = 0
    j = 1
    newSub = [current[0]]
    while True:
        while j < len(current):
            if current[i][0] != current[j][0]:
                newSub.append(current[j])
                i = j
                j += 1

            else:
                remains.append(current[j])
                j += 1

        substrings.append(newSub)
        current = remains

        if max(remains, key=kp) == min(remains, key=kp):
            for i in range(len(remains)):
                substrings.append([remains[i]])
            break


def solve3(s):
    end1 = []
    end0 = []
    ans = [None for _ in range(len(s))]

    for i in range(len(s)):
        newPos = len(end0) + len(end1)
        if s[i] == '0':
            if end1 == []:
                end0.append(newPos)
            else:
                newPos = end1[-1]
                end1.pop()
                end0.append(newPos)
        else:
            if end0 == []:
                end1.append(newPos)
            else:
                newPos = end0[-1]
                end0.pop()
                end1.append(newPos)

        ans[i] = newPos + 1
    
    print(len(end0) + len(end1))
    print(" ".join(list(map(str, ans))))



T = int(input())
for i in range(T):
    n = int(input())
    s = input()
    ss = solve3(s)