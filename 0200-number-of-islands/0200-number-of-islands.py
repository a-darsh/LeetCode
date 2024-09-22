class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m,n = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(i,j):
            if (i,j) not in visited and grid[i][j]=="1":
                visited.add((i,j))
                for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
                    r,c = i+di, j+dj
                    if 0<=r<m and 0<=c<n and grid[r][c]=="1":
                        dfs(r,c)
            return
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]=="1":
                    islands+=1
                    dfs(i,j)
        
        return islands
        
        
        