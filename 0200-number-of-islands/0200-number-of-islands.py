class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n  = len(grid), len(grid[0])
        visited = set()
        res = 0
        def dfs(i,j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for x,y in [[1,0], [-1,0], [0,1], [0,-1]]:
                r,c = i+x, j+y
                if 0<=r<m and 0<=c<n and grid[r][c]=="1":
                    dfs(r,c)
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]=="1":
                    res+=1
                    dfs(i,j)
        return res
                    