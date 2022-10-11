import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



i = ni()
for _ in range(i):
    a, b = INP().split(" ")
    if a[-1] == "S":
        if b[-1] == "L" or b[-1] == "M":
            print("<")
        elif len(a) == len(b):
            print("=")
        elif len(a) > len(b):
            print("<")
        else:
            print(">")
    if a[-1] == "M":
        if b == "M":
            print("=")
        if b[-1] == "L":
            print("<")
        if b[-1] == "S":
            print(">")
    if a[-1] == "L":
        if b[-1] == "S" or b[-1] == "M":
            print(">")
        else:
            if len(a) == len(b):
                print("=")
            if len(a) > len(b):
                print(">")
            if len(b) > len(a):
                print("<")