class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float('inf')
        res = 0
        for p in prices:
            if p<minP:
                minP = p
            res = max(res, p-minP)
        return res
    


