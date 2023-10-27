class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i, j, k = 0, len(nums)-1, 0
        
        while(i<=j):
          if (nums[i]==val and nums[j]!=val):
            nums[i] = nums[j]
            i += 1
            j -= 1
            k += 1
          
          elif nums[j]==val:
            j -= 1
            
          elif nums[i]!=val:
            i += 1
            k += 1
        
        return  k