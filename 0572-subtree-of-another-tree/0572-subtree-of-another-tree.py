# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def sameTree(p,q):
          
          if (p and not q) or (not p and q):
            return False
          
          if not p and not q:
            return True
          
          if p.val != q.val:
            return False
          
          return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        if not root and not subRoot:
          return True
        
        if not root:
          return False
        
        if sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
          return True
        
        return False
          
          
        