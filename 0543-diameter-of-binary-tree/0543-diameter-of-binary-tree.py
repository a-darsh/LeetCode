# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0

        def dfsHeight(node):
            nonlocal maxD
            if not node:
                return 0
            
            leftH = dfsHeight(node.left)
            rightH = dfsHeight(node.right)
            d = leftH + rightH
            maxD = max(maxD, d)

            return 1 + max(leftH, rightH)
        
        dfsHeight(root)
        return maxD
