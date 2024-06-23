# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        
        def dfs(root, target, path=[]):
            if not root:
                return path
            if root.val==target and not root.left and not root.right:
                res.append(path+[root.val])
                return
            dfs(root.left, target-root.val, path+[root.val])
            dfs(root.right, target-root.val, path+[root.val])
        
        dfs(root, targetSum)
        return res
        
        