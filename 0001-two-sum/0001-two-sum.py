class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        for i, num in enumerate(nums):
            dif = target-num
            if dif in hmap:
                return [hmap[dif],i]
            hmap[num]=i