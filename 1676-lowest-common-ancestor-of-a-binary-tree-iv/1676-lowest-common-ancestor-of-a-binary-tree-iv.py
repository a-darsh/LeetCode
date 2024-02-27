# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        nodes = set(nodes)
        
        def dfs(node, nodes):
            if not node:
                return None
            
            if node in nodes:
                return node
            
            l = dfs(node.left, nodes)
            r = dfs(node.right, nodes)
            
            if l and r:
                return node
            
            return l if l else r
        
        return dfs(root, nodes)