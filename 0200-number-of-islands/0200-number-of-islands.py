class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      
      if not grid:
        return 0
      
      r, c = len(grid), len(grid[0])
      
      num = 0
      
      visit = set()
      
      def dfs(row,col):
        
        #bounds
        row_check = 0 <= row < r
        col_check = 0 <= col < c
        
        if( not row_check or not col_check):
          return False
        
        if(grid[row][col] == '0'):
          return False
        
        if (row,col) not in visit:
          visit.add((row,col))
          dfs(row-1,col)
          dfs(row+1, col)
          dfs(row, col-1)
          dfs(row, col+1)
          
      
      for i in range(r):
        for j in range(c):
          
          if ((i,j) not in visit) and (grid[i][j] == '1'):
            dfs(i,j)
            num += 1
      
      return num
        