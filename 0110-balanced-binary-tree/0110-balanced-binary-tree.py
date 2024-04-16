# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, height):
            if not node:
                return (True, 0)
            lc,lh = dfs(node.left, height+1)
            rc,rh = dfs(node.right, height+1)
            if lc and rc and abs(lh-rh)<=1:
                return (True, 1+max(lh,rh))
            else:
                return (False, 1+max(lh,rh))
        
        return dfs(root, 0)[0]
            
            