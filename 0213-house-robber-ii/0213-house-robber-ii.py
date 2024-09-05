class Solution:
    def rob(self, nums: List[int]) -> int:
    
        
        def robSimple(nums):
            prev0, prev1 = 0,0
            for n in nums:
                temp = max(n+prev0, prev1)
                prev0, prev1 = prev1, temp
            return prev1
        
        return max(nums[0],robSimple(nums[1:]), robSimple(nums[:-1]))