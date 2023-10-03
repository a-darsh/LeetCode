class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      
      if not grid:
        return 0
      
      row, col = len(grid), len(grid[0])
      visited = set()
      count = 0
      
      def bfs(r,c):
        queue = collections.deque()
        queue.append((r,c))
        while queue:
            cr, cc = queue.popleft()
            for ir, ic in [[+1,0], [-1,0], [0,+1], [0, -1]]:
              rn, cn = cr+ir, cc + ic
              if (rn in range(0, row)) and (cn in range(0, col)) and (grid[rn][cn] == "1") and ((rn,cn) not in visited):
                queue.append((rn, cn))
                visited.add((rn,cn))
                
                
      
      for r in range(row):
        for c in range(col):
          if (r,c) not in visited and grid[r][c] == "1":
            bfs(r,c)
            visited.add((r,c))
            count += 1
            
      return count
            
      