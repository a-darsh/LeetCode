class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        
        stack = sorted([(x,i) for i,x in enumerate(nums)], reverse=True)
        maxLen = 0
        for i,x in enumerate(nums):
            while stack and stack[-1][0]<x:
                y, j = stack.pop()
                maxLen = max(maxLen, j-i + 1)
        
        return maxLen