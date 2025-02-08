class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, node):
        lastNode = self.tail.prev
        lastNode.next  = node
        node.prev = lastNode
        node.next = self.tail
        self.tail.prev = node
        self.cache[node.key] = node
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = node.next
        nextNode.prev = prevNode
        del self.cache[node.key]
    
    def removeLru(self):
        lru = self.head.next
        self.remove(lru)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.add(node)

        else:
            if len(self.cache)>=self.cap:
                self.removeLru()
            node = ListNode(key, value)
            self.add(node)

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)