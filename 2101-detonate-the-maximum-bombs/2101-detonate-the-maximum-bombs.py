class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def checkInside(b1,b2):
            d = (b1[0]-b2[0])**2+(b1[1]-b2[1])**2
            if d>b1[2]**2:
                return False
            return True
        
        graph = defaultdict(list)
        for i, b1 in enumerate(bombs):
            for j, b2 in enumerate(bombs):
                if checkInside(b1,b2) and i!=j:
                    graph[i].append(j)
        
        maxCount = float('-inf')
        def dfs(i, visited):
            if i in visited:
                return 0
            count=1
            visited.add(i)
            for neigh in graph[i]:
                count+=dfs(neigh,visited)
            return count
        
        for i,_ in enumerate(bombs):
            visited = set()
            maxCount = max(maxCount, dfs(i, visited))
            
        return maxCount