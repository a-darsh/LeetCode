class Solution:
    def fib(self, n: int) -> int:
        
        f = {}
        
        if n in f:
          return f[n]
        
        if n==0:
          f[0] = 0
          return f[0]
        
        if n == 1:
          f[1] = 1
          return f[1]
        
        return self.fib(n-1) + self.fib(n-2)
