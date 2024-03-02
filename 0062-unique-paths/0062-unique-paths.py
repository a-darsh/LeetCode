class Solution:
    def uniquePaths(self, m: int, n: int, hmap = {}) -> int:
        
        if (m,n) in hmap:
            return hmap[(m,n)]
        
        if m==0 or n==0:
            return 0
        
        if m==1 and n==1:
            return 1
        
        hmap[(m,n)] = self.uniquePaths(m-1,n, hmap) + self.uniquePaths(m, n-1, hmap)
        
        return hmap[(m,n)]