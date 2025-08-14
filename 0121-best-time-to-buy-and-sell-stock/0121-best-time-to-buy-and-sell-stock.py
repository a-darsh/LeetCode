class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for price in prices:
            if price > buy:
                res = max(res, price - buy)
            else:
                buy = price
        return res
        # O(N), O(1)
