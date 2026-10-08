class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def insert(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def refresh(self, node):
        self.remove(node)
        self.insert(node)

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.refresh(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.refresh(node)
        else:
            self.map[key] = Node(key, value)
            self.insert(self.map[key])
            if len(self.map) > self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.map[lru.key]
