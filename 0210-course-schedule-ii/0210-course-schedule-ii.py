class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            graph[i].append(j)
        
        visit, cycle = set(), set()
        ans = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for neigh in graph[crs]:
                if not dfs(neigh):
                    return False
            cycle.remove(crs)
            
            ans.append(crs)
            visit.add(crs)
            return True
        
        
        for crs in graph:
            if not dfs(crs):
                return []
        
        return ans