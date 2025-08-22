class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0
        for sell in range(len(prices)):
            if prices[sell]<prices[buy]:
                buy=sell
            else:
                maxProfit = max(maxProfit, prices[sell]-prices[buy])
        return maxProfit
        #O(N), O(1)