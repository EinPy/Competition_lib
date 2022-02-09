import sys

def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("D:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("D:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()
from math import sqrt

itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code starts here

def solve(hay):
    moves = 0
    Cs = 0  
    for i in range(len(hay)-1,-1,-1):


hay = input()
print(hay)
solve(hay)