# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def checkPath(node, target, temp):
            if not node:
                return 
            target -= node.val
            if not node.left and not node.right and target==0:
                ans.append(temp+[node.val])
            checkPath(node.left, target, temp+[node.val])
            checkPath(node.right, target, temp+[node.val])
            return 
        
        checkPath(root, targetSum, [])
        
        return ans
        