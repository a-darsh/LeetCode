class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preq = { i: [] for i in range(numCourses)}
        
        for l in prerequisites:
          preq[l[0]].append(l[1])
        
        
        visited = set()
        
        def dfs(c):
          
          #loop check
          if c in visited:
            return False
          
          #no prereq
          if not preq[c]:
            return True
          
          visited.add(c)
          
          for n in preq[c]:
            
            if not dfs(n):
              return False
            
          visited.remove(c)
          preq[c] = []
          
          return True
        
        for c in preq:
          if not dfs(c):
            return False
          
        return True
            
            
          
        