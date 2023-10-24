class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
          return nums[0]
        
        rob1, rob2 = nums[-1], 0
        
        for i in range(len(nums)-2, -1, -1):
          temp = max(rob1, nums[i]+rob2)
          rob1, rob2 = temp, rob1
          
        return rob1
      