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
        queue = deque([(0,root)])
        minX, maxX = float('inf'), float('-inf')
        while queue:
            x,node = queue.popleft()
            minX = min(minX, x)
            maxX = max(maxX, x)
            hmap[x].append(node.val)
            if node.left:
                queue.append((x-1, node.left))
            if node.right:
                queue.append((x+1,node.right))
        return [hmap[x] for x in range(minX, maxX+1)]


        
