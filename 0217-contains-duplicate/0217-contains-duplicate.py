class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      hMap = {}
      for i in range(len(nums)):
        if nums[i] in hMap:
          return True
        hMap[nums[i]] = i
      return False
        