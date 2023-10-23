class Solution:
    def climbStairs(self, n: int) -> int:
      
      wayList = []
      k = 0 
      for i in range(n,-1,-1):
        
        if i == n or i==n-1:
          wayList.append(1)
          k += 1
        
        else:
          wayList.append(wayList[k-1]+wayList[k-2])
          k += 1
          
      
      return wayList[k-1]
          
        
        
        
        
        
        