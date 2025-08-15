class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        
        #prefix
        prefix = 1
        for i in range(n):
            res[i]*=prefix
            prefix*=nums[i]
        
        #suffix
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i]*=suffix
            suffix*=nums[i]
        
        return res

        #O(N), O(1)- excluding the output array