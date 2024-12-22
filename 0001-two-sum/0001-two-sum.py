class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        for i, n in enumerate(nums):
            rem = target - n
            if rem in hmap:
                return [hmap[rem],i]
            hmap[n]=i
        
        # TC: O(n), SC: O(n)