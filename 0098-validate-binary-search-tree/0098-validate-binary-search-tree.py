# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lbound = float("-inf"), rbound = float("inf")):
            if not root:
                return True
            if root.val<=lbound or root.val>=rbound:
                return False
            if not dfs(root.left, lbound, root.val) or not dfs(root.right, root.val, rbound):
                return False
            return True
        
        return dfs(root)
    
            
        