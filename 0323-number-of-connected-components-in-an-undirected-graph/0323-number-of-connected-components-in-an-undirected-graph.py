class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {}
        
        for i, j in edges:
            
            if i not in graph: graph[i] = []
            if j not in graph: graph[j] = []
            
            graph[i].append(j)
            graph[j].append(i)
        
        
        
        visited = set()
        
        #checking for single nodes, not present in edges
        if len(graph)!=n:
            count = n-len(graph)
        else:
            count = 0
        
        for node in graph:
            if node not in visited:
                count += 1
                visited.add(node)
                self.explore(graph, node, visited)
        
        return count
        
    def explore(self, graph, node, visited):

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                self.explore(graph, nei, visited)

                    
                                    
        