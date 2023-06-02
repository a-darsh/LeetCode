class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        l = len(nums)
        
        subNum = [1] * l
        
        for i in range(l-1, -1, -1):
          for j in range(i+1, l):
            
            if nums[i] < nums[j]:
              subNum[i] = max(subNum[i], 1 + subNum[j])
              
        return max(subNum)
            
        