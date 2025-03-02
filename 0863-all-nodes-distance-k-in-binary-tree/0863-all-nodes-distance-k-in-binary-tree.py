# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k==0:
            return [target.val]
        
        q=deque([root])
        adjList = defaultdict(list)
        while q:
            node = q.popleft()
            if node.left:
                adjList[node].append(node.left)
                adjList[node.left].append(node)
                q.append(node.left)
            if node.right:
                adjList[node].append(node.right)
                adjList[node.right].append(node)
                q.append(node.right)
        
        res = []
        q = deque([(target, 0)])
        seen = set([target])
        while q:
            node, dist = q.popleft()
            if dist==k:
                res.append(node.val)
            elif dist<k:
                for neigh in adjList[node]:
                    if neigh not in seen:
                        q.append((neigh, dist+1))
                        seen.add(neigh)
        
        return res