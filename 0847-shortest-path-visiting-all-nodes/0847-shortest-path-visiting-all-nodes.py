class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        N  = len(graph)
        
        allVisited = (1<<N) -1
        
        visited = set()
        queue = deque()
        
        for i in range(N):
            queue.append((i, 1<<i, 0))
            visited.add((i, 1<<i))
        
        while(queue):
            node, visited_nodes, path = queue.popleft()
            
            if visited_nodes==allVisited:
                return path
            
            for neigh in graph[node]:
                next_visit = visited_nodes | (1<<neigh)
                if (neigh, next_visit) not in visited:
                    queue.append((neigh, next_visit, path+1))
                    visited.add((neigh, next_visit))
            
        return -1
            