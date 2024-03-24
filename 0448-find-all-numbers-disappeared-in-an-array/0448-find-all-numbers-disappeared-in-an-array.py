class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i
        
        ans = []
        for i in range(1, len(nums)+1):
            if i not in hmap:
                ans.append(i)
        
        return ans
        