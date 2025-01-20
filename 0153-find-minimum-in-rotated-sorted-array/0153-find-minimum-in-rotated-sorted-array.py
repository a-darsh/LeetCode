class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        res = float('inf')
        while(l<=r):
            if nums[r]>nums[l]:
                res = min(nums[l], res)
                break
            mid = (l+r)//2
            res = min(nums[mid], res)
            if nums[mid]>=nums[l]:
                l = mid+1
            else:
                r = mid-1
        return res