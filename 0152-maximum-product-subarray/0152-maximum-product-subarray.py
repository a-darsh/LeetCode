class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax, curmin = 1, 1
        res = max(nums)
        for n in nums:
            temp = n*curmax
            curmax = max(n*curmax, n*curmin, n)
            curmin = min(temp, n*curmin, n)
            res = max(curmax, curmin, res)
        return res