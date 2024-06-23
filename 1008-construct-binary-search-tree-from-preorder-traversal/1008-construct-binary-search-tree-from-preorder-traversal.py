# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        inorder = sorted(preorder)
        
        def construct(preorder, inorder):
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = construct(preorder[1:mid+1], inorder[:mid])
            root.right = construct(preorder[mid+1:], inorder[mid+1:])
            return root
        
        return construct(preorder, inorder)
        