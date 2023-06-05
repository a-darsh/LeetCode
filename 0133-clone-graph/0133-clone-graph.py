"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        hmap = {}
        
        def dfs(node):
          
          if node in hmap:
            return hmap[node]
          
          copy = Node(node.val)
          hmap[node] = copy
          
          for n in node.neighbors:
            temp = dfs(n)
            copy.neighbors.append(temp)
            
          return copy
        
        return dfs(node) if node else None
          
            