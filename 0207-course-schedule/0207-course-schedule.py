class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for c1, c2 in prerequisites:
            graph[c1].append(c2)
        
        visited = set()
        def dfs(course):
            if not graph[course]:
                return True
            if course in visited:
                return False
            visited.add(course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True