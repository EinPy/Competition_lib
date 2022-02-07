

import sys

def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
#setupInputOutputSublime()
from math import sqrt

itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#solution to https://codeforces.com/problemset/problem/1527/B1
def solve(s):
    #modeling approach
    s = list(s)
    Al = 0
    Bob = 0
    turn = 1
    isPal = True
    canRev = False
    lastAdd = None
    print(s)
    if len(s) == 1:
        if s[0] == '0':
            print("BOB")
        else:
            print("DRAW")
        return
    if len(s) % 2 != 0:
        odd = True
    else:
        odd = False
    while len(s) != s.count('1'):
        if canRev:
            s = s[::-1]
            turn += 1
            canRev = False
        else:
            if turn == 1 and odd:
                mid = (len(s) // 2)
                s[mid] = '1'
                isPal = True
                canRev = False
                turn += 1
            else:
                if lastAdd:
                    s[lastAdd] = '1'
                    if turn % 2 == 0:
                        Bob += 1
                    else:
                        Al += 1
                    lastAdd = None
                    canRev = True
                    turn += 1
                else:
                    next0 = s.index('0')
                    s[next0] = '1'
                    if turn % 2 == 0:
                        Bob += 1
                    else:
                        Al += 1
                    lastAdd = next0
                    canRev = True
                    turn += 1
    print(Al, Bob)
    if Al > Bob:
        print("ALICE")
    elif Bob > Al:
        print("BOB")
    else:
        print("DRAW")

def solve2(s):
    #mathematical approach
    n = s.count('0')
    if n == 0:
        print("DRAW")
    elif n == 1:
        print("BOB")
    elif n%2 == 0:
        print("BOB")
    else:
        print("ALICE")


T = int(input())
for i in range(T):
    n = int(input())
<<<<<<< HEAD:30DaysOfCodeforces/03_Palindrome_Game.py
    s = list(map(int,input().split()))
=======
    s = input()
>>>>>>> 152a69b571cf69734b9210a897099d72c333d21e:30DaysOfCodeforces/04_Palindrome_Game.py
    solve2(s)