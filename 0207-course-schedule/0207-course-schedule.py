class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
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
            graph[course]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True