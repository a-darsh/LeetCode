class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        req = len(nums)//2
        hmap = {}
        for i in range(0, len(nums)):
            hmap[nums[i]] = hmap.get(nums[i],0)+1
            if hmap[nums[i]]>req:
                return nums[i]
            