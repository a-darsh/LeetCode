class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(numCourses)}
        
        for i,j in prerequisites:
            graph[i].append(j)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not graph[course]:
                return True
            
            visited.add(course)
            for neigh in graph[course]:
                if not dfs(neigh):
                    return False
            
            visited.remove(course)
            graph[course] = []
            return True
            
        
        for course in graph:
            if not dfs(course):
                return False
            
        return True
    
        