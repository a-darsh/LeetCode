class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in checkSet:
                return True
            seen.add(num)
        return False
        #O(N), O(N)
        