class Solution:
    def fib(self, n: int) -> int:
        
        #bottom up - bottom is 0, top is n
        
        one , two = 0,1
        
        for i in range(2, n+1):
          
          temp = two
          two = one + two
          one  = temp
        
        return two if n > 0 else one
          
          
          
