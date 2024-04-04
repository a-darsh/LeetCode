class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for i, j in prerequisites:
            graph[i].append(j)
        
        visited = set()
        def dfs(course):
            if not graph[course]:
                return True
            if course in visited:
                return False
            visited.add(course)
            for neigh in graph[course]:
                if not dfs(neigh):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
        