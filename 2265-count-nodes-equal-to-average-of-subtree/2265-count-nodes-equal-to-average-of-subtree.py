# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        self.ans = 0
        
        def dfs(node):
            
            if not node:
                return (0,0) #count, sum
            
            left = dfs(node.left)
            right = dfs(node.right)
            totalSum = node.val + left[1] + right[1] 
            totalCount = left[0] + right[0] + 1
            
            if node.val==(totalSum//totalCount):
                self.ans+=1
            
            return (totalCount, totalSum)
            
        
        dfs(root)
        
        return self.ans