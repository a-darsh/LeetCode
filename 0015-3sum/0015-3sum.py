class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums = sorted(nums)
        ans = []
        for i in range(n-2):
            l,r = i+1, n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            while(l<r):
                if nums[i]+nums[l]+nums[r]==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    r-=1
                    while (nums[r]==nums[r+1] and l<r):
                        r-=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return ans