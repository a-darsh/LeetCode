class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = {}
        total = 0
        for i,n in enumerate(nums):
            total+=n
            rem = total%k
            if rem==0 and i>0:
                return True
            if rem not in hmap:
                hmap[rem]=i
            elif i-hmap[rem]>1:
                return True
        return False
        