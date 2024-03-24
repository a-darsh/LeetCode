class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i
        
        for check in range(0, len(nums)+1):
            if check not in hmap:
                return check
        