class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b,s = 0, 1
        maxP = 0
        
        while s <len(prices):
          prof = prices[s] - prices[b]
          
          if prof>0:
            if prof>maxP:
              maxP = prof
            s+=1
          
          else:
            b = s
            s += 1
            
        return maxP