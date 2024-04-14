# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def search(node, ans):
            if not node:
                return ans
            ans = max(ans, search(node.left, ans+1), search(node.right, ans+1))
            return ans
        return search(root, 0)