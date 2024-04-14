# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        
        def inorder(node, curPath):
            if not node:
                return
            if not node.left and not node.right:
                curPath.append(str(node.val))
                ans.append("->".join(curPath))
                return
            inorder(node.left, curPath+[str(node.val)])
            inorder(node.right, curPath+[str(node.val)])
        
        inorder(root, [])
        
        return ans