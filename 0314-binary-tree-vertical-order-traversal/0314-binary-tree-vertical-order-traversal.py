# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        hmap = defaultdict(list)
        q = deque([(root,0)])
        while q:
            node, col = q.popleft()
            hmap[col].append(node.val)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
        return [hmap[k] for k in sorted(hmap.keys())]
    
    #O(N), O(N)