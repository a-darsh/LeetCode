class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        stack = sorted([(x,i) for i,x in enumerate(nums)], reverse=True)
        best  = 0
        for i,x in enumerate(nums):
            while stack and x>stack[-1][0]:
                y,j = stack.pop()
                best  = max(best, j-i+1)
        
        return best