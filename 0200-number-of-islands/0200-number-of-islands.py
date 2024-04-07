class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m,n  = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r,c):
            if (r,c) in visited or grid[r][c]=='0':
                return 
            visited.add((r,c))
            for i,j in [[1,0], [-1,0], [0,1], [0,-1]]:
                rd, cd = r+i, c+j
                if 0<=rd<m and 0<=cd<n and grid[rd][cd]=='1' and (rd,cd) not in visited:
                    dfs(rd,cd)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] =='1' and (i,j) not in visited:
                    islands+=1
                    dfs(i,j)
                    
        return islands