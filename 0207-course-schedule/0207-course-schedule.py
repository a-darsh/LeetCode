class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preq = {i:[] for i in range(numCourses)}
        
        for l in prerequisites:
          preq[l[0]].append(l[1])
          
        visited  = set()
        
        def dfs(c):
          
          if c in visited:
            return False
          
          if preq[c] == [] :
            return True
          
          visited.add(c)
          for i in preq[c]:
            if not dfs(i): return False
            
          visited.remove(c)
          preq[c] = []
          
          return True
        
        
        
        for i in range(numCourses):
          
          if not dfs(i): 
            return False
          
        return True
            
            
          
        