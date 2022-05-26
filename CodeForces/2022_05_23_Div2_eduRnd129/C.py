import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def bubble_sort(a1, a2):
    n = len(a1)
    moves = []

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the a1 that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if a1[j] > a1[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                a1[j], a1[j + 1] = a1[j + 1], a1[j]
                #swap for both arrays
                a2[j] ,a2[j+1] = a2[j+1], a2[j]
                moves.append((j+1,j+2))

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the a1 is already sorted, and you can terminate
        if already_sorted:
            break

    return a1, a2, moves


def seg_sort(array, l, r):
    n = len(array)
    #non inclusive
    r += 1
    moves = []

    for i in range(l, r):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(r - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]
                moves.append((j+1,j+2))
                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array, moves


def moves(m):
    if m == []:
        print(0)
    else:
        print(len(m))
        for l, r in m:
            print(l, r)

def solve(n, a, b):
    #first try sorting based on a
    Asor, Bsor, m = bubble_sort(a,b)
    segs = []
    p = 0
    while p < n-1:
        first = -1
        last = -1
        while p < n-1 and a[p] == a[p+1]:
            if first == -1:
                first = p+1
            p += 1
        last = p+1
        if first != -1:
            segs.append((first, last))
        p += 1
            
    #print(a,b,m,Asor,Bsor)
    srt = b[:]
    srt.sort()
    if Bsor == srt:
        #happned
        #print("HAP", Bsor, srt)
        moves(m)
        return
    bbSor = Bsor[:]
    m2 = []
    for l,r in segs:
        bbSor, m2 = seg_sort(Bsor,l, r)

    cop = bbSor[:]
    cop.sort()
    if bbSor == cop:
        total = m + m2
        moves(total)
    else:
        print(-1)
t = ni()
for case in range(t):
    n = ni()
    a = nl()
    b = nl()
    solve(n, a, b)