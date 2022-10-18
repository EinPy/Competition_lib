import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

#solution to https://cses.fi/problemset/result/4832924/


n, x = nl()
price = nl()
page = nl()
#typical knapsack dp
#determine for each weight determine the maximal value
dp = [[0 for _ in range(x + 2)] for _ in range(n + 2)]
#rows are items, cols are total price
#top row is 0 items, thus empty and all zeroes
best = 0
for item in range(1,n+1):
    for cost in range(x+1):
        #we can always choose to not buy the book
        dp[item][cost] = dp[item-1][cost]
        left = cost - price[item-1]
        if left >= 0:
            #if we have enough money to buy book:
            #the best value with totCost amount of money, is either not buying the book, and
            #having bought the previous book, or buying the book, and allocating the remainding funds to 
            #previous books
            dp[item][cost] = max(dp[item][cost], dp[item-1][left] + page[item-1])
            
print(dp[n][x])