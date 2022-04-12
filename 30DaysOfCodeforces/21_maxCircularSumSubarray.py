#solution to https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    # flips the problem, finds the subarray with the minimum sum
    #then the answer is the sum of the array - min_subarray
    #it works because you are finding the smallest subarray, and removing 
    #it from the array, which you can do since the array is circular
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums)
        curMax = subMax = -1e5
        curMin = subMin = 1e5
        tot = 0
        
        for i, v in enumerate(nums):
            curMax = max(curMax + v, v)
            subMax = max(subMax, curMax)
            
            curMin = min(curMin + v, v)
            subMin = min(curMin, subMin)
            
            tot += v
            
        if subMin == tot: return subMax
        return max(subMax, tot - subMin)