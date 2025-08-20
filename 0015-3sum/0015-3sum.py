class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        L = len(nums)
        res = set()
        for i, n in enumerate(nums):
            j=i+1
            k=L-1
            while j<k:
                if nums[j]+nums[k]+n==0 and (n,nums[j],nums[k]) not in res:
                    res.add((n,nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[j]+nums[k]+n<0:
                    j+=1
                else:
                    k-=1
        return list(res)
        #O(N), O(N)