class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            graph[i].append(j)
            
        
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if not graph[crs]:
                return True
            
            cycle.add(crs)
            for neigh in graph[crs]:
                if not dfs(neigh):
                    return False
            cycle.remove(crs)
            graph[crs] = []
            return True
        
        for crs in graph:
            if not dfs(crs):
                return False
        
        return True