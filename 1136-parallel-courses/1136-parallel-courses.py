class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        graph = {i: [] for i in range(1, n + 1)}
        for start_node, end_node in relations:
            graph[start_node].append(end_node)
        
        visited = {} #stores maximum depth for a particular course(minimum time/sem taken to complete it)
        def dfs(cur_node):
            if cur_node in visited:
                return visited[cur_node]
            
            visited[cur_node] = -1
            maxlen = 1
            for neigh in graph[cur_node]:
                length = dfs(neigh)
                if length==-1:
                    return -1
                maxlen = max(length+1, maxlen)
            visited[cur_node] = maxlen
            return visited[cur_node]
        
        maxlen = -1
        for node in graph:
            length = dfs(node)
            if length==-1:
                return -1
            maxlen = max(maxlen, length)
        
        return maxlen
                
        
        
                
                
        