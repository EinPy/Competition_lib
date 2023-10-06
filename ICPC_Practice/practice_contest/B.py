import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nf(): return float(INP())
def nl(): return [float(_) for _ in INP().split()]
import math


bulls_eye, bull, innerTrip, outerTrip, innerDoub, outerDoub = nl()
std_dev = nf()


# #integral 0 -> 2pi 0 - r evaluates to 
# def calc(r_0, r_1, sigma):
#     return (1 / sigma ** 2) * (math.sqrt(math.pi) / 2) * (math.erf(r_1 / (math.sqrt(2) * sigma)) - math.erf(r_0 / (math.sqrt(2) * sigma)))

def calc(r_0, r_1, sigma):
    return - (math.exp(-r_1**2 / (2 * sigma ** 2))  - math.exp(-r_0**2 / (2 * sigma ** 2)))


EV = 0

#inner bulleye
EV += calc(0,bulls_eye, std_dev) * 50
#bull
EV += calc(bulls_eye, bull, std_dev) * 25
#normal points
EV += calc(bull,innerTrip, std_dev) * 10.5
#trip
EV += calc(innerTrip, outerTrip, std_dev) * 31.5
#norm
EV += calc(outerTrip, innerDoub, std_dev) * 10.5
#doub
EV += calc(innerDoub, outerDoub, std_dev) * 21



n, d, t = 0,0,0
for i in range(1,21):
    n += i
    d += i * 2
    t += i * 3
#print(n / 20, d / 20, t / 20)


#print(calc(0,10000,17))
print(EV)