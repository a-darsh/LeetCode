class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for i,j in prerequisites:
            graph[i].append(j)
            
        visit, cycle = set(), set()
        res = []
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            cycle.add(c)
            for neig in graph[c]:
                if not dfs(neig):
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res