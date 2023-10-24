class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
  
        row = [1]*(m)
        
        newRow = [0]*(m)
        
        for i in range(n-2, -1, -1):
          for j in range(m-1,-1,-1 ):
            if j+1 <= m-1: 
              newRow[j] = (row[j]+newRow[j+1])
            else:
              newRow[j] = (row[j])
              
          
          row = newRow
          
        return row[0]