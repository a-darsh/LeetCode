# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(lnode, rnode):
            if not lnode and not rnode:
                return True
            if not lnode or not rnode:
                return False
            if lnode.val!=rnode.val:
                return False
            lcheck = dfs(lnode.right, rnode.left)
            rcheck = dfs(lnode.left, rnode.right)
            if not lcheck or not rcheck:
                return False
            return True
        return dfs(root.left, root.right)
            
        