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
        copy_dict = {}
        copy_dict[head] = Node(head.val)
        cur = head
        while cur:
            if cur.next and cur.next not in copy_dict:
                copy_dict[cur.next] = Node(cur.next.val)
            copy_dict[cur].next = copy_dict.get(cur.next, None)

            if cur.random and cur.random not in copy_dict:
                copy_dict[cur.random] = Node(cur.random.val)
            copy_dict[cur].random = copy_dict.get(cur.random, None)

            cur = cur.next
        
        return copy_dict[head]

        #O(N), O(N)