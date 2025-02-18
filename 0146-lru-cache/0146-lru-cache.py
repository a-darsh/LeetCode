class LinkedList:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = LinkedList(-1,-1)
        self.tail = LinkedList(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lru = {}
    
    def add(self, node):
        prevLast = self.tail.prev
        prevLast.next = node
        node.prev = prevLast
        node.next = self.tail
        self.tail.prev = node
        self.lru[node.key] = node
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        del self.lru[node.key]
    
    def removeFirst(self):
        self.remove(self.head.next)

    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            self.remove(node)
            node.val = value
            self.add(node)
            self.lru[key] = node
        else:
            node = LinkedList(key, value)
            if len(self.lru)==self.cap:
                self.removeFirst()
            self.add(node)
            self.lru[key] = node

                        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)