"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        copyList = {}
        
        cur = head
        while(cur):
            copy = Node(cur.val)
            copyList[cur] = copy
            cur = cur.next
        
        cur = head
        while(cur):
            copy = copyList[cur]
            copy.next = copyList.get(cur.next)
            copy.random = copyList.get(cur.random)
            cur = cur.next
        
        return copyList[head]
            
        