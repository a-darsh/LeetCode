class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        preq = {i:[] for i in range(numCourses)}
        
        for l in prerequisites:
          preq[l[0]].append(l[1])
          
        courseOrder = []
        
        if not prerequisites:
          courseOrder = [i for i in range(numCourses)]
        
        visited = set()
        
        def dfs(c):
          
          if c in visited:
            return False
          
          if preq[c] == []:
            if c not in courseOrder:
              courseOrder.append(c)
            return True
          
          visited.add(c)
          for i in preq[c]:
            if not dfs(i): return False
            
          visited.remove(c)
          preq[c] = []
          if c not in courseOrder:
            courseOrder.append(c)
          return True
                 
        for i in range(numCourses):
          if not dfs(i) : return []
          
        return courseOrder