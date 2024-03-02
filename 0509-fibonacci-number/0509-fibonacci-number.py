class Solution:
    def fib(self, n: int, hmap = {}) -> int:
        
        if n in hmap:
            return hmap[n]
        
        if n==0:
            return 0
        if n==1:
            return 1
        
        hmap[n] = self.fib(n-1) + self.fib(n-2)
        
        return hmap[n]