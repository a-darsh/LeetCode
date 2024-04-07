class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m,n  = len(grid), len(grid[0])
        visited = set()
        num = 0
        def dfs(r,c):
            if (r,c) in visited:
                return
            visited.add((r,c))
            for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                rd, cd = r+i, c+j
                if 0<=rd<m and 0<=cd<n and grid[rd][cd]==0 and (rd,cd) not in visited:
                    dfs(rd,cd)
        
        for i in range(m):
            if grid[i][0]==0:
                dfs(i,0)
            if grid[i][n-1]==0:
                dfs(i,n-1)
        
        for j in range(n):
            if grid[0][j]==0:
                dfs(0,j)
            if grid[m-1][j]==0:
                dfs(m-1,j)
            
        
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j]==0 and (i,j) not in visited:
                    num+=1
                    dfs(i,j)
                    
        return num