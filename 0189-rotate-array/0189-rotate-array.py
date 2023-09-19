class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def rotateHelp(i,j, li):
          
          while i<j:
            li[i], li[j] = li[j], li[i]
            i+=1
            j-=1
            
          return li
        
        l = len(nums)
        
        k = k%l
        
        nums = rotateHelp(0,l-1, nums)
        nums = rotateHelp(0,k-1, nums)
        nums = rotateHelp(k,l-1, nums)
        
          
          
        