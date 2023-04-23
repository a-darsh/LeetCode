class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1:
          return 0
        
        l, r = 0, 1
        maxp = 0
        while(r<len(prices)):
          if(prices[r] > prices[l]):
            maxp = max(maxp, (prices[r] - prices[l]))
            
          else:
            l = r
          r += 1
        return maxp
        
        