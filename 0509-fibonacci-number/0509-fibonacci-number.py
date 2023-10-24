class Solution:
    def fib(self, n: int, memo = {}) -> int:
      
      #top down
      
      
      if n in memo:
        return memo[n]
      
      if n==0:
        memo[n] = 0 
        return 0
      
      if n==1:
        memo[n] = 1
        return 1
      
      memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
      return memo[n]
      
      
      
      
      
#         #bottom up - bottom is 0, top is n
        
#         one , two = 0,1
        
#         for i in range(2, n+1):
          
#           temp = two
#           two = one + two
#           one  = temp
        
#         return two if n > 0 else one
      
          
          
          
