class Solution(object):
    def twoSum(self, nums, target):
        
        hMap = {}
        
        for i, val in enumerate(nums):
          
          if target-val in hMap:
            return hMap[target-val], i
          
          hMap[val] = i