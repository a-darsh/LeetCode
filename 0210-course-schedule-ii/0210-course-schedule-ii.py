class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            graph[i].append(j)
        
        ans = []
        visit, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for neigh in graph[course]:
                if not dfs(neigh):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            ans.append(course)
            return True
        
        for course in graph:
            if not dfs(course):
                return []
        
        return ans
        