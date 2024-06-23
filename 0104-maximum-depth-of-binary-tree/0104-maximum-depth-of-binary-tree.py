# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        maxD = 0
        
        def dfs(root, depth=0):
            nonlocal maxD
            if not root:
                return
            if not root.left and not root.right:
                maxD = max(depth+1, maxD)
                return
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        dfs(root)
        return maxD