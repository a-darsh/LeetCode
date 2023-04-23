# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
          return False
        
        if not subRoot:
          return False
        
        if self.sameTree(root, subRoot):
          return True
        
        leftR = self.isSubtree(root.left, subRoot)
        rightR = self.isSubtree(root.right, subRoot)
        
        return leftR or rightR
      
    def sameTree(self, p,q):
          
        if p and not q:
          return False

        if not p and q:
          return False

        if not p and not q:
          return True

        if p.val != q.val:
          return False

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        
        