class LinkNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = LinkNode(-1,-1)
        self.tail = LinkNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
    
    def add(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        
        return node.value
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.value = value
            self.cache[key] = node
            self.add(node)
        
        elif self.size<self.capacity:
            node = LinkNode(key, value)
            self.cache[key] = node
            self.add(node)
            self.size+=1
        
        else:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
            node = LinkNode(key, value)
            self.cache[key] = node
            self.add(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)