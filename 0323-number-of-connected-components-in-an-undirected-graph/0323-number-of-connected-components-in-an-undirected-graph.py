class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        comp  = 0
        graph = defaultdict(list)
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for nei in graph[node]:
                    dfs(nei)
            return
        
        for node in range(n):
            if node not in visited:
                comp+=1
                dfs(node)
        
        return comp
        
                