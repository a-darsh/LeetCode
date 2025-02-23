"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        cur = head
        while cur.next!=head:
            if cur.val<=insertVal<=cur.next.val:
                node=Node(insertVal, cur.next)
                cur.next = node
                return head
            elif cur.val>cur.next.val:
                if insertVal>=cur.val or insertVal<=cur.next.val:
                    node = Node(insertVal, cur.next)
                    cur.next = node
                    return head
            cur = cur.next

        node = Node(insertVal, cur.next)
        cur.next = node
        return head

    #O(N), O(1)
