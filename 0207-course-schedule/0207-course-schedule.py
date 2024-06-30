class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for c1,c2 in prerequisites:
            graph[c1].append(c2)
        
        visited = set()
        def dfs(c):
            if c in visited:
                return False
            if not graph[c]:
                return True
            visited.add(c)
            for neigh in graph[c]:
                if not dfs(neigh):
                    return False
            visited.remove(c)
            graph[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True