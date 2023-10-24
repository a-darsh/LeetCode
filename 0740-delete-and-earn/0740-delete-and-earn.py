class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        
        nums = sorted(list(set(nums)))
        
        earn1, earn2 = 0, nums[0]*count[nums[0]]
        
        for i in range(1, len(nums)):
          
          if nums[i-1] != nums[i]-1:
            temp = earn2 + nums[i]*count[nums[i]]
            earn1, earn2 = earn2, temp
            
          else:
            temp = max(nums[i]*count[nums[i]] + earn1, earn2)
            earn1, earn2 = earn2, temp
            
        
        return earn2
            
          