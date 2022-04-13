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