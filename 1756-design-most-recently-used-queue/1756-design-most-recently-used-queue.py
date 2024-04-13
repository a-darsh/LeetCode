class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MRUQueue:

    def __init__(self, n: int):
        self.head = LinkNode(-1)
        self.tail = LinkNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.create(n)
        
    def add(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def create(self, n):
        for i in range(1,n+1):
            self.add(LinkNode(i))

    def fetch(self, k: int) -> int:
        temp = self.head
        while k:
            temp = temp.next
            k-=1
        self.remove(temp)
        self.add(temp)
        return temp.value
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)