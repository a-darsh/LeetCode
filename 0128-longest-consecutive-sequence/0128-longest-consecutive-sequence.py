class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        resStreak = 0
        numSet = set(nums)
        for n in numSet:
            if n-1 not in numSet:
                curNum = n
                curStreak = 1
                while curNum+1 in numSet:
                    curStreak+=1
                    curNum+=1
                resStreak = max(resStreak, curStreak)
        return resStreak

        #O(N), O(N)