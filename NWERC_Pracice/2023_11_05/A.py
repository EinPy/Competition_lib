import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def solve(n,a):
    pass


while True:
    w, p, t = nl()
    if w == p == t == 0:
        break
    attacks = [] # strenght of attack at turn i
    #want to minimize army size, a production facility is always better 
    #than a worker? Or?
    #damn

    """
        4 workers, 3 factories, starting turn one then with 4 dollars?
        -> 4 workers, 7 factories, 4 armies end of turn 2
        -> 4 workers, 7 factories, 11 armies?
        >
    """
    #is this dp or somehow grundy number / MEX {XOR}?
    #greedy strategy=
    for i in range(
        
    )