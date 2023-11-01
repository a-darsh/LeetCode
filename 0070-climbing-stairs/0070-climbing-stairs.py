class Solution:
    def climbStairs(self, n: int, map = {}) -> int:
        
        if n in map:
            return map[n]
        
        if n==1 or n==0:
            return 1
        
        if n<0:
            return 0
        
        map[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return map[n]
            