class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def inRange(b1, b2):
            d = (b1[0]-b2[0])**2+(b1[1]-b2[1])**2
            if d>b1[2]**2:
                return False
            return True
        
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i!=j and inRange(bombs[i], bombs[j]):
                    graph[i].append(j)
        
    
        def dfs(i, visited):
            if i in visited:
                return 0
            visited.add(i)
            count = 1
            for neigh in graph[i]:
                count += dfs(neigh, visited)
            return count
        
        maxCount = float('-inf')
        for i in range(len(bombs)):
            visited = set()
            maxCount = max(maxCount, dfs(i, visited))
        # for i in graph.keys():
        #     visited = set()
        #     maxCount = max(maxCount, dfs(i, visited))
            
        return maxCount
            