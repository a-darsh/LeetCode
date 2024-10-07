class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for c1, c2 in prerequisites:
            graph[c1].append(c2)
        
        visited = [0]*numCourses
        ans = []
        def dfs(course):
            if visited[course]==1:
                return False
            if visited[course]==2:
                return True
            visited[course]=1
            for neigh in graph[course]:
                if not dfs(neigh):
                    return False
            visited[course]=2
            ans.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return ans