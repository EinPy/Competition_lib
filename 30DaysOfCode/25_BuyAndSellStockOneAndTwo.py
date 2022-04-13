#solution to https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

def maxProfit(prices):
    curMin, curMax = 10**6, 0
    bestDiff = 0
    
    for i in range(len(prices)):
        if prices[i] < curMin:
            curMin = prices[i]
            curMax = 0

        curMax = max(curMax, prices[i])
        if curMax != curMin:
            bestDiff =  max(bestDiff,curMax - curMin)
    
    return bestDiff


def maxProfit2(prices):       
    profit = 0
    buyPrice = -1
    
    for i in range(len(prices)-1):
        if prices[i+1] < prices[i]:
            if buyPrice != -1:
                profit += prices[i] - buyPrice
                buyPrice = -1
        if prices[i+1] > prices [i]:
            if buyPrice == -1:
                buyPrice = prices[i]
                
    if buyPrice != -1:
        profit += prices[-1] - buyPrice
                
    return profit