class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m,n  = len(grid), len(grid[0]) 
        
        ans = 0
        visited = set()
        
        def dfs(r,c):
            visited.add((r,c))
            for i,j in [[0,1],[0,-1], [1,0], [-1,0]]:
                row, col=r+i, c+j
                if 0<=row<m and 0<=col<n and grid[row][col]=="1" and (row, col) not in visited:
                    dfs(row,col)
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]=="1":
                    ans+=1
                    dfs(i,j)
        return ans