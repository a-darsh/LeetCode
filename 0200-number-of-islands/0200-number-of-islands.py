class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rmax, cmax = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        for i in range(rmax):
            for j in range(cmax):
                if grid[i][j] == '1' and (i,j) not in visited:
                    visited.add((i,j))
                    count += 1
                    self.explore(grid, i,j, rmax, cmax, visited)
                    
        return count
                    
    def explore(self, grid, i, j, rmax, cmax, visited):
        pos = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        
        for p in pos:
            if self.check(p[0], p[1], rmax, cmax) and p not in visited and grid[p[0]][p[1]]=='1':
                visited.add(p)
                self.explore(grid, p[0], p[1], rmax, cmax, visited)
        
    
    def check(self, r, c, rmax, cmax):
        if r>=0 and r<rmax and c>=0 and c<cmax:
            return True
        else:
            return False
        