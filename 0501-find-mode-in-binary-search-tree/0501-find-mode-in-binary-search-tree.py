# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        hmap = defaultdict(int)
        def inorder(node):
            if not node:
                return
            hmap[node.val]+=1
            inorder(node.left)
            inorder(node.right)
            
        inorder(root)
        
        maxVal = float('-inf')
        ans = []
        for k,v in hmap.items():
            if v==maxVal:
                ans.append(k)
            elif v>maxVal:
                ans = [k]
                maxVal = v
        
        return ans
        