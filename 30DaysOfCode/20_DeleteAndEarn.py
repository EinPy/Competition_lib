#dynamic programming solution to: https://leetcode.com/problems/delete-and-earn/


def deleteAndEarn(nums):
    big = max(nums)
    
    dp = [0 for _ in range(big+1)]
    
    for n in nums:
        dp[n] += n
        
    for i in range(2, big+1):
        dp[i] = max(dp[i-1], dp[i-2] + dp[i])
        
    return dp[big]