# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        forest = []
        
        def dfs(node, isRoot):
            if not node:
                return
            
            deleted = node.val in to_delete
            
            if isRoot and not deleted:
                forest.append(node)
            
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)
            
            return None if deleted else node
                
        dfs(root, True)
        return forest
            
        