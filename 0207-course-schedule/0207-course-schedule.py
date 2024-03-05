class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(numCourses)}
        
        for i,j in prerequisites:
            graph[i].append(j)
        
        
        def dfs(course, visited):
            print(course, visited)
            
            if course in visited:
                return False
            
            if not graph[course]:
                return True
            
            for neigh in graph[course]:
                if not dfs(neigh, set(list(visited) + [course]) ):
                    return False
            
            graph[course] = []
            return True
            
        
        for course in graph:
            if not dfs(course, set()):
                return False
            
        return True

# #         5
# [[1,4],[2,4],[3,1],[3,2]]
# 0: 
# 1: 4
# 2: 4
# 3: 1, 2
# 4: 

    
    
    
        