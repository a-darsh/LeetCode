# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        val = True
        
        def dfs(root):
          nonlocal val
          if not root:
            return 0
          
          leftH = dfs(root.left)
          rightH = dfs(root.right)
          
          val = val and (abs(leftH - rightH) <= 1)
          
          return max(leftH, rightH) + 1
        
        dfs(root)
        
        return val