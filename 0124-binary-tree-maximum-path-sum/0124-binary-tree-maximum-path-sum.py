# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = root.val
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            lmax = max(0, dfs(root.left))
            rmax = max(0, dfs(root.right))
            ans = max(ans, root.val+lmax+rmax)
            return max(root.val+lmax, root.val+rmax)
        dfs(root)
        return ans
            
        