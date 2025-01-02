class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0, len(nums)
        while(i<j):
            if nums[i]==target:
                return i
            elif nums[i]<target:
                i+=1
            else:
                j-=1
        return -1

        #O(logn), O(1)

