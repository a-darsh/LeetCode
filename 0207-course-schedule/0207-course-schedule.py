class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(numCourses)}
        
        for i,j in prerequisites:
            graph[i].append(j)
        
        def dfs(course, visited = set()):
            if course in visited:
                return False
            if not graph[course]:
                return True
            
            visited.add(course)
            for neigh in graph[course]:
                if not dfs(neigh, visited):
                    return False
            
            visited.remove(course)
            graph[course] = []
            return True
            
        
        for course in graph:
            if not dfs(course):
                return False
            
        return True
    
        