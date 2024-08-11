class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for n in nums:
            if n in hmap:
                return True
            hmap[n]=1
        return False
        