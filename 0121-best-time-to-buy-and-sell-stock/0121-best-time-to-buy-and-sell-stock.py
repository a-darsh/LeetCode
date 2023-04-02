class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      l,r = 0,0
      mp = 0
      while(r < len(prices)):
        dif = prices[r] - prices[l]
        if(dif > mp):
          mp = dif
  
        if(dif < 0):
          l = r
        
        r = r+1
          
      return mp