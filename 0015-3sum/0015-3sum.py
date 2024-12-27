class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #ans = []
        seen = set()
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]>0:
                break
            j,k = i+1, len(nums)-1
            while (j<k):
                s = nums[i]+nums[j]+nums[k]
                if s==0 and (nums[i],nums[j],nums[k]) not in seen:
                    #ans.append([nums[i],nums[j],nums[k]])
                    seen.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif s<0:
                    j+=1
                else:
                    k-=1
                    
        return list(seen)
                
                
            