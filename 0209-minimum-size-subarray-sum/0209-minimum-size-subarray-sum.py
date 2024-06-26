class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        curSum = 0
        ans = float('inf')
        for r in range(len(nums)):
            curSum+=nums[r]
            while curSum>=target:
                ans = min(ans, r-l+1)
                curSum-=nums[l]
                l+=1
        return ans if ans!=float('inf') else 0
        