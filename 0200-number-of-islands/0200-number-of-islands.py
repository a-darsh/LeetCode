class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m,n  = len(grid), len(grid[0])
        visited = set()
        def dfs(i,j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for dr,dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                r,c = i+dr, j+dc
                if 0<=r<m and 0<=c<n and grid[r][c]=="1" and (r,c) not in visited:
                    dfs(r,c)
            return
        
        islands = 0
        for row in range(m):
            for col in range(n):
                if (row,col) not in visited and grid[row][col]=="1":
                    islands+=1
                    dfs(row,col)
        return islands