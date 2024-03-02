class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def dfs(m,n, hmap={}):
            
            if (m,n) in hmap:
                return hmap[(m,n)]
            
            if obstacleGrid[m-1][n-1]==1:
                return 0
            
            if m==1 and n==1:
                return 1
            
            if m==0 or n==0:
                return 0
            
            hmap[(m,n)] = dfs(m-1,n, hmap) + dfs(m, n-1, hmap)
            
            return hmap[(m,n)]
        
        return dfs(len(obstacleGrid), len(obstacleGrid[0]))
            
        