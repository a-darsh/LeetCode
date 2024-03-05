class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(numCourses)}
        
        for i,j in prerequisites:
            graph[i].append(j)
        
        
        def dfs(course, visited = set()):
            if not graph[course]:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for neigh in graph[course]:
                if not dfs(neigh):
                    return False
            
            graph[course] = []
            return True
            
        
        for course in graph:
            if not dfs(course):
                return False
            
        return True

# #         5
# [[1,4],[2,4],[3,1],[3,2]]
# 0: 
# 1: 4
# 2: 4
# 3: 1, 2
# 4: 

    
    
    
        