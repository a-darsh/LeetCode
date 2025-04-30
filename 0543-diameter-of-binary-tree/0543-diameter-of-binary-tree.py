# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0
        def height(node):
            nonlocal maxDiam
            if not node:
                return 0
            leftH = height(node.left)
            rightH = height(node.right)
            maxDiam = max(maxDiam, leftH+rightH)
            return max(leftH,rightH)+1
        height(root)
        return maxDiam

    #O(N), O(N)