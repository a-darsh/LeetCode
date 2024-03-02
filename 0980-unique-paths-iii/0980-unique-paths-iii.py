class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        empty = 0
        start=end=(0,0)
        for i in range(m):
            for j in range(n):
                
                if grid[i][j]==1:
                    start = (i,j)
                
                if grid[i][j]==2:
                    end = (i,j)
                    
                if grid[i][j]==0:
                    empty+=1
                    
        visited = set()
        walk = 0
        self.ans=0
        def dfs(r,c,visited, walk):
            
            if (r,c)==end:
                if walk ==empty+1:
                    self.ans+=1
                return
            
            if 0<=r<m and 0<=c<n and grid[r][c]!=-1 and (r,c) not in visited:
                visited.add((r,c))
                for i,j in [(0,1),(0,-1), (1,0), (-1,0)]:
                    dfs(r+i,c+j, visited, walk+1)
                visited.remove((r,c))
            
            
        dfs(start[0], start[1], visited, walk)    
        
        return self.ans
                
                