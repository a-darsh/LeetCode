class Solution:
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
      
      #top up
      
      if (m,n) in memo:
        return memo[(m,n)]
      
      if m==1 and n==1:
        memo[(1,1)] = 1
        return 1
      
      if m==0 or n ==0:
        return 0
      
      memo[(m,n)] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)
      return memo[(m,n)]
      
      
  
#         #bottom up
#         row = [1]*(m)
        
#         newRow = [0]*(m)
        
#         for i in range(n-2, -1, -1):
#           for j in range(m-1,-1,-1 ):
#             if j+1 <= m-1: 
#               newRow[j] = (row[j]+newRow[j+1])
#             else:
#               newRow[j] = (row[j])
              
          
#           row = newRow
          
#         return row[0]