class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}
        for i, num in enumerate(nums):
            if target-num in seenMap:
                return [seenMap[target-num], i]
            seenMap[num]=i
        #O(N), O(N)
