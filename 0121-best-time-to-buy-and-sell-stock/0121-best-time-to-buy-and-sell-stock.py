class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit  = 0
        l = 0
        for r, p in enumerate(prices):
            if p>prices[l]:
                maxProfit = max(maxProfit, p-prices[l])
            else:
                l=r
        return maxProfit

        #O(N), O(1)