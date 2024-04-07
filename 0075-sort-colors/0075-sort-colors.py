class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        
        l,i,r = 0,0,len(nums)-1
        
        while(i<=r):
            if nums[i]==0:
                nums[i], nums[l] = nums[l], nums[i]
                l+=1
            elif nums[i]==2:
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
                i-=1
            i+=1
                
                
            
        
        
#         hmap = defaultdict(int)
#         for i in range(len(nums)):
#             hmap[nums[i]] += 1
        
#         for i in range(len(nums)):
#             if hmap[0]:
#                 nums[i]=0
#                 hmap[0]-=1
#             elif hmap[1]:
#                 nums[i]=1
#                 hmap[1]-=1
#             else:
#                 nums[i]=2
#                 hmap[2]-=1

                
        
        