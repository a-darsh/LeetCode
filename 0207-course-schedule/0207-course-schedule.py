class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        for i in range(numCourses):
            graph[i]=[]
        for preq in prerequisites:
            graph[preq[0]].append(preq[1])
        
        visited = set()
        def dfs(i):
            if graph[i]==[]:
                return True
            if i in visited:
                return False
            visited.add(i)
            for neigh in graph[i]:
                if not dfs(neigh):
                    return False
            visited.remove(i)
            graph[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        