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
            leftsum = max(dfs(root.left),0)
            rightsum = max(dfs(root.right),0)
            ans = max(ans, root.val + leftsum + rightsum)
            return root.val + max(leftsum, rightsum)
        
        dfs(root)
        return ans
            
        