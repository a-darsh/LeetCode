class Solution(object):
    def twoSum(self, nums, target):
        
        hmap = {}
        
        for i,n in enumerate (nums):
          
          if (target-n) in hmap:
            return [hmap[target-n],  i]
          
          hmap[n] = i