class Solution:
    def rob(self, nums: List[int]) -> int:
        prev0, prev1 = 0, 0
        
        for n in nums:
            temp = max(n+prev0, prev1)
            prev0, prev1 = prev1, temp
        return temp