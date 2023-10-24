class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        r, c = len(grid), len(grid[0])
        
        row = [float("inf")]*c
        row[c-1] = 0
        
        print(row)
        newRow = [0]*c
        for i in range(r-1, -1, -1):
          for j in range(c-1, -1, -1):
            
            if j+1 <= c-1:
              newRow[j] = grid[i][j] + min(newRow[j+1], row[j])
              
            else:
              newRow[j] = grid[i][j] + row[j]
          
          print(newRow)
          row = newRow
          
        
        return row[0]
                
                
              
        
          