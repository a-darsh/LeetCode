# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def ifPath(node, target):
            if not node:
                return False
            target -= node.val
            if not node.left and not node.right and target==0:
                return True
            return ifPath(node.left, target) or ifPath(node.right, target)
        
        return ifPath(root, targetSum)
        