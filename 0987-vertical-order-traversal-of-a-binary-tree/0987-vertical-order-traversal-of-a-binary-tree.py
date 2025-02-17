# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(0,0,root)])
        hmap = defaultdict(list)
        while queue:
            r,c, node = queue.popleft()
            hmap[c].append((r, node.val))
            if node.left:
                queue.append((r+1, c-1, node.left))
            if node.right:
                queue.append((r+1, c+1, node.right))
        res = []
        for key in sorted(hmap.keys()):
            temp = []
            for _, val in sorted(hmap[key]):
                temp.append(val)
            res.append(temp)
        return res