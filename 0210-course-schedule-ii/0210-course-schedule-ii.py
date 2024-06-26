class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph  = defaultdict(list)
        for i,j in prerequisites:
            graph[i].append(j)
        
        visited = set()
        cycle = set()
        res = []
        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            cycle.add(c)
            for neigh in graph[c]:
                if not dfs(neigh) and neigh not in visited:
                    return False
            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res