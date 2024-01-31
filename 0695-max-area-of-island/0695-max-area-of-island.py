class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rmax, cmax = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        
        for i in range(rmax):
            for j in range(cmax):
                if (i,j) not in visited and grid[i][j]==1:
                    visited.add((i,j))
                    area = self.explore(grid, i,j,rmax,cmax, visited)
                    if area > maxArea:
                        maxArea = area
        return maxArea
        
        
        
    def explore(self, grid, i,j, rmax, cmax, visited):
        posList = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        area = 1
        for pos in posList:
            if self.check(pos[0], pos[1], rmax, cmax) and pos not in visited and grid[pos[0]][pos[1]]==1:
                visited.add(pos)
                area += self.explore(grid, pos[0], pos[1], rmax, cmax, visited)
        
        return area
                
        
    def check(self, r,c,rmax,cmax):
        if r>=0 and r<rmax and c>=0 and c<cmax:
            return True
        else:
            return False
        
        