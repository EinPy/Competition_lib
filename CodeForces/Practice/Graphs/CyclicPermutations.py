#https://codeforces.com/problemset/problem/1391/C
import math
n = int(input())
d = 1
num = 1
mod = 10**9 + 7
#print((math.factorial(n) - 2**(n-1)) % (10**9 + 7))
for i in range(1, n):
    num *= i
    d *= 2
    num %= mod
    d %= mod
num *= n
num %= mod
#print(num, type(num))
num -= d
num %= mod
if num <= 0 : num += mod
print(num)

